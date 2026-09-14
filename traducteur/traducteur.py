#!/usr/bin/env python3
"""Traducteur langage naturel (français) → IR.

C'est l'axe B de `../PLANNING.md`. Le module ne produit **jamais** de commande
Eos : il produit une IR, que `grammar/generateur.py` transforme ensuite en
commande. La syntaxe reste la propriété exclusive du modèle.

    >>> t = Traducteur()
    >>> t.traduire("circuits 10 a 20 en lee 195").ir
    [{'selection': {'objet': 'Chan', 'de': 10, 'a': 20}, 'action': {...}}]

TROIS ISSUES, PAS DEUX. C'est le choix de conception central :

  compris      → une IR, prête à rendre
  a_preciser   → une ou plusieurs questions à poser à l'utilisateur
  incompris    → rien, et la liste des mots non reconnus

« a_preciser » n'est pas un échec dégradé, c'est le comportement correct face à
une ambiguïté que seul l'utilisateur peut lever. Sans cette issue, un traducteur
n'a d'autre choix que de deviner — et une couleur devinée produit une macro
valide, acceptée par la console, et la mauvaise teinte sur scène. C'est le pire
des trois échecs possibles parce qu'il est silencieux. Voir `APP.md`.

AUCUNE IA À L'EXÉCUTION, et c'est délibéré :

  1. Dans le théâtre, le téléphone est sur le Wi-Fi de la console. Rien ne
     garantit un accès Internet. Un traducteur qui dépend d'un serveur distant
     tombe exactement quand on en a besoin.
  2. La règle n°1 du dépôt est « n'invente rien ». Un modèle de langue invente
     par construction : il peut produire une syntaxe plausible et inexistante.
     Un lexique ne peut sortir que ce qu'on y a mis.
  3. C'est réversible. L'IR est le contrat : un jour, une couche de
     compréhension plus souple peut se brancher devant et émettre la même IR
     sans que rien en aval ne bouge.
"""
from __future__ import annotations

import copy
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

RACINE = Path(__file__).parent
GRAMMAIRE = RACINE.parent / "grammar"
if str(GRAMMAIRE) not in sys.path:
    sys.path.insert(0, str(GRAMMAIRE))


# --------------------------------------------------------------------------
# Résultats
# --------------------------------------------------------------------------
@dataclass
class Option:
    cle: str
    libelle: str
    detail: str = ""
    demande_valeur: bool = False


@dataclass
class Question:
    id: str                        # clé stable, à réutiliser dans `reponses`
    texte: str
    pourquoi: str
    options: list[Option] = field(default_factory=list)
    contexte: dict = field(default_factory=dict)


@dataclass
class Hypothese:
    """Une valeur retenue SANS marqueur explicite dans la phrase — le
    traducteur a tranché à la place de l'utilisateur plutôt que de bloquer.

    Ce n'est ni un `compris` plein (rien à confirmer) ni un `a_preciser`
    (qui bloque tant que la question n'est pas répondue) : la traduction
    part quand même, mais ce champ précis reste marqué comme une supposition
    — code couleur orange côté UI — avec de quoi la corriger d'un geste
    plutôt que de retaper toute la phrase. Décidé avec l'utilisateur en
    session le 2026-08-07.
    """
    champ: str                     # ex. "nuancier"
    valeur: str                    # ce qui a été retenu, ex. "Lee"
    pourquoi: str
    correction: Question           # rejouable via `reponses[correction.id]`


@dataclass
class Traduction:
    statut: str                    # compris | a_preciser | incompris
    ir: list[dict] = field(default_factory=list)
    questions: list[Question] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    non_reconnus: list[str] = field(default_factory=list)
    # Mots du lexique présents dans la phrase mais restés inutilisés. Distinct
    # de `non_reconnus` (mots inconnus) : ici l'app savait ce que le mot veut
    # dire et ne s'en est pas servie. À afficher sur tous les statuts, `compris`
    # compris — voir `Traducteur._ignores`.
    ignores: list[str] = field(default_factory=list)
    intention: str | None = None
    hypotheses: list[Hypothese] = field(default_factory=list)

    @property
    def compris(self) -> bool:
        return self.statut == "compris"


# --------------------------------------------------------------------------
# Normalisation
# --------------------------------------------------------------------------
def normaliser(texte: str, ponctuation: str) -> str:
    """Minuscules, accents retirés, ponctuation neutralisée.

    Retirer les accents n'est pas cosmétique : l'utilisateur écrit « 1 a 6 »
    aussi souvent que « 1 à 6 ». Sans cela, la moitié des plages échouent.
    """
    texte = texte.lower()
    texte = unicodedata.normalize("NFD", texte)
    texte = "".join(c for c in texte if unicodedata.category(c) != "Mn")
    for signe in ponctuation:
        texte = texte.replace(signe, " ")
    return texte


def tokeniser(texte: str) -> list[str]:
    """Mots, nombres, `%` et `-` — le reste tombe."""
    return re.findall(r"[a-z0-9]+|%|-", texte)


def distance(a: str, b: str) -> int:
    """Distance d'édition de Levenshtein, itérative."""
    if a == b:
        return 0
    if not a or not b:
        return len(a) or len(b)
    precedente = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        courante = [i]
        for j, cb in enumerate(b, 1):
            courante.append(min(precedente[j] + 1,
                                courante[j - 1] + 1,
                                precedente[j - 1] + (ca != cb)))
        precedente = courante
    return precedente[-1]


# Marqueurs qui introduisent un niveau (`_niveau`).
MARQUEURS_NIVEAU = ("%", "pourcent", "intensite", "niveau")

# Sous-ensemble de `MARQUEURS_NIVEAU` qui ne s'emploie qu'en POSTFIXE en
# français naturel — la valeur est toujours le nombre qui les précède
# immédiatement (« 50 % », « 50 pourcent »), jamais l'inverse. `_plage` s'en
# sert pour éviter de lire ce nombre comme la borne haute d'une plage (voir
# `_plage`). « intensité »/« niveau » en sont volontairement exclus : ces deux
# mots s'emploient aussi, et même surtout, en PRÉFIXE d'un niveau qui suit
# (« intensité 50 » — la forme déjà déclarée sourcée pour lever l'ambiguïté
# du second « à », voir `_regler_intensite`) ; le nombre qui les précède dans
# ce cas est un endpoint de plage légitime, pas la valeur d'un niveau, et les
# traiter comme `%`/`pourcent` casserait cette forme déjà correcte.
MARQUEURS_NIVEAU_POSTFIXES = ("%", "pourcent")

# Unité postfixe propre à `_regler_parametre` (Pan/Tilt : degrés). Même rôle
# que `MARQUEURS_NIVEAU_POSTFIXES` pour `%` — désambiguïser « circuit 1 à 10
# degrés » (une sélection ET une valeur, pas une plage 1-10) sans toucher au
# mécanisme partagé `_plage`, qui n'a aucune raison de connaître les degrés.
MARQUEURS_UNITE_PARAMETRE = ("degres", "degre")

# Sépare une phrase en plusieurs COMMANDES séquentielles, pour bâtir une
# macro multi-lignes plutôt qu'une seule ligne. Volontairement restreint à
# « puis » et « ; » — des connecteurs qui ne servent JAMAIS à autre chose en
# français de métier. « et » est exclu à dessein : il sert déjà à l'intérieur
# d'une seule commande (« circuits 1 et 3 », listes de couleurs...) et le
# lire comme séparateur de commandes couperait des phrases simples en plein
# milieu, sans qu'aucun mot ne le signale. Élargir cette liste est le genre
# d'assouplissement que la doctrine du projet encourage (2026-09-09) — mais
# seulement un connecteur sourcé sans double-sens à la fois, jamais par lot.
SEPARATEUR_COMMANDES = re.compile(r"\bpuis\b|;", re.IGNORECASE)


# --------------------------------------------------------------------------
def charger_lexique(chemin):
    """Charge le lexique en REFUSANT les clés dupliquées.

    `yaml.safe_load` garde silencieusement la dernière valeur quand une clé
    apparaît deux fois dans le même bloc. Le 2026-09-09, un ajout de verbes a
    créé un second `declencheurs_optionnels:` sous `plein_feu` : le groupe
    d'objets du premier bloc a disparu sans erreur, sans avertissement, et le
    lexique s'est mis à refuser des phrases qu'il acceptait la veille. Une
    demi-heure de recherche pour une faute invisible à la lecture.

    C'est exactement la classe de panne que le projet combat partout ailleurs
    (règle 4 de REGLES_POUR_UI.md) : ça marche, ça ne dit rien, et c'est faux.
    Le lexique mérite le même traitement que les macros."""
    import yaml

    class SansDoublon(yaml.SafeLoader):
        pass

    def construire(loader, noeud, deep=False):
        vues = set()
        for cle_noeud, _ in noeud.value:
            cle = loader.construct_object(cle_noeud, deep=deep)
            if cle in vues:
                raise ValueError(
                    f"{chemin} ligne {cle_noeud.start_mark.line + 1} : clé "
                    f"« {cle} » dupliquée dans le même bloc. YAML garderait "
                    f"la dernière en silence et perdrait la première.")
            vues.add(cle)
        return yaml.SafeLoader.construct_mapping(loader, noeud, deep)

    SansDoublon.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construire)
    return yaml.load(chemin.read_text(encoding="utf-8"), Loader=SansDoublon)


class Traducteur:
    def __init__(self, lex: dict | None = None, generateur: object | None = None) -> None:
        """`lex` et `generateur` permettent d'injecter des données/instance
        déjà chargées plutôt que de lire `lexique.yaml` et `modele.yaml`
        depuis le disque — nécessaire dans Pyodide (voir `app/`), qui n'a pas
        de vrai système de fichiers pointant sur ce dépôt. Import de PyYAML
        local à cette branche pour la même raison que dans `generateur.py` :
        Pyodide ne l'a pas installé, et n'en a pas besoin ici."""
        if lex is not None:
            self.lex = lex
        else:
            self.lex = charger_lexique(RACINE / "lexique.yaml")
        self._generateur = generateur
        self._ponctuation = self.lex["normalisation"]["ponctuation_ignoree"]
        self._outils = set(self.lex["mots_outils"])
        self._mots_plage = set(self.lex["plage"]["mots"])
        self._objets = self._indexer(self.lex["objets"])
        self._objets_cible = self._indexer(self.lex["objets_cible"])
        self._parametres = self._indexer(self.lex["parametres"])
        self._nuanciers = self._indexer(self.lex["nuanciers"])
        self._couleurs = self._indexer(self.lex["couleurs"])
        self._cue_cibles = self._indexer(self.lex["cue_cibles"])
        self._familles = self._indexer(self.lex["familles_palette"])
        d = self.lex["durees"]
        self._marqueurs_duree = tuple(d["marqueurs"])
        self._marqueurs_duree_post = tuple(d["marqueurs_postfixes"])
        self._mots_sans = set(d["mots_sans"])
        self._mots_temps = set(d["mots_temps"])
        # Intention retenue par l'appel `traduire()` en cours — voir la note
        # de `traduire()`. Champ de travail, pas un état du traducteur : il
        # est posé puis restauré à chaque appel, et vaut None hors appel.
        self._intention_courante: str | None = None

    @staticmethod
    def _indexer(section: dict) -> dict[str, str]:
        """alias → clé canonique. La clé est elle-même un alias d'elle-même."""
        index: dict[str, str] = {}
        for cle, corps in section.items():
            index[cle] = cle
            for alias in corps.get("alias", []):
                index[alias.replace(" ", "")] = cle
        return index

    # -- résolution d'un mot, restreinte à un créneau ----------------------
    def _resoudre(self, mot: str, index: dict[str, str]) -> tuple[str | None, list[str]]:
        """Cherche `mot` dans `index`, avec tolérance aux fautes de frappe.

        La tolérance est **restreinte à cet index**, jamais globale — c'est le
        créneau en cours de remplissage qui sert de désambiguïsateur. Cas réel :
        l'utilisateur écrit « chang » pour « chaud ». Cherché dans tout le
        lexique, le plus proche voisin de « chang » est « chan » (distance 1),
        le mot-clé Eos pour un circuit — une correction globale aurait traduit
        une couleur en sélection de circuits, sans rien dire. Restreint aux
        couleurs, où « chan » n'est pas candidat, « chaud » gagne seul.

        Retourne (clé trouvée, ex-æquo). Deux candidats à égalité ne sont jamais
        départagés au hasard : la liste des ex-æquo remonte pour être posée en
        question.
        """
        if mot in index:
            return index[mot], []

        tol = self.lex["tolerance"]
        if len(mot) < tol["longueur_minimale"]:
            return None, []
        maxi = tol["distance_max_mot_long"] if len(mot) >= 5 else tol["distance_max_mot_court"]

        meilleur = maxi + 1
        trouves: list[str] = []
        for alias, cle in index.items():
            d = distance(mot, alias)
            if d > maxi:
                continue
            if d < meilleur:
                meilleur, trouves = d, [cle]
            elif d == meilleur and cle not in trouves:
                trouves.append(cle)

        if len(trouves) == 1:
            return trouves[0], []
        return None, trouves

    # -- extraction de créneaux -------------------------------------------
    @staticmethod
    def _nombres(toks: list[str], pris: set[int]) -> list[tuple[int, int]]:
        """(index, valeur) de chaque nombre encore libre."""
        return [(i, int(t)) for i, t in enumerate(toks)
                if i not in pris and t.isdigit()]

    def _plage(self, toks: list[str], pris: set[int]) -> tuple[int, int] | None:
        """`10 a 20`, `10 thru 20`, `10-20` → (10, 20). Marque les jetons pris.

        Un nombre immédiatement suivi d'un marqueur POSTFIXE de niveau
        (`MARQUEURS_NIVEAU_POSTFIXES` — `%`, `pourcent`) n'est jamais lu comme
        la borne haute d'une plage : c'est la valeur d'un niveau, et le mot de
        plage juste avant (« à », le plus souvent) joue alors le rôle d'« à
        quel niveau », pas celui de séparateur de plage. Sans cette exclusion,
        « circuit 4 à 50 % » (un seul « à » dans la phrase) se lisait comme la
        plage 4 à 50, laissant `_niveau` sans rien à trouver — bug trouvé le
        2026-08-09 en construisant `_parquer`, corrigé ici avec la suite de
        tests complète en main (voir PLANNING.md). Fonctionnait déjà quand la
        phrase porte DEUX « à » (« circuits 1 à 5 à 50 % ») : le second « à »
        n'est jamais suivi d'un marqueur immédiatement après sa borne haute,
        donc ce cas n'est pas affecté par cette exclusion — et « intensité »/
        « niveau » en sont délibérément exclus, voir `MARQUEURS_NIVEAU_POSTFIXES`."""
        for i in range(len(toks) - 2):
            if i in pris or i + 2 in pris:
                continue
            if toks[i].isdigit() and toks[i + 1] in self._mots_plage and toks[i + 2].isdigit():
                if i + 3 < len(toks) and toks[i + 3] in MARQUEURS_NIVEAU_POSTFIXES:
                    continue
                pris.update({i, i + 1, i + 2})
                return int(toks[i]), int(toks[i + 2])
        return None

    def _cibles(self, toks: list[str], pris: set[int]) -> list[int]:
        """Une plage, sinon un nombre isolé, sinon rien."""
        bornes = self._plage(toks, pris)
        if bornes:
            debut, fin = bornes
            pas = 1 if fin >= debut else -1
            return list(range(debut, fin + pas, pas))
        libres = self._nombres(toks, pris)
        if libres:
            i, valeur = libres[0]
            pris.add(i)
            return [valeur]
        return []

    # -- couleurs ----------------------------------------------------------
    def _couleurs_de(self, toks: list[str], pris: set[int],
                     questions: list[Question], notes: list[str],
                     reponses: dict | None = None) -> list[dict] | None:
        """Résout les mots de couleur restants, dans l'ordre de la phrase.

        Retourne None si une couleur est ambiguë — dans ce cas la question est
        déjà empilée, À MOINS que `reponses` ne porte déjà une réponse valide
        pour cette question précise (`couleur:<mot>`), auquel cas elle est
        consommée ici plutôt que reposée — c'est le contrat documenté par
        `traduire()` (« le même appel, relancé avec la réponse, doit reprendre
        où il s'était arrêté »). Une teinte devinée serait le pire des
        échecs : macro valide, console d'accord, mauvaise couleur sur scène.
        """
        reponses = reponses or {}
        trouvees: list[dict] = []
        for i, tok in enumerate(toks):
            if i in pris or tok.isdigit() or tok in self._outils:
                continue
            cle, exaequo = self._resoudre(tok, self._couleurs)
            if cle is None:
                if exaequo:
                    reponse = reponses.get(f"couleur:{tok}")
                    if reponse in exaequo:
                        cle = reponse
                    else:
                        questions.append(self._question_couleur(tok, exaequo))
                        return None
                else:
                    continue
            if cle not in self.lex["couleurs"]:
                # `reponse` validé contre `exaequo` mais pas une clé connue —
                # ne devrait pas arriver, mais ne jamais planter dessus.
                questions.append(self._question_couleur(tok, exaequo))
                return None
            pris.add(i)
            corps = self.lex["couleurs"][cle]
            if corps.get("ambigu"):
                reponse = reponses.get(f"couleur:{cle}")
                candidat = None
                if reponse is not None:
                    try:
                        gel_choisi = int(reponse)
                    except (TypeError, ValueError):
                        gel_choisi = None
                    candidat = next((c for c in corps["candidats"] if c["gel"] == gel_choisi), None)
                if candidat is None:
                    questions.append(self._question_couleur_ambigue(cle, corps))
                    return None
                trouvees.append({"nom": cle, "gel": candidat["gel"],
                                 "nom_lee": candidat["nom_lee"], "detaillee": False})
                continue
            detaillee = bool(corps.get("note_utilisateur"))
            trouvees.append({"nom": cle, "gel": corps["gel"],
                             "nom_lee": corps["nom_lee"], "detaillee": detaillee})
            if detaillee:
                note = " ".join(corps["note_utilisateur"].split())
                if note not in notes:
                    notes.append(note)
        return trouvees

    def _question_couleur_ambigue(self, cle: str, corps: dict) -> Question:
        modele = self.lex["questions"]["couleur_ambigue"]
        return Question(
            id=f"couleur:{cle}",
            texte=f"« {cle} » — quelle nuance exactement ?",
            pourquoi=" ".join(modele["pourquoi"].split()),
            options=[Option(cle=str(c["gel"]),
                            libelle=f"Lee {c['gel']:03d} {c['nom_lee']}",
                            detail=c.get("effet", ""))
                     for c in corps["candidats"]],
            contexte={"mot": cle},
        )

    @staticmethod
    def _question_couleur_unique(couleurs: list[dict]) -> Question:
        """Plusieurs teintes nommées pour une seule commande de couleur.

        Ce n'est pas une couleur ambiguë (`_question_couleur_ambigue`, où un
        mot a plusieurs candidats au catalogue) : ici chaque mot est résolu
        sans doute, mais la commande n'en applique qu'un."""
        return Question(
            id="couleur_unique",
            texte="Plusieurs couleurs dans la phrase — laquelle appliquer ?",
            pourquoi="Une commande de couleur ne pose qu'une teinte. En retenir "
                     "une d'office laisserait les autres de côté sans le dire, "
                     "et la macro aurait l'air complète.",
            options=[Option(cle=str(c["gel"]),
                            libelle=f"{c['nom']} — Lee {c['gel']:03d} {c['nom_lee']}")
                     for c in couleurs],
        )

    @staticmethod
    def _question_couleur(mot: str, exaequo: list[str]) -> Question:
        return Question(
            id=f"couleur:{mot}",
            texte=f"« {mot} » — plusieurs couleurs possibles, laquelle ?",
            pourquoi="Le mot n'est pas au lexique et plusieurs couleurs en sont "
                     "aussi proches l'une que l'autre. Départager au hasard "
                     "donnerait la mauvaise teinte sans le dire.",
            options=[Option(cle=c, libelle=c) for c in exaequo],
            contexte={"mot": mot},
        )

    # -- intentions --------------------------------------------------------
    @staticmethod
    def _tous_declencheurs(corps: dict) -> dict:
        """Groupes exigés ET optionnels réunis.

        Sert partout où il s'agit de savoir si un mot APPARTIENT au lexique —
        `_vocabulaire_connu`, `_ignores` — par opposition à la détection
        d'intention, seule à distinguer les deux familles. Un mot optionnel
        reste du vocabulaire connu : l'oublier ferait annoncer « circuits »
        comme mot inconnu sur une phrase où il est simplement facultatif."""
        return {**corps["declencheurs"], **corps.get("declencheurs_optionnels", {})}

    def _intention(self, toks: list[str]) -> str | None:
        """Première intention dont tous les groupes EXIGÉS sont servis.

        `declencheurs_optionnels` (2026-09-09) porte les groupes qui nomment
        la cible sans être nécessaires pour reconnaître l'intention. Un
        praticien écrit « monte à fond en 20 secondes » sur un bouton de magic
        sheet : le mot « circuits » n'y est pas, et n'a pas à y être — la
        commande vise ce qui est sélectionné. Exiger le mot d'objet rendait
        toute cette famille intraduisible (9 entrées sur 26 au banc de
        rétro-traduction du 2026-09-08).

        Ce qui protège, ce n'est PAS l'exigence du mot d'objet : c'est
        `_vise_la_selection_courante`, qui refuse toujours une phrase où
        l'objet est nommé sans numéro. Voir sa note.

        Insensible à l'ordre des mots : le français du métier est télégraphique,
        et la dictée vocale ne rendra pas une syntaxe propre. L'ordre de
        déclaration dans le lexique fait la priorité — la plus spécifique
        d'abord.
        """
        presents = set(toks)
        for nom, corps in self.lex["intentions"].items():
            if all(self._groupe_servi(mots, presents, toks)
                   for mots in corps["declencheurs"].values()):
                return nom
        return None

    def _groupe_servi(self, mots: list[str], presents: set[str], toks: list[str]) -> bool:
        """Un groupe de déclencheurs est servi par un mot littéral, ou par le
        joker `@couleurs` — n'importe quel nom de teinte du lexique.

        Le joker évite de recopier les 200 noms de couleurs dans les
        déclencheurs : « circuits 1 à 5 en rouge » doit marcher sans que
        « rouge » figure deux fois dans ce fichier.

        **Toujours en correspondance EXACTE, jamais tolérante aux fautes.**
        La détection d'intention est le routeur, pas un créneau — la tolérance
        y est trop dangereuse : « groupe » est à distance 2 de « rouge », dans
        la marge acceptée pour un mot de sa longueur. Une correction tolérante
        ici ferait basculer une phrase sur GROUPES vers l'intention COULEUR,
        une bascule d'interprétation entière plutôt qu'une simple faute de
        frappe corrigée. La tolérance reste réservée au remplissage d'un
        créneau déjà choisi, où le champ restreint des candidats la rend sûre.
        """
        if presents & set(mots):
            return True
        if "@couleurs" in mots:
            return any(t in self._couleurs for t in toks if not t.isdigit())
        return False

    # -- point d'entrée ----------------------------------------------------
    def traduire(self, phrase: str, reponses: dict | None = None) -> Traduction:
        """Traduit une phrase, éventuellement composée de plusieurs commandes
        séquentielles séparées par `SEPARATEUR_COMMANDES` (« puis », « ; »).

        `reponses` porte les questions déjà tranchées. Le même appel, relancé
        avec la réponse, doit reprendre où il s'était arrêté : c'est ce qui
        permet à l'app de poser une question puis de continuer sans redemander
        le reste.
        """
        reponses = reponses or {}
        segments = [s.strip() for s in SEPARATEUR_COMMANDES.split(phrase) if s.strip()]
        if len(segments) > 1:
            return self._traduire_composee(segments, reponses)
        return self._traduire_simple(phrase, reponses)

    def _traduire_composee(self, segments: list[str], reponses: dict) -> Traduction:
        """Traduit chaque segment indépendamment et assemble une seule IR
        multi-lignes — le contenu d'une macro, pas encore la macro elle-même
        (`Learn`/`Enter`/`Learn` restent la responsabilité de l'appelant, via
        `grammar/generateur.py:rendre_macro`).

        Règle : TOUT doit être `compris` pour composer quoi que ce soit. Une
        étape ambiguë ou incomprise fait échouer la phrase entière plutôt que
        de produire une macro à moitié traduite — même principe que « rien ne
        tombe en silence » appliqué à l'échelle de la phrase composée : mieux
        vaut nommer l'étape qui bloque que publier une macro tronquée.
        """
        ir: list[dict] = []
        notes: list[str] = []
        non_reconnus: list[str] = []
        ignores: list[str] = []
        hypotheses: list = []

        for i, segment in enumerate(segments, start=1):
            trad = self._traduire_simple(segment, reponses)

            if trad.statut == "a_preciser":
                return Traduction(
                    statut="a_preciser", questions=trad.questions,
                    notes=notes + [
                        f"Étape {i} (« {segment} ») demande une précision "
                        "avant de composer la macro."],
                )
            if trad.statut != "compris":
                raison = "; ".join(trad.notes) if trad.notes else "non comprise."
                return Traduction(
                    statut="incompris",
                    notes=notes + [f"Étape {i} (« {segment} ») : {raison}"],
                    non_reconnus=non_reconnus + trad.non_reconnus,
                    ignores=ignores + trad.ignores,
                )

            ir += trad.ir
            notes += [f"Étape {i} : {n}" for n in trad.notes]
            non_reconnus += trad.non_reconnus
            ignores += trad.ignores
            hypotheses += trad.hypotheses

        return Traduction(statut="compris", ir=ir, notes=notes,
                          non_reconnus=non_reconnus, ignores=ignores,
                          hypotheses=hypotheses, intention="composee")

    def _traduire_simple(self, phrase: str, reponses: dict) -> Traduction:
        """Corps de `traduire()` pour UNE seule commande — inchangé, juste
        renommé pour laisser `traduire()` gérer la composition en tête."""
        toks = tokeniser(normaliser(phrase, self._ponctuation))
        intention = self._intention(toks)

        if intention is None:
            return Traduction(statut="incompris",
                              **self._mots(toks, set()),
                              notes=["Aucune intention reconnue dans la phrase."])

        handler = {
            "creer_palettes_couleur": self._creer_palettes_couleur,
            "colorer_selection": self._colorer_selection,
            "regler_intensite": self._regler_intensite,
            "regler_parametre": self._regler_parametre,
            "enregistrer_cue": self._enregistrer_cue,
            "aller_a_cue": self._aller_a_cue,
            "enregistrer_sub": self._enregistrer_sub,
            "appliquer_effet": self._appliquer_effet,
            "arreter_effet": self._arreter_effet,
            "bump_sub": self._bump_sub,
            "enregistrer_preset": self._enregistrer_preset,
            "rappeler_preset": self._rappeler_preset,
            "appel_macro": self._appel_macro,
            "selectionner_query": self._selectionner_query,
            "marquer": self._marquer,
            "parquer": self._parquer,
            "asserter": self._asserter,
            "effacer_filtres": self._effacer_filtres,
            "enregistrer_snapshot": self._enregistrer_snapshot,
            "rappeler_snapshot": self._rappeler_snapshot,
            "appliquer_courbe": self._appliquer_courbe,
            "retirer_courbe": self._retirer_courbe,
            "selectionner_partition": self._selectionner_partition,
            "supprimer_partition": self._supprimer_partition,
            "plein_feu": self._action_sur_selection,
            "hors_scene": self._action_sur_selection,
            "sneak": self._action_sur_selection,
            "verifier": self._verifier,
            "copier_libelles": self._copier_libelles,
            "creer_plage": self._creer_plage,
            "update_cue": self._update_cue,
            "selection_derniere": self._action_sans_argument,
            "selection_active": self._action_sans_argument,
            "selection_manuelle": self._action_sans_argument,
        }[intention]

        # `_ignores` a besoin de savoir quelle intention a été retenue, pour
        # distinguer un déclencheur qui a fait son travail (celui de CETTE
        # intention) d'un déclencheur resté sur le carreau (celui d'une autre
        # — « effet » dans une phrase partie sur `colorer_selection »). Les 27
        # sites qui construisent une `Traduction` ne connaissent pas leur
        # propre nom d'intention ; le passer par un champ le temps de l'appel
        # évite de tous les retoucher. Sauvegarde/restauration parce que
        # `interpreter_flou` rappelle `traduire()` de façon imbriquée : sans
        # ça, l'appel interne laisserait le champ faussé pour l'externe.
        precedente = self._intention_courante
        self._intention_courante = intention
        try:
            trad = handler(toks, reponses)
        finally:
            self._intention_courante = precedente
        trad.intention = intention
        return trad

    # -- nuancier : seul Lee est connu, donc « pas de mot dans la phrase »
    # veut presque toujours dire Lee — mais c'est une supposition du
    # traducteur, jamais une confirmation de l'utilisateur. Partagé par
    # `_creer_palettes_couleur` et `_colorer_selection`, les deux seuls
    # endroits qui peuvent avoir à deviner le nuancier.
    def _nuancier_avec_hypothese(
        self, reponses: dict
    ) -> tuple[int | None, Hypothese | None, str | None]:
        """Retourne (numero, hypothese_ou_None, erreur_ou_None).

        `reponses["nuancier"]` déjà répondu ("lee", ou un dict
        `{cle:"autre", valeur:<texte>}` pour une saisie libre) : résolu et
        confirmé, aucune hypothèse. Non répondu : Lee retenu par défaut,
        mais marqué comme HYPOTHÈSE (voir la classe `Hypothese`) — le
        traducteur ne l'affirme pas, il le suppose. `erreur` n'est renseigné
        que si l'utilisateur a explicitement demandé un nuancier que le
        projet ne connaît pas (Rosco, Apollo...) : étape 3bis de
        `PIPELINE_TRADUCTION.md`, jamais improviser, le dire plutôt.
        """
        reponse = reponses.get("nuancier")
        if reponse is not None:
            mot = reponse.get("valeur", "") if isinstance(reponse, dict) else reponse
            cle, _ = self._resoudre(str(mot).strip().lower(), self._nuanciers)
            if cle is None:
                return None, None, (
                    f"« {mot} » n'est pas un nuancier connu de ce projet — seul Lee est "
                    "sourcé aujourd'hui (voir reference/lee_filters_theatre.md). Il faudrait "
                    "d'abord l'ajouter au corpus à partir d'un catalogue officiel, pas "
                    "improviser une correspondance."
                )
            return self.lex["nuanciers"][cle]["numero"], None, None

        hypothese = Hypothese(
            champ="nuancier", valeur="Lee",
            pourquoi="Aucun nuancier nommé dans la phrase (ex. « lee ») — Lee est le seul "
                     "connu de ce projet, retenu par défaut plutôt que de bloquer.",
            correction=Question(
                id="nuancier", texte="Quel nuancier ?",
                pourquoi="Rien dans la phrase ne précisait le nuancier — Lee a été supposé, "
                         "pas confirmé.",
                options=[
                    Option(cle="lee", libelle="Lee — confirmer"),
                    Option(cle="autre", libelle="Un autre nuancier", demande_valeur=True),
                ],
            ),
        )
        return self.lex["nuanciers"]["lee"]["numero"], hypothese, None

    def _vocabulaire_connu(self) -> set[str]:
        """Tout ce que le lexique sait nommer, créneaux compris.

        Pas seulement les déclencheurs d'intention : les couleurs, les objets,
        les nuanciers et les cibles de cue en font partie. Ces mots-là, l'app
        les connaît — qu'elle ait su ou non quoi en faire dans une phrase
        donnée est une autre question, et c'est justement la distinction que
        `_non_reconnus` doit préserver (voir son commentaire)."""
        connus = {m for corps in self.lex["intentions"].values()
                  for mots in self._tous_declencheurs(corps).values() for m in mots}
        connus |= self._outils | self._mots_plage | {"%"}
        connus |= set(self._marqueurs_duree) | set(self._marqueurs_duree_post)
        connus |= self._mots_sans | self._mots_temps
        connus |= set(MARQUEURS_UNITE_PARAMETRE)
        for index in (self._objets, self._objets_cible, self._nuanciers,
                      self._couleurs, self._cue_cibles, self._parametres):
            connus |= set(index)
        return connus

    def _non_reconnus(self, toks: list[str], pris: set[int]) -> list[str]:
        """Mots que le lexique ne sait pas nommer du tout.

        **Ne jamais y remettre le vocabulaire de créneau** (bug corrigé le
        2026-08-28). La version précédente ne considérait « connus » que les
        déclencheurs d'intention : sur une phrase dont l'intention échouait,
        l'app annonçait donc ne pas reconnaître « jaune » — une couleur de son
        propre lexique, qu'elle venait de traduire correctement dans la phrase
        d'avant. Elle enseignait ainsi à l'utilisateur des limites fausses, et
        lui faisait abandonner des mots qui marchent.

        Un mot connu mais resté inutilisé n'est pas « non reconnu » : il est
        *ignoré*, ce que rapporte `_ignores` — deux problèmes distincts qui
        appellent deux messages distincts."""
        connus = self._vocabulaire_connu()
        return [t for i, t in enumerate(toks)
                if i not in pris and not t.isdigit() and t not in connus]

    def _ignores(self, toks: list[str], pris: set[int]) -> list[str]:
        """Mots du lexique présents dans la phrase mais absents du résultat.

        Le pendant de `_non_reconnus`, et le plus dangereux des deux : ces
        mots-là ont un sens pour l'app, elle ne s'en est simplement pas
        servie. « circuits 1 à 5 en jaune bleu » ne retient qu'une teinte.
        Sans ce signalement, la macro produite a l'air complète et ne l'est
        pas — exactement la classe d'erreur que `REGLES_POUR_UI.md` (règle 4)
        désigne comme la pire du projet : celle qui ne lève aucune erreur.
        L'UI doit les afficher sur TOUS les statuts, y compris `compris`.

        Deux familles de mots y entrent.

        1. Le vocabulaire de CRÉNEAU — couleurs, objets, nuanciers, cibles de
           cue — c'est-à-dire les mots qui portent du contenu jusqu'à l'IR.

        2. Les déclencheurs d'une AUTRE intention que celle retenue (paramètre
           `intention`, ajouté le 2026-09-03). « je veux un effet jaune sur les
           circuits 1 à 5 » part sur `colorer_selection` et rend un jaune fixe :
           le mot « effet », qui nomme une capacité entière du lexique,
           disparaissait sans un mot. Il n'était ni « non reconnu » (l'app le
           connaît) ni « ignoré » (tous les déclencheurs en étaient exclus).

        Les déclencheurs de l'intention RETENUE restent exclus, eux : ils ont
        fait leur travail — choisir le handler — sans jamais entrer dans
        `pris`, faute de remplir un créneau. Les compter ferait crier au mot
        perdu sur presque chaque phrase correcte (51 faux positifs mesurés sur
        la suite de tests avant d'affiner)."""
        interessants: set[str] = set()
        for index in (self._objets, self._objets_cible, self._nuanciers,
                      self._couleurs, self._cue_cibles):
            interessants |= set(index)

        # Les déclencheurs des AUTRES intentions, moins ceux de l'intention
        # retenue. `self._intention_courante` est posé par `traduire()` le
        # temps d'un appel (voir sa note) : quand il vaut None — appel direct
        # d'un handler en test, ou phrase sans intention du tout — aucun
        # déclencheur n'entre, ce qui reste le comportement prudent.
        retenue = self._intention_courante
        siens: set[str] = set()
        if retenue:
            tous = set()
            for nom, corps in self.lex["intentions"].items():
                mots = {m for groupe in self._tous_declencheurs(corps).values()
                        for m in groupe}
                tous |= mots
                if nom == retenue:
                    siens = mots
            interessants |= tous

        # Le retrait des déclencheurs de l'intention retenue se fait EN
        # DERNIER, sur l'ensemble — pas seulement sur ce qu'on vient
        # d'ajouter. Un même mot peut appartenir aux deux mondes : « dernière »
        # est à la fois le déclencheur de `selection_derniere` et un alias de
        # la cible de cue `Last`. Retiré trop tôt, il rentrait quand même par
        # la famille de créneau et se faisait signaler sur sa propre phrase
        # (trouvé le 2026-09-03 en ajoutant la tranche « quotidien »).
        interessants -= siens
        interessants -= self._outils | self._mots_plage
        return [t for i, t in enumerate(toks)
                if i not in pris and not t.isdigit() and t in interessants]

    def _mots(self, toks: list[str], pris: set[int]) -> dict[str, list[str]]:
        """Les deux comptes rendus de mots, à splatter dans une `Traduction`.

        Groupés en un seul appel pour qu'aucun site de construction ne puisse
        rapporter les mots inconnus en oubliant les mots ignorés — c'est
        précisément cet oubli qui a produit le bug de la règle 4."""
        return {"non_reconnus": self._non_reconnus(toks, pris),
                "ignores": self._ignores(toks, pris)}

    # -- intention : créer des palettes de couleur -------------------------
    def _creer_palettes_couleur(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        notes: list[str] = []
        questions: list[Question] = []
        hypotheses: list[Hypothese] = []

        # Le nuancier avant les cibles : « lee » précède souvent le numéro de
        # gel, qu'il ne faut pas confondre avec un numéro de palette.
        nuancier, i_nuancier = self._nuancier(toks, pris)
        if nuancier is None:
            nuancier, hyp, erreur = self._nuancier_avec_hypothese(reponses)
            if erreur:
                return Traduction(statut="incompris", notes=[erreur])
            if hyp:
                hypotheses.append(hyp)

        cibles = self._cibles(toks, pris)
        couleurs = self._couleurs_de(toks, pris, questions, notes, reponses)

        if couleurs is None:                       # une couleur ambiguë
            return Traduction(statut="a_preciser", questions=questions, notes=notes)
        if not cibles:
            return Traduction(statut="incompris", notes=notes + [
                "Aucun numéro de palette trouvé dans la phrase."])
        if not couleurs:
            return Traduction(statut="incompris",
                              **self._mots(toks, pris),
                              notes=notes + ["Aucune couleur reconnue dans la phrase."])
        if len(couleurs) != len(cibles):
            return Traduction(statut="incompris", notes=notes + [
                f"{len(cibles)} palette(s) demandée(s) mais {len(couleurs)} "
                f"couleur(s) donnée(s) : "
                + ", ".join(c["nom"] for c in couleurs) + "."])

        # Portée : jamais devinée. `Record Color Palette` capture la sélection
        # courante — ou tous les channels non-défaut si rien n'est sélectionné,
        # ce qui n'est presque jamais l'intention. Voir `APP.md`.
        portee = reponses.get("portee_enregistrement")
        if portee is None:
            return Traduction(statut="a_preciser", notes=notes,
                              questions=[self._question_portee()])

        # Les deux options exigent une sélection. `{By Type}` ne dispense pas
        # d'en donner une — il décrit ce que la palette contiendra, pas comment
        # elle s'enregistre (manuel §10 « Storing a By Type Palette »).
        if isinstance(portee, dict):
            cle, valeur = portee.get("cle"), portee.get("valeur")
        else:
            cle, valeur = portee, None
        if cle not in ("par_type", "selection"):
            return Traduction(statut="a_preciser", notes=notes,
                              questions=[self._question_portee()])
        selection = self._selection_depuis(valeur)
        if selection is None:
            return Traduction(statut="a_preciser", notes=notes,
                              questions=[self._question_portee()])
        options = ["{By Type}"] if cle == "par_type" else []
        if options:
            notes.append("Palette générique `{By Type}` : donner de préférence un "
                         "seul circuit par type d'appareil — les autres circuits du "
                         "même type seraient figés en valeurs individuelles.")

        # LA SÉLECTION EST REPOSÉE À CHAQUE ÉTAPE, y compris sur le Record.
        # Elle ne survit pas à un enregistrement : `Record` désélectionne les
        # channels (manuel §6, énoncé deux fois). Sans cette répétition, seule
        # la PREMIÈRE palette d'une série serait correcte, les suivantes
        # s'enregistrant depuis une sélection vide — sans que la console refuse
        # quoi que ce soit. Le workbook officiel L2 repose la sélection à chaque
        # enregistrement pour cette raison exacte.
        ir: list[dict] = []
        for cible, couleur in zip(cibles, couleurs):
            ir.append({"selection": dict(selection),
                       "action": {"type": "couleur_gel",
                                  "nuancier": nuancier, "teinte": couleur["gel"]}})
            record = {"type": "record_palette", "famille": "Color Palette",
                      "cible": cible, "label": couleur["nom"].capitalize()}
            if options:
                record["options"] = list(options)
            ir.append({"selection": dict(selection), "action": record})

        # Les teintes qui portent déjà une note détaillée (une décision du
        # projet à expliquer) ne sont pas re-listées : elles sont plus haut.
        for couleur in couleurs:
            if not couleur["detaillee"]:
                notes.append(f"{couleur['nom']} → Lee {couleur['gel']:03d} "
                             f"({couleur['nom_lee']})")
        return Traduction(statut="compris", ir=ir, notes=notes, hypotheses=hypotheses,
                          **self._mots(toks, pris))

    def _question_portee(self) -> Question:
        modele = self.lex["questions"]["portee_enregistrement"]
        return Question(
            id="portee_enregistrement",
            texte=modele["texte"],
            pourquoi=" ".join(modele["pourquoi"].split()),
            options=[Option(cle=o["cle"], libelle=o["libelle"],
                            detail=" ".join(o.get("detail", "").split()),
                            demande_valeur=o.get("demande_valeur", False))
                     for o in modele["options"]],
        )

    def _selection_depuis(self, valeur) -> dict | None:
        """La réponse à la question de portée, en dict, en entier ou en texte.

        Le texte accepte un groupe (« groupe 99 ») autant que des circuits :
        c'est la forme qu'emploie le workbook officiel L2 pour enregistrer une
        série de palettes — un groupe de travail contenant un appareil de
        chaque type.
        """
        if isinstance(valeur, dict):
            return valeur
        if isinstance(valeur, int):
            return {"objet": "Chan", "numero": valeur}
        if isinstance(valeur, str) and valeur.strip():
            toks = tokeniser(normaliser(valeur, self._ponctuation))
            pris: set[int] = set()
            objet = self._objet(toks, pris) or "Chan"
            return self._selection_de(objet, toks, pris)
        return None

    # -- intention : colorer une sélection ---------------------------------
    def _colorer_selection(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        notes: list[str] = []
        questions: list[Question] = []
        hypotheses: list[Hypothese] = []

        objet = self._objet(toks, pris) or "Chan"
        nuancier, i_nuancier = self._nuancier(toks, pris)

        # Un numéro de gel écrit après « lee » : c'est le seul nombre qui ne
        # décrit pas la sélection. On le retire avant de lire la plage.
        teinte = None
        if i_nuancier is not None:
            for i, valeur in self._nombres(toks, pris):
                if i > i_nuancier:
                    teinte, _ = valeur, pris.add(i)
                    break

        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        if teinte is None:
            couleurs = self._couleurs_de(toks, pris, questions, notes, reponses)
            if couleurs is None:
                return Traduction(statut="a_preciser", questions=questions, notes=notes)
            if couleurs:
                # Une seule teinte peut être appliquée par commande. Retenir
                # silencieusement la première quand la phrase en nomme
                # plusieurs — ce que faisait la version précédente — produit
                # une macro d'apparence impeccable qui perd une couleur en
                # route (« circuits 1 à 5 en jaune bleu » donnait un jaune,
                # sans une note). C'est une ambiguïté que seul l'utilisateur
                # peut lever : elle vaut une question, pas un choix d'office
                # (REGLES_POUR_UI.md, règles 4 et 5). Corrigé le 2026-08-28.
                choisie = couleurs[0]
                if len(couleurs) > 1:
                    reponse = str(reponses.get("couleur_unique", ""))
                    choisie = next((c for c in couleurs
                                    if str(c["gel"]) == reponse), None)
                    if choisie is None:
                        questions.append(self._question_couleur_unique(couleurs))
                        return Traduction(statut="a_preciser", questions=questions,
                                          notes=notes, **self._mots(toks, pris))
                teinte = choisie["gel"]
                notes.append(f"{choisie['nom']} → Lee {teinte:03d} "
                             f"({choisie['nom_lee']})")
            else:
                # Aucun mot de couleur, aucun « lee » : un numéro resté libre
                # ICI a déjà survécu à l'extraction de la sélection (qui a
                # pris ses propres nombres en premier, voir `_selection_de`
                # ci-dessus) — il ne peut donc plus désigner que le gel.
                # Sans ce repli, « groupe 1 à 5 en 205 » restait injustement
                # incompris faute du mot « lee » — trouvé le 2026-08-07 en
                # testant l'app avec une phrase réelle, pas écrite pour le
                # traducteur.
                libres = self._nombres(toks, pris)
                if not libres:
                    return Traduction(statut="incompris",
                                      **self._mots(toks, pris),
                                      notes=notes + ["Aucune couleur reconnue."])
                i, teinte = libres[0]
                pris.add(i)
                notes.append(f"« {teinte} » interprété comme un numéro de gel "
                             "(aucun mot de couleur reconnu dans la phrase).")

        if nuancier is None:
            nuancier, hyp, erreur = self._nuancier_avec_hypothese(reponses)
            if erreur:
                return Traduction(statut="incompris", notes=notes + [erreur])
            if hyp:
                hypotheses.append(hyp)

        ir = [{"selection": selection,
               "action": {"type": "couleur_gel", "nuancier": nuancier, "teinte": teinte}}]
        return Traduction(statut="compris", ir=ir, notes=notes, hypotheses=hypotheses,
                          **self._mots(toks, pris))

    # -- intention : régler une intensité ----------------------------------
    def _regler_intensite(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        notes: list[str] = []

        objet = self._objet(toks, pris)

        # La sélection SE LIT EN PREMIER, et l'ordre compte. « circuits 1 à 5
        # à 50 % » contient deux fois le mot « à » : la première plage désigne
        # les circuits, ce qui reste désigne le niveau. Lire le niveau d'abord
        # ferait comprendre « dégradé de 5 à 50 » sur les circuits 1 seul.
        #
        # Mais ce raisonnement ne vaut QUE si un objet est nommé. Sans lui,
        # « à 50 % » n'a qu'un seul nombre, et le lire comme une sélection le
        # confisquait au niveau : la phrase repartait en « niveau introuvable »
        # alors que le 50 était là, sous les yeux.
        selection = None
        i_sub = None if objet is not None else \
            self._indice_objet_cle("Sub", toks, pris, index=self._objets_cible)
        if objet is not None:
            selection = self._selection_de(objet, toks, pris)
            if selection is None:
                return Traduction(statut="incompris", notes=[
                    "Aucun numéro trouvé pour la sélection."])
        elif i_sub is not None:
            # `Sub` + `At` : refusé en confiance S jusqu'au 2026-09-09, puis
            # requalifié `inconnu` faute d'observation (voir modele.yaml,
            # legalite Sub+intensite) — TRANCHÉ `oui` au banc réel le
            # 2026-09-13 (`Sub 1 At 50 Enter`, fader du sub observé montant à
            # 50 %). Un seul numéro, jamais une plage `Thru` : aucune source
            # du dépôt n'atteste `Sub <a> Thru <b> At <n>`, donc on ne
            # l'invente pas — seul `self._selection_de` (via `self._objet`)
            # gère les plages, volontairement contourné ici.
            cible = None
            for i, valeur in self._nombres(toks, pris):
                if i > i_sub:
                    cible = valeur
                    pris.add(i)
                    break
            if cible is None:
                return Traduction(statut="incompris", notes=[
                    "Aucun numéro de sub trouvé après « sub »."])
            selection = {"objet": "Sub", "numero": cible}
        elif not self._vise_la_selection_courante(toks, pris):
            return Traduction(statut="incompris",
                              notes=[self._motif_refus_selection(toks, pris)])
        elif not self._selection_courante_permise("intensite"):
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])
        else:
            notes.append(self.NOTE_SELECTION_COURANTE)

        # Le niveau se lit au marqueur, jamais par position : c'est le nombre
        # qui précède `%`, ou celui qui suit « intensité » / « niveau ».
        niveau = self._niveau(toks, pris)
        if niveau is None:
            return Traduction(statut="incompris", notes=[
                "Niveau introuvable — préciser « % », « pourcent », "
                "« intensité » ou « niveau »."])

        action = {"type": "intensite"}
        action.update(niveau)

        # « en 8 secondes » sur un niveau, c'est un SNEAK, pas un `Time` : le
        # manuel §6 donne `[5] [At] [50] [Sneak] [8] [Enter]` — « sneaks
        # channel 5 to 50% in 8 seconds ». Et la durée s'y colle sans le
        # mot-clé `Time`, contrairement au sneak sans destination. Aucune
        # forme `At <niveau> Time <n>` n'est attestée : on ne l'invente pas.
        duree = self._duree(toks, pris)
        if duree is not None:
            action["sneak"] = duree
            notes.append(
                "La durée passe par `Sneak` — c'est la forme documentée pour "
                "amener une sélection à un niveau en un temps donné.")

        etape: dict = {"action": action}
        if selection is not None:
            etape["selection"] = selection
        return Traduction(statut="compris", ir=[etape], notes=notes,
                          **self._mots(toks, pris))

    # -- intention : régler un paramètre générique (Pan, Tilt...) -----------
    def _regler_parametre(self, toks: list[str], reponses: dict) -> Traduction:
        """Une seule fonction pour tout paramètre déclaré dans
        `lexique.yaml:parametres` / `grammar/modele.yaml:parametres` — voir
        leurs commentaires. Ajouter un paramètre n'ajoute aucun code ici."""
        pris: set[int] = set()
        notes: list[str] = []

        # 1. quel paramètre ? Même discipline que `_objet` : correspondance
        #    exacte sur toute la phrase d'abord, tolérance seulement au
        #    second passage — la détection reste un routeur, pas un créneau.
        parametre = None
        for exact in (True, False):
            for i, tok in enumerate(toks):
                if i in pris:
                    continue
                if exact:
                    cle = self._parametres.get(tok)
                else:
                    cle, _ = self._resoudre(tok, self._parametres)
                if cle:
                    parametre = cle
                    pris.add(i)
                    break
            if parametre is not None:
                break
        if parametre is None:
            return Traduction(statut="incompris", notes=[
                "Aucun paramètre reconnu (Pan, Tilt...)."])

        # 2. quelle forme ? Lue dans le modèle pour CE paramètre précis,
        #    jamais supposée : « inverse le tilt » doit rester incompris tant
        #    que Tilt ne déclare pas `echelle` (seule Pan la déclare, source
        #    « Mirror Pan », confiance B — voir grammar/modele.yaml).
        formes_dispo = self._formes_parametre(parametre)
        i_inverse = self._indice_mot(toks, pris, {"inverse", "inverser", "inversez"})
        i_ajout = self._indice_mot(toks, pris, {"ajoute", "ajouter", "monte", "monter"})
        i_retrait = self._indice_mot(toks, pris, {"retire", "retirer", "enleve", "enlever",
                                                    "descend", "descends", "descendre"})

        i_valeur = None    # index du jeton valeur, pour consommer un `%` adjacent au 4.
        if i_inverse is not None:
            if "echelle" not in formes_dispo:
                return Traduction(statut="incompris", notes=[
                    f"Aucune forme d'inversion sourcée pour « {parametre} »."])
            forme, valeur = "echelle", -100
        else:
            forme = ("relatif_ajout" if i_ajout is not None else
                     "relatif_retrait" if i_retrait is not None else "absolue")
            if forme not in formes_dispo:
                return Traduction(statut="incompris", notes=[
                    f"Aucune forme « {forme} » sourcée pour « {parametre} »."])

            if forme == "absolue":
                # Par défaut, même convention que `_regler_intensite` : la
                # SÉLECTION se lit en premier (voir plus bas), la valeur est
                # le nombre libre restant. Mais si un nombre est immédiatement
                # suivi d'une unité (« 10 degrés »), il est pris ICI, avant la
                # sélection — sinon « circuit 1 à 10 degrés » lirait « 1 à 10 »
                # comme une PLAGE de circuits (`_plage` ne connaît pas les
                # degrés, seulement `%`/« pourcent ») et n'aurait plus rien
                # pour la valeur. Même principe que le verrou verbe ci-dessus,
                # avec un marqueur d'unité au lieu d'un verbe.
                valeur = None
                for i, tok in enumerate(toks):
                    if (i not in pris and tok.isdigit()
                            and i + 1 < len(toks) and toks[i + 1] in MARQUEURS_UNITE_PARAMETRE
                            and (i + 1) not in pris):
                        valeur = int(tok)
                        pris.update({i, i + 1})
                        break
            else:
                # « ajoute »/« retire » inversent cet ordre habituel : « ajoute
                # 10 au pan du circuit 1 » place la valeur AVANT le numéro de
                # sélection. Le nombre le plus proche du verbe est donc pris
                # ICI, avant la sélection — ce qui reste ira nécessairement à
                # elle, quel que soit l'ordre d'écriture par ailleurs.
                candidats = self._nombres(toks, pris)
                if not candidats:
                    return Traduction(statut="incompris", notes=[
                        f"Aucune valeur trouvée pour « {parametre} »."])
                i_verbe = i_ajout if i_ajout is not None else i_retrait
                i_valeur, valeur = min(candidats, key=lambda iv: abs(iv[0] - i_verbe))
                pris.add(i_valeur)

        # 3. la sélection — PAS `_selection_de` (qui essaie `_plage` en
        #    premier) : rien ne source de plage/fan de circuits pour ces
        #    paramètres, et « hue du circuit 1 à 180 » se ferait lire comme
        #    une plage de circuits 1-180 (bug réel trouvé en session), le
        #    « à » jouant à la fois le rôle de séparateur de plage et de
        #    préposition vers la valeur — même famille de piège que celui
        #    déjà documenté pour `_regler_intensite`, mais sans marqueur
        #    (`%`/« degrés ») pour le lever ici. On ne cherche donc que le
        #    nombre COLLÉ à l'objet, jamais plus loin.
        avant = set(pris)
        objet = self._objet(toks, pris)
        selection = None
        if objet is not None:
            i_objet = next(iter(pris - avant))
            candidat = None
            if i_objet + 1 < len(toks) and toks[i_objet + 1].isdigit() \
                    and (i_objet + 1) not in pris:
                candidat = (i_objet + 1, int(toks[i_objet + 1]))
            elif i_objet - 1 >= 0 and toks[i_objet - 1].isdigit() \
                    and (i_objet - 1) not in pris:
                candidat = (i_objet - 1, int(toks[i_objet - 1]))
            if candidat is None:
                return Traduction(statut="incompris", notes=[
                    "Aucun numéro trouvé pour la sélection."])
            i_num, numero = candidat
            pris.add(i_num)
            selection = {"objet": objet, "numero": numero}
        elif not self._vise_la_selection_courante(toks, pris):
            return Traduction(statut="incompris",
                              notes=[self._motif_refus_selection(toks, pris)])
        elif not self._selection_courante_permise("regler_parametre"):
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])
        else:
            notes.append(self.NOTE_SELECTION_COURANTE)

        # 4. forme absolue : la valeur est ce qu'il reste, une fois la
        #    sélection retirée du jeu de nombres libres.
        if valeur is None:
            candidats = self._nombres(toks, pris)
            if not candidats:
                return Traduction(statut="incompris", notes=[
                    f"Aucune valeur trouvée pour « {parametre} »."])
            i_valeur, valeur = candidats[0]
            pris.add(i_valeur)

        # `%`/« pourcent » juste après la valeur (Zoom, Iris...) : purement
        # décoratif une fois la valeur trouvée — `_plage` l'excluait déjà
        # d'une plage (MARQUEURS_NIVEAU_POSTFIXES) — mais un mot CONNU laissé
        # de côté est un `ignores`, pas un silence acceptable (règle 4).
        if i_valeur is not None and i_valeur + 1 < len(toks) \
                and toks[i_valeur + 1] in MARQUEURS_NIVEAU_POSTFIXES \
                and (i_valeur + 1) not in pris:
            pris.add(i_valeur + 1)

        etape: dict = {"action": {"type": "regler_parametre", "parametre": parametre,
                                  "forme": forme, "valeur": valeur}}
        if selection is not None:
            etape["selection"] = selection
        return Traduction(statut="compris", ir=[etape], notes=notes,
                          **self._mots(toks, pris))

    def _formes_parametre(self, parametre: str) -> set[str]:
        """Formes sourcées pour CE paramètre précis, lues dans
        `grammar/modele.yaml:parametres` — jamais empruntées à un paramètre
        voisin. Même pattern d'accès que `_selection_courante_permise`."""
        try:
            catalogue = self._generateur_ou_defaut().modele["parametres"]
            return set(catalogue.get(parametre, {}).get("formes", {}))
        except Exception:                                     # noqa: BLE001
            return set()

    def _niveau(self, toks: list[str], pris: set[int]) -> dict | None:
        """`50 %` → {valeur: 50}. `10 a 50 %` → dégradé {de: 10, a: 50}."""
        for i, tok in enumerate(toks):
            if tok not in MARQUEURS_NIVEAU:
                continue
            # dégradé : `10 a 50 %`
            if i >= 3 and toks[i - 1].isdigit() and toks[i - 2] in self._mots_plage \
                    and toks[i - 3].isdigit() and not {i - 1, i - 2, i - 3} & pris:
                pris.update({i, i - 1, i - 2, i - 3})
                return {"de": int(toks[i - 3]), "a": int(toks[i - 1])}
            if i >= 1 and toks[i - 1].isdigit() and (i - 1) not in pris:
                pris.update({i, i - 1})
                return {"valeur": int(toks[i - 1])}
            if i + 1 < len(toks) and toks[i + 1].isdigit() and (i + 1) not in pris:
                pris.update({i, i + 1})
                return {"valeur": int(toks[i + 1])}
        return None

    def _duree(self, toks: list[str], pris: set[int]) -> int | None:
        """`en 20 secondes` → 20. Lu au marqueur, jamais par position.

        Même principe que `_niveau` et pour la même raison : sans marqueur, un
        nombre est un numéro de circuit ou de cue. « circuits 1 à 5 en 3
        secondes » et « circuits 1 à 5 » ne doivent pas se disputer le 3.

        `s` n'est accepté qu'en POSTFIXE collé à un nombre (« 20 s »), comme
        `%` pour les niveaux : une lettre isolée n'a pas assez de matière pour
        arbitrer, et la tolérance aux fautes ne s'applique pas sous 4 lettres.
        """
        for i, tok in enumerate(toks):
            if i in pris:
                continue
            if tok in self._marqueurs_duree:
                for j in (i - 1, i + 1):
                    if 0 <= j < len(toks) and toks[j].isdigit() and j not in pris:
                        pris.update({i, j})
                        return int(toks[j])
            elif tok in self._marqueurs_duree_post:
                j = i - 1
                if j >= 0 and toks[j].isdigit() and j not in pris:
                    pris.update({i, j})
                    return int(toks[j])
        return None

    def _sans_temps(self, toks: list[str], pris: set[int]) -> bool:
        """« sans les temps », « sans temporisation ».

        Rend `Time 0`, jamais un `Time` nu — le manuel §16 est explicite :
        `Go To Cue 8 Time Enter` emploie au contraire les temps STOCKÉS dans
        la cue. C'est l'erreur exacte de la macro « Quickstep » de la feuille
        communautaire, qui écrit `[time] [enter]` en annonçant l'inverse.
        """
        for i, tok in enumerate(toks):
            if i in pris or tok not in self._mots_sans:
                continue
            for j in range(i + 1, min(i + 4, len(toks))):
                if toks[j] in self._mots_temps and j not in pris:
                    pris.update({i, j})
                    return True
        return False

    # -- intention : parquer (Park, un seul circuit/groupe, forme absolue) --
    def _parquer(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # Volontairement PAS `_selection_de` : sa détection de plage
        # (`_plage`) lirait « circuit 4 à 50 » comme la plage 4 à 50, jamais
        # comme un circuit et un niveau — le même mot « à » sert aux deux
        # rôles, et rien ici ne permet de trancher avant coup (contrairement
        # à `_regler_intensite`, qui ne rencontre l'ambiguïté qu'avec DEUX
        # « à » dans la phrase). Le seul exemple sourcé de Park porte sur un
        # circuit unique (`grammar/modele.yaml`, section `park`) : cette
        # tranche se limite donc à un seul circuit/groupe, jamais une plage,
        # ce qui élimine l'ambiguïté à la racine plutôt que de la deviner.
        objet = self._objet(toks, pris) or "Chan"
        libres = self._nombres(toks, pris)
        if not libres:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])
        i_objet, numero = libres[0]
        pris.add(i_objet)
        selection = {"objet": objet, "numero": numero}

        # Un dégradé (« de/a ») n'a pas de sens pour Park — une seule valeur,
        # pas une transition — donc seule la clé `valeur` est acceptée.
        niveau = self._niveau(toks, pris)
        if niveau is None or "valeur" not in niveau:
            return Traduction(statut="incompris", notes=[
                "Niveau introuvable — préciser « % », « pourcent », « intensité » "
                "ou « niveau ». Sans valeur, le parquage est un bascule qui dépend "
                "d'un état console que ce traducteur ne devine pas."])

        ir = [{"selection": selection,
               "action": {"type": "parquer", "valeur": niveau["valeur"]}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : enregistrer une sélection dans une cue -----------------
    def _enregistrer_cue(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # Le marqueur « cue » d'abord : c'est lui qui sépare, dans la liste de
        # nombres de la phrase, celui qui désigne la cible (après le marqueur)
        # de ceux qui désignent la sélection (partout ailleurs).
        i_cue = self._indice_objet_cle("Cue", toks, pris)
        if i_cue is None:
            return Traduction(statut="incompris", notes=[
                "Aucune cue désignée — le mot « cue » (ou « mémoire ») est requis."])

        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_cue:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de cue trouvé après « cue »."])

        objet = self._objet(toks, pris) or "Chan"
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        ir = [{"selection": selection, "action": {"type": "record_cue", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : aller à une cue -----------------------------------------
    def _aller_a_cue(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # Une cible symbolique (« noir », « suivante »…) d'abord : elle seule
        # dispense de tout numéro dans la phrase.
        for i, tok in enumerate(toks):
            if i in pris:
                continue
            cle, _ = self._resoudre(tok, self._cue_cibles)
            if cle:
                pris.add(i)
                action = {"type": "go_to_cue", "mot": cle}
                self._temps_de_cue(action, toks, pris)
                return Traduction(statut="compris", ir=[{"action": action}],
                                  **self._mots(toks, pris))

        # Le mot « cue » lui-même : il désigne bien l'objet de l'action, et
        # doit donc compter comme consommé, sans quoi `_ignores` le signale à
        # tort comme un mot perdu sur une phrase pourtant traduite entière.
        self._objet(toks, pris)

        libres = self._nombres(toks, pris)
        if not libres:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de cue ni destination reconnue "
                "(noir, suivante, précédente, home)."])
        i, cible = libres[0]
        pris.add(i)
        action = {"type": "go_to_cue", "cible": cible}
        self._temps_de_cue(action, toks, pris)
        return Traduction(statut="compris", ir=[{"action": action}],
                          **self._mots(toks, pris))

    def _temps_de_cue(self, action: dict, toks: list[str], pris: set[int]) -> None:
        """Pose le `Time` d'un `Go To Cue`, s'il y en a un dans la phrase.

        Deux formes seulement, et jamais un `Time` nu : « en 3 secondes »
        donne `Time 3`, « sans les temps » donne `Time 0`. Le manuel §16 est
        explicite sur le fait qu'un `Time` sans valeur emploie au contraire
        les temps stockés dans la cue — produire ça pour « sans les temps »
        serait exactement l'inverse de la demande."""
        duree = self._duree(toks, pris)
        if duree is not None:
            action["temps"] = {"valeur": duree}
        elif self._sans_temps(toks, pris):
            action["temps"] = {"valeur": 0}

    # -- intention : enregistrer une sélection dans un submaster ------------
    def _enregistrer_sub(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # Même schéma que `_enregistrer_cue` : le mot-clé cible d'abord (ici
        # « sub », résolu dans `self._objets_cible`, jamais `self._objets` —
        # voir le commentaire de `objets_cible` dans lexique.yaml), qui sépare
        # dans la phrase le numéro de sub (après) de la sélection (ailleurs).
        i_sub = self._indice_objet_cle("Sub", toks, pris, index=self._objets_cible)
        if i_sub is None:
            return Traduction(statut="incompris", notes=[
                "Aucun submaster désigné — le mot « sub » est requis."])

        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_sub:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de sub trouvé après « sub »."])

        objet = self._objet(toks, pris) or "Chan"
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        ir = [{"selection": selection, "action": {"type": "record_sub", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : appliquer un effet à une sélection ----------------------
    def _appliquer_effet(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        i_effet = self._indice_mot(toks, pris, {"effet", "effets"})
        if i_effet is None:
            return Traduction(statut="incompris", notes=[
                "Aucun effet désigné — le mot « effet » est requis."])

        # Le numéro d'effet se lit juste après « effet », avant la sélection —
        # même logique positionnelle que le numéro de cue dans `_enregistrer_cue`.
        numero = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_effet:
                numero, _ = valeur, pris.add(i)
                break
        if numero is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro d'effet trouvé après « effet »."])

        objet = self._objet(toks, pris) or "Chan"
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        ir = [{"selection": selection,
               "action": {"type": "appliquer_effet", "numero": numero}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : arrêter un effet ----------------------------------------
    def _arreter_effet(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        i_effet = self._indice_mot(toks, pris, {"effet", "effets"})
        if i_effet is None:
            return Traduction(statut="incompris", notes=[
                "Aucun effet désigné — le mot « effet » est requis."])

        # « tous les effets » dispense d'un numéro : `Stop Effect Enter` sans
        # argument arrête tout ce qui tourne (manuel §18).
        if self._indice_mot(toks, pris, {"tous", "toutes", "tout"}) is not None:
            ir = [{"action": {"type": "arreter_effet"}}]
            return Traduction(statut="compris", ir=ir,
                              **self._mots(toks, pris))

        numero = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_effet:
                numero, _ = valeur, pris.add(i)
                break
        if numero is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro d'effet trouvé — préciser lequel, ou dire "
                "« tous les effets »."])

        ir = [{"action": {"type": "arreter_effet", "numero": numero}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : bump d'un submaster (haut / bas) ------------------------
    def _bump_sub(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        i_sub = self._indice_objet_cle("Sub", toks, pris, index=self._objets_cible)
        if i_sub is None:
            return Traduction(statut="incompris", notes=[
                "Aucun submaster désigné — le mot « sub » est requis."])

        libres = self._nombres(toks, pris)
        if not libres:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de sub trouvé."])
        i, numero = libres[0]
        pris.add(i)

        direction = None
        if self._indice_mot(toks, pris, {"haut", "up"}) is not None:
            direction = "haut"
        elif self._indice_mot(toks, pris, {"bas", "down"}) is not None:
            direction = "bas"
        elif reponses.get("bump_direction") in ("haut", "bas"):
            direction = reponses["bump_direction"]

        # Aucune source du dépôt ne documente ce que « haut »/« bas » font
        # fonctionnellement (voir lexique.yaml, note de `bump_sub`) — sans
        # marqueur dans la phrase, c'est une question, jamais un choix par défaut.
        if direction is None:
            return Traduction(statut="a_preciser",
                              questions=[self._question_bump_direction()])

        type_action = "sub_bump_haut" if direction == "haut" else "sub_bump_bas"
        ir = [{"action": {"type": type_action, "numero": numero}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    def _question_bump_direction(self) -> Question:
        modele = self.lex["questions"]["bump_direction"]
        return Question(
            id="bump_direction",
            texte=modele["texte"],
            pourquoi=" ".join(modele["pourquoi"].split()),
            options=[Option(cle=o["cle"], libelle=o["libelle"],
                            detail=" ".join(o.get("detail", "").split()))
                     for o in modele["options"]],
        )

    # -- intention : enregistrer une sélection dans un preset ----------------
    def _enregistrer_preset(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # Même schéma que `_enregistrer_sub` : le mot-clé cible d'abord (ici
        # « preset », résolu dans `self._objets_cible`, jamais `self._objets`
        # — un preset ne peut pas en référencer un autre, manuel §11).
        i_preset = self._indice_objet_cle("Preset", toks, pris, index=self._objets_cible)
        if i_preset is None:
            return Traduction(statut="incompris", notes=[
                "Aucun preset désigné — le mot « preset » est requis."])

        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_preset:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de preset trouvé après « preset »."])

        objet = self._objet(toks, pris) or "Chan"
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        ir = [{"selection": selection, "action": {"type": "record_preset", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : rappeler un preset sur une sélection ---------------------
    def _rappeler_preset(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        i_preset = self._indice_objet_cle("Preset", toks, pris, index=self._objets_cible)
        if i_preset is None:
            return Traduction(statut="incompris", notes=[
                "Aucun preset désigné — le mot « preset » est requis."])

        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_preset:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de preset trouvé après « preset »."])

        objet = self._objet(toks, pris) or "Chan"
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        ir = [{"selection": selection, "action": {"type": "rappeler_preset", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : lancer une macro -----------------------------------------
    def _appel_macro(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        i_macro = self._indice_mot(toks, pris, {"macro", "macros"})
        if i_macro is None:
            return Traduction(statut="incompris", notes=[
                "Aucune macro désignée — le mot « macro » est requis."])

        numero = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_macro:
                numero, _ = valeur, pris.add(i)
                break
        if numero is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de macro trouvé après « macro »."])

        ir = [{"action": {"type": "appel_macro", "numero": numero}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : sélectionner via Query (Is In / Isn't In) ---------------
    def _selectionner_query(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # La négation est le seul endroit du langage Eos qui en offre une
        # (manuel §15) — « pas »/« jamais » suffisent à la repérer, le
        # français négatif encadre le verbe plutôt que de le précéder.
        negation = any(t in ("pas", "jamais") for t in toks)

        # Preset et Cue d'abord : mots-clés univoques, pas d'ambiguïté de
        # famille contrairement à « palette ». `Cue` est résolu via l'index
        # générique `self._objets` (même pattern que `_enregistrer_cue`),
        # `Preset` via `self._objets_cible` (même raison que pour Sub :
        # jamais une sélection générique — voir lexique.yaml).
        i_preset = self._indice_objet_cle("Preset", toks, pris, index=self._objets_cible)
        if i_preset is not None:
            type_cible = "Preset"
            i_cible_mot = i_preset
        else:
            i_cue = self._indice_objet_cle("Cue", toks, pris)
            if i_cue is not None:
                type_cible = "Cue"
                i_cible_mot = i_cue
            else:
                i_palette = self._indice_mot(toks, pris, {"palette", "palettes"})
                if i_palette is None:
                    return Traduction(statut="incompris", notes=[
                        "Aucune cible reconnue — « palette », « preset » ou « cue » est requis."])
                # Seule la palette couleur est modélisée dans ce projet
                # (voir `creer_palettes_couleur`) — un « palette » nu, sans
                # le mot « couleur »/« color », ne doit pas être supposé
                # être une palette couleur plutôt qu'une autre famille
                # (Int/Focus/Beam) que ce traducteur ne couvre pas.
                # Le mot de famille est marqué consommé : il désigne bien la
                # cible (Color Palette plutôt qu'Int/Focus/Beam), donc il
                # travaille. Sans ça, `_ignores` le signalait comme un mot
                # perdu — c'est un déclencheur de `colorer_selection`, une
                # autre intention (trouvé le 2026-09-03 en affinant `_ignores`).
                i_famille = self._indice_mot(toks, pris, {"couleur", "couleurs", "color"})
                if i_famille is None:
                    return Traduction(statut="incompris", notes=[
                        "Seule la palette couleur est prise en charge — préciser "
                        "« couleur » (les autres familles de palette ne sont pas "
                        "encore couvertes)."])
                type_cible = "Color Palette"
                i_cible_mot = i_palette

        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_cible_mot:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro trouvé pour la cible de la requête."])

        condition = "Isn't In" if negation else "Is In"
        ir = [{"query": [{"condition": condition,
                          "cible": {"type": type_cible, "numero": cible}}]}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : marquer (drapeau Mark, cue ou channels) -----------------
    def _marquer(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # `self._objet` choisit Chan/Group/Cue selon le mot présent — le
        # même mécanisme, réutilisé ici, sert aussi bien « marque la cue 10 »
        # (le drapeau M) que « marque les circuits 1 à 5 » (la cue source où
        # sont stockés les mouvements NP) : deux usages distincts de la même
        # touche `Mark` (manuel §9), que le traducteur ne cherche pas à
        # départager — c'est le générateur qui porte l'avertissement sur
        # AutoMark/marques référencées, pas le traducteur.
        objet = self._objet(toks, pris)
        if objet is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit, groupe ni cue désigné — le marquage exige une cible explicite."])
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro trouvé pour la cible du marquage."])

        ir = [{"selection": selection, "action": {"type": "marquer"}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : asserter (réaffirmer l'autorité d'une cue/sélection) ---
    def _asserter(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # `self._objet` ne connaît que Chan/Group/Cue (jamais Sub, qui vit
        # dans `objets_cible`) : une phrase « assert le sub 3 » ne trouve
        # donc structurellement aucun objet et reste `incompris`, cohérent
        # avec le constat de banc (S) que `Sub <n> Assert` échoue en erreur
        # de syntaxe (grammar/modele.yaml, section `asserter`).
        objet = self._objet(toks, pris)
        if objet is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit, groupe ni cue désigné — l'assert exige une cible explicite."])
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro trouvé pour la cible de l'assert."])

        ir = [{"selection": selection, "action": {"type": "asserter"}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : effacer tous les filtres (Clear Filters) ---------------
    def _effacer_filtres(self, toks: list[str], reponses: dict) -> Traduction:
        # Aucune sélection, aucune cible : « Clear Filters » agit globalement.
        ir = [{"action": {"type": "effacer_filtres"}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, set()))

    # -- intention : enregistrer un snapshot ---------------------------------
    def _enregistrer_snapshot(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        i_snap = self._indice_mot(toks, pris, {"snapshot", "snapshots"})
        if i_snap is None:
            return Traduction(statut="incompris", notes=[
                "Aucun snapshot désigné — le mot « snapshot » est requis."])
        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_snap:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de snapshot trouvé après « snapshot »."])
        ir = [{"action": {"type": "record_snapshot", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : rappeler un snapshot ------------------------------------
    def _rappeler_snapshot(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        i_snap = self._indice_mot(toks, pris, {"snapshot", "snapshots"})
        if i_snap is None:
            return Traduction(statut="incompris", notes=[
                "Aucun snapshot désigné — le mot « snapshot » est requis."])
        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_snap:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de snapshot trouvé après « snapshot »."])
        ir = [{"action": {"type": "rappeler_snapshot", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : appliquer une courbe à une cue --------------------------
    def _appliquer_courbe(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()

        # Chaque numéro par son propre marqueur, jamais par position : l'ordre
        # naturel place souvent la courbe avant la cue (« la courbe 4 à la
        # cue 5 »), l'inverse de ce qu'un extracteur positionnel attendrait.
        i_courbe = self._indice_mot(toks, pris, {"courbe", "courbes"})
        if i_courbe is None:
            return Traduction(statut="incompris", notes=[
                "Aucune courbe désignée — le mot « courbe » est requis."])
        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_courbe:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de courbe trouvé après « courbe »."])

        i_cue = self._indice_objet_cle("Cue", toks, pris)
        if i_cue is None:
            return Traduction(statut="incompris", notes=[
                "Aucune cue désignée — le mot « cue » (ou « mémoire ») est requis."])
        numero_cue = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_cue:
                numero_cue, _ = valeur, pris.add(i)
                break
        if numero_cue is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de cue trouvé après « cue »."])

        ir = [{"selection": {"objet": "Cue", "numero": numero_cue},
               "action": {"type": "appliquer_courbe", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : retirer la courbe d'une cue (idiome `Curve At`) --------
    def _retirer_courbe(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        i_cue = self._indice_objet_cle("Cue", toks, pris)
        if i_cue is None:
            return Traduction(statut="incompris", notes=[
                "Aucune cue désignée — le mot « cue » (ou « mémoire ») est requis."])
        numero_cue = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_cue:
                numero_cue, _ = valeur, pris.add(i)
                break
        if numero_cue is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de cue trouvé après « cue »."])
        ir = [{"selection": {"objet": "Cue", "numero": numero_cue},
               "action": {"type": "retirer_courbe"}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    # -- intention : contrôle partitionné, sélectionner/supprimer une partition
    # Volontairement limité à `selectionner_partition`/`supprimer_partition` :
    # les deux seuls actes du manuel §28 sans second numéro implicite (celui
    # d'une partition déjà active) à deviner. `partition_ajouter`/
    # `partition_retirer` (l'idiome `+`/`-`) et `partition_cue_list`
    # (assigner/retirer une partition d'une cue list précise) restent hors
    # périmètre de cette tranche — voir traducteur/README.md. Les deux
    # intentions partagent la même extraction (un numéro après « partition »),
    # seul le type d'action change — factorisé pour ne jamais diverger.
    def _partition(self, toks: list[str], type_action: str) -> Traduction:
        pris: set[int] = set()
        i_partition = self._indice_mot(toks, pris, {"partition", "partitions"})
        if i_partition is None:
            return Traduction(statut="incompris", notes=[
                "Aucune partition désignée — le mot « partition » est requis."])
        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_partition:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de partition trouvé après « partition »."])
        ir = [{"action": {"type": type_action, "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          **self._mots(toks, pris))

    def _selectionner_partition(self, toks: list[str], reponses: dict) -> Traduction:
        return self._partition(toks, "selectionner_partition")

    def _supprimer_partition(self, toks: list[str], reponses: dict) -> Traduction:
        return self._partition(toks, "supprimer_partition")

    # -- intentions du quotidien (tranche 2026-09-03) ----------------------
    #
    # Trois handlers génériques couvrent six intentions, parce que ces
    # commandes n'ont aucune spécificité de traduction : elles désignent une
    # sélection (ou rien), et le mot-clé Eos vient du modèle. Le type d'action
    # est lu dans `self._intention_courante` — le nom de l'intention et celui
    # de l'action du modèle sont volontairement IDENTIQUES pour ces six-là
    # (`plein_feu`, `hors_scene`, `sneak`, `update_cue`, `selection_derniere`,
    # `selection_active`), ce qui évite une table de correspondance qui
    # n'apporterait rien et pourrait dériver.
    #
    # Toute la syntaxe reste au modèle : le générateur sait déjà rendre ces
    # six actions, et il porte seul les particularités — `Out` s'auto-termine
    # donc pas d'`Enter`, `Select Last` porte l'avertissement du corpus #083.
    # Cette tranche n'a ajouté aucune ligne à `grammar/`.

    def _action_sur_selection(self, toks: list[str], reponses: dict) -> Traduction:
        """`<sélection> <mot-clé>` — Full, Out, Sneak."""
        pris: set[int] = set()
        notes: list[str] = []
        objet = self._objet(toks, pris)
        selection = self._selection_de(objet, toks, pris) if objet else None

        if selection is None:
            action_type = self._intention_courante or ""
            if objet is not None:
                return Traduction(statut="incompris", notes=[
                    "Aucun numéro trouvé pour la sélection."])
            if not self._vise_la_selection_courante(toks, pris):
                return Traduction(statut="incompris",
                                  notes=[self._motif_refus_selection(toks, pris)])
            if not self._selection_courante_permise(action_type):
                return Traduction(statut="incompris", notes=[
                    "Aucun circuit ni groupe désigné, et le modèle n'autorise "
                    f"pas « {self.modele_mot_cle()} » sur la sélection en cours."])
            notes.append(self.NOTE_SELECTION_COURANTE)

        action: dict = {"type": self._intention_courante}

        # Une durée dans la phrase doit TOUJOURS ressortir quelque part :
        # produite, ou refusée. La laisser tomber donnerait une commande d'air
        # complet et fausse — « à fond en 20 secondes » rendu `Full Enter`
        # allume à pleine intensité instantanément, ce qui est exactement le
        # contraire de la demande, sans le moindre signal.
        duree = self._duree(toks, pris)
        if duree is not None:
            if self._intention_courante == "sneak":
                action["temps"] = {"valeur": duree}       # `Sneak Time 3`
            elif self._intention_courante == "plein_feu":
                action["sneak"] = duree                   # `Full Sneak 20`
            else:
                # `Out` n'a aucune forme temporisée attestée. La demande a un
                # sens et une traduction — mais par un autre chemin, et c'est
                # à l'utilisateur de le choisir, pas au traducteur de le
                # supposer.
                return Traduction(statut="incompris", notes=[
                    f"Aucune forme temporisée n'est documentée pour "
                    f"« {self.modele_mot_cle()} ». Pour une extinction "
                    f"progressive, passer par un niveau : « à 0 % en "
                    f"{duree} secondes »."])

        etape: dict = {"action": action}
        if selection is not None:
            etape["selection"] = selection
        return Traduction(statut="compris", ir=[etape], notes=notes,
                          **self._mots(toks, pris))

    def _verifier(self, toks: list[str], reponses: dict) -> Traduction:
        """`<sélection> At <niveau> Check` — la revue circuit par circuit.

        Le niveau n'est pas décoratif : `{Check}` amène le premier circuit AU
        niveau donné, puis `Next`/`Last` défilent. Sans niveau, la commande
        n'a pas de sens, donc pas de valeur par défaut inventée ici."""
        pris: set[int] = set()
        objet = self._objet(toks, pris) or "Chan"
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit désigné — préciser les circuits à vérifier."])

        niveau = self._niveau(toks, pris)
        if niveau is None:
            return Traduction(statut="incompris", notes=[
                "Niveau manquant : une vérification amène chaque circuit à un "
                "niveau donné (« vérifie les circuits 1 à 20 à 75 % »)."])
        if "de" in niveau:
            return Traduction(statut="incompris", notes=[
                "Une vérification prend un niveau unique, pas un dégradé : "
                "chaque circuit est amené au même niveau à son tour."])

        # UNE seule ligne : `Chan 1 At 75 Check Enter`. Deux étapes d'IR
        # donneraient deux lignes et deux `Enter`, et le second validerait une
        # commande vide — le drapeau garde la commande entière.
        ir = [{"selection": selection,
               "action": {"type": "intensite", **niveau, "check": True}}]
        return Traduction(statut="compris", ir=ir, **self._mots(toks, pris))

    def _famille_palette(self, toks: list[str], pris: set[int],
                         reponses: dict | None = None):
        """La famille de palettes nommée dans la phrase, ou une question.

        Jamais de famille par défaut. Les quatre familles d'Eos ont des
        mots-clés différents et aucune n'est plus probable qu'une autre quand
        la phrase dit seulement « palettes » : deviner produirait une commande
        parfaitement valide visant la mauvaise famille — erreur silencieuse,
        la pire du catalogue (REGLES_POUR_UI.md règle 4)."""
        reponses = reponses or {}
        choisie = reponses.get("famille_palette")
        if choisie:
            return choisie, None
        # Exact d'abord, flou ensuite — même correctif que `_objet` après le
        # bug « lance l'effet 2 sur le groupe 3 » : un mot de la phrase peut
        # être à distance 1 d'un candidat sans être celui-là, et le premier
        # passage flou gagnerait sur un mot exact placé plus loin.
        for exact in (True, False):
            for i, tok in enumerate(toks):
                if i in pris:
                    continue
                cle = self._familles.get(tok) if exact \
                    else self._resoudre(tok, self._familles)[0]
                if cle:
                    pris.add(i)
                    return cle, None
        modele = self.lex["questions"]["famille_palette"]
        return None, Question(
            id="famille_palette",
            texte=modele["texte"],
            pourquoi=" ".join(modele["pourquoi"].split()),
            options=[Option(cle=o["cle"], libelle=o["libelle"])
                     for o in modele["options"]],
        )

    def _creer_plage(self, toks: list[str], reponses: dict) -> Traduction:
        """`<cible> <a> Thru Thru <b> Enter` — créer toute une plage d'un coup.

        Le double `Thru` n'est pas une insistance : `Thru` désigne ce qui
        existe, `Thru Thru` crée. `Cue 1 Part 1 Thru 4` ne crée que les parts
        1 et 4 (manuel §17 l. 149). Seul un verbe de création dans la phrase
        l'autorise ici.

        Une plage est EXIGÉE : créer une cible unique n'a pas besoin de cette
        commande, et « crée la palette 100 » n'aurait aucune raison de devenir
        `100 Thru Thru 100`."""
        pris: set[int] = set()
        objet = self._objet(toks, pris)
        selection: dict = {"creer": True}

        if objet in (None, "Chan"):
            famille, question = self._famille_palette(toks, pris, reponses)
            if question is not None:
                return Traduction(statut="a_preciser", questions=[question])
            selection["famille"] = famille
        else:
            selection["objet"] = objet

        plage = self._plage(toks, pris)
        if plage is None:
            return Traduction(statut="incompris", notes=[
                "Aucune plage à créer — `Thru Thru` crée une SÉRIE, il faut "
                "donc un début et une fin (« 100 à 150 »)."])
        selection["de"], selection["a"] = plage
        return Traduction(statut="compris", ir=[{"selection": selection}],
                          **self._mots(toks, pris))

    def _copier_libelles(self, toks: list[str], reponses: dict) -> Traduction:
        """`<famille> <plage> Copy To Cue <liste>/<n> {Labels Only}`.

        Renommer des cues d'après les palettes dont elles viennent : le
        manuel §15 autorise la copie de libellés « between any target types
        that can have labels », ce qui couvre palette -> cue alors qu'aucun
        exemple chiffré ne montre ce couple précis.

        La borne haute de la destination n'est jamais demandée ni produite :
        la console la déduit de la longueur de la source (manuel §10 l. 379,
        « You do not have to supply the end value »). En réclamer une
        apprendrait une syntaxe qui n'existe pas."""
        pris: set[int] = set()
        famille, question = self._famille_palette(toks, pris, reponses)
        if question is not None:
            return Traduction(statut="a_preciser", questions=[question])

        plage = self._plage(toks, pris)
        if plage is None:
            nombres = self._nombres(toks, pris)
            if not nombres:
                return Traduction(statut="incompris", notes=[
                    "Aucun numéro de palette — préciser lesquelles copier."])
            i, n = nombres[0]
            pris.add(i)
            plage = (n, n)

        restants = self._nombres(toks, pris)
        if not restants:
            return Traduction(statut="incompris", notes=[
                "Aucune cue de destination — préciser où les libellés vont."])
        i, cible = restants[0]
        pris.add(i)
        destination: dict = {"objet": "Cue", "cible": cible}
        # `Cue 3/1` : une seconde valeur libre est le numéro dans la liste.
        suite = self._nombres(toks, pris)
        if suite:
            j, dedans = suite[0]
            pris.add(j)
            destination = {"objet": "Cue", "liste": cible, "cible": dedans}

        selection: dict = {"famille": famille}
        if plage[0] == plage[1]:
            selection["numero"] = plage[0]
        else:
            selection["de"], selection["a"] = plage

        ir = [{"selection": selection,
               "action": {"type": "copier_vers", "destination": destination},
               "modificateurs": ["Labels Only"]}]
        return Traduction(statut="compris", ir=ir, **self._mots(toks, pris))

    def _action_sans_argument(self, toks: list[str], reponses: dict) -> Traduction:
        """Mot-clé seul, sans sélection — Select Last, Select Active.

        Ces deux-là agissent sur un état de la console (la sélection
        précédente, les channels actifs), pas sur une cible nommée dans la
        phrase : exiger une sélection les rendrait inutilisables.

        Un mot d'objet est donc consommé s'il est là : dans « sélectionne les
        circuits actifs », « circuits » est du remplissage grammatical, pas une
        cible perdue — le signaler enseignerait une limite fausse.

        Un NUMÉRO, en revanche, fait refuser la phrase. « sélectionne les
        circuits 1 à 5 actifs » n'a pas de traduction : la commande ne prend
        pas de sélection, et laisser filer les nombres serait une perte
        silencieuse — d'autant plus invisible que ni `_non_reconnus` ni
        `_ignores` ne rapportent les chiffres."""
        pris: set[int] = set()
        self._objet(toks, pris)
        restants = self._nombres(toks, pris)
        if restants:
            mot = self.modele_mot_cle()
            return Traduction(statut="incompris", notes=[
                f"« {mot} » ne prend pas de sélection : il agit sur un état de "
                f"la console (la sélection précédente, ou les circuits actifs). "
                f"Le numéro {restants[0][1]} n'a donc pas de place ici."])

        ir = [{"action": {"type": self._intention_courante}}]
        return Traduction(statut="compris", ir=ir, **self._mots(toks, pris))

    def modele_mot_cle(self) -> str:
        """Le mot-clé Eos de l'intention en cours, pour un message d'erreur.

        Lu dans le modèle, jamais écrit ici : c'est lui qui possède la
        syntaxe, y compris quand elle ne sert qu'à formuler un refus."""
        if not self._intention_courante:
            return "cette commande"
        try:
            actions = self._generateur_ou_defaut().modele["actions"]
        except Exception:                                     # noqa: BLE001
            # Un message d'erreur ne doit jamais faire échouer une traduction :
            # à défaut du mot-clé Eos, le nom interne reste lisible.
            return self._intention_courante
        return actions.get(self._intention_courante, {}).get(
            "mot_cle", self._intention_courante)

    def _selection_courante_permise(self, type_action: str) -> bool:
        """Le modèle autorise-t-il cette action sans objet nommé ?

        L'assouplissement du 2026-09-09 ne relâche RIEN sur la syntaxe : il
        aligne le traducteur sur ce que `grammar/modele.yaml` déclarait déjà.
        La table `legalite` porte des entrées `objet: selection_courante`
        valides en confiance A, sourcées du manuel §15 (« une sélection déjà
        posée — par Query, Select Active, Select Last ou une étape précédente
        — accepte directement `At` »). Le générateur les rendait sans un seul
        avertissement ; seul le traducteur refusait de les produire.

        L'autorisation est donc LUE, jamais codée en dur ici : le jour où le
        banc réel infirme une de ces cases, c'est le modèle qu'on corrige, et
        le traducteur suit sans être retouché."""
        try:
            legalite = self._generateur_ou_defaut().modele["legalite"]
        except Exception:                                     # noqa: BLE001
            return False
        return any(r.get("objet") == "selection_courante"
                   and r.get("action") == type_action
                   and r.get("valide") == "oui"
                   for r in legalite)

    # Renforcée le 2026-09-09. La première version disait « vérifier ce qui est
    # sélectionné », ce qui laissait croire que le risque était l'inattention
    # de l'opérateur. Le manuel §24 l. 105-109 dit autre chose et de plus
    # grave : en Background, la macro « will run on the MASTER DEVICE » — pas
    # sur l'appareil de l'opérateur. La sélection courante n'est alors PAS la
    # sienne, et la commande peut ne rien faire du tout sans lever d'erreur.
    # Le nom interne du mode Foreground le confirme : `foreground_mode` vaut
    # MACRO_USER.
    NOTE_SELECTION_COURANTE = (
        "Aucune cible nommée : la commande vise la SÉLECTION EN COURS. "
        "Attention si elle part dans une macro en mode Background — celle-ci "
        "s'exécute sur l'appareil maître, pas sur celui de l'opérateur, donc "
        "sur une autre sélection, voire aucune : la commande ne fera alors "
        "rien, en silence. Poser la sélection dans la macro (« sélectionne le "
        "manuel », « sélectionne les circuits actifs ») lève le doute."
    )

    def _motif_refus_selection(self, toks: list[str], pris: set[int]) -> str:
        """Pourquoi le repli sur la sélection courante est refusé, en clair.

        Trois blocages, trois messages. Répondre « aucun numéro trouvé » quand
        le vrai obstacle est un mot inconnu apprend à l'utilisateur une limite
        qui n'existe pas, et le pousse à retirer des mots qui marchent — le
        même défaut que le bug de `_non_reconnus` corrigé le 2026-08-28."""
        inconnus = self._non_reconnus(toks, set())
        if inconnus:
            mots = ", ".join(f"« {m} »" for m in inconnus[:3])
            return (f"Sans cible nommée, je n'agis sur la sélection en cours "
                    f"que si je comprends toute la phrase — or {mots} "
                    f"m'échappe. Nommer les circuits lèverait le doute.")
        return "Aucun numéro trouvé pour la sélection."

    def _vise_la_selection_courante(self, toks: list[str], pris: set[int]) -> bool:
        """Phrase sans cible : commande implicite, ou phrase incomplète ?

        Le garde-fou tient en une ligne et il est indispensable. « monte à
        fond en 20 secondes » ne nomme aucun objet : l'utilisateur parle de ce
        qu'il a sous la main, comme le fait n'importe quel bouton de magic
        sheet. « les circuits à 50 % » nomme un objet mais aucun numéro :
        c'est une phrase à laquelle il manque un morceau, pas un ordre sur la
        sélection courante.

        Sans cette distinction, une phrase dont le numéro a été perdu — faute
        de frappe, mot avalé par la dictée — deviendrait silencieusement un
        ordre sur une sélection inconnue. C'est précisément la panne que
        REGLES_POUR_UI.md règle 4 désigne comme la plus grave du projet :
        la console accepte, et fait autre chose.

        Les CIBLES comptent autant que les objets, et l'oublier a coûté une
        régression le 2026-09-09 : « sub 3 à 50 % » ne contient aucun mot de
        `objets` (qui n'a que Chan, Group, Cue), donc la phrase basculait sur
        la sélection courante et rendait `At 50 Enter` — une commande visant
        des circuits quelconques au lieu du submaster demandé, sans aucune
        erreur.

        NOTE 2026-09-14 : ce verrou était alors justifié par « le banc a
        tranché Sub + intensite INVALIDE ». C'est FAUX depuis le 2026-09-13,
        où le banc a tranché l'inverse (valide, confiance S), et
        `_regler_intensite` a désormais une branche Sub explicite. Le verrou
        reste néanmoins nécessaire, pour sa raison propre et suffisante : la
        phrase DÉSIGNE une cible, donc se replier sur « ce qui est
        sélectionné » viserait autre chose que ce qui est demandé. Un mot qui
        nomme une cible, quelle que soit sa famille, interdit le repli — la
        légalité de l'action sur cette cible est une question séparée, et elle
        se lit dans le modèle."""
        essai: set[int] = set(pris)
        if self._objet(toks, essai) is not None:
            return False
        if any(self._resoudre(tok, self._objets_cible)[0]
               for i, tok in enumerate(toks) if i not in pris):
            return False

        # DERNIER verrou, et le plus important : pas un seul mot inconnu dans
        # la phrase. Viser la sélection courante, c'est agir sans cible
        # nommée — on ne peut se le permettre qu'en ayant compris la phrase
        # ENTIÈRE. Un mot inconnu veut dire qu'elle parle de quelque chose que
        # le lexique ne connaît pas encore ; produire quand même une commande
        # sur « ce qui est sélectionné » invente une réponse à une question
        # qu'on n'a pas comprise.
        #
        # Deux cas réels, trouvés au banc de rétro-traduction le jour même de
        # l'assouplissement, l'un et l'autre silencieux :
        #   « passe le fondu de couleur à fond »  ->  `Full Enter`
        #   « vérifie les adresses à 75 % »       ->  `At 75 Enter`
        # La première envoie tout le plateau à pleine intensité pour une
        # demande qui ne parlait que de fondu de couleur. Avant
        # l'assouplissement, le mot d'objet manquant servait de filet par
        # accident ; ce verrou-ci le remplace exprès.
        return not self._non_reconnus(toks, set())

    def _update_cue(self, toks: list[str], reponses: dict) -> Traduction:
        """`Update Cue <n>` — la cible est toujours explicite.

        Jamais d'`Update` nu : le modèle porte l'avertissement sourcé qu'une
        cible implicite dépend de préférences persistantes entre sessions
        ({Make Absolute}, {Break Nested}). Une phrase sans numéro reste donc
        `incompris` plutôt que de viser « la cue courante »."""
        pris: set[int] = set()
        i_cue = self._indice_objet_cle("Cue", toks, pris)
        if i_cue is None:
            return Traduction(statut="incompris", notes=[
                "Aucune cue désignée — le mot « cue » est requis."])

        cible = None
        for i, valeur in self._nombres(toks, pris):
            if i > i_cue:
                cible, _ = valeur, pris.add(i)
                break
        if cible is None:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de cue trouvé — un Update sans cible explicite "
                "dépend d'un état de console que le traducteur ne peut pas lire."])

        ir = [{"action": {"type": "update_cue", "cible": cible}}]
        return Traduction(statut="compris", ir=ir, **self._mots(toks, pris))

    # -- petits extracteurs partagés ---------------------------------------
    def _indice_mot(self, toks: list[str], pris: set[int],
                    mots: set[str]) -> int | None:
        """Index du premier jeton libre appartenant littéralement à `mots`,
        marqué pris. Sert aux mots-clés qui ne sont ni un objet (`self._objets`)
        ni une couleur ni une cible de cue — juste un déclencheur littéral
        (« effet », « tous », direction d'un bump…)."""
        for i, tok in enumerate(toks):
            if i in pris:
                continue
            if tok in mots:
                pris.add(i)
                return i
        return None

    def _indice_objet_cle(self, cle_cible: str, toks: list[str], pris: set[int],
                          index: dict[str, str] | None = None) -> int | None:
        """Comme `_objet`, mais cherche UN objet précis (ex. `Cue`) et rend son
        index — nécessaire quand la phrase distingue par position deux jeux de
        nombres (la cible d'un `Record Cue`, et la sélection qui l'enregistre).

        `index` permet de chercher dans un autre lexique que `self._objets`
        (ex. `self._objets_cible` pour `Sub`, qui n'est délibérément pas une
        cible de sélection générique — voir le commentaire dans lexique.yaml)."""
        index = self._objets if index is None else index
        for i, tok in enumerate(toks):
            if i in pris:
                continue
            cle, _ = self._resoudre(tok, index)
            if cle == cle_cible:
                pris.add(i)
                return i
        return None

    def _objet(self, toks: list[str], pris: set[int]) -> str | None:
        """Le premier mot de la phrase qui désigne un objet (Chan, Group, Cue).

        **Correspondance exacte d'abord, tolérance aux fautes seulement en
        second passage** — corrigé le 2026-08-28, sur un cas grave. Un seul
        balayage tolérant retenait le PREMIER mot approximativement proche,
        verbes compris : dans « lance l'effet 2 sur le groupe 3 », « lance »
        tombe à distance 2 de « lampe » (alias de Chan) et gagnait la place,
        avant même que « groupe » soit examiné. Résultat : `Chan 3 Effect 2`
        au lieu de `Group 3` — le bon numéro sur le mauvais objet, statut
        `compris`, aucun avertissement, macro d'apparence impeccable.

        C'est la troisième fois que la tolérance aux fautes change un SENS au
        lieu de corriger une frappe (voir « chang »/« chan » et
        « groupe »/« rouge » dans le README) : la parade est toujours la même
        — ne l'autoriser que là où rien d'exact ne se présente."""
        for exact in (True, False):
            for i, tok in enumerate(toks):
                if i in pris:
                    continue
                if exact:
                    cle = self._objets.get(tok)
                else:
                    cle, _ = self._resoudre(tok, self._objets)
                if cle:
                    pris.add(i)
                    return cle
        return None

    def _nuancier(self, toks: list[str], pris: set[int]) -> tuple[int | None, int | None]:
        for i, tok in enumerate(toks):
            if i in pris:
                continue
            cle, _ = self._resoudre(tok, self._nuanciers)
            if cle:
                pris.add(i)
                return self.lex["nuanciers"][cle]["numero"], i
        return None, None

    def _selection_de(self, objet: str, toks: list[str], pris: set[int]) -> dict | None:
        bornes = self._plage(toks, pris)
        if bornes:
            return {"objet": objet, "de": bornes[0], "a": bornes[1]}
        libres = self._nombres(toks, pris)
        if libres:
            i, valeur = libres[0]
            pris.add(i)
            return {"objet": objet, "numero": valeur}
        return None

    # -- corriger une IR déjà produite, en langage naturel -------------------
    def corriger(self, ir: list[dict], instruction: str) -> Traduction:
        """« remplace X par Y » (ou « change X en Y ») appliqué à une IR déjà
        produite par `traduire()` — jamais une retraduction depuis zéro.
        Pensé pour l'usage « à la manière d'un LLM » : plutôt que de taper sur
        un champ dans l'interface, on écrit la correction en une phrase
        courte, adressée à la dernière macro proposée.

        Portée volontairement restreinte à deux cas, chacun sans ambiguïté
        possible :

          - **objet de sélection, Chan <-> Group uniquement** — les deux
            seuls objets génériques de ce traducteur (voir
            `traducteur/README.md`). Cue/Sub/Preset ne sont jamais des cibles
            de remplacement : les proposer inviterait à deviner une intention
            entièrement différente plutôt qu'une simple retouche — ce ne
            serait plus une correction, ce serait une nouvelle traduction
            déguisée.
          - **un numéro déjà présent dans l'IR**, seulement s'il apparaît à
            un seul endroit (sélection ou cible d'action). S'il apparaît à
            plusieurs endroits, corriger le mauvais serait pire que ne rien
            corriger — la traduction reste `incompris` plutôt que de choisir.

        Ne mute jamais l'IR reçue : travaille sur une copie, pour que
        l'appelant garde l'original si la correction échoue.
        """
        if not ir or not isinstance(ir, list) or not ir[0]:
            return Traduction(statut="incompris", notes=[
                "Aucune macro en cours à corriger."])
        etape = copy.deepcopy(ir[0])

        toks = tokeniser(normaliser(instruction, self._ponctuation))
        i_sep = next((i for i, tok in enumerate(toks) if tok in ("par", "en")), None)
        if i_sep is None:
            return Traduction(statut="incompris", notes=[
                "Aucun « par » ou « en » trouvé — dire par exemple « remplace groupe par circuit »."])

        verbes = {"remplace", "remplacer", "change", "changer"}
        gauche = [t for t in toks[:i_sep] if t not in verbes and t not in self._outils]
        droite = [t for t in toks[i_sep + 1:] if t not in self._outils]
        if not gauche or not droite:
            return Traduction(statut="incompris", notes=[
                "Rien à corriger de part et d'autre de « par »/« en »."])

        # -- cas 1 : objet de sélection (Chan <-> Group uniquement) ---------
        OBJETS_REMPLACABLES = {"Chan", "Group"}
        cle_gauche, _ = self._resoudre(gauche[0], self._objets)
        cle_droite, _ = self._resoudre(droite[0], self._objets)
        if cle_gauche in OBJETS_REMPLACABLES or cle_droite in OBJETS_REMPLACABLES:
            if cle_droite not in OBJETS_REMPLACABLES:
                return Traduction(statut="incompris", notes=[
                    f"« {droite[0]} » n'est pas une cible de remplacement prise en charge "
                    "(seuls circuit et groupe le sont)."])
            selection = etape.get("selection")
            objet_actuel = selection.get("objet") if selection else None
            if not selection or objet_actuel != cle_gauche:
                return Traduction(statut="incompris", notes=[
                    f"La macro actuelle ne contient pas « {gauche[0]} »"
                    + (f" — elle contient « {objet_actuel} »." if objet_actuel else ".")])
            selection["objet"] = cle_droite
            return Traduction(statut="compris", ir=[etape], intention="corriger")

        # -- cas 2 : un numéro déjà présent, à un seul endroit ---------------
        if gauche[0].isdigit() and droite[0].isdigit():
            valeur_gauche, valeur_droite = int(gauche[0]), int(droite[0])
            candidats = []
            for cle_conteneur in ("selection", "action"):
                conteneur = etape.get(cle_conteneur)
                if not isinstance(conteneur, dict):
                    continue
                for cle, val in conteneur.items():
                    if isinstance(val, int) and not isinstance(val, bool) and val == valeur_gauche:
                        candidats.append((conteneur, cle))
            if not candidats:
                return Traduction(statut="incompris", notes=[
                    f"Le numéro {valeur_gauche} n'apparaît nulle part dans cette macro."])
            if len(candidats) > 1:
                return Traduction(statut="incompris", notes=[
                    f"Le numéro {valeur_gauche} apparaît à plusieurs endroits de cette macro — "
                    "trop ambigu pour savoir lequel corriger."])
            conteneur, cle = candidats[0]
            conteneur[cle] = valeur_droite
            return Traduction(statut="compris", ir=[etape], intention="corriger")

        return Traduction(statut="incompris", notes=[
            f"« {' '.join(gauche)} » n'est pas reconnu comme quelque chose à remplacer "
            "(objet de sélection circuit/groupe, ou un numéro déjà présent dans la macro)."])

    # -- interpréter une réponse LLM (moteur flou) ---------------------------
    def interpreter_flou(self, phrase: str, sortie_llm: dict | None,
                         reponses: dict | None = None) -> Traduction:
        """Utilise l'interprétation d'un LLM externe pour compléter une
        traduction que le lexique seul n'a pas pu terminer.

        Ne touche JAMAIS le réseau : `sortie_llm` est un dict déjà produit
        (par un appel LLM réel côté navigateur) et déjà validé contre le
        vocabulaire fermé exporté par `traducteur/build_vocabulaire_llm.py`
        — c'est ce qui rend cette méthode testable de façon aussi
        déterministe que le reste du traducteur, avec un `sortie_llm` écrit
        à la main dans les tests.

        Le lexique déterministe (`traduire()`) reste la seule autorité :

          - un résultat déjà `compris` par le lexique seul n'est **jamais**
            remplacé par l'avis du LLM — un mot littéral reconnu prime
            toujours sur une supposition.
          - une question déjà posée (`a_preciser`) peut être complétée par
            une réponse du LLM, à la STRICTE condition qu'elle corresponde à
            l'une des `Option.cle` déjà proposées par cette question — donc
            déjà membre du vocabulaire fermé du lexique. Une valeur hors de
            ce vocabulaire est silencieusement ignorée pour ce champ (jamais
            acceptée), et la question reste posée telle quelle.
          - `sortie_llm["reponses"]` est un dict `{question_id: cle}` (une
            seule proposition confiante) ou `{question_id: [cle, ...]}`
            (plusieurs candidats de confiance comparable — "propose
            plusieurs choses"). Plusieurs candidats valides réduisent la
            question à ces seules options plutôt que de choisir à la place
            de l'utilisateur ; c'est le même mécanisme que la question
            `couleur_ambigue` déjà posée par le lexique seul, jamais une
            nouvelle forme d'UI.
          - un `incompris` complet (aucune intention reconnue par les mots
            littéraux de la phrase) N'EST PAS rescapé ici : router vers une
            intention sur la seule foi du LLM demanderait de modifier
            `_intention()` elle-même — hors périmètre de cette tranche
            (voir PLANNING.md, moteur flou).
        """
        base = self.traduire(phrase, reponses=reponses)
        if base.statut != "a_preciser" or not base.questions:
            return base

        reponses_llm = (sortie_llm or {}).get("reponses") or {}
        reponses_completees = dict(reponses or {})
        questions_restantes: list[Question] = []
        toutes_resolues = True

        for question in base.questions:
            cles_valides = {o.cle for o in question.options}
            propose = reponses_llm.get(question.id)
            candidats = propose if isinstance(propose, list) else ([propose] if propose else [])
            candidats_valides = [c for c in candidats if c in cles_valides]

            if len(candidats_valides) == 1:
                reponses_completees[question.id] = candidats_valides[0]
            elif len(candidats_valides) > 1:
                options_filtrees = [o for o in question.options if o.cle in candidats_valides]
                questions_restantes.append(Question(
                    id=question.id, texte=question.texte, pourquoi=question.pourquoi,
                    options=options_filtrees, contexte=question.contexte))
                toutes_resolues = False
            else:
                questions_restantes.append(question)
                toutes_resolues = False

        if toutes_resolues:
            return self.traduire(phrase, reponses=reponses_completees)
        if questions_restantes != base.questions:
            # Au moins une question a été réduite à des candidats validés
            # par le LLM, même si elle reste ouverte — renvoyer la version
            # affinée plutôt que la question d'origine, non filtrée.
            return Traduction(statut="a_preciser", questions=questions_restantes,
                              intention=base.intention, notes=base.notes,
                              non_reconnus=base.non_reconnus,
                              ignores=base.ignores)
        return base

    # -- confort : traduire puis rendre ------------------------------------
    def rendre(self, traduction: Traduction, **kwargs):
        """Passe l'IR au générateur. Ne court-circuite rien : les
        avertissements du modèle sur les zones non validées remontent tels
        quels, en plus des notes du traducteur.

        Réutilise le générateur donné à la construction s'il y en a un —
        évite de relire `modele.yaml` depuis le disque à chaque traduction,
        et c'est obligatoire en Pyodide, où il n'y a rien à relire."""
        if not traduction.compris:
            raise ValueError("seule une traduction comprise peut être rendue")
        return self._generateur_ou_defaut().rendre(traduction.ir, **kwargs)

    def _generateur_ou_defaut(self):
        """Le générateur injecté, ou un chargé à la demande et mémorisé.

        Mémorisé pour ne pas relire `modele.yaml` à chaque appel : depuis que
        `modele_mot_cle` s'en sert aussi (pour formuler un refus avec le vrai
        mot-clé Eos plutôt qu'un nom interne), l'accès n'est plus limité au
        rendu d'une traduction comprise."""
        if self._generateur is None:
            from generateur import Generateur
            self._generateur = Generateur()
        return self._generateur


def _demo() -> None:
    t = Traducteur()
    phrase = ("créer les palette de couleur 1 a 6 avec les références lee, "
              "chang froid r v b j")
    print(f"« {phrase} »\n")

    trad = t.traduire(phrase)
    print(f"statut : {trad.statut}")
    for q in trad.questions:
        print(f"  ? {q.texte}")
        for o in q.options:
            print(f"      - {o.libelle}")

    trad = t.traduire(phrase, reponses={"portee_enregistrement": "par_type"})
    print(f"\nstatut : {trad.statut}")
    for note in trad.notes:
        print(f"  · {note}")
    print()
    print(t.rendre(trad).commande)


if __name__ == "__main__":
    _demo()

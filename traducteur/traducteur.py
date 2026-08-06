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

import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml

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
class Traduction:
    statut: str                    # compris | a_preciser | incompris
    ir: list[dict] = field(default_factory=list)
    questions: list[Question] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    non_reconnus: list[str] = field(default_factory=list)
    intention: str | None = None

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


# --------------------------------------------------------------------------
class Traducteur:
    def __init__(self) -> None:
        self.lex = yaml.safe_load((RACINE / "lexique.yaml").read_text(encoding="utf-8"))
        self._ponctuation = self.lex["normalisation"]["ponctuation_ignoree"]
        self._outils = set(self.lex["mots_outils"])
        self._mots_plage = set(self.lex["plage"]["mots"])
        self._objets = self._indexer(self.lex["objets"])
        self._nuanciers = self._indexer(self.lex["nuanciers"])
        self._couleurs = self._indexer(self.lex["couleurs"])
        self._cue_cibles = self._indexer(self.lex["cue_cibles"])

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
        """`10 a 20`, `10 thru 20`, `10-20` → (10, 20). Marque les jetons pris."""
        for i in range(len(toks) - 2):
            if i in pris or i + 2 in pris:
                continue
            if toks[i].isdigit() and toks[i + 1] in self._mots_plage and toks[i + 2].isdigit():
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
                     questions: list[Question], notes: list[str]) -> list[dict] | None:
        """Résout les mots de couleur restants, dans l'ordre de la phrase.

        Retourne None si une couleur est ambiguë — dans ce cas la question est
        déjà empilée. Une teinte devinée serait le pire des échecs : macro
        valide, console d'accord, mauvaise couleur sur scène.
        """
        trouvees: list[dict] = []
        for i, tok in enumerate(toks):
            if i in pris or tok.isdigit() or tok in self._outils:
                continue
            cle, exaequo = self._resoudre(tok, self._couleurs)
            if cle is None:
                if exaequo:
                    questions.append(self._question_couleur(tok, exaequo))
                    return None
                continue
            pris.add(i)
            corps = self.lex["couleurs"][cle]
            if corps.get("ambigu"):
                questions.append(self._question_couleur_ambigue(cle, corps))
                return None
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
    def _intention(self, toks: list[str]) -> str | None:
        """Première intention dont TOUS les groupes de déclencheurs sont servis.

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
        """Traduit une phrase. `reponses` porte les questions déjà tranchées.

        Le même appel, relancé avec la réponse, doit reprendre où il s'était
        arrêté : c'est ce qui permet à l'app de poser une question puis de
        continuer sans redemander le reste.
        """
        reponses = reponses or {}
        toks = tokeniser(normaliser(phrase, self._ponctuation))
        intention = self._intention(toks)

        if intention is None:
            return Traduction(statut="incompris",
                              non_reconnus=self._non_reconnus(toks, set()),
                              notes=["Aucune intention reconnue dans la phrase."])

        handler = {
            "creer_palettes_couleur": self._creer_palettes_couleur,
            "colorer_selection": self._colorer_selection,
            "regler_intensite": self._regler_intensite,
            "enregistrer_cue": self._enregistrer_cue,
            "aller_a_cue": self._aller_a_cue,
        }[intention]
        trad = handler(toks, reponses)
        trad.intention = intention
        return trad

    def _non_reconnus(self, toks: list[str], pris: set[int]) -> list[str]:
        """Mots qui ne sont ni consommés, ni outils, ni déclencheurs connus."""
        connus = {m for corps in self.lex["intentions"].values()
                  for mots in corps["declencheurs"].values() for m in mots}
        connus |= self._outils | self._mots_plage | {"%"}
        return [t for i, t in enumerate(toks)
                if i not in pris and not t.isdigit() and t not in connus]

    # -- intention : créer des palettes de couleur -------------------------
    def _creer_palettes_couleur(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        notes: list[str] = []
        questions: list[Question] = []

        # Le nuancier avant les cibles : « lee » précède souvent le numéro de
        # gel, qu'il ne faut pas confondre avec un numéro de palette.
        nuancier, i_nuancier = self._nuancier(toks, pris)
        if nuancier is None:
            nuancier = self.lex["nuanciers"]["lee"]["numero"]
            notes.append("Nuancier non précisé — Lee retenu (seul nuancier au lexique).")

        cibles = self._cibles(toks, pris)
        couleurs = self._couleurs_de(toks, pris, questions, notes)

        if couleurs is None:                       # une couleur ambiguë
            return Traduction(statut="a_preciser", questions=questions, notes=notes)
        if not cibles:
            return Traduction(statut="incompris", notes=notes + [
                "Aucun numéro de palette trouvé dans la phrase."])
        if not couleurs:
            return Traduction(statut="incompris",
                              non_reconnus=self._non_reconnus(toks, pris),
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

        selection = None
        options: list[str] = []
        if isinstance(portee, dict):
            cle, valeur = portee.get("cle"), portee.get("valeur")
        else:
            cle, valeur = portee, None
        if cle == "par_type":
            options = ["{By Type}"]
        elif cle == "selection":
            selection = self._selection_depuis(valeur)
            if selection is None:
                return Traduction(statut="a_preciser", notes=notes,
                                  questions=[self._question_portee()])
        else:
            return Traduction(statut="a_preciser", notes=notes,
                              questions=[self._question_portee()])

        ir: list[dict] = []
        for cible, couleur in zip(cibles, couleurs):
            etape = {"action": {"type": "couleur_gel",
                                "nuancier": nuancier, "teinte": couleur["gel"]}}
            if selection:
                etape["selection"] = dict(selection)
            ir.append(etape)
            record = {"type": "record_palette", "famille": "Color Palette",
                      "cible": cible, "label": couleur["nom"].capitalize()}
            if options:
                record["options"] = list(options)
            ir.append({"action": record})

        # Les teintes qui portent déjà une note détaillée (une décision du
        # projet à expliquer) ne sont pas re-listées : elles sont plus haut.
        for couleur in couleurs:
            if not couleur["detaillee"]:
                notes.append(f"{couleur['nom']} → Lee {couleur['gel']:03d} "
                             f"({couleur['nom_lee']})")
        return Traduction(statut="compris", ir=ir, notes=notes,
                          non_reconnus=self._non_reconnus(toks, pris))

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
        """La réponse « circuits précis » peut arriver en dict ou en texte."""
        if isinstance(valeur, dict):
            return valeur
        if isinstance(valeur, int):
            return {"objet": "Chan", "numero": valeur}
        if isinstance(valeur, str) and valeur.strip():
            toks = tokeniser(normaliser(valeur, self._ponctuation))
            pris: set[int] = set()
            bornes = self._plage(toks, pris)
            if bornes:
                return {"objet": "Chan", "de": bornes[0], "a": bornes[1]}
            nombres = self._nombres(toks, pris)
            if nombres:
                return {"objet": "Chan", "numero": nombres[0][1]}
        return None

    # -- intention : colorer une sélection ---------------------------------
    def _colorer_selection(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        notes: list[str] = []
        questions: list[Question] = []

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
            couleurs = self._couleurs_de(toks, pris, questions, notes)
            if couleurs is None:
                return Traduction(statut="a_preciser", questions=questions, notes=notes)
            if not couleurs:
                return Traduction(statut="incompris",
                                  non_reconnus=self._non_reconnus(toks, pris),
                                  notes=notes + ["Aucune couleur reconnue."])
            teinte = couleurs[0]["gel"]
            notes.append(f"{couleurs[0]['nom']} → Lee {teinte:03d} "
                         f"({couleurs[0]['nom_lee']})")

        if nuancier is None:
            nuancier = self.lex["nuanciers"]["lee"]["numero"]
            notes.append("Nuancier non précisé — Lee retenu (seul nuancier au lexique).")

        ir = [{"selection": selection,
               "action": {"type": "couleur_gel", "nuancier": nuancier, "teinte": teinte}}]
        return Traduction(statut="compris", ir=ir, notes=notes,
                          non_reconnus=self._non_reconnus(toks, pris))

    # -- intention : régler une intensité ----------------------------------
    def _regler_intensite(self, toks: list[str], reponses: dict) -> Traduction:
        pris: set[int] = set()
        notes: list[str] = []

        objet = self._objet(toks, pris) or "Chan"

        # La sélection SE LIT EN PREMIER, et l'ordre compte. « circuits 1 à 5
        # à 50 % » contient deux fois le mot « à » : la première plage désigne
        # les circuits, ce qui reste désigne le niveau. Lire le niveau d'abord
        # ferait comprendre « dégradé de 5 à 50 » sur les circuits 1 seul.
        selection = self._selection_de(objet, toks, pris)
        if selection is None:
            return Traduction(statut="incompris", notes=[
                "Aucun circuit ni groupe désigné dans la phrase."])

        # Le niveau se lit au marqueur, jamais par position : c'est le nombre
        # qui précède `%`, ou celui qui suit « intensité » / « niveau ».
        niveau = self._niveau(toks, pris)
        if niveau is None:
            return Traduction(statut="incompris", notes=[
                "Niveau introuvable — préciser « % », « pourcent », "
                "« intensité » ou « niveau »."])

        action = {"type": "intensite"}
        action.update(niveau)
        ir = [{"selection": selection, "action": action}]
        return Traduction(statut="compris", ir=ir, notes=notes,
                          non_reconnus=self._non_reconnus(toks, pris))

    def _niveau(self, toks: list[str], pris: set[int]) -> dict | None:
        """`50 %` → {valeur: 50}. `10 a 50 %` → dégradé {de: 10, a: 50}."""
        for i, tok in enumerate(toks):
            if tok not in ("%", "pourcent", "intensite", "niveau"):
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
                          non_reconnus=self._non_reconnus(toks, pris))

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
                ir = [{"action": {"type": "go_to_cue", "mot": cle}}]
                return Traduction(statut="compris", ir=ir,
                                  non_reconnus=self._non_reconnus(toks, pris))

        libres = self._nombres(toks, pris)
        if not libres:
            return Traduction(statut="incompris", notes=[
                "Aucun numéro de cue ni destination reconnue "
                "(noir, suivante, précédente, home)."])
        i, cible = libres[0]
        pris.add(i)
        ir = [{"action": {"type": "go_to_cue", "cible": cible}}]
        return Traduction(statut="compris", ir=ir,
                          non_reconnus=self._non_reconnus(toks, pris))

    # -- petits extracteurs partagés ---------------------------------------
    def _indice_objet_cle(self, cle_cible: str, toks: list[str], pris: set[int]) -> int | None:
        """Comme `_objet`, mais cherche UN objet précis (ex. `Cue`) et rend son
        index — nécessaire quand la phrase distingue par position deux jeux de
        nombres (la cible d'un `Record Cue`, et la sélection qui l'enregistre)."""
        for i, tok in enumerate(toks):
            if i in pris:
                continue
            cle, _ = self._resoudre(tok, self._objets)
            if cle == cle_cible:
                pris.add(i)
                return i
        return None

    def _objet(self, toks: list[str], pris: set[int]) -> str | None:
        for i, tok in enumerate(toks):
            if i in pris:
                continue
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

    # -- confort : traduire puis rendre ------------------------------------
    def rendre(self, traduction: Traduction, **kwargs):
        """Passe l'IR au générateur. Ne court-circuite rien : les
        avertissements du modèle sur les zones non validées remontent tels
        quels, en plus des notes du traducteur."""
        from generateur import Generateur
        if not traduction.compris:
            raise ValueError("seule une traduction comprise peut être rendue")
        return Generateur().rendre(traduction.ir, **kwargs)


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

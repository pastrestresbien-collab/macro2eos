#!/usr/bin/env python3
"""Génère une commande Eos à partir d'une représentation intermédiaire (IR).

Le traducteur NL produira l'IR ; ce module la transforme en chaîne de commande
et signale les zones non validées au banc réel.

    >>> g = Generateur()
    >>> r = g.rendre([{"selection": {"objet": "Chan", "de": 10, "a": 20},
    ...                "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}}])
    >>> r.commande
    'Chan 10 Thru 20 Color 3/195 Enter'

Deux sorties distinctes, à ne pas confondre :
  - `rendre()`      → lignes de ligne de commande, injectables par `/eos/newcmd`
  - `rendre_macro()` → contenu de macro, qui s'enveloppe (`Learn`/éditeur) et
                       obéit à des règles propres (chaînage, modes, boucles)

Règle non négociable : une combinaison marquée `inconnu` dans le modèle produit
un avertissement, jamais un silence. Une macro générée sans avertissement n'est
pas pour autant validée — seul un banc réel tranche (voir PLANNING.md).

Deuxième règle, structurelle : on assemble des TOKENS, jamais du texte. Une
commande construite par concaténation (`"Go_To_Cue_" + str(n)`) tronque les
décimales sur console réelle (corpus #060).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

RACINE = Path(__file__).parent

# Mots-clés de destination acceptés par Go To Cue à la place d'un numéro.
CIBLES_SYMBOLIQUES = {"Out", "Next", "Last", "Home"}


@dataclass
class Resultat:
    commande: str
    avertissements: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def sur(self) -> bool:
        """Vrai si aucune zone d'ombre n'a été traversée."""
        return not self.avertissements


@dataclass
class Message:
    """Un paquet OSC prêt à partir."""
    adresse: str
    arguments: list = field(default_factory=list)

    def __str__(self) -> str:
        if not self.arguments:
            return self.adresse
        return f"{self.adresse} {self.arguments!r}"


@dataclass
class ResultatOSC:
    messages: list[Message] = field(default_factory=list)
    avertissements: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def sur(self) -> bool:
        return not self.avertissements


class Generateur:
    def __init__(self) -> None:
        self.modele = yaml.safe_load((RACINE / "modele.yaml").read_text(encoding="utf-8"))
        self._legalite = self.modele["legalite"]
        self._thru = self.modele["operateurs"]["plage"]["symbole"]
        self._plus = self.modele["operateurs"]["ajout"]["symbole"]

    # -- vérification -------------------------------------------------------
    def _regle(self, objet: str | None, action: str) -> dict | None:
        for r in self._legalite:
            if r.get("objet") == objet and r.get("action") == action:
                return r
        return None

    def _verifier(self, objet: str | None, action: str, avert: list[str]) -> None:
        regle = self._regle(objet, action)
        if regle is None:
            avert.append(
                f"combinaison `{objet or 'selection'}` + `{action}` absente du modèle — "
                f"non vérifiable"
            )
        elif regle["valide"] == "inconnu":
            avert.append(
                f"`{objet}` + `{action}` non tranché (PLANNING #{regle['backlog']})"
            )
        elif regle["valide"] == "non":
            avert.append(f"`{objet}` + `{action}` invalide selon le modèle")

    def _verifier_combinaison(self, cle: str, avert: list[str]) -> None:
        for r in self._legalite:
            if r.get("combinaison", "").startswith(cle) and r["valide"] == "inconnu":
                avert.append(f"{r['combinaison']} non tranché (PLANNING #{r['backlog']})")

    def _backlog_de(self, cle: str) -> int | None:
        for r in self._legalite:
            if r.get("combinaison", "").startswith(cle):
                return r.get("backlog")
        return None

    def _verifier_label(self, texte: object, avert: list[str]) -> None:
        """Un libellé multi-mots passe par le clavier virtuel de la console, dont
        le comportement avec espaces et tirets n'a jamais été observé."""
        if " " not in str(texte):
            return
        backlog = self._backlog_de("Record Color Palette <n> Label")
        avert.append(
            f"libellé multi-mots « {texte} » — comportement du clavier virtuel "
            f"non observé (PLANNING #{backlog})"
        )

    # -- rendu : sélection --------------------------------------------------
    def _rendre_sous_groupes(self, blocs: list) -> str:
        """`( 1 Thru 4 ) ( 5 Thru 8 )` — chaque parenthèse comptera pour UN seul
        channel dans un Fan, un effet, ou un parcours Next/Last."""
        ouvre, ferme = self.modele["operateurs"]["sous_groupe"]["symbole"]
        morceaux: list[str] = []
        for bloc in blocs:
            morceaux.append(ouvre)
            if isinstance(bloc, (list, tuple)) and len(bloc) == 2:
                morceaux += [str(bloc[0]), self._thru, str(bloc[1])]
            else:
                morceaux.append(str(bloc))
            morceaux.append(ferme)
        return " ".join(morceaux)

    def _rendre_selection(self, sel: dict, avert: list[str]) -> str:
        # une sélection en sous-groupes ne porte pas de mot-clé d'objet :
        # ce sont des channels, entre parenthèses (manuel §7)
        if "sous_groupes" in sel:
            return self._rendre_sous_groupes(sel["sous_groupes"])

        objet = sel["objet"]
        mot = self.modele["objets"][objet]["mot_cle"]
        thru, plus = self._thru, self._plus

        # préfixe de cue list : `Cue 2/5`
        prefixe = f"{sel['liste']}/" if "liste" in sel else ""

        if "de" in sel:
            morceaux = [mot, f"{prefixe}{sel['de']}", thru, str(sel["a"])]
        elif "mot" in sel:                       # Out / Next / Last / Home
            morceaux = [mot, f"{prefixe}{sel['mot']}"]
        elif "numero" in sel:
            morceaux = [mot, f"{prefixe}{sel['numero']}"]
        elif prefixe:
            # `Cue 2/` — la liste entière, sans numéro derrière le slash.
            # C'est ce qui distingue un assert de liste d'un assert de cue.
            morceaux = [mot, prefixe]
        else:
            raise ValueError(f"sélection sans cible : {sel!r}")

        # `Group 7 + 5` — ajouter une cible de MÊME type, forme documentée A
        # (manuel §7). À ne pas confondre avec `plus_plage`, qui mélange les
        # types et reste non tranché.
        if "plus" in sel:
            ajouts = sel["plus"] if isinstance(sel["plus"], (list, tuple)) else [sel["plus"]]
            for n in ajouts:
                morceaux += [plus, str(n)]

        if "plus_plage" in sel:
            debut, fin = sel["plus_plage"]
            morceaux += [plus, str(debut), thru, str(fin)]
            self._verifier_combinaison(f"{objet} <n> +", avert)

        if "part" in sel:
            part = sel["part"]
            morceaux.append(self.modele["objets"]["Part"]["mot_cle"])
            if isinstance(part, (list, tuple)):
                morceaux += [str(part[0]), thru, str(part[1])]
            else:
                morceaux.append(str(part))

        return " ".join(morceaux)

    # -- rendu : Query ------------------------------------------------------
    def _rendre_cible(self, cible: dict, avert: list[str]) -> str:
        """Une cible référencée : `Color Palette 2`, `Cue 4 Thru 9`…"""
        nom = cible["type"]
        spec = self.modele["cibles"].get(nom)
        if spec is None:
            avert.append(f"cible `{nom}` absente du modèle — non vérifiable")
            mot = nom
        else:
            mot = spec["mot_cle"]
        if "de" in cible:
            return f"{mot} {cible['de']} {self._thru} {cible['a']}"
        if "numero" in cible:
            return f"{mot} {cible['numero']}"
        return mot                      # `Query Effect` — toutes les cibles

    def _rendre_query(self, conditions: list[dict], avert: list[str]) -> str:
        """Query est le seul endroit du langage Eos où existe une négation.
        Toute logique conditionnelle du traducteur passe par ici, ou nulle part."""
        specs = self.modele["query"]["conditions"]
        morceaux = [self.modele["query"]["mot_cle"]]

        for critere in conditions:
            # `Query Effect 1` — une cible sans softkey de condition (manuel §18)
            if "condition" not in critere:
                morceaux.append(self._rendre_cible(critere["cible"], avert))
                continue

            nom = critere["condition"]
            spec = specs.get(nom)
            if spec is None:
                avert.append(f"condition Query `{nom}` absente du modèle — non vérifiable")
                morceaux.append(f"{{{nom}}}")
                continue

            morceaux.append(spec["mot_cle"])

            # une condition sans touche OSC ne s'atteint qu'au doigt : pour une
            # app qui injecte en OSC, c'est une impasse, pas un détail
            if spec["osc"] is None:
                avert.append(
                    f"condition Query `{nom}` : aucune touche OSC (manuel §31) — "
                    f"atteignable au doigt seulement (PLANNING #{spec['backlog']})"
                )

            attendu = spec["attend"]
            if attendu == "cible":
                if "cible" not in critere:
                    avert.append(f"condition Query `{nom}` attend une cible — absente de l'IR")
                else:
                    morceaux.append(self._rendre_cible(critere["cible"], avert))
            elif attendu == "valeur":
                if "valeur" not in critere:
                    avert.append(f"condition Query `{nom}` attend une valeur — absente de l'IR")
                else:
                    morceaux.append(str(critere["valeur"]))
            elif attendu == "aucun" and ("cible" in critere or "valeur" in critere):
                avert.append(f"condition Query `{nom}` n'attend aucun argument — ignoré")

            if "contextes" in spec:
                avert.append(
                    f"condition Query `{nom}` : valable uniquement en "
                    f"{'/'.join(spec['contextes'])}"
                )

        return " ".join(morceaux)

    # -- rendu : Fan --------------------------------------------------------
    def _rendre_fan(self, fan: dict, avert: list[str]) -> str:
        """Fan ne change jamais la commande qui le porte, seulement la façon dont
        la plage se répartit. `Fan` est inutile pour le style par défaut."""
        nom = fan["style"]
        styles = self.modele["fan"]["styles"]

        # le manuel abrège parfois `{Mirror Out}` en `{Mirror}` — jamais confirmé
        if nom == "Mirror":
            backlog = self._backlog_de("Fan {Mirror}")
            avert.append(
                f"`{{Mirror}}` n'est pas un nom de softkey confirmé — "
                f"`{{Mirror Out}}` émis à la place (PLANNING #{backlog})"
            )
            nom = "Mirror Out"

        spec = styles.get(nom)
        if spec is None:
            avert.append(f"style de Fan `{nom}` absent du modèle — non vérifiable")
            return f"{self.modele['fan']['mot_cle']} {{{nom}}}"

        morceaux = [self.modele["fan"]["mot_cle"], spec["mot_cle"]]

        if "backlog" in spec:
            avert.append(
                f"style de Fan `{nom}` : touche confirmée, comportement jamais "
                f"observé (PLANNING #{spec['backlog']})"
            )

        attendu = spec["argument"]
        if attendu == "entier":
            if "argument" not in fan:
                avert.append(f"style de Fan `{nom}` attend un entier — absent de l'IR")
            else:
                morceaux.append(str(fan["argument"]))
        elif attendu == "aucun" and "argument" in fan:
            avert.append(f"style de Fan `{nom}` n'attend pas d'argument — ignoré")
        elif attendu == "inconnu" and "argument" in fan:
            morceaux.append(str(fan["argument"]))

        return " ".join(morceaux)

    def _verifier_niveau(self, valeur: object, avert: list[str]) -> None:
        """`At 5` vaut 50 %, pas 5 % : un chiffre unique reçoit un zéro
        implicite (manuel §6, notation `<0>`, cinq occurrences). C'est le seul
        piège du modèle qui transforme une commande valide en résultat faux
        d'un facteur dix, sans erreur de syntaxe."""
        texte = str(valeur)
        if len(texte) == 1 and texte.isdigit() and texte != "0":
            backlog = self._backlog_de("niveau à un seul chiffre")
            avert.append(
                f"niveau `{texte}` : un chiffre unique reçoit un zéro implicite — "
                f"la console lira {int(texte) * 10} %, pas {texte} % "
                f"(manuel §6). Écrire `{int(texte) * 10}` pour {int(texte) * 10} %, "
                f"ou voir PLANNING #{backlog} pour {texte} %"
            )

    def _plage_ou_valeur(self, act: dict, cle: str = "valeur") -> str:
        """`10` ou `10 Thru 50` — la seconde forme est un fan implicite."""
        if "de" in act:
            return f"{act['de']} {self._thru} {act['a']}"
        return str(act[cle])

    def _suffixe_fan(self, act: dict, avert: list[str]) -> list[str]:
        if "fan" not in act:
            return []
        if "de" not in act:
            avert.append(
                "style de Fan demandé sans plage de valeurs — Fan répartit une "
                "plage, il ne la crée pas"
            )
        return [self._rendre_fan(act["fan"], avert)]

    # -- rendu : actions ----------------------------------------------------
    def _rendre_action(self, act: dict, avert: list[str]) -> str:
        t = act["type"]
        spec = self.modele["actions"][t]
        mot = spec["mot_cle"]

        # une action dont la syntaxe ne vient pas d'une source officielle ne doit
        # jamais passer en silence, même quand la matrice la déclare légale
        if spec.get("confiance") in ("B", "C", "D"):
            avert.append(
                f"`{mot}` : syntaxe de confiance {spec['confiance']} "
                f"({spec.get('source', 'source non précisée')})"
            )

        if t == "couleur_gel":
            return f"{mot} {act['nuancier']}/{act['teinte']}"

        if t == "intensite":
            for cle in ("valeur", "de", "a"):
                if cle in act:
                    self._verifier_niveau(act[cle], avert)
            return " ".join([mot, self._plage_ou_valeur(act)]
                            + self._suffixe_fan(act, avert))

        if t in ("temps", "delai"):
            if "montee" in act:                  # `Time 4/3` — montée / descente
                valeur = f"{act['montee']}/{act['descente']}"
            elif "de" not in act and "valeur" not in act:
                valeur = ""                      # `Time Enter` remet au défaut
            else:
                valeur = self._plage_ou_valeur(act)
            morceaux = [mot] + ([valeur] if valeur else [])
            return " ".join(morceaux + self._suffixe_fan(act, avert))

        if t in ("palette_intensite", "palette_couleur"):
            self._verifier_fan_references(act, avert)
            return " ".join([mot, self._plage_ou_valeur(act, "numero")]
                            + self._suffixe_fan(act, avert))

        if t in ("record_palette", "record_only_palette", "update_palette",
                 "rappeler_palette", "rappeler_depuis"):
            famille = self.modele["palettes"]["familles"].get(act["famille"])
            if famille is None:
                avert.append(f"famille de palette `{act['famille']}` absente du modèle")
                mot_famille = act["famille"]
            else:
                mot_famille = famille["mot_cle"]
            morceaux = ([mot] if mot else []) + [mot_famille]
            if "cible" in act:
                morceaux.append(str(act["cible"]))
            if "proportion" in act:
                morceaux += ["At", str(act["proportion"])]
            for option in act.get("options", []):
                if option not in self.modele["palettes"]["options"]:
                    avert.append(f"option de palette `{option}` absente du modèle")
                morceaux.append(option)
            if act.get("label"):
                morceaux += ["Label", str(act["label"])]
                self._verifier_label(act["label"], avert)
            return " ".join(morceaux)

        if t in ("record_preset", "record_only_preset", "rappeler_preset"):
            out = mot if "cible" not in act else f"{mot} {act['cible']}"
            if act.get("label"):
                out += f" Label {act['label']}"
                self._verifier_label(act["label"], avert)
            return out

        if t == "record_palette_couleur":
            out = f"{mot} {act['cible']}"
            if act.get("label"):
                out += f" Label {act['label']}"
                self._verifier_label(act["label"], avert)
            return out

        if t in ("record_cue", "record_only_cue", "update_cue",
                 "record_sub", "record_only_sub", "update_sub"):
            cible = act["cible"]
            if "liste" in act:
                cible = f"{act['liste']}/{cible}"
            out = f"{mot} {cible}"
            if "a" in act:                       # plage de cibles
                out += f" {self._thru} {act['a']}"
            if act.get("label"):
                out += f" Label {act['label']}"
                self._verifier_label(act["label"], avert)
            return out

        if t == "go_to_cue":
            cible = act.get("mot", act.get("cible"))
            if cible is None:
                avert.append("`Go To Cue` sans destination — ni numéro ni mot-clé")
                cible = "?"
            elif not str(cible).replace(".", "", 1).isdigit() \
                    and cible not in CIBLES_SYMBOLIQUES:
                avert.append(
                    f"destination `{cible}` inconnue : attendu un numéro ou "
                    f"{', '.join(sorted(CIBLES_SYMBOLIQUES))}"
                )
            if "liste" in act:
                cible = f"{act['liste']}/{cible}"
            return f"{mot} {cible}"

        if t == "cue_link":
            out = f"{mot} {act['cible']}"
            if "iterations" in act:
                out += f" {mot} {act['iterations']}"
                if act["iterations"] == 0:
                    avert.append("boucle à 0 itération = boucle infinie (manuel §12)")
            return out

        if t in ("sub_bump_bas", "sub_bump_haut"):
            return f"{mot} {act['numero']}"

        if t == "temps_bump_sub":
            return " ".join([mot, str(act["montee"]),
                             mot, str(act["dwell"]),
                             mot, str(act["descente"])])

        if t == "label":
            self._verifier_label(act["texte"], avert)
            return f"{mot} {act['texte']}"

        if t == "appel_macro":
            return f"{mot} {act['numero']}"

        if t in ("selection_active", "selection_derniere", "retirer_effet",
                 "hors_scene", "niveau_setup", "incrementer", "decrementer"):
            return mot

        if t in ("plein_feu", "sneak"):
            # le double appui est une AUTRE commande, pas une insistance
            return f"{mot} {mot}" if act.get("double") else mot

        if t == "valeur_dmx":
            valeur = int(act["valeur"])
            if not 0 <= valeur <= 255:
                avert.append(f"valeur DMX {valeur} hors bornes 0-255")
            return f"{mot} {valeur}"

        if t in ("patcher", "patch_courbe", "patch_preheat", "patch_proportion"):
            if t == "patcher":
                self._verifier_mode_patch(act, avert)
            return f"{mot} {act['adresse' if t == 'patcher' else 'valeur']}"

        if t == "patch_univers":
            self._verifier_mode_patch(act, avert)
            return f"{mot} {act['univers']} / {act['adresse']}"

        if t == "patcher_par_adresse":
            # seule forme documentée qui lève l'ambiguïté du mode Format
            return f"{mot} {act['adresse']} At {act['channel']}"

        if t in ("retirer_adresse", "depatcher", "patch_hors_sortie",
                 "reordonner", "inverser_ordre", "ordre_aleatoire",
                 "marquer", "marquer_au_plus_tot", "asserter",
                 "tout_deparquer", "effacer_filtres"):
            if t == "marquer":
                self._verifier_combinaison("AutoMark ou marques référencées", avert)
            if t == "effacer_filtres":
                self._verifier_combinaison("pose de filtres par accord maintenu", avert)
            return mot

        if t in ("appliquer_courbe", "record_snapshot", "rappeler_snapshot"):
            out = f"{mot} {act['cible']}"
            if act.get("label"):
                out += f" Label {act['label']}"
                self._verifier_label(act["label"], avert)
            return out

        if t == "retirer_courbe":
            return mot

        if t == "parquer":
            if "valeur" in act:
                self._verifier_niveau(act["valeur"], avert)
            if "valeur" not in act:
                avert.append(
                    "`At Park` sans valeur est un bascule : il déparque si le "
                    "channel est déjà parqué (manuel §19) — passer une valeur "
                    "pour un résultat déterministe"
                )
                return f"At {mot}"
            return f"At {act['valeur']} {mot}"

        if t == "parquer_echelle":
            return f"{mot} {act['valeur']} Park"

        if t == "affecter_part":
            return mot if "cible" not in act else f"{mot} {act['cible']}"

        if t == "supprimer_part":
            return f"{mot} {act['cible']}"

        if t in ("marquer_vers_cue", "mark_time"):
            if t == "marquer_vers_cue":
                self._verifier_combinaison("AutoMark ou marques référencées", avert)
            return f"{mot} {act['cible' if t == 'marquer_vers_cue' else 'valeur']}"

        if t in ("record_groupe", "record_only_groupe", "update_groupe",
                 "inserer_avant", "inserer_apres"):
            out = f"{mot} {act['cible']}"
            if act.get("label"):
                out += f" Label {act['label']}"
                self._verifier_label(act["label"], avert)
            if t in ("inserer_avant", "inserer_apres"):
                self._verifier_combinaison("{Insert Before} / {Insert After}", avert)
            return out

        if t == "supprimer":
            return mot

        if t == "focus_onglet":
            numero = act["numero"]
            ecrans = self.modele["contexte"]["ecrans"]
            if numero not in ecrans:
                avert.append(f"écran {numero} absent de la table officielle des Tabs")
            return f"{mot} {numero}"

        if t == "appliquer_effet":
            return f"{mot} {act['numero']}"

        if t == "arreter_effet":
            if act.get("tout"):                  # double appui = stop all
                return f"{mot} {mot}"
            if "numero" in act:
                return f"{mot} {act['numero']}"
            return mot

        if t == "effet_bpm":
            return f"{{{mot}}} {act['valeur']}"

        raise ValueError(f"action non gérée : {t}")

    def _verifier_mode_patch(self, act: dict, avert: list[str]) -> None:
        """`5 At 100` patche le channel 5 à l'adresse 100 en mode par channel,
        et l'adresse 5 au channel 100 en mode par adresse. Le générateur ne peut
        ni lire ni régler ce mode : il ne peut que le signaler."""
        modes = self.modele["contexte"]["modes_patch"]
        avert.append(
            f"patch : le sens de `At` dépend du mode Format, que le générateur "
            f"ne peut ni lire ni régler (PLANNING #{modes['bascule']['backlog']}) — "
            f"`Address <n> At <channel>` lève l'ambiguïté"
        )

    def _verifier_fan_references(self, act: dict, avert: list[str]) -> None:
        """Fan sur 2 références ou moins interpole en absolu et perd la
        référence — piège documenté A, pas une erreur de syntaxe."""
        if "de" not in act:
            return
        nombre = abs(int(act["a"]) - int(act["de"])) + 1
        if nombre <= 2:
            avert.append(
                f"fan sur {nombre} référence(s) : Eos interpole en données "
                f"ABSOLUES et casse la référence (manuel §8, « Fanning "
                f"References ») — il en faut 3 ou plus pour rester référencé"
            )

    # -- rendu : modificateurs ----------------------------------------------
    def _rendre_modificateurs(self, noms: list[str], action: str,
                              avert: list[str]) -> list[str]:
        morceaux: list[str] = []
        for nom in noms:
            spec = self.modele["modificateurs"].get(nom)
            if spec is None:
                avert.append(f"modificateur `{nom}` absent du modèle — non vérifiable")
                morceaux.append(nom)
                continue
            if action not in spec.get("porte_sur", []):
                avert.append(
                    f"modificateur `{nom}` non documenté sur `{action}` "
                    f"(porte sur : {', '.join(spec.get('porte_sur', [])) or 'rien'})"
                )
            morceaux.append(spec["mot_cle"])
            if nom in ("Q Only", "Track"):
                avert.append(
                    "`Q Only` et `Track` sont la même touche : son sens dépend du "
                    "réglage système de la console — vérifier le mode avant envoi"
                )
        return morceaux

    # -- cues multipart -----------------------------------------------------
    def _verifier_instruction_unique(self, ir: list[dict], avert: list[str]) -> None:
        """Un channel ne peut recevoir qu'UNE instruction dans une cue multipart
        (manuel §17). C'est vérifiable statiquement : deux affectations du même
        channel à des parts différentes sont une erreur de construction, pas un
        cas limite de la console."""
        vus: dict[int, object] = {}
        for etape in ir:
            action = etape.get("action", {})
            if action.get("type") != "affecter_part":
                continue
            sel = etape.get("selection", {})
            if "de" in sel:
                channels = range(int(sel["de"]), int(sel["a"]) + 1)
            elif "numero" in sel:
                channels = [int(sel["numero"])]
            else:
                continue
            part = action.get("cible")
            for c in channels:
                if c in vus and vus[c] != part:
                    avert.append(
                        f"channel {c} affecté à deux parts ({vus[c]} puis {part}) — "
                        f"une cue multipart n'accepte qu'une instruction par channel "
                        f"(manuel §17)"
                    )
                vus[c] = part

    # -- contexte d'écran ---------------------------------------------------
    def _numero_ecran(self, nom: str) -> int | None:
        """Un onglet peut héberger plusieurs modes : le Tab 1 est « Live/Blind »
        et `Live` comme `Blind` y mènent."""
        for numero, spec in self.modele["contexte"]["ecrans"].items():
            if nom == spec["nom"] or nom in spec["nom"].split("/"):
                return numero
        return None

    def _verifier_contexte(self, action: dict, contexte: str,
                           avert: list[str]) -> None:
        """La ligne de commande Eos est modale : le même mot ne dit pas la même
        chose selon l'écran actif. C'est vérifié ici, pas supposé."""
        t = action["type"]
        spec = self.modele["actions"][t]

        attendus = spec.get("contextes")
        if not attendus or contexte in attendus:
            return          # l'action est documentée pour cet écran : rien à dire

        # hors contexte. Si le mot-clé est polysémique, dire ce qu'il voudra
        # dire ICI est plus utile que de dire qu'on est hors contexte.
        polysemie = self.modele["contexte"]["polysemie"]
        sens = polysemie.get(spec["mot_cle"], {}).get("sens", {})
        if contexte in sens:
            avert.append(
                f"`{spec['mot_cle']}` en contexte {contexte} signifie "
                f"« {sens[contexte]} » — pas ce que l'action `{t}` demande"
            )
        else:
            avert.append(
                f"action `{t}` documentée en {'/'.join(attendus)} seulement, "
                f"pas en {contexte}"
            )

    # -- rendu : ligne de commande -----------------------------------------
    def rendre(self, ir: list[dict], *, contexte: str = "Live",
               forcer_focus: bool = False) -> Resultat:
        """Transforme une IR (liste d'étapes) en commande Eos multi-lignes.

        `contexte` est l'écran supposé actif. `forcer_focus` préfixe la sortie
        d'un `Tab <n> Enter` pour ne plus rien supposer — au prix de déplacer
        ce que voit l'opérateur : le focus visuel et le focus logique sont le
        même mécanisme (corpus #168).
        """
        lignes: list[str] = []
        avert: list[str] = []

        self._verifier_instruction_unique(ir, avert)

        if forcer_focus:
            numero = self._numero_ecran(contexte)
            if numero is None:
                avert.append(f"écran `{contexte}` absent de la table officielle des Tabs")
            else:
                mot = self.modele["actions"]["focus_onglet"]["mot_cle"]
                lignes.append(f"{mot} {numero} Enter")

        for etape in ir:
            morceaux: list[str] = []
            objet = None

            if "controle" in etape:
                lignes.append(self._rendre_controle(etape, avert))
                continue

            if "query" in etape:
                morceaux.append(self._rendre_query(etape["query"], avert))
                if "selection" in etape:
                    avert.append(
                        "une Query construit elle-même sa sélection — la sélection "
                        "explicite fournie en plus n'a pas de sens documenté"
                    )

            if "selection" in etape:
                # une sélection en sous-groupes désigne des channels sans le dire
                objet = etape["selection"].get("objet", "Chan")
                morceaux.append(self._rendre_selection(etape["selection"], avert))

            auto_termine = False

            if "action" in etape:
                action = etape["action"]
                spec = self.modele["actions"][action["type"]]
                # certaines actions portent leur objet dans leur mot-clé
                # (`Go To Cue 5`) : pas de sélection, mais pas non plus une
                # action sur la sélection courante
                cible = objet or spec.get("objet_implicite") or "selection_courante"
                self._verifier(cible, action["type"], avert)
                self._verifier_contexte(action, contexte, avert)
                morceaux.append(self._rendre_action(action, avert))

                auto_termine = spec.get("auto_termine", False)
                # `Full Full` et `Sneak Sneak` auto-terminent, pas leur forme simple
                if action.get("double") and action["type"] in ("plein_feu", "sneak"):
                    auto_termine = True

                mods = etape.get("modificateurs", [])
                if mods:
                    morceaux += self._rendre_modificateurs(mods, action["type"], avert)

                # manuel §16 : sur un Go To Cue, `Time` se pose toujours en
                # dernier, après les autres modificateurs
                if "temps" in action:
                    morceaux.append(
                        self._rendre_action(
                            {"type": "temps", **action["temps"]}, avert))

            # un `Enter` de trop sur une commande déjà terminée peut valider la
            # ligne suivante — la terminaison n'est pas une formalité
            if not auto_termine:
                morceaux.append(self.modele["terminaison"]["defaut"]["mot_cle"])
            lignes.append(" ".join(morceaux))

        return Resultat("\n".join(lignes), avert)

    # -- rendu : contenu de macro -------------------------------------------
    def _rendre_controle(self, etape: dict, avert: list[str]) -> str:
        """Token de contrôle de macro (`{Wait}`, `{Loop Begin}`…)."""
        nom = etape["controle"]
        spec = self.modele["macro"]["controle"].get(nom)
        if spec is None:
            avert.append(f"token de contrôle `{nom}` absent du modèle — non vérifiable")
            return nom

        morceaux = [spec["mot_cle"]]
        attendu = spec["argument"]
        if attendu == "entier_obligatoire":
            if "argument" not in etape:
                avert.append(
                    f"`{spec['mot_cle']}` exige un nombre ENTIER de secondes "
                    f"(manuel §24) — absent de l'IR"
                )
            elif not isinstance(etape["argument"], int):
                avert.append(
                    f"`{spec['mot_cle']}` exige un entier, reçu "
                    f"`{etape['argument']}` — la console refusera"
                )
            else:
                morceaux.append(str(etape["argument"]))
        elif attendu == "entier" and "argument" in etape:
            morceaux.append(str(etape["argument"]))
            if nom == "Loop Begin" and etape["argument"] == 0:
                avert.append(
                    "boucle à 0 itération = boucle infinie (manuel §24) : seule "
                    "la touche [Escape] l'arrête sur la console"
                )
        return " ".join(morceaux)

    def rendre_macro(self, numero: int, contenu: list[dict], *,
                     voie: str = "learn", mode: str = "Foreground",
                     label: str | None = None) -> Resultat:
        """Enveloppe une IR dans une macro.

        `voie` : "learn" (voie primaire ETC, enregistre les frappes réelles) ou
        "editeur" (voie corrective, écrit le contenu sans l'exécuter).
        """
        interne = self.rendre(contenu)
        avert = list(interne.avertissements)
        notes: list[str] = []

        mot_macro = self.modele["objets"]["Macro"]["mot_cle"]
        lignes: list[str] = []

        if voie == "learn":
            lignes.append(f"Learn {numero} Enter")
            lignes += interne.commande.splitlines()
            lignes.append("Learn")
            notes.append(
                "voie Learn : toute frappe est enregistrée, y compris un `Clear` "
                "de rattrapage (manuel §24)"
            )
        elif voie == "editeur":
            lignes.append(f"{mot_macro} {numero} Enter")
            lignes.append("{Edit}")
            lignes += interne.commande.splitlines()
            lignes.append("Select")
            notes.append("voie éditeur : `Select` valide, `Escape` annule (manuel §24)")
        else:
            raise ValueError(f"voie de création inconnue : {voie}")

        if label:
            lignes.append(f"{mot_macro} {numero} Label {label} Enter")
            self._verifier_label(label, avert)

        # -- règles propres au contexte macro --------------------------------
        defaut = self.modele["macro"]["modes"]["defaut_projet"]
        if mode != defaut:
            avert.append(
                f"mode `{mode}` : le projet impose `{defaut}` sauf raison explicite "
                f"({{Target}} vers un User n'existe qu'en Foreground, corpus #068)"
            )
        notes.append(f"mode à régler sur {{{mode}}} dans l'éditeur — hors contenu de la macro")

        types = [e["action"]["type"] for e in contenu if "action" in e]

        if "appel_macro" in types:
            self._verifier_combinaison("Macro <n> Enter en fin de contenu", avert)
            if types[-1] != "appel_macro":
                avert.append(
                    "chaînage macro-dans-macro : l'appel doit être en FIN de contenu "
                    "(manuel §24), il ne l'est pas ici"
                )
            # [Macro] fait partie des touches que le mode Learn n'enregistre pas
            # (manuel §24) — d'où l'exemple officiel de chaînage écrit à l'éditeur
            if voie == "learn":
                exclues = self.modele["macro"]["creation"]["learn"]["touches_exclues"]
                if mot_macro in exclues:
                    avert.append(
                        f"`{mot_macro}` fait partie des touches que le mode Learn "
                        f"n'enregistre pas : un chaînage macro-dans-macro doit passer "
                        f"par l'éditeur (voie `editeur`)"
                    )

        if "go_to_cue" in types:
            backlog = self._backlog_de("Go To Cue en macro")
            avert.append(
                f"`Go To Cue` en macro : exécution non déterministe selon le mode "
                f"et le timing (PLANNING #{backlog})"
            )

        if {"sub_bump_bas", "sub_bump_haut"} & set(types):
            self._verifier_combinaison("macro contenant SubDown/SubUp", avert)

        return Resultat("\n".join(lignes), avert, notes)


    # -- injection OSC ------------------------------------------------------
    def _adresse(self, chemin: str, utilisateur: int | None) -> str:
        """`/eos/newcmd` ou `/eos/user/3/newcmd`."""
        if utilisateur is None:
            return f"{self.modele['osc']['prefixe']}{chemin}"
        return f"{self.modele['osc']['prefixe']}user/{utilisateur}/{chemin}"

    def rendre_osc(self, source: Resultat | str, *, adresse: str = "newcmd",
                   utilisateur: int | None = None) -> ResultatOSC:
        """Transforme une commande rendue en paquets OSC injectables.

        Une ligne de commande correctement engendrée mais mal injectée ne vaut
        rien : c'est ici que se vérifient les règles propres au transport.
        """
        spec = self.modele["osc"]["ligne_commande"].get(adresse)
        if spec is None:
            raise ValueError(f"adresse de ligne de commande inconnue : {adresse}")

        commande = source.commande if isinstance(source, Resultat) else source
        avert = list(source.avertissements) if isinstance(source, Resultat) else []
        notes: list[str] = []
        messages: list[Message] = []

        regles = {r["id"]: r for r in self.modele["osc"]["regles"]}

        for ligne in commande.splitlines():
            if not ligne.strip():
                continue

            # les accolades n'ont jamais été vues dans une chaîne de ligne de
            # commande OSC — ni au manuel, ni au corpus, ni au banc
            if "{" in ligne:
                regle = regles["accolades_non_confirmees"]
                avert.append(
                    f"« {ligne} » contient un token entre accolades : jamais "
                    f"observé dans une chaîne `{spec['adresse']}` "
                    f"(PLANNING #{regle['backlog']})"
                )

            if "Assert" in ligne:
                avert.append(
                    f"« {ligne} » : `Assert` n'a pas de mot-clé de ligne de "
                    f"commande — erreur de syntaxe confirmée au banc (confiance S)"
                )

            if not ligne.endswith("Enter") and not ligne.endswith("#"):
                avert.append(
                    f"« {ligne} » sans terminaison : la console la laissera en "
                    f"attente sur la ligne de commande"
                )

            messages.append(Message(self._adresse(adresse, utilisateur), [ligne]))

        if utilisateur is None:
            notes.append(
                "aucun User# précisé : le client hérite de l'utilisateur de la "
                "console primaire. Recommandation B (corpus #066) — en réserver un."
            )

        notes.append(
            f"terminaison par le mot `Enter` littéral — forme employée au banc "
            f"de transport (`reference/tools/`)"
        )
        if spec.get("reinitialise"):
            notes.append(f"`{spec['adresse']}` réinitialise la ligne de commande avant d'écrire")

        return ResultatOSC(messages, avert, notes)

    def rendre_osc_macro(self, numero: int, *,
                         utilisateur: int | None = None) -> ResultatOSC:
        """Déclenche une macro déjà enregistrée — adresse normative du projet."""
        adresse = self.modele["osc"]["macro"]["execution"]["adresse"]
        chemin = adresse[len(self.modele["osc"]["prefixe"]):]
        return ResultatOSC(
            [Message(self._adresse(chemin, utilisateur), [numero])],
            [],
            ["déclencher une macro enregistrée ne rejoue pas sa syntaxe : "
             "la console l'a déjà acceptée à l'enregistrement"],
        )

    def rendre_osc_touche(self, nom: str, *, front: float | None = None,
                          utilisateur: int | None = None) -> ResultatOSC:
        """Simule un appui de touche. Seule voie pour ce que la ligne de
        commande ne sait pas exprimer (Assert, conditions Query sans mot)."""
        avert: list[str] = []
        nommage = self.modele["osc"]["touche"]["nommage"]
        if " " in nom:
            avert.append(
                f"nom de touche `{nom}` avec espace : le générateur n'émet que la "
                f"forme underscore de eosKeys.ts (PLANNING #{nommage['backlog']})"
            )
            nom = nom.replace(" ", "_")
        args = [front] if front is not None else []
        return ResultatOSC([Message(self._adresse(f"key/{nom}", utilisateur), args)], avert)


if __name__ == "__main__":
    g = Generateur()
    exemples = [
        ("circuits 10 à 20 en Lee 195", [
            {"selection": {"objet": "Chan", "de": 10, "a": 20},
             "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
        ]),
        ("groupe 5 + circuits 1 à 6 en Lee 195, puis palette 5 « 195-Par LED »", [
            {"selection": {"objet": "Group", "numero": 5, "plus_plage": [1, 6]},
             "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
            {"action": {"type": "record_palette_couleur", "cible": 5,
                        "label": "195-Par LED"}},
        ]),
        ("circuits 1 à 5 en dégradé de 10 à 50 %", [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "intensite", "de": 10, "a": 50}},
        ]),
        ("circuits 1 à 12 de 50 à 70 %, par paquets répétés de 3", [
            {"selection": {"objet": "Chan", "de": 1, "a": 12},
             "action": {"type": "intensite", "de": 50, "a": 70,
                        "fan": {"style": "Repeat", "argument": 3}}},
        ]),
        ("temps des cues 1 à 5 échelonnés de 6 à 10 s", [
            {"selection": {"objet": "Cue", "de": 1, "a": 5},
             "action": {"type": "temps", "de": 6, "a": 10}},
        ]),
        ("circuits 6 à 10 dans le submaster 3", [
            {"selection": {"objet": "Chan", "de": 6, "a": 10},
             "action": {"type": "record_sub", "cible": 3}},
        ]),
        ("tout ce qui est dans la palette couleur 2, à 50 %", [
            {"query": [{"condition": "Is In",
                        "cible": {"type": "Color Palette", "numero": 2}}],
             "action": {"type": "intensite", "valeur": 50}},
        ]),
        ("tout ce qui n'est PAS dans la palette beam 25", [
            {"query": [{"condition": "Isn't In",
                        "cible": {"type": "Beam Palette", "numero": 25}}]},
        ]),
    ]
    for nl, ir in exemples:
        r = g.rendre(ir)
        print(f"\nNL  : {nl}")
        for ligne in r.commande.splitlines():
            print(f"EOS : {ligne}")
        if r.sur:
            print("      ✔ aucune zone d'ombre traversée")
        for a in r.avertissements:
            print(f"      ⚠ {a}")

    print("\n--- contenu de macro ---")
    r = g.rendre_macro(1, [
        {"action": {"type": "go_to_cue", "mot": "Out", "temps": {"valeur": 0}}},
    ])
    print("NL  : macro 1 — aller à Cue Out en 0 s")
    for ligne in r.commande.splitlines():
        print(f"EOS : {ligne}")
    for a in r.avertissements:
        print(f"      ⚠ {a}")
    for n in r.notes:
        print(f"      · {n}")

    print("\n--- injection OSC ---")
    rendu = g.rendre([
        {"selection": {"objet": "Chan", "de": 10, "a": 20},
         "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
    ])
    osc = g.rendre_osc(rendu, utilisateur=3)
    for m in osc.messages:
        print(f"OSC : {m}")
    for n in osc.notes:
        print(f"      · {n}")

    print()
    avec_fan = g.rendre([
        {"selection": {"objet": "Chan", "de": 1, "a": 10},
         "action": {"type": "intensite", "de": 10, "a": 30,
                    "fan": {"style": "Mirror Out"}}},
    ])
    osc = g.rendre_osc(avec_fan, utilisateur=3)
    for m in osc.messages:
        print(f"OSC : {m}")
    for a in osc.avertissements:
        print(f"      ⚠ {a}")

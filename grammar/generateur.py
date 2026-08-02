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
    def _rendre_selection(self, sel: dict, avert: list[str]) -> str:
        objet = sel["objet"]
        mot = self.modele["objets"][objet]["mot_cle"]
        thru, plus = self._thru, self._plus

        # préfixe de cue list : `Cue 2/5`
        prefixe = f"{sel['liste']}/" if "liste" in sel else ""

        if "de" in sel:
            morceaux = [mot, f"{prefixe}{sel['de']}", thru, str(sel["a"])]
        elif "mot" in sel:                       # Out / Next / Last / Home
            morceaux = [mot, f"{prefixe}{sel['mot']}"]
        else:
            morceaux = [mot, f"{prefixe}{sel['numero']}"]

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

        raise ValueError(f"action non gérée : {t}")

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

    # -- rendu : ligne de commande -----------------------------------------
    def rendre(self, ir: list[dict]) -> Resultat:
        """Transforme une IR (liste d'étapes) en commande Eos multi-lignes."""
        lignes: list[str] = []
        avert: list[str] = []

        for etape in ir:
            morceaux: list[str] = []
            objet = None

            if "controle" in etape:
                lignes.append(self._rendre_controle(etape, avert))
                continue

            if "selection" in etape:
                objet = etape["selection"]["objet"]
                morceaux.append(self._rendre_selection(etape["selection"], avert))

            if "action" in etape:
                action = etape["action"]
                spec = self.modele["actions"][action["type"]]
                # certaines actions portent leur objet dans leur mot-clé
                # (`Go To Cue 5`) : pas de sélection, mais pas non plus une
                # action sur la sélection courante
                cible = objet or spec.get("objet_implicite") or "selection_courante"
                self._verifier(cible, action["type"], avert)
                morceaux.append(self._rendre_action(action, avert))

                mods = etape.get("modificateurs", [])
                if mods:
                    morceaux += self._rendre_modificateurs(mods, action["type"], avert)

                # manuel §16 : sur un Go To Cue, `Time` se pose toujours en
                # dernier, après les autres modificateurs
                if "temps" in action:
                    morceaux.append(
                        self._rendre_action(
                            {"type": "temps", **action["temps"]}, avert))

            morceaux.append("Enter")
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

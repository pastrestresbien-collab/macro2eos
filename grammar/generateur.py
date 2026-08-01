#!/usr/bin/env python3
"""Génère une commande Eos à partir d'une représentation intermédiaire (IR).

Le traducteur NL produira l'IR ; ce module la transforme en chaîne de commande
et signale les zones non validées au banc réel.

    >>> g = Generateur()
    >>> r = g.rendre([{"selection": {"objet": "Chan", "de": 10, "a": 20},
    ...                "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}}])
    >>> r.commande
    'Chan 10 Thru 20 Color 3/195 Enter'

Règle non négociable : une combinaison marquée `inconnu` dans le modèle produit
un avertissement, jamais un silence. Une macro générée sans avertissement n'est
pas pour autant validée — seul un banc réel tranche (voir PLANNING.md).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

RACINE = Path(__file__).parent


@dataclass
class Resultat:
    commande: str
    avertissements: list[str] = field(default_factory=list)

    @property
    def sur(self) -> bool:
        """Vrai si aucune zone d'ombre n'a été traversée."""
        return not self.avertissements


class Generateur:
    def __init__(self) -> None:
        self.modele = yaml.safe_load((RACINE / "modele.yaml").read_text(encoding="utf-8"))
        self._legalite = self.modele["legalite"]

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

    # -- rendu --------------------------------------------------------------
    def _rendre_selection(self, sel: dict, avert: list[str]) -> str:
        objet = sel["objet"]
        mot = self.modele["objets"][objet]["mot_cle"]
        thru = self.modele["operateurs"]["plage"]["symbole"]
        plus = self.modele["operateurs"]["ajout"]["symbole"]

        if "de" in sel:
            morceaux = [mot, str(sel["de"]), thru, str(sel["a"])]
        else:
            morceaux = [mot, str(sel["numero"])]

        if "plus_plage" in sel:
            debut, fin = sel["plus_plage"]
            morceaux += [plus, str(debut), thru, str(fin)]
            self._verifier_combinaison(f"{objet} <n> +", avert)

        return " ".join(morceaux)

    def _rendre_action(self, act: dict, avert: list[str]) -> str:
        t = act["type"]
        spec = self.modele["actions"][t]
        mot = spec["mot_cle"]

        if t == "couleur_gel":
            return f"{mot} {act['nuancier']}/{act['teinte']}"
        if t == "intensite":
            return f"{mot} {act['valeur']}"
        if t == "record_palette_couleur":
            out = f"{mot} {act['cible']}"
            if act.get("label"):
                out += f" Label {act['label']}"
                if " " in str(act["label"]):
                    self._verifier_combinaison("Record Color Palette <n> Label", avert)
            return out
        raise ValueError(f"action non gérée : {t}")

    def rendre(self, ir: list[dict]) -> Resultat:
        """Transforme une IR (liste d'étapes) en commande Eos multi-lignes."""
        lignes: list[str] = []
        avert: list[str] = []

        for etape in ir:
            morceaux: list[str] = []
            objet = None

            if "selection" in etape:
                objet = etape["selection"]["objet"]
                morceaux.append(self._rendre_selection(etape["selection"], avert))

            if "action" in etape:
                action = etape["action"]
                cible = objet if objet else "selection_courante"
                self._verifier(cible, action["type"], avert)
                morceaux.append(self._rendre_action(action, avert))

            morceaux.append("Enter")
            lignes.append(" ".join(morceaux))

        return Resultat("\n".join(lignes), avert)


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

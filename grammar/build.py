#!/usr/bin/env python3
"""Compile le modèle YAML en JSON et vérifie sa cohérence.

Usage:
    python3 grammar/build.py            # compile + vérifie
    python3 grammar/build.py --check    # vérifie seulement (CI)

Produit `grammar/dist/modele.json` et `grammar/dist/patrons.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).parent
DIST = RACINE / "dist"
CONFIANCES = {"S", "A", "B", "C", "D", None}


def charger(nom: str) -> dict:
    return yaml.safe_load((RACINE / f"{nom}.yaml").read_text(encoding="utf-8"))


def verifier(modele: dict, patrons: dict) -> list[str]:
    """Contrôles de cohérence interne. Retourne la liste des erreurs."""
    erreurs: list[str] = []
    objets = set(modele["objets"])
    actions = set(modele["actions"])

    for i, regle in enumerate(modele["legalite"]):
        ref = regle.get("combinaison") or f"{regle.get('objet')}/{regle.get('action')}"

        if regle["valide"] not in ("oui", "non", "inconnu"):
            erreurs.append(f"legalite[{i}] ({ref}) : `valide` doit être oui/non/inconnu")

        if regle.get("confiance") not in CONFIANCES:
            erreurs.append(f"legalite[{i}] ({ref}) : confiance `{regle.get('confiance')}` invalide")

        # une combinaison validée doit porter une confiance, une inconnue doit
        # renvoyer au backlog — sinon la zone d'ombre devient invisible
        if regle["valide"] == "oui" and regle.get("confiance") is None:
            erreurs.append(f"legalite[{i}] ({ref}) : validée mais sans niveau de confiance")
        if regle["valide"] == "inconnu" and "backlog" not in regle:
            erreurs.append(f"legalite[{i}] ({ref}) : inconnue mais sans renvoi PLANNING.md")

        # les références objet/action doivent exister
        obj = regle.get("objet")
        if obj and obj not in objets and obj != "selection_courante":
            erreurs.append(f"legalite[{i}] : objet inconnu `{obj}`")
        act = regle.get("action")
        if act and act not in actions:
            erreurs.append(f"legalite[{i}] : action inconnue `{act}`")

    for p in patrons["patrons"]:
        if p.get("confiance") not in CONFIANCES:
            erreurs.append(f"patron `{p['id']}` : confiance invalide")
        if p.get("confiance") is None and not p.get("avertissements"):
            erreurs.append(
                f"patron `{p['id']}` : sans confiance établie, il doit lister "
                f"ses avertissements (renvois PLANNING.md)"
            )

    return erreurs


def main() -> int:
    modele = charger("modele")
    patrons = charger("patrons")

    erreurs = verifier(modele, patrons)
    if erreurs:
        print("Incohérences détectées :", file=sys.stderr)
        for e in erreurs:
            print(f"  - {e}", file=sys.stderr)
        return 1

    inconnues = [r for r in modele["legalite"] if r["valide"] == "inconnu"]
    print(f"Modèle v{modele['meta']['version']} — cohérent.")
    print(f"  {len(modele['objets'])} objets, {len(modele['actions'])} actions, "
          f"{len(modele['legalite'])} règles de légalité")
    print(f"  {len(inconnues)} zone(s) non tranchée(s) → banc réel : "
          f"{', '.join('PLANNING#%s' % r['backlog'] for r in inconnues)}")
    print(f"  {len(patrons['patrons'])} patron(s)")

    if "--check" in sys.argv:
        return 0

    DIST.mkdir(exist_ok=True)
    for nom, data in (("modele", modele), ("patrons", patrons)):
        cible = DIST / f"{nom}.json"
        cible.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"  → {cible.relative_to(RACINE.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

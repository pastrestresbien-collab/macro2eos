#!/usr/bin/env python3
"""Non-régression : le modèle doit régénérer à l'identique les macros déjà
passées au banc de transport (`reference/tools/`).

Ces chaînes sont la référence : si une évolution du modèle les modifie, c'est
une régression — le travail déjà validé en transport doit rester reproductible.

    python3 grammar/test_generateur.py
"""
from __future__ import annotations

import sys

from generateur import Generateur

CAS = [
    {
        "nom": "test-client.ts — plage de channels + gel",
        "ir": [
            {"selection": {"objet": "Chan", "de": 10, "a": 20},
             "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
        ],
        "attendu": "Chan 10 Thru 20 Color 3/195 Enter",
        "avertissements": 0,
    },
    {
        "nom": "test-client3.ts — sélection mixte + record palette",
        "ir": [
            {"selection": {"objet": "Group", "numero": 5, "plus_plage": [1, 6]},
             "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
            {"action": {"type": "record_palette_couleur", "cible": 5,
                        "label": "195-Par LED"}},
        ],
        "attendu": ("Group 5 + 1 Thru 6 Color 3/195 Enter\n"
                    "Record Color Palette 5 Label 195-Par LED Enter"),
        # doit signaler les deux zones d'ombre — un silence ici serait le vrai bug
        "avertissements": 2,
    },
]


def main() -> int:
    g = Generateur()
    echecs = 0

    for cas in CAS:
        r = g.rendre(cas["ir"])
        if r.commande != cas["attendu"]:
            echecs += 1
            print(f"ÉCHEC — {cas['nom']}")
            print(f"  attendu : {cas['attendu']!r}")
            print(f"  obtenu  : {r.commande!r}")
            continue
        if len(r.avertissements) != cas["avertissements"]:
            echecs += 1
            print(f"ÉCHEC — {cas['nom']} : {cas['avertissements']} avertissement(s) "
                  f"attendu(s), {len(r.avertissements)} obtenu(s)")
            for a in r.avertissements:
                print(f"    - {a}")
            continue
        print(f"OK — {cas['nom']}")

    print(f"\n{len(CAS) - echecs}/{len(CAS)} cas conformes.")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Le catalogue ne promet que des phrases qui marchent.

Le catalogue (`build_catalogue.py`) est ce que l'app montre à l'utilisateur
pour répondre à « qu'est-ce que cette app sait faire ? ». Si une seule de ses
phrases retombe en `incompris`, il ment — et il ment précisément à quelqu'un
qui le consulte parce qu'il ne savait pas quoi taper. Ce serait pire que de
n'avoir aucun catalogue.

Ce test rejoue donc CHAQUE phrase contre le vrai traducteur. Il n'y a rien à
maintenir ici : les cas sont générés depuis `lexique.yaml`, donc toute
intention ajoutée au lexique est automatiquement couverte, et une intention
dont l'`exemple_nl` cesserait de fonctionner fait échouer la suite.

    cd traducteur && python3 test_catalogue.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

from build_catalogue import construire
from traducteur import Traducteur

RACINE = Path(__file__).parent


def main() -> int:
    lexique = yaml.safe_load((RACINE / "lexique.yaml").read_text(encoding="utf-8"))
    catalogue = construire(lexique)
    t = Traducteur()

    echecs = 0
    sans_exemple = [
        nom for nom, corps in (lexique.get("intentions") or {}).items()
        if not str(corps.get("exemple_nl") or "").strip()
    ]

    # Une intention sans exemple est invisible dans le catalogue : elle
    # existe dans le moteur et n'est découvrable nulle part. C'est un trou de
    # découvrabilité, pas seulement une coquette de documentation.
    for nom in sans_exemple:
        print(f"  ÉCHEC — l'intention « {nom} » n'a pas d'exemple_nl, "
              f"elle n'apparaîtra dans aucun catalogue")
        echecs += 1

    for entree in catalogue:
        phrase = entree["phrase"]
        trad = t.traduire(phrase)

        if trad.statut == "incompris":
            print(f"  ÉCHEC — « {phrase} » ({entree['intention']}) est au catalogue "
                  f"mais retombe en incompris")
            print(f"    notes : {trad.notes}")
            print(f"    mots inconnus : {trad.non_reconnus}")
            echecs += 1
            continue

        # Un mot du catalogue que le traducteur laisse tomber signalerait une
        # phrase d'exemple mal choisie — l'utilisateur la recopierait et
        # récolterait un avertissement dès son premier essai.
        if trad.non_reconnus or trad.ignores:
            print(f"  ÉCHEC — « {phrase} » ({entree['intention']}) laisse des mots "
                  f"de côté : inconnus={trad.non_reconnus} ignorés={trad.ignores}")
            echecs += 1
            continue

        # `compris` doit aller jusqu'au bout du rendu : une IR que le
        # générateur refuse serait une promesse creuse elle aussi.
        if trad.statut == "compris":
            try:
                t.rendre(trad)
            except Exception as err:                      # noqa: BLE001
                print(f"  ÉCHEC — « {phrase} » se traduit mais ne se rend pas : {err}")
                echecs += 1

        if not entree["description"]:
            print(f"  ÉCHEC — « {phrase} » n'a pas de description à afficher")
            echecs += 1

    total = len(catalogue)
    if echecs:
        print(f"\n{echecs} problème(s) sur {total} phrases de catalogue.")
        return 1
    print(f"{total} phrases de catalogue, {len(lexique['intentions'])} intentions "
          f"— toutes traduisibles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

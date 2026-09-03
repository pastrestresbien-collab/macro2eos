#!/usr/bin/env python3
"""Compile le catalogue des phrases que le traducteur sait comprendre.

À quoi ça sert
--------------
L'app présentait jusqu'ici un champ de saisie vide. Derrière ce champ, le
lexique connaît 23 intentions et un peu plus de cent mots déclencheurs, sans
qu'aucun écran ne dise jamais lesquels — et la détection d'intention exige une
correspondance EXACTE (voir `Traducteur._groupe_servi`). L'utilisateur devait
donc deviner. C'est le « problème d'habitabilité » classique des interfaces en
langage naturel : il ne se corrige pas en comprenant mieux, mais en MONTRANT
les limites.

Ce catalogue est cette monstration : une phrase concrète par capacité, dans le
format exact que l'utilisateur devra taper ensuite.

Ce n'est PAS une deuxième source
---------------------------------
Comme `build_vocabulaire_llm.py`, ce script lit le même `lexique.yaml` que tout
le reste, et n'en extrait que ce qui y est déjà écrit : `description` (ce que
fait l'intention, en français) et `exemple_nl` (la phrase d'exemple). Rien
n'est rédigé ici. Une liste d'exemples écrite à la main dériverait du lexique
au premier ajout d'intention — et un catalogue qui ment sur ce que l'app sait
faire est pire que pas de catalogue du tout.

Plusieurs exemples pour une même intention se déclarent dans `exemple_nl`
séparés par « ; » (ex. `bump_sub`, `arreter_effet`).

Garantie
--------
`test_catalogue.py` rejoue CHAQUE phrase du catalogue contre le vrai
traducteur et échoue si l'une d'elles retombe en `incompris`. Le catalogue ne
peut donc pas promettre une phrase qui ne marche pas.

Usage:
    python3 traducteur/build_catalogue.py

Produit `traducteur/dist/catalogue.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

RACINE = Path(__file__).parent
DIST = RACINE / "dist"


def exemples_de(corps: dict) -> list[str]:
    """Les phrases d'exemple d'une intention, une par entrée de catalogue.

    « ; » sépare plusieurs exemples dans un même `exemple_nl` — c'est la
    convention déjà en place dans lexique.yaml, pas une invention d'ici.
    """
    brut = str(corps.get("exemple_nl") or "").strip()
    return [phrase.strip() for phrase in brut.split(";") if phrase.strip()]


def construire(lexique: dict) -> list[dict]:
    """Une entrée par phrase d'exemple, dans l'ordre du lexique.

    L'ordre du lexique est celui de la priorité de détection d'intention (la
    plus spécifique d'abord, voir `Traducteur._intention`) — le conserver rend
    le catalogue lisible dans le même ordre que le moteur raisonne.
    """
    entrees: list[dict] = []
    for nom, corps in (lexique.get("intentions") or {}).items():
        description = corps.get("description", "")
        for phrase in exemples_de(corps):
            entrees.append({
                "intention": nom,
                "phrase": phrase,
                "description": description,
            })
    return entrees


def main() -> int:
    lexique = yaml.safe_load((RACINE / "lexique.yaml").read_text(encoding="utf-8"))
    catalogue = construire(lexique)
    DIST.mkdir(exist_ok=True)
    cible = DIST / "catalogue.json"
    cible.write_text(
        json.dumps(catalogue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"  → {cible.relative_to(RACINE.parent)} ({len(catalogue)} phrases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

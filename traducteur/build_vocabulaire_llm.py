#!/usr/bin/env python3
"""Compile un résumé compact de `lexique.yaml`, pensé pour un prompt LLM.

Ce n'est PAS une deuxième source : ce script lit exactement le même
`lexique.yaml` que `build.py` compile en entier, et n'en extrait que les clés
canoniques (jamais les alias, jamais les champs `source`/`choix`/`origine`,
qui n'apportent rien à un LLM et gonfleraient le prompt pour rien). Le moteur
flou ne doit jamais désigner autre chose que ces clés — voir
`Traducteur.interpreter_flou` (traducteur.py) pour la validation qui l'impose.

Un mot ambigu peut recevoir une courte note via le champ optionnel
`description_llm:` sur son entrée dans lexique.yaml (ex. « chaud »/« froid »,
familles de couleur et non des températures). Sans ce champ, la clé seule
sert de description.

Usage:
    python3 traducteur/build_vocabulaire_llm.py

Produit `traducteur/dist/vocabulaire_llm.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

RACINE = Path(__file__).parent
DIST = RACINE / "dist"

# Sections indexées par `Traducteur._indexer` (traducteur.py) — les seules
# familles de mots que le moteur flou a le droit de désigner.
SECTIONS_VOCABULAIRE = ["objets", "objets_cible", "nuanciers", "couleurs", "cue_cibles"]


def _entree_compacte(cle: str, corps: dict) -> dict:
    out = {"cle": cle}
    if corps.get("description_llm"):
        out["description"] = corps["description_llm"]
    return out


def construire(lexique: dict) -> dict:
    vocabulaire: dict = {}

    for section in SECTIONS_VOCABULAIRE:
        corps_section = lexique.get(section) or {}
        vocabulaire[section] = [
            _entree_compacte(cle, corps) for cle, corps in corps_section.items()
        ]

    intentions = {}
    for nom, corps in (lexique.get("intentions") or {}).items():
        intentions[nom] = {
            "description": corps.get("description", ""),
            "champs": list((corps.get("declencheurs") or {}).keys()),
        }
    vocabulaire["intentions"] = intentions

    return vocabulaire


def main() -> int:
    lexique = yaml.safe_load((RACINE / "lexique.yaml").read_text(encoding="utf-8"))
    vocabulaire = construire(lexique)
    DIST.mkdir(exist_ok=True)
    cible = DIST / "vocabulaire_llm.json"
    cible.write_text(
        json.dumps(vocabulaire, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"  → {cible.relative_to(RACINE.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

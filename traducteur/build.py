#!/usr/bin/env python3
"""Compile lexique.yaml en JSON.

Même principe que `grammar/build.py` : le YAML reste la source (commentaires,
diffs Git lisibles), le JSON est l'artefact consommé par du code qui ne peut
pas dépendre de PyYAML — notamment le prototype navigateur, où faire tourner
un parseur YAML dans Pyodide demanderait un paquet WASM supplémentaire pour
rien, alors que `json` fait déjà partie de la bibliothèque standard.

Usage:
    python3 traducteur/build.py

Produit `traducteur/dist/lexique.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

RACINE = Path(__file__).parent
DIST = RACINE / "dist"


def main() -> int:
    lexique = yaml.safe_load((RACINE / "lexique.yaml").read_text(encoding="utf-8"))
    DIST.mkdir(exist_ok=True)
    cible = DIST / "lexique.json"
    cible.write_text(
        json.dumps(lexique, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"  → {cible.relative_to(RACINE.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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


def verifier_observations_llm_recurrentes(observations_llm: dict) -> list[str]:
    """Avertit (jamais ne bloque) quand un même mot/expression revient
    plusieurs fois dans le journal de renforcement du moteur flou sans avoir
    été promu ni explicitement rejeté — signe qu'un vrai trou de vocabulaire
    se répète sans qu'on l'ait encore traité. Même esprit que
    `grammar.build.verifier_refus_non_reportes`, adapté à un journal de
    vocabulaire plutôt qu'à un journal de légalité console : voir
    `traducteur/observations_llm.yaml` pour le détail des champs."""
    en_attente: dict[str, int] = {}
    for obs in observations_llm.get("observations", []):
        if obs.get("promu") == "non":
            mot = obs.get("mot_ou_expression", "?")
            en_attente[mot] = en_attente.get(mot, 0) + 1
    return [
        f"« {mot} » revient {n} fois dans observations_llm.yaml sans être promu ni rejeté "
        f"— vrai trou de vocabulaire probable, à trancher"
        for mot, n in sorted(en_attente.items()) if n >= 2
    ]


def main() -> int:
    lexique = yaml.safe_load((RACINE / "lexique.yaml").read_text(encoding="utf-8"))
    DIST.mkdir(exist_ok=True)
    cible = DIST / "lexique.json"
    cible.write_text(
        json.dumps(lexique, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"  → {cible.relative_to(RACINE.parent)}")

    obs_path = RACINE / "observations_llm.yaml"
    if obs_path.exists():
        observations_llm = yaml.safe_load(obs_path.read_text(encoding="utf-8")) or {}
        print(f"  {len(observations_llm.get('observations', []))} observation(s) LLM enregistrée(s)")
        for avertissement in verifier_observations_llm_recurrentes(observations_llm):
            print(f"  ATTENTION : {avertissement}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

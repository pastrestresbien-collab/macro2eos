#!/usr/bin/env bash
# Régénère app/data/ à partir des sources canoniques.
#
# app/data/ n'est PAS une source — c'est une copie figée, faite pour être
# servie telle quelle au navigateur (Pyodide n'a pas accès au reste du dépôt,
# et fetch() de fichiers locaux hors de app/ échoue en file:// de toute façon).
# La source de vérité reste grammar/modele.yaml et traducteur/lexique.yaml,
# et le code reste grammar/generateur.py et traducteur/traducteur.py.
#
# À relancer après TOUTE modification de ces quatre fichiers, sinon le
# prototype teste une version périmée du corpus sans que rien ne le signale.
#
#     ./app/build_data.sh
set -euo pipefail
cd "$(dirname "$0")/.."

python3 -c "
import json, yaml
from pathlib import Path
for paquet in ('grammar', 'traducteur'):
    src = Path(paquet) / ('modele.yaml' if paquet == 'grammar' else 'lexique.yaml')
    data = yaml.safe_load(src.read_text(encoding='utf-8'))
    nom = 'modele.json' if paquet == 'grammar' else 'lexique.json'
    dst = Path('app/data') / nom
    dst.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'  {src} -> {dst}')
"

cp grammar/generateur.py app/data/generateur.py
cp traducteur/traducteur.py app/data/traducteur.py
echo "  grammar/generateur.py -> app/data/generateur.py"
echo "  traducteur/traducteur.py -> app/data/traducteur.py"

echo "app/data/ à jour."

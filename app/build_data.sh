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
#     ./app/build_data.sh              régénère app/data/
#     ./app/build_data.sh --verifier   ne touche à rien, échoue si périmé
#
# Le mode --verifier existe parce que l'avertissement ci-dessus ne suffisait
# pas : le 2026-08-28, quatre corrections du traducteur ont failli être
# déployées avec un app/data/ vieux de deux semaines — l'app servait alors
# l'ANCIEN moteur, tests au vert et correctifs invisibles, sans le moindre
# signal. Il tourne désormais en tête du workflow de déploiement, où un
# app/data/ périmé fait échouer la publication au lieu de la réussir avec le
# mauvais contenu.
set -euo pipefail
cd "$(dirname "$0")/.."

MODE=generer
if [ "${1:-}" = "--verifier" ]; then
  MODE=verifier
elif [ -n "${1:-}" ]; then
  echo "usage: $0 [--verifier]" >&2
  exit 2
fi

DEST=app/data
if [ "$MODE" = verifier ]; then
  DEST=$(mktemp -d)
  trap 'rm -rf "$DEST"' EXIT
fi

DEST="$DEST" python3 -c "
import json, os, sys, yaml
from pathlib import Path
dest = Path(os.environ['DEST'])
for paquet in ('grammar', 'traducteur'):
    src = Path(paquet) / ('modele.yaml' if paquet == 'grammar' else 'lexique.yaml')
    data = yaml.safe_load(src.read_text(encoding='utf-8'))
    nom = 'modele.json' if paquet == 'grammar' else 'lexique.json'
    dst = dest / nom
    dst.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'  {src} -> app/data/{nom}')

# Vocabulaire fermé pour le moteur flou (LLM) — réutilise le même
# constructeur que traducteur/build_vocabulaire_llm.py, jamais une
# deuxième description écrite à la main.
sys.path.insert(0, 'traducteur')
from build_vocabulaire_llm import construire
lexique = yaml.safe_load(Path('traducteur/lexique.yaml').read_text(encoding='utf-8'))
(dest / 'vocabulaire_llm.json').write_text(
    json.dumps(construire(lexique), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('  traducteur/lexique.yaml -> app/data/vocabulaire_llm.json (vocabulaire moteur flou)')
"

cp grammar/generateur.py "$DEST/generateur.py"
cp traducteur/traducteur.py "$DEST/traducteur.py"
echo "  grammar/generateur.py -> app/data/generateur.py"
echo "  traducteur/traducteur.py -> app/data/traducteur.py"

if [ "$MODE" = verifier ]; then
  if diff -rq "$DEST" app/data >/dev/null 2>&1; then
    echo "app/data/ est à jour."
  else
    echo >&2
    echo "ÉCHEC — app/data/ ne correspond plus à ses sources :" >&2
    diff -rq "$DEST" app/data >&2 || true
    echo >&2
    echo "L'app servirait une version périmée du moteur, sans le signaler." >&2
    echo "Lancer ./app/build_data.sh puis committer le résultat." >&2
    exit 1
  fi
else
  echo "app/data/ à jour."
fi

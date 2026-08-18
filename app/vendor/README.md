# app/vendor/pyodide/ — runtime Python compilé en WebAssembly

Vendu directement dans le dépôt (pas chargé depuis un CDN), pour deux raisons :

1. **Réseau restreint dans cet environnement de développement** (voir `CLAUDE.md`
   règle n°1) — l'accès à `cdn.jsdelivr.net`, où Pyodide est distribué par défaut,
   est bloqué ici. Vendre le runtime permet de tester réellement l'intégration
   (`app/engine.js`) avant de la livrer, plutôt que d'écrire du code jamais exécuté.
2. **Fonctionne sans dépendre d'un tiers qui reste en ligne** — une fois ces fichiers
   présents, `app/prototype.html` n'a plus besoin d'Internet pour faire tourner le
   vrai traducteur (seule la console reste hors de portée, ce qui est normal).

## Origine

- Paquet npm officiel `pyodide`, version **0.26.2** — récupéré via
  `npm pack pyodide@0.26.2` (le registre npm est accessible dans cet environnement,
  contrairement au CDN habituel de Pyodide).
- Fichiers conservés : `pyodide.js`, `pyodide.asm.js`, `pyodide.asm.wasm`,
  `python_stdlib.zip`, `pyodide-lock.json` — le runtime minimal pour exécuter du
  Python pur. Aucun paquet supplémentaire (numpy, pyyaml...) n'est vendu : le
  traducteur n'en a besoin d'aucun, voir `app/engine.js` pour pourquoi (JSON plutôt
  que YAML côté navigateur).
- Fichiers du paquet npm **non conservés** : `pyodide.d.ts`, `ffi.d.ts` (types,
  inutiles à l'exécution), `pyodide.js.map`/`pyodide.mjs.map` (sourcemaps),
  `console.html`, `README.md`, `package.json` du paquet lui-même.

## Mettre à jour

Pas de mécanisme automatique. Pour changer de version :

```bash
npm pack pyodide@<version>
tar xzf pyodide-<version>.tgz
cp package/{pyodide.js,pyodide.asm.js,pyodide.asm.wasm,python_stdlib.zip,pyodide-lock.json} \
   app/vendor/pyodide/
```

Puis retester (`app/build_data.sh` suivi d'un chargement réel dans un navigateur,
pas seulement `python3 traducteur/test_traducteur.py`).

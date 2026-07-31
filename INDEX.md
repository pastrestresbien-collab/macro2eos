# macro2eos — Corpus de référence ETC Eos

Corpus de référence sur la syntaxe et la grammaire des consoles ETC Eos,
destiné à un outil de traduction langage naturel → macros Eos (injection OSC / ASCII).

## Corpus de collecte (grammaire, macros, risques)

| Document | Emplacement | Statut |
|---|---|---|
| Corpus EOS complet — 34 vagues, entrées #001-174, grammaire consolidée, référentiel de risques | [`corpus/CORPUS_EOS_COMPLET.md`](corpus/CORPUS_EOS_COMPLET.md) | ✅ Quasi complet (manquent uniquement le titre et les premières lignes de l'entrée #154, lacune marquée dans le fichier) |

## Manuels convertis en Markdown

| # | Document | Dossier | Statut |
|---|----------|---------|--------|
| 1 | Eos Family Operations Manual (v2.7.0+ / v3.x) | [`manuals/operations-manual/`](manuals/operations-manual/) | 🟡 Partie 1 convertie (Introduction, Concepts, System Basics) — reste du PDF en attente (accès réseau bloqué — voir `SOURCES.md`) |
| 2 | Eos Family Show Control User Guide (Rev C) | [`manuals/show-control-guide/`](manuals/show-control-guide/) | ⏳ En attente du PDF |
| 3 | Eos Family L1 Essentials Workbook (v3.3B) | [`manuals/l1-essentials-workbook/`](manuals/l1-essentials-workbook/) | ⏳ En attente du PDF |
| 4 | Eos Family L3 Advanced/Intermediate Workbook (v3.3B) | [`manuals/l3-advanced-workbook/`](manuals/l3-advanced-workbook/) | ⏳ En attente du PDF |
| 5 | Eos Family L4 Proficient Workbook (v3.3B) | [`manuals/l4-proficient-workbook/`](manuals/l4-proficient-workbook/) | ⏳ En attente du PDF |
| 6 | Eos Family Hotkeys v3.0.0 (Rev A, 2020-08) | [`manuals/hotkeys/`](manuals/hotkeys/) | ✅ Converti intégralement (PDF source inclus) |
| 7 | Eos Integration via OSC (Eos 2.6.0, 2017) | [`manuals/osc-integration/`](manuals/osc-integration/) | ✅ Converti intégralement (PDF source inclus) |

## Organisation

- `manuals/<document>/` — un dossier par manuel. Chaque dossier contiendra :
  - `00-index.md` — table des matières du document avec liens vers les chapitres
  - `NN-<chapitre>.md` — un fichier par chapitre, texte intégral (pas de résumé)
- `manuals/<document>/source/` — déposer ici le PDF officiel correspondant
  (voir `SOURCES.md` pour les URLs exactes) ; la conversion intégrale en `.md`
  est faite à partir de ce PDF.
- `SOURCES.md` — URLs officielles vérifiées de chaque PDF + miroirs.

## Règle de fidélité

Le corpus est une référence technique : le texte des manuels est converti
**intégralement**, sans résumé ni raccourci. Seule la mise en forme est adaptée
(titres, tableaux, listes Markdown).

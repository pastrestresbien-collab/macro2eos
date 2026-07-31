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
| 1 | Eos Family Operations Manual (v2.7.0+ / v3.x) | [`manuals/operations-manual/`](manuals/operations-manual/) | 🟡 Partie 1 convertie (Introduction, Concepts, System Basics) — PDF complet toujours attendu |
| 2 | Eos Family Show Control User Guide (Rev C) | [`manuals/show-control-guide/`](manuals/show-control-guide/) | ⏳ En attente du PDF |
| 3 | Eos Family L1 Essentials Workbook (v3.3C, 2026-05) | [`manuals/l1-essentials-workbook/`](manuals/l1-essentials-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 4 | Eos Family L2 Enhanced Workbook (v3.3C, 2026-05) | [`manuals/l2-enhanced-workbook/`](manuals/l2-enhanced-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 5 | Eos Family L3 Intermediate Workbook (v3.3C, 2026-05) | [`manuals/l3-advanced-workbook/`](manuals/l3-advanced-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 6 | Eos Family L4 Proficient Workbook (v3.3C, 2026-02) | [`manuals/l4-proficient-workbook/`](manuals/l4-proficient-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 7 | Eos Family Hotkeys v3.0.0 (Rev A, 2020-08) | [`manuals/hotkeys/`](manuals/hotkeys/) | ✅ Converti intégralement (PDF source inclus) |
| 8 | Eos Integration via OSC (Eos 2.6.0, 2017) | [`manuals/osc-integration/`](manuals/osc-integration/) | ✅ Converti intégralement (PDF source inclus) |
| 9 | Eos Family Magic Sheet Intensive Workbook (v3.0.1A, 2021-02) | [`manuals/magic-sheets-workbook/`](manuals/magic-sheets-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 10 | Eos Family Effects Intensive Workbook (v3.0.1B, 2021-07) | [`manuals/effects-workbook/`](manuals/effects-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 11 | Busking with the Eos Family Workbook (v3.0.1, 2021-04) | [`manuals/busking-workbook/`](manuals/busking-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 12 | Intro to Augment3d Workbook (v3.0 Rev B, 2020-11) | [`manuals/augment3d-workbook/`](manuals/augment3d-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 13 | Virtual Media Server & Pixel Map Control Workbook (v3.0.0A, 2020-12) | [`manuals/virtual-media-server-workbook/`](manuals/virtual-media-server-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 14 | White Paper « Entertainment Lighting Control Philosophy » (ETC, 2009) | [`manuals/control-philosophy-whitepaper/`](manuals/control-philosophy-whitepaper/) | ✅ Converti intégralement (PDF source inclus) |

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

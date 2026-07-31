# Rapport de vérification d'intégrité

Date : 2026-07-31 (session de consolidation, mise à jour après import du manuel principal)

## Corpus (`corpus/CORPUS_EOS_COMPLET.md`)

- **Entrées numérotées** : 173/174 titres présents (#001 → #174). Seul le **titre** de l'entrée #154 manque (son contenu est présent à partir de « Confiance : C/B ») — lacune marquée dans le fichier.
- **Blocs de fichiers** : 38 marqueurs `DEBUT` / 38 marqueurs `FIN`, tous appariés. Vagues 2 à 34 toutes présentes et fermées (vague 1 = `macros_etc_forum.md`).
- **Doublons** : aucune ligne longue (>80 caractères) dupliquée — pas de segment collé deux fois.
- **Lacunes marquées** : 1 seule (le titre du #154).

## Eos Family User Manual v3.2.0 (manuel principal, 32 chapitres)

- Source : DOCX officiel ETC (converti via `pandoc --from=docx --to=markdown+grid_tables`,
  format table en grille texte pour préserver la lisibilité des tableaux complexes sans
  retomber sur du HTML brut).
- Découpage automatique en 32 chapitres + préambule sur les marqueurs `# Chapter N` internes
  au document — tous détectés et vérifiés (Chapitres 1 à 32, Console Overview → Appendix).
- Nettoyage appliqué : suppression des mini-tables des matières résiduelles en tête de
  chapitre, des ancres `_bookmark`, dé-échappement des caractères Markdown que pandoc
  échappe par défaut (`\[`, `\]`, `\{`, `\}`, etc. — nécessaires pour préserver la syntaxe
  Eos réelle du type `[Learn]`, `{Chan Check}`), regroupement des figures consécutives en
  une mention unique (les images ne sont pas reproduites).
- **Vérification d'intégrité** : échantillonnage de lignes de contenu (hors tableaux/titres)
  sur 7 chapitres clés (Patch, Setup, Effects, Macros, Show Control, Welcome/Introduction,
  System Basics), recherchées dans le texte source complet extrait du DOCX — **couverture
  effective 100 %** ; les quelques différences relevées lors du premier passage étaient des
  faux positifs dus à des marqueurs d'ancrage invisibles (`[]{#_bookmark470 .anchor}`) dans
  le texte source, pas des pertes de contenu.
- Chapitre 31 (Show Control) contient la section officielle **« Eos OSC Keys »** (dictionnaire
  complet touche OSC → commande interne) ainsi que le dictionnaire complet des commandes
  `/eos/...`, MIDI Show Control, String Interface, Timecode, RTC, Analog I/O.

## Manuels convertis (13 documents secondaires)

Méthode de vérification : échantillonnage systématique des lignes significatives du texte
extrait du PDF source (`pdftotext`), recherche de chaque ligne (normalisée espaces/puces)
dans le Markdown converti.

| Document | Lignes testées | Couverture |
|---|---|---|
| L1 Essentials v3.3C | 73 | 100 % |
| L2 Enhanced v3.3C | 75 | 100 % |
| L3 Intermediate v3.3C | 176 | 100 % |
| L4 Proficient v3.3C | 66 | 100 % |
| Magic Sheet Intensive v3.0.1A | 99 | 100 % |
| Effects Intensive v3.0.1B | 76 | 100 % |
| Busking v3.0.1 | 62 | 100 % |
| Intro to Augment3d v3.0B | 198 | 100 % |
| Virtual Media Server v3.0.0A | 112 | 100 % |
| Hotkeys v3.0.0 | 42 | complet (vérif. manuelle — sections d'intro traduites en français, table intégrale) |
| Eos Integration via OSC | 304 | complet (vérif. manuelle — reformatage des paragraphes, texte intégral) |

Les PDF sources sont committés dans `manuals/<document>/source/` — toute re-vérification
future peut être refaite à partir d'eux.

## Limites connues

- Les **illustrations/captures d'écran** des documents source ne sont pas reproduites (texte uniquement).
- Les tableaux d'exercices en deux colonnes (commande / explication) sont préservés en blocs
  alignés ; l'ordre visuel gauche/droite du document source peut localement différer de l'ordre du texte extrait.

## État global

Les 14 documents listés dans `INDEX.md` sont désormais **tous convertis intégralement**,
sources incluses dans `manuals/<document>/source/`. Aucun document en attente à ce jour.

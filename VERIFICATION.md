# Rapport de vérification d'intégrité

Date : 2026-07-31 (session de consolidation)

## Corpus (`corpus/CORPUS_EOS_COMPLET.md`)

- **Entrées numérotées** : 173/174 titres présents (#001 → #174). Seul le **titre** de l'entrée #154 manque (son contenu est présent à partir de « Confiance : C/B ») — lacune marquée dans le fichier.
- **Blocs de fichiers** : 38 marqueurs `DEBUT` / 38 marqueurs `FIN`, tous appariés. Vagues 2 à 34 toutes présentes et fermées (vague 1 = `macros_etc_forum.md`).
- **Doublons** : aucune ligne longue (>80 caractères) dupliquée — pas de segment collé deux fois.
- **Lacunes marquées** : 1 seule (le titre du #154).

## Manuels convertis (11 documents)

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

- Les **illustrations/captures d'écran** des PDF ne sont pas reproduites (texte uniquement).
- Les tableaux d'exercices en deux colonnes (commande / explication) sont préservés en blocs
  alignés ; l'ordre visuel gauche/droite du PDF peut localement différer de l'ordre du texte extrait.
- `manuals/operations-manual/` : seule la partie 1 existe (Introduction, Concepts, System
  Basics) — le PDF complet n'a pas encore été fourni.
- `manuals/show-control-guide/` : aucun contenu reçu à ce jour.

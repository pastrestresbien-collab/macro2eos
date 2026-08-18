# macro2eos — Corpus de référence ETC Eos

Corpus de référence sur la syntaxe et la grammaire des consoles ETC Eos,
destiné à un outil de traduction langage naturel → macros Eos (injection OSC / ASCII).

**Point d'entrée** : [`reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md`](reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md)
pour la syntaxe Eos de référence · [`PLANNING.md`](PLANNING.md) pour l'état d'avancement
et le backlog de travail · [`REGLES_POUR_UI.md`](REGLES_POUR_UI.md) pour **développer
l'interface** : les neuf règles de la grammaire qui contraignent l'UI, et pourquoi.

## Corpus de collecte (grammaire, macros, risques)

| Document | Emplacement | Statut |
|---|---|---|
| Corpus EOS complet — 34 vagues, entrées #001-174, grammaire consolidée, référentiel de risques | [`corpus/CORPUS_EOS_COMPLET.md`](corpus/CORPUS_EOS_COMPLET.md) | ✅ Quasi complet (manquent uniquement le titre et les premières lignes de l'entrée #154, lacune marquée dans le fichier) |

## Référence canonique

| Document | Emplacement | Statut |
|---|---|---|
| `eosKeys.ts` — 1155 touches OSC officielles (projet xtouch2Eos), nom OSC → commande interne | [`reference/eosKeys.ts`](reference/eosKeys.ts) | ✅ Reçu, intégré tel quel |
| Comparaison eosKeys.ts ↔ table officielle « Eos OSC Keys » du manuel v3.2.0 | [`reference/eosKeys_vs_manual_comparison.md`](reference/eosKeys_vs_manual_comparison.md) | ✅ 1152/1155 entrées identiques ; écarts documentés (résout corpus #148) |
| Journal d'observations terrain nomad réel (projet xtouch2Eos, source de la vague 28) | [`reference/JOURNAL_observations_nomad.md`](reference/JOURNAL_observations_nomad.md) | ✅ Reçu, intégré tel quel (source S) |
| Compléments du journal utiles à macro2eos (au-delà de la vague 28) | [`reference/JOURNAL_nomad_complements.md`](reference/JOURNAL_nomad_complements.md) | ✅ `/eos/macro/.../fire` confirmé, Assert sans mot-clé cmd, syntaxe wheel coarse/fine/home |
| EOS OSC Support — Supported OSC Commands (ETCLabs/EosSyncLib, 2017) | [`reference/Supported_OSC_Commands.md`](reference/Supported_OSC_Commands.md) | ✅ Converti intégralement (PDF source inclus) — colonne « Min Eos Version » par commande, absente du manuel v3.2.0 |
| `fakeeos.ts` — simulateur ETCnomad minimal (transport OSC/TCP, projet xtouch2Eos) + client de test | [`reference/tools/`](reference/tools/) | ✅ Reçu et testé bout en bout (voir `reference/tools/README.md`) — valide le transport, pas la grammaire Eos |
| **Grammaire ETC Eos consolidée** — synthèse de référence (corpus 174 entrées + manuel v3.2.0 32 chapitres + workbooks + eosKeys.ts + OSC docs), 15 sections, remplace la grammaire consolidée historique du corpus | [`reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md`](reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md) | ✅ Rédigée à partir de l'ensemble du corpus disponible |
| Table Lee Filters (théâtre) — numéro de gel par teinte nommée, hors ETC | [`reference/lee_filters_theatre.md`](reference/lee_filters_theatre.md) | ✅ Catalogue officiel Lee « Art of Light » (~2007) reçu et intégré — gamme couleur complète (~230 teintes, nom + description officielle), PDF source conservé — `PLANNING.md` #34 |

## Grammaire exploitable par le code

| Document | Emplacement | Statut |
|---|---|---|
| Modèle Eos typé (objets/actions/matrice de légalité), patrons, générateur IR → commande, injection OSC | [`grammar/`](grammar/README.md) | ✅ v0.16 — 79 actions, 164 règles, 113 tests |
| Traducteur français → IR (lexique, intentions, questions) — entre en amont du générateur | [`traducteur/`](traducteur/README.md) | 🚧 v0.2 — 9 intentions, 9 couleurs, 39 tests. Déterministe, sans IA à l'exécution |

Le modèle couvre : sélection, Fan, cues (simples, multipart, listes multiples), macros,
submasters, Query, effets, palettes, presets, groupes, patch, mark, park, filtres, courbes,
snapshots, magic sheets, show control, contrôle partitionné, contexte d'écran, terminaison,
et l'injection OSC. Hors périmètre : Augment3d, pixel mapping, serveur média virtuel,
multi-console, et l'export ASCII faute de spécification (voir `PLANNING.md` #32).

**25 zones non tranchées** y sont déclarées `inconnu` et reliées au backlog : le modèle
avertit au lieu d'injecter en aveugle. Voir [`VERIFICATION.md`](VERIFICATION.md) pour la
méthode et [`PLANNING.md`](PLANNING.md) pour les points à valider au banc.

## Manuels convertis en Markdown

| # | Document | Dossier | Statut |
|---|----------|---------|--------|
| 1 | Eos Family User Manual v3.2.0 (réf. 4250M1210-3.2.0 Rev A, 2023-04) | [`manuals/operations-manual/`](manuals/operations-manual/) | ✅ Converti intégralement, 32 chapitres (DOCX source inclus) — contient Patch, Setup, Effects, Macros, **Show Control (dictionnaire OSC complet + Eos OSC Keys)** |
| 2 | Eos Family L1 Essentials Workbook (v3.3C, 2026-05) | [`manuals/l1-essentials-workbook/`](manuals/l1-essentials-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 3 | Eos Family L2 Enhanced Workbook (v3.3C, 2026-05) | [`manuals/l2-enhanced-workbook/`](manuals/l2-enhanced-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 4 | Eos Family L3 Intermediate Workbook (v3.3C, 2026-05) | [`manuals/l3-advanced-workbook/`](manuals/l3-advanced-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 5 | Eos Family L4 Proficient Workbook (v3.3C, 2026-02) | [`manuals/l4-proficient-workbook/`](manuals/l4-proficient-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 6 | Eos Family Hotkeys v3.0.0 (Rev A, 2020-08) | [`manuals/hotkeys/`](manuals/hotkeys/) | ✅ Converti intégralement (PDF source inclus) |
| 7 | Eos Integration via OSC (Eos 2.6.0, 2017) | [`manuals/osc-integration/`](manuals/osc-integration/) | ✅ Converti intégralement (PDF source inclus) |
| 8 | Eos Family Magic Sheet Intensive Workbook (v3.0.1A, 2021-02) | [`manuals/magic-sheets-workbook/`](manuals/magic-sheets-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 9 | Eos Family Effects Intensive Workbook (v3.0.1B, 2021-07) | [`manuals/effects-workbook/`](manuals/effects-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 10 | Busking with the Eos Family Workbook (v3.0.1, 2021-04) | [`manuals/busking-workbook/`](manuals/busking-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 11 | Intro to Augment3d Workbook (v3.0 Rev B, 2020-11) | [`manuals/augment3d-workbook/`](manuals/augment3d-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 12 | Virtual Media Server & Pixel Map Control Workbook (v3.0.0A, 2020-12) | [`manuals/virtual-media-server-workbook/`](manuals/virtual-media-server-workbook/) | ✅ Converti intégralement (PDF source inclus) |
| 13 | White Paper « Entertainment Lighting Control Philosophy » (ETC, 2009) | [`manuals/control-philosophy-whitepaper/`](manuals/control-philosophy-whitepaper/) | ✅ Converti intégralement (PDF source inclus) |

## Organisation

- `manuals/<document>/` — un dossier par manuel. Le manuel principal
  (`operations-manual/`) est découpé en un fichier par chapitre
  (`00-INDEX.md` + `NN-<chapitre>.md`) ; les autres documents sont un
  fichier unique par manuel, texte intégral (pas de résumé).
- `manuals/<document>/source/` — PDF/DOCX officiel correspondant, conservé **en
  archive uniquement** pour re-vérification ou re-conversion future. Ne pas
  consulter systématiquement (fichiers volumineux, jusqu'à 15 Mo) : travailler
  à partir des `.md` déjà convertis, n'ouvrir la source que sur besoin précis
  et avéré (voir `CLAUDE.md`, règle n°2).
- `SOURCES.md` — URLs officielles vérifiées de chaque document + miroirs.
- `VERIFICATION.md` — rapport d'intégrité (couverture texte source ↔ Markdown).
- `PLANNING.md` — état d'avancement, axes de travail, backlog unique des points à
  valider au banc réel. Volontairement court (relu à chaque session) ; le récit
  détaillé, daté, tranche par tranche est dans `PLANNING_HISTORIQUE.md` — à consulter
  sur besoin précis, pas à relire systématiquement.
- `APP.md` — spécification produit : décisions, flux, contraintes techniques établies.
- `REGLES_POUR_UI.md` — cadrage pour la session qui développe l'interface : les règles
  structurantes de la grammaire Eos et ce que chacune impose à l'UI.
- `PIPELINE_TRADUCTION.md` — le déroulé en 9 étapes d'une requête, de la saisie NL à
  l'ajout au corpus (analyse, affichage par paramètre, validation, envoi, constat).
- `app/` — prototype interactif (`prototype.html`, branché sur le vrai traducteur via
  Pyodide, voir `app/engine.js`) et maquette visuelle (`maquette.html`, périmée).
- `CLAUDE.md` — règles de travail pour toute session sur ce dépôt.

## Règle de fidélité

Le corpus est une référence technique : le texte des manuels est converti
**intégralement**, sans résumé ni raccourci. Seule la mise en forme est adaptée
(titres, tableaux, listes Markdown).

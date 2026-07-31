# CORPUS EOS COMPLET — Fusion de tous les fichiers

Document unique regroupant l'index, la grammaire consolidée, le référentiel de risques,
les notes produit, et les 34 vagues de collecte détaillées.

---

<!-- ===== DEBUT : INDEX.md ===== -->

# INDEX — Corpus EOS (macros, effets, grammaire)

Dernière mise à jour : 29/07/2026 — eosKeys.ts intégré (1155 touches officielles ETC)

## ⚠️ Source de référence canonique disponible

`eosKeys.ts` (projet xtouch2Eos de Cy, extrait du PDF officiel ETC "Eos OSC Keys") est désormais **la table de référence pour toute validation de touche OSC** — 1155 entrées, niveau A. Voir vague29 pour l'intégration complète, les corrections apportées (dont résolution du conflit #145 : `go_0` = GO, pas Stop/Back) et la découverte de la famille complète des styles Fan (9+ modificateurs).

## Point d'entrée recommandé

**`GRAMMAIRE_CONSOLIDEE.md`** — vue par thématique. **`vague29_eoskeys_integration.md`** — corrections les plus importantes du corpus, à lire avant toute utilisation de la grammaire pour la conception.

## Fichiers du corpus

| Fichier | Contenu | Entrées | Confiance dominante |
|---|---|---|---|
| `macros_etc_forum.md` | Fil "Macro Favorites" — vague 1 | 001-019 | C, quelques D |
| `macros_etc_forum_vague2.md` | Fils thématiques — indirection, effets absolus | 020-025 | C |
| `macros_etc_forum_vague3.md` | Submasters — alerte critique ASCII | 026-030 | C, alerte A à vérifier |
| `macros_etc_forum_vague4.md` | Manuel officiel v3.3.6 + pièges édition | 031-037 | A dominant |
| `macros_etc_forum_vague5.md` | Palettes couleur, by-type, dummy channels | 038-043 | C, une A |
| `effets_etc_officiel_vague6.md` | Article officiel "Common Effects" — LA référence effets | 044-056 | A quasi-total |
| `groupes_etc_forum_vague7.md` | Groupes, pattern SelectLast, génération en série | 057-059 | C |
| `navigation_etc_forum_vague8.md` | Navigation/Go To Cue — fragilité macro confirmée | 060-064 | C, témoignages denses |
| `multiconsole_etc_forum_vague9.md` | Multiconsole, ciblage User OSC, bug édition concurrente | 065-069 | C, une A |
| `vague10_editing_macros_officiel.md` | Page officielle Editing Macros — macro-dans-macro confirmé A | 070-074 | A |
| `vague11_show_control_l4.md` | Doublons liste recherche, Show Control Guide, L4 Workbook | 075-078 | A dominant |
| `vague12_liste_image_F_M.md` | Transcription image liste native (F→M), ~40 termes nouveaux | 079 | A (image), termes non confirmés en syntaxe |
| `vague13_correction_greater_less_than.md` | Correction : Greater/Less Than = Query keywords, pas logique conditionnelle | 080 | B |
| `vague14_query_semantique_variables.md` | **Sémantique Query close** + confirmation ETC absence de variables — valide l'archi | 081-085 | A/B dominant |
| `vague15_securite_exploitation.md` | Sécurité/exploitation — Grand Master, Shielded, Inhibitive (première couverture) | 086-089 | A/C |
| `vague16_lamp_controls.md` | Lamp Controls — syntaxe confirmée, règle Learn-only renforcée | 090-092 | C, cohérent x2 |
| `vague17_magic_sheets_github.md` | Magic Sheets approfondi + dépôt GitHub ETC Labs identifié (à consulter) | 093-099 | C |
| `vague18_correction_etclabs.md` | Correction : ETCLabs non-officiel, PDF introuvable — piste close | 100-101 | B/C |
| `vague19_midi_show_control.md` | MIDI Show Control — commandes MSC confirmées A, QLab/OSC identifié | 102-105 | A dominant |
| `vague20_send_string_bugs_officiels.md` | **Send_String — deux bugs à tickets ETC confirmés**, règles de génération non négociables | 106-110 | B/A dominant |
| `vague21_affichage_flexi_snapshots.md` | Affichage/Flexi/Snapshots — motif de contournement générique identifié | 111-116 | A/B/C |
| `vague22_mark_automark.md` | Mark/AutoMark détaillé — confirme risque Enable/Disable, nouveau piège Blind | 117-121 | A/B/C |
| `vague23_merge_selectif_constat.md` | Merge sélectif confirmé A + alerte méthodo (contenu IA détecté en forum) | 122-124 | A/D |
| `vague24_fan_autopalette_precedent.md` | **Fan mode découvert** (4e stratégie masse) + précédent communautaire proche du projet | 125-127 | A/C |
| `vague25_confirmation_absence_autopalette.md` | **Validation stratégique majeure** : ETC confirme (2010, toujours vrai en 2024) l'absence délibérée d'auto-palette | 128 | B/A |
| `vague26_fan_syntaxe_confirmee.md` | **Correction structurelle** : Fan = mécanisme natif de `[Thru]`, pas une stratégie séparée | 129-131 | A |
| `vague27_highlight_lowlight_remdim.md` | Nouveau domaine : Highlight/Lowlight/RemDim, exemple officiel complet | 132-135 | A |
| `vague28_journal_terrain_xtouch2eos.md` | **Source S (observation terrain)** — corrections majeures, conflit à trancher | 136-145 | S |
| `vague29_eoskeys_integration.md` | **eosKeys.ts intégré** — table canonique 1155 touches, conflit #145 résolu, famille Fan complète | 146-153 | A |
| `vague30_resolution_isnt_in_syntaxe_generale.md` | **Règle Objet-Action-Cible découverte** ; logique conditionnelle définitivement fermée | 154-156 | B/C |
| `vague31_syntaxe_gel_confirmee.md` | Syntaxe Gel confirmée (`Color <bib>/<n°>`), Lee=3, limite de fidélité colorimétrique | 157-160 | A/C |
| `vague32_polysemie_contextuelle_at.md` | **Découverte S critique** : `At` polysémique selon écran (Patch≠Live) — nouvel axe de validation requis | 161 | S |
| `vague33_syntaxe_ecran_patch.md` | Syntaxe Patch complète, confirmation indépendante de la polysémie (`@` aussi) | 162-166 | A/B |
| `vague34_operations_manual_focus_tabs.md` | **Réponse directe** : navigation `Tab <n> Enter` confirmée A, table complète des 37 tabs, focus=affichage | 167-174 | A |
| `GRAMMAIRE_CONSOLIDEE.md` | Vue unique par thématique, synthèse exploitable de tout le corpus | — | — |
| `REFERENTIEL_RISQUES_ET_GRILLE.md` | Référentiel : risques contextuels + grille de collecte + taxonomie + stratégies de contournement | — | — |
| `notes_produit_futures.md` | Idées produit à traiter en conception (pas du corpus grammaire) | — | — |

**Total entrées collectées : 174**

## À partir de maintenant

- Ne plus dupliquer la liste "commandes à risque contextuel" en fin de vague — ajouter une ligne dans `REFERENTIEL_RISQUES_ET_GRILLE.md`
- Utiliser le format de fiche standardisé du référentiel pour toute nouvelle entrée
- Prioriser les thématiques encore vides : Sécurité/exploitation, Show Control détaillé, Magic Sheets, Lamp Control

## Découvertes structurantes pour l'architecture (à ne pas perdre de vue)

1. **Trois stratégies de génération en masse identifiées** (détail en fin de vague7) :
   - Spread par plage unique `[Thru] x [Thru] y` — le plus fiable (source A, #056)
   - Boucle `Macro_Loop_Begin`/`SelectLast`/`Next` — flexible (#057)
   - Indirection macro-dans-macro — le plus puissant mais confiance faible (#020)

2. **Alerte critique non résolue** : un témoignage (#027) indique qu'une macro pilotant un bump submaster (`SubDown`/`SubUp`) peut ne pas survivre à l'aller-retour ASCII. **Premier test au banc prioritaire.**

3. **Deux familles d'effets à traiter séparément dans le parseur** : Absolute Effects (référencent des palettes, `{Grouping}`, `{Action}`) vs Step-Based/Chase (channels ou groupes attachés directement aux steps)

4. **Syntaxe `{Offset} {Mirror Out}` / `{Offset} {Mirror In}`** confirmée (source A) — répond au besoin d'offset du cadrage initial

5. **Liste exhaustive des commandes macro consultable sur la console elle-même** (champ de recherche en mode édition, #033) — objectif prioritaire du premier accès matériel, potentiellement supérieure à toute doc externe

6. **Touches réellement exclues du Learn** : [Macro], flèches, [Escape], [Select], [Learn]. [Clear] N'EN FAIT PAS PARTIE — elle s'enregistre et pollue (#032), distinction fine à ne pas perdre

7. **Commandes à comportement contextuel/non-déterministe**, à signaler dans le validateur : `{Enable}/{Disable}` vs toggle, `Update` (source ambiguë), `SelectManual` (comportement différent macro vs live)

8. **Commandes à risque de non-fonctionnement malgré enregistrement réussi** : `More_SoftKeys`, `Open_Browser`

9. **Piège Scroll Lock** en édition directe — argument supplémentaire en faveur de la voie ASCII structurée

## Mots-clés/softkeys confirmés à ce stade (vocabulaire brut, non exhaustif)

Contrôle de macro : `Macro_Wait`, `Macro_Loop_Begin`, `Macro_Loop_End`, `Wait_For_Enter`, `Wait_For_Input`, `Clear_CmdLine`, `Clear_Cmd`

Sélection : `Select_Active`, `Select_Last`/`SelectLast`, `Query` (+ `Dark_Moves`, `Live_Moves`, `UpMoves`), `Flexi_Selected`, `AllNPs`

Submasters : `SubDown <n> Enter`, `SubUp <n> Enter`

Effets : `{Step Based}`, `{Absolute}`, `{Linear}`, `{Build}`, `{Bounce}`, `{Reverse}`, `{Grouping}`, `{Offset} {Mirror Out}`, `{Offset} {Mirror In}`, `{Action}`, `{On State}`, `{Off State}`, `{Random Group}`, `{Random Rate}`, `{Cycle Time}`

Palettes : `[Record] [Color Palette] [n] [Label] <nom> [Enter]`, `{By Type}`, `{Lock}`, `[Recall From]`

Divers : `[At][Enter]` (release), `Copy To`, `Move_To`, `CueOnlyTrack`, `Effect_Edit` (non confirmé fonctionnel — D)

## Prochaines thématiques à couvrir (non encore traitées en profondeur)

- Show Control (MIDI, OSC, timecode) — abordé indirectement (Learn/timecode), pas en détail
- Navigation/conduite pure (Go, Back, sauts de cue)
- Multiconsole/backup, User ID
- Sécurité/exploitation (grand master, inhibitions)
- Magic Sheets liés aux macros

<!-- ===== FIN : INDEX.md ===== -->

---

<!-- ===== DEBUT : GRAMMAIRE_CONSOLIDEE.md ===== -->

# GRAMMAIRE CONSOLIDÉE — Corpus EOS pour traducteur NL → macro

Document de synthèse unique, organisé par thématique (pas par ordre de collecte).
Les fichiers `vagueN_*.md` restent la trace d'audit détaillée (citations, contexte, sources exactes) — ce document est la vue exploitable pour la conception.
153 entrées sources, collecte du 29/07/2026 — mise à jour post-intégration eosKeys.ts (vague29).

## ⚠️ RÉFÉRENCE CANONIQUE : eosKeys.ts

`src/shared/eosKeys.ts` (projet xtouch2Eos de Cy, extrait du PDF officiel ETC "Eos OSC Keys") liste **1155 touches OSC officielles**, nom OSC → commande interne. C'est la source de vérité pour toute question "cette touche existe-t-elle, sous quel nom exact" — supérieure à toute collecte web fragmentaire de ce corpus.

**Deux nuances établies (vague29)** :
- Cette liste couvre les touches `/eos/key/<nom>`, pas nécessairement 100% du vocabulaire de grammaire ligne de commande au sens large (recoupement très large mais non total — ex: `Isn't In`/`Could Be` confirmés textuellement ailleurs mais absents de cette liste, `Group Cells`/`From Absolute` vus en image mais sans correspondance exacte)
- Toute nouvelle collecte devrait désormais vérifier systématiquement contre cette liste avant de qualifier une touche de confirmée ou introuvable

---

## 1. NAVIGATION / CONDUITE

- `Go To Cue Out [Time] [0] [Enter]` — aller à Cue Out avec temps forcé [031, A]
- `Go_To_Cue <n> Enter` — si concaténé sans espace type `Go_To_Cue_0.9`, tronque la décimale (nom réservé en collision) [060, C]
- `go_0` → `GO` (démarrage de cue) — ⚠️ CORRIGÉ vague29 : ce n'est PAS l'équivalent de Stop/Back, contrairement à ce qui avait été noté en vague 20. C'est `stopback` → `PLAYBACK_STOP_BACK` la bonne touche pour Stop/Back [146, A — eosKeys.ts]
- `GoToCue Out [Enter] / Sub 1 Thru Out [Enter]` — clear all subs + reset playback en tête de show [026]
- `[Cue] [7] {Execute} [Macro] [101] [Enter]` — lie une macro à l'exécution d'une cue
- `[Blind] [Cue] [Enter]` / `[Blind] [Sub] [Enter]` — `[Blind] [Enter]` seul est ambigu en macro, toujours qualifier l'objet cible [119, C]
- RISQUE MAJEUR : `Go_To_Cue` a un comportement non déterministe selon Foreground/Background et timing, aggravé si des movers sont dans la cue [061, C]

## 2. SÉLECTION & PATCH

- `Select_Active`, `Select_Last`/`SelectLast` — sélection courante, très utilisés en tête de macro
- `select_last_params @ +01 Enter` / `@ + -01 Enter` — incrémente/décrémente le dernier paramètre travaillé [098, C]
- Pattern `SelectLast Record Group N Enter Next` en boucle — génération de groupes en série [057, C]
- `Query <critère> {Is In}/{Isn't In}/{Could Be}/{Can't Be} [cible] [Enter]` — sémantique complète confirmée [081, A/B]. ⚠️ Nuance vague29 : seuls `is_in` et `can_be` sont confirmés comme touches OSC nommées dans eosKeys.ts (source A directe) ; `isn't_in`/`could_be` restent confirmés textuellement (vague14) mais absents de cette liste officielle — probablement une construction différente (modificateur de négation ?) plutôt qu'un mot-clé séparé. Non résolu [148].
- `Query Dark_Moves`, `Query Live_Moves`, `Query UpMoves`, `Query is_in Unpatched` — famille Query très répandue. `unpatched` → `UNPATCHED_QUERY` confirmé A [153]
- `[Query] {Unpatched} {Is In} [Cue] [1] [Thru] [Enter]` — Query combiné avec plage de cues [135, A]
- `[Group][Color Palette][1][Enter]` — Group = sélecteur pur, ne modifie pas les valeurs [082, A/B]
- `Greater Than` / `Less Than` — confirmés comme touches OSC à part entière (`greater_than`, `less_than`, eosKeys.ts, A) — existent bel et bien en tant que commandes, au-delà du seul usage Query par mots-clés [080, 147]
- `{Select Last}` après un `Query` composé — relance la syntaxe de requête au lieu de renvoyer la sélection [083, C]

## 3. PALETTES & PRESETS

- `[Record] [Color Palette] [n] [Label] <nom> [Enter]` — syntaxe normative officielle [041, A]
- `Chan <n> Color <bibliothèque> / <numéro> Enter` — sélection de gel par référence fabricant, Lee = bibliothèque 3 (confirmé A, workbook L1) [157, 158]. ⚠️ Le rendu ne correspond pas toujours fidèlement à la teinte physique réelle — limite reconnue, à traiter comme point de départ approximatif plutôt que résultat garanti [159]. Syntaxe OSC alternative possible : format `<initiale><numéro>` (ex: `L195`), distincte de la syntaxe ligne de commande — à clarifier laquelle utiliser selon le transport [160]
- `{By Type}` `{Lock}` — palette applicable à tous fixtures du même type, verrouillée
- Pattern dummy channels by-type — channels fictifs par type, groupés, pour réutiliser des palettes entre showfiles [039, C]
- Spread de 30 palettes en dégradé via double `[Thru]` + Hue [040, C]
- `{Action}[1][Thru][7][@][Color Palette] x [Thru] y [Enter]` — meilleur exemple de génération en masse du corpus [056, A]
- Piège récurrent : copier un channel réglé sur une palette copie la référence, pas le contenu, sauf `make_absolute` → `MAKE_ABSOLUTE` (confirmé A, eosKeys.ts) [042, 077, 149]. ⚠️ `{From Absolute}` vu dans l'image/workbook L4 ne correspond à aucune entrée exacte de eosKeys.ts — probablement un softkey contextuel de l'écran Copy To plutôt qu'une touche nommée du dictionnaire général, à trancher [149]
- `{Record Only}` + filtres (`[Color]`, `{Beam}`, `{Focus}`, `{Intensity}`)
- `Update` — cible ambiguë, historique confirmé A [025] ; comportement persistant entre sessions (Make Absolute/Break Nested) [126, C]
- Absence officielle et durable (2010→2024) de fonction auto-palette native — choix assumé par ETC [128, B/A]
- Précédent communautaire inachevé : "Autopalette Macros" (2024) [127, C]

## 4. EFFETS

Distinction fondamentale à toujours maintenir : **Absolute Effects** (channels assignés séparément, référencent des palettes via `{Action}`) vs **Step-Based/Chase** (channels/groupes attachés directement aux steps) [023, A].

Recettes step-based officielles : chase simple, build, bounce, linéaire fluide, `{Offset} {Mirror Out}`/`{Mirror In}` [048, 049, A], random flicker.
Recettes absolute officielles : `{Action}` + Color Palettes, `{Grouping}` pour alternance.
Pièges : `effect_edit` → `EFFECT_PATTERN_EDIT` — ⚠️ CORRIGÉ vague29 : la touche existe bel et bien (confirmée A, eosKeys.ts), contrairement au statut D initial. L'échec rapporté par l'utilisateur du forum tenait probablement à la syntaxe des arguments (`action 1 level CP1`), pas à l'inexistence de la commande [021, 151]. Contournement toujours valable par ailleurs : palette factice + `Copy_to` [097, C].

## 5. SUBMASTERS & FADERS

- `SubDown <n> Enter` / `SubUp <n> Enter` — confirmé A dans eosKeys.ts (`subdown`→`SUB_BUMP_DOWN`, `subup`→`SUB_BUMP_UP`) [026, 147]
- RISQUE MAJEUR NON RÉSOLU : macro SubDown/SubUp peut ne pas survivre à l'export/import ASCII [027, C — test prioritaire]
- Proportional vs Intensity Master ; Shielded (priorité absolue) vs Inhibitive (limite proportionnelle) [086, A ; 087, C]
- Grand Master : configuration interface graphique uniquement (Tab 36), pas de commande texte identifiée [089, C]

## 6. AFFICHAGE / INTERFACE

- `{Flexi}` `{Select}` `{Expand}` [115, A]
- Snapshot + `[Select Last]` = pont générique pour toute action d'affichage non capturable en macro [111, C]
- Magic Sheets : préférer Command à macro dédiée [093, 099, C] ; préfixe `macro:` obligatoire [063, C] ; `local:` indisponible en macro [109, C]
- Feedback dynamique de bouton via `Copy Macro X to Y` en fin de macro — motif confirmé et reclassé C [097]
- Highlight/Lowlight/RemDim — exemple officiel complet, preset de référence 9997 par convention [132-134, A]

## 7. SHOW CONTROL (MIDI / OSC / TIMECODE / ANALOGIQUE)

OSC fondamentaux : `/eos/cmd="<commande>"` avec substitution `%1`; `/eos/key/<touche>` pour fonctions à état ; `/eos/user/<n>` pour ciblage utilisateur [065, C]. CR systématique en fin de chaîne [076, A].

**Déclenchement de macro par OSC, confirmé A (manuel v3.2.0 chapitre 31 + confirmation terrain indépendante)** : `/eos/macro=<n>` sélectionne une macro ; `/eos/macro/fire=<n>` l'exécute ; `/eos/macro/<n>/fire=1.0` l'exécute avec argument optionnel de front de bouton (1.0=appui, 0.0=relâchement). C'est l'adresse normative pour le moteur d'injection OSC de macro2eos. Voir `reference/JOURNAL_nomad_complements.md`.

**Assert — confirmé sans mot-clé de ligne de commande dédié** : `/eos/newcmd "Sub n Assert#"` échoue en erreur de syntaxe (confirmé au banc à deux reprises, source S). Assert est une fonction de touche/contexte console, pas un mot-clé `newcmd`/`cmd` — toute génération de macro impliquant Assert doit passer par la séquence de touches console normale, pas par une construction de chaîne de commande. Voir `reference/JOURNAL_nomad_complements.md`.

Send_String — bugs à tickets ETC (règles non négociables) :
- **[EOS-55864]** : toujours en dernière position d'une macro multi-lignes (sinon `/r` parasite) [106, B/A]
- **[EOS-53576]** : `Macro_Wait` entre `Send_String` multiples si déclenché depuis un Client [107, B]

MSC : commandes reconnues = Go, Stop, Resume, Set, Fire [102, A]. Abstraction utilisateur "Go Cue#"/Macro# au-dessus du SysEx hex [103, A].

Analogique/contacts secs : `<Event> [4] [/] [1] {Address} [n] [Cue/Macro/Sub] ... [Enter]` [076, A].

Absence officielle confirmée de variables/formules natives — valide la stratégie d'indirection macro-dans-macro [085, A/B].

## 8. MULTICONSOLE / BACKUP / USER TARGETING

- `{Target}` : Device ou User ID [037, 069, A] — ne fonctionne qu'en Foreground [068, C]
- BUG CONFIRMÉ : édition de macro + macro background simultanée → commandes s'insèrent dans l'édition en cours [067, C]
- Merge sélectif par catégorie via File > Merge [122, A]
- Vigilance : un extrait de forum peut être une reproduction de sortie IA, pas un témoignage humain [123]

## 9. UTILITAIRES

`Clear_CmdLine`/`Clear_Cmd`, `AllNPs`, `CueOnlyTrack`. Pattern nettoyage en boucle infinie avec `Wait_For_Enter` [010]. Renumérotation de cues — macro à haut risque si mal comprise [015, C].

## 10. SÉCURITÉ / EXPLOITATION

Cf. section 5 (Shielded/Inhibitive/Grand Master) — cœur de cette thématique.

## 11. MÉTADONNÉES DE MACRO

`[Label]`, `{Icon}`, `{Color}`, `{Toggle Blink}`, `{Target}`, `{SC Learn}`, `{Macro Mode}` — confirmés officiellement (Tab 18, A).

---

## MÉCANIQUE DE FOND

### Règle syntaxique générale (vague30, C mais cohérente sur tout le corpus)

**La ligne de commande EOS suit la structure Objet → Action → Cible**, avec omission possible de l'objet ou de la cible selon le contexte. Exemples : `Chan 1 At 50 Cue 5 Time 20` ; `Chan 1 Record Preset 3`. Une commande `Cue # Record` seule échoue : `Record` cherche sa cible dans ce qui la précède, pas dans `Cue #`. **Cette règle devrait structurer le squelette de la représentation interne du traducteur.**

**Confirmation officielle et définitive (vague30 #155, B, réponse support ETC directe) : aucun opérateur de négation générale n'existe hors du sous-système Query.** La piste "logique conditionnelle en macro" ouverte en vague 12 est fermée : ce type de logique n'existe structurellement qu'à l'intérieur de `Query`, nulle part ailleurs. `Isn't In`/`Could Be` sont des softkeys contextuels de l'écran Query (pas des touches OSC nommées indépendamment, d'où leur absence de eosKeys.ts) — cf. vague30 #154.

### Polysémie contextuelle liée à l'écran actif (vague32 #161, S — correction directe de Cy, CRITIQUE)

**Un même mot-clé peut avoir un sens radicalement différent selon l'écran/mode actif au moment de l'exécution.** Exemple confirmé : `At` signifie "adresse DMX de départ" en écran **Patch**, mais "niveau d'intensité" en écran **Live**. Confirmé indépendamment (vague33 #162, B) : le symbole `@` lui-même est traduit en "Address" en Patch, "Channel" ailleurs.

**Navigation de focus confirmée officiellement (vague34 #167-168, A)** : `[Tab] [n] Enter` force le focus vers le tab numéroté n — **le focus logique et l'affichage visuel sont le même mécanisme** ("draw focus"), pas deux systèmes séparés. Table des tabs les plus utiles : Live/Blind=1, Playback Status=2, Magic Sheet=3, Show Control=11, **Patch=12**, Effects=13, Cue List=16, Groups=17, **Macros=18**, Snapshots=19, Intensity Palettes=22, Focus Palettes=23, Color Palettes=24, Beam Palettes=25, Presets=26, Color Picker=27, Curves=21, Lamp Controls=31. Exemple : `Tab 12 Enter 1 Thru 100 At 100 Enter` bascule le focus en Patch puis exécute le patch en masse.

**Conséquence non négociable pour l'architecture** : la représentation interne du traducteur doit inclure un champ **"contexte d'écran actif"** en tête de structure — soit en le supposant déjà correct, soit en générant systématiquement le `Tab <n> Enter` de tête pour garantir le contexte avant toute commande sensible à la polysémie.

### Deux voies de création
1. **Learn** — méthode primaire recommandée par ETC. Tout s'enregistre, y compris [Clear] (pollue, pas une exclusion).
2. **Édition directe** — secondaire/corrective. Piège Scroll Lock : texte tapé sans Scroll Lock = lettres individuelles, pas commandes.

### Touches exclues du Learn
`[Macro]`, flèches, `[Escape]`, `[Select]`, `[Learn]`.

### Sorties distinctes de l'éditeur
`[Select]` termine l'édition ; `[Escape]` abandonne ; `{Done}`/`[Learn]` sortent du mode édition.

### Softkeys de contrôle (avec variantes ligne de commande)
| Softkey | Variante commande | Fonction |
|---|---|---|
| `{Loop Begin}` | `Macro_Loop_Begin` | 0 = boucle infinie |
| `{Loop End}` | `Macro_Loop_End` | ferme la boucle |
| `{Wait}` | `Macro_Wait` | secondes, entier obligatoire |
| `{Wait for Entr}` | `Wait_For_Enter` | pause jusqu'à Enter |
| `{Wait for Input}` | `Wait_For_Input` | pause jusqu'à [Macro] |
| `{Delete}` | — | jamais la hardkey [Delete] |
| `{Enable}`/`{Disable}` | — | absolu vs toggle — non fiable pour le marking (contredit la doctrine générale) |

### Modes Foreground/Background/Default
Foreground = posté sur ligne de commande, tous appareils de l'utilisateur. Background = non posté, appareil appelant seul. Default = Foreground si manuel, Background si système.

⚠️ CORRECTION vague29 : ce ne sont pas des positions cycliques d'un seul softkey `{Macro Mode}` — eosKeys.ts confirme **trois touches OSC distinctes** : `foreground_mode`→`MACRO_USER`, `background_mode`→`MACRO_BACKGROUND`, `default_mode`→`MACRO_DEFAULT_MODE`, plus `macro_mode`→`MACRO_MODE` comme sélecteur général [147]. À corriger dans toute génération : ne pas supposer un cycle unique, mais trois cibles adressables séparément.

**RÈGLE DE GÉNÉRATION RETENUE : Foreground par défaut**, sauf raison explicite.

### Trois stratégies de génération en masse
1. Spread par plage `[Thru] x [Thru] y` — mécanisme Fan natif, le plus fiable (A). **Famille Fan complète désormais connue (vague29, #150)** : `Center`, `Cluster`, `Interleave`, `Jump`, `Mirror In`, `Mirror Out`, `Num Groups`, `Repeat`, `Curve`, `Channels Per Group` — 9+ modificateurs, tous confirmés A dans eosKeys.ts. Zone "styles non documentés" du référentiel considérée résolue.
2. Boucle `Macro_Loop_Begin`/`SelectLast`/`Next` — flexible
3. Indirection macro-dans-macro — syntaxe A, fiabilité d'exécution C (à tester au banc)

### Absences structurelles confirmées (valident l'architecture du projet)
- Pas de variables/formules natives (A/B, ETC)
- Pas d'auto-palette native (A/B, ETC, stable depuis 2010) — cohérent avec la stratégie de validation utilisateur déjà retenue

---

## PRIORITÉS BANC (consolidé, mis à jour vague29)

1. `SubDown`/`SubUp` — survie export/import ASCII [027] (touche confirmée A, reste à tester la survie ASCII spécifiquement)
2. `Go_To_Cue_<décimale>` concaténé — troncature [060]
3. `{Enable}/{Disable}` sur le marking — toggle vs absolu [118]
4. Macro-dans-macro — fiabilité d'exécution réelle [070 vs 095]
5. ~~Liste de recherche complète de l'éditeur~~ — **RÉSOLU par eosKeys.ts (1155 touches, source A)** [146-153]
6. Send_String multiples depuis Client — bug EOS-53576 toujours présent ? [107]
7. **(nouveau)** Clarifier `Isn't In`/`Could Be`/`Group Cells`/`From Absolute` — absents de eosKeys.ts malgré confirmation ailleurs, syntaxe exacte à vérifier au banc [148, 149]
8. **(nouveau)** Vérifier fonctionnellement les 9+ styles de Fan découverts (`Center`, `Cluster`, `Interleave`, `Jump`, `Mirror In/Out`, `Num Groups`, `Repeat`, `Curve`) — noms confirmés, comportements non testés [150]

## ZONES ENCORE OUVERTES

- ~~Styles de Fan alternatifs~~ — **RÉSOLU en nom** (9+ styles identifiés, vague29 #150), reste à tester fonctionnellement
- Suite du projet "Autopalette Macros" [127]
- Nouvelles familles entières découvertes par eosKeys.ts mais jamais explorées fonctionnellement : RTC/Astro (déclenchement horaire), Pixel Mapping complet, Curve editing, `startup_macro`/`shutdown_macro` [152]
- Lamp Control : cause de l'incohérence entre softkeys en édition directe [091]
- Écart eosKeys.ts vs image de liste de recherche (vague12) — `Group Cells` sans correspondance, à clarifier [148]

Voir `REFERENTIEL_RISQUES_ET_GRILLE.md` pour la table de risques contextuels vivante et à jour (12 entrées).
Voir `vague29_eoskeys_integration.md` pour le détail complet de l'intégration de la référence canonique.

<!-- ===== FIN : GRAMMAIRE_CONSOLIDEE.md ===== -->

---

<!-- ===== DEBUT : REFERENTIEL_RISQUES_ET_GRILLE.md ===== -->

# RÉFÉRENTIEL — Commandes/mécanismes à risque contextuel

Ce fichier centralise ce qui était dispersé et dupliqué en fin de chaque vague (vagues 3, 8, 9).
Une seule liste vivante à partir de maintenant — les futures vagues y ajoutent des lignes, ne recréent plus la liste.

## Principe

Une commande "à risque contextuel" est syntaxiquement valide mais dont l'effet dépend d'un facteur externe non visible dans le texte de la macro : mode Foreground/Background, état courant de la console, contexte macro vs ligne de commande live, ou survie à l'aller-retour ASCII. Le validateur doit signaler ces cas à l'utilisateur plutôt que les exécuter en confiance aveugle.

## Liste vivante

| Commande/mécanisme | Facteur de risque | Confiance | Source | Statut de test |
|---|---|---|---|---|
| `{Enable}/{Disable}` vs toggle | Dépend de l'état courant | A (manuel) | vague grammaire initiale | non testé |
| `Update` | Cible ambiguë (palette source vs dernière appliquée) | A | vague5 #025 | historique confirmé par ETC |
| `SelectManual` | Comportement différent macro vs ligne de commande live | D | vague5 #043 | non testé, peu fiable même en usage rapporté |
| `SubDown`/`SubUp` sur bump submaster | Possible non-survie à l'export ASCII | C | vague3 #027 | **prioritaire au banc** |
| `Go_To_Cue` | Non déterministe selon Foreground/Background + timing, aggravé si movers dans la cue | C | vague8 #061 | non testé |
| `Go_To_Cue_<décimale>` (concaténation) | Nom réservé si concaténé sans espace — tronque la décimale | C | vague8 #060 | **prioritaire au banc**, cas simple |
| `{Target}` vers un User | Ne fonctionne qu'en Foreground, jamais en Background | C, confirmé empiriquement | vague9 #068 | non testé |
| Édition de macro concurrente + déclenchement background | Bug système : commandes background s'insèrent dans la fenêtre d'édition en cours | C | vague9 #067 | statut actuel inconnu, à revérifier |
| `More_SoftKeys` | Ne s'enregistre pas en macro | C | vague4 #035 | non testé |
| `Open_Browser` | S'enregistre mais ne rejoue rien | C | vague4 #035 | non testé |
| Frappe texte libre avec Scroll Lock désactivé | Interprétée comme lettres individuelles, pas comme commandes | C | vague4 #036 | argument pro-ASCII |
| Copie de palette/circuit référencé | Copie la référence, pas le contenu, sauf "make absolute" | C | vague5 #042, grammaire initiale | récurrent, motif générique |
| `{Select Last}` après `Query` composé | Relance la syntaxe de requête au lieu de renvoyer la sélection résultante | C | vague14 #083 | non testé |
| Macro-dans-macro (`Macro <n> Enter` en fin de macro) | Syntaxe correcte confirmée A (manuel), mais exécution fiable non garantie selon contexte | A (syntaxe) / C (fiabilité) | vague10 #070, vague17 #095 | **prioritaire au banc** |
| `Send_String` suivi d'un `[Enter]` en macro multi-lignes | Génère un `/r` parasite dans l'adresse OSC — bug ETC-55864 | B/A (ticket ETC confirmé) | vague20 #106 | **règle non négociable : toujours en dernière position** |
| `Send_String` multiples consécutifs depuis un Client | Risque de fusion en un seul paquet UDP malformé — bug ETC-53576 | B (ticket ETC confirmé) | vague20 #107 | **règle : `Macro_Wait` entre chaque** |
| `{Enable}/{Disable}` pour le marking | Se comporte encore comme un toggle en macro, malgré la doctrine générale officielle contraire | C, contredit #074 | vague22 #118 | **prioritaire au banc** |
| `[Blind] [Enter]` non qualifié | Syntaxe ambiguë/insuffisante en macro, doit préciser l'objet cible (`Cue`, `Sub`, etc.) | C | vague22 #119 | **règle : jamais nu, toujours qualifié** |
| `Update` (Make Absolute/Break Nested) | Comportement persistant entre sessions (dernier choix mémorisé), non visible dans le texte de la macro | C | vague24 #126 | non testé |

## Stratégies de génération en masse (mise à jour, corrigée en vague26)

1. **Spread par plage unique `[Thru] x [Thru] y`** — le plus fiable (source A, #056). **C'est le mécanisme Fan lui-même**, appliqué par défaut sans invocation explicite de `[Fan]`/`{Fan}` (confirmé A, vague26 #129). `[Fan]` ne sert qu'à changer de style de répartition parmi plusieurs disponibles (styles non exhaustivement documentés à ce stade).
2. Boucle `Macro_Loop_Begin`/`SelectLast`/`Next` — flexible (#057)
3. Indirection macro-dans-macro — syntaxe A, fiabilité C (#020, #070, #095)

## Reclassifications

- Entrée #011 (vague1, "parking macro auto-modifiante") : reclassée de **D** à **C** — confirmée par un cas indépendant et clair (vague17 #097, pattern `Copy Macro X to Y` pour feedback de label sur bouton Magic Sheet)

## Règle de validation générique à en tirer

**Toute macro générée par le traducteur doit être marquée Foreground par défaut**, sauf raison explicite de passer en Background — c'est la règle la plus simple qui couvre déjà 3 des cas ci-dessus (`Go_To_Cue` en partie, `{Target}` vers User, et par cohérence `Update`/`{Enable}` gagnent à être exécutés dans un contexte prévisible). Background reste réservé à des cas maîtrisés et testés individuellement.

## Stratégies de contournement génériques identifiées

1. **Snapshot + `[Select Last]`** — pont pour toute action d'affichage/interface non capturable directement en macro (encodeurs, pages spécifiques). Fonctionnalité de sélectivité fine du Snapshot confirmée officiellement depuis v2.6 (vague21 #114).
2. **Trois stratégies de génération en masse** (détail complet en fin de vague7, rappel) : spread par plage unique `[Thru] x [Thru] y` (le plus fiable, source A) ; boucle `Macro_Loop_Begin`/`SelectLast`/`Next` ; indirection macro-dans-macro (confirmée A en syntaxe, fiabilité d'exécution C, cf. tableau de risques).

---

# GRILLE DE COLLECTE STANDARDISÉE — à utiliser pour toute future vague

Pour chaque macro/commande trouvée, remplir strictement ces champs (reprend et fixe le format déjà utilisé, pour arrêter les variations de présentation d'une vague à l'autre) :

```
## [N° global] — Titre court

- **Contenu** : (bloc de code exact si disponible, sinon "non capturé")
- **Fonction déclarée** : (résumé en une phrase, reformulé, jamais copié verbatim au-delà de 15 mots)
- **Source** : (nom du fil ou du document, URL en référence de fichier)
- **Auteur** : (si pertinent, pour traçabilité forum)
- **Thématique** : (une des catégories de la taxonomie, cf. plus bas)
- **Confiance** : A/B/C/D
- **Statut** : non testé / testé au banc / confirmé / incomplet / invalidé
- **Impact/intérêt** : (seulement si structurant pour l'archi — sinon omettre ce champ)
```

Ne plus dupliquer une section "risque contextuel" par vague — ajouter directement une ligne au tableau ci-dessus quand un cas de ce type apparaît.

## Taxonomie stabilisée (thématiques)

1. Navigation / conduite
2. Sélection & patch
3. Palettes & presets
4. Effets — **sous-diviser systématiquement en Absolute vs Step-based/Chase**
5. Submasters & faders
6. Affichage / interface
7. Show control (MIDI/OSC/timecode)
8. Multiconsole / backup / User targeting
9. Utilitaires (nettoyage de show, Query, renumérotation)
10. Sécurité / exploitation
11. Métadonnées de macro (Label, Icon, Color, Target, SC Learn — distinctes du contenu exécutable)

## Ce qui reste non couvert (prioriser les prochaines vagues là-dessus)

- Sécurité / exploitation (grand master, inhibitions, dim de salle) — zéro entrée à ce stade
- Show control MIDI/timecode en détail (seulement effleuré via #064)
- Magic Sheets au-delà de la syntaxe `macro:` déjà notée
- Lamp Control (mentionné en négatif dans vague4 #034 comme alternative à une macro, jamais creusé pour lui-même)

## Rappel méthode (déjà en place, à ne pas relâcher)

- Grammaire (normative) = sources A/B uniquement → Operations Manual, Show Control Manual, pages support.etcconnect.com et etcconnect.com/WebDocs
- Catalogue d'usages = C/D admis, toujours marqués non-autoritaires, statut "non testé" par défaut
- Un seul quote/paraphrase par source, jamais de citation verbatim de plus de 15 mots

<!-- ===== FIN : REFERENTIEL_RISQUES_ET_GRILLE.md ===== -->

---

<!-- ===== DEBUT : notes_produit_futures.md ===== -->

# Notes produit — à traiter en phase conception (pas maintenant)

## Idée : validation post-NL par édition à menus déroulants

Après traduction langage naturel → représentation interne, l'utilisateur doit valider
avant tout envoi (ASCII ou OSC). Cette validation n'est pas une simple confirmation
oui/non — chaque élément reconnu par le parseur devient éditable individuellement :

- **Type de cible** (ex: "circuit 3") → menu déroulant proposant les fonctions proches
  (circuit / groupe / palette / preset...) pour corriger une mauvaise interprétation
  du NL sans tout retaper
- **Valeurs numériques** (ex: le "3" dans "circuit 3") → éditable directement,
  changement de nombre sans changement de structure

Objectif : corriger une erreur de compréhension du parseur NL par petites retouches
ciblées, plutôt que reformuler toute la phrase d'origine.

Impact architecture : la représentation interne (le "ticket", cf. échange précédent)
doit exposer chaque champ comme une entité adressable indépendamment, avec pour
chaque champ un type connu et une liste de valeurs/alternatives plausibles générable
à partir du corpus de grammaire — pas juste une chaîne de texte plate.

À reprendre lors de la conception de l'UI et du format de représentation interne.

<!-- ===== FIN : notes_produit_futures.md ===== -->

---

<!-- ===== DEBUT : macros_etc_forum.md ===== -->

# Corpus — Macros EOS collectées (forum officiel ETC)

Source : community.etcconnect.com — page "Macro Favorites" (section dédiée officielle du forum ETC)
Confiance générale de la source : **B/C** (communauté ETC, forum officiel mais contenu utilisateur non validé par ETC)
Statut de vérification : **non testé au banc**
Date de collecte : 29/07/2026

---

## 001 — Pan Fan Center

- **Contenu** : non capturé (titre seul, contenu tronqué dans le résultat de recherche)
- **Auteur** : Philip77739
- **Confiance** : D (à revisiter, fiche individuelle non ouverte)
- **Statut** : incomplet

## 002 — Smarty Groups

- **Contenu** : non capturé (fichier .jpg référencé, contenu image non extrait)
- **Auteur** : Wuz314159
- **Confiance** : D
- **Statut** : incomplet

## 003 — Symmetrical circle effect (2 versions publiées)

- **Contenu** :
```
Group 1 Effect 201.1
Group 2 Offset Reverse Effect 201.2
```
- **Fonction déclarée** : Group 1 = fixtures mobiles côté gauche, Group 2 = côté droit. Effet 201.1 = cercle, 201.2 = même effet inversé. Donne un effet de cercle symétrique.
- **Auteur** : fohlwilting
- **Thématique** : Effets
- **Confiance** : C
- **Statut** : non testé

## 004 — Query Dark_Moves cleanup

- **Contenu** :
```
Query Dark_Moves Enter
AllNPs @ Enter
Update Enter
Clear_Cmd
```
- **Fonction déclarée** : nettoyage rapide des "dark moves" (mouvements non visibles)
- **Auteur** : Angie221
- **Thématique** : Utilitaires / nettoyage de show
- **Confiance** : C
- **Statut** : non testé

## 005 — Create Black Out & Create Fade to black

- **Contenu** :
```
Select_Active at Out Record Cue Next Block Assert [enter]
Label BO [enter]
Time 0 [enter]
live [enter]
```
- **Fonction déclarée** : création rapide d'un blackout en fin de scène, one-touch
- **Auteur** : Robin Baston
- **Thématique** : Conduite / navigation
- **Confiance** : C
- **Statut** : non testé
- **Note** : utilise `Record Cue Next` — dépend de la position dans la cue list

## 006 — RGBW Test Macro

- **Contenu** (tronqué, incomplet) :
```
Color @ 0 [Enter]
Intens @ Full [Enter]
Red @ Full Sneak Time 0.5 [Enter]
Macro_Wait 1 [Enter]
Green @ Full Sneak Time 0.5 [Enter]
Macro_Wait ... (suite non capturée)
```
- **Fonction déclarée** : test d'installations LED RGBW
- **Auteur** : shanapu
- **Thématique** : Utilitaires / test matériel
- **Confiance** : C
- **Statut** : incomplet — à recompléter (fiche individuelle à ouvrir)
- **Intérêt** : confirme l'existence de `Sneak Time` en paramètre inline et de `Macro_Wait` comme mot-clé de pause (variante de `{Wait}` documenté dans les manuels ETC)

## 007 — Select last / record preset 999

- **Contenu** : non capturé intégralement
- **Fonction déclarée** : en tant que console d'accueil ("guest house"), enregistre les moving lights et LED sans intensité dans le preset "home" 999 après focus/réglage
- **Auteur** : jolsson
- **Thématique** : Presets / workflow tournée
- **Confiance** : C
- **Statut** : incomplet

## 008 — Track Autoclean FCB v.0.1

- **Contenu** :
```
Qurey Intensity Cue 1/5 Thru [Enter]
Select_Last
Record Group 9999.99 [Enter][Enter]
Blind
Cue[Enter]
Last Last[Enter]
Macro_Loop_Begin
Next
Group 9999.99-Select Active Focus Color Beam@[Enter]
Macro_Loop_End
```
- **Fonction déclarée** : conçue pour les shows en mode Cue Only. En parcourant les cues depuis le début, nettoie automatiquement tous les Dark Moves et Live Moves (D & L) générés.
- **Auteur** : Mutja Engel
- **Thématique** : Utilitaires / nettoyage de show
- **Confiance** : C
- **Statut** : non testé
- **Intérêt majeur** : exemple complet et détaillé d'usage de `Macro_Loop_Begin` / `Macro_Loop_End`, confirmant la syntaxe des softkeys de boucle documentées côté manuel ETC (cf. corpus grammaire)

## 009 — Framing Mirror

- **Contenu déclaré** (résumé, contenu technique non capturé intégralement) : prend un premier groupe de channels, attend la saisie d'un second groupe, puis copie et inverse les paramètres appropriés pour obtenir une copie miroir. Conçu pour des unités de découpe (framing shutters) type FOH. Applique le volet B de l'un sur le D de l'autre, en gardant A inchangé, et en inversant.
- **Auteur** : Stanley Olden
- **Thématique** : Utilitaires / conduite
- **Confiance** : C
- **Statut** : incomplet — probablement utilise `Wait_For_Input`
- **Date** : Fév. 2026 (source récente)

## 010 — Blind Dark Move Cleaning

- **Contenu** :
```
Blind Cue Enter
Macro_Loop_Begin 0 Enter
Cue Wait_For_Enter Enter
Query Dark_Moves Enter
AllNPs @ CueOnlyTrack Enter
Macro_Loop_End Enter
```
- **Fonction déclarée** : macro en boucle infinie (`Macro_Loop_Begin 0` = boucle sans fin selon doc ETC). Il suffit de taper le numéro de la cue suivante à chaque itération.
- **Auteur** : Merle DeWitt 3
- **Thématique** : Utilitaires / nettoyage de show
- **Confiance** : C
- **Statut** : non testé
- **Intérêt majeur** : confirme la sémantique `Macro_Loop_Begin 0` = boucle infinie, cohérente avec le manuel ETC (`{Loop Begin}` valeur 0 = infini). Confirme aussi `Wait_For_Enter` comme mot-clé de pause distinct de `Wait_For_Input`.

## 011 — Macro sequence pour parking

- **Contenu** :
```
Macro x: Color red [group xxx full park on enter
          macro y+1 copy to macro x]
Macro y: Color red [group xxx at full park on enter
          Macro y+1 copy to macro x]
Macro y+1: Color green [group xxx park out enter
          macro y copy to macro x]
```
- **Fonction déclarée** : système de parking de groupe avec macro auto-modifiante (une macro qui se copie elle-même sur un autre numéro pour changer de comportement au prochain appel)
- **Auteur** : KonstantinLi
- **Thématique** : Submasters / faders / parking
- **Confiance** : D (formulation confuse, non reproductible en l'état, à clarifier avant tout usage)
- **Statut** : incomplet / à vérifier — syntaxe douteuse
- **Intérêt** : montre l'usage de `Copy To` exécuté depuis l'intérieur d'une macro pour du comportement dynamique — piste architecturale intéressante mais fragile

## 012 — Mark Live Move

- **Contenu** : non capturé intégralement
- **Fonction déclarée** : copiée dans la macro 821 en cours de programmation, sert de "mark" rapide pour la cue en cours — récupère tous les live moves et les marque automatiquement. Utile en changeant de vue entre programmation et exploitation.
- **Auteur** : jolson
- **Thématique** : Mark / Auto-Mark
- **Confiance** : C
- **Statut** : incomplet

## 013 — Record Palette/Preset avec Wait_For_Input + Label

- **Contenu** : non capturé intégralement (titre = début du contenu)
```
Clear_CmdLine Select_Last Record Color_Palette Wait_For_Input Label ...
```
- **Fonction déclarée** : deux variantes pour les Presets (avec/sans intensité). Enregistre la palette/preset pour les derniers channels modifiés, attend une saisie de numéro, ouvre le dialogue de label.
- **Auteur** : jolsson
- **Thématique** : Palettes & presets
- **Confiance** : C
- **Statut** : incomplet
- **Intérêt** : confirme `Wait_For_Input` suivi directement de `Label` — enchaînement utile pour ton parseur NL (motif "attendre saisie utilisateur puis nommer")

## 014 — Query Live_Moves + Flexi_Selected

- **Contenu** :
```
Query Live_Moves Enter
Flexi_Selected Enter
```
- **Fonction déclarée** : variante de la macro classique Query Live/Dark Moves, ajoute un passage en état "flexi selected" pour visualisation rapide
- **Auteur** : Cody Whitfield
- **Thématique** : Affichage / interface
- **Confiance** : C
- **Statut** : non testé — la plus simple et la plus fiable du corpus, bon candidat pour premier test au banc

## 015 — Reorder cues (non-integers → integers)

- **Contenu** :
```
Record Cue 9999 ENTER
Cue 9999 ENTER
Last Move_To Cue 1001 ENTER
Macro_Loop_Begin 1000 ENTER
Cue 1001 ENTER
Last Move_To Cue 1000 ENTER
Cue 1000 ENTER
Thru Move_To Cue 1001 ENTER
ENTER
Macro_Loop_End ENTER
Cue 10001 ENTER
Move_To ... (suite non capturée)
```
- **Fonction déclarée** : renumérote les cues décimales en entiers
- **Auteur** : davidstreetuk
- **Thématique** : Utilitaires / cue list
- **Confiance** : C
- **Statut** : incomplet, macro complexe et à haut risque si mal comprise (renumérotation de show réel)
- **Date** : avril 2026 (source très récente)

## 016 — Record Preset avec paramètres sélectifs

- **Contenu déclaré** (contenu technique non capturé) : variante avec Select Active. Sélectionne uniquement les paramètres typiquement enregistrés dans les presets, économise des frappes.
- **Auteur** : Dionysus
- **Thématique** : Palettes & presets
- **Confiance** : C
- **Statut** : incomplet

## 017 — Clear + Select Active minus FOH + Effect

- **Contenu déclaré** (non capturé intégralement) : Clear command line, Select Active en excluant le matériel FOH et tout FX Effect, puis applique un effet au choix
- **Auteur** : Nervaxon
- **Thématique** : Effets / conduite danse
- **Confiance** : C
- **Statut** : incomplet
- **Note utilisateur** : signale que la touche "Stop FX" est jugée moins fiable qu'une macro équivalente — signal d'usage intéressant

## 018 — Query UpMoves cleanup

- **Contenu** :
```
Query UpMoves @ 0 @enter
```
- **Fonction déclarée** (en allemand dans la source) : petite macro pour nettoyer rapidement en Blind les "zéros bleus" (up moves non voulus), appliquée cue par cue
- **Auteur** : Tobsen
- **Thématique** : Utilitaires / nettoyage de show
- **Confiance** : C
- **Statut** : non testé — syntaxe courte et simple, bon candidat de test

## 019 — Shift+Out (Flash_Off) — non résolu

- **Contenu** : aucun, c'est une question non répondue
- **Constat de l'auteur** : tentative de reproduire le raccourci clavier Shift+Out en macro, bloqué car Shift n'est pas capturable dans l'éditeur de macro
- **Auteur** : ramellje
- **Thématique** : Limite connue
- **Confiance** : A (négatif) — confirme une limite documentée : les modificateurs clavier type Shift ne sont pas capturables dans le Macro Editor
- **Statut** : confirmé comme non réalisable en l'état

---

## Synthèse des mots-clés/softkeys confirmés par usage réel dans ce lot

Au-delà de ce qui était déjà en corpus grammaire (Foreground/Background, {Loop Begin}, {Wait}, {Wait for Input}, {Enable}/{Disable}) :

- `Macro_Wait` — variante en ligne de commande de `{Wait}`
- `Macro_Loop_Begin` / `Macro_Loop_End` — variante en ligne de commande de `{Loop Begin}`/`{Loop End}`, confirmée à deux reprises avec la sémantique "0 = boucle infinie"
- `Wait_For_Enter` — variante en ligne de commande de `{Wait for Entr}`
- `Wait_For_Input` — confirmé, utilisé juste avant `Label`
- `Clear_CmdLine` / `Clear_Cmd` — nettoyage de ligne de commande en tête de macro, motif très répandu
- `Select_Active` / `Select_Last` — sélection courante très utilisée en tête de macro de type "record"
- `Query Dark_Moves`, `Query Live_Moves`, `Query UpMoves` — famille de commandes Query très présente, thématique "nettoyage de show"
- `AllNPs` — "All Non-Parked" probablement, à confirmer
- `Flexi_Selected` — mode d'affichage
- `CueOnlyTrack` — mot-clé lié au mode Cue Only

## Limite non résolue confirmée par la communauté

Les modificateurs clavier (Shift notamment) ne sont pas capturables dans le Macro Editor — confirme et précise la liste d'exclusions déjà connue (Macro, flèches, Escape, Select, Learn).

## Fiches incomplètes à recompléter (priorité de re-visite)

001, 002, 006, 007, 009, 012, 013, 015, 016, 017 — nécessitent l'ouverture de leur page individuelle pour capturer le contenu technique complet.

<!-- ===== FIN : macros_etc_forum.md ===== -->

---

<!-- ===== DEBUT : macros_etc_forum_vague2.md ===== -->

# Corpus — Macros EOS, vague 2 (fils thématiques forum ETC)

Source : community.etcconnect.com, divers fils (hors fil dédié "Macro Favorites")
Date de collecte : 29/07/2026

---

## 020 — Macro appelant une macro (indirection / "variables")

- **Fil source** : "Populate groups by type via macro"
- **Découverte majeure** : une macro peut appeler une autre macro en son sein. Si la macro appelée ne contient qu'une suite de chiffres, elle peut servir de référence indirecte — un mécanisme proche d'une **variable**.
- **Citation reformulée** : un contributeur explique avoir utilisé ce principe pour régler le BPM sur plusieurs effets à la fois — une macro applique le BPM en lisant sa valeur depuis une autre macro dédiée, qui ne contient que le chiffre.
- **Confiance** : C (témoignage détaillé et cohérent, non contredit dans le fil)
- **Statut** : non testé
- **Impact architecture majeur** : ce mécanisme est directement exploitable pour ta fonctionnalité "génération en masse sur N groupes" (point de blocage n°3 identifié en tout début de cadrage). Au lieu de générer N macros complètes et redondantes, ton traducteur pourrait générer une macro "modèle" + une macro "paramètre" par cible, réduisant la duplication. À creuser en conception.

## 021 — Effect_Edit (piste non aboutie, signal négatif utile)

- **Fil source** : "edit effect macros"
- **Intention de l'utilisateur** : modifier dynamiquement la couleur utilisée dans un effet chase existant via macro, syntaxe tentée : `Effect_Edit 1 action 1 level CP1`
- **Résultat** : n'a pas fonctionné pour l'auteur du fil ; aucune réponse positive dans le fil
- **Confiance** : D (négatif — approche testée et invalidée par un utilisateur, sans confirmation alternative)
- **Statut** : à ne pas intégrer comme syntaxe valide. Solution de contournement proposée par un autre membre : utiliser une palette de couleur "factice" (dummy) référencée par l'effet, et faire pointer les macros sur la modification de cette palette plutôt que sur l'effet directement.
- **Intérêt pour toi** : ce contournement (palette factice comme point d'indirection) est un motif de conception réutilisable pour ton propre moteur — modifier le contenu d'un objet référencé plutôt que tenter de réécrire un effet en direct.

## 022 — Grouping / sub-grouping sur les effets (limite de version)

- **Fil source** : "Grouping on Effects"
- **Contenu technique** : pour appliquer un effet avec des sous-groupes de fixtures agissant à l'unisson (ex: 3 + (2+4) + (1+5)), un contributeur ETC répond que le **sub-grouping n'était pas disponible en v2.0** mais prévu pour une version ultérieure.
- **Confiance** : B (réponse d'un profil identifié comme proche d'ETC dans le fil)
- **Statut** : fonctionnalité — à vérifier si présente en 3.2.4 (version de prod de Cy), non vérifié ici
- **Workaround documenté avant l'arrivée du sub-grouping** : enregistrer chaque sous-groupe de fixtures comme une Intensity Palette discrète (ex: 1+5=IP1, 2+4=IP2), puis placer l'IP en action de chaque step de l'effet absolu

## 023 — Effets absolus vs step-based (distinction structurante pour la grammaire)

- **Fil source** : "Record parameter specific effects"
- **Contenu technique** : un effet absolu (Absolute Effect) n'a pas de channels attachés en dur — on assigne les channels séparément (dans une cue, un sub, ou une macro). Exemple donné : chase couleur à deux étapes, step 1 = Color Palette rouge, step 2 = Color Palette bleu foncé.
- **Paramètre de "grouping" dans l'effet** : une valeur de groupement à 2 fait alterner les fixtures pairs/impairs en unisson.
- **Syntaxe de retour au fond (background release)** : `[At][Enter]` — confirmé comme méthode générale de suppression d'une instruction de mouvement dans la console, pas seulement pour les effets.
- **Confiance** : C (réponse détaillée d'un utilisateur expérimenté, cohérente avec la doc)
- **Statut** : non testé
- **Intérêt majeur pour ta taxonomie** : confirme que "Effets" doit se scinder en au moins deux sous-familles très différentes dans ton corpus — **Absolute Effects** (channels assignés séparément, référencés par palette) et **Step-based/Chase classiques** (channels attachés directement). Ton traducteur NL devra distinguer ces deux logiques dès la représentation interne.

## 024 — Filtres de record (Record Only Filters)

- **Fil source** : "[Record Only] Help"
- **Contenu technique** : `{Record Only}` peut être combiné avec des filtres pour cibler des types de données précis — ex. `{Record Only} [Color]`, ou `{Beam} {Focus} {Intensity}`. Utile en "busking" (impro live) pour capturer rapidement des looks partiels dans des palettes/presets/sub playlists.
- **Confiance** : C
- **Statut** : non testé
- **Thématique** : Palettes & presets / enregistrement sélectif

## 025 — Update : ambiguïté documentée par ETC lui-même (piège pour macros de type "Update")

- **Fil source** : "Update vs. Record Only" — réponse directe d'un modérateur/développeur ETC
- **Contenu technique** : lorsqu'un channel change de palette référencée en cue puis reçoit une modification manuelle, la commande `[Update][Enter]` était ambiguë quant à sa cible (la palette d'origine stockée en cue, ou la dernière palette appliquée manuellement). Comportement par défaut confirmé : Eos met à jour vers la source d'origine. Une option pour changer ce comportement a été ajoutée dans une version ultérieure (1.4 à l'époque du fil).
- **Confiance** : A (source ETC directe)
- **Statut** : confirmé comme piège connu, historique
- **Intérêt** : toute macro générée par ton outil contenant `Update` doit être signalée comme sensible au contexte — comportement non déterministe selon l'état de la console au moment de l'exécution, cohérent avec le risque déjà identifié sur `{Enable}/{Disable}` vs toggle

---

## Synthèse — apports de cette vague pour l'architecture

1. **Mécanisme d'indirection macro-dans-macro** (#020) — piste concrète pour la génération en masse sur N cibles, à intégrer dans la réflexion sur la représentation interne
2. **Deux familles d'effets distinctes** (#023) — absolute vs step-based, distinction à faire remonter dans le validateur et le parseur NL
3. **Palette factice comme point d'indirection** (#021) — motif de conception pour modifier des objets référencés sans réécrire l'objet cible
4. **Commandes sensibles au contexte/non déterministes** — liste qui s'allonge : `{Enable}/{Disable}` (toggle), `Update` (source ambiguë). Le validateur devra maintenir une liste de commandes "à risque contextuel" et avertir l'utilisateur.

## Nouveaux mots-clés/concepts confirmés

- `Effect_Edit` — commande tentée mais non confirmée fonctionnelle (statut D, à ne pas utiliser tel quel)
- `{Record Only}` + filtres (`[Color]`, `{Beam}`, `{Focus}`, `{Intensity}`)
- Notion de "grouping" numérique dans les effets absolus (paramètre de step)
- `[At][Enter]` — méthode générale de release/suppression de mouvement manuel

<!-- ===== FIN : macros_etc_forum_vague2.md ===== -->

---

<!-- ===== DEBUT : macros_etc_forum_vague3.md ===== -->

# Corpus — Macros EOS, vague 3 (submasters, limites ASCII)

Source : community.etcconnect.com, fils thématiques submasters
Date de collecte : 29/07/2026

---

## 026 — SubDown/SubUp pour piloter un bump submaster depuis une macro

- **Fil source** : "macro activate submaster"
- **Contenu confirmé** :
```
SubDown <n> Enter
SubUp <n> Enter
```
- **Syntaxe correcte confirmée par un membre expérimenté**, en réponse à un auteur dont la macro ne fonctionnait pas (il avait écrit "SubDown SubUp" sans numéro ni Enter — erreur de syntaxe identifiée)
- **Usage déclaré** : déclencher un effet placé sur un sub depuis une cue, pour le laisser tourner sur plusieurs cues avant de le couper
- **Confiance** : C (confirmé par un contributeur expérimenté, cohérent, corrige une erreur d'un autre utilisateur)
- **Statut** : non testé

## 027 — DÉCOUVERTE CRITIQUE : les macros pilotant un submaster via apprentissage ne survivent pas à l'export ASCII

- **Même fil**, témoignage du même contributeur :
- **Citation reformulée** : l'auteur explique avoir dû entièrement réécrire son approche après avoir constaté qu'une macro apprise en enregistrant un "Go" sur le bump button d'une routine de submaster **ne se lit pas correctement lors d'un import ASCII**. Il a remplacé cette approche par un effet appliqué directement en cue (`Ch XX thru XX, Effect 1, Record Cues X thru X`), en évitant complètement la combinaison Macro + Submaster.
- **Confiance** : C, mais témoignage très spécifique et technique, cohérent avec un vrai retour d'expérience de terrain
- **Statut** : à vérifier au banc en priorité — si confirmé, c'est une limite dure pour ton moteur ASCII
- **Impact architecture majeur** : c'est la **première preuve concrète et spécifique** que le contenu d'une macro peut être fonctionnel sur la console mais se corrompre ou se perdre lors d'un aller-retour ASCII. Jusqu'ici on savait seulement que "les macros ne font pas partie du standard USITT" et qu'il fallait utiliser l'extension propriétaire ETC — on a maintenant un exemple concret d'un type de contenu qui, empiriquement, ne survit pas au trajet. Cette information doit être un signal d'alarme central pour la conception du moteur ASCII : **certains contenus de macro peuvent nécessiter une validation supplémentaire ou un contournement spécifique avant export**, pas seulement une traduction syntaxique directe.

## 028 — Macro assignée à un bouton submaster (config console, pas contenu de macro)

- **Fil source** : "Macros And Submaster"
- **Contenu confirmé** : une macro peut être assignée à un bouton de submaster (bump ou fader) via l'onglet Fader Config (Tab 36) ou l'onglet Blind Submaster (Tab 15), en sélectionnant {Macro} dans un menu déroulant puis le numéro de macro
- **Confiance** : C
- **Thématique** : Submasters & faders — configuration, pas contenu de macro
- **Statut** : non testé, mais procédure simple et cohérente avec l'interface documentée

## 029 — Distinction Proportional / Intensity Master (contexte technique pour comprendre les subs)

- **Fils sources** : "Submaster - Intensity only", "I-Master bump buttons"
- **Contenu confirmé** : un sub en mode "Proportional" (par défaut) fait varier tous les paramètres enregistrés (couleur, position...) proportionnellement au fader. Un sub en mode "Intensity Master" restreint le fader à l'intensité seule ; dans ce mode, le bump button devient une touche de "mark" plutôt qu'un flash.
- **Confiance** : C, cohérent entre plusieurs fils indépendants
- **Statut** : contexte utile pour valider la cohérence sémantique des macros ciblant des subs — un `SubDown/SubUp` sur un sub en Intensity Master n'aura pas le même effet perçu que sur un sub Proportional

## 030 — Shift+Out confirmé comme non capturable en macro (deuxième confirmation)

- **Fil source** : "Flash Off button option for submasters and cue lists" (fil de feature request)
- **Contenu** : un membre suggère `[Shift]+[Out]` comme méthode manuelle pour flasher une sélection à 0, en alternative à une macro
- **Confiance** : B (renforce la confirmation déjà obtenue au fil #019 — Shift n'est pas capturable en macro, donc cette méthode reste manuelle uniquement)
- **Statut** : confirmé deux fois, à traiter comme quasi-certain dans le validateur

---

## Synthèse — apports de cette vague

1. **Syntaxe `SubDown <n> Enter` / `SubUp <n> Enter`** confirmée et directement exploitable pour la thématique Submasters de ta taxonomie
2. **Alerte structurante sur le moteur ASCII** : au moins un type de contenu de macro (piloter un bump submaster) semble mal survivre à l'aller-retour ASCII, d'après un témoignage de terrain précis. Cette alerte doit être testée en priorité dès que le banc est accessible — potentiellement avec exactement ce cas de figure (macro Go-sur-bump-submaster) comme test de validation
3. **Confirmation redondante** que Shift n'est pas capturable en macro (deux fils indépendants, aucune contradiction)

## Question ouverte pour le prochain test au banc

Ajouter à la liste de macros-tests à créer avant export ASCII (cf. protocole encore à écrire) : une macro contenant `SubDown <n> Enter` / `SubUp <n> Enter`, pour vérifier concrètement si elle survit à l'export/import — ce serait la confirmation ou l'infirmation directe du témoignage #027.

<!-- ===== FIN : macros_etc_forum_vague3.md ===== -->

---

<!-- ===== DEBUT : macros_etc_forum_vague4.md ===== -->

# Corpus — Macros EOS, vague 4 (manuel officiel v3.3.6 + pièges d'édition)

Sources : etcconnect.com/WebDocs (manuel en ligne officiel, v3.3.6) + forum ETC
Date de collecte : 29/07/2026
Confiance : A pour tout ce qui provient de etcconnect.com/WebDocs

---

## 031 — Exemples officiels supplémentaires d'usage de [Learn] (source A)

Page manuel "Using the [Learn] Key", v3.3.6 :

```
[Learn] [1] [Enter] [Go To Cue] [Out] [Time] [0] [Enter] [Learn]
→ enregistre la macro 1 avec la commande "aller à Cue Out, temps 0"

[Learn] [5] [Enter] [1] [Full] {Chan Check} [Enter] [Learn]
→ enregistre la macro 5 avec "channel 1 à full en mode channel check"

[Learn] [4] [Enter] [-] [Sub] [Record] [Learn]
→ enregistre la macro 4 avec instruction d'enregistrement excluant toutes les données de submaster

[Learn] [2] [Enter] ... (exemple tronqué, non capturé en entier)
```

- **Confiance** : A — manuel officiel
- **Statut** : référence directe, exploitable telle quelle dans le corpus grammaire

## 032 — Précisions officielles sur le mode Learn (source A, complète ce qu'on avait déjà)

- <cite>Pendant le mode Learn, chaque appui de touche est enregistré comme contenu, y compris la touche [Clear] en cas d'erreur de frappe. Il n'y a aucun moyen de corriger une erreur de contenu en mode live — il faut soit ré-enregistrer entièrement la macro, soit l'éditer ensuite dans l'éditeur pour retirer les commandes indésirables.</cite>
- **Confiance** : A
- **Impact** : confirme et renforce ce qu'on savait déjà — [Clear] N'EST PAS dans la liste des touches exclues du Learn (contrairement à ce qu'on pourrait supposer), il s'enregistre bel et bien et pollue la macro. Distinction importante à faire dans le validateur : les touches réellement exclues sont [Macro], flèches, [Escape], [Select], [Learn] — [Clear] n'en fait PAS partie et doit être traité comme un risque de pollution, pas une exclusion automatique.

## 033 — Interface d'édition v3.3.6 : liste de recherche et catégories (source A, nouveau)

Page "Editing Macros", v3.3.6 :

- <cite>En mode édition, le CIA affiche tous les softkeys disponibles pour le système, autrement difficiles à trouver en enregistrement live. On peut aussi choisir dans une liste des commandes de macro les plus courantes, ou toute commande de lampe (lamp command).</cite>
- <cite>Un bouton de recherche permet de chercher dans une liste défilante de toutes les commandes de macro possibles. Taper filtre la liste. Appuyer sur [Enter] sur une commande l'insère dans la macro et retourne au champ de recherche.</cite>

- **Confiance** : A
- **Impact majeur pour ton corpus** : ceci confirme qu'**il existe, dans la console elle-même, une liste exhaustive et consultable de toutes les commandes de macro possibles** — accessible via ce champ de recherche. C'est potentiellement ta meilleure source de vérité pour la grammaire complète, plus fiable que tout ce qu'on peut trouver en ligne. **Action à prévoir pour ton premier accès console (ou Nomad)** : ouvrir cette liste de recherche en mode édition macro et la parcourir/exporter intégralement si possible (capture d'écran systématique, ou export si le champ le permet).

## 034 — Piège confirmé : perte de disponibilité d'un softkey en cours d'édition

- **Fil source** : "Macro Editing Softkey Anomaly" (mai 2025)
- **Symptôme rapporté** : un utilisateur insère `{Address}`, puis un `Wait 5`, puis `Clear_CmdLine` — et constate que le softkey `{Address}` n'est ensuite plus disponible pour un second usage dans la même macro
- **Réponse ETC (modérateur)** : <cite>règle générale recommandée — apprendre une macro d'abord (Learn), puis l'éditer si nécessaire, plutôt que d'écrire une macro de zéro dans l'éditeur.</cite> Suggestion alternative pour ce cas précis : utiliser la fonctionnalité **Lamp Control** en Patch plutôt qu'une macro, car elle est conçue pour l'envoi de valeurs DMX temporisées.
- **Confiance** : B (réponse officielle ETC dans le fil, sur un cas non entièrement résolu)
- **Statut** : anomalie confirmée mais non expliquée en profondeur — à traiter comme signal de prudence : certains softkeys peuvent devenir indisponibles selon le contexte d'édition, pas seulement selon une liste fixe d'exclusions
- **Impact** : renforce la doctrine ETC elle-même que **le Learn est la méthode primaire recommandée**, l'édition manuelle en éditeur étant secondaire/corrective. Cohérent avec la stratégie déjà retenue pour ton moteur OSC (simulation de Learn plutôt que construction depuis l'éditeur).

## 035 — Confirmation de touches non capturées, avec exemples concrets supplémentaires

- **Fil source** : "Macro Editor" (fil ancien mais riche)
- <cite reformulé>Certains appuis ne s'enregistrent pas dans l'éditeur de macro, que ce soit en Learn live ou en édition directe — notamment "More Softkeys". Un utilisateur signale que presser cette touche s'affiche bien comme un appui dans l'écran de diagnostic (sous le nom `More_SoftKeys`), mais n'apparaît pas dans le contenu de la macro enregistrée.</cite>
- <cite reformulé>Même constat pour l'ouverture/fermeture du navigateur (Displays, Displays) : la macro enregistre `Open_Browser`, mais rejouer la macro ne produit aucun effet, quel que soit le mode.</cite>
- **Réponse technique d'un contributeur (Hans, profil technique reconnu du forum)** : les commandes UDP suivent la même syntaxe que les commandes série, documentées dans le Eos Family Show Control User Guide.
- **Confiance** : C pour le témoignage utilisateur (non résolu, bug potentiel non confirmé par ETC directement dans ce fil), mais cohérent avec la liste d'exclusions déjà connue
- **Statut** : `More_SoftKeys` et `Open_Browser` à traiter comme **commandes à risque** — soit non enregistrables, soit enregistrables mais non fonctionnelles à la relecture. À exclure ou avertir dans le validateur.

## 036 — Piège du Scroll Lock en édition directe (texte interprété comme touches individuelles)

- **Même fil**
- <cite reformulé>Il est possible de taper directement dans l'éditeur de macro quand le Scroll Lock est désactivé, mais l'éditeur traite alors le texte tapé comme des lettres individuelles plutôt que comme des commandes. Par exemple, taper "Full" avec Scroll Lock désactivé est traité différemment que d'éditer avec Scroll Lock activé et presser la touche {Full}, qui s'insère automatiquement comme commande complète.</cite>
- **Confiance** : C (témoignage utilisateur non contredit)
- **Statut** : piège majeur pour toute génération de macro par du texte brut — confirme qu'il ne suffit pas d'"écrire" une commande, il faut que l'état Scroll Lock soit correct et/ou que la commande soit insérée comme token complet, pas comme suite de caractères
- **Impact architecture** : renforce fortement l'intérêt de la voie ASCII (où ce risque d'interprétation contextuelle ne devrait pas exister, le fichier étant structuré) par rapport à toute méthode qui simulerait de la frappe de texte libre dans l'éditeur.

## 037 — Champs de macro documentés officiellement, non encore capturés dans le corpus (source A)

Page "Macro Editor [Tab 18]", v3.3.6 :

- `[Label]` — nommer la macro
- `{Icon}` — assigner une icône, affichable en Direct Select
- `{Color}` — assigner {Red}, {Green}, {White} ou {Dark} (aucune couleur), affiché à côté du nom en Direct Select et sur les hardkeys personnalisables (Eos Ti, Gio, Gio @5, RPU)
- `{Toggle Blink}` — désactive le clignotement par défaut d'une hardkey personnalisable pendant l'exécution de la macro qui lui est assignée ; un "BD" s'affiche dans la colonne couleur si désactivé
- `{Target}` — assigne un Device ou un User ID cible à la macro, sélectionnable via {Device}/{User}, affiche la liste des devices connectés
- `{SC Learn}` — active/désactive l'exclusion d'une macro spécifique de l'apprentissage en tant qu'événement de show control (renvoi vers la doc Timecode/Learn)

- **Confiance** : A
- **Impact** : ce sont des **métadonnées de macro**, distinctes du contenu exécutable — à intégrer comme champs à part entière dans ta représentation interne (le "ticket"), pas mélangées avec la séquence de touches elle-même

---

## Synthèse — apports de cette vague (la plus riche en source A jusqu'ici)

1. **Trouvaille la plus importante** : la console elle-même expose une **liste de recherche exhaustive de toutes les commandes de macro possibles**, en mode édition. C'est potentiellement une source de vérité supérieure à toute documentation externe — objectif prioritaire pour le premier accès matériel (console ou Nomad).
2. **[Clear] n'est pas une touche exclue** — elle s'enregistre et pollue, contrairement aux 5 vraies exclusions (Macro, flèches, Escape, Select, Learn). Distinction fine à corriger dans le validateur.
3. **Deux commandes à risque identifiées** : `More_SoftKeys` et `Open_Browser`, potentiellement non fonctionnelles à la relecture même si elles s'enregistrent.
4. **Piège Scroll Lock** confirmé — renforce l'argument en faveur de la voie ASCII structurée plutôt que toute simulation de frappe de texte libre.
5. **Champs de métadonnée officiels** (Label, Icon, Color, Toggle Blink, Target, SC Learn) à intégrer dans la représentation interne comme attributs de macro, séparés du contenu exécutable.
6. **Doctrine ETC elle-même** confirmée : Learn d'abord, édition manuelle en correction seulement — cohérent avec la stratégie déjà retenue.

<!-- ===== FIN : macros_etc_forum_vague4.md ===== -->

---

<!-- ===== DEBUT : macros_etc_forum_vague5.md ===== -->

# Corpus — Macros/syntaxe EOS, vague 5 (palettes couleur, by-type, dummy channels)

Sources : forum ETC + manuel officiel v3.3.6 + blog ETC
Date de collecte : 29/07/2026

---

## 038 — Enregistrement de palette by-type + lock (source C, syntaxe complète confirmée)

```
41 [Record] [Color Palette] {By Type} {Lock} 45 [Enter]
```
- **Fonction** : enregistre le channel 41 comme palette couleur 45, en mode "by type" (applicable à tous les fixtures du même type) et verrouillée (protégée contre écrasement accidentel)
- **Confiance** : C
- **Thématique** : Palettes & presets
- **Statut** : non testé

## 039 — Pattern "dummy channels by-type" (workflow avancé confirmé, C)

- **Principe reformulé** : patcher des channels fictifs (non reliés à un vrai projecteur), un par type de fixture, les grouper, régler leur couleur, puis `Group x Record Color Palette y By Type Enter`. Avantage : ces channels dummy peuvent être conservés dans un showfile "modèle" et fusionnés (merge) dans n'importe quel autre show utilisant les mêmes types de fixtures — récupération instantanée de toutes les palettes couleur.
- **Confiance** : C, workflow détaillé et cohérent, confirmé par plusieurs contributeurs indépendants sur le fil
- **Thématique** : Palettes & presets, réutilisation multi-show
- **Statut** : non testé
- **Intérêt pour toi** : ce pattern "showfile modèle + merge" est directement pertinent pour ta problématique de réutilisabilité inter-tournées — c'est une solution native EOS au même problème que tu adresses avec ton outil, à documenter comme référence de comparaison

## 040 — Génération de spread de palettes via Hue en Blind (syntaxe complète, C confirmée par plusieurs utilisateurs)

```
[Blind] [Color Palette] [401] [Thru] [430] [Enter]
[4116] {Hue} [0] [Thru] [340] [Enter]
```
- **Fonction** : crée 30 palettes couleur vides (401 à 430) en Blind, puis applique une teinte répartie de 0 à 340° sur le channel by-type 4116, générant un dégradé automatique de couleurs sur l'ensemble des palettes
- **Correction apportée par un second utilisateur** : la syntaxe exacte nécessite `401 Thru THRU 430` (double Thru) et un réglage préalable de la Saturation à Full sur le channel dummy, sinon toutes les palettes ressortent blanches
- **Confiance** : C, corrigée et validée par deux utilisateurs successifs dans le même fil — plus fiable que la moyenne des entrées C
- **Thématique** : Palettes & presets — génération en masse
- **Statut** : non testé
- **Intérêt majeur** : c'est le premier exemple concret et complet dans le corpus d'une **génération en masse par un seul enchaînement de commandes** (30 palettes en une opération), directement dans l'esprit de ta fonctionnalité "génération en masse sur N cibles". Bon candidat de test au banc.

## 041 — Storing Palettes with [Record] — précisions officielles importantes (source A)

Manuel v3.3.6, page "Storing Palettes with [Record]" :

- <cite>Les palettes sont numérotées de 0.001 à 9999.999, chacune pouvant recevoir un label.</cite>
- <cite>[Record] stocke les données de paramètres actuelles pertinentes pour tous les channels ayant des données non-défaut, pour le type de palette approprié, modulées par les réglages de filtre.</cite>
- **Exemple officiel complet** : `[Record] [Color Palette] [4] [Label] <FOH Blue> [Enter]`
- <cite>Pour un enregistrement sélectif, il faut spécifier la liste de channels à inclure/exclure via le modificateur [+]/[-] dans la commande [Record], sinon tous les channels avec des données pertinentes non-défaut seront stockés.</cite>
- <cite>[Record] stocke toute la catégorie de paramètre dans une palette ; [Record Only] stocke uniquement les valeurs ajustées manuellement.</cite>
- **Confiance** : A
- **Statut** : directement exploitable — c'est la référence normative pour toute génération de commande `Record` par ton traducteur

## 042 — Piège confirmé : copie de palette référencée vs valeur absolue (C, technique)

- **Fil source** : "Colour Palette Macro"
- <cite reformulé>Si le fixture source d'une copie est lui-même réglé sur une palette couleur, c'est le numéro de la palette qui est copié, pas son contenu — sauf à faire un "make absolute" au préalable, ce qui peut être source de confusion.</cite>
- **Confiance** : C
- **Impact** : recoupe et confirme le piège déjà identifié dans le corpus grammaire concernant les numéros de circuits/références en dur qui ne survivent pas à un Copy To — même logique de fond ici avec les références de palette
- **Statut** : à intégrer comme règle de validation — le validateur devrait signaler toute macro copiant des données depuis un channel dont l'état exact (référence vs absolu) n'est pas connu au moment de la génération

## 043 — SelectManual : confirmé comme invalide en syntaxe de ligne de commande directe (D, signal négatif utile)

- **Même fil**
- <cite reformulé>Un utilisateur tente d'utiliser SelectManual dans une macro pour retrouver automatiquement le dernier channel travaillé, avec un succès partiel. Un autre contributeur signale que si on essaie de taper cette même syntaxe directement en Live (hors macro), SelectManual n'est pas autorisé dans ce contexte.</cite>
- **Confiance** : D pour l'usage en macro (rapporté comme partiellement fonctionnel mais peu fiable par son propre auteur — "the macro fails to find the channel... and either kicks up the last colour palette... or the next channel available")
- **Statut** : à ne pas recommander comme méthode fiable dans le traducteur ; signal que certaines commandes ont un comportement différent selon qu'elles sont exécutées en macro ou en ligne de commande live directe — point de vigilance générale pour le validateur

---

## Synthèse — apports de cette vague

1. **Premier exemple complet de génération en masse validé par la communauté** (#040, spread de 30 palettes) — bon cas de référence pour illustrer/tester la fonctionnalité de génération en masse de ton outil
2. **Confirmation officielle A** de la syntaxe `[Record] [Color Palette] [n] [Label] <nom> [Enter]` — normative
3. **Deux pièges de "référence vs valeur absolue"** convergents (palette copiée par référence, comme déjà vu pour les circuits en macro) — un motif de risque récurrent à traiter une seule fois dans le validateur, applicable à plusieurs types d'objets
4. **Signal que le comportement de certaines commandes diffère entre contexte macro et contexte ligne de commande live** — nuance à garder à l'esprit, notamment si un jour le corpus grammaire distingue ces deux contextes séparément

<!-- ===== FIN : macros_etc_forum_vague5.md ===== -->

---

<!-- ===== DEBUT : effets_etc_officiel_vague6.md ===== -->

# Corpus — Effets EOS, vague 6 (article officiel ETC — source A)

Source : support.etcconnect.com — "Common Effects and How to Program Them on an Eos Family Console"
Publié 08/03/2018, mis à jour 21/01/2025 — support officiel ETC
Confiance : **A** — c'est un article de la base de connaissance officielle ETC, avec syntaxe exacte pas-à-pas
Date de collecte : 29/07/2026

**Note de méthode** : cet article utilise channels 1 à 10 comme exemple constant. C'est la source la plus structurée et la plus fiable trouvée jusqu'ici pour la thématique Effets — à traiter comme référence normative, au même niveau que les manuels officiels déjà collectés.

---

## EFFETS D'INTENSITÉ

### 044 — Chase d'intensité simple (step-based)

```
[Effect] [1] [Enter]                          → crée effet 1
{Step Based}                                   → le déclare step-based
{Step} [1] [Thru] [1] [0] [Enter] [Enter]      → crée les steps 1 à 10
[Page Right]                                   → avance à la colonne Channels
[1] [Thru] [1] [0] [Enter]                     → distribue channels 1-10 aux steps 1-10
[Live]
[Group] [Effect] [1] [Effect] [1] [Enter]      → sélectionne tous les channels de l'effet et l'applique
```
- **Note officielle** : la syntaxe "Group Effect" ne s'applique qu'aux effets step-based.
- **Confiance** : A
- **Thématique** : Effets — intensité, step-based

### 045 — Chase d'intensité avec "build"

```
[Effect] [1] [Copy To] [2] [Enter]             → copie effet 1 vers effet 2
{Attributes} → {Build}
[Live]
[Group] [Effect] [2] [Effect] [2] [Enter]
```
- **Confiance** : A

### 046 — Chase d'intensité avec "bounce"

```
[Effect] [1] [Copy To] [Effect] [3] [Enter]
{Attributes} → {Bounce}
[Live]
[Group] [Effect] [3] [Effect] [3] [Enter]
```
- **Confiance** : A

### 047 — Chase d'intensité fluide (effet linéaire)

```
[Effect] [4] [Enter]
{Linear}
{Parameters} → {Intensity} [Enter]
{Size} [1] [0] [0] [Enter]
[Live]
[1] [Thru] [1] [0] [Effect] [4] [Enter]
```
- **Confiance** : A
- **Thématique** : Effets — intensité, linéaire

### 048 — Même chase fluide, depuis le centre vers l'extérieur

```
[1] [Thru] [1] [0] {Offset} {Mirror Out} [Effect] [4] [Enter]
```
- **Confiance** : A
- **Intérêt majeur** : confirme la syntaxe exacte de `{Offset} {Mirror Out}` — directement pertinent pour ta fonctionnalité "offset" mentionnée dès le début du projet

### 049 — Même chase fluide, de l'extérieur vers le centre

```
[1] [Thru] [1] [0] {Offset} {Mirror In} [Effect] [4] [Enter]
```
- **Confiance** : A

### 050 — Scintillement aléatoire (random flicker)

```
[Effect] [5] [Enter]
{Linear}
{Parameters} → {Intensity} [Enter]
{Edit} → {Clear}                               → efface la ligne courante
[dessiner un triangle simple sur la courbe]
{Apply}
{Attributes} → {Random Group}
{Random Rate} [5] [0] [Thru] [3] [0] [0] [Enter]
{Cycle Time} [0] [.] [3] [Enter]
[Live]
[1] [Thru] [1] [0] [Effect] [5] [Enter]
```
- **Précision officielle importante** : l'effet est relatif à l'intensité courante des fixtures. Pour changer le niveau de base, on tape `[channels] [At] <niveau> [Enter]`. `{Size}` détermine l'amplitude au-dessus (ou en dessous, si la ligne passe sous le centre) du niveau de base.
- **Confiance** : A
- **Intérêt** : seul effet non step-based/linéaire simple du lot — introduit la notion de courbe dessinée à la main (`{Edit}` + dessin), probablement hors de portée d'un traducteur NL en V1

---

## EFFETS DE COULEUR

### 051 — Color wipe gauche→droite (une seule fois puis arrêt)

```
[1] [Thru] [1] [0] [At] <rouge via color picker>
[1] [Thru] [1] [0] [Record] [Color Palette] [1] [Enter]
[Effect] [1] [1] [Enter]
{Step Based}
{Step}[1] → [Page Right] → [1] [Enter]         → step 1 = channel 1
[down arrow] → [2] [Enter]                     → step 2 = channel 2
... répété jusqu'au step 10 = channel 10 ...
{Step}[1][Thru][1][0]{On State}[Color Palette][1][Enter]
[right arrow] → {Off State} → [Color Palette][1][Enter]
{Attributes} → {Build}
{Exit} → {Stop and Hold}
[Live]
[1] [Thru] [1] [0] [At] [Full] [Enter]
[Group] [Effect] [1] [Enter]
```
- **Confiance** : A
- **Thématique** : Effets — couleur, step-based, non-bouclé
- **Intérêt majeur** : c'est l'exemple le plus complet et détaillé de tout le corpus jusqu'ici — chaque étape est explicite, aucune ambiguïté. Excellent candidat de référence pour la conception du traducteur NL, et bon candidat de premier test au banc.

### 052 — Même wipe mais droite→gauche

```
[Effect][1][1][Copy To][1][2][Enter]
{Attributes} → {Reverse}
```
- **Confiance** : A
- **Intérêt** : confirme que `{Reverse}` (déjà vu ailleurs comme "Offset Reverse") s'applique aussi comme attribut simple d'un effet copié

### 053 — Même wipe mais depuis le centre vers l'extérieur

```
(Channel) [5][Thru][1] [+] [6][Thru][1][0] [Record][Group][1][Enter]
[Effect][1][3][Enter]
{Step Based}
{Step}{1}{Thru}{5} → [Group][1][3][Enter]
{On State} [Color Palette][1]
{Off State} [Color Palette][1]
{Attributes} → {Build}
{Exit} → {Stop and Hold}
[Live]
[Group][1][Effect][1][Enter]
```
- **Confiance** : A
- **Note technique** : ici on assigne un **Group** (pas des channels un par un) à une plage de steps — motif utile pour la génération en masse

### 054 — Chase couleur avec effet absolu (base)

```
[Effect][Effect] → créer Effet 14 → {Absolute}
{Action}[1] → [Color Palette][1]
{Action}[2] → [Color Palette][2]
[Live] → channels 1 thru 10 dans effet 14
```
- **Confiance** : A
- **Thématique** : Effets — couleur, absolu (confirme et détaille ce qui était déjà en corpus vague 2, entrée #023)

### 055 — Chase couleur absolu depuis le centre vers l'extérieur

```
[Effect][1][4][Copy To][Effect][1][5][Enter]
Effet 15 → {Grouping} [5]
[Live] → [Group][1] dans [Effect][1][5]
```
- **Confiance** : A
- **Intérêt** : confirme la syntaxe exacte du paramètre `{Grouping}` déjà évoqué en vague 2 (#022) mais jamais précisé avec cette clarté

### 056 — Chase arc-en-ciel (rainbow chase)

```
[créer 7 color palettes représentant les 7 couleurs de l'arc-en-ciel, une par une :]
[channels 1 thru 10] → régler la couleur → [Record][Color Palette] # [Enter]  (répété x7)

[Effect][Effect] → créer Effet 16 → {Absolute}
{Action}[1][Thru][7][@][Color Palette] x [Thru] y [Enter]
  (où x = première palette du dégradé, y = dernière)
[Live] → sélectionner channels → [Effect][1][6][Enter]
```
- **Confiance** : A
- **Intérêt majeur** : syntaxe `{Action}[1][Thru][7][@][Color Palette] x [Thru] y [Enter]` — assignation en masse de N steps à N palettes en une seule commande. C'est le **meilleur exemple du corpus entier** pour ta fonctionnalité de génération en masse : une seule ligne de commande couvre 7 étapes distinctes.

---

## Synthèse — apports de cette vague (la plus structurante à ce stade)

1. **Confirmation exacte de la syntaxe `{Offset} {Mirror Out}` / `{Offset} {Mirror In}`** — répond directement au besoin d'offset mentionné dès le cadrage initial du projet
2. **Confirmation exacte de `{Grouping}`** pour les effets absolus
3. **Meilleur exemple de génération en masse du corpus** : `{Action}[1][Thru][7][@][Color Palette] x [Thru] y [Enter]` — un seul enchaînement de commande pour assigner 7 valeurs distinctes à 7 steps. Ce motif syntaxique (plage de steps `[Thru]` + plage de valeurs `[Thru]`) est un candidat sérieux pour le cœur du moteur de génération en masse de ton traducteur.
4. **Distinction confirmée entre deux workflows de construction d'effet step-based** : assignation channel par channel (#051) vs assignation par Group sur une plage de steps (#053) — le second est nettement plus adapté à un usage "génération automatique"
5. Cet article devient la **référence normative prioritaire** pour toute génération de commande liée aux effets — à consulter avant toute autre source communautaire sur ce sujet

## Lien complémentaire identifié, non encore dépouillé

Un lien similaire existe pour Congo/Cobalt ("Chase Effects Tutorial") — architecture de commande différente (autre famille de consoles ETC), à ne pas mélanger avec la grammaire EOS. Écarté du corpus EOS mais noté pour référence si jamais utile en comparaison.

<!-- ===== FIN : effets_etc_officiel_vague6.md ===== -->

---

<!-- ===== DEBUT : groupes_etc_forum_vague7.md ===== -->

# Corpus — Groupes EOS, vague 7

Source : community.etcconnect.com
Date de collecte : 29/07/2026

---

## 057 — Pattern SelectLast pour enregistrer des groupes en série (C, motif directement réutilisable)

```
Highlight Chan 1 Enter
SelectLast Record Group 1 Enter
Next
SelectLast Record Group 2 Enter
Next
SelectLast Record Group 1 Enter
Next
SelectLast Record Group 2 Enter
... (répété)
```
- **Contexte** : utilisateur cherchant à reproduire un workflow type "Hog console" — sélectionner un fixture, l'enregistrer dans un groupe, passer au suivant, sans redéfinir la sélection depuis zéro
- **Réponse validée par un contributeur expérimenté** : `SelectLast` est la clé — elle permet d'enchaîner Record Group / Next / SelectLast en boucle rapide
- **Confiance** : C
- **Statut** : non testé
- **Intérêt majeur pour ta génération en masse** : c'est le **deuxième motif concret de génération en série** trouvé dans le corpus (après le spread de palettes en #040), et le plus simple à généraliser algorithmiquement — une boucle `SelectLast Record Group N Enter Next` est un candidat naturel pour `Macro_Loop_Begin`/`Macro_Loop_End` avec incrémentation. À rapprocher du mécanisme d'indirection macro-dans-macro (#020) pour la conception du moteur de génération en masse.

## 058 — Distinction Group vs Palette (C, confirmée par plusieurs sources convergentes)

- **Fil source** : "grouping channels together"
- **Contenu confirmé** : un Group ne contient que des références de channels, pas de niveaux d'intensité. Pour stocker une combinaison de channels + niveaux, il faut une Intensity Palette. Rappel : `[Group][Intensity Palette]` peut être utilisé pour sélectionner tous les channels contenus dans une palette — donc une palette peut aussi servir de mécanisme de sélection, comme un groupe.
- **Confiance** : C, cohérent avec la doc palette déjà en corpus (vague 5)
- **Impact pour la grammaire** : distinction essentielle pour ton parseur NL — si l'utilisateur dit "sélectionne le groupe X" en visant en réalité une combinaison channels+niveaux, le traducteur doit orienter vers Palette et non Group. À intégrer dans les règles de désambiguïsation, en lien direct avec l'idée de menu déroulant "circuit → groupe ou autre fonction proche" déjà notée pour la conception UI.

## 059 — Réordonnancement et renumérotation de groupes (signal négatif partiel)

- **Fil source** : "Groups, Labels"
- **Contenu** : un utilisateur demande s'il est possible de renuméroter/réorganiser des groupes après coup sans tout refaire, et de dupliquer des labels en série (ex: "Column 1" à "Column 12") pour automatiser la création de 12 groupes
- **Réponse** : <cite reformulé>oui c'est possible, mais le déplacement de groupes ne fonctionne pas exactement de la même manière que pour les Presets et Palettes</cite> — réponse incomplète, pas de détail sur la méthode exacte
- **Confiance** : D (question non résolue en détail dans le fil)
- **Statut** : signal que la manipulation de groupes a des subtilités différentes des autres objets EOS (palettes/presets) — à garder en tête comme point de vigilance, sans détail exploitable pour l'instant
- **Intérêt** : l'utilisateur suggère lui-même l'idée d'une macro pour automatiser cette tâche répétitive de labellisation en série — confirme, par la demande elle-même, l'existence d'un vrai besoin utilisateur pour ce que ton outil vise à résoudre

---

## Synthèse de cette vague

Le motif `SelectLast` + boucle (#057) est le candidat le plus solide, à ce stade du corpus, pour implémenter concrètement la génération en masse "un modèle appliqué à N cibles" — combiné aux mécanismes déjà identifiés :
- Indirection macro-dans-macro (#020)
- Spread par plage `[Thru]`/`[Thru]` en une commande (#040, #056)
- Boucle `Macro_Loop_Begin`/`Macro_Loop_End` (confirmée à plusieurs reprises)

Ce sont maintenant **trois stratégies distinctes de génération en masse**, à des niveaux de risque et de complexité différents, qui pourront être comparées lors de la conception du moteur :
1. **Spread par plage unique** (`[Thru] x [Thru] y`) — le plus simple, mais limité aux cas où la progression de valeur est linéaire/régulière
2. **Boucle Macro_Loop avec SelectLast/Next** — plus flexible, applicable à des séquences pas nécessairement régulières
3. **Indirection macro-dans-macro** — le plus avancé, permet de factoriser un "modèle" réutilisable, mais confiance la plus faible (un seul témoignage, C, non testé)

<!-- ===== FIN : groupes_etc_forum_vague7.md ===== -->

---

<!-- ===== DEBUT : navigation_etc_forum_vague8.md ===== -->

# Corpus — Navigation/conduite EOS, vague 8

Source : community.etcconnect.com
Date de collecte : 29/07/2026

---

## 060 — ALERTE : bug de syntaxe Go_To_Cue avec underscore mal placé (C, confirmé et corrigé dans le fil)

- **Fil source** : "Macro: GO TO CUE"
- **Symptôme rapporté** : une macro apprise contenant `Go_To_Cue_0.9 ENTER` s'exécute comme `Go To Cue 0` — tronque la décimale
- **Diagnostic proposé par un contributeur** : `Go_To_Cue_0` serait un nom de commande réservé à part entière (fix command), pas une concaténation de `Go_To_Cue` + `_0`. La syntaxe correcte serait `Go_To_Cue 0.9 ENTER` (espace, pas de underscore devant le chiffre).
- **Confiance** : C — hypothèse plausible d'un contributeur, non confirmée par ETC dans ce fil, mais cohérente et précise
- **Note complémentaire** : un autre utilisateur indique que ça fonctionnait correctement en version 1.9.11/1.9.12 — suggère que le bug (s'il en est un) est version-dépendant, ce qui **contredit partiellement** l'hypothèse de départ du projet ("les macros sont les mêmes sur toutes les versions, sauf exception rare"). À noter comme exception confirmée.
- **Statut** : à tester en priorité au banc — cas simple et bien isolé
- **Impact architecture** : si confirmé, ceci est un piège de **génération automatique par concaténation de texte** — un traducteur NL qui construirait la commande en assemblant des chaînes (`"Go_To_Cue_" + str(numero_cue)`) tomberait exactement dans ce piège. Argument supplémentaire pour que le moteur de génération traite les commandes comme des tokens structurés (nom de commande + paramètres séparés), jamais comme de la concaténation de texte brut.

## 061 — ALERTE MAJEURE : comportement inconsistant de Go_To_Cue selon le contexte d'exécution en macro (C, témoignage détaillé et technique)

- **Fil source** : "Multiple cue lists and macros"
- **Symptôme rapporté**, avec logs de diagnostic console à l'appui : une macro censée exécuter une cue list en boucle, attendre sa fin, puis revenir (`Assert`) à la cue list principale et forcer le retour de channels capturés, **ne fonctionne pas de manière fiable** quand déclenchée en macro, alors qu'elle fonctionne systématiquement en exécution manuelle.
- **Citation reformulée** : l'auteur précise que les macros en mode Foreground ne fonctionnent pas avec sa syntaxe, et que les macros en Background n'exécutent pas toujours le Go To Cue — ou l'exécutent mais pas nécessairement sur la bonne cue list assertée, possiblement lié au timing. Il note que le problème est particulièrement marqué quand un mover fait partie de la cue : le fixture ne revient pas à la cue list principale sauf commande manuelle.
- **Confiance** : C, mais témoignage technique dense avec logs — parmi les plus sérieux du corpus
- **Statut** : non résolu dans le fil consulté
- **Impact architecture majeur** : ceci est la **deuxième preuve concrète** (après #027 sur les submasters) qu'une commande peut se comporter différemment selon qu'elle est tapée manuellement ou exécutée depuis une macro — et de façon non déterministe qui plus est (dépendance au mode Foreground/Background et à un possible facteur de timing). C'est un signal fort que **le validateur ne peut pas se contenter de vérifier la syntaxe** : certaines commandes syntaxiquement valides ont un comportement d'exécution non garanti en contexte macro. `Go_To_Cue` doit être ajouté à la liste des commandes "à risque contextuel" aux côtés de `{Enable}/{Disable}`, `Update`, `SelectManual`.

## 062 — Syntaxe confirmée pour macro liée à un ajustement fin de timing de cue (C, motif utile)

- **Fil source** : "Go to cue next macro"
- **Besoin exprimé** : une macro type "Go to Cue_next_time_5" pour forcer un temps de montée sans connaître/casser le temps de descente déjà réglé dans la cue
- **Tentative de solution proposée (non aboutie)** : scinder en deux cues séparées (montée puis descente en `{Follow} 0`) — corrigée en séance par son propre auteur : `[Go to cue]` n'active le follow cue qu'avec `{Complete}`, qui lui-même ignore le temps de descente déjà réglé sur la cue de suivi
- **Confiance** : D pour la solution (invalidée par son propre auteur en cours de fil) — mais l'échec est lui-même une donnée utile
- **Statut** : problème non résolu dans le fil — bon candidat de recherche complémentaire si cette fonctionnalité s'avère demandée par les futurs utilisateurs de ton outil
- **Intérêt** : encore un exemple de piège où l'intuition "simple en apparence" (changer juste le temps de montée) cache une interaction complexe entre plusieurs mécanismes EOS (`{Follow}`, `{Complete}`, temps de cue). Type de cas qui justifie ton système de validation avec alternatives proposées à l'utilisateur plutôt qu'une exécution aveugle.

## 063 — Syntaxe `macro:` pour appeler une macro depuis un bouton de Magic Sheet (C, confirmée)

- **Fil source** : "Commands in Magic Sheet"
- **Contenu confirmé** : pour qu'un bouton de Magic Sheet exécute une macro, la commande doit être préfixée par `macro:` — exemple cité comme provenant directement de l'infobulle d'aide native de l'éditeur de Magic Sheet
- **Confiance** : C, mais renvoie à une source native de l'interface elle-même (donc quasi-A dans les faits)
- **Avantage confirmé par un second contributeur** : référencer une macro depuis un bouton de Magic Sheet (plutôt que d'y copier-coller directement la commande) facilite la fusion (merge) de Magic Sheets entre showfiles
- **Thématique** : Affichage/interface, mais pertinent aussi pour la distribution multi-tournée (cohérent avec le pattern dummy channels de la vague 5)
- **Statut** : non testé

## 064 — Pattern avancé : macro pilotant l'enregistrement d'une Event List via Learn + Show Control (C, complexe, à haut risque)

- **Fil source** : "Record Manual Cue Playback Timing?"
- **Principe reformulé** : combiner `[Learn] [Macro 35] [Enter]`, navigation vers l'écran Show Control interne, création d'un Event 1, nouveau `[Learn]` pour arrêter l'enregistrement de la macro — puis activation du timecode interne en mode Learn pour enregistrer en direct le timing des Go successifs, avant de désactiver le tout
- **Confiance** : C, résolu collectivement dans le fil après plusieurs itérations d'essai-erreur entre plusieurs contributeurs (dont un flux alternatif "quick and dirty" proposé par un second utilisateur, légèrement différent)
- **Statut** : non testé, complexité élevée
- **Intérêt** : montre une utilisation de macro comme **méta-outil pour configurer un autre sous-système** (Show Control/Timecode) plutôt que pour piloter directement la lumière — cas d'usage hors du périmètre probable de ta V1, mais à garder en mémoire comme extension possible

---

## Synthèse — apports de cette vague

1. **Deux commandes distinctes signalées avec comportement non déterministe en contexte macro** : `Go_To_Cue` (#060, #061) rejoint `SubDown/SubUp` (#027) dans la liste des commandes à risque contextuel élevé — **la thématique Navigation/conduite semble être une zone de fragilité récurrente pour l'exécution via macro**, pas seulement pour l'export ASCII
2. **Piège de concaténation de texte confirmé** (#060) — argument technique fort pour que ton moteur traite toute commande comme structure typée (nom + paramètres), jamais comme chaîne assemblée par simple concaténation
3. **Nuance importante sur l'hypothèse "macros identiques sur toutes versions"** — au moins un témoignage suggère une différence de comportement entre versions anciennes (1.9.x) — à traiter avec prudence, sans sur-interpréter un seul témoignage non confirmé par ETC
4. **Syntaxe `macro:` pour Magic Sheets** confirmée — utile pour la distribution/réutilisation multi-tournée

## Mise à jour de la liste des commandes à risque contextuel (cumulée depuis le début du corpus)

- `{Enable}/{Disable}` — dépend de l'état courant (toggle)
- `Update` — cible ambiguë selon contexte (source A, historique confirmé)
- `SelectManual` — comportement différent macro vs ligne de commande live
- `SubDown`/`SubUp` sur bump submaster — possible non-survie à l'export ASCII (à tester)
- **`Go_To_Cue`** (nouveau) — comportement non déterministe selon Foreground/Background et timing, particulièrement avec des movers dans la cue

<!-- ===== FIN : navigation_etc_forum_vague8.md ===== -->

---

<!-- ===== DEBUT : multiconsole_etc_forum_vague9.md ===== -->

# Corpus — Multiconsole / User targeting, vague 9

Source : community.etcconnect.com + manuel officiel + support ETC
Date de collecte : 29/07/2026

---

## 065 — Ciblage OSC par utilisateur : `/eos/user/<n>` (C, confirmé par un contributeur technique du forum)

- **Fil source** : "eos/key OSC commands in multi-console session"
- **Contenu confirmé** :
```
/eos/user/15                    → fixe l'utilisateur ciblé pour toute la session, jusqu'à changement ou fin de connexion
/eos/user/15/key/record         → cible un utilisateur pour une seule commande
```
- <cite reformulé>Toutes les commandes listées dans le dictionnaire OSC peuvent être ciblées vers un utilisateur si la ligne du tableau apparaît en fond grisé (plutôt que noir) — c'est le cas de `/eos/key`.</cite>
- **Confiance** : C, réponse technique précise, cohérente avec la doc OSC officielle déjà en corpus
- **Statut** : non testé
- **Limite signalée dans le même fil** : toutes les commandes `/eos/key/...` ne suivent pas ce comportement de façon uniforme — l'exemple donné est `Encoder_Category_Color`, qui fonctionne en session simple mais ne se comporte pas comme attendu en session multiconsole avec ciblage utilisateur explicite. Non résolu dans le fil.
- **Impact architecture** : cette découverte est **directement structurante pour ton moteur OSC**. Si ton appli doit un jour piloter une console en environnement multiconsole (plusieurs opérateurs), le ciblage utilisateur est le mécanisme à connaître — mais avec la réserve immédiate que toutes les commandes ne s'y comportent pas de façon fiable. À traiter comme fonctionnalité "avancée/optionnelle", pas comme un socle garanti.

## 066 — Réservation d'un User# dédié pour client OSC (B, réponse officielle probable ETC)

- **Fil source** : "Background Macro firing and commands being recorded whilst editing Macro"
- **Contenu confirmé** : <cite reformulé>à la connexion initiale d'un client OSC à Eos, le logiciel assigne au client OSC le même numéro d'utilisateur que la console primaire ; si celle-ci change de User#, le client OSC suit automatiquement. Il est recommandé de réserver un User# dédié pour le client OSC et de basculer vers celui-ci dès la connexion, via `/eos/user=99` par exemple. À partir de ce moment et jusqu'à déconnexion, le client OSC opère sous ce User 99.</cite>
- **Confiance** : B (réponse détaillée d'un profil qui semble avoir une connaissance approfondie du système, formulation proche d'une documentation)
- **Statut** : non testé
- **Impact majeur pour ton architecture** : c'est une **recommandation de bonne pratique directement actionnable** pour ton moteur OSC — ton appli Android devrait, dès la connexion, s'assigner un User# dédié et fixe plutôt que d'hériter du user de la console primaire, pour éviter toute interférence avec le travail des opérateurs humains sur la console.

## 067 — BUG CONFIRMÉ : fuite de commandes d'une macro background vers la fenêtre d'édition d'une autre macro (C, décrit avec précision, non résolu)

- **Même fil**
- **Symptôme rapporté** : pendant l'édition d'une macro (Tab 18), si une macro background déclenchée via OSC se déclenche en parallèle, ses commandes s'insèrent dans la fenêtre d'édition en cours, comme si elles avaient été tapées par l'utilisateur en train d'éditer — au lieu de s'exécuter en arrière-plan comme prévu
- **Explication analogique fournie par un contributeur** : <cite reformulé>le comportement est similaire à ce qui se produit si on appuie sur un bouton Direct Select de macro pendant qu'on édite une autre macro — la macro déclenchée ne se joue pas, elle est ajoutée au contenu de la macro en cours d'édition.</cite>
- **Confiance** : C, bug technique précis et confirmé indirectement par analogie avec un comportement connu
- **Statut** : bug non résolu au moment du fil (juin 2022) — statut actuel inconnu, à vérifier
- **Impact architecture majeur** : ceci est une **alerte de sécurité fonctionnelle sérieuse** pour ton outil. Si un régisseur utilise ton appli pour déclencher des macros en background via OSC pendant qu'un tiers (ou lui-même) est en train d'éditer une macro sur la console, le contenu de la macro en cours d'édition peut être silencieusement corrompu par l'injection de commandes non désirées. **À documenter explicitement comme avertissement utilisateur dans ton outil** : ne pas déclencher de macros via l'app pendant qu'une édition de macro est en cours sur la console.

## 068 — Ciblage de macro vers un User spécifique : piège Foreground/Background (C, confirmé par test empirique d'un contributeur)

- **Fil source** : "Macro - Target to User"
- **Symptôme** : une macro avec `{Target}` réglé sur un User spécifique ne fonctionne pas comme attendu
- **Diagnostic confirmé par un second contributeur, avec test empirique explicite** : <cite reformulé>il faut s'assurer que la macro tourne en mode Foreground — les tests confirment que le mode Background ne fonctionne pas pour ce cas, ce qui n'est pas totalement surprenant puisque le mode Background n'affecte pas la ligne de commande...</cite> (phrase tronquée dans la source, logique probable : la commande ciblée doit passer par la ligne de commande de l'utilisateur cible, ce que Background ne permet pas de faire correctement)
- **Confiance** : C, mais avec confirmation empirique explicite ("Testing on my system confirms")
- **Solution de contournement documentée par l'auteur original du fil** (imparfaite, qualifiée lui-même de non idéale) : une macro qui change temporairement l'utilisateur local, exécute le Sneak + Clear command line, puis revient à l'utilisateur assigné du Gio
- **Confiance de la solution de contournement** : D (spécifique à une console, l'auteur lui-même la qualifie de non satisfaisante à long terme)
- **Impact architecture** : **troisième confirmation** (après #027 submasters, #061 Go_To_Cue) que le choix Foreground/Background n'est pas un simple détail cosmétique — c'est un facteur déterminant de succès/échec pour plusieurs catégories de commandes. Ton validateur devrait maintenir une règle explicite : toute macro utilisant `{Target}` vers un User doit être forcée en mode Foreground, jamais Background.

## 069 — Précision officielle sur {Target} du Macro Editor (source A, déjà partiellement en corpus, complétée)

- Rappel de la vague 4 (#037), confirmé et recontextualisé ici : <cite>le Target Device peut être un nom de device ou un User ID, assigné via le softkey {Target} et {Device}/{User}.</cite>
- **Confiance** : A pour l'existence du mécanisme, complétée par C (#068) pour ses limites pratiques réelles

---

## Synthèse — apports de cette vague

1. **Mécanisme `/eos/user/<n>` et bonne pratique de réservation d'un User# dédié pour client OSC** — directement actionnable pour la conception du moteur OSC de ton outil
2. **Bug sérieux identifié** (#067) : risque de corruption silencieuse d'une macro en cours d'édition si des commandes background arrivent en parallèle — à documenter comme avertissement utilisateur explicite
3. **Quatrième cas confirmé de sensibilité au mode Foreground/Background** (après Update, Go_To_Cue en usage cue-list complexe, et maintenant le ciblage User) — ce facteur devient une **règle de validation quasi-systématique** à vérifier pour toute macro générée par ton traducteur, pas un détail secondaire

## Mise à jour de la liste des commandes/mécanismes à risque contextuel (cumulée)

- `{Enable}/{Disable}` — dépend de l'état courant (toggle)
- `Update` — cible ambiguë selon contexte (A, historique confirmé)
- `SelectManual` — comportement différent macro vs live
- `SubDown`/`SubUp` sur bump submaster — possible non-survie export ASCII (à tester)
- `Go_To_Cue` — comportement non déterministe selon Foreground/Background et timing
- **`{Target}` vers un User** (nouveau) — nécessite Foreground, ne fonctionne pas en Background (confirmé empiriquement)
- **Édition de macro concurrente avec déclenchement background** (nouveau, bug système plutôt que commande) — risque de corruption de contenu de macro en cours d'édition

<!-- ===== FIN : multiconsole_etc_forum_vague9.md ===== -->

---

<!-- ===== DEBUT : vague10_editing_macros_officiel.md ===== -->

# Corpus — vague 10 (page officielle "Editing Macros", dépouillement complet)

Source : etcconnect.com/WebDocs — manuel v3.3.6, page "Editing Macros"
Confiance : A
Date de collecte : 29/07/2026

---

## 070 — Exemple complet et inédit : macro avec Select Active, Sneak, et enchaînement vers une autre macro

Exemple officiel donné pour créer la macro 3 :

```
<Macro> [3] [Enter]
{Edit}
[Select Active] [At] [5] [Enter]
[Sneak] [Time] [1] [0] [Enter]
[Macro] [5] [Enter]
[Select]
```
- **Fonction déclarée par ETC** : régler tous les channels actifs à 50%, les faire "sneak" (fondu progressif) vers leurs niveaux d'origine sur 10 secondes, puis enchaîner (lier) vers la macro 5
- **Confiance** : A
- **Intérêt majeur** : **premier exemple officiel confirmé d'une macro qui en appelle une autre par simple juxtaposition** (`[Macro] [5] [Enter]` en fin de contenu) — jusqu'ici on n'avait que le témoignage communautaire de la vague 2 (#020, indirection macro-dans-macro) pour ce mécanisme. C'est maintenant confirmé niveau A. Ça valide directement la piste retenue pour la génération en masse.
- **Autre point technique** : confirme `[Select Active]` comme syntaxe officielle (déjà vu en usage communautaire, vague 1 #006), et introduit `[Sneak] [Time] [n] [Enter]` comme motif de fondu temporisé distinct de `Sneak Time n` (variante déjà vue en vague 1 #006 sous forme collée)

## 071 — Procédure officielle complète de création/édition en éditeur (précise et complète ce qui était fragmentaire)

- <cite>Sélectionner un numéro de macro existant et appuyer sur [Enter] affiche le détail du contenu de la macro sélectionnée. Appuyer sur {Edit} pour modifier le contenu.</cite>
- <cite>Le curseur se déplace dans la liste de contenu via les flèches. Les flèches ne sont pas stockées comme contenu de macro. Pour ajouter du contenu, positionner le curseur à l'endroit voulu puis ajouter la commande. Pour supprimer une commande, positionner le curseur juste avant elle puis presser {Delete}.</cite>
- <cite>Presser [Select] une fois l'édition terminée. Presser [Escape] pour quitter l'éditeur.</cite>
- **Confiance** : A
- **Précision structurante non capturée avant** : **[Select] termine l'édition, [Escape] quitte l'éditeur** — ce sont deux actions distinctes, pas synonymes. Jusqu'ici le corpus ne distinguait pas clairement ces deux sorties. À corriger dans la grammaire : {Done} (déjà connu), [Learn] (déjà connu), et maintenant [Select] comme troisième mécanisme de sortie/validation, différent de [Escape] qui abandonne.

## 072 — Confirmation officielle explicite de {Delete} vs la touche [Delete] (clarifie une ambiguïté du corpus)

- Le texte utilise systématiquement `{Delete}` (softkey) pour la suppression de contenu en édition — cohérent avec le piège déjà noté en vague 4 (#034) où la **hardkey** [Delete] se poste dans la macro par erreur si on l'utilise à la place de la softkey `{Delete}`. Cette page confirme sans ambiguïté que la bonne pratique documentée est bien la softkey.
- **Confiance** : A

## 073 — Liste des softkeys spécifiques à l'édition, reconfirmée texte par texte (déjà en grande partie en corpus, revalidé mot pour mot)

- `{Loop Begin}` — 0 itérations = boucle infinie (déjà confirmé x2 en usage réel, vagues 1)
- `{Loop End}`
- `{Wait}` — doit être suivi d'un nombre entier de secondes (précision : entier, pas décimal — cohérent avec le bug de décimales signalé en vague 4 #044 historique 2012, toujours d'actualité en v3.3.6)
- `{Delete}`
- `{Wait for Entr}` — reprend après [Enter]
- `{Wait for Input}` — pause jusqu'à nouvel appui sur [Macro]
- `{Done}` — sortie d'édition, alternative à [Learn]

## 074 — Confirmation officielle du motif {Enable}/{Disable} pour toggles (déjà connu, reformulation officielle exacte)

- <cite>Les macros pour des options à bascule entre activé et désactivé, comme AutoMark en setup, peuvent utiliser les softkeys {Enable} et {Disable} pour créer des actions absolues plutôt que des toggles.</cite>
- **Confiance** : A
- **Déjà en corpus** (grammaire initiale, référentiel de risques) mais cette formulation officielle confirme que le problème de non-déterminisme du toggle est **connu et documenté par ETC lui-même**, pas seulement déduit par déduction communautaire — renforce la priorité de cette règle dans le validateur.

---

## Sur l'image transmise par Cy

L'image montrée est cohérente avec cette page mais correspond au **champ de recherche** (scrollable, filtrable par frappe), pas à l'image `macro_editor_all_softkeys.png` intégrée à cette page (softkeys du CIA, disposition physique de la console) — ce sont deux vues différentes de la même liste sous-jacente de commandes. Le fetch ne peut pas lire les images (erreur technique), donc `macro_editor_all_softkeys.png` reste non exploitée. Si Cy peut la capturer en écran et la partager, ce serait la meilleure complétion possible pour clore le sujet.

**Estimation à partir de la portion visible dans l'image de Cy** : environ 50 entrées couvrant les lettres F à M de la liste. Si la liste est alphabétique complète (A à Z ou au-delà), le total pourrait avoisiner 250 à 400 commandes distinctes — largement au-delà de ce que 74 entrées collectées via forum ont permis de couvrir jusqu'ici. C'est une estimation, pas un chiffre vérifié.

---

## Synthèse — apports de cette vague

1. **Confirmation A du mécanisme macro-dans-macro** (#070) — la piste de génération en masse la plus incertaine du corpus (auparavant confiance C, un seul témoignage) passe à une confirmation officielle
2. **Clarification [Select] vs [Escape] vs {Done} vs [Learn]** comme sorties distinctes de l'éditeur — zone qui était floue
3. **La vraie priorité de collecte devient claire** : la liste de recherche complète (visible en partie dans l'image de Cy) est très probablement plus riche que tout ce que la collecte fragmentaire par forum peut fournir en un temps raisonnable. Si cette liste est capturable intégralement (capture d'écran systématique par Cy, ou toute autre méthode d'extraction), ce serait désormais l'action prioritaire n°1 du projet, devant toute poursuite de collecte par recherche web.

<!-- ===== FIN : vague10_editing_macros_officiel.md ===== -->

---

<!-- ===== DEBUT : vague11_show_control_l4.md ===== -->

# Corpus — vague 11 (nature de la liste de recherche + nouvelles sources majeures)

Date de collecte : 29/07/2026

---

## 075 — CONFIRMATION IMPORTANTE : la liste de recherche macro contient des doublons (C, mais technique et cohérent)

- **Fil source** : "Macro Editor" (déjà partiellement en corpus, vague 4 #035 — relu plus en profondeur ici)
- **Citation reformulée** : un utilisateur observe qu'en parcourant la liste de softkeys dans l'éditeur de macro, on voit en fait défiler toutes les "pages" de softkeys successivement, ce qui génère de nombreux doublons dans la liste. Il mentionne avoir vu ailleurs sur le forum une discussion évoquant un projet pour améliorer ça.
- **Confiance** : C, mais cohérent avec le fonctionnement connu des pages de softkeys sur consoles EOS
- **Impact direct sur l'estimation faite en vague 10** : mon estimation "250 à 400 commandes distinctes" à partir de l'échantillon transmis par Cy est probablement **surestimée** si la liste contient des doublons structurels. Cela ne remet pas en cause l'intérêt de la capturer, mais il faudra dédupliquer soigneusement en constituant le corpus final à partir de cette liste — ne pas prendre le nombre brut d'entrées comme nombre de commandes réellement distinctes.

## 076 — Nouvelle source majeure identifiée : Eos Family Show Control User Guide (PDF complet, Rev C, 2017 — à vérifier si version plus récente existe)

- URL : media.musson.com/mti/docs/e/o/eosfamily_showcontrol_userguide_revc.pdf (miroir tiers, contenu ETC)
- **Confiance** : A pour le contenu (document ETC officiel), miroir non-ETC donc à re-confirmer sur etcconnect.com si possible dans une prochaine recherche
- **Extraits déjà exploitables, source A** :
```
<Event> [4] [/] [1] {Address} [2] [Cue] [1] [1] [Enter]
→ crée un événement d'entrée analogique : une entrée sur l'adresse 2 déclenche la cue 11

<Event> [4] [/] [1] {Address} [3] [Macro] [1] [Enter]
→ entrée sur adresse 3 déclenche la macro 1, exécution immédiate

<Event> [4] [/] [1] {Address} [4] [Sub] [1] {On} [Enter]
→ entrée sur adresse 4 met le Sub 1 sur On
```
- <cite>Il existe quatre modes pour une entrée de submaster déclenchée en Show Control : On, Off, Bump, et Fader.</cite>
- <cite>Comme il n'y a pas de softkey d'action dédiée, appuyer sur [Cue], [Sub], ou [Macro] indique que l'on poste sur la ligne de commande.</cite>
- <cite>Toutes les chaînes envoyées depuis les appareils Eos Family sont complétées par un retour chariot (CR, 0x0D, ou 13).</cite>
- **Impact majeur** : cette dernière précision (CR systématique en fin de chaîne) est une information technique bas niveau **directement utile pour ton moteur OSC/série** — confirme un détail de protocole qui pourrait autrement causer des bugs de communication difficiles à diagnostiquer.
- **Thématique** : Show Control (MIDI/analogique/contacts secs) — zone précédemment vide du corpus, désormais couverte

## 077 — Nouvelle source majeure identifiée : Level 4 Proficient Workbook (v3.0, PDF officiel ETC)

- URL : etcconnect.com/uploadedFiles/.../Eos_Family_L4_Proficient_v2.9A.pdf
- **Confiance** : A
- Confirme et reformule ce qui était déjà connu du Tab 18 (#037, #069) : <cite>le Target Device peut être un nom de device ou un User ID, assigné via {Target} dans le Macro Display.</cite>
- **Nouvelle information** : <cite>les macros peuvent être appelées pour s'exécuter sur ou hors de la ligne de commande ("Macros can be called to run on or off the command line")</cite> — reformule et confirme la distinction Foreground/Background déjà bien documentée dans le corpus, mais avec une formulation légèrement différente à noter pour la compréhension de la grammaire
- **Autre extrait pertinent, hors macro mais utile pour le contexte grammaire général** : `[1] [CopyTo] [2] {From Absolute} [Enter]` — confirme et précise le softkey `{From Absolute}` déjà visible dans l'image transmise par Cy (premier item de la liste !), avec sa fonction exacte : fixe le channel 2 au niveau absolu du channel 1 lors d'un Copy To
- **Thématique** : ce document couvre officiellement le niveau "Proficient", au-delà du Level 3 déjà dépouillé — probablement riche en contenu macro avancé non encore exploré. À prioriser pour une prochaine vague de dépouillement complet.

## 078 — Softkeys de priorité de marking, confirmées (A, complète la thématique Mark/Auto-Mark encore peu couverte)

- Source : supplément au manuel v2.6.0/v2.6.3
- <cite>Pour assigner une priorité de marking, on utilise les softkeys {High Priority} et {Low Priority}. Lors du marking, les channels tentent d'abord de marquer vers les cues de haute priorité. Les cues simplement marquées "Mark" sont de priorité normale et utilisées en second recours. Les cues de basse priorité sont utilisées en dernier recours.</cite>
- Indicateurs d'état : `mh`/`MH` (haute priorité, en attente / en cours de marking), `ml`/`ML` (basse priorité, idem)
- **Confiance** : A
- **Intérêt** : `{High Priority}` et `{Low Priority}` apparaissent aussi dans l'image transmise par Cy — confirme que cette liste de recherche inclut bien des softkeys couvrant des fonctions générales de la console (Mark), pas seulement des commandes strictement "macro"

---

## Synthèse — apports de cette vague

1. **Correction méthodologique importante** : la liste de recherche macro contient des doublons structurels (pages de softkeys empilées) — à garder en tête pour ne pas surestimer le corpus une fois la liste capturée intégralement
2. **Deux nouvelles sources A majeures identifiées**, l'une déjà partiellement exploitée (Show Control User Guide — couvre enfin la thématique vide identifiée dans le référentiel), l'autre à peine entamée (Level 4 Proficient Workbook)
3. **Détail protocole bas niveau utile** : retour chariot systématique en fin de chaîne série/show control
4. **Confirmation croisée** entre l'image transmise par Cy et les sources texte déjà en corpus (`{From Absolute}`, `{High Priority}`/`{Low Priority}`) — bon signal de cohérence, la liste vue par Cy correspond bien au même référentiel de commandes que celui documenté par ETC

## Mise à jour du référentiel — sources à prioriser pour les prochaines vagues

- Show Control User Guide — entamé, à poursuivre (contacts secs, MIDI Show Control, timecode en détail)
- Level 4 Proficient Workbook — à peine entamé, probablement riche en Mark/Auto-Mark et fonctions avancées
- Toujours en attente : Sécurité/exploitation (grand master, inhibitions), Magic Sheets en détail, Lamp Control

<!-- ===== FIN : vague11_show_control_l4.md ===== -->

---

<!-- ===== DEBUT : vague12_liste_image_F_M.md ===== -->

# Corpus — vague 12 : liste native de commandes macro (image, portion F→M)

Source : capture d'écran transmise par Cy, provenant très probablement de la liste de recherche
de l'éditeur de macro EOS (cf. page officielle "Editing Macros", confirmée en vague 10 comme
contenant une liste "scrollable de toutes les commandes de macro").
Confiance : **A** — capture directe de l'interface console/logiciel, pas une reformulation tierce
Statut : liste brute, transcription fidèle. Doublons possibles selon l'avertissement de vague 11 (#075).
Date de collecte : 29/07/2026

---

## 079 — Transcription intégrale de la portion visible (60 entrées, ordre alphabétique F→M)

Ligne 1 : From Absolute, GEL, Go After Loop, Go To Cue 0, Greater Than, Green, Group Cells, Height, HForm, High Priority

Ligne 2 : Highlight, Hold, HS, HTP, In Time, Infinite, Input String, Insert, Insert After, Insert Before

Ligne 3 (catégorie "Common") : InterLeave, Internal, Interpolate, Intime Effect, Invert, Is In, Isn't In, Jump, Labels Only, Lamp Controls

Ligne 4 (catégorie "Softkeys") : Last Ref, Last Time, Learn Events, Less Than, Level By Address, Linear, Link, List Partition, Live, Live Moves

Ligne 5 (catégorie "Lamp Controls") : Lock, Loop, Low Priority, Macro, Macro Entry Delete, Macro Loop Begin, Macro Loop End, Macro Mode, Macro Wait, Magic Sheet

Ligne 6 (barre de recherche) : Magic Sheet Apply, Magic Sheet Edit, Make Absolute, Make Manual, Make Null, Manual, Manual Override, Mapped To, Mark, Marking

## Nouvelles entrées jamais vues dans le corpus jusqu'ici (à haute valeur)

- **From Absolute** — déjà confirmé en vague 11 (#077) via le Level 4 workbook, avec sa syntaxe complète (`[1] [CopyTo] [2] {From Absolute} [Enter]`) — confirmation croisée entre deux sources indépendantes, confiance renforcée
- **GEL** — probablement lié à la sélection de couleur par référence de gélatine, à creuser
- **Go After Loop** — mot-clé de contrôle de boucle jamais vu, distinct de `{Loop Begin}`/`{Loop End}` déjà connus — hypothèse : action à exécuter après la fin d'une boucle. **Non confirmé, à vérifier.**
- **Go To Cue 0** — confirme qu'il existe une entrée dédiée "aller à Cue 0" dans la liste, cohérent avec le motif déjà vu en vague 4 (#031, exemple officiel `Go To Cue Out`)
- **Greater Than / Less Than / Is In / Isn't In** — confirme la famille de comparaison/logique déjà repérée à la première lecture de l'image — la présence groupée de ces quatre opérateurs renforce l'hypothèse que les macros supportent une forme de logique conditionnelle, au-delà de la simple séquence linéaire déjà documentée. **Structurant, à investiguer en priorité.**
- **Group Cells** — terme inconnu du corpus, sens à déterminer (possiblement lié aux tableaux/grilles d'affichage, pas au concept de "Group" de sélection de channels déjà bien documenté)
- **Height / HForm / HS / HTP** — probablement liés à des paramètres de fixture (HS = Hue/Saturation ? HTP = Highest Takes Precedence, terme d'éclairage standard non spécifique à EOS) ou d'affichage. HTP en particulier est un terme métier connu en dehors d'EOS (règle de priorité DMX classique) — cohérence à confirmer mais probable.
- **In Time / Intime Effect** — nouveau, probablement lié aux temps d'entrée d'effet (déjà vu "Entry"/"Exit" en vague 6 pour les effets, mais jamais sous ce nom exact)
- **Infinite** — confirme indirectement le motif "0 = infini" déjà documenté pour les boucles (`{Loop Begin} 0`), suggère qu'il existe peut-être un mot-clé dédié `Infinite` utilisable ailleurs aussi
- **Input String** — nouveau, pertinent pour `{Wait for Input}` déjà connu — probablement le mécanisme sous-jacent de saisie
- **InterLeave** — nouveau, terme d'effet ou de patch (interleave = entrelacement), à investiguer
- **Internal** — nouveau, contexte à déterminer (peut-être lié à Show Control interne, cf. vague 8 #064 "Displays_More_Show Control_Internal")
- **Invert** — cohérent avec les motifs déjà vus (`{Reverse}` pour les effets, "inverts appropriate things" en vague 1 #009 Framing Mirror) — pourrait être le mot-clé générique sous-jacent
- **Labels Only** — nouveau, probablement un filtre de record/copy
- **Lamp Controls** — confirme et catégorise ce qui était déjà mentionné en vague 4 (#034) comme alternative recommandée par ETC à une macro pour l'envoi de valeurs DMX temporisées
- **Last Ref / Last Time** — nouveau, probablement liés à Select_Last déjà connu, ou au dernier temps utilisé
- **Learn Events** — confirme et nomme précisément le mécanisme déjà documenté en vague 8 (#064, "Learn_Events" utilisé de façon empirique dans le fil timecode)
- **Level By Address** — nouveau, méthode d'assignation de niveau par adresse DMX plutôt que par channel/groupe — pertinent pour un usage bas niveau
- **Link** — nouveau, à rapprocher de l'enchaînement macro-vers-macro déjà confirmé (#070, `[Macro][5][Enter]` en fin de macro) — pourrait être un mécanisme de liaison plus formel
- **List Partition** — nouveau, terme lié aux cue lists, sens exact à déterminer
- **Macro Entry Delete** — nouveau, complète la famille déjà connue (Loop Begin/End, Wait, Wait for Entr, Wait for Input, Delete) avec une variante plus spécifique
- **Macro Mode** — confirme et nomme précisément le softkey déjà documenté en vague 4/vague6 (`{Macro Mode}`, permet de choisir Foreground/Background/Default) — confirmation croisée supplémentaire
- **Magic Sheet / Magic Sheet Apply / Magic Sheet Edit** — nouveau, trois commandes distinctes liées aux Magic Sheets, jamais vues dans le corpus qui n'avait que la syntaxe `macro:` côté bouton Magic Sheet (vague 8 #063) — ici on voit le sens inverse potentiel (piloter un Magic Sheet depuis une macro)
- **Make Absolute** — confirme et nomme précisément le mécanisme déjà évoqué en vague 5 (#042, "make absolute" mentionné en passant sans nom de commande officiel)
- **Make Manual / Make Null** — nouveau, probablement liés au statut de données (manuel vs tracké/référencé, donnée nulle/vide)
- **Manual Override** — nouveau, cohérent avec le concept déjà documenté de données manuelles (fils vague 3, Proportional/Intensity Master)
- **Mapped To** — nouveau, probablement lié au patch ou au fader mapping (cohérent avec "Manual Time Master... fader mapped as" en vague 11 #101 non encore intégrée formellement)
- **Mark / Marking** — confirme et nomme les commandes derrière la thématique Mark/Auto-Mark déjà documentée en creux (vague 11 #078, indicateurs mh/MH/ml/ML) mais jamais vue sous forme de commande de macro elle-même

---

## Synthèse — apports de cette vague

1. **Trois confirmations croisées fortes** entre cette image et des sources texte déjà collectées indépendamment : `From Absolute`, `Macro Mode`, `Make Absolute` — la cohérence entre les deux types de sources (image de liste native + documentation textuelle éparse) valide la fiabilité de la méthode de collecte suivie jusqu'ici.
2. **Découverte structurante non résolue** : la présence groupée de `Greater Than`, `Less Than`, `Is In`, `Isn't In` suggère une capacité de logique conditionnelle dans les macros EOS, jamais documentée ni même évoquée ailleurs dans le corpus. Si confirmée, c'est une extension majeure du modèle mental "macro = séquence linéaire de touches" retenu jusqu'ici pour la conception de la représentation interne.
3. **Famille Magic Sheet côté macro** (Magic Sheet, Magic Sheet Apply, Magic Sheet Edit) — jamais vue, à investiguer, pertinent pour la thématique Affichage/interface encore peu couverte.
4. **~40 termes nouveaux au total**, dont la majorité reste **non confirmée quant à sa syntaxe exacte et sa fonction précise** — cette liste donne des noms, pas des exemples d'usage. Elle doit être croisée avec de la recherche ciblée (documentaire ou test au banc) terme par terme pour devenir exploitable dans un traducteur, pas seulement listée.

## Portions encore manquantes de la liste complète

Cette capture couvre uniquement F→M. Restent inconnues : **A→E** et **N→Z** (au minimum — l'ordre alphabétique strict n'est pas garanti sur toute la liste, à vérifier). Etant donné le rythme d'environ 60 entrées pour ~7 lettres, une estimation grossière pour la liste complète serait de l'ordre de 200-250 entrées **avant déduplication** (rappel de l'avertissement vague 11 #075 sur les doublons de pages).

## Action prioritaire suggérée pour la suite

Plutôt que de continuer à chercher cette liste par fragments aléatoires (peu fructueux jusqu'ici), il serait plus efficace de rechercher spécifiquement les termes non résolus de cette vague un par un dans la documentation ou le forum ETC — en particulier `Go After Loop`, `Greater Than`/`Less Than`/`Is In`/`Isn't In` (logique conditionnelle), et la famille Magic Sheet.

<!-- ===== FIN : vague12_liste_image_F_M.md ===== -->

---

<!-- ===== DEBUT : vague13_correction_greater_less_than.md ===== -->

# Corpus — vague 13 : clarification des opérateurs de comparaison (correction d'hypothèse)

Date de collecte : 29/07/2026

---

## 080 — CORRECTION : Greater Than / Less Than sont liés au système de Query par mots-clés custom, pas à une logique conditionnelle générale de macro

- **Fil source** : "Possible Query Keyword bug" (fil ancien, ~2010-2011 d'après le contexte, toujours d'actualité pour la mécanique de fond)
- **Contenu confirmé, source B** (échange direct avec un développeur/support ETC identifié comme "Josh" dans le fil) :
- <cite reformulé>Après import de mots-clés personnalisés depuis un logiciel tiers (LightWright) vers Eos, un utilisateur teste des requêtes Query et remarque deux problèmes : les mots-clés commençant par un chiffre échouent à la requête et effacent partiellement la ligne de commande ; les mots-clés contenant des espaces échouent aussi.</cite>
- <cite reformulé>Il note également que les symboles "greater than" (>), "less than" (<), et l'accent circonflexe (^) ne peuvent pas non plus se poster comme premier caractère — ce qui pose problème car de nombreux ALD (Assistant Lighting Designers) utilisent ces symboles en début de mot-clé pour indiquer un objectif ou une intention dans leurs annotations.</cite>
- **Réponse du support ETC confirmée dans le fil** : le problème des espaces est expliqué — <cite reformulé>quand un mot-clé est stocké dans le show, tous les espaces sont convertis en underscores, probablement parce que des espaces dans le mot-clé le feraient ressembler à deux mots distincts pour le parseur. Ces espaces ne sont pas convertis de façon symétrique dans les champs Texte du Patch, d'où l'échec de correspondance lors d'une requête Query.</cite>
- **Confiance** : B (échange direct avec profil support/développeur ETC identifiable, contenu technique précis et cohérent)
- **Statut** : confirmé quant au contexte d'usage, mais **ne donne pas la syntaxe exacte de commande** `Greater Than`/`Less Than` telle qu'utilisable dans une macro moderne — seulement le contexte historique de leur origine (mots-clés Query, pas opérateurs logiques de macro au sens programmation)

## Révision de l'hypothèse posée en vague 12 (#079)

L'hypothèse formulée en vague 12 — "les macros supportent une forme de logique conditionnelle" — **doit être révisée à la baisse**. Ce que confirme cette vague 13 : `Greater Than` et `Less Than` sont très probablement des **opérateurs de filtre pour les requêtes Query sur mots-clés/attributs de patch** (typiquement : rechercher tous les channels dont un attribut numérique personnalisé est supérieur/inférieur à une valeur), pas des instructions de branchement conditionnel façon `if/else` dans une séquence de macro.

Ça reste un mécanisme puissant et pertinent pour ton corpus (motif de **sélection dynamique de channels par condition sur un mot-clé/attribut**, thématique Sélection & patch), mais ce n'est pas la découverte "programmation conditionnelle en macro" que la première lecture de l'image suggérait. **`Is In` / `Isn't In`** restent non résolus dans cette vague — probablement de la même famille (filtre d'appartenance à un ensemble, ex: "channel appartient à Group X"), à confirmer séparément.

- **Impact sur le référentiel** : correction méthodologique importante à retenir — une liste de noms de commandes sans exemple de syntaxe (comme l'image collectée en vague 12) peut suggérer des interprétations excessives. Toujours croiser avec une source d'usage réel avant de tirer une conclusion structurante pour l'architecture.

---

## Synthèse de cette vague

1. **Hypothèse de logique conditionnelle en macro invalidée** (ou du moins non confirmée) — reclassée en mécanisme de filtre Query, cohérent avec la famille déjà connue (`Query Dark_Moves`, `Query Live_Moves`, etc.)
2. **Deux bugs historiques documentés** sur le système de mots-clés custom (espaces convertis en underscore de façon asymétrique, échec sur premier caractère spécial) — pertinent si ton traducteur doit un jour générer des requêtes Query sur mots-clés personnalisés, mais périphérique à la priorité actuelle (macros)
3. **`Is In`/`Isn't In` restent à investiguer** séparément — hypothèse actuelle : filtre d'appartenance, cohérent avec la famille Query

<!-- ===== FIN : vague13_correction_greater_less_than.md ===== -->

---

<!-- ===== DEBUT : vague14_query_semantique_variables.md ===== -->

# Corpus — vague 14 : sémantique Query complète, fragilité macro confirmée à grande échelle

Date de collecte : 29/07/2026

---

## 081 — Sémantique complète des quatre opérateurs Query (A/B, réponse ETC officielle dans le fil)

- **Fil source** : "Query on Query" — réponse identifiée comme provenant d'ETC (contexte du fil, réponses techniques précises typiques du support)
- **Contenu confirmé** :
```
{Is In}      → le channel est actuellement dans cet état ("is in CP5")
{Could Be}   → le channel a des données stockées dans la cible visée, sans y être actuellement
{Can't Be}   → le channel n'a pas de données stockées dans la cible visée
{Isn't In}   → le channel n'est pas actuellement dans cet état
```
- **Exemple officiel donné** : `[Query]{Is In}[Preset][2][0][Enter]`
- **Confiance** : A/B (réponse à caractère officiel, cohérente et précise)
- **Impact direct sur la révision de vague 13** : ceci confirme et complète parfaitement l'hypothèse révisée — `{Is In}`/`{Isn't In}` (vus dans l'image, vague 12) sont bien de la famille Query, pas de la logique conditionnelle de macro. Et on découvre au passage **deux opérateurs Query supplémentaires non présents dans l'image** : `{Could Be}` et `{Can't Be}` — la liste de recherche capturée par Cy ne couvrait donc pas tout, même sur les lettres qu'elle affichait (C se trouve avant F, donc logique qu'elle soit absente de la portion F→M).

## 082 — Précision officielle sur {Group} comme sélecteur pur (A/B, distingue Group de Recall From)

- **Même fil**
- <cite reformulé>Le Group est uniquement un sélecteur de channels. `[Group][Color Palette][1][Enter]` sélectionne tous les channels ayant des données stockées dans la palette couleur 1.</cite>
- <cite reformulé>`[Group][Preset][xx][Enter]` sélectionne les channels associés à ce preset ET les place à leur valeur IFCB enregistrée ; `[Group][Preset][xx][At][0][Enter]` sélectionne les channels et leur assigne uniquement une valeur de zéro.</cite>
- **Confiance** : A/B
- **Note de transparence intéressante d'ETC lui-même** : le même contributeur reconnaît qu'<cite reformulé>il y a eu beaucoup de confusion sur le fonctionnement de Group, Recall From et Query, et que ces règles étaient en cours d'ajustement dans une version à venir (1.3.1) pour rendre le jeu de règles complètement cohérent.</cite>
- **Impact architecture** : cette reconnaissance officielle d'une ambiguïté historique corrobore directement pourquoi ton système de validation avec menus déroulants (déjà noté en idée produit) est pertinent — même ETC admet que la distinction entre ces mécanismes de sélection a été/est source de confusion pour les utilisateurs eux-mêmes.

## 083 — Exemple complet et avancé combinant Group + Query en macro (C, syntaxe détaillée)

- **Fil source** : "Query; single vs multiple cues in blind; select last"
```
[Group] [1] [Query] {Is In} [Que] [Home] [Thru] [Query] {Can Be} [Preset] [3] [Enter]
```
- **Fonction déclarée** : limite la recherche au Group 1 en tête de ligne (réduisant fortement le résultat), puis interroge, à travers toute la cue list (Home Thru), quels channels de ce groupe ont des données stockées ("Can Be" — sic, l'utilisateur semble utiliser une variante de {Could Be}) dans le Preset 3
- **Confiance** : C, utilisateur expérimenté mais syntaxe non revérifiée par ETC dans ce fil précis
- **Piège confirmé par l'auteur lui-même dans le fil** : `{Select Last}` ne fonctionne pas comme attendu après une requête Query complexe — au lieu de renvoyer la sélection de channels résultante, il relance la syntaxe de la requête Query elle-même. Comportement jugé säcompris comme un problème par l'utilisateur, non résolu formellement dans le fil.
- **Impact** : nouveau cas à ajouter au référentiel de risques contextuels — `{Select Last}` après une requête Query composée a un comportement différent de son usage simple déjà bien documenté ailleurs dans le corpus (vague 1, vague 7).

## 084 — TÉMOIGNAGE MAJEUR : confirmation systémique et frontale de la fragilité des macros par un utilisateur expérimenté (C, mais extrêmement révélateur)

- **Fil source** : "Macro syntax help"
- **Contexte** : un utilisateur tente de construire une macro pour sélectionner uniquement les channels patchés (l'inverse fonctionne : sélectionner les non-patchés), en utilisant `Query is_in Unpatched` / `Query isn't in Unpatched` — confirme au passage la syntaxe exacte de cette famille de commandes en usage réel, cohérente avec #081
- **Citation reformulée, la plus importante du corpus à ce stade** : après plusieurs échanges infructueux avec d'autres membres du forum, l'utilisateur écrit être amusé par toute cette histoire — il indique être venu chercher de l'aide et n'avoir reçu que très peu d'information réellement utile, la plupart de ce qu'on lui a répondu étant soit franchement faux, soit trompeur. Il trouve cela symptomatique d'un problème systémique dans la création de macros sur EOS : de nombreuses astuces, réglages et comportements par défaut qui fonctionnent en usage normal ne se traduisent pas en macro.
- **Confiance** : C — c'est un témoignage d'expérience, pas une donnée technique vérifiable en soi — **mais sa valeur documentaire pour ton projet est exceptionnelle**, précisément parce qu'il formule en une phrase le problème central que 84 entrées de collecte fragmentaire ont mis en évidence indirectly depuis le début : `Go_To_Cue` inconsistant (#060-061), `SubDown/SubUp` fragile à l'export (#027), `{Target}` vers User qui échoue en Background (#068), `SelectManual` invalide en live mais partiellement utilisable en macro (#043), et maintenant `{Select Last}` après Query composé (#083).
- **Statut** : à conserver comme citation de référence — pas une donnée de grammaire à proprement parler, mais une validation qualitative forte du besoin auquel ton outil répond, et un rappel que la validation de sécurité (côté outil, pas juste côté syntaxe) doit être prise très au sérieux
- **Détail technique confirmé dans le même fil, à valeur normative (source utilisateur avancé, résultat vérifié ~20 fois)** : en Blind, la vue par défaut est la Cue List ; invoquer une IP (Intensity Palette ou équivalent) transforme les tombstones de Blind en tombstones IP, mais **ne bascule pas la vue vers la IP List View** — nuance fine sur l'état d'affichage en Blind, pertinente si ton outil doit un jour générer des macros de navigation d'affichage.

## 085 — ABSENCE CONFIRMÉE de variables/formules dans EOS, feature request de longue date sans suite (B/A, réponse ETC directe)

- **Fil source** : "Using variables on EOS"
- **Demande formulée par les utilisateurs** : possibilité de faire des chases/effets basés sur des maths/formules, sélectionner un groupe selon une condition (`if mode=1 use group 1`), choisir une palette couleur selon l'effet tournant sur un autre groupe
- **Réponse ETC (identifiable comme tel dans le fil, "Patrick")** : <cite reformulé>c'est sur la liste des évolutions envisagées côté EOS, mais difficile de dire quand — c'est un chemin sinueux.</cite> Puis en réponse à une relance plusieurs mois/années après : <cite reformulé>pas de rumeur particulière, étant donné la charge de travail sur les priorités du haut de la liste, il ne faut pas s'attendre à ce que le sujet des variables prenne beaucoup de traction. Il existe quelques extensions au système de Query qui... (phrase tronquée dans la source)</cite>
- **Confiance** : A/B pour la confirmation officielle de l'absence de mécanisme de variable global
- **Impact architecture majeur, et definitif sur un point resté ouvert depuis la vague 2** : ceci **confirme officiellement, par ETC lui-même**, que EOS ne dispose pas nativement d'un vrai système de variables ou de formules. Le mécanisme d'indirection macro-dans-macro (#020, confirmé A en #070) reste donc le seul palliatif disponible — pas une fonctionnalité native cachée, mais un contournement créatif de la communauté face à une limitation reconnue et documentée comme telle par ETC. Cela **valide directement** la pertinence de la stratégie retenue pour la génération en masse dans ton architecture : c'est la meilleure option disponible sur la plateforme, pas une solution de second choix.

---

## Synthèse — apports de cette vague (l'une des plus importantes du corpus à ce stade)

1. **Sémantique Query complètement close** : les 4 opérateurs (`Is In`, `Isn't In`, `Could Be`, `Can't Be`) sont maintenant tous confirmés avec leur fonction exacte — clôt définitivement la question ouverte depuis la vague 12/13
2. **Confirmation officielle ETC de l'absence de variables** — valide rétroactivement la stratégie de génération en masse retenue pour l'architecture (macro-dans-macro)
3. **Nouveau cas de risque contextuel** : `{Select Last}` après une requête Query composée
4. **Le témoignage #084 mérite une place à part** — il ne s'agit pas d'une donnée de grammaire mais d'une validation qualitative externe et indépendante du problème que ton projet cherche à résoudre. À citer si besoin de justifier l'intérêt du projet plus tard (pitch, argumentaire).

## Mise à jour du référentiel de risques

Ajouter au tableau de `REFERENTIEL_RISQUES_ET_GRILLE.md` :
- `{Select Last}` après une requête `Query` composée — relance la syntaxe de requête au lieu de renvoyer la sélection résultante (C, vague14 #083)

<!-- ===== FIN : vague14_query_semantique_variables.md ===== -->

---

<!-- ===== DEBUT : vague15_securite_exploitation.md ===== -->

# Corpus — vague 15 : Sécurité / exploitation (première couverture de cette thématique)

Date de collecte : 29/07/2026

---

## 086 — Distinction officielle Shielded vs Inhibitive (source A, article support dédié)

- Source : support.etcconnect.com, "Is There a Difference Between a Shielded Fader and an Inhibitive Fader?"
- <cite>Régler le mode d'un submaster sur Inhibitive limite la sortie live de son contenu. Les channels maîtrisés par un submaster inhibitif sont indiqués par un "I" à côté de la valeur d'intensité dans l'affichage live. Les submasters inhibitifs ne fournissent pas de niveaux à l'image scénique, ils les limitent.</cite>
- <cite>Autrement dit, le submaster inhibitif agit comme un grand master pour les channels qu'il contient, et peut manipuler leur sortie live de façon proportionnelle. Ce comportement est identique sur toutes les versions du logiciel Eos.</cite>
- **Confiance** : A
- **Statut** : directement exploitable, formulation officielle exacte
- **Thématique** : Sécurité / exploitation — première entrée du corpus sur ce sujet

## 087 — Shielded submaster : priorité absolue, y compris sur le Grand Master (C, confirmée, avec contrainte de version)

- **Fil source** : "Independent Submaster"
- <cite reformulé>Régler la priorité d'un sub sur "Shielded" signifie que les channels de ce sub ne sont contrôlés que par ce sub et ne peuvent être outrepassés par aucun autre moyen, y compris le Grand Master.</cite>
- **Contrainte de version précisée** : fonctionnalité introduite en v1.9.6 — nécessite une version égale ou supérieure
- **Confiance** : C, mais cohérente avec la doc officielle #086 (qui n'emploie pas le terme "Shielded" mais en décrit implicitement le principe par contraste)
- **Cas d'usage concret donné** : protéger des channels d'éclairage de travail (worklights) pour qu'ils restent toujours pilotables indépendamment du reste du système, même en cas de blackout général via Grand Master
- **Thématique** : Sécurité / exploitation
- **Statut** : non testé

## 088 — Pattern combiné Inhibitive Sub + macro pour un scénario "pause déjeuner" (C, motif directement transposable)

- **Même fil**
- <cite reformulé>On pourrait créer un sub inhibitif contenant tous les channels sauf les worklights, le laisser toujours en position haute, et au moment de la pause, baisser ce sub inhibitif tout en montant un autre sub dédié — le tout transformable en une macro pour éviter d'avoir à manipuler physiquement les faders.</cite>
- **Confiance** : C
- **Statut** : non testé
- **Intérêt** : c'est un **motif de sécurité/exploitation directement descriptible en langage naturel** ("mets tout en pause sauf les éclairages de travail") — bon candidat de cas d'usage pour illustrer/tester ton traducteur NL sur cette thématique encore peu couverte

## 089 — Configuration d'un fader en Grand Master : procédure d'interface, pas syntaxe de commande (C, procédure confirmée)

- **Fil source** : "Grand Master Submaster"
- **Procédure confirmée** : Fader Config (Tab 36) → sélectionner un fader vide → cliquer sur "Unassigned" → choisir "Grandmaster" dans le nouveau menu qui apparaît
- **Confiance** : C
- **Statut** : procédure d'interface tactile/souris, pas de syntaxe de ligne de commande associée trouvée dans ce fil — **pertinent surtout pour signaler que cette configuration n'est probablement pas pilotable par macro/commande texte**, contrairement à la plupart des autres objets EOS déjà documentés dans le corpus. Point de vigilance pour le périmètre de ton traducteur : certaines configurations restent liées à l'interface graphique et hors de portée d'une génération par commande.

---

## Synthèse — apports de cette vague

1. **Première couverture réelle de la thématique Sécurité/exploitation**, restée vide depuis le début du corpus (identifiée comme manquante dans le référentiel dès la vague de consolidation)
2. **Distinction Shielded/Inhibitive/Grand Master clarifiée**, avec une source A directe
3. **Motif "pause déjeuner" (#088)** — bon cas d'usage de test pour le traducteur NL sur cette thématique
4. **Limite de périmètre identifiée** : la configuration de fader en Grand Master semble être une opération d'interface graphique (Tab 36), pas une commande texte — à vérifier si un équivalent en ligne de commande existe ailleurs dans la documentation avant de conclure définitivement que cette fonction est hors de portée du traducteur

<!-- ===== FIN : vague15_securite_exploitation.md ===== -->

---

<!-- ===== DEBUT : vague16_lamp_controls.md ===== -->

# Corpus — vague 16 : Lamp Control (première couverture de cette thématique)

Date de collecte : 29/07/2026

---

## 090 — Syntaxe exacte de macro Lamp Control (C, confirmée et corrigée en cours de fil)

- **Fil source** : "recording lamp controls into macros"
- **Contenu initial rapporté (EOS 1.8)** :
```
Group 301 [enter]
Lamp_controls Lamp_control Fixture_Global_Wakeup [enter][enter]
```
- **Symptôme du bug initial** : la macro apprise sélectionne bien les channels mais n'exécute pas le lamp control lui-même
- **Correction confirmée fonctionnelle par l'auteur original après suggestion d'un autre membre** : le premier `Lamp_controls` (au pluriel, en tête) est superflu et problématique — la syntaxe correcte omet ce premier terme, de même que le premier `[enter]` qui le suit
- **Confiance** : C, mais correction confirmée explicitement comme fonctionnelle ("your suggestion worked")
- **Piège complémentaire signalé par le même auteur** : impossible de faire apparaître les commandes Lamp Control dans la liste de l'éditeur de macro en construisant depuis zéro — les tuiles tactiles de lamp control sur l'écran n'ont aucun effet en mode édition directe. La seule méthode fonctionnelle constatée est d'apprendre (Learn) la macro en direct pour que les commandes lamp control y apparaissent.
- **Confiance de ce second point** : C
- **Impact architecture majeur** : ceci est un **nouveau cas confirmé, et particulièrement net**, de la règle déjà établie en vague 4 (#034, doctrine ETC "Learn d'abord, édition en correction seulement"). Pour Lamp Control spécifiquement, l'édition directe semble carrément non fonctionnelle, pas seulement déconseillée. À noter comme règle forte pour ce sous-domaine particulier.

## 091 — Deuxième confirmation indépendante, avec syntaxe complète pour deux macros (Lamp On / Lamp Off) (C)

- **Fil source** : "Me Again - Eos Lamp On Command Macro"
```
[Learn] [Macro] [1] [Enter] [Channel Select] [Lamp On] [Enter] [Learn]
[Learn] [Macro] [2] [Enter] [Channel Select] [Lamp Off] [Enter] [Learn]
```
- **Contexte du besoin exprimé** : allumer les lampes de fixtures (Mac 250 Krypton/Wash) en tout début de show, avec un délai de 5 minutes pour laisser le temps de calibration, intégré à la cue 1/1
- **Confiance** : C, réponse d'un contributeur habituel, non contestée dans le fil
- **Piège rapporté par l'auteur original du fil, non résolu explicitement** : en éditeur de macro Blind, la softkey "Lamp On" du CID ne fait rien apparaître dans la fenêtre de contenu de macro — alors que "Fixture Reset" fonctionne correctement dans le même contexte. Question posée si c'est lié au profil du fixture, restée sans réponse claire dans l'extrait consulté.
- **Confiance de ce point** : D (comportement incohérent, cause non identifiée)
- **Recoupement avec #090** : ce second témoignage indépendant confirme le même phénomène général (Lamp Control capricieux en édition directe), avec un niveau de détail différent (Lamp On fonctionne différemment de Fixture Reset) — renforce la crédibilité du problème sans le résoudre complètement

## 092 — Où se configurent les Lamp Controls disponibles pour un fixture (C, confirmée, structurel plutôt que syntaxe de commande)

- **Fil source** : "I can't find the Lamp Controls for a Custom Fixture"
- <cite reformulé>En éditant un profil de fixture personnalisé, il ne faut pas ajouter un paramètre de la catégorie "control" avec des plages de valeurs configurées manuellement — il faut plutôt, après avoir ajouté le paramètre, presser la softkey "LampCtrls" et y ajouter les fonctions de reset voulues (par exemple Pan/Tilt Reset, Lamp Reset, Global Fixture Reset).</cite>
- **Confiance** : C
- **Statut** : configuration de patch/profil, en amont de tout usage en macro — pertinent pour comprendre pourquoi certains fixtures n'ont pas de Lamp Control disponible du tout (absence de configuration côté profil, pas un bug de macro)
- **Thématique** : à cheval entre Sélection & patch et la nouvelle sous-catégorie Lamp Controls

---

## Synthèse — apports de cette vague

1. **Première couverture réelle de Lamp Controls**, thématique identifiée comme manquante depuis la vague 4 (où elle n'apparaissait qu'en négatif, comme alternative recommandée par ETC à une macro pour l'édition de guirlande DMX temporisée — jamais creusée pour elle-même jusqu'ici)
2. **Confirmation redondante et cohérente (deux fils indépendants) que Lamp Control ne se construit fiablement qu'en Learn**, jamais en édition directe — cas le plus net du corpus pour la règle déjà connue "Learn d'abord"
3. **Syntaxe de commande confirmée et corrigée** : `Group <n> [enter] Lamp_control <fonction> [enter][enter]` (sans le premier "Lamp_controls" pluriel superflu)
4. Reste non résolu : la cause exacte de l'incohérence de comportement entre différentes softkeys de Lamp Control (`Lamp On` vs `Fixture Reset`) en édition directe — signalé mais non expliqué dans les sources consultées

<!-- ===== FIN : vague16_lamp_controls.md ===== -->

---

<!-- ===== DEBUT : vague17_magic_sheets_github.md ===== -->

# Corpus — vague 17 : Magic Sheets approfondi + découverte dépôt GitHub ETC officiel

Date de collecte : 29/07/2026

---

## 093 — Règle de conception Magic Sheet confirmée par plusieurs contributeurs convergents (C, bonne pratique)

- **Fil source** : "Commands in Magic Sheet"
- <cite reformulé>Si une action peut être faite directement en Command, il vaut mieux utiliser Command plutôt qu'une macro ; si nécessaire, apprendre la macro puis copier son contenu directement dans le champ texte de commande du bouton.</cite>
- **Confiance** : C, avis convergent de plusieurs contributeurs
- **Impact architecture** : suggère une hiérarchie de préférence pour ton moteur — privilégier la génération de commande texte directe (type Command) plutôt qu'une macro dédiée, quand c'est possible. Cohérent avec la philosophie déjà retenue de séparer représentation interne et moteurs de rendu : le "rendu Magic Sheet" pourrait être un troisième mode de sortie à envisager, à côté d'ASCII et OSC/clavier.

## 094 — DÉCOUVERTE MAJEURE : dépôt GitHub officiel ETC Labs listant les clés OSC (à vérifier et exploiter en priorité)

- **Fil source** : "Magic Sheet Target: Command"
- **URL mentionnée dans le fil** : `github.com/ElectronicTheatreControlsLabs/OSCLayouts/blob/master/Eos OSC Keys.pdf`
- **Confirmation dans le même fil** : <cite reformulé>les commandes utilisables en Magic Sheet de type Command sont généralement celles qu'on retrouve dans les macros — en cas de doute, la méthode recommandée reste d'apprendre la commande comme macro puis de l'observer.</cite> Un second contributeur confirme que les commandes OSC et les commandes de macro sont vraisemblablement les mêmes, avec une réserve : le PDF ne permet pas de distinguer visuellement laquelle est la véritable touche (key) parmi les entrées.
- **Confiance** : **B/C** — dépôt communautaire ETCLabs, explicitement marqué non-officiel malgré le nom (voir correction en vague18 #100). Le PDF mentionné n'a pas été retrouvé dans le dépôt actuel (vague18 #101) — piste non aboutie.
- **Impact architecture majeur** : si ce PDF existe et est à jour, c'est potentiellement **la meilleure source de grammaire OSC/macro trouvée à ce jour**, au même niveau que le dictionnaire OSC officiel déjà consulté en début de projet (Show Control Manual en ligne). **Action prioritaire de la prochaine vague : consulter directement ce PDF.**

## 095 — NUANCE IMPORTANTE sur macro-dans-macro : confirmé en théorie, mais rapporté comme non fonctionnel dans au moins un cas réel (C, contredit partiellement #070)

- **Fil source** : "Can a macro be referenced in another macro or in a Command button on a magic sheet?"
- **Syntaxe confirmée par un contributeur, cohérente avec #070** : dans l'éditeur, taper `Macro Z Enter` à la fin d'une macro pour enchaîner vers la macro Z
- **MAIS l'auteur original du fil rapporte explicitement que cette même syntaxe, dans son cas, ne fonctionne pas** : <cite reformulé>c'est la syntaxe qu'il essayait déjà d'utiliser, mais ça ne semble pas exécuter la macro Z depuis la macro A.</cite>
- **Confiance** : C, mais c'est un signal direct et net de non-fiabilité
- **Statut** : fil consulté sans résolution claire de la cause (pas de suite visible dans l'extrait) — **à traiter comme un cas de risque contextuel supplémentaire**, potentiellement lié au mode Foreground/Background (cohérent avec le pattern déjà établi ailleurs dans le corpus) ou à un autre facteur non identifié
- **Impact sur le référentiel** : le mécanisme de macro-dans-macro, bien que confirmé niveau A dans son principe syntaxique (#070, manuel officiel), **n'est visiblement pas garanti fonctionner dans toutes les configurations**. À rétrograder d'un niveau de confiance opérationnelle : la syntaxe est officiellement correcte, mais l'exécution fiable reste à valider au banc avant de baser une fonctionnalité critique de génération en masse dessus sans filet.

## 096 — Piège de syntaxe non-évidente pour la navigation entre vues de Magic Sheet (C, motif de "chaîne figée")

- **Fil source** : "Magic Sheet view macro"
- **Symptôme rapporté** : une macro destinée à naviguer vers une vue/partie spécifique d'un Magic Sheet (`magic_sheet>1>part>1`), bien que syntaxiquement identique à un ancien fichier fonctionnel, ne se comporte pas de la même façon — le nombre attendu ne peut être modifié comme dans l'original, qui était stocké comme une seule chaîne non modifiable (`'10 part 1'`)
- **Résolution finale** : erreur opérateur — un bouton et un texte étaient groupés par erreur, redirigeant le focus d'édition vers le mauvais objet
- **Confiance** : D pour la cause du problème initial (résolu comme erreur humaine, pas un vrai piège système) mais **information utile en creux** : ceci confirme que la commande de navigation Magic Sheet peut être stockée comme une chaîne figée non-paramétrable dans certains contextes — pertinent si ton outil génère un jour ce type de navigation
- **Thématique** : Affichage/interface

## 097 — Pattern avancé : feedback visuel dynamique sur bouton Magic Sheet, deux méthodes documentées (C, motif directement transposable)

- **Fil source** : "Colour Changing Buttons on Magic Sheets"
- **Méthode 1 (changement de couleur du bouton)** : deux color palettes factices sur un channel dummy (l'une rouge, l'autre verte), copiées alternativement vers une palette "active" référencée par l'objet bouton via `Copy_to`
- **Méthode 2 (changement de label du bouton, jugée préférée par les contributeurs)** :
```
Macro 101 (ON) se termine par : Copy Macro 102 to 100
Macro 102 (OFF) se termine par : Copy Macro 101 to 100
```
Le bouton Magic Sheet référence toujours Macro 100, réglé pour afficher son label plutôt qu'un texte fixe — chaque pression fait basculer le label affiché
- **Confiance** : C, plusieurs contributeurs, méthode confirmée comme fonctionnelle par l'auteur original du fil après clarification
- **Impact majeur** : **troisième confirmation indépendante et concrète du mécanisme d'auto-modification de macro** (`Copy Macro X to Y` exécuté depuis l'intérieur d'une macro elle-même) — fait écho direct à l'entrée D peu fiable de la toute première vague (#011, "parking macro auto-modifiante", jugée alors confuse et non reproductible). Ici la même logique de fond est confirmée avec une syntaxe claire et un cas d'usage cohérent. **Reclassification recommandée** : ce motif passe de "D, non reproductible" à "C, confirmé par un cas indépendant et clair" — à mettre à jour rétroactivement dans le référentiel.

## 098 — Confirmation supplémentaire de motif Query avec paramétrage relatif (C, nouvelle famille)

- **Fil source** : "Magic Sheet...is this possible?"
```
select_last_params @ +01 Enter
select_last_params @ + -01 Enter
```
- **Fonction déclarée** : sélectionne le dernier fixture/attribut travaillé et ajoute ou soustrait 1 à sa valeur — équivalent macro du raccourci clavier Shift+At
- **Confiance** : C
- **Intérêt** : nouvelle variante de la famille `Select_Last` déjà bien documentée, avec incrémentation relative — pertinent pour tout scénario de réglage fin généré par ton traducteur

## 099 — Clear Sneak Enter en Magic Sheet : Command préféré à macro (C, confirme #093)

- **Fil source** : "Magic Sheet- button or macro for clear-sneak-enter?"
- Confirmation pratique et directe de la règle #093 : l'auteur du fil confirme avoir utilisé l'option Command (texte `Clear Sneak Enter` dans le champ commande) plutôt qu'une macro dédiée, et que "ça a marché comme un charme"
- **Confiance** : C, confirmation directe par test réel
- **Thématique** : Affichage/interface, Navigation/conduite

---

## Synthèse — apports de cette vague (riche en révisions et nuances importantes)

1. **Découverte prioritaire pour la prochaine vague** : dépôt GitHub `ElectronicTheatreControlsLabs/OSCLayouts`, contenant potentiellement un PDF exhaustif des clés OSC — à consulter directement en premier lieu
2. **Nuance majeure sur macro-dans-macro** (#095) : le mécanisme est officiellement correct en syntaxe (déjà confirmé A) mais son exécution fiable n'est pas garantie dans tous les contextes — à traiter avec la même prudence que les autres cas de risque contextuel du référentiel, malgré son statut de confiance syntaxique élevé
3. **Reclassification recommandée** du motif d'auto-modification de macro (`Copy Macro X to Y` depuis l'intérieur d'une macro) : de D (premier témoignage confus) à C (confirmé par un second cas clair et cohérent, #097)
4. **Règle de conception confirmée** : privilégier Command à macro quand c'est possible (#093, #099) — pertinent pour la hiérarchie de rendu de ton moteur

## Actions à reporter dans le référentiel

- Ajouter au tableau de risques : macro-dans-macro (`Macro <n> Enter` en fin de macro) — syntaxe correcte confirmée A, mais exécution fiable non garantie selon contexte (C, #095)
- Reclassifier l'entrée #011 (vague 1) de D vers C, avec renvoi vers #097 comme confirmation croisée

<!-- ===== FIN : vague17_magic_sheets_github.md ===== -->

---

<!-- ===== DEBUT : vague18_correction_etclabs.md ===== -->

# Corpus — vague 18 : correction de statut ETCLabs, PDF introuvable

Date de collecte : 29/07/2026

---

## 100 — CORRECTION DE CONFIANCE : ETCLabs/OSCLayouts est explicitement non-officiel (invalide partiellement l'optimisme de vague 17 #094)

- Le dépôt GitHub `ETCLabs/OSCLayouts` (anciennement sous le nom d'organisation `ElectronicTheatreControlsLabs`, d'où l'URL trouvée dans le forum) affiche explicitement dans son README : <cite>ce n'est pas un logiciel ETC officiel. Le support ETC ne connaît pas ces outils et ne pourra pas aider en cas de problème.</cite>
- <cite>Les layouts de ce projet sont développés par une combinaison d'utilisateurs finaux et d'employés ETC sur leur temps libre.</cite>
- **Confiance corrigée** : **C/B**, pas A. C'est un espace communautaire officieux, avec participation d'employés ETC à titre personnel — plus fiable qu'un forum anonyme, mais pas une source normative au même titre que la documentation officielle ETC (etcconnect.com, support.etcconnect.com).
- **Correction à appliquer** : la mention "confiance A potentielle" faite en vague 17 (#094) était trop optimiste et doit être révisée à B/C dans toute référence future.

## 101 — Le PDF "Eos OSC Keys.pdf" mentionné dans le forum n'a pas été retrouvé dans le dépôt actuel

- Recherche effectuée directement dans le dépôt cloné (`ETCLabs/OSCLayouts`, état au 29/07/2026) : aucun fichier nommé "Eos OSC Keys" ou équivalent
- Le dépôt contient en revanche plusieurs layouts pour l'application tierce TouchOSC (`.touchosc`), utiles pour comprendre des mappings d'usage réel mais **pas une liste de référence de grammaire**
- **Statut** : piste **non aboutie**. Le lien mentionné dans le fil forum (2019) semble caduc — soit le fichier a été supprimé/déplacé depuis, soit il n'a jamais été committé dans la branche principale accessible aujourd'hui.
- **Autres dépôts ETCLabs identifiés en passant, potentiellement utiles pour plus tard** : `OSCRouter` (routage de paquets OSC/UDP, pourrait intéresser l'architecture de transport de ton outil), `sACN` (implémentation ANSI E1.31, hors périmètre macro mais pertinent si le projet s'étend un jour au DMX direct)

## Discipline méthodologique à noter pour la suite

Ce constat d'échec est volontairement documenté plutôt que passé sous silence, conformément à l'engagement de vigilance de Cy ("dire je ne sais pas plutôt qu'extrapoler"). Toutes les pistes ne mènent pas à une découverte exploitable — c'est une information utile en soi pour ne pas revenir sur cette voie sans raison nouvelle.

---

## Synthèse de cette vague

1. Correction de confiance sur l'écosystème ETCLabs — à traiter comme C/B, jamais A
2. Piste PDF "Eos OSC Keys" non aboutie — abandonnée pour l'instant, faute de fichier retrouvable
3. Deux dépôts annexes repérés (OSCRouter, sACN) — hors périmètre immédiat, notés pour référence future

<!-- ===== FIN : vague18_correction_etclabs.md ===== -->

---

<!-- ===== DEBUT : vague19_midi_show_control.md ===== -->

# Corpus — vague 19 : MIDI Show Control (approfondissement)

Date de collecte : 29/07/2026

---

## 102 — Commandes MSC supportées par Eos, confirmées officiellement (source A)

- Source : etcconnect.com/WebDocs, page "System > Show Control" (manuel v3.3.6) + article support dédié
- <cite reformulé>Quand Eos reçoit une commande depuis une source MIDI, il reconnaît et prend en charge : Go (exécute une cue), Stop (met en pause une cue), Resume (reprend une cue en pause), Set (contrôle un submaster, un playback, ou le grandmaster), Fire (exécute une macro).</cite>
- **Confiance** : A
- **Précisions officielles complémentaires (source A, manuel v3.3.6)** :
  - <cite>Le réglage "envoi MSC" est désactivé par défaut ; une fois activé, la console peut envoyer des messages MSC pour les actions effectuées dessus, comme les actions de cue, le déclenchement de macros, et les bumps de submaster.</cite>
  - <cite>Les commandes MSC peuvent être envoyées à l'ID 127, l'ID de périphérique "All Call" ; bien qu'Eos ne puisse pas être réglé sur l'ID 127 lui-même, il répond aux commandes envoyées à cet ID.</cite>
- **Thématique** : Show Control — MIDI, complète significativement cette catégorie

## 103 — Nature technique du protocole MSC : SysEx hexadécimal (source A, article support dédié)

- Source : support.etcconnect.com, "Understanding the MSC Commands Eos Family Receives and Transmits"
- <cite reformulé>Les commandes MSC qu'Eos peut recevoir ou envoyer sont très spécifiques et préprogrammées dans le logiciel. L'information littérale est transmise via un langage particulier appelé "chaîne hexadécimale". MIDI Show Control est un sous-ensemble du standard MIDI connu sous le nom de "SysEx" (System Exclusive), généralement représenté en format hexadécimal.</cite>
- <cite reformulé>La plupart du temps, les utilisateurs interagissent avec un logiciel intermédiaire qui traduit une information simple, comme "Go Cue#" ou "Macro#", vers cette chaîne hexadécimale.</cite>
- **Confiance** : A
- **Impact architecture** : confirme que le niveau d'abstraction pertinent pour ton outil est bien "Go Cue#" / "Macro#" (haut niveau, déjà celui de toute la grammaire collectée jusqu'ici), pas le hex SysEx bas niveau — rassurant pour la cohérence de l'approche retenue depuis le début, MSC n'introduit pas de nouvelle couche de complexité à gérer directement dans le traducteur si l'outil reste au niveau OSC/commande plutôt que MIDI brut

## 104 — QLab via OSC : alternative moderne à MSC, article officiel dédié identifié mais fil communautaire obsolète signalé comme tel

- **Fil source** : "A guide to triggering Qlab cues from Eos over OSC" — **fil verrouillé par un modérateur avec la mention explicite que son contenu est obsolète**, renvoi vers un article support à jour : "Triggering QLab from Eos using OSC"
- <cite reformulé>Depuis la version 2.3, il est possible de déclencher des cues QLab via OSC. OSC fonctionne comme MIDI Show Control mais en mieux, sur des protocoles réseau modernes comme TCP ou UDP — plus besoin de matériel MIDI, juste une connexion réseau entre l'ordinateur QLab et le réseau lumière Eos.</cite>
- **Détail technique confirmé** : Eos et QLab utilisent des adresses OSC légèrement différentes (`/eos/out/event/cue/1/2/fire` côté Eos vs `/cue/2/start` côté QLab attendu), nécessitant un routeur de conversion (OSCRouter, déjà repéré en vague 18 comme dépôt ETCLabs)
- **Confiance** : A pour le principe général (renvoi vers article support explicitement à jour), C pour les détails d'implémentation (fil verrouillé, donc non vérifié à la source primaire dans cette vague)
- **Statut** : **article support "Triggering QLab from Eos using OSC" non encore consulté directement** — bonne cible pour une prochaine vague si le sujet redevient pertinent
- **Thématique** : Show Control — interopérabilité, nouvelle sous-thématique

## 105 — Piège classique de MIDI confirmé par plusieurs contributeurs : mauvais mode MIDI (C, bonne pratique de diagnostic)

- **Fils sources** : "Using MIDI with Element", "Show Cue System"
- <cite reformulé>MIDI recouvre une vingtaine de "saveurs" différentes ; pour ce type d'usage (avancer des cues depuis un ordinateur), il faut s'assurer d'utiliser spécifiquement MSC (MIDI Show Control), et vérifier que la réception MSC est bien activée dans les réglages Show Settings de la console.</cite>
- **Confiance** : C, mais recoupé par plusieurs fils indépendants avec la même cause de dysfonctionnement
- **Piège complémentaire signalé** : mauvais port/connecteur MIDI physique branché, erreur fréquente selon un contributeur expérimenté
- **Thématique** : Show Control, diagnostic pratique — pertinent si ton outil doit un jour intégrer une checklist de dépannage pour les utilisateurs non-experts

---

## Synthèse — apports de cette vague

1. **Confirmation officielle A de la liste complète des commandes MSC** reconnues par Eos : Go, Stop, Resume, Set, Fire — clôt la question ouverte depuis le début sur cette thématique
2. **Confirmation rassurante pour l'architecture** : le niveau hexadécimal SysEx reste caché derrière une couche d'abstraction "Go Cue#"/"Macro#" — cohérent avec le niveau d'abstraction déjà retenu pour tout le projet
3. **Piste OSC/QLab identifiée mais non approfondie** — pertinent si le périmètre du projet s'étend un jour à l'interopérabilité avec d'autres logiciels de spectacle, actuellement hors scope (le projet vise EOS spécifiquement)
4. Thématique Show Control désormais bien couverte : Learn/timecode (vague 8), analogique/contacts secs (vague 11), et maintenant MIDI/MSC — reste OSC show-control détaillé déjà couvert en tout début de projet (dictionnaire OSC officiel)

<!-- ===== FIN : vague19_midi_show_control.md ===== -->

---

<!-- ===== DEBUT : vague20_send_string_bugs_officiels.md ===== -->

# Corpus — vague 20 : Send_String, bug officiel ETC avec ticket de suivi

Date de collecte : 29/07/2026

---

## 106 — BUG OFFICIELLEMENT ENREGISTRÉ PAR ETC : Send_String ajoute un retour chariot parasite en macro multi-lignes (B/A, ticket de suivi confirmé)

- **Fil source** : "Send String includes /r when used in a multi-line macro"
- **Symptôme confirmé** : quand un `[Enter]` suit une commande `Send_String` dans une macro, la sortie OSC inclut un caractère `/r` parasite — problématique car ce caractère devient une partie non désirée de l'adresse OSC envoyée, cassant l'intégration avec des logiciels tiers
- **RÈGLE DE CONTOURNEMENT CONFIRMÉE, à retenir absolument** : <cite reformulé>`Send_String` doit toujours être la toute dernière commande d'une macro multi-lignes.</cite>
- **Suivi officiel confirmé** : un intervenant du forum (rôle technique identifiable) indique avoir créé le ticket **[EOS-55864]** "Macro Send String includes /r when part of a multi-line macro" pour suivre la correction. Un second message, plus récent dans le fil, confirme que le bug est **toujours présent dans la version courante au moment du post**, et signale qu'il affecte aussi les objets Magic Sheet de type Command utilisant une chaîne OSC sans argument.
- **Confiance** : **B/A** — ticket de suivi ETC nommé et confirmé, c'est aussi proche d'une source officielle qu'un fil communautaire peut l'être
- **Statut** : bug confirmé actif au moment de la dernière observation dans le fil (2022+), statut actuel (2026) non revérifié séparément — **à vérifier lors du premier accès console**, mais la règle de contournement (Send_String en dernière position) doit être appliquée par défaut par ton moteur de génération, qu'elle soit encore nécessaire ou non
- **Impact architecture majeur** : **règle de génération non négociable pour le moteur OSC/macro** — toute macro générée par ton traducteur contenant `Send_String` doit systématiquement placer cette commande en toute dernière position de la séquence.

## 107 — Second bug confirmé et documenté : Send_String multiples fusionnés en un seul paquet UDP en contexte Client (B, ticket confirmé, cause identifiée)

- **Fil source** : "Send Multiple UDP Strings"
- **Symptôme initial rapporté** : une macro contenant deux commandes `Send_String` successives n'envoie que le contenu de la première, la seconde semblant ignorée
- **Ticket de suivi confirmé** : **[EOS-53576]**, avec sortie brute observée montrant les deux chaînes concaténées en un seul paquet UDP malformé : `pst act ShoHseFL, Global, 0 Send_Stringgrp tog WhitesMS, Global, 0`
- **Cause identifiée précisément par un contributeur technique, après investigation approfondie avec Wireshark** : <cite reformulé>en test direct sur la console Primary, les deux messages partent bien séparément (visible en Tab 99 Diagnostics et confirmé par capture réseau, ~0.025 seconde d'écart). Le problème n'apparaît que lorsque la macro est déclenchée depuis un Client plutôt que directement sur la console Primary.</cite>
- **Contournement suggéré** : ajouter un `Macro_Wait` (valeur suggérée : 0.1, voire 0.01) entre les deux commandes `Send_String` pour laisser le temps aux paquets de partir séparément
- **Confiance** : B, diagnostic technique rigoureux avec preuve réseau (Wireshark), ticket nommé
- **Statut** : confirmé sur v2.9.2.8 et v3.1.2.20 par le même contributeur — bug de longue date, pas une régression récente
- **Impact architecture** : **second cas de fragilité confirmé spécifiquement lié au contexte Client vs Primary** (fait écho au facteur Foreground/Background déjà bien documenté, mais ici c'est un troisième facteur de risque contextuel distinct : la topologie multiconsole elle-même). Règle de génération à ajouter : si une macro contient plusieurs `Send_String` consécutifs et pourrait être déclenchée depuis un Client, insérer un `Macro_Wait` de sécurité entre chacun.

## 108 — Syntaxe complète et confirmée de Send_String (C, avec exemple détaillé issu d'un blog technique tiers de qualité)

- Source : blog.etcconnect.com (blog officiel ETC, mais l'article lui-même est de la plume d'un tiers expert — à traiter comme B, pas A pur)
- **Syntaxe confirmée** :
```
Send_String /cue/1/start=1,3.142,"a string with spaces"
```
- **Fonction déclarée** : transmet un message OSC au format adresse=arguments séparés par virgules, les arguments texte devant être entre guillemets s'ils contiennent des espaces
- **Confiance** : B
- **Avantage de l'usage en macro (plutôt qu'en commande directe de cue) confirmé** : <cite reformulé>une macro peut servir de référence unique dans tout le showfile — reliée à une cue, ciblée depuis un objet Magic Sheet, ou déclenchée depuis un fader. Si par exemple la première cue QLab du show n'est plus la cue 1 mais devient 0.5, il suffit de mettre à jour la macro pour que le changement se répercute partout dans le showfile.</cite>
- **Impact** : confirme et illustre concrètement, avec un cas d'usage réel, l'intérêt de l'indirection déjà identifiée comme stratégie de génération en masse (vague 2 #020, vague 10 #070 confirmé A) — ici appliquée à une problématique différente (maintenance de synchronisation cross-logiciel) mais avec la même logique de fond

## 109 — Limite confirmée : pas de préfixe `local:` disponible en macro pour de l'auto-adressage OSC (C, workaround documenté)

- **Fil source** : "Self Targeting Osc from local Macro"
- **Besoin exprimé** : depuis une macro, déclencher une commande qui normalement nécessite un envoi OSC vers soi-même (la console cible ses propres entrées OSC) — l'auteur cite l'exemple du bouton Stop/Back du playback principal, `Send_String /eos/key/stop=1`
- <cite reformulé>Le préfixe `local:` existe pour les objets Magic Sheet mais ne semble pas fonctionner depuis une macro.</cite>
- **Contournement rapporté par l'auteur lui-même** : router le TX UDP directement vers le RX OSC de la même console, au prix d'un trafic réseau superflu qu'il aimerait éviter
- **RÉSOLUTION APPORTÉE PAR UN AUTRE CONTRIBUTEUR, syntaxe directe et simple** : <cite reformulé>il existe une commande native `Go_0`, trouvable dans le champ de recherche de l'éditeur de macro, qui fait exactement cela sans détour OSC.</cite>
- **Confiance** : C pour le problème, mais la solution `Go_0` est directement vérifiable et cohérente avec la liste de recherche déjà en partie capturée (vague 12) — même si `Go_0` lui-même n'apparaissait pas dans la portion F→M déjà transcrite
- **Impact** : **confirmation supplémentaire, très concrète, que la liste de recherche de l'éditeur contient des solutions directes à des besoins que la communauté résout parfois de façon détournée** — renforce encore la priorité, déjà notée, de capturer cette liste dans son intégralité si l'occasion se présente

## 110 — Bug USB OSC distinct (lighthack/#lighthack), Send_String limité au réseau (C, non résolu dans le fil, périphérique au projet)

- **Fil source** : "Eos Macro Send_String function not working with USB OSC"
- <cite reformulé>Les messages générés par Send_String ne sortent que sous forme de paquets OSC UDP réseau — rien n'est envoyé via la route USB OSC vers un périphérique comme un Arduino.</cite>
- **Explication technique avancée par un contributeur** : <cite reformulé>Send_String semble par défaut toujours transmis en UDP vers l'adresse IP configurée dans les réglages de transmission OSC (osctxip) ; l'OSC sur USB est une fonctionnalité relativement récente et l'initiation de commandes depuis la console vers ce canal ne semble pas avoir été traitée. Le périphérique USB reçoit les événements auxquels il est abonné et tout ce qui répond aux transmissions du périphérique, mais pas les envois initiés côté console.</cite>
- **Confiance** : C, non résolu explicitement comme un vrai bug confirmé par ETC dans cet extrait (contexte #lighthack = programme communautaire de hacking matériel autour d'EOS, hors périmètre直接 de ton projet actuel)
- **Statut** : périphérique, à ne pas prioriser — pertinent seulement si ton architecture évolue un jour vers du matériel USB direct plutôt que réseau OSC pur

---

## Synthèse — apports de cette vague (très riche en règles de génération directement actionnables)

1. **Deux bugs officiellement suivis par ETC (tickets nommés)** — la vague la plus solide en termes de confirmation officielle depuis le début du corpus, hors documentation pure
2. **Deux règles de génération non négociables à intégrer dans le moteur** :
   - `Send_String` toujours en dernière position d'une macro multi-lignes
   - `Macro_Wait` de sécurité entre plusieurs `Send_String` consécutifs si déclenchement possible depuis un Client
3. **Nouvelle commande utile découverte** : `Go_0` — équivalent direct du Stop/Back du playback principal, sans détour OSC
4. **Confirmation supplémentaire de l'intérêt de l'indirection macro** pour la maintenabilité cross-logiciel (QLab)

## Mise à jour du référentiel de risques

Ajouter :
- `Send_String` suivi d'un `[Enter]` en macro multi-lignes → génère un `/r` parasite dans l'adresse OSC (bug ETC-55864, B/A) — règle : toujours en dernière position
- `Send_String` multiples consécutifs déclenchés depuis un Client (pas Primary) → risque de fusion en un seul paquet UDP malformé (bug ETC-53576, B) — règle : `Macro_Wait` entre chaque

<!-- ===== FIN : vague20_send_string_bugs_officiels.md ===== -->

---

<!-- ===== DEBUT : vague21_affichage_flexi_snapshots.md ===== -->

# Corpus — vague 21 : Affichage, Flexi, Snapshots (approfondissement)

Date de collecte : 29/07/2026

---

## 111 — Piège confirmé et contournement officieux : "Encoder Display" non capturable en macro (C, solution de contournement fonctionnelle)

- **Fil source** : "Encoder Display macro"
- **Symptôme** : naviguer vers une page d'encodeur spécifique (ex: "Shutter Page 2/2") ne génère aucune syntaxe capturable dans l'éditeur de macro
- **Contournement confirmé par un contributeur expérimenté** : <cite reformulé>enregistrer un Snapshot qui n'inclut que les encodeurs, puis appeler ce Snapshot depuis une macro. Technique utilisée fréquemment avant l'introduction des Flexi encoders, et aussi en travaillant avec des serveurs média — dans ce cas, ajouter `[Select Last]` dans la macro après le déclenchement du Snapshot.</cite>
- **Confiance** : C, mais méthode confirmée comme éprouvée dans le temps par son auteur
- **Impact architecture** : **nouveau motif de contournement générique à retenir** — quand une action d'affichage/interface n'est pas directement capturable en macro (comme déjà vu pour `More_SoftKeys`/`Open_Browser` en vague 4, et pour la navigation Encoder ici), le Snapshot peut servir de pont. Ce motif ("Snapshot + Select Last comme substitut à une commande non macro-capturable") mérite d'être ajouté comme stratégie de repli générale dans le référentiel, pas seulement documenté au cas par cas.

## 112 — Confirmation, par un second témoignage indépendant, que les macros contournent d'elles-mêmes le problème de changement d'onglet (C, rassurant)

- **Fil source** : "Macro syntax help" (déjà en corpus, vague 14 #084)
- **Nouvelle information tirée du même fil, non exploitée en vague 14** : après que l'utilisateur ait passé 45 minutes à essayer de comprendre comment forcer un changement d'onglet (vers la vue IP/Intensity Palette) depuis une macro, un contributeur répond : <cite reformulé>il n'est pas nécessaire d'y penser explicitement — il suffit d'enregistrer la macro normalement, et le changement d'onglet nécessaire y sera inclus automatiquement.</cite>
- **Confiance** : C
- **Impact** : ceci **nuance positivement** l'inquiétude soulevée par le témoignage plus large déjà noté en #084 — certains aspects de navigation d'affichage, bien que non évidents à construire depuis l'éditeur à froid, se capturent correctement via Learn. Cohérent avec la doctrine déjà bien établie "Learn d'abord" — encore un cas qui la confirme.

## 113 — Confirmation officielle du terminateur de chaîne en Show Control String Input (source A, complète #076)

- Source : supplément manuel v2.5.0/v2.6.x
- <cite reformulé>Pour une entrée de type String Input (incluant OSC et chaînes ASCII/UDP), l'appareil émetteur doit ajouter "SC" (sensible à la casse) au début de la chaîne. La chaîne doit être terminée par un retour chariot (hex 0D), \r, ou #.</cite>
- **Confiance** : A
- **Impact** : précise et complète l'information déjà notée en vague 11 (#076, retour chariot systématique en sortie Eos) — ici côté réception (String Input), avec la précision supplémentaire du préfixe `SC` obligatoire et des trois terminateurs acceptés (hex 0D, `\r`, ou `#`). Cohérent avec le terminateur `#` déjà vu dans la syntaxe `/eos/cmd="Chan 1 At 75#"` du dictionnaire OSC officiel consulté en tout début de projet.

## 114 — Confirmation officielle : contrôle du contenu d'un Snapshot affiné en v2.6 (source A)

- Même supplément manuel
- <cite reformulé>Depuis la version 2.6, un contrôle plus fin est disponible sur ce qui est inclus dans un Snapshot. Lors de l'enregistrement, un aperçu de tous les displays tels qu'ils seront enregistrés est visible, avec possibilité de sélectionner/désélectionner divers composants, moniteurs, cadres, etc.</cite>
- **Confiance** : A
- **Impact direct sur #111** : ceci confirme et enrichit la faisabilité technique du motif "Snapshot encodeurs uniquement" décrit plus haut — la sélectivité fine du contenu de Snapshot est une fonctionnalité officiellement documentée, pas une astuce fragile

## 115 — Confirmation officielle : {Flexi}/{Select}/{Expand} comme famille de softkeys d'affichage cohérente (source A)

- Même supplément manuel
- <cite>Use Select affiche le bouton {Select}. Use Flexi affiche le bouton {Flexi}. Use Expand affiche le bouton {Expand}. Use Arrows affiche les flèches de pagination haut/bas.</cite>
- **Confiance** : A
- **Thématique** : Affichage/interface — précise le fonctionnement de configuration de ces boutons, cohérent avec les mentions déjà éparses de `{Flexi}` (vague grammaire initiale, `{View Chans}`) et `[Select]` (vague 10, sortie d'édition de macro)

## 116 — Recommandation officielle pour les templates de showfile : snapshots organisés par Flexi state usuel (B, blog ETC, bonne pratique)

- Source : blog.etcconnect.com, "Eos Template Show File Creation: Settings and Snapshots"
- <cite reformulé>Il est recommandé de préparer des snapshots avec les displays de channels dans le format et l'état Flexi le plus utilisé — par exemple format résumé avec Flexi Active, et/ou format tableau avec Flexi Patched.</cite>
- **Confiance** : B (article officiel du blog ETC, signé par un auteur identifié, bonne pratique plutôt que fait technique strict)
- **Impact** : renforce indirectement la pertinence du motif Snapshot pour ton outil — si ETC recommande officiellement de préparer des snapshots comme brique de base réutilisable de showfile, ça légitime encore davantage l'usage de ce mécanisme comme solution générique de contournement pour l'affichage en macro (#111)

---

## Synthèse — apports de cette vague

1. **Nouveau motif de contournement générique identifié et à formaliser** : Snapshot + `[Select Last]` comme pont pour toute action d'affichage non capturable directement en macro — à ajouter comme stratégie standard dans le référentiel, au même titre que les trois stratégies de génération en masse déjà identifiées
2. **Précision officielle sur le terminateur de String Input Show Control** (`SC` en préfixe, `\r`/hex 0D/`#` en terminateur) — complète le protocole bas niveau déjà entamé en vague 11
3. **Confirmation supplémentaire, redondante, de la doctrine "Learn d'abord"** — le changement d'onglet s'auto-résout en Learn, cohérent avec tout ce qui a été établi jusqu'ici sur ce point

## Mise à jour à faire dans le référentiel

Ajouter aux stratégies de contournement génériques (à côté des 3 stratégies de génération en masse déjà listées en vague 7) :
- **Snapshot + `[Select Last]`** comme pont pour toute action d'affichage/interface non capturable directement en macro (encodeurs, pages spécifiques, etc.)

<!-- ===== FIN : vague21_affichage_flexi_snapshots.md ===== -->

---

<!-- ===== DEBUT : vague22_mark_automark.md ===== -->

# Corpus — vague 22 : Mark / AutoMark (approfondissement)

Date de collecte : 29/07/2026

---

## 117 — Mécanique complète d'AutoMark, confirmée en détail (C, réponse très complète et pédagogique d'un contributeur expérimenté)

- **Fil source** : "Auto Mark"
- **Principe confirmé** : <cite reformulé>quand une cue fait passer l'intensité d'un projecteur de zéro/éteint vers un niveau actif, et qu'il y a en même temps une transition de paramètre non-intensité (couleur, position...), la console exécute ce mouvement non-intensité dans la cue immédiatement précédente. Si la cue précédente contient elle-même une extinction vers zéro pour ces mêmes channels, la console attend que les lumières atteignent zéro avant de déplacer focus/couleur/gobo.</cite>
- **Indicateur visuel confirmé** : un "M" apparaît dans le champ flags de la cue list pour toute cue dont les mouvements seront effectivement exécutés en avance dans la cue précédente
- **Mécanisme de désactivation ponctuelle confirmé** : `[Cue]` ou `[Record]` avec AutoMark activé fait apparaître "S6 = Automark Off" — sélectionner cette option désactive l'auto-mark pour cette cue/part précise, indiqué par un "D" dans les flags
- **Confiance** : C, mais cohérence totale avec la doc et usage détaillé pédagogique
- **Syntaxe directe confirmée pour un mark avec décimale** : `[Mark] [6] [.] [9] [9] [Enter]` déclenche un prompt "Create Mark Cue?" ; valider crée automatiquement la cue 6.99 et y effectue le marking, évitant de passer par Blind manuellement

## 118 — BUG CONFIRMÉ ET NON RÉSOLU : {Enable}/{Disable} pour le marking ne fonctionne pas comme prévu en macro (C, contredit directement la doctrine officielle déjà en corpus)

- **Fil source** : "Marking"
- **Question posée dans le fil** : <cite reformulé>est-il possible d'utiliser l'option enable/disable dans les macros pour le marking ? Je n'arrive pas à le faire fonctionner.</cite>
- **Réponse d'un autre contributeur, non résolutive** : <cite reformulé>ça continue à se comporter comme un toggle, ou du moins c'est le cas sur l'OLE (Offline Editor).</cite>
- **Confiance** : C, mais **contrediction directe et documentée** avec la règle officielle déjà établie niveau A (vague 10, #074 : *"les macros pour des options à bascule... peuvent utiliser les softkeys {Enable} et {Disable} pour créer des actions absolues plutôt que des toggles"*)
- **Statut** : ni confirmé ni infirmé de façon définitive dans ce fil — semble être un cas spécifique où la règle générale documentée par ETC ne s'applique pas comme attendu, au moins pour le marking et au moins en Offline Editor
- **Impact architecture majeur** : ceci est la **preuve la plus directe et la plus nette, à ce stade du corpus, que la règle générale "utiliser {Enable}/{Disable} pour éviter le comportement toggle" n'est pas fiable à 100% selon le contexte fonctionnel visé** (ici : marking spécifiquement). Le référentiel de risques traitait déjà `{Enable}/{Disable}` comme risque contextuel générique — cette entrée **confirme concrètement** ce risque avec un cas d'usage précis et documenté, plutôt que par simple prudence théorique. À signaler comme prioritaire pour un test au banc, avec un scénario précis reproductible (macro de bascule d'AutoMark).

## 119 — Piège de construction de macro pour Mark en cue part : contexte Live vs Blind déterminant (C, syntaxe fine confirmée)

- **Fil source** : "Mark Macro"
- **Contexte du besoin** : créer une macro pour marquer dans un cue part 20 spécifique
- **Explication technique confirmée** : <cite reformulé>il faut d'abord qu'un part 20 existe pour qu'une instruction y faisant référence fonctionne. Si ce part 20 est enregistré en Live, il n'inclura pas que les marks — il embarquera aussi une forme de données de cue additionnelles. Si ce part est ajouté en Blind, ce problème ne se produit pas.</cite>
- **Conséquence pratique pour la macro** : <cite reformulé>la macro proposée par l'auteur du fil devrait fonctionner correctement si elle est exécutée en Blind. On peut aussi ajouter des commandes dans la macro pour basculer en Blind puis revenir en Live — mais l'entrée en Blind depuis une macro doit être plus spécifique qu'un simple `[Blind] [Enter]` : dans ce cas précis, il faut `[Blind] [Cue] [Enter]`, alors que dans d'autres contextes ce serait `[Blind] [Sub] [Enter]`.</cite>
- **Confiance** : C, réponse technique précise et cohérente
- **Impact architecture** : **nouveau piège de syntaxe contextuelle** : `[Blind] [Enter]` seul est ambigu/insuffisant en macro, il faut préciser la cible (`Cue`, `Sub`, etc.) explicitement. Règle de génération à intégrer : le moteur ne doit jamais générer un `[Blind] [Enter]` nu, toujours qualifié par son objet cible.

## 120 — Confirmation officielle A du mécanisme de Referenced Mark (structurel, complète la compréhension du domaine)

- Source : etcconnect.com/WebDocs, "Referenced Marks"
- <cite>Si la programmation démarre avec AutoMark activé puis que la fonctionnalité est désactivée, tous les AutoMarks du show sont convertis en marks référencés.</cite>
- <cite>Un mark référencé réussi comporte deux parties : la cue portant le flag de mark (définie par l'utilisateur) — appelée cue marquée — où les paramètres non-intensité changeront ; et la cue portant la valeur d'intensité pour les channels concernés — appelée cue source — qui est aussi celle où sont stockés les mouvements non-intensité. Pour utiliser le mark correctement, il faut spécifier les channels à marquer dans la cue source ; Eos ne suppose pas que tous les fixtures automatisés s'appliquent à un mark donné.</cite>
- **Confiance** : A
- **Thématique** : Mark/Auto-Mark — clarifie enfin structurellement ce domaine resté flou depuis les mentions éparses en vague 11 (#078, indicateurs mh/MH/ml/ML)

## 121 — Confirmation d'une limitation connue et assumée par ETC sur les cues multi-parts et le marking (B, réponse ETC directe)

- **Fil source** : "Marking"
- <cite reformulé>Un contributeur identifié comme faisant partie de l'équipe ETC confirme que le problème de marking sur cues multi-parts (où le marking semble attendre la fin de toute la cue plutôt que de démarrer dès que le channel concerné atteint zéro) est un comportement connu, actuellement sur la liste des points à corriger côté ETC.</cite>
- **Confiance** : B
- **Statut** : limitation reconnue par ETC — statut de correction actuel non vérifié séparément dans cette vague

---

## Synthèse — apports de cette vague (importante pour la robustesse du référentiel)

1. **Confirmation concrète et documentée du risque déjà identifié sur `{Enable}/{Disable}`** (#118) — passe de risque générique théorique à cas précis reproductible (marking), renforçant la priorité de test au banc sur ce point
2. **Nouveau piège de syntaxe contextuelle découvert** : `[Blind] [Enter]` doit toujours être qualifié par son objet cible en macro — règle de génération à intégrer immédiatement
3. **Mécanique AutoMark/Mark/Referenced Mark désormais bien comprise structurellement**, avec confirmation A pour les Referenced Marks

## Mise à jour du référentiel de risques

Ajouter :
- `{Enable}/{Disable}` pour le marking spécifiquement → confirmé comme se comportant encore comme un toggle en macro, malgré la doctrine générale officielle contraire (C, contredit #074, vague22 #118) — **cas prioritaire de test au banc**
- `[Blind] [Enter]` non qualifié → syntaxe ambiguë/insuffisante en macro, doit toujours préciser l'objet cible (`Cue`, `Sub`, etc.) (C, vague22 #119)

<!-- ===== FIN : vague22_mark_automark.md ===== -->

---

<!-- ===== DEBUT : vague23_merge_selectif_constat.md ===== -->

# Corpus — vague 23 : Merge sélectif (rendement faible sur multiconsole/backup ce tour-ci)

Date de collecte : 29/07/2026

---

## 122 — Merge sélectif par type d'objet, confirmé officiellement (source A, procédure claire)

- Source : support.etcconnect.com, "Merging custom fixture profiles into an Eos showfile"
- **Procédure confirmée** : <cite reformulé>charger le showfile source contenant l'objet à fusionner sur une clé USB formatée en FAT32, l'insérer dans la console, puis dans le File Browser naviguer vers File > Merge > [clé USB] > [showfile source]. Un écran de sélection apparaît ; il faut s'assurer que seule la catégorie voulue (ex: "Fixtures") est cochée avant de valider.</cite>
- **Confiance** : A
- **Impact** : confirme et précise le mécanisme de Merge sélectif déjà évoqué en creux depuis la vague 5 (pattern dummy channels/palettes réutilisables entre showfiles) — ici avec la procédure exacte et officielle. Directement pertinent pour ta problématique de réutilisabilité inter-tournées : ton outil pourrait générer des showfiles "modèles" contenant uniquement des macros, à fusionner sélectivement (catégorie "Macros" plutôt que tout le show) dans le showfile de chaque date de tournée.

## 123 — Confirmation indirecte, via anecdote d'un tiers, que Change To et Merge sont utilisés en pratique pour l'harmonisation de patch entre venues (D, source non fiable en tant que telle mais usage confirmé cohérent)

- **Fil source** : "My NOMAD ---> Other NOMAD" (déjà partiellement en corpus, vague 3 #026, relu sous un angle différent ici)
- **Contexte particulier de cette source** : l'utilisateur du forum partage littéralement une réponse générée par un assistant IA générique (nommé dans le fil), en demandant l'avis de la communauté dessus — <cite reformulé>"voici ce que Gemini me suggère... mais je prends ça avec des pincettes."</cite>
- **Confiance** : **D — cette portion spécifique du fil n'est PAS une source humaine vérifiée**, c'est du contenu généré par un autre outil IA, partagé pour avis. À ne jamais traiter comme donnée de grammaire fiable en soi.
- **Ce qui reste exploitable malgré tout** : la fonction `Change To` elle-même (déjà confirmée ailleurs, vague 3 #026, comme `Channel Change To`) est correctement décrite dans ce contenu généré, de façon cohérente avec le reste du corpus — mais ce n'est pas une confirmation supplémentaire indépendante, juste une reformulation non vérifiée d'un fait déjà établi par ailleurs
- **Note méthodologique importante** : cette source illustre un risque réel pour la collecte — du contenu IA généré peut se retrouver posté sur des forums techniques par des utilisateurs de bonne foi cherchant une validation. Vigilance à maintenir : toujours vérifier si un extrait de forum est un témoignage humain direct ou une reproduction de sortie IA, avant de lui accorder un niveau de confiance C.

## 124 — Constat d'échec partiel de cette vague sur la thématique visée

- La recherche ciblée sur "backup console failover sync macro" n'a pas produit de résultat solide spécifiquement pour **Eos** — le résultat le plus détaillé concernait un bug de sauvegarde sur console **Hog** (marque concurrente, hors périmètre du corpus)
- **Statut** : la thématique "multiconsole/backup" reste incomplète au-delà de ce qui était déjà établi en vague 9 (ciblage User OSC, bug d'édition concurrente) — pas de nouvelle donnée solide sur la mécanique de failover Primary/Backup elle-même pour Eos
- **Action suggérée pour une prochaine vague** : reformuler la recherche avec des termes plus spécifiques à Eos (ex: "Eos Backup console troubleshoot reconnect", déjà partiellement vu en vague 9 avec le fil "Issues with Multiconsole", jamais approfondi)

---

## Synthèse — apports de cette vague

1. **Procédure Merge sélective confirmée officiellement (A)** — actionnable directement pour la stratégie de distribution multi-tournée de ton outil
2. **Alerte méthodologique importante** : détection d'une source de forum contenant en réalité du contenu généré par IA, partagé pour avis — renforce la nécessité de rester vigilant sur la nature exacte de chaque source avant de lui attribuer une confiance C
3. **Échec honnête signalé** sur la thématique failover/backup Eos spécifiquement — pas de nouvelle donnée exploitable, à retenter avec des termes différents plus tard

<!-- ===== FIN : vague23_merge_selectif_constat.md ===== -->

---

<!-- ===== DEBUT : vague24_fan_autopalette_precedent.md ===== -->

# Corpus — vague 24 : Fan mode, Break Nested, et un précédent direct au projet (Autopalette)

Date de collecte : 29/07/2026

---

## 125 — Découverte du mode Fan, mécanisme de répartition automatique de valeurs (source A, nouveau concept)

- Source : Eos Family L3 Intermediate Workbook v3.1 (officiel ETC)
- <cite reformulé>Fan est un mode du logiciel Eos. Une fois activé, tout paramètre déplacé se répartit uniformément sur la sélection courante, selon différents styles. Il est possible de répartir ("fan") des données référencées sur une plage de channels, et les plages peuvent aussi être utilisées pour répartir des temps et délais discrets.</cite>
- **Confiance** : A
- **Impact architecture majeur** : c'est un **quatrième mécanisme de génération en masse natif d'EOS**, distinct des trois déjà identifiés (spread par plage `[Thru]`/`[Thru]`, boucle `SelectLast`/`Macro_Loop`, indirection macro-dans-macro). Fan semble être le mécanisme le plus proche d'une vraie fonction mathématique de distribution — pertinent en particulier pour tout scénario de gradient (déjà vu avec le spread de teintes en vague 5 #040, qui aurait peut-être pu s'exprimer plus simplement via Fan). **À investiguer en priorité dans une prochaine vague** — syntaxe exacte non capturée dans cet extrait, seulement le principe.

## 126 — Précisions officielles sur Break Nested et Make Absolute lors d'un Update (source A, complète #041/#042)

- **Fil source** : "Palettes" (2009, mais principe stable)
- <cite reformulé>Lors d'un Update, la CIA affiche des informations sur la cue en cours de mise à jour ainsi que les channels concernés. Si des palettes/presets sont listés, "Update All" permet de mettre à jour les palettes de intensité/focus/couleur/beam de ces lumières. "Make Absolute" code l'information en donnée figée directement dans la cue. "Break Nested" est censé "casser le lien" palette-preset.</cite>
- **Confiance** : C pour cette formulation (utilisateur expérimenté, pas ETC direct dans ce fil), mais cohérente et confirmée en creux par les mentions déjà en corpus (#042, "make absolute" mentionné sans détail)
- **Piège rapporté par l'auteur, non résolu explicitement** : le réglage Make Absolute/Break Nested/Update All est **persistant d'une session à l'autre** — la console se souvient du dernier choix effectué et le réapplique par défaut au prochain Update, ce qui peut piéger un opérateur qui a oublié son dernier réglage
- **Impact** : nouveau cas à ajouter au référentiel — un `Update` peut se comporter différemment non seulement selon le contexte immédiat (déjà documenté, #025), mais aussi selon un **état persistant de préférence utilisateur** non visible dans la macro elle-même. Renforce encore la nécessité de traiter `Update` comme commande à haut risque contextuel.

## 127 — DÉCOUVERTE MAJEURE : un précédent direct et non abouti du projet de Cy existe déjà dans la communauté ("Autopalette Macros")

- **Fil source** : "Autopallette Macros" (2024, récent)
- **Projet décrit par l'auteur du fil, en tous points comparable à une sous-fonction de ton propre projet** : <cite reformulé>l'objectif est de sélectionner n'importe quel fixture du showfile et de faire en sorte qu'une macro construise automatiquement une palette by-type de base pour chaque paramètre, sans avoir à détailler chaque profil manuellement — inspiré d'une fonctionnalité équivalente déjà existante sur les consoles Hog (marque concurrente), qui aurait fait gagner des heures de programmation sur plusieurs shows passés.</cite>
- **État d'avancement rapporté par l'auteur lui-même** : <cite reformulé>le prototype actuel demande à l'utilisateur de sélectionner un instrument, valide, puis parcourt tous les paramètres du fixture pour les mettre à 0 ; ensuite, pour chaque paramètre de couleur, les met à 100%, met à jour une palette by-type, remet le paramètre à 0%, et recommence. Ça casse actuellement après la première palette — des erreurs de programmation restent à corriger.</cite>
- **Conseil apporté par un autre contributeur** : privilégier Hue/Saturation (disponible virtuellement dans EOS, à activer) plutôt que RGB, car tous les fixtures n'ont pas les mêmes paramètres de couleur natifs — offre à partager la syntaxe de macro pour affiner l'aide
- **Confiance** : C, témoignage direct et détaillé d'un projet en cours, non finalisé
- **Statut** : projet inachevé au moment du post (avril 2024), issue non connue dans cet extrait
- **IMPACT MAJEUR POUR TON PROJET** : cette découverte mérite une attention particulière. Un membre de la communauté ETC a entrepris, de façon indépendante et pour un besoin très proche du tien (génération automatique de palettes par un mécanisme de macro auto-itérant), un projet non abouti à ce jour. Ça confirme trois choses :
  1. **Le besoin est réel et partagé** au-delà de ton propre contexte
  2. **La difficulté est réelle aussi** — même un utilisateur avancé bute sur la fiabilité de bout en bout d'une macro auto-itérante complexe
  3. **Une piste de collecte à fort potentiel existe** : si ce fil a eu une suite (résolution, code final, abandon), la retrouver donnerait un retour d'expérience direct et très proche de ton cas d'usage — bien plus précieux qu'un exemple isolé

## Action prioritaire suggérée pour la prochaine vague

Rechercher la suite du fil "Autopallette Macros" ou tout fil connexe plus récent du même auteur, pour savoir si ce projet communautaire a abouti — ce serait le retour d'expérience le plus directement transposable trouvé à ce jour dans tout le corpus.

---

## Synthèse — apports de cette vague

1. **Nouveau mécanisme de génération en masse identifié** (Fan) — syntaxe à creuser en priorité, quatrième stratégie disponible aux côtés des trois déjà connues
2. **Nouveau facteur de risque contextuel** pour `Update` : état persistant de préférence utilisateur (Make Absolute/Break Nested), non visible dans le texte de la macro elle-même
3. **Découverte du précédent communautaire le plus proche du projet de Cy trouvé à ce jour** — piste de suivi prioritaire

## Mise à jour du référentiel de risques

Ajouter :
- `Update` — en plus de l'ambiguïté de cible déjà connue (#025), le comportement Make Absolute/Break Nested/Update All est **persistant entre sessions** et non visible dans le texte de la macro (C, vague24 #126)

## Mise à jour des stratégies de génération en masse

Ajouter comme 4e stratégie, à documenter :
- **Fan mode** — répartition automatique de valeurs sur une sélection ou une plage de channels, mécanisme natif EOS distinct des trois autres déjà listées. Syntaxe exacte non capturée, à rechercher en priorité.

<!-- ===== FIN : vague24_fan_autopalette_precedent.md ===== -->

---

<!-- ===== DEBUT : vague25_confirmation_absence_autopalette.md ===== -->

# Corpus — vague 25 : confirmation officielle de l'absence d'auto-palette native (2010, toujours pertinent)

Date de collecte : 29/07/2026

---

## 128 — CONFIRMATION OFFICIELLE ETC : pas de fonction auto-palette native, et raisons produit explicites (B/A, réponse ETC directe et argumentée)

- **Fil source** : "Auto-Pallets" (2010)
- **Réponse officielle ETC citée dans le fil (contributeur identifiable comme faisant partie d'ETC)** : <cite reformulé>il n'existe pas actuellement de fonction auto-palette dans la gamme Eos. Le sujet a été beaucoup discuté en interne — pour que ce soit un outil réellement utile, la génération des palettes et l'ordre dans lequel elles apparaissent sont des aspects que la plupart des utilisateurs veulent contrôler eux-mêmes.</cite>
- **Exemple donné par ETC pour justifier la prudence** : <cite reformulé>prendre l'exemple de la couleur — faire générer par la console 500+ palettes basées sur le nombre de correspondances de gélatine qu'un fixture peut atteindre n'est pas réellement utile. La plupart des shows utilisent une palette de couleurs spécifique, organisée avec soin par les programmeurs (ex: ordre RGBIV, ou regroupement par teintes chaudes/froides saturées/non saturées).</cite>
- **Position officielle sur l'avenir de la fonctionnalité** : <cite reformulé>une fonction auto-palette sera envisagée à l'avenir, ainsi que des données de groupement abstraites, mais ce n'est pas encore arrivé en haut de la liste des priorités.</cite>
- **Confiance** : B/A — réponse directe et argumentée d'un profil ETC identifiable, formulée comme position produit officielle
- **Statut temporel important** : réponse datée de 2010. Le fil "Autopallette Macros" de 2024 (vague 24, #127) confirme, 14 ans plus tard, qu'**aucune fonction auto-palette native n'a été ajoutée depuis** — la situation décrite en 2010 reste d'actualité, un utilisateur devant encore bricoler sa propre solution par macro en 2024.

## Impact architecture majeur — le plus important de cette vague

Cette confirmation officielle, croisée avec le témoignage indépendant de 2024, établit un fait solide et déterminant pour la valeur de ton projet :

1. **ETC a délibérément choisi de ne jamais automatiser entièrement la génération de palettes**, pour une raison de fond assumée : la personnalisation de l'organisation des palettes est jugée essentielle par la profession, et une génération purement automatique produirait un résultat jugé peu utile (trop de palettes, mal organisées)
2. **Cette position n'a pas changé en 14 ans** — ce n'est donc pas un oubli temporaire mais un choix de conception stable
3. **Pour ton outil, ça implique une nuance de conception importante** : un traducteur NL qui générerait des palettes de façon totalement automatique, sans intervention de l'utilisateur sur l'organisation/l'ordre, irait à l'encontre de ce qu'ETC elle-même a identifié comme le vrai besoin de la profession. Ton système déjà prévu de **validation avec menus déroulants avant envoi** (note produit du tout début de la conversation) est donc **aligné avec la doctrine produit officielle d'ETC**, pas juste une bonne pratique générique de ton cru — c'est exactement le type de contrôle utilisateur qu'ETC identifie comme manquant dans toute automatisation complète.

## Exemple concret donné par un second contributeur du fil de 2010 (C, illustratif)

- <cite reformulé>Idée d'auto-palette simplifiée proposée par un utilisateur : pour un parc de 8 VL3000 et 12 Mac700, générer automatiquement des groupes par type de fixture et par parité (tous VL3000, tous Mac700, VL3000 pairs, VL3000 impairs, etc.), puis pour la couleur une palette de base simple (Cyan, Magenta, Jaune, Bleu Congo, Rouge, Vert, Orange, Lavande), et pour le beam tous les gobos des deux roues en une palette.</cite>
- **Confiance** : D (idée non implémentée, proposition informelle)
- **Intérêt** : illustre concrètement à quoi pourrait ressembler un jeu de règles de génération "raisonnable" (pas 500+ palettes, mais un jeu limité et structuré) — cohérent avec l'argument officiel d'ETC sur la nécessité de limiter et structurer plutôt que tout générer

---

## Synthèse — apports de cette vague (validation stratégique majeure pour le projet)

1. **Confirmation officielle et durable (14 ans) qu'aucune solution native n'existe** pour l'auto-génération de palettes — validation de la pertinence du projet de Cy sur ce point précis
2. **La doctrine produit d'ETC elle-même valide le choix déjà fait par Cy** de prévoir une étape de validation/ajustement utilisateur après génération automatique, plutôt qu'un pipeline entièrement automatique
3. Cette vague n'apporte pas de nouvelle syntaxe technique, mais une **validation stratégique de fond** pour la direction du projet — à conserver comme argumentaire de référence

<!-- ===== FIN : vague25_confirmation_absence_autopalette.md ===== -->

---

<!-- ===== DEBUT : vague26_fan_syntaxe_confirmee.md ===== -->

# Corpus — vague 26 : Fan — syntaxe confirmée (source A)

Date de collecte : 29/07/2026

---

## 129 — DÉCOUVERTE MAJEURE : Fan n'est pas une commande séparée, c'est un comportement implicite de [Thru] (source A)

- Source : etcconnect.com/WebDocs, page "Fan From the Command Line" (manuel v3.3.5)
- <cite>Une commande de niveau ou de temps qui utilise [Thru] ou une liste de références est une commande de fan en ligne de commande. Utiliser la touche [Fan] n'est nécessaire que si un style de fan autre que celui par défaut est souhaité.</cite>
- **Confiance** : A
- **IMPACT ARCHITECTURAL MAJEUR, qui reformule complètement la vague 24** : ceci change la compréhension du mécanisme. Fan **n'est pas** une quatrième stratégie de génération en masse distincte des trois autres — **c'est le mécanisme sous-jacent qui explique pourquoi le spread par plage `[Thru] x [Thru] y` fonctionne déjà** (stratégie n°1 déjà identifiée, vague 6 #056, confirmée A). Autrement dit : chaque fois que ton traducteur génère une commande du type `[Thru]` avec une plage de valeurs de part et d'autre, il utilise déjà Fan implicitement, par défaut, sans avoir besoin d'invoquer `[Fan]` explicitement — sauf s'il faut un style de répartition non standard.
- **Correction à faire dans le référentiel** : retirer "Fan mode" comme 4e stratégie séparée, et la fusionner avec la stratégie n°1 (spread par plage), en précisant que c'est le même mécanisme sous un nom différent.

## 130 — Confirmation de la disponibilité de plusieurs "styles" de Fan, non exhaustivement listés dans cet extrait (A, incomplet)

- **Fil source complémentaire** : "Fan Instructions" (2012), confirmant et pointant vers la documentation officielle
- <cite reformulé>Quand [Fan]/{Fan} est pressé après une sélection de channels, les softkeys se repeignent pour afficher les différents styles de fan disponibles.</cite>
- **Confiance** : A pour l'existence de plusieurs styles, mais liste exacte des styles **non capturée** dans les extraits consultés — seule la page support/vidéo YouTube ETC mentionnée (v1.8 update) semble détailler la liste complète, non consultée directement dans cette vague
- **Historique de version confirmé** : Fan a été introduit avec Eos v1.8

## 131 — Confirmation A du principe général de Fan, complète #125 avec plus de détail

- Source : Eos Family L3 Advanced Workbook (déjà consulté en partie, relu ici sous cet angle)
- <cite>Dans le logiciel Eos Family, Fan est un mode. Quand il est activé, tout paramètre déplacé se répartit uniformément sur la sélection, selon le style choisi.</cite>
- Exemple illustratif du workbook (contexte pratique, non verbatim) : application de Fan sur un délai (**"delay"**), avec un exemple explicite où les channels de rang inférieur reçoivent une valeur différente de ceux de rang supérieur selon une progression — cohérent avec le principe déjà bien compris de spread linéaire
- **Confiance** : A

---

## Synthèse — apports de cette vague (correction structurelle importante)

1. **Correction majeure de la vague 24** : Fan n'est pas une 4e stratégie de génération en masse indépendante — c'est le mécanisme natif déjà à l'œuvre dans la stratégie n°1 (spread par plage `[Thru]`). Le référentiel doit être corrigé en conséquence.
2. **Simplification bienvenue pour l'architecture** : ça réduit le nombre de mécanismes distincts que le moteur de génération doit vraiment traiter comme des cas séparés — de 4 stratégies apparentes à 3 réelles, l'une d'elles (spread par plage) étant elle-même l'expression de Fan
3. **Reste à documenter** : la liste exacte des styles de Fan disponibles (non capturée) — pertinent si ton traducteur doit un jour proposer un choix de style plutôt que le style par défaut

## Correction à appliquer au référentiel

Remplacer la stratégie n°4 ("Fan mode... syntaxe à rechercher") par une note de clarification sur la stratégie n°1 : le spread par plage `[Thru] x [Thru] y` est directement le mécanisme Fan, appliqué par défaut sans invocation explicite de `[Fan]`. `[Fan]`/`{Fan}` ne sert qu'à changer de style de répartition.

<!-- ===== FIN : vague26_fan_syntaxe_confirmee.md ===== -->

---

<!-- ===== DEBUT : vague27_highlight_lowlight_remdim.md ===== -->

# Corpus — vague 27 : Highlight/Lowlight/RemDim (nouveau domaine, exemple officiel complet)

Date de collecte : 29/07/2026

---

## 132 — Exemple officiel complet de macro Highlight/Lowlight avec RemDim (source A, workbook L3)

Source : Eos Family L3 Advanced Workbook (déjà consulté, nouvel extrait)

```
[Query] {Unpatched} {Is In} [Cue] [1] [Thru] [Enter]
→ sélectionne tous les channels non patchés référencés dans les cues 1 et suivantes

[1] [Thru] [9] [At] [Full] [Enter]  (reformulé du contexte "Turns on channels 1 through 9")
[11] [Thru] [16] [At] [75] [RemDim] [/] [50] [Enter]
→ channels 11 à 16 à 75%, avec RemDim (dimming réduit/atténuation) réglé à 50%, séparé par "/"

[Select Last] [-] {Focus} [Record] [Preset] [9997] [Label] Highlight
→ sélectionne la dernière sélection moins le paramètre Focus, enregistre en Preset 9997 nommé "Highlight"
```

- **Confiance** : A
- **Fonction déclarée du système complet** : construire un mécanisme de Highlight/Lowlight avec un preset de référence (9997) et un niveau de "Highlight RemDim" distinct — permet de mettre en avant un ou plusieurs fixtures pendant que le reste du parc passe en Lowlight, avec un niveau intermédiaire (RemDim) pour tout ce qui reste hors sélection
- **Syntaxe de configuration confirmée** : `{Highlight RemDim} [Preset] [XX] [Enter]` pour définir le preset de référence ; `{Highlight RemDim} [Enter]` seul pour désactiver la fonction

## 133 — Résultat décrit du mécanisme Highlight (A, comportement observable confirmé)

- <cite reformulé>En pratique, le channel sélectionné individuellement affiche sa valeur de Highlight Preset, le reste du Group utilise la valeur de Lowlight Preset, et tous les channels en dehors de la sélection utilisent le niveau de Highlight RemDim.</cite>
- **Confiance** : A
- **Thématique** : nouveau — à ajouter comme sous-catégorie de la taxonomie (probablement sous Sélection & patch, ou Affichage/interface selon l'angle)

## 134 — Confirmation de la syntaxe RemDim avec séparateur "/" (A, nouvelle syntaxe confirmée)

- Repris de l'exemple #132 : `[At] [75] [RemDim] [/] [50] [Enter]`
- **Interprétation** : niveau principal (75) et niveau RemDim (50) spécifiés dans la même commande, séparés par `/`
- **Confiance** : A
- **Intérêt pour ton traducteur** : nouveau motif syntaxique à connaître — une commande `[At]` peut porter deux valeurs liées par `/` pour des paramètres de dimming réduit, distinct de la syntaxe simple `[At] [niveau]` déjà bien connue

## 135 — Confirmation de Query avec Cue range comme cible (A, nouvelle combinaison)

- Repris de l'exemple #132 : `[Query] {Unpatched} {Is In} [Cue] [1] [Thru] [Enter]`
- **Interprétation** : combine le mot-clé déjà connu `Unpatched` (vu en vague 14, #084) avec `{Is In}` (vu en vague 14, #081) et une cible `[Cue] [1] [Thru] [Enter]` — recherche à travers une plage de cues plutôt que sur l'état courant seul
- **Confiance** : A


- **Impact** : confirme que la famille Query peut cibler explicitement une plage de cues, cohérent avec le motif déjà vu en vague 14 (#083, `[Que] [Home] [Thru]`) mais avec une syntaxe légèrement différente (`[Cue] [1] [Thru]` plutôt que `[Que] [Home] [Thru]`) — à noter comme variantes possibles selon le contexte, sans certitude sur laquelle est la plus canonique

---

## Synthèse — apports de cette vague

1. **Nouveau domaine fonctionnel découvert et documenté avec un exemple officiel complet** : Highlight/Lowlight/RemDim, absent du corpus jusqu'ici
2. **Nouvelle syntaxe de paramètre double via séparateur `/`** — motif à ajouter à la grammaire générale
3. **Confirmation supplémentaire de la flexibilité de ciblage de `Query`** sur des plages de cues

## Mise à jour de la taxonomie suggérée

Ajouter Highlight/Lowlight/RemDim comme sous-thématique, rattachée à Sélection & patch (mécanisme de sélection différenciée avec niveaux de référence multiples).

<!-- ===== FIN : vague27_highlight_lowlight_remdim.md ===== -->

---

<!-- ===== DEBUT : vague28_journal_terrain_xtouch2eos.md ===== -->

# Corpus — vague 28 : intégration du journal d'observations terrain (projet xtouch2Eos)

Date d'intégration : 29/07/2026
Source : documents de cadrage internes de Cy (JOURNAL_observations_nomad.md, Etude_Pont_MIDI-OSC_EOS.md)

## NOUVEAU NIVEAU DE CONFIANCE À INTRODUIRE : **S** (supérieur à A)

Jusqu'ici l'échelle du corpus plafonnait à A (manuel/doc officielle ETC). Ce journal introduit une catégorie au-dessus : **observation directe et datée sur nomad réel, avec protocole de test explicite et résultat mesuré**. Contrairement à la doc officielle (qui peut être ambiguë, obsolète ou silencieuse sur un point), ce niveau S est vérifié empiriquement par quelqu'un dont je peux tracer exactement ce qu'il a fait et observé. Je propose de noter ces entrées **S** dans le référentiel, au-dessus de A.

À noter : ce journal documente le **canal OSC/TCP + MIDI** pour un pont temps réel (hors macro), donc il ne remplace pas le corpus macro — mais il éclaire directement plusieurs zones où le corpus macro restait dans l'incertitude (comportement de connexion, fiabilité de certaines touches, anti-répétition).

---

## 136 — Framing OSC : auto-détection nécessaire, aucune version fixe garantie (S, observé sur nomad réel)

- **Fait constaté (2026-07-03)** : ce nomad (3.3.5.69, FR) fonctionne en **TCP OSC 1.1 SLIP**, pas en 1.0 packet-length. Détecté par le premier octet reçu (`0xC0` = délimiteur SLIP).
- **Impact direct pour ton projet macro** : si ton futur moteur OSC pour le traducteur de macros communique en TCP, il ne doit **jamais supposer un framing fixe** — l'auto-détection (discriminant : un flux 1.0 ne commence jamais par `0xC0`, un flux SLIP jamais par `0x00`) est une nécessité pratique confirmée, pas une précaution excessive.

## 137 — À la connexion TCP, Eos rejoue tout son état (~40 messages, ~130 ms) (S, observé)

- **Fait constaté** : show/name, user, cues active/previous/pending, 12 softkeys (libellés localisés FR), wheel, switch, active/chan, color/hs, pantilt, xyz, event/state, event/locked — rejoués systématiquement à chaque nouvelle connexion.
- **Impact pour ton outil** : si ton appli Android se connecte à la console pour envoyer une macro, elle recevra un burst initial d'état à absorber/ignorer avant tout envoi — à anticiper dans la gestion de connexion.

## 138 — Eos accepte plusieurs clients TCP simultanés et diffuse à tous (S, observé)

- Confirmé en conditions réelles : observation passive possible pendant qu'un autre logiciel pilote activement la console via un autre client.
- **Impact** : ton appli peut coexister avec un pupitreur qui travaille en direct sur la console sans le perturber, au niveau transport — mais rappelle le risque déjà noté au niveau macro (vague 9, #067 : édition de macro en cours + déclenchement background simultané reste un risque logique, distinct du transport).

## 139 — Feedback de niveau de sub : PAS spontané sur `/eos/out/sub/<n>`, doit passer par les banques OSC (S, confirmé au banc actif)

- **Fait constaté (2026-07-03, banc actif)** : niveau réglé sur `/eos/sub/1` à 0.75 → **aucun retour en 8 secondes** sur `/eos/out/sub/<n>`. Le feedback de niveau nécessite les banques OSC (`/eos/fader/<bank>/config/...` puis niveaux sur `/eos/fader/<bank>/<n>`).
- **Écho de niveau via banque** : mesuré à **+522 ms**, beaucoup plus rapide que les "+3 s" documentés dans l'étude de cadrage (R2) — donnée corrigée empiriquement par rapport à une inquiétude initiale issue de la communauté.
- **Impact pour le corpus macro** : ceci nuance/précise directement le risque déjà noté en vague 3 (#027, macro `SubDown`/`SubUp` et survie ASCII). Ce n'est pas le même sujet exactement (ici c'est le feedback temps réel, pas la persistance ASCII), mais ça confirme que **l'écosystème sub/fader OSC d'EOS a des comportements de feedback non triviaux et non uniformément documentés** — cohérence avec la prudence déjà appliquée à ce risque.

## 140 — Ligne de commande diffusée en clair avec flag d'erreur (S, observé — TRÈS PERTINENT pour un validateur de macro)

- **Fait constaté** : `/eos/out/cmd` et `/eos/out/user/<u>/cmd` diffusent le texte de la ligne de commande en clair, avec un flag d'erreur (`flag_erreur_int`, 1 = erreur de syntaxe). Exemple observé : `"LIVE: Cue 2 : Sub 2 Bouton Go Go Bump #"`.
- **IMPACT MAJEUR POUR TON PROJET DE TRADUCTEUR MACRO** : ceci est potentiellement **le mécanisme de validation en temps réel** que ton architecture cherchait. Le cadrage initial prévoyait un validateur *avant* envoi (syntaxique, statique) — mais ce canal permet une **validation après envoi, par observation du flag d'erreur retourné par la console elle-même**. C'est un filet de sécurité supplémentaire directement exploitable : ton appli pourrait envoyer une commande de test, observer si `/eos/out/cmd` retourne une erreur de syntaxe, et alerter l'utilisateur avant de la graver dans une macro. **Piste d'architecture à ajouter explicitement à la conception.**

## 141 — Liste ETC "Eos OSC Keys" — 1155 touches, déjà récupérée et convertie par toi-même (S — CHANGE COMPLÈTEMENT LA PRIORITÉ 5 DU CORPUS)

- **Fait constaté (2026-07-03)** : <cite reformulé>liste officielle ETC "Eos OSC Keys" récupérée et convertie en module TypeScript (`src/shared/eosKeys.ts`), 1155 touches, nom OSC → commande interne.</cite>
- **CORRECTION MAJEURE À APPORTER AU CORPUS** : la priorité banc n°5 ("liste de recherche complète de l'éditeur, capturer au-delà de F→M") est **déjà résolue** par ce fichier, avec une couverture bien supérieure (1155 entrées vs ~60 vues en image) et une source officielle ETC directe, pas une capture d'écran partielle. **Ce fichier `eosKeys.ts` devient la référence prioritaire absolue pour toute la grammaire de touches** — bien au-dessus de tout ce que la collecte web a pu produire jusqu'ici.
- **Correction de contenu déjà identifiée par toi** : `stop_0` n'existe pas — le stop du master playback est `stop`. `go_0` = GO, `go` = PLAYBACK_GO, `stopback` = PLAYBACK_STOP_BACK. Ceci **contredit potentiellement** l'entrée #109 du corpus (`Go_0` confirmé comme équivalent du Stop/Back) — à clarifier : soit une confusion de casse/nom entre les deux sources, soit deux touches réellement différentes. **Point de vigilance à trancher.**
- Insensible à la casse ; l'espace remplace `_` dans les noms de touches.
- **Action recommandée immédiate** : si tu peux partager `src/shared/eosKeys.ts`, je l'intègre comme référence structurelle unique du corpus de touches — ça remplacerait avantageusement des dizaines d'entrées collectées une par une depuis le début du projet.

## 142 — Anti-répétition : Eos supprime les répétitions rapides de LA MÊME touche OSC (S, mesuré précisément)

- **Fait constaté et quantifié (2026-07-04)** : Eos supprime les répétitions consécutives de la même touche OSC espacées de moins de ~1 s. Mesures précises : à 700 ms, une frappe sur deux passe ; à 1000 ms, tout passe. Les touches différentes passent sans limite. Le clavier physique n'est pas concerné. L'alternance de casse ne contourne pas le filtre (normalisation avant anti-répétition).
- **Correction ultérieure importante (2026-07-07)**, à ne pas perdre : re-test avec la touche Go (`go_0`) en rafale de 13 appuis à ~150 ms → **13/13 reçus et exécutés**, aucune coalescence. **La règle "~1 s" n'est PAS universelle** — elle s'avère **spécifique aux touches `encoder_category_*`** (Eos coalesce le fait de re-sélectionner une catégorie déjà active), pas une règle générale de anti-répétition de touche.
- **IMPACT MAJEUR, CORRECTION À APPORTER AU CORPUS** : ceci nuance très concrètement plusieurs entrées déjà collectées sur des comportements "capricieux" de touches en macro (ex: vague 16 sur Lamp Control, vague 8 sur Go_To_Cue). Une partie de ce qui semblait être des bugs aléatoires côté communauté pourrait en réalité être ce mécanisme d'anti-répétition **ciblé sur certaines familles de touches précises**, pas un problème de macro en général. Priorité de recherche à ajouter : identifier si d'autres familles de touches que `encoder_category_*` sont concernées.
- **Leçon méthodologique explicitement formulée par toi, à adopter pour tout le corpus** : *"ne jamais figer un comportement matériel à partir de la seule lecture d'un tableau/menu d'éditeur — toujours revérifier avec un envoi réel et une observation confirmée avant de coder en dur."* Cette leçon s'applique un cran plus haut à mon propre travail de collecte web : je devrais systématiquement signaler, comme tu le fais, quand une hypothèse a été révisée après test, plutôt que de la laisser comme un fait isolé.

## 143 — Encodeurs relatifs : complément à deux confirmé, pas sign-magnitude Mackie (S, mesuré)

- **Fait constaté (2026-07-03)** : encodeur 1 (CC10) en relatif complément à deux — droite = valeur 1, gauche = valeur 127 (pas de convention "65 = -1" façon Mackie). Décodage confirmé par distribution mesurée ({1×35, 127×28}).
- **Pertinence pour le corpus macro** : périphérique au projet macro directement, mais utile si un jour ton traducteur doit produire des séquences liées à des molettes/encodeurs (`/eos/wheel`) — la convention d'encodage réelle est confirmée expérimentalement, contrairement à toute documentation qui pourrait laisser deviner l'autre convention.

## 144 — Pagination des encodeurs NON publiée en OSC — limite structurelle confirmée par ETC en creux (S, observé + recherche communautaire)

- **Fait constaté** : cliquer les onglets de catégorie sur la GUI Eos n'émet **aucun** message OSC — confirmé par appui clavier direct ("Encoder Page Focus" → rien en OSC). Demande communautaire de "subscribe to the active encoder page" jamais implémentée par ETC.
- **Règle de correspondance déduite et validée sur deux projecteurs différents** : Pan/Tilt épinglés seuls en première page de Focus, reste dans l'ordre des index Eos par tranches de 4 — reproductible et confirmée par observation croisée (Rogue R2 Wash et K15).
- **Pertinence pour le corpus macro** : confirme une **limite structurelle du protocole OSC d'EOS** (certains états d'affichage/navigation restent invisibles en OSC) cohérente avec ce qu'on avait déjà déduit indirectement en vague 21 (motif de contournement Snapshot pour la navigation Encoder Display non capturable en macro, #111). Ce journal **confirme empiriquement, au niveau protocole**, la même limite que la communauté du forum contournait de façon empirique au niveau macro.

## 145 — Deux touches à clarifier d'urgence entre les deux sources du projet (conflit potentiel à trancher)

- Corpus macro (vague 20, #109) : `Go_0` = équivalent du Stop/Back du playback principal, trouvé dans le champ de recherche macro
- Journal xtouch2Eos (#141 ci-dessus) : `go_0` = GO (démarrage de cue), distinct de `stopback` = PLAYBACK_STOP_BACK
- **Ces deux affirmations semblent contradictoires** sur ce que fait `go_0`/`Go_0`. Possibilités : erreur dans l'une des deux sources, confusion de casse représentant en fait deux touches distinctes (`Go_0` vs `go_0` pourraient être normalisées différemment), ou erreur de ma part en vague 20 dans l'interprétation du témoignage forum d'origine.
- **Statut : à trancher en priorité.** La source `eosKeys.ts` (1155 entrées officielles) devrait faire foi si elle est consultée directement — recommandation de vérifier ce point spécifiquement en premier si tu partages ce fichier.

---

## Synthèse de cette vague — la plus importante en qualité de source depuis le début du corpus

1. **Nouveau niveau de confiance S introduit**, au-dessus de A — observation directe datée et protocolée sur matériel réel
2. **La priorité banc n°5 du corpus (liste de touches complète) est en réalité déjà résolue** ailleurs dans ton propre travail (`eosKeys.ts`, 1155 entrées) — la recherche web que je menais pour la reconstituer était une duplication d'effort
3. **Piste d'architecture majeure découverte** : validation post-envoi via observation du flag d'erreur sur `/eos/out/cmd` — à ajouter au cadrage du validateur
4. **Correction méthodologique de fond, applicable rétroactivement à plusieurs entrées C du corpus** : l'anti-répétition ~1s n'est pas générale, elle cible spécifiquement `encoder_category_*` — plusieurs comportements "capricieux" rapportés par la communauté forum pourraient avoir des explications structurelles similaires, non génériques
5. **Un conflit factuel à trancher** entre deux sources internes au corpus (#145)

## Recommandation immédiate

Si tu peux partager `src/shared/eosKeys.ts`, c'est la pièce la plus précieuse identifiable à ce stade pour l'ensemble du projet — elle remplacerait avantageusement une bonne partie de la collecte fragmentaire de touches menée depuis le début, avec une fiabilité largement supérieure (source officielle ETC directe, complète, déjà structurée en code).

<!-- ===== FIN : vague28_journal_terrain_xtouch2eos.md ===== -->

---

<!-- ===== DEBUT : vague29_eoskeys_integration.md ===== -->

# Corpus — vague 29 : intégration eosKeys.ts (liste officielle ETC, 1155 touches)

Date d'intégration : 29/07/2026
Source : `src/shared/eosKeys.ts`, projet xtouch2Eos de Cy — extraction du PDF officiel ETC "Eos OSC Keys.pdf"
**Niveau de confiance : A — la meilleure source structurelle du corpus entier pour la grammaire de touches.**

Ce fichier devient LA référence pour toute question "cette touche existe-t-elle, sous quel nom OSC exact".

---

## 146 — RÉSOLUTION DU CONFLIT #145 : Go_0 tranché, correction à porter au corpus macro

Vérification directe dans la liste :
```
{ osc: "go", internal: "PLAYBACK_GO" }
{ osc: "go_0", internal: "GO" }
{ osc: "gocue0", internal: "PLAYBACK_CUE_ZERO" }
{ osc: "gotocue", internal: "PLAYBACK_GOTOCUE" }
{ osc: "stopback", internal: "PLAYBACK_STOP_BACK" }
{ osc: "stop", internal: "STOP" }
```

**Verdict** : le journal terrain (#141) avait raison, ma vague 20 (#109) était **incorrecte**. `go_0` correspond bien à `GO` (déclenchement de cue), pas au Stop/Back. Le témoignage forum que j'avais interprété en vague 20 concernant "une commande native `Go_0` qui fait la même chose que Send_String /eos/key/stop=1" était soit une erreur de l'utilisateur du forum, soit une mauvaise lecture de ma part. **`stopback` est la touche correcte pour Stop/Back du playback principal**, `go_0`/`GO` sert à déclencher.

**Action : corriger l'entrée #109 du corpus** (vague 20) — la commande citée pour l'auto-adressage OSC "stop" devrait être `stopback`, pas `Go_0`.

## 147 — Confirmation et correction de casse pour toute la famille déjà connue

Vérifications directes contre la liste officielle — tout ce qui suit est maintenant **niveau A certain**, remplaçant les niveaux C/D antérieurs du corpus :

| Terme du corpus (vagues 1-27) | Confirmé dans eosKeys.ts | Note |
|---|---|---|
| `Macro_Loop_Begin` | `macro_loop_begin` → `MACRO_LOOP_BEGIN` | confirmé exact |
| `Macro_Loop_End` | `macro_loop_end` → `MACRO_LOOP_END` | confirmé exact |
| `Macro_Wait` | `macro_wait` → `MACRO_WAIT` | confirmé exact |
| `Wait_For_Enter` | `wait_for_enter` → `MACRO_PAUSE_FOR_ENTER` | confirmé, nom interne différent |
| `Wait_For_Input` | `wait_for_input` → `MACRO_PAUSE_FOR_INPUT` | confirmé |
| `Select_Last` | `select_last` → `SELECT_LAST` | confirmé |
| `Select_Active` | `select_active` → `SELECT_ACTIVE` | confirmé |
| `select_last_params` | `select_last_params` → `SELECT_LAST_PARAMS` | confirmé exact |
| `SubDown`/`SubUp` | `subdown` → `SUB_BUMP_DOWN`, `subup` → `SUB_BUMP_UP` | **confirmé A, remplace la confiance C de la vague 3** |
| `Is In` | `is_in` → `IS_IN` | confirmé |
| `Greater Than` / `Less Than` | `greater_than` → `GREATER_THAN`, `less_than` → `LESS_THAN` | confirmé — **existent bel et bien comme touches macro à part entière**, pas seulement comme concept Query abstrait (nuance à la correction de vague 13) |
| `Can Be` | absent — mais `can_be` → `CAN_BE` existe | confirmé, orthographe correcte = `can_be` (le corpus vague 14 #083 utilisait "Can Be" avec espace, à corriger) |
| **`Isn't In` / `Could Be`** | **ABSENTS de la liste officielle** | ⚠️ voir #148 ci-dessous — écart important |
| `Highlight`/`Highlight RemDim` | `highlight` → `HIGHLIGHT`, `highlight_remdim` → `HIGHLIGHT_REM_DIM`, `highlight_preset` → `HIGHLIGHT_PRESET`, `lowlight_preset` → `LOWLIGHT_PRESET` | confirmé exact |
| `From Absolute` | absent tel quel — voir `make_absolute` → `MAKE_ABSOLUTE` | ⚠️ nuance, voir #149 |
| `Break Nested` | `break_nested` → `BREAK_NESTED`, `break_nested_off` → `BREAK_NESTED_OFF` | confirmé exact |
| `Fan` (mirror in/out, etc.) | `mirror_in` → `FAN_MIRROR_IN`, `mirror_out` → `FAN_MIRROR_OUT`, `interleave` → `FAN_INTERLEAVE`, `cluster` → `FAN_CLUSTER`, `jump` → `FAN_JUMP`, `repeat` → `FAN_REPEAT`, `center` → `FAN_CENTER`, `chan_per_group` → `FAN_CHANNELS_PER_GROUP`, `num_groups` → `FAN_NUM_GROUPS` | **découverte majeure, voir #150** |
| `Effect_Edit` | absent tel quel — `open_pattern_effects`, `effect_edit`... en réalité `effect_edit` → `EFFECT_PATTERN_EDIT` existe | ⚠️ nuance, voir #151 |
| `More_SoftKeys` | `more_softkeys` → `MORE_SOFTKEYS` | confirmé existant — infirme partiellement la vague 4 (#035) qui le donnait comme "ne s'enregistre pas" : la touche EXISTE officiellement, le problème rapporté était peut-être un bug d'enregistrement spécifique, pas une absence de la touche elle-même |
| `Open_Browser` | `open_browser` → `OPENBROWSER` | confirmé existant, même remarque que ci-dessus |
| `RFR Enable` | `rfr` → `RFR_ENABLE` | confirmé, nom OSC = `rfr` seul (pas `rfr_enable`) |
| `Macro Mode` | `macro_mode` → `MACRO_MODE` ; `background_mode` → `MACRO_BACKGROUND` ; `foreground_mode` → `MACRO_USER` ; `default_mode` → `MACRO_DEFAULT_MODE` | confirmé, et révèle que Foreground/Background/Default sont *trois touches distinctes*, pas un seul softkey cyclique comme je le pensais |
| `Send_String` | `send_string` → `SEND_SERIAL_STRING` | confirmé — nom interne révèle qu'il s'agit d'abord d'un mécanisme "serial string", l'OSC en est une extension |
| `Macro Entry Delete` | `macro_entry_delete` → `MACRO_ENTRY_DELETE` | confirmé exact (vu dans l'image, vague 12) |
| `List Partition` | `list_partition` → `CUE_PARTITION` | confirmé, nom interne clarifie le sens (partition de cue list) |
| `Interpolate` | `interpolate` → `INTERPOLATE` | confirmé existant — **reste à documenter fonctionnellement**, mais son existence est maintenant certaine |
| `Group Cells` | **ABSENT** — le plus proche est `group_channels_by_5` → `GROUP_CHANNELS_BY_5` | ⚠️ écart, voir #148 |

## 148 — Écarts constatés entre l'image (vague 12) et la liste officielle eosKeys.ts

Plusieurs termes vus dans ton image de capture n'apparaissent pas identiques dans cette liste :
- **"Group Cells"** de l'image ≠ toute entrée de eosKeys.ts. Le plus proche sémantiquement est `group_channels_by_5`. Hypothèse : l'image montrait peut-être un intitulé d'affichage (UI) différent du nom de commande OSC sous-jacent, ou une fonctionnalité plus récente que la version du PDF source d'eosKeys.ts.
- **"Isn't In" et "Could Be"** (confirmés textuellement en vague 14, #081, comme faisant partie de la famille Query) sont **absents** de eosKeys.ts, alors que `is_in` et `can_be` y figurent. **RÉSOLU (session de consolidation, 2026-07-31)** par comparaison croisée avec la table officielle « Eos OSC Keys » du chapitre 31 de l'Eos Family User Manual v3.2.0 (`manuals/operations-manual/31-show-control.md`, voir `reference/eosKeys_vs_manual_comparison.md` pour le détail complet) :
  - **`isn't_in` → `ISNT_IN`** : existe réellement comme touche OSC nommée, présente dans le manuel officiel v3.2.0 mais absente de `eosKeys.ts` (probablement une omission lors de l'extraction automatique du PDF source, l'apostrophe ayant pu perturber le parsing). **Confiance A, à traiter comme confirmée.**
  - **`can't_be` → `CANT_BE`** : même situation, existe réellement, absente de `eosKeys.ts`. **Confiance A, à traiter comme confirmée.**
  - **`could_be`** : absent des deux sources officielles (ni le manuel v3.2.0 ni `eosKeys.ts`) — confirme l'hypothèse déjà posée ici : ce n'est probablement pas une touche OSC nommée indépendamment, mais un softkey contextuel de l'écran Query sans exposition OSC directe.
- **Constat général important** : eosKeys.ts liste des **noms de touches OSC** (`/eos/key/<nom>`), pas nécessairement l'intégralité du vocabulaire de la grammaire de ligne de commande au sens large (qui peut inclure des mots comme `Thru`, `Enter`, des labels de softkeys contextuels non listés séparément, etc. — même si beaucoup s'y trouvent aussi, ex: `thru` → `THRU` est bien présent). Les deux corpus (grammaire ligne de commande générale et liste de touches OSC) se recoupent très largement mais ne sont pas rigoureusement identiques.

## 149 — Nuance sur `{From Absolute}` : absent en tant que tel, mais mécanique confirmée autrement

- eosKeys.ts ne contient pas d'entrée `from_absolute`. Ce qui existe : `make_absolute` → `MAKE_ABSOLUTE`.
- **Hypothèse à vérifier** : soit `{From Absolute}` (vu dans l'image et le Level 4 workbook, vague 11 #077) est un **softkey contextuel** de l'écran Copy To, pas une touche macro nommée indépendamment dans le dictionnaire OSC général ; soit c'est une erreur de transcription de ma part en vague 11/12 et le vrai nom est `make_absolute`. **À trancher : les deux corpus se recoupent mais ne sont pas identiques (cf. #148).**

## 150 — DÉCOUVERTE MAJEURE : la famille complète des paramètres Fan est maintenant connue (source A directe)

Confirmé dans eosKeys.ts, réponse directe à la zone encore ouverte "styles de Fan alternatifs" (référentiel, vague 26) :

```
center        → FAN_CENTER
chan_per_group → FAN_CHANNELS_PER_GROUP
cluster       → FAN_CLUSTER
interleave    → FAN_INTERLEAVE
jump          → FAN_JUMP
mirror_in     → FAN_MIRROR_IN
mirror_out    → FAN_MIRROR_OUT
num_groups    → FAN_NUM_GROUPS
repeat        → FAN_REPEAT
fan_curve     → FAN_CURVE
```

**Impact** : la zone "styles de Fan non exhaustivement documentés" (référentiel de risques, section zones ouvertes) est **résolue**. Fan dispose d'au moins 9 modificateurs/styles distincts : Center, Channels Per Group, Cluster, Interleave, Jump, Mirror In, Mirror Out, Num Groups, Repeat, plus une Curve dédiée. C'est une richesse de contrôle bien supérieure à ce qu'on avait supposé — chacun mériterait une vérification fonctionnelle individuelle avant usage dans le traducteur, mais leur existence et leur nom exact ne sont plus une inconnue.

## 151 — Nuance sur Effect_Edit : la touche existe réellement, contredit le statut D de la vague 2

- eosKeys.ts confirme : `effect_edit` → `EFFECT_PATTERN_EDIT`
- **Correction à porter à l'entrée #021** (vague 2) : la commande `Effect_Edit` **existe bel et bien** comme touche officielle. L'échec rapporté par l'utilisateur du forum (vague 2) tenait donc probablement à une erreur de syntaxe des arguments qui suivent (`action 1 level CP1`), pas à l'inexistence de la commande elle-même. Le statut D doit être révisé : la touche est confirmée A, seul l'usage précis rapporté par l'utilisateur reste non résolu.

## 152 — Champ complet de nouvelles familles jamais vues dans le corpus, à fort potentiel

Plusieurs familles entières découvertes d'un coup, absentes de toute vague précédente :

- **RTC (Real Time Clock) / Astro** : `after_sunrise`, `before_sunrise`, `after_sunset`, `before_sunset`, `rtc_date`, `rtc_days`, `rtc_time`, jours de la semaine (`rtc_monday`...`rtc_sunday`) — système de déclenchement horaire/astronomique jamais mentionné dans tout le corpus jusqu'ici. Pertinent si un régisseur veut un jour une macro liée à l'heure réelle.
- **Pixel Mapping complet** : `pixelmap`, `pixel_map_edit`, `pixel_map_flash`, `pixel_map_mask`, `pixel_map_direction`, etc. — domaine entièrement absent du corpus, pertinent pour dance floors/LED walls (en lien avec le contexte Capture déjà connu de Cy).
- **Multiconsole power management** : `multiconsole_power_off`/`_on` — gestion d'extinction à distance, absent du corpus vague 9.
- **RVI (Remote Video Interface)** : `rvi_settings` — jamais vu.
- **Curve editing** : `curve`, `curve_edit`, `curves` — courbes de fade personnalisées, domaine jamais exploré.
- **Color Path avancé** : `color_path`, `cie_xyy`, `gel_match_setting_brightest/hybrid/spectrum` — bien plus riche que ce que la vague 5 (palettes) avait couvert.
- **Partition de cue list et de contrôle** : `partition`, `partitionedcontrol`, `list_partition` — confirme et enrichit #058 (vague 7).
- **Lamp Controls étendus** : `lamp_on`, `lamp_control`, `lamp_controls_edit`, `lamp_ctrls`, `preheat`/`preheat_off`/`preheat_time`, `shutdown_fixture`, `shutdown_macro`, `test_fixture` — bien plus complet que la vague 16.
- **`startup_macro`** — mécanisme de macro exécutée au démarrage du show, jamais documenté dans le corpus, potentiellement très pertinent pour ton cas d'usage "début de show" déjà évoqué en vague 4 (#031 exemples officiels channel check).
- **`shutdown_macro`** — équivalent en fin de show.

## 153 — Confirmation de `Query {Unpatched}` sous forme de touche dédiée

- `unpatched` → `UNPATCHED_QUERY` — confirme et précise l'usage vu en vague 14 (#084) et vague 27 (#135), avec la clarification que c'est un mot-clé de filtre Query dédié, nom interne explicite

---

## Synthèse — apports de cette vague (la plus corrective du corpus à ce jour)

1. **Conflit #145 résolu** : `go_0` = GO (démarrage), pas Stop/Back — correction à porter rétroactivement sur l'entrée #109
2. **Dizaines d'entrées C/D élevées à confiance A** par confirmation directe dans la source officielle
3. **Famille Fan complète découverte** (9+ modificateurs) — comble une zone ouverte identifiée depuis la vague 26
4. **`Effect_Edit` réhabilité** : la touche existe, l'échec rapporté n'invalide pas son existence
5. **Plusieurs familles entières jamais couvertes découvertes d'un coup** (RTC/Astro, Pixel Mapping, Curves, Lamp Controls étendus, startup/shutdown macro) — perimètre de la grammaire globale bien plus large que ce que la collecte fragmentaire avait laissé deviner
6. **Deux écarts non résolus** à garder en tête : `Isn't In`/`Could Be` absents de cette liste malgré confirmation textuelle ailleurs ; `Group Cells` et `From Absolute` de l'image ne correspondent à aucune entrée exacte

## Action immédiate recommandée

Ce fichier devrait être considéré comme **la table de référence canonique** pour toute validation syntaxique future du traducteur — bien supérieure à toute liste partielle collectée par recherche web. Toute nouvelle vague de collecte devrait désormais **vérifier systématiquement contre cette liste** avant de qualifier une touche de "confirmée" ou "non trouvée".

<!-- ===== FIN : vague29_eoskeys_integration.md ===== -->

---

<!-- ===== DEBUT : vague30_resolution_isnt_in_syntaxe_generale.md ===== -->

# Corpus — vague 30 : résolution Isn't In / Could Be, syntaxe softkey vs mot OSC clarifiée

Date de collecte : 29/07/2026

---

<!-- ⚠️ Il manque ici uniquement le titre et les premières lignes de l'entrée #154
     (vague 30) — le texte reprend ci-dessous en cours d'entrée #154, à la ligne
     « Confiance : C/B ». Lacune mineure, à compléter si retrouvée. -->


- **Confiance** : C/B — softkeys confirmés fonctionnels dans plusieurs témoignages indépendants et un article pédagogique dédié, mais nom OSC exact toujours non capturé formellement
- **Statut** : la fonctionnalité existe et est documentée en usage réel ; seul le nom de touche OSC précis (si distinct de `is_in`/`can_be` avec un modificateur) reste à vérifier au banc

## 155 — DÉCOUVERTE MAJEURE ET NON PRÉVUE : absence native d'un bouton "Not" général, confirmée par ETC lui-même (B, réponse support directe)

- **Fil source** : "query with channels, groups and cue ranges"
- **Demande formulée par un utilisateur expérimenté** (habitué d'une autre console où ce bouton existe) : <cite reformulé>il manque un bouton "Not" qui fonctionnerait en dehors du contexte Query — par exemple "Select Active Not Enter" (sélectionne tout ce qui n'est pas actif), "Group 990 Not Out" (éteint tout ce qui n'est pas dans le groupe 990), "Capture Not Enter" (sélectionne tout ce qui n'est pas capturé) — un peu comme le softkey "Isn't" de Query, mais utilisable partout.</cite>
- **Réponse du support technique ETC, confirmant une limite structurelle** : <cite reformulé>la syntaxe recherchée en sélection de Group n'est actuellement pas valide, mais elle l'est en Intensity Palette : `[1] [Thru] [10] [Query] [Can Be] [Intensity Palette]...`</cite>
- **Confiance** : B — réponse directe du support technique ETC
- **Impact architecture majeur, nouveau pour le corpus** : ceci confirme une **limite structurelle du langage de commande EOS** — la négation logique (`Not`) n'est PAS un opérateur général disponible partout, elle est **restreinte au contexte Query**. Ça complète et confirme définitivement la correction déjà faite en vague 13/14 : `Greater Than`/`Less Than`/`Is In`/`Isn't In` ne sont *jamais* des opérateurs conditionnels génériques de macro — ils sont structurellement enfermés dans le sous-système Query, et rien d'équivalent n'existe ailleurs dans la grammaire. **Ceci ferme définitivement la piste "logique conditionnelle en macro"** ouverte en vague 12 puis nuancée en vague 13/14 — la réponse est maintenant catégorique et officielle : ce type de logique n'existe structurellement qu'à l'intérieur de Query, nulle part ailleurs.

## 156 — Syntaxe générale de la ligne de commande EOS confirmée officiellement : Objet-Action-Cible (C, mais formulation très claire d'un contributeur expérimenté)

- **Fil source** : "EOS syntax"
- <cite reformulé>La syntaxe est très cohérente, parfois même de façon rigide — toujours de la forme Objet Action Cible, avec omission possible de l'objet ou de la cible selon le contexte. Exemples : `Chan 1 At 50 Cue 5 Time 20`, `Chan 1 Record Preset 3`. Le comportement qui semblait incohérent à l'utilisateur d'origine (`Cue # label name` accepté, mais pas `Cue # Record`) s'explique : dans le premier cas, `label` est l'action et `name` la cible dans la continuité du même objet `Cue #` ; dans le second cas, `Record` a pour cible ce qui la précède (ex: `group 5 focus Record Cue 5`), donc `Cue # Record` seul n'a pas de sens dans cette grammaire.</cite>
- **Confiance** : C, mais formulation pédagogique très claire, cohérente avec tout ce qu'on a observé empiriquement dans le corpus jusqu'ici
- **Impact architecture majeur** : c'est la **première formulation explicite et généralisée de la grammaire syntaxique de fond** de toute la ligne de commande EOS trouvée dans le corpus. Jusqu'ici on avait des dizaines d'exemples concrets mais jamais la règle générale sous-jacente. **Cette règle Objet-Action-Cible devrait devenir le squelette de la grammaire formelle (BNF ou équivalent) que ton parseur NL → représentation interne devra produire.**

---

## Synthèse — apports de cette vague (deux découvertes structurantes majeures)

1. **Écart eosKeys.ts résolu** (#154) : `Isn't In`/`Could Be` sont des softkeys contextuels de l'écran Query, pas des touches OSC nommées indépendamment — cohérent avec l'architecture du dictionnaire OSC
2. **Confirmation officielle et définitive qu'aucune négation générale n'existe hors du contexte Query** (#155) — ferme la piste de "logique conditionnelle en macro" une fois pour toutes, avec une source B directe
3. **Règle syntaxique de fond découverte : Objet-Action-Cible** (#156) — pièce manquante pour formaliser la grammaire générale que le traducteur devra produire, au-delà du simple recensement de mots-clés isolés accumulé jusqu'ici

## Mise à jour à porter à la grammaire consolidée

- Ajouter en tête de la section "Mécanique de fond" : **la grammaire de ligne de commande EOS suit la structure Objet-Action-Cible**, avec omissions contextuelles possibles — règle de fond pour tout générateur de commande
- Fermer définitivement la question de la logique conditionnelle : confirmée absente hors du sous-système Query (limite structurelle assumée, pas un manque à combler)

<!-- ===== FIN : vague30_resolution_isnt_in_syntaxe_generale.md ===== -->

---

<!-- ===== DEBUT : vague31_syntaxe_gel_confirmee.md ===== -->

# Corpus — vague 31 : syntaxe Gel confirmée (Color <bibliothèque> / <numéro>)

Date de collecte : 29/07/2026, en réponse à un test pratique de traduction NL→EOS mené par Cy

---

## 157 — Syntaxe officielle confirmée pour sélection de gel par référence fabricant (A, exemple exact du workbook officiel)

- Source : Eos Family Console Programming Level 1 Essentials Workbook v3.1 (officiel ETC)
- **Syntaxe confirmée** : `[Channel/Select Last] {Color} [n° bibliothèque] [/] [n° gel] [Enter]`
- Exemple exact donné : `[Select Last] {Color} [5] [/] [381] [Enter]` → bleu (bibliothèque 5)
- `[At]` peut remplacer `{Color}` dans la même syntaxe, utilisable n'importe où en Live
- **Confiance** : A

## 158 — Confirmation indépendante de la numérotation des bibliothèques, Lee = 3 (C, deux fils convergents)

- **Fils sources** : "loading color palettes with LEE colors", cheat sheet Tower Theatre (document tiers mais citant fidèlement l'interface officielle)
- <cite reformulé>Chaque fabricant a un numéro affiché devant son nom dans le color picker — Lee est le numéro 3. La syntaxe `[Channel] {Color} [3] [/] [201]` sélectionne Lee 201.</cite>
- **Confiance** : C, mais cohérent avec #157 et confirmé par plusieurs utilisateurs indépendants
- **Réponse au cas testé (Chan 4, Lee 195)** : `Chan 4 Color 3 / 195 Enter`

## 159 — Limite reconnue et documentée : le rendu du gel picker ne correspond pas toujours fidèlement à la teinte physique réelle (C, multiples témoignages convergents, dont un profil technique ETC)

- **Fils sources** : "loading color palettes with LEE colors", "Why do gel colors differ from link-to colors?", "Rosco Files Suit Against ETC" (ControlBooth)
- <cite reformulé>Ce n'est pas un défaut du logiciel — c'est inévitable compte tenu de l'énorme variété de fixtures pour lesquels le color picker doit fonctionner. Pratique courante des programmeurs : utiliser le gel comme point de départ approximatif, ajuster manuellement jusqu'à obtenir le rendu voulu, puis enregistrer ce résultat ajusté comme palette by-type portant le numéro du gel d'origine — réutilisable ensuite d'un show à l'autre par merge.</cite>
- **Confiance** : C, mais multiples sources indépendantes convergentes sur ce point, dont une discussion impliquant directement la précision colorimétrique du système (affaire Rosco vs ETC mentionnée dans un fil, hors périmètre juridique mais confirmant que le sujet est reconnu comme un point de friction sérieux dans la profession)
- **Impact pour le traducteur** : toute commande générée à partir d'une référence de gel doit être présentée à l'utilisateur comme un **point de départ approximatif**, pas un résultat garanti fidèle — cohérent avec le principe déjà retenu de validation utilisateur avant tout envoi définitif. Bon argument supplémentaire pour le système de menus déroulants déjà noté en idée produit.

## 160 — Conventions OSC officielles pour les chaînes de gel (A, référence structurelle utile)

- Source : etcconnect.com/WebDocs, "Eos OSC Conventions"
- <cite>Les gels sont représentés sous forme de chaînes selon un format tel que : L2 pour Lee 2, AP1150 pour Apollo 1150, T12 pour TokyoBS Poly Color 12.</cite>
- **Confiance** : A
- **Impact** : révèle une **deuxième syntaxe possible**, orientée OSC plutôt que ligne de commande console — potentiellement plus directement exploitable si ton moteur de transport communique en OSC pur plutôt qu'en simulation de ligne de commande. Format `<initiale fabricant><numéro>` (ex: `L195` pour Lee 195) plutôt que `<numéro bibliothèque>/<numéro gel>`. **Les deux syntaxes coexistent probablement pour deux contextes différents (ligne de commande vs argument OSC direct) — à clarifier au banc si les deux sont utilisées dans le traducteur.**

---

## Synthèse de cette vague

1. **Syntaxe de gel résolue et confirmée A** : `Chan <n> Color <bibliothèque> / <numéro> Enter`, avec Lee = bibliothèque 3
2. **Découverte d'une seconde syntaxe possible côté OSC pur** (`L195` façon lettre+chiffre) — distincte de la syntaxe ligne de commande, à clarifier laquelle utiliser selon le mode de transport retenu par le traducteur
3. **Limite de fidélité colorimétrique bien documentée** — argument supplémentaire pour la validation utilisateur avant envoi définitif, cohérent avec la doctrine produit déjà établie (cf. vague 25, absence délibérée d'auto-palette)

<!-- ===== FIN : vague31_syntaxe_gel_confirmee.md ===== -->

---

<!-- ===== DEBUT : vague32_polysemie_contextuelle_at.md ===== -->

# Corpus — vague 32 : polysémie de `At` selon le contexte d'écran (correction de Cy)

Date de collecte : 29/07/2026, via correction directe de Cy sur un test de traduction

---

## 161 — DÉCOUVERTE STRUCTURANTE MAJEURE : `At` a un sens différent selon l'écran/contexte actif (S — source Cy, expert du domaine)

- **Correction directe de Cy** : la commande `1 Thru 100 At 100 Enter` sur l'écran **Patch** assigne l'adresse DMX de départ (channels 1 à 100 patchés à partir de l'adresse 100), alors que la même syntaxe `Chan X At <valeur> Enter` en écran **Live** assigne un niveau d'intensité (0-100%).
- **Confiance** : S — correction directe d'un expert du domaine sur un cas concret, la source la plus fiable possible pour ce type d'affirmation
- **IMPACT ARCHITECTURAL MAJEUR, LE PLUS IMPORTANT DEPUIS LA DÉCOUVERTE DE LA RÈGLE OBJET-ACTION-CIBLE (vague 30)** : ceci révèle que la grammaire EOS n'est **pas purement contextuelle au sens Objet-Action-Cible seul** — le sens d'un même mot-clé (`At`) dépend aussi de **l'écran/mode actif au moment de l'exécution** (Patch vs Live vs probablement Blind, Effect, etc.). C'est une dimension supplémentaire de la grammaire qui n'avait jamais été formalisée dans le corpus jusqu'ici, bien qu'on ait déjà croisé des symptômes isolés de ce phénomène sans le nommer clairement :
  - Vague 22 (#119) : `[Blind] [Enter]` non qualifié était déjà identifié comme ambigu selon le contexte
  - Vague 9 (#068) : `{Target}` vers un User dépend du mode Foreground/Background
  - Vague 8 (#061) : `Go_To_Cue` dépend du contexte d'exécution
  
  Mais aucune de ces observations n'avait explicitement isolé le mécanisme **"même mot-clé, sens différent selon l'écran"** — c'était toujours interprété comme un problème de fiabilité d'exécution (la commande marche ou pas), pas comme un vrai problème de **polysémie sémantique contextuelle** qu'il faut résoudre AVANT même de valider la syntaxe.

## Conséquence directe et non négociable pour l'architecture du traducteur

**La représentation interne (le "ticket", cf. discussion initiale du projet) doit impérativement inclure un champ "contexte d'écran actif"**, pas seulement l'action et ses paramètres. Sans ce champ, le traducteur ne peut pas savoir si générer `At 100` signifie "adresse DMX 100" ou "intensité 100%" — la même sortie textuelle a un sens radicalement différent selon où elle s'exécute.

Ça reconfigure une partie du modèle déjà esquissé :
- Avant : `{action: "assign_value", target: "chan_1_thru_100", value: 100}`
- Correction nécessaire : `{screen_context: "patch", action: "assign_value", target: "chan_1_thru_100", value: 100}` — le contexte d'écran devient un champ de tête, pas une métadonnée secondaire

## Action de collecte prioritaire à ajouter

Établir une **table de correspondance contexte d'écran → sens des mots-clés polysémiques**, en commençant par `At` (Patch=adresse, Live=intensité) et en cherchant systématiquement d'autres cas similaires (`Time`, `Label`, `Record`... ont-ils aussi des sens différents selon l'écran ?). C'est potentiellement plus important pour la fiabilité du traducteur que la poursuite de la collecte de vocabulaire brut.

---

## Synthèse

Cette vague, bien que courte (une seule entrée), est l'une des plus structurantes du corpus : elle révèle une dimension de la grammaire EOS non formalisée jusqu'ici — la **polysémie contextuelle liée à l'écran actif**, distincte de la polysémie liée au mode Foreground/Background déjà bien documentée. Le référentiel et la grammaire consolidée doivent intégrer cette dimension comme un axe de validation à part entière.

<!-- ===== FIN : vague32_polysemie_contextuelle_at.md ===== -->

---

<!-- ===== DEBUT : vague33_syntaxe_ecran_patch.md ===== -->

# Corpus — vague 33 : syntaxe complète écran Patch (source A/B)

Date de collecte : 29/07/2026

---

## 162 — CONFIRMATION OFFICIELLE DIRECTE de la découverte de Cy (#161) : la ligne de commande "traduit" @ en Address dans le contexte Patch (B, réponse forum très explicite)

- **Fil source** : "Remove fixture in patch"
- **Citation reformulée, la plus directement pertinente trouvée à ce jour pour la découverte de Cy** : <cite reformulé>quand on est en Patch, la ligne de commande fait une sorte de traduction, de sorte que `@` devient "address" (adresse) plutôt que "channel" comme ce serait le cas ailleurs.</cite>
- **Confiance** : B — réponse précise et technique dans un fil de support communautaire
- **Impact** : ceci confirme, avec une source indépendante de Cy, exactement le phénomène qu'il a lui-même identifié en vague 32. Le mécanisme n'est pas limité au mot-clé `At` seul — c'est plus large : le symbole `@` lui-même change de sens selon l'écran actif. **Ça renforce encore la priorité de la table de correspondance contexte→sens déjà décidée en vague 32.**

## 163 — Deux modes de Patch, bascule via `[Format]` (A, structurel)

- Source : etcconnect.com/WebDocs, "Patch [Tab 12]"
- <cite>Deux modes de patch existent : Patching By Channel et Patching By Address. Eos utilise par défaut le mode par channel. Presser `[Format]` en affichage Patch bascule entre les deux modes.</cite>
- **Confiance** : A
- **Impact** : la syntaxe `1 Thru 100 At 100 Enter` confirmée par Cy suppose très probablement le mode **Patching By Channel** (on part d'une plage de channels, on leur assigne une adresse de départ). En mode Patching By Address, la logique d'entrée serait probablement inversée (partir d'une adresse, assigner un channel) — **point non vérifié, à tester si le traducteur doit un jour couvrir aussi ce second mode.**

## 164 — Comportement du spread automatique en Patch confirmé officiellement (A)

- Même source
- <cite>Vous pouvez entrer une adresse de départ sans définir d'adresse de fin. Eos tire cette information des données de bibliothèque (fixture library). Si vous souhaitez laisser un espace de sortie plus grand que ce que requiert la bibliothèque, utilisez `{Offset}`. Si vous spécifiez une adresse de départ qui entre en conflit avec des channels déjà patchés, les channels en conflit seront dépatchés après confirmation de l'utilisateur.</cite>
- **Confiance** : A
- **Impact direct pour la syntaxe testée** : `1 Thru 100 At 100 Enter` fonctionne parce qu'EOS calcule automatiquement, pour chaque channel de la plage, son adresse de départ en fonction de l'empreinte DMX (footprint) du type de fixture déjà sélectionné — ce n'est pas un simple `+1` linéaire si les fixtures ont un footprint DMX de plusieurs canaux. **Nuance importante pour le traducteur** : le spread `Thru`/`At` en Patch n'est pas garanti donner des adresses consécutives simples si le fixture patché occupe plusieurs canaux DMX (ex: une lyre avec 20 canaux) — c'est le mécanisme Fan/spread déjà connu, mais avec un pas de progression qui dépend du footprint, pas toujours de +1.
- **Confirmation du risque de conflit géré nativement** : contrairement à d'autres écrans où les conflits pourraient créer un état incohérent silencieux, EOS demande confirmation utilisateur avant d'écraser un patch existant — bon point pour la sécurité du traducteur, EOS a déjà un filet de sécurité natif ici.

## 165 — Champs complets de l'écran Patch confirmés officiellement (A)

- Sources combinées : "Patch > Patch", "Patch Section" (doc Ion, cohérente avec Eos), "Patch [Tab 12]"
- **Champs confirmés** :
  - `{Type}` — type de device/dimmer, sélection par fabricant puis modèle (par défaut : dimmer)
  - `[Label]`/`{Label}` — label optionnel, `[Label][Label]` efface le label existant
  - `{Offset}` — espace de sortie supplémentaire au-delà du footprint requis
  - `{Interface}` — protocole/interface de sortie (optionnel, sinon hérite du défaut réseau)
  - Colonne `Address` vs `Port/Offset` — bascule d'affichage via `[Data]`
  - Colonne `Type` — type de device/dimmer/élément scénique patché
  - Indicateurs d'erreur RDM/CEM+/CEM3/ACN : `!` (erreur) et `?` (avertissement), ouverts via `{!}` ou `{?}`

## 166 — Accès à l'écran Patch, raccourcis confirmés (A)

- `[Address/Patch]` en double-tap
- `[Displays]` puis `{S3 Patch}`
- Ajout d'onglet (`{+}`) ou `[Tab] [12]` maintenu — Patch est fixé au numéro d'onglet 12
- Pour fixtures avancés : `{Search}` ouvre une recherche par fabricant, nom, ou empreinte DMX (ex: chercher "31" donne tous les fixtures à empreinte de 31 canaux)
- `[At] <adresse de départ>` — confirmé comme méthode officielle pour assigner l'adresse de départ d'un channel ou groupe de channels sélectionnés, avec offset automatique selon le type de fixture [025, A — source "Patching Automated Fixtures, LEDs, and Accessories"]

---

## Synthèse — apports de cette vague

1. **Confirmation indépendante et directe de la découverte de Cy** (#161/#162) — le phénomène de traduction contextuelle n'est pas limité à `At`, il touche aussi `@` lui-même
2. **Nuance importante sur le spread en Patch** : le pas de progression d'adresse dépend du footprint DMX du fixture, pas systématiquement +1 — à ne pas simplifier excessivement dans le traducteur
3. **Structure complète de l'écran Patch documentée** : deux modes (By Channel/By Address), champs, raccourcis, gestion des conflits

## Mise à jour du référentiel

Ajouter à la section polysémie contextuelle (déjà ouverte en vague32) : `@` change de sens selon l'écran (Address en Patch, Channel ailleurs) — confirmé indépendamment par une source communautaire, en plus de la correction directe de Cy.

<!-- ===== FIN : vague33_syntaxe_ecran_patch.md ===== -->

---

<!-- ===== DEBUT : vague34_operations_manual_focus_tabs.md ===== -->

# Corpus — vague 34 : Operations Manual v2.7.0 complet — grammaire officielle et mécanisme de focus

Date de collecte : 29/07/2026
Source : Eos Family Operations Manual v2.7.0 (officiel ETC, via miroir tiers musson.com — contenu ETC)
Confiance : A

---

## 167 — CONFIRMATION OFFICIELLE EXACTE de la règle Objet-Action-Cible (A, remplace/renforce vague30 #156 qui était C)

- <cite>La plupart des instructions peuvent être saisies dans Eos via la ligne de commande. La ligne de commande attend que les instructions soient saisies dans une structure, ou syntaxe, spécifique. En général, l'ordre de la syntaxe peut être décrit comme : Qu'essayez-vous d'affecter ? (Channel, group) — Que voulez-vous qu'il fasse ? (changer l'intensité, le focus, le pan/tilt) — Quelle valeur voulez-vous ? (Intensité à full, Iris à 50).</cite>
- <cite>La plupart des autres fonctions sont des modificateurs de ces trois étapes de base. En travaillant avec des Record Targets, la syntaxe est similaire.</cite>
- **Confiance** : A — remplace la confirmation C de la vague 30, désormais du niveau le plus solide possible pour une règle aussi structurante

## 168 — RÉPONSE DIRECTE à la question de Cy : le focus suit le Tab/Display actif, mécanisme précisé (A)

- <cite>Quand vous appuyez sur [Tab] de façon répétée, le focus se déplace numériquement à travers tous les tabs ouverts sur les workspaces actifs.</cite>
- <cite>Tous les tabs d'affichage et de contrôle ont des numéros de tab fixes (par exemple, "Live" ouvre sous le Tab 1, "Patch" sous le Tab 12, "Color Picker" sous le Tab 27).</cite>
- **Table de correspondance officielle Tab → Display, la plus importante trouvée à ce jour** :
```
1  Live/Blind          11 Show Control      21 Curves             31 Lamp Controls
2  Playback Status      12 Patch             22 Intensity Palettes 32 Channels In Use
3  Magic Sheet          13 Effects           23 Focus Palettes     33 Color Path
4  Direct Selects        14 Magic Sheet List  24 Color Palettes     34 (non utilisé)
5  ML Controls          15 Submaster List    25 Beam Palettes      35 Fader List
6  Effect Status        16 Cue List          26 Presets            36 Fader Configuration
7  Keys                 17 Groups            27 Color Picker       37 sACN Output View
8  Effect Channels      18 Macros            28 Virtual Faders     99 Diagnostics
9  Pixel Maps           19 Snapshots         29 About              100 User Manual
10 Pixel Preview        20 Park              30 Command History
```
- **Confiance** : A
- **RÉPONSE DIRECTE à ta question "peux-tu ajouter l'envoi vers la bonne page"** : oui, la commande officielle est `[Tab] [n] Enter` où n est le numéro de tab cible — confirmé exhaustif ci-dessus. Exemple pour forcer le focus logique sur Patch avant une commande de patch : `Tab 12 Enter`.
- **Nuance capitale, réponse à l'inquiétude posée plus tôt sur focus visuel vs focus logique** : <cite reformulé>"draw focus" est le terme employé constamment dans le manuel — presser une touche, toucher un tab, ou taper `[Tab][n]` "tire" le focus vers cet affichage. Rien dans le manuel ne suggère qu'il existe un focus logique distinct de l'affichage visible — ce sont le même mécanisme.</cite> **Ceci répond à l'incertitude que j'avais signalée avant de faire cette recherche : le focus logique ET l'affichage suivent la même mécanique de Tab, il n'y a pas de préfixe de commande séparé qui changerait le contexte sans changer aussi l'affichage.**

## 169 — Confirmation des raccourcis d'accès direct par double-pression de touche de Record Target (A)

- <cite>Les affichages Blind des record targets (aussi appelés "listes") peuvent être rapidement accédés en pressant deux fois le bouton du record target (par exemple, [Cue][Cue] ouvre l'index de la cue list).</cite>
- **Confiance** : A
- **Impact** : donne une alternative plus courte à `Tab [n] Enter` pour certains cas — `[Patch][Patch]` n'est cependant pas listé explicitement comme raccourci ici (Patch a son propre raccourci dédié `[Address/Patch]` en double-tap, déjà noté vague 33 #166)

## 170 — Confirmation A de la structure Workspaces > Frames > Tabs > Displays

- <cite>Workspaces offre un contrôle d'affichage indépendant sur tous les moniteurs connectés. Chaque moniteur peut avoir jusqu'à trois workspaces. Chaque workspace peut avoir jusqu'à quatre frames. Chaque frame peut contenir plusieurs tabs. Chaque tab contient un display.</cite>
- Accès direct à un workspace : `{Workspace}` softkey après `[Displays]`, puis taper 1, 2, ou 3
- **Confiance** : A — clarifie une hiérarchie qui n'était pas formalisée dans le corpus jusqu'ici, pertinent si le traducteur doit un jour gérer des configurations multi-moniteurs

## 171 — Précisions officielles sur Enter et commandes auto-terminées (A, complète la grammaire de fond)

- <cite>Certaines commandes sont auto-terminées et ne nécessitent donc pas que [Enter] soit pressé. Certaines de ces commandes sont : Out, +%, -%, Level, Actions depuis les direct selects.</cite>
- **Confiance** : A
- **Impact pour le traducteur** : nuance importante à la règle Objet-Action-Cible — toutes les commandes ne nécessitent pas `Enter` en fin de séquence. Une liste (même partielle) de commandes auto-terminées est utile pour éviter de générer un `Enter` superflu, ou pire, l'omettre là où il est nécessaire.

## 172 — Confirmation A de la définition Channel = Fixture, structurante pour tout le corpus

- <cite>Un channel est un unique nom numérique utilisé par Eos pour contrôler un dimmer, un groupe de dimmers, un dimmer et un appareil, ou un fixture complet de type moving light. Eos traite fixtures et channels comme une seule et même chose. Contrairement aux anciennes consoles ETC où un fixture occupait un channel par paramètre, Eos assigne à chaque fixture un unique numéro de channel — les paramètres individuels sont ensuite associés à ce channel.</cite>
- **Confiance** : A
- **Impact** : clarifie et formalise ce qui était implicite dans tout le corpus depuis le début — utile comme définition de référence pour le glossaire du traducteur

## 173 — Confirmation exacte de la syntaxe `1 Thru 100 At 100` — cohérente avec ce que Cy a montré, contextualisée dans "Advanced Manual Control"

- Le manuel confirme, dans la table des matières et par la structure Objet-Action-Cible, que la syntaxe montrée par Cy suit exactement ce squelette : **Objet** = `1 Thru 100` (plage de channels), **Action** = implicite dans le contexte Patch (assigner une adresse), **Cible/Valeur** = `At 100`
- Ceci est cohérent avec la découverte indépendante de Cy et la confirme une fois de plus dans le cadre de la grammaire générale officielle

## 174 — Table complète des indicateurs de couleur et texte en Live/Blind (A, très riche, jamais capturée avant)

Cette section est une mine d'information jamais explorée dans le corpus. Extraits les plus pertinents pour un futur validateur/afficheur dans ton outil :

- **Couleurs de niveau** : Rouge vif = donnée manuelle (même User ID) ; Rouge foncé = donnée manuelle (autre User ID) ; Bleu = intensité plus haute que cue précédente / NP en mouvement ; Vert = intensité plus basse / marqué en referenced mark ; Magenta = inchangé (tracké) ; Blanc = bloqué ; Blanc souligné = auto-bloqué ; Gris = défaut/valeur nulle ; Jaune = donnée d'un submaster
- **Indicateurs texte** : `A`/`a` = asserted (cue entière / partiel) ; `B`/`b` = blocked ; `I` = channel contrôlé par sub inhibitif ou grandmaster (ou intensity block en Flags) ; `IP`/`CP`/`FP`/`BP` = référence à une palette (Intensity/Color/Focus/Beam) suivie du numéro ; `M`/`m` = mark (stocké/non stocké) ; `MK` = marqué pour une cue ultérieure ; `N` = valeur nulle ; `P` = parked ; `Ph` = preheat ; `Pr` = référence à un preset ; `R` = override manuel de référence ; `S` = stocké sur sub shielded
- **Confiance** : A
- **Impact potentiel pour ton architecture** : si ton outil doit un jour lire l'état de la console (pas seulement écrire des commandes), cette table d'indicateurs est la référence pour interpréter l'affichage — pertinent pour la piste de "validation post-envoi" évoquée en vague 28 (lecture du flag d'erreur `/eos/out/cmd`), qui pourrait s'étendre à une lecture d'état plus large.

---

## Synthèse — apports de cette vague (réponse directe à la question de Cy + grosse moisson structurelle)

1. **Réponse directe confirmée** : `[Tab] [n] Enter` est la commande officielle pour forcer le focus vers un display donné — table complète des 37 tabs numérotés fournie
2. **Clarification majeure** : focus logique et affichage visuel sont le même mécanisme dans la doc officielle ("draw focus") — pas de distinction cachée entre les deux comme on se le demandait
3. **Règle Objet-Action-Cible passée de confiance C à A** — citation officielle exacte trouvée
4. **Liste des commandes auto-terminées** (sans besoin d'Enter) — nuance utile pour la génération
5. **Table exhaustive des indicateurs Live/Blind** — ouvre une piste pour une future fonctionnalité de lecture d'état, pas seulement d'écriture de commande

## Mise à jour à porter à la grammaire consolidée

- Ajouter la table Tab→Display complète en référence
- Confirmer/renforcer à A la règle Objet-Action-Cible déjà notée
- Ajouter la clarification focus logique = focus visuel (répond à l'incertitude posée avant recherche)

<!-- ===== FIN : vague34_operations_manual_focus_tabs.md ===== -->

---

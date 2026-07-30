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
- **Explication analogique fournie par un contributeur** : <cite reformulé>le comportement est similaire à ce qui se produit si on appuie sur un bouton Direct Select de macro pendant qu'on édite une autre macro — la macro déclenchée ne se joue pas, elle est ajoutée au contenu de la macro en cours d'édit

# Grammaire ETC Eos consolidée — référence pour le traducteur NL → macro

Document de synthèse **définitif**, construit à partir de l'ensemble des sources du
dépôt : le corpus de collecte (174 entrées, `corpus/CORPUS_EOS_COMPLET.md`), le manuel
officiel complet (`manuals/operations-manual/`, 32 chapitres, Eos Family User Manual
v3.2.0), les 9 workbooks (`manuals/*-workbook/`), les documents OSC officiels
(`manuals/osc-integration/`, `reference/Supported_OSC_Commands.md`), la table
canonique des touches (`reference/eosKeys.ts`, croisée avec le manuel dans
`reference/eosKeys_vs_manual_comparison.md`), et le journal terrain
(`reference/JOURNAL_observations_nomad.md`).

Ce document **remplace** la section « GRAMMAIRE CONSOLIDÉE » de `corpus/CORPUS_EOS_COMPLET.md`
comme référence à jour — celle-ci reste en place comme trace d'audit historique (elle a été
écrite avant l'import du manuel complet et contient des zones d'incertitude désormais résolues).

**Niveaux de confiance utilisés** : **S** (observation terrain protocolée, la plus fiable)
> **A** (manuel officiel v3.2.0, workbooks officiels, documents OSC officiels) > **B**
(réponse officielle ETC en forum/blog) > **C** (communauté, cohérent mais non testé) > **D**
(signal négatif ou non fiable).

---

## 1. Principe syntaxique fondamental : Objet → Action → Cible

**Confirmé A** (Eos Family User Manual v3.2.0, section « Important Concepts » ;
recoupé indépendamment par le corpus, vague 30 #156 puis vague 34 #167) :

> La plupart des instructions suivent la structure : (1) Qu'essayez-vous d'affecter ?
> (channel, group) — (2) Que voulez-vous qu'il fasse ? (changer l'intensité, le focus,
> le pan/tilt) — (3) Quelle valeur voulez-vous ? (intensité à full, iris à 50).

Avec les Record Targets, la syntaxe est similaire. La plupart des autres fonctions sont
des **modificateurs** de ces trois étapes. Toutes les actions ne passent pas par la ligne
de commande — certaines la contournent entièrement (softkeys, direct selects, encodeurs).

**Commandes auto-terminées** (n'ont pas besoin de `[Enter]`, confirmé A) : `Out`, `+%`,
`-%`, `Level`, actions depuis les direct selects.

**`[Enter]` termine la ligne de commande**, pas la sélection de channels — la sélection
reste active pour la commande suivante jusqu'à ce qu'une nouvelle sélection soit faite.

---

## 2. Sélection de channels

### 2.1 Syntaxe de base

```
1                          → sélectionne le channel 1
1 Thru 10                  → sélectionne les channels 1 à 10
1 Thru 10 + 15             → ajoute le channel 15 à la sélection
1 Thru 10 - 5              → retire le channel 5 de la sélection
Group 3                    → sélectionne le groupe 3 (tous ses channels)
Group 3 + 1 Thru 6         → groupe 3 ET channels 1-6 (confirmé par test transport,
                              non confirmé au banc réel — cf. reference/tools/README.md)
```

- `Group` sélectionne des channels — **il ne contient jamais de niveaux**, contrairement à
  une palette (corpus #058, #082 A/B — distinction Group/Palette confirmée par ETC).
- `[Group][Color Palette][1]` sélectionne tous les channels ayant des données dans la
  palette couleur 1 (sélecteur pur, ne modifie pas les valeurs).
- `[Group][Preset][xx]` sélectionne les channels associés au preset **et** les place à
  leur valeur IFCB enregistrée ; `[Group][Preset][xx][At][0]` sélectionne seulement.

### 2.2 Select_Active / Select_Last

- `Select_Active` (`SELECT_ACTIVE`, confirmé A eosKeys.ts) — sélectionne tous les channels
  actifs (intensité > 0 ou en mouvement).
- `Select_Last` (`SELECT_LAST`) — rappelle la dernière sélection. Pattern de boucle
  confirmé (corpus #057) : `SelectLast Record Group N Enter Next` pour créer des groupes
  en série sans redéfinir la sélection à chaque fois.
- `select_last_params @ +01 Enter` (`SELECT_LAST_PARAMS`) — incrémente/décrémente le
  dernier paramètre travaillé (corpus #098, C).

### 2.3 Query — grammaire complète (confirmée A, manuel v3.2.0 §15 « Advanced Manual Control »)

`[Query]` sélectionne les channels remplissant un critère conditionnel. C'est le **seul**
endroit du langage Eos où existe une forme de logique conditionnelle/négation (confirmé
définitivement par ETC — corpus vague 30 #155 : pas de `Not` générique ailleurs).

**Liste complète des conditions Query disponibles** (source A, jamais entièrement listée
avant dans le corpus) :
`Is In` · `Isn't In` · `Can Be` · `Can't Be` · `Or` · `Moves Only` · `Unpatched` ·
`Mark` (cue où l'intensité est active) · `Less Than` (inclut égal) · `Greater Than`
(inclut égal) · `Broken Mark` · `Marking` (cue future) · `Track` · `Up Moves` ·
`Down Moves` · `Live Moves` · `Dark Moves` · `Autoblock` · `Block` · `Assert` · `Part` ·
`Park` · `Time` · `Delay` · `Capture`.

> Par défaut, une requête Query s'applique à la sortie courante — l'usage de `{Is In}`
> est donc optionnel.

Exemples officiels :
```
Query <Is In> Color Palette 2 At 50 Enter
Query {Isn't In} Beam Palette 25 Enter
Query {Accessory} {Can Be} Color Palette 8 Enter
Query {Unpatched} Delete Enter Enter        (ne fonctionne qu'en Patch)
Query {Fixture Type} {Revolution} {Can Be} Focus Palette 6 {Isn't In} Cue 4 Thru 9 Enter
```
`[Next]`/`[Last]` permettent de parcourir le résultat d'une query un channel à la fois.
Des mots-clés personnalisés définis en Patch (jusqu'à 10 par channel) peuvent aussi servir
de critère : `Query {votre mot-clé} {Can't Be} {Beam Palette 5} Enter`.

⚠️ Piège confirmé (corpus #083, C) : `{Select Last}` après une Query composée relance la
syntaxe de la requête au lieu de renvoyer la sélection résultante.

---

## 3. Patch

Syntaxe fondamentale confirmée A (manuel §4) :
```
601 At 250 Enter                 → patche l'adresse 250 au channel 601
602 At 657 Enter
603 At 2 / 146 Enter              → 2e univers, adresse 146
604 Thru 610 At 101 Enter         → patch en masse séquentiel (mécanisme Fan)
611 At 108 Thru 111 Enter         → patch une plage d'adresses à UN channel (crée des parts)
612 Thru 620 At 201 {Offset} 3 Enter   → cyclorama 3 cellules
```
- `[Data]` bascule l'affichage entre adresse de sortie et port/offset.
- `[601] [At] [Enter]` — retire l'adresse (garde le type).
- `[602] {Unpatch} [Enter]` — restaure aux propriétés par défaut (retire adresse, type,
  label...).
- `[Delete] [603] [Enter]` — supprime tout le channel du show.
- **Deux modes de patch** : Patching By Channel (défaut) / Patching By Address, bascule
  via `[Format]`.
- Le spread `Thru`/`At` en Patch calcule automatiquement l'adresse de chaque channel selon
  l'empreinte DMX (footprint) du fixture — **pas forcément +1** si le fixture occupe
  plusieurs canaux DMX (corpus #164, A).

⚠️ **Polysémie contextuelle confirmée (corpus vague 32/33, source S puis B)** : `At` et
`@` changent de sens selon l'écran actif — adresse DMX en Patch, niveau d'intensité en
Live. **Le traducteur doit connaître le contexte d'écran actif avant de générer `At`.**
Réponse officielle (corpus #167-168, A) : `[Tab] [n] Enter` force le focus/contexte vers
l'écran cible ; le focus logique et l'affichage visuel sont le **même** mécanisme
(« draw focus »). Table des tabs utiles : Live/Blind=1, Patch=12, Effects=13, Cue List=16,
Groups=17, Macros=18, Snapshots=19, Palettes=22-25, Presets=26, Color Picker=27.

---

## 4. Fan — répartition automatique de valeurs (confirmé A, manuel §8)

**Découverte structurelle majeure (corpus vague 26, confirmée et détaillée ici)** : Fan
n'est **pas** une commande séparée — c'est le comportement **implicite** de toute commande
de niveau/temps utilisant `[Thru]` ou une liste de références. La touche `[Fan]` ne sert
qu'à changer de **style** de répartition parmi ceux disponibles.

**Styles de Fan confirmés** (corpus #150 via eosKeys.ts + manuel, syntaxe complète) :

| Style | Comportement |
|---|---|
| `{Center}` | Le channel du milieu reste inchangé, les extrêmes varient dans des directions opposées |
| `{Reverse}` | Inverse l'ordre de sélection avant d'appliquer le fan |
| `{Mirror Out}` | Le milieu = point de départ, les extrémités = points d'arrivée |
| `{Mirror In}` | Inverse de Mirror Out |
| `{Repeat}` | Motif répété toutes les N channels |
| `{Cluster}` | Channels regroupés en paquets de valeur identique |
| `{Random}` | Ordre randomisé avant application du fan |
| `{Interleave}`, `{Jump}`, `{Num Groups}`, `{Channels Per Group}`, `{Curve}` | confirmés dans eosKeys.ts, syntaxe/comportement détaillé non capturé |

Exemples confirmés A :
```
1 Thru 10 At 10 Thru 30 Fan {Mirror Out} Enter
  → channel 1=30%, 2=20%, 3=10%, 4=20%, 5=30% (sur 10 channels, motif symétrique)

1 Thru 12 At 50 Thru 70 Fan {Repeat} 3 Enter
  → channels 1,4,7,10=50% ; 2,5,8,11=60% ; 3,6,9,12=70%

1 Thru 12 At 50 Thru 80 Fan {Cluster} 4 Enter
  → channels 1-3=50%, 4-6=60%, 7-9=70%, 10-12=80%

1 Thru 5 Fan Enter              → met encodeurs/molette en mode fan sans valeur figée
```

---

## 5. Palettes & Presets

Syntaxe normative de Record (confirmée A, manuel §10-11, corpus #041) :
```
Record Color Palette 4 Label FOH Blue Enter
```
- Numérotation 0.001 à 9999.999, chacune labellisable.
- `[Record]` stocke toutes les données pertinentes non-défaut ; `[Record Only]` stocke
  uniquement les valeurs ajustées manuellement (distinction fondamentale).
- Filtre par catégorie/paramètre : `[Color] [Record] [Target]` ou `[-] [Intensity] [Record] [Target]`.
- `{By Type}` `{Lock}` — palette applicable à tout fixture du même type, verrouillée.
- **Piège récurrent** (référence/absolu, corpus #042 C) : copier un channel réglé sur une
  palette copie la **référence**, pas le contenu, sauf `make_absolute`/`{From Absolute}`.
- `Move To` (`[Copy To][Copy To]`) — déplace les données au lieu de les copier, écrase la
  cible après confirmation.

**Syntaxe gel confirmée A** (corpus vague 31, workbook L1) :
```
Chan 4 Color 3/195 Enter    → applique Lee 195 (bibliothèque 3 = Lee)
```
⚠️ Limite documentée (corpus #159, C multi-sources) : le rendu du gel picker est une
**approximation**, pas garanti fidèle à la teinte physique réelle — à présenter comme
point de départ, pas résultat garanti.
Convention OSC distincte pour les gels (confirmée A, `Eos_Integration_via_OSC.md` +
`Supported_OSC_Commands.md`) : chaîne `<initiale fabricant><numéro>`, ex. `"L2"` (Lee 2),
`"R80"` (Rosco 80), `"AP1150"` (Apollo 1150), `"G101"` (Gam 101), `"T12"` (TokyoBS).

---

## 6. Effets

Distinction fondamentale (confirmée A, manuel §18, corpus #023) :
- **Step-Based/Chase** : channels/groupes attachés directement aux steps.
- **Absolute** : channels assignés séparément, chaque step référence une palette via `{Action}`.

Recettes officielles confirmées (corpus vague 6, source A — support.etcconnect.com) :
```
Effect 1 Enter {Step Based} {Step} 1 Thru 10 Enter Enter
  1 Thru 10 [Page Right] [assigner channels aux steps]
  → chase simple

Effect 1 Copy To 2 Enter {Attributes} {Build}     → chase en construction
Effect 1 Copy To 3 Enter {Attributes} {Bounce}    → chase aller-retour
Effect 4 Enter {Linear} {Parameters}{Intensity} {Size} 100 Enter
  1 Thru 10 Effect 4 Enter                        → fondu linéaire fluide

1 Thru 10 {Offset} {Mirror Out} Effect 4 Enter    → offset depuis le centre
1 Thru 10 {Offset} {Mirror In} Effect 4 Enter     → offset vers le centre

[Effect][Effect] → {Absolute}
{Action} 1 → Color Palette 1
{Action} 2 → Color Palette 2                       → chase couleur absolu

{Action} 1 Thru 7 @ Color Palette x Thru y Enter    → assignation en masse N steps → N palettes
                                                       (meilleur exemple de génération en masse du corpus)
```
`{Grouping}` (paramètre numérique) fait alterner les fixtures par sous-groupes en unisson.

---

## 7. Cues & Cue List

- `Chan 1 At 50 Cue 5 Time 20` — exemple canonique de la grammaire Objet-Action-Cible.
- `Go To Cue Out Time 0 Enter` — aller à Cue Out avec temps forcé (corpus #031, A).
- **Tracking vs Cue Only** (défaut Tracking, confirmé A, White Paper Control Philosophy +
  manuel) : une donnée trace en avant jusqu'à nouvelle move instruction. `[Cue Only/Track]`
  inverse le comportement par défaut pour une cue donnée.
- `{Trace}` fonctionne comme Tracking mais **en arrière** ; `{Trace}{Trace}` force au-delà
  du premier obstacle.
- **Block** = convention d'édition (n'affecte pas le playback) ; **Assert** = force le
  playback d'une valeur trackée/bloquée. Peut être posé au niveau cue, part, channel, ou
  paramètre.
- Sortie de séquence (`Go To Cue`, un Link, ou changement manuel de pending) : **tout** le
  contenu de la cue (moves ET tracks) est asserté — comportement standard des consoles
  tracking, confirmé A (White Paper).
- `HTP`/`LTP` : Eos = **LTP par défaut pour l'intensité en cue list**, HTP disponible en
  option. Submasters = **HTP par défaut**, LTP disponible en option. NPs toujours LTP.

---

## 8. Mark / Auto-Mark

- Syntaxe directe : `[Mark] [6] [.] [9] [9] [Enter]` → prompt de création de cue de mark,
  crée automatiquement la cue 6.99 et y effectue le marking.
- **AutoMark** (confirmé A + C détaillé, corpus #117) : quand une cue fait passer un
  projecteur de 0 à actif avec un mouvement NP simultané, la console exécute ce mouvement
  NP **dans la cue précédente**. Indicateur `M` dans les flags.
- **Referenced Mark** (confirmé A, manuel — jamais aussi précis dans le corpus) : deux
  parties — la **cue marquée** (flag utilisateur, où les NP changent) et la **cue source**
  (intensité, où les moves NP sont réellement stockés). Il faut spécifier les channels à
  marquer dans la cue source.
- ⚠️ Piège confirmé (corpus #118, C, contredit la doctrine générale) : `{Enable}/{Disable}`
  sur le marking se comporte encore comme un **toggle** en macro, malgré la doctrine
  officielle générale (#074, A) qui dit le contraire pour les autres cas.
- ⚠️ `[Blind] [Enter]` non qualifié est ambigu en macro — toujours préciser `[Blind] [Cue]`
  ou `[Blind] [Sub]` (corpus #119, C).

---

## 9. Submasters & Faders

- `SubDown <n> Enter` / `SubUp <n> Enter` — confirmé A (eosKeys.ts : `SUB_BUMP_DOWN`/`SUB_BUMP_UP`).
- ⚠️ **RISQUE MAJEUR NON RÉSOLU** (corpus #027, C, prioritaire au banc) : une macro pilotant
  un bump submaster pourrait ne pas survivre à l'export/import ASCII.
- **Proportional** (défaut) vs **Intensity Master** : en mode Intensity Master, le bump
  devient une touche de mark plutôt qu'un flash.
- **Shielded** (priorité absolue, même sur Grand Master, v1.9.6+) vs **Inhibitive** (limite
  proportionnelle la sortie live, comme un grand master local) — corpus #086-087, A/C.
- **Assert n'a pas de mot-clé de ligne de commande** (confirmé S, journal terrain) :
  `/eos/newcmd "Sub n Assert#"` échoue en erreur de syntaxe. Contournement OSC spécifique :
  `/eos/user/1/fader/1/<n>/stop` réalise la fonction Assert pour un sub piloté par banque
  de faders OSC.
- Feedback de niveau : **pas de republication spontanée** sur `/eos/sub/<n>` — confirmé S
  au banc (journal terrain, silence total après changement). Le feedback passe par les
  **banques OSC** (`/eos/fader/<bank>/<n>`), avec un délai documenté officiellement à 3 s
  (`Supported_OSC_Commands.md`, 2017) mais mesuré à ~522 ms sur nomad 3.3.5.69 en 2026.

---

## 10. Macros — syntaxe complète (confirmé A, manuel §24)

### 10.1 Deux voies de création
1. **Learn** (méthode primaire recommandée) : `[Learn] [n] [Enter] <séquence> [Learn]`.
   Tout s'enregistre, y compris `[Clear]` en cas d'erreur (pollue, n'est pas exclu).
2. **Éditeur de macro** (`[Macro][Macro]` ou `[Tab][18]`) : édition/création directe,
   secondaire/corrective selon la doctrine ETC.

Touches **exclues** du Learn : `[Macro]`, flèches, `[Escape]`, `[Select]`, `[Learn]`.

Exemples officiels :
```
Learn 1 Enter Go To Cue Out Time 0 Enter Learn
Learn 5 Enter 1 Full {Chan Check} Enter Learn
Learn 4 Enter -Sub Record Learn                → exclut les données de submaster
Learn 2 Enter -Group 6 {Color} Record Learn    → exclut la couleur du groupe 6
```

### 10.2 Enchaînement de macros (confirmé A, manuel — clôt la question du corpus)

**Une macro peut en appeler une autre par simple juxtaposition en fin de contenu**
(corpus #070, confirmé A ; nuance opérationnelle #095, C — fiabilité d'exécution non
garantie selon contexte, prioritaire au banc) :
```
Macro 3: {Edit} Select Active At 5 Enter Sneak Time 10 Enter Macro 5 Enter Select
```

### 10.3 Softkeys de contrôle (confirmé A)

| Softkey | Fonction |
|---|---|
| `{Loop Begin}` | 0 itérations = boucle infinie |
| `{Loop End}` | ferme la boucle |
| `{Wait}` | pause, doit être suivi d'un **entier** de secondes |
| `{Wait for Enter}` | pause jusqu'à `[Enter]` |
| `{Delete}` | softkey de suppression — **jamais** la hardkey `[Delete]` |

### 10.4 Modes Foreground/Background/Default (confirmé A, corrigé corpus vague 29)

Ce sont **trois touches OSC distinctes**, pas un cycle sur un seul softkey :
`foreground_mode`→`MACRO_USER`, `background_mode`→`MACRO_BACKGROUND`,
`default_mode`→`MACRO_DEFAULT_MODE`, plus `macro_mode`→`MACRO_MODE` (sélecteur général).

- **Foreground** : posté sur ligne de commande, tous les appareils du même User.
- **Background** : non posté, appareil appelant seul.
- **Default** : Foreground si appel manuel, Background si appel système (cue, show control).

**Règle de génération retenue : Foreground par défaut**, sauf raison explicite — couvre
plusieurs risques déjà identifiés (`Go_To_Cue`, `{Target}` vers un User qui ne fonctionne
qu'en Foreground, corpus #068).

### 10.5 Métadonnées de macro (confirmé A)

`[Label]` · `{Icon}` · `{Color}` (Red/Green/White/Dark) · `{Toggle Blink}` ·
`{Target}` (Device ou User ID) · `{SC Learn}` (exclusion de l'apprentissage show control).

### 10.6 Risque de sécurité fonctionnelle (confiance C, corpus #067)

Édition de macro en cours (Tab 18) + macro background déclenchée en parallèle → les
commandes de la macro background **s'insèrent dans l'édition en cours** au lieu de
s'exécuter en arrière-plan. **Ne jamais déclencher de macro via l'app pendant qu'une
édition de macro est en cours sur la console.**

> **Corrigé le 2026-08-06** : cette section affichait « confirmé S » — le niveau de
> confiance le plus élevé du projet, réservé à l'observation terrain protocolée. L'entrée
> source, corpus #067, est en réalité étiquetée **C** (« décrit avec précision, non résolu
> dans le fil consulté ») : un témoignage de forum sérieux, mais pas une observation
> confirmée. L'erreur avait été copiée telle quelle dans `REGLES_POUR_UI.md` sans être
> revérifiée contre le corpus — voir `PLANNING.md` #37. La recommandation elle-même
> (ne jamais déclencher de macro pendant une édition en cours) reste une précaution
> raisonnable, mais elle ne s'appuie pas sur une preuve de niveau S.

---

## 11. Show Control / OSC — adresses fondamentales

### 11.1 Déclenchement de macro (confirmé A, manuel §31 « OSC Macro » + journal S)

```
/eos/macro=<n>              → sélectionne une macro
/eos/macro/fire=<n>         → exécute la macro n
/eos/macro/<n>/fire=1.0     → exécute avec argument de front de bouton (1.0=appui, 0.0=relâchement)
```
C'est l'adresse **normative** pour le moteur d'injection OSC de macro2eos.

### 11.2 Ligne de commande générique

```
/eos/cmd="Chan 1 At 75 Enter"      → construit et exécute une ligne de commande
/eos/newcmd="..."                  → identique mais réinitialise la ligne de commande d'abord
```
Substitution d'argument : `/eos/cmd="Chan %1 At 75"`.
Terminaison : soit le mot `Enter` littéral dans la chaîne, soit `#` en fin de chaîne selon
contexte (Serial String/ASCII), soit `\r`/hex 0D pour les chaînes String Input.

### 11.3 Touches à état

```
/eos/key/<nom>              → simule l'appui d'une touche (voir reference/eosKeys.ts, 1155 entrées)
/eos/param/<parameter>/home → remise à la valeur par défaut d'un paramètre nommé
/eos/user/1/wheel/coarse/<param>   → rotation molette nommée normale
/eos/user/1/wheel/fine/<param>     → rotation en précision
```

### 11.4 Ciblage utilisateur

`/eos/user/<n>/...` cible un utilisateur spécifique. Recommandation confirmée B (corpus
#066) : réserver un User# dédié pour tout client OSC externe dès la connexion, plutôt que
d'hériter du user de la console primaire.

### 11.5 Send_String — règles non négociables (bugs à tickets ETC confirmés B/A)

- **[EOS-55864]** : `Send_String` doit toujours être en **dernière position** d'une macro
  multi-lignes (sinon `/r` parasite dans l'adresse OSC générée).
- **[EOS-53576]** : insérer un `Macro_Wait` entre plusieurs `Send_String` consécutifs si
  la macro peut être déclenchée depuis un Client (pas la Primary) — risque de fusion en un
  seul paquet UDP malformé.

### 11.6 Validation post-envoi (piste d'architecture confirmée S, corpus #140)

`/eos/out/cmd` et `/eos/out/user/<u>/cmd` diffusent la ligne de commande en clair avec un
**flag d'erreur** (1=erreur de syntaxe, 0=ok, Eos 2.6.0+). C'est un mécanisme de validation
en temps réel exploitable : envoyer une commande de test, observer le flag, alerter
l'utilisateur avant de graver la macro — complémentaire à la validation statique pré-envoi.

### 11.7 Référence exhaustive

Voir `manuals/operations-manual/31-show-control.md` (dictionnaire complet officiel,
section « Eos OSC Keys »), `reference/Supported_OSC_Commands.md` (table par version
minimale requise), `reference/eosKeys.ts` (1155 touches, croisées à 99,7% avec le manuel).

---

## 12. Absences structurelles confirmées (valident l'architecture du projet)

- **Pas de variables/formules natives** (confirmé A/B, ETC, feature request sans suite
  depuis 2010+) — l'indirection macro-dans-macro reste le seul palliatif disponible sur
  la plateforme, pas une solution de second choix.
- **Pas d'auto-palette native** (confirmé A/B, ETC, choix de conception assumé et stable
  depuis 2010) — raison donnée par ETC : la génération purement automatique produirait un
  résultat jugé peu utile (organisation/ordre des palettes jugés essentiels au métier).
  **Valide directement** la stratégie de validation utilisateur avant envoi déjà retenue
  pour macro2eos.
- **Pas de négation générale hors du sous-système Query** (confirmé B, réponse support ETC
  directe) — toute logique conditionnelle du traducteur doit passer par Query, nulle part
  ailleurs.

---

## 13. Stratégies de génération en masse (3, pas 4 — correction du corpus)

1. **Spread par plage `[Thru] x [Thru] y`** — le mécanisme **Fan lui-même**, appliqué par
   défaut sans invocation explicite (cf. §4). Le plus fiable, confirmé A.
2. **Boucle `Macro_Loop_Begin`/`Select_Last`/`Next`** — flexible, pour séquences non
   linéaires (corpus #057).
3. **Indirection macro-dans-macro** — syntaxe confirmée A (§10.2), fiabilité d'exécution
   encore C (à tester au banc).

---

## 14. Référentiel de risques — résumé (détail complet dans le corpus)

| Commande/mécanisme | Risque | Confiance |
|---|---|---|
| `{Enable}/{Disable}` sur le marking | Comportement toggle malgré la doctrine générale | C |
| `Update` | Cible ambiguë + préférence persistante entre sessions (Make Absolute/Break Nested) | A/C |
| `SubDown`/`SubUp` | Survie à l'export ASCII non confirmée | C — prioritaire banc |
| `Go_To_Cue` | Non déterministe selon Foreground/Background + timing | C |
| `{Target}` vers un User | Fonctionne uniquement en Foreground | C |
| Édition de macro concurrente + macro background | Corruption silencieuse du contenu en cours d'édition | S |
| Macro-dans-macro | Syntaxe A, fiabilité d'exécution C | A/C — prioritaire banc |
| `Send_String` en macro multi-lignes | `/r` parasite sauf en dernière position | B/A |
| `Send_String` multiples depuis un Client | Fusion UDP malformée sans `Macro_Wait` | B |
| `[Blind] [Enter]` non qualifié | Ambigu, toujours qualifier l'objet cible | C |
| Assert | Pas de mot-clé `newcmd`/`cmd` — fonction hardkey uniquement | S |
| `duration` (OSC key) | Deux commandes internes différentes selon contexte — possible polysémie non résolue | À trancher au banc |
| `console_settings`/`desk_settings` | Dérive de terminologie entre versions, alias non confirmé | À trancher au banc |

Détail complet, sources exactes et citations : `corpus/CORPUS_EOS_COMPLET.md`,
section « REFERENTIEL_RISQUES_ET_GRILLE ».

---

## 15. Ce qui reste à valider au banc réel (priorités, mise à jour)

1. `SubDown`/`SubUp` — survie export/import ASCII
2. Macro-dans-macro — fiabilité d'exécution réelle selon contexte
3. `{Enable}/{Disable}` sur le marking — toggle vs absolu confirmé en usage réel
4. `Group 5 + 1 Thru 6` (combinaison groupe + plage de channels) — syntaxe testée en
   transport seulement (`reference/tools/test-client3.ts`), jamais confirmée au banc
5. `Record ... Label <texte multi-mots>` — comportement du clavier virtuel avec espaces/tiret
6. Ambiguïté `duration` (OSC) et dérive `console_settings`/`desk_settings`
7. Styles de Fan `{Interleave}`, `{Jump}`, `{Num Groups}`, `{Channels Per Group}`, `{Curve}` —
   noms confirmés, comportements jamais testés

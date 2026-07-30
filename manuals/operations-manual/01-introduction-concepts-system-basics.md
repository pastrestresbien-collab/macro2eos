# Eos Family Operations Manual v2.7.0 — Conversion .md (Partie 1/N)

Source officielle ETC : https://media.musson.com/mti/docs/e/o/eosfamily_v2.7.0_operationsmanual_reva.pdf
Confiance : A
Couverture de cette partie : Introduction, Important Concepts, Console Overview, System Basics (jusqu'à Encoders)

---

## Introduction

### Conventions du manuel
- Menus et commandes de navigateur : **texte gras**
- Boutons clavier alphanumériques : TOUT EN MAJUSCULES
- Boutons de façade console : **[crochets gras]**, ex. [LIVE] ou [Enter]. Touches optionnelles : <chevrons>, ex. <Cue> ou <Sub>
- Touches à presser/maintenir simultanément : symbole "et", ex. [Load] & [Timing Disable]
- Softkeys et direct selects : **{accolades grasses}**. `<More SK>` toujours optionnel, indiqué une seule fois par instruction quelle que soit la page de softkeys active

### Aide intégrée
- Maintenir [Help] puis presser une touche affiche : nom de la touche, description, exemples de syntaxe, liens vers le manuel

---

## Concepts importants

### Channel = Fixture
Un channel est un nom numérique unique utilisé par Eos pour contrôler un dimmer, un groupe de dimmers, un dimmer + appareil, ou un fixture moving light complet. **Eos traite fixtures et channels comme identiques.** Contrairement aux anciennes consoles ETC (un fixture = un channel par paramètre), Eos assigne un seul numéro de channel par fixture ; les paramètres individuels sont associés au channel comme lignes d'information supplémentaires.

Note : les fixtures multicell sont gérées différemment (multiples channels et adresses).

### Address
Identifiants numériques réglés sur les dimmers/fixtures physiques réels. Le Patch relie adresses et channels. **On peut patcher plusieurs adresses à un seul channel, mais jamais plusieurs channels à une seule adresse.**

### Structure de syntaxe (RÈGLE FONDAMENTALE — confirmée A)
> La plupart des instructions s'entrent via la ligne de commande, dans une structure/syntaxe spécifique. L'ordre général peut se décrire comme :
> 1. Qu'essayez-vous d'affecter ? (Channel, group)
> 2. Que voulez-vous qu'il fasse ? (changer intensité, focus, pan/tilt)
> 3. Quelle valeur voulez-vous ? (Intensité à full, Iris à 50)

La plupart des autres fonctions sont des modificateurs de ces trois étapes de base. Avec les Record Targets, la syntaxe est similaire. Toutes les actions ne passent pas par la ligne de commande — certaines la contournent entièrement.

### Enter et commandes auto-terminées
[Enter] termine une instruction multi-éléments. **Commandes auto-terminées (n'ont pas besoin de [Enter])** : `Out`, `+%`, `-%`, `Level`, actions depuis les direct selects.

### Catégories de paramètres
Quatre catégories majeures : **Intensity** (intensité), **Focus** (pan/tilt), **Color** (roue couleur, CMY, scrollers...), **Beam** (tout paramètre non couvert ailleurs). Les paramètres non-intensité sont appelés NPs (Non-intensity Parameters) dans tout le manuel.

### Record Targets
Un record target est tout emplacement de données stockable via [Record]. Exemples : cues, palettes, macros.

### Cues
Une cue est un record target composé de channels avec données de paramètre associées, timing discret (niveau channel/paramètre), timing de cue, et attributs de cue (preheat, follow, hang...).

### Tracking vs Cue Only
Eos est par défaut une console **tracking** :
- Une fois une donnée dans une cue list, elle y reste à sa valeur d'origine et **trace en avant** à travers les cues suivantes, jusqu'à nouvelle instruction ou suppression via filtre/null
- Un changement dans une cue trace en avant jusqu'à rencontrer une move instruction ou un block

Peut être inversé en "Cue Only" par défaut (Setup). Le bouton `[Cue Only/Track]` inverse le comportement par défaut pour une cue donnée : si console en Tracking, agit comme Cue Only ; si console en Cue Only, agit comme Track.

**Cue Only Mode** : `[Record] <Cue> [3] [Q Only] [Enter]` empêche l'info de tracer vers la cue suivante et protège les niveaux tracking précédents en ajoutant une move instruction dans la cue suivante pour ces niveaux.

### Trace
`{Trace}` fonctionne comme Tracking mais **en arrière** dans la cue list, jusqu'à rencontrer une move instruction. `[Record] <Cue> [3] {Trace} [Enter]`. Pour forcer la nouvelle valeur vers l'arrière même au-delà, `{Trace}{Trace}`.

### Move Instruction / Manual Data / Move Fade
- **Move instruction** : tout changement de paramètre par rapport à sa valeur stockée précédente
- **Manual data** : toute valeur réglée via ligne de commande, reste jusqu'à move instruction
- **Move Fade** (philosophie adoptée par Eos) : les paramètres ne changent pas de leur réglage courant tant qu'une move instruction n'est pas fournie (en cue ou manuellement)

### Cue List Ownership
La propriété d'une cue list sur un channel est déterminée par la cue dont le channel reçoit actuellement sa valeur. En alternant entre cue lists, une liste active ne "possède" pas nécessairement un channel sauf si elle a fourni la dernière move instruction. `Assert` outrepasse ce comportement par défaut. Règle non suivie pour une **out-of-sequence cue** (rappelée via [Go To Cue], une instruction Link, ou changement manuel de la cue pending) : tout le contenu de la cue (moves ET tracks) est asserté.

### Block vs Assert
Sur anciennes consoles ETC, un block traitait une valeur trackée comme move instruction, en édition ET en playback. **Sur Eos, ce comportement est scindé** :
- **Blocked** = convention d'édition uniquement, empêche les instructions trackées de modifier la donnée associée. Aucun impact sur le playback (continue de jouer comme un track)
- **Assert** = force le playback d'une valeur trackée/bloquée
- Assert non disponible sur Element 2

### Live et Blind
- **[Live]** : données affichées = données envoyées par la console à l'instant présent (sur scène)
- **[Blind]** : données affichées = données du record target choisi (cues, presets, palettes...). Modifications non visibles immédiatement sur scène, même si le record target modifié est actif. **Aucun [Record] requis en Blind** — les édits sont stockés dès terminaison de la ligne de commande
- Tout affichage qui n'est pas Live est considéré Blind, LED [Blind] allumée. **Exemple confirmé : ouvrir Patch allume la LED bleue [Blind].**

### HTP vs LTP
- **HTP** (Highest-Takes-Precedence) : le niveau le plus haut de toutes les sources est exécuté. Applicable uniquement à l'intensité. Aussi appelé "pile-on"
- **LTP** (Latest-Takes-Precedence) : la valeur la plus récente reçue est exécutée. Applicable à tout paramètre. Toute nouvelle valeur remplace la précédente, peu importe le niveau fourni
- Cue lists : HTP ou LTP pour intensité uniquement (NPs toujours LTP). Submasters : HTP ou LTP pour intensité, défaut HTP. **Défaut cue list Eos pour intensité : LTP.**
- Eos détermine la valeur LTP d'un channel, outrepassée par toute entrée HTP supérieure, elle-même finalement modifiée par le contrôle manuel

---

## Console Overview (résumé — peu pertinent pour le traducteur macro, gardé pour référence)

- Capacités : jusqu'à 32 768 channels (numérotables de 1 à 99 999), 999 cue lists, 10 000 cues, 1000 groups, 1000×4 palettes (I/F/C/B), 1000 presets, 1000 effects, **99 999 macros**, 1000 snapshots, 1000 curves, 1000 color paths
- Grandmaster : inhibe toutes les valeurs d'intensité live proportionnellement. Blackout : met tous les niveaux à zéro
- Eos Ti : 20 hardkeys personnalisables, défaut macros 801-820. Gio : 9 hardkeys, 8 en macros 801-808, 9e en macro 821. Gio@5 : 20 hardkeys, défaut macros 801-820

---

## System Basics

### CIA (Central Information Area)
Partie basse de l'écran : ligne de commande, affichage de paramètres, browser, softkeys.

**Ligne de commande** : bordée en or en Live, affichée en bleu en Blind. `[Clear]` retire les commandes d'une ligne terminée. `[Shift] & [Clear]` retire les commandes d'une ligne non terminée.

**Recherche de ligne de commande** : icône Search en fin de ligne, ou `[Shift] & [About]` — recherche parmi record targets et channels enregistrés, affiche objet/numéro/label.

### Labels
`[Label]` attache un label alphanumérique. `[Label][Label]` après une commande de record target efface le label courant (y compris labels de showfile).

### Browser
Interface pour sauvegarde/chargement de show, ouverture de displays, etc. `[Displays]` l'ouvre. Focus par toucher n'importe où dans la zone browser du CIA.

**Codes couleur browser** : Save/Save As = vert, Open = rouge, Merge = jaune, New/Clear = rouge

**Clear Functions** : `{Clear}` depuis browser → fenêtre de sélection des record targets à effacer. ⚠️ **Ne peut pas être annulé par Undo.**

**Reset System vs Clear Show** : `{Reset System}` ouvre nouveau show + reset Setup aux défauts. `{Clear Show}` ouvre nouveau show seulement.

**Patch 1 to 1 vs Clear Patch** : `{Patch 1 to 1}` efface le patch et le règle en 1-à-1. `{Clear Patch}` efface seulement.

**Verrouillage façade** : `[Shift] & [Escape]` verrouille (empêche toute action ligne de commande/CIA), même combo pour déverrouiller. Verrouille aussi wings et périphériques USB connectés.

### Softkeys
Contextuels, repeignent selon l'affichage/commande en cours. Ligne blanche = actives, ligne grise = deuxième page (accès via `[More SK]`). Sur Gio/Gio@5/Ion Xe/Programming Wing : `[More SK] & <Encoder Category Button>` maintenu accède à la deuxième page. Exemple officiel : avec un channel en ligne de commande, `[More SK] & [Intensity]` poste "Make Manual".

### Displays — hiérarchie complète
**Monitors** > **Workspaces** (jusqu'à 3 par moniteur) > **Frames** (jusqu'à 4 par workspace) > **Tabs** (plusieurs par frame) > **Displays** (un par tab)

**Navigation workspace** : `[Tab] & [Page▲]` / `[Tab] & [Page▼]` cycle les workspaces (incrémente et force tous les autres moniteurs à suivre le même numéro). Accès direct : `[Displays]` → `{Workspace}` → taper 1/2/3. Clavier externe : maintenir `[` ou `]` + taper le numéro.

**Tabs — table complète des numéros fixes (RÉFÉRENCE CANONIQUE)** :
```
1  Live/Blind           11 Show Control       21 Curves              31 Lamp Controls
2  Playback Status       12 Patch              22 Intensity Palettes  32 Channels In Use
3  Magic Sheet           13 Effects            23 Focus Palettes      33 Color Path
4  Direct Selects        14 Magic Sheet List   24 Color Palettes      34 (non utilisé)
5  ML Controls           15 Submaster List     25 Beam Palettes       35 Fader List
6  Effect Status         16 Cue List           26 Presets             36 Fader Configuration
7  Keys                  17 Groups             27 Color Picker        37 sACN Output View
8  Effect Channels       18 Macros             28 Virtual Faders      99 Diagnostics
9  Pixel Maps            19 Snapshots          29 About               100 User Manual
10 Pixel Preview         20 Park               30 Command History
```
Texte blanc dans le tab = Display Tab, texte magenta = Control Tab. Instances multiples : numéro suivi de décimale (n.2, n.3...).

**Fermeture de tabs** : `[Shift]&[Tab]` une fois = ferme tous les tabs du moniteur sélectionné (sauf frames verrouillées) ; deux fois = tous moniteurs ; trois fois = tous moniteurs y compris frames verrouillées.

**Ouverture/fermeture** : accessible via Home Screen (`{+}`), Browser, Hardkeys (double-pression touche record target, ex `[Cue][Cue]` ouvre l'index cue list), Softkeys (après `[Displays]`).

**Sélection d'un display déjà ouvert** :
- `[Tab]` seul : change le focus vers le tab immédiatement à droite (ou premier tab à gauche si aucun à droite)
- `[Tab] & [n]` : va directement au tab n
- `[Live]`/`[Blind]` : ramène Live/Blind en focus (`[Shift]&[Live/Blind]` pour l'instance suivante s'il y en a plusieurs)
- Double-pression d'un bouton record target : ouvre ou sélectionne le display associé

**Zoom** : maintenir `[Format]` + rouler la molette de niveau (haut = zoom in, bas = zoom out)

**Déplacement entre moniteurs** : maintenir `[Tab]` + touches de pagination fléchées

### Scroll Lock
`[Scroll Lock]` (LED rouge quand actif) — état toggle. Une fois activé : `[Page▼]` scroll bas (table/spreadsheet/channel), `[Page▲]` scroll haut, `[Page▶]` scroll droite (table/spreadsheet), `[Page◀]` scroll gauche.

⚠️ **Rappel du piège déjà documenté (vague 4, #036)** : en édition de macro, taper du texte SANS Scroll Lock actif = interprété comme lettres individuelles, pas comme commandes.

### About & Display Toggles (jamais documenté avant dans le corpus — nouveau)
En Live/Blind, `[About]` affiche des infos additionnelles (mode affiché en haut à gauche) :
- `[About] & [Data]` — niveau de fond (background level)
- `[About] & [Park]` — niveaux parkés
- `[About] & [Part]` — numéro de part de cue par paramètre
- `[About] & [Cue]` — type et numéro de la source ; pour cues, affiche cue list + numéro du dernier move
- `[About] & [Mark]` — cue de mark utilisée par les channels
- `[About] & [Next]/[Last]` — prochaine/dernière cue de move des channels
- `[About] & [Label]` — labels de référence
- `[About] & [Time]` — temps discret
- `[About] & [Path]`/`{Color Path}` — chemins de couleur
- Double-pression `[About] & [touche]` verrouille le mode

### Indicateurs Live/Blind — table de couleurs (RÉFÉRENCE, jamais capturée avant)
**Numéros/headers de channel** : Gris = non patché. Blanc = sélectionné. Blanc vif = parqué. Or = capturé. Contour or = sélectionné.

**Niveaux channel/paramètre** :
- Rouge vif = donnée manuelle (même User ID)
- Rouge foncé = donnée manuelle (autre User ID)
- Bleu = intensité plus haute que cue précédente ; NPs en bleu si move instruction survenue
- Vert = intensité plus basse ; aussi utilisé en referenced marking pour indiquer channel marqué
- Magenta = inchangé depuis cue précédente (tracké)
- Blanc = bloqué ; **Blanc souligné = auto-bloqué**
- Gris = défaut ou valeur nulle (`{Make Null}` ou filtre) — un "n" gris apparaît à côté
- Jaune = donnée réglée depuis un submaster
- Donnée en transition (mouvement) = version plus claire de sa couleur

**Indicateurs texte** (couleur pertinente en plus) :
- `_` souligné blanc = block système (auto-block)
- `+` = tous les paramètres de la catégorie ne sont pas à la même valeur (summary view / table view collapsée)
- `!` = avertissement ACN/RDM/dimmer ; `?` = erreur ACN/RDM/dimmer
- `A`/`a` = asserted (cue entière / partiel)
- `B` = manuellement bloqué (doit être stocké)
- `C` = capturé (jaune) ou Color Path (autre couleur)
- `I` = contrôlé par sub inhibitif/grandmaster ; en flag Block = intensity block niveau cue
- `IP`/`CP`/`FP`/`BP` = référence palette (Intensity/Color/Focus/Beam) + numéro, substituable par label si Show Reference Label actif. `[Shift]&[Label]` bascule label/numéro
- `M` = mark placé mais manuel (doit être stocké, bleu une fois stocké) ; `m` = cue non marking
- `MK` = marqué pour cue ultérieure, numéro affiché ailleurs
- `ND` = fixture patché non-dim
- `N` = valeur nulle
- `P` = parqué ; `Ph` = à un niveau preheat
- `Pr` = référence à un preset + numéro
- `Q` (catégories NP d'un channel marqué) = numéro de cue en préparation du mark
- `t` = channel a un timing discret
- `S` = stocké sur sub shielded
- `R` = override manuel de référence — une fois enregistré, la référence est cassée ; si update, la cible référencée est aussi mise à jour sauf instruction contraire

### Flexichannel
`[Flexi]` maintenu → CIA affiche états/modes disponibles. **États** : All, All Patched, Manual, All Show (données en cue/sub), Active (intensité>0 ou move), In Use (intensité>0/fading/effects/NP moves/marking), Selected. **Modes** (combinables aux états) : Cells Off (masters seuls des multicell), Masters Off (cells seules), Partitioned (channels de la partition courante).

`[Flexi] & [.]` toggle rapide cells on/off. `[Next/Last]` sélectionne prochain/dernier channel dans l'état flexi courant. `[Thru]` limite la vue aux channels de l'état courant (sauf sélectionnés) ; `[Thru][Thru]` inclut aussi les channels hors état.

**View Channels** (nouvel état créé à la demande) : sélectionner channels sans Enter → maintenir `[Flexi]` → `{View Chans}`.

**Channels with Timing** : `[Flexi] & [Time]` — affiche uniquement channels à timing discret dans la cue courante.

---

*Fin de la partie 1. Suite : Managing Show Files, Patch (détail complet), Setup, Basic Manual Control.*

---

## ⚠️ LIMITE TECHNIQUE CONSTATÉE — lecture intégrale du PDF non réalisable par cette voie

`web_fetch` sur ce PDF (600+ pages) ne renvoie systématiquement que les premières ~15000 tokens (Introduction + System Basics), sans mécanisme de pagination vers les sections suivantes (Patch détaillé, Setup, Basic Manual Control, Effects, Show Control, OSC Keys...) malgré plusieurs tentatives. `bash_tool` ne peut pas non plus télécharger le fichier directement — le domaine `media.musson.com` n'est pas dans la liste des domaines réseau autorisés du container (seuls github/npm/pypi et quelques autres le sont).

**Conséquence honnête** : je ne peux pas convertir ce manuel dans son intégralité par les outils disponibles dans cette session. Ce qui est capturé dans cette partie 1 (Introduction, Concepts, System Basics complet) reste la seule portion réellement convertie en .md à ce stade — le reste de la table des matières (Patch détaillé, Setup, Basic Manual Control, Groups, Fan, Mark, Palettes, Presets, Cues, Effects, Park, Submasters, Curves, Snapshots, **Macros**, Magic Sheets, Show Control, **OSC Keys**) reste à couvrir par la méthode habituelle de recherche ciblée par section, comme dans les vagues précédentes.

**Alternative proposée** : si tu as accès à ce PDF (ou un équivalent plus récent) en local, tu peux me l'uploader directement en pièce jointe — je pourrai alors le lire nativement sans cette limite de pagination web, et le convertir intégralement.

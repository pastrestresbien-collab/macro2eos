# Analyse du layout TouchOSC Eos — `Eos_TouchOSC.touchosc`

Fichier source conservé en archive : [`reference/touchosc/source/Eos_TouchOSC.touchosc`](source/Eos_TouchOSC.touchosc) (archive ZIP au format TouchOSC — un seul fichier interne `index.xml`).

Format : layout TouchOSC XML version 14, mode 1 (iPad plein écran), orientation `vertical`.
Les attributs `name` et `text` des contrôles, ainsi que les adresses OSC (`osc_cs`), sont encodés en base64 dans le XML brut — décodés ci-dessous.

## Vue d'ensemble

Le layout comporte **5 pages** (`tabpage`), organisées comme un onglet vertical à droite de l'écran (labels "Keyboard", "Attributes", "Groups", "Fader", "Cues") :

| # | Page | Contrôles | Rôle |
|---|---|---|---|
| 1 | Keyboard | 164 | Pavé numérique + touches de fonction Eos (équivalent clavier physique complet : chiffres, Group/Sub/Record/Cue, Live/Blind, Effect, Palettes, etc.) |
| 2 | Attributes | 154 | Molette (wheel) de paramètres (Pan/Tilt/Hue/Sat/Intensity), boutons Min/Max/Home par paramètre, couleurs directes (Reds/CTO/etc.), pavé numérique réduit |
| 3 | Groups | 146 | Grille de groupes (`/eos/group/N`) + Direct Selects (DS) 1-30 avec retour de nom via `/eos/out/ds/...`, effets favoris, pagination DS |
| 4 | Fader | 103 | 10 faders (submasters) avec Load/Fire/Stop, retour de nom via `/eos/out/fader/...`, pagination fader |
| 5 | Cues | 68 | Contrôle de Cue List : Go/Stop/Back, pavé numérique, affichage cue active/pending (`/eos/out/active/cue/text`, `/eos/out/pending/cue/text`), Blackout |

## Éléments communs à toutes les pages

- Barre de navigation verticale à droite (5 `labelv` cliquables, non-OSC — le changement de page est géré nativement par TouchOSC, pas par des messages OSC).
- Ligne de commande Eos en bas : `/eos/out/cmd` (affichage texte de la ligne de commande retournée par la console) et `/eos/key/clear_cmdline`.
- Bascule Live/Blind : `/eos/key/live`, `/eos/key/blind`, avec retour d'état via `/eos/out/event/state`.

## Patterns d'adresses OSC observés (par page, dédupliqués)


### Page 1 — Keyboard (69 contrôles avec adresse OSC)

| Pattern | Occurrences | Exemple |
|---|---|---|
| `/eos/key/about/` | 1 | `/eos/key/about/` |
| `/eos/key/copy_to` | 1 | `/eos/key/copy_to` |
| `/eos/key/recall_from` | 1 | `/eos/key/recall_from` |
| `/eos/key/park` | 1 | `/eos/key/park` |
| `/eos/key/last` | 1 | `/eos/key/last` |
| `/eos/key/go_to_cue` | 1 | `/eos/key/go_to_cue` |
| `/eos/key/block` | 1 | `/eos/key/block` |
| `/eos/key/undo` | 1 | `/eos/key/undo` |
| `/eos/key/capture` | 1 | `/eos/key/capture` |
| `/eos/key/next` | 1 | `/eos/key/next` |
| `/eos/key/+` | 1 | `/eos/key/+` |
| `/eos/key/thru` | 1 | `/eos/key/thru` |
| `/eos/key/-` | 1 | `/eos/key/-` |
| `/eos/key/N` | 10 | `/eos/key/7` |
| `/eos/key/clear_cmd` | 1 | `/eos/key/clear_cmd` |
| `/eos/key/.` | 1 | `/eos/key/.` |
| `/eos/key/macro_button` | 1 | `/eos/key/macro_button` |
| `/eos/key/learn` | 1 | `/eos/key/learn` |
| `/eos/key/label` | 1 | `/eos/key/label` |
| `/eos/key/delete` | 1 | `/eos/key/delete` |
| `/eos/key/help` | 1 | `/eos/key/help` |
| `/eos/key/effect` | 1 | `/eos/key/effect` |
| `/eos/key/\` | 1 | `/eos/key/\` |
| `/eos/key/sneak` | 1 | `/eos/key/sneak` |
| `/eos/key/rem_dim` | 1 | `/eos/key/rem_dim` |
| `/eos/key/home` | 1 | `/eos/key/home` |
| `/eos/key/out` | 1 | `/eos/key/out` |
| `/eos/key/select_last` | 1 | `/eos/key/select_last` |
| `/eos/key/full` | 1 | `/eos/key/full` |
| `/eos/key/cueonlytrack` | 1 | `/eos/key/cueonlytrack` |
| `/eos/key/at` | 1 | `/eos/key/at` |
| `/eos/key/enter` | 1 | `/eos/key/enter` |
| `/eos/key/part` | 1 | `/eos/key/part` |
| `/eos/key/cue` | 1 | `/eos/key/cue` |
| `/eos/key/record` | 1 | `/eos/key/record` |
| `/eos/key/intensity_palette` | 1 | `/eos/key/intensity_palette` |
| `/eos/key/focus_palette` | 1 | `/eos/key/focus_palette` |
| `/eos/key/record_only` | 1 | `/eos/key/record_only` |
| `/eos/key/color_palette` | 1 | `/eos/key/color_palette` |
| `/eos/key/beam_palette` | 1 | `/eos/key/beam_palette` |
| `/eos/key/update` | 1 | `/eos/key/update` |
| `/eos/key/preset` | 1 | `/eos/key/preset` |
| `/eos/key/sub` | 1 | `/eos/key/sub` |
| `/eos/key/group` | 1 | `/eos/key/group` |
| `/eos/key/shift` | 1 | `/eos/key/shift` |
| `/eos/key/delay` | 1 | `/eos/key/delay` |
| `/eos/key/time` | 1 | `/eos/key/time` |
| `/eos/key/escape` | 1 | `/eos/key/escape` |
| `/eos/key/Displays` | 1 | `/eos/key/Displays` |
| `/eos/key/format` | 1 | `/eos/key/format` |
| `/eos/key/expand` | 1 | `/eos/key/expand` |
| `/eos/key/data` | 1 | `/eos/key/data` |
| `/eos/key/tab` | 1 | `/eos/key/tab` |
| `/eos/key/flexichannel_mode` | 1 | `/eos/key/flexichannel_mode` |
| `/eos/out/cmd` | 1 | `/eos/out/cmd` |
| `/eos/key/live` | 1 | `/eos/key/live` |
| `/eos/key/blind` | 1 | `/eos/key/blind` |
| `/eos/out/event/state` | 2 | `/eos/out/event/state` |
| `/eos/key/clear_cmdline` | 1 | `/eos/key/clear_cmdline` |

### Page 2 — Attributes (73 contrôles avec adresse OSC)

| Pattern | Occurrences | Exemple |
|---|---|---|
| `/eos/cmd/Warm_White` | 1 | `/eos/cmd/Warm_White` |
| `/eos/param/hue/min` | 1 | `/eos/param/hue/min` |
| `/eos/param/hue/max` | 1 | `/eos/param/hue/max` |
| `/eos/param/hue/home` | 1 | `/eos/param/hue/home` |
| `/eos/param/saturation/min` | 1 | `/eos/param/saturation/min` |
| `/eos/param/saturation/max` | 1 | `/eos/param/saturation/max` |
| `/eos/param/saturation/home` | 1 | `/eos/param/saturation/home` |
| `/eos/at/home` | 1 | `/eos/at/home` |
| `/eos/at/max` | 1 | `/eos/at/max` |
| `/eos/at/min` | 1 | `/eos/at/min` |
| `/eos/param/tilt/max` | 1 | `/eos/param/tilt/max` |
| `/eos/param/tilt/home` | 1 | `/eos/param/tilt/home` |
| `/eos/param/tilit/min` | 1 | `/eos/param/tilit/min` |
| `/eos/param/pan/max` | 1 | `/eos/param/pan/max` |
| `/eos/param/pan/home` | 1 | `/eos/param/pan/home` |
| `/eos/param/pan/min` | 1 | `/eos/param/pan/min` |
| `/eos/cmd/Pan` | 1 | `/eos/cmd/Pan` |
| `/eos/cmd/Intensity` | 1 | `/eos/cmd/Intensity` |
| `/eos/key/cue` | 1 | `/eos/key/cue` |
| `/eos/key/enter` | 2 | `/eos/key/enter` |
| `/eos/key/+` | 1 | `/eos/key/+` |
| `/eos/key/thru` | 1 | `/eos/key/thru` |
| `/eos/key/-` | 1 | `/eos/key/-` |
| `/eos/key/N` | 10 | `/eos/key/7` |
| `/eos/key/clear_cmd` | 1 | `/eos/key/clear_cmd` |
| `/eos/key/.` | 1 | `/eos/key/.` |
| `/eos/cmd/Tilt` | 1 | `/eos/cmd/Tilt` |
| `/eos/cmd/Hue` | 1 | `/eos/cmd/Hue` |
| `/eos/cmd/Saturation` | 1 | `/eos/cmd/Saturation` |
| `/eos/out/cmd` | 1 | `/eos/out/cmd` |
| `/eos/key/live` | 1 | `/eos/key/live` |
| `/eos/key/blind` | 1 | `/eos/key/blind` |
| `/eos/out/event/state` | 2 | `/eos/out/event/state` |
| `/eos/key/clear_cmdline` | 1 | `/eos/key/clear_cmdline` |
| `/eos/wheel` | 2 | `/eos/wheel` |
| `/eos/key/sub` | 1 | `/eos/key/sub` |
| `/eos/key/group` | 2 | `/eos/key/group` |
| `/eos/key/record` | 1 | `/eos/key/record` |
| `/eos/key/color_palette` | 1 | `/eos/key/color_palette` |
| `/eos/key/save_show` | 1 | `/eos/key/save_show` |
| `/eos/key/at` | 1 | `/eos/key/at` |
| `/eos/key/update` | 1 | `/eos/key/update` |
| `/eos/key/preset` | 1 | `/eos/key/preset` |
| `/eos/key/focus_palette` | 1 | `/eos/key/focus_palette` |
| `/eos/wheel/hue` | 1 | `/eos/wheel/hue` |
| `/eos/wheel/level/` | 1 | `/eos/wheel/level/` |
| `/eos/wheel/pan` | 1 | `/eos/wheel/pan` |
| `/eos/wheel/tilt` | 1 | `/eos/wheel/tilt` |
| `/eos/out/wheel` | 2 | `/eos/out/wheel` |
| `/eos/cmd/Cool_White` | 1 | `/eos/cmd/Cool_White` |
| `/eos/cmd/Blue` | 1 | `/eos/cmd/Blue` |
| `/eos/cmd/Green_Cyan` | 1 | `/eos/cmd/Green_Cyan` |
| `/eos/cmd/Red` | 1 | `/eos/cmd/Red` |
| `/eos/cmd/Yellow` | 1 | `/eos/cmd/Yellow` |
| `/eos/cmd/Magenta` | 1 | `/eos/cmd/Magenta` |
| `/eos/cmd/Cyan` | 1 | `/eos/cmd/Cyan` |
| `/eos/wheel/saturation` | 1 | `/eos/wheel/saturation` |
| `/eos/cmd/Amber` | 1 | `/eos/cmd/Amber` |
| `/eos/cmd/CTO` | 1 | `/eos/cmd/CTO` |

### Page 3 — Groups (107 contrôles avec adresse OSC)

| Pattern | Occurrences | Exemple |
|---|---|---|
| `/eos/out/ds/N` | 2 | `/eos/out/ds/1` |
| `/eos/ds/N/fx/N` | 1 | `/eos/ds/2/fx/20` |
| `/eos/cmd/effect enter` | 1 | `/eos/cmd/effect enter` |
| `/eos/group/N` | 20 | `/eos/group/1` |
| `/eos/out/ds/N/N` | 30 | `/eos/out/ds/1/1` |
| `/eos/ds/N/N` | 30 | `/eos/ds/1/1` |
| `/eos/ds/N/ip/N` | 1 | `/eos/ds/2/ip/20` |
| `/eos/ds/N/fp/N` | 1 | `/eos/ds/2/fp/20` |
| `/eos/ds/N/cp/N` | 1 | `/eos/ds/2/cp/20` |
| `/eos/ds/N/bp/N` | 1 | `/eos/ds/2/bp/20` |
| `/eos/cmd/effect 901 enter` | 1 | `/eos/cmd/effect 901 enter` |
| `/eos/cmd/effect 902 enter` | 1 | `/eos/cmd/effect 902 enter` |
| `/eos/cmd/effect 903 enter` | 1 | `/eos/cmd/effect 903 enter` |
| `/eos/cmd/effect 904 enter` | 1 | `/eos/cmd/effect 904 enter` |
| `/eos/cmd/effect 905 enter` | 1 | `/eos/cmd/effect 905 enter` |
| `/eos/cmd/effect 906 enter` | 1 | `/eos/cmd/effect 906 enter` |
| `/eos/cmd/effect 915 enter` | 1 | `/eos/cmd/effect 915 enter` |
| `/eos/cmd/effect 918 enter` | 1 | `/eos/cmd/effect 918 enter` |
| `/eos/cmd/effect 917 enter` | 1 | `/eos/cmd/effect 917 enter` |
| `/eos/cmd/effect 914 enter` | 1 | `/eos/cmd/effect 914 enter` |
| `/eos/ds/N/page/N` | 2 | `/eos/ds/2/page/1` |
| `/eos/ds/N/preset/N` | 1 | `/eos/ds/2/preset/20` |
| `/eos/out/cmd` | 1 | `/eos/out/cmd` |
| `/eos/key/live` | 1 | `/eos/key/live` |
| `/eos/key/blind` | 1 | `/eos/key/blind` |
| `/eos/out/event/state` | 2 | `/eos/out/event/state` |
| `/eos/key/clear_cmdline` | 1 | `/eos/key/clear_cmdline` |

### Page 4 — Fader (59 contrôles avec adresse OSC)

| Pattern | Occurrences | Exemple |
|---|---|---|
| `/eos/fader/N/page/N` | 2 | `/eos/fader/1/page/-1` |
| `/eos/fader/N/N/load` | 10 | `/eos/fader/1/1/load` |
| `/eos/out/fader/N` | 1 | `/eos/out/fader/1` |
| `/eos/out/fader/N/N/name` | 10 | `/eos/out/fader/1/2/name` |
| `/eos/fader/N/N` | 10 | `/eos/fader/1/1` |
| `/eos/fader/N/N/fire` | 10 | `/eos/fader/1/1/fire` |
| `/eos/fader/N/N/stop` | 10 | `/eos/fader/1/1/stop` |
| `/eos/out/cmd` | 1 | `/eos/out/cmd` |
| `/eos/key/live` | 1 | `/eos/key/live` |
| `/eos/key/blind` | 1 | `/eos/key/blind` |
| `/eos/out/event/state` | 2 | `/eos/out/event/state` |
| `/eos/key/clear_cmdline` | 1 | `/eos/key/clear_cmdline` |

### Page 5 — Cues (28 contrôles avec adresse OSC)

| Pattern | Occurrences | Exemple |
|---|---|---|
| `/eos/key/stop` | 1 | `/eos/key/stop` |
| `/eos/key/go_0` | 1 | `/eos/key/go_0` |
| `/eos/key/N` | 10 | `/eos/key/7` |
| `/eos/key/clear_cmd` | 1 | `/eos/key/clear_cmd` |
| `/eos/key/go_to_cue` | 1 | `/eos/key/go_to_cue` |
| `/eos/out/active/cue/text` | 1 | `/eos/out/active/cue/text` |
| `/eos/out/pending/cue/text` | 1 | `/eos/out/pending/cue/text` |
| `/eos/key/shift` | 1 | `/eos/key/shift` |
| `/eos/key/enter` | 1 | `/eos/key/enter` |
| `/eos/key/blackout` | 1 | `/eos/key/blackout` |
| `/eos/key/.` | 1 | `/eos/key/.` |
| `/eos/key/out` | 1 | `/eos/key/out` |
| `/eos/key/\` | 1 | `/eos/key/\` |
| `/eos/out/cmd` | 1 | `/eos/out/cmd` |
| `/eos/key/live` | 1 | `/eos/key/live` |
| `/eos/key/blind` | 1 | `/eos/key/blind` |
| `/eos/out/event/state` | 2 | `/eos/out/event/state` |
| `/eos/key/clear_cmdline` | 1 | `/eos/key/clear_cmdline` |

## Constat notable

- `/eos/param/tilit/min` (page Attributes) : coquille dans le layout d'origine (« tilit » au lieu de « tilt »). Reproduit tel quel ci-dessus par fidélité à la source ; à ne pas copier dans une implémentation corrigée — utiliser `/eos/param/tilt/min`.
- Les adresses `/eos/key/...` correspondent au dictionnaire de touches OSC documenté dans [`reference/eosKeys.ts`](../eosKeys.ts) et [`manuals/operations-manual/`](../../manuals/operations-manual/) (chapitre Show Control) — cohérent avec le corpus déjà consolidé.
- Les adresses `/eos/ds/<page>/<index>`, `/eos/fader/<page>/<index>` et `/eos/wheel/...` correspondent à l'API OSC « Direct Select / Fader / Wheel » de la doc `osc-integration`.


## Détail intégral des contrôles par page

Table complète, contrôle par contrôle, dans l'ordre du XML source (texte et noms décodés depuis le base64 d'origine). Utile pour retrouver la position (`x,y`), la taille (`w×h`) et la couleur exactes d'un bouton si on veut reproduire ou adapter ce layout.


### Page 1 — "Keyboard"

- Nombre de contrôles : 164


| type | x,y | w×h | color | texte | osc_cs | autres attrs |
|---|---|---|---|---|---|---|
| labelv | 688,788 | 30×215 | orange |  | `` | background=false, outline=true |
| labelv | 688,669 | 30×110 | orange |  | `` | background=false, outline=true |
| labelv | 30,891 | 455×110 | gray |  | `` | background=false, outline=true |
| labelv | 493,891 | 185×110 | gray |  | `` | background=false, outline=true |
| labelv | 493,668 | 185×215 | gray |  | `` | background=false, outline=true |
| labelv | 30,668 | 455×215 | gray |  | `` | background=false, outline=true |
| labelv | 30,339 | 455×320 | gray |  | `` | background=false, outline=true |
| labelv | 493,339 | 185×320 | gray |  | `` | background=false, outline=true |
| labelv | 493,10 | 185×320 | gray |  | `` | background=false, outline=true |
| labelv | 30,10 | 455×320 | gray |  | `` | background=false, outline=true |
| labelv | 734,2 | 34×190 | orange | Keyboard | `` | background=false, outline=false |
| labelv | 734,390 | 34×190 | gray | Groups | `` | background=false, outline=false |
| labelv | 734,196 | 34×190 | gray | Attributes | `` | background=false, outline=false |
| labelv | 734,585 | 34×190 | gray | Fader | `` | background=false, outline=false |
| labelv | 734,780 | 34×190 | gray | Cues | `` | background=false, outline=false |
| push | 587,343 | 87×102 | gray |  | `/eos/key/about/` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,448 | 87×102 | gray |  | `/eos/key/copy_to` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,553 | 87×102 | gray |  | `/eos/key/recall_from` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,672 | 87×102 | gray |  | `/eos/key/park` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,777 | 87×102 | gray |  | `/eos/key/last` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,343 | 87×102 | gray |  | `/eos/key/go_to_cue` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,448 | 87×102 | gray |  | `/eos/key/block` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,553 | 87×102 | gray |  | `/eos/key/undo` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,672 | 87×102 | gray |  | `/eos/key/capture` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,777 | 87×102 | gray |  | `/eos/key/next` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,343 | 87×102 | gray |  | `/eos/key/+` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,448 | 87×102 | gray |  | `/eos/key/thru` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,553 | 87×102 | gray |  | `/eos/key/-` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,343 | 87×102 | gray |  | `/eos/key/7` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,448 | 87×102 | gray |  | `/eos/key/8` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,553 | 87×102 | gray |  | `/eos/key/9` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,343 | 87×102 | gray |  | `/eos/key/4` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,448 | 87×102 | gray |  | `/eos/key/5` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,553 | 87×102 | gray |  | `/eos/key/6` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,343 | 87×102 | gray |  | `/eos/key/1` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,448 | 87×102 | gray |  | `/eos/key/2` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,553 | 87×102 | gray |  | `/eos/key/3` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,343 | 87×102 | gray |  | `/eos/key/clear_cmd` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,448 | 87×102 | gray |  | `/eos/key/0` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,553 | 87×102 | gray |  | `/eos/key/.` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,14 | 87×102 | gray |  | `/eos/key/macro_button` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,119 | 87×102 | gray |  | `/eos/key/learn` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 587,224 | 87×102 | gray |  | `/eos/key/label` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,14 | 87×102 | gray |  | `/eos/key/delete` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,119 | 87×102 | gray |  | `/eos/key/help` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,224 | 87×102 | gray |  | `/eos/key/effect` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,672 | 87×102 | gray |  | `/eos/key/\` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,777 | 87×102 | gray |  | `/eos/key/sneak` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,672 | 87×102 | gray |  | `/eos/key/rem_dim` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,777 | 87×102 | gray |  | `/eos/key/home` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,672 | 87×102 | gray |  | `/eos/key/out` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,777 | 87×102 | gray |  | `/eos/key/select_last` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,672 | 87×102 | gray |  | `/eos/key/full` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,777 | 87×102 | gray |  | `/eos/key/cueonlytrack` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,672 | 87×102 | gray |  | `/eos/key/at` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,777 | 87×102 | gray |  | `/eos/key/enter` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 620,14 | 20×102 | gray | Macro | `` | background=false, outline=false |
| labelv | 620,119 | 20×102 | gray | Learn | `` | background=false, outline=false |
| labelv | 612,224 | 61×102 | gray | Label | `` | background=false, outline=false |
| labelv | 530,14 | 20×102 | gray | Delete | `` | background=false, outline=false |
| labelv | 530,119 | 20×102 | gray | Help | `` | background=false, outline=false |
| labelv | 530,224 | 20×102 | gray | Effect | `` | background=false, outline=false |
| labelv | 620,343 | 20×102 | gray | About | `` | background=false, outline=false |
| labelv | 620,448 | 20×102 | gray | Copy To | `` | background=false, outline=false |
| labelv | 530,448 | 20×102 | gray | Block | `` | background=false, outline=false |
| labelv | 530,553 | 20×102 | gray | Undo | `` | background=false, outline=false |
| labelv | 620,672 | 20×102 | gray | Park | `` | background=false, outline=false |
| labelv | 620,777 | 20×102 | gray | Last | `` | background=false, outline=false |
| labelv | 530,672 | 20×102 | gray | Capture | `` | background=false, outline=false |
| labelv | 530,777 | 20×102 | gray | Next | `` | background=false, outline=false |
| labelv | 427,343 | 20×102 | gray | + | `` | background=false, outline=false |
| labelv | 427,448 | 20×102 | gray | Thru | `` | background=false, outline=false |
| labelv | 427,553 | 20×102 | gray | - | `` | background=false, outline=false |
| labelv | 427,672 | 20×102 | gray | / | `` | background=false, outline=false |
| labelv | 427,777 | 20×102 | gray | Sneak | `` | background=false, outline=false |
| labelv | 337,343 | 20×102 | orange | 7 | `` | background=false, outline=false |
| labelv | 337,448 | 20×102 | orange | 8 | `` | background=false, outline=false |
| labelv | 337,553 | 20×102 | orange | 9 | `` | background=false, outline=false |
| labelv | 337,777 | 20×102 | gray | Home | `` | background=false, outline=false |
| labelv | 157,343 | 20×102 | orange | 1 | `` | background=false, outline=false |
| labelv | 247,448 | 20×102 | orange | 5 | `` | background=false, outline=false |
| labelv | 247,553 | 20×102 | orange | 6 | `` | background=false, outline=false |
| labelv | 247,343 | 20×102 | orange | 4 | `` | background=false, outline=false |
| labelv | 157,448 | 20×102 | orange | 2 | `` | background=false, outline=false |
| labelv | 157,553 | 20×102 | orange | 3 | `` | background=false, outline=false |
| labelv | 67,343 | 20×102 | gray | Clear | `` | background=false, outline=false |
| labelv | 67,448 | 20×102 | orange | 0 | `` | background=false, outline=false |
| labelv | 67,553 | 30×102 | gray | . | `` | background=false, outline=false |
| labelv | 247,672 | 20×102 | gray | Out | `` | background=false, outline=false |
| labelv | 157,672 | 20×102 | gray | Full | `` | background=false, outline=false |
| labelv | 67,672 | 20×102 | gray | At | `` | background=false, outline=false |
| labelv | 67,777 | 20×102 | gray | Enter | `` | background=false, outline=false |
| push | 394,14 | 87×102 | gray |  | `/eos/key/part` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,119 | 87×102 | gray |  | `/eos/key/cue` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,224 | 87×102 | gray |  | `/eos/key/record` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,14 | 87×102 | gray |  | `/eos/key/intensity_palette` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,119 | 87×102 | gray |  | `/eos/key/focus_palette` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,224 | 87×102 | gray |  | `/eos/key/record_only` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,14 | 87×102 | gray |  | `/eos/key/color_palette` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,119 | 87×102 | gray |  | `/eos/key/beam_palette` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,224 | 87×102 | gray |  | `/eos/key/update` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,14 | 87×102 | gray |  | `/eos/key/preset` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,119 | 87×102 | gray |  | `/eos/key/sub` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,224 | 87×102 | gray |  | `/eos/key/group` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,14 | 87×102 | gray |  | `/eos/key/shift` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,119 | 87×102 | gray |  | `/eos/key/delay` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,224 | 87×102 | gray |  | `/eos/key/time` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 427,14 | 20×102 | gray | Part | `` | background=false, outline=false |
| labelv | 427,119 | 20×102 | gray | Cue | `` | background=false, outline=false |
| labelv | 427,224 | 20×102 | gray | Record | `` | background=false, outline=false |
| labelv | 247,224 | 20×102 | gray | Update | `` | background=false, outline=false |
| labelv | 157,14 | 20×102 | gray | Preset | `` | background=false, outline=false |
| labelv | 157,119 | 20×102 | gray | Sub | `` | background=false, outline=false |
| labelv | 67,119 | 20×102 | gray | Delay | `` | background=false, outline=false |
| labelv | 157,224 | 20×102 | gray | Group | `` | background=false, outline=false |
| labelv | 67,224 | 20×102 | gray | Time | `` | background=false, outline=false |
| labelv | 323,14 | 67×102 | gray | Int | `` | background=false, outline=false |
| labelv | 588,224 | 59×102 | gray | Note | `` | background=false, outline=false |
| labelv | 607,224 | 59×102 | gray | _ | `` | background=false, outline=false |
| labelv | 305,14 | 67×102 | gray | Palette | `` | background=false, outline=false |
| labelv | 323,118 | 67×102 | gray | Focus | `` | background=false, outline=false |
| labelv | 305,120 | 67×102 | gray | Palette | `` | background=false, outline=false |
| labelv | 323,224 | 67×102 | gray | Record | `` | background=false, outline=false |
| labelv | 305,225 | 67×102 | gray | Only | `` | background=false, outline=false |
| labelv | 216,14 | 67×102 | gray | Palette | `` | background=false, outline=false |
| labelv | 215,120 | 67×102 | gray | Palette | `` | background=false, outline=false |
| labelv | 233,14 | 67×102 | gray | Color | `` | background=false, outline=false |
| labelv | 232,118 | 67×102 | gray | Beam | `` | background=false, outline=false |
| labelv | 323,224 | 67×102 | gray | Record | `` | background=false, outline=false |
| labelv | 605,552 | 67×102 | gray | Recall | `` | background=false, outline=false |
| labelv | 588,553 | 67×102 | gray | From | `` | background=false, outline=false |
| labelv | 517,343 | 67×102 | gray | Got To | `` | background=false, outline=false |
| labelv | 497,343 | 67×102 | gray | Cue | `` | background=false, outline=false |
| labelv | 322,672 | 67×102 | gray | Rem | `` | background=false, outline=false |
| labelv | 304,672 | 67×102 | gray | Dim | `` | background=false, outline=false |
| labelv | 233,778 | 67×102 | gray | Select | `` | background=false, outline=false |
| labelv | 215,777 | 67×102 | gray | Last | `` | background=false, outline=false |
| labelv | 149,777 | 61×102 | gray | Q Only | `` | background=false, outline=false |
| labelv | 145,777 | 59×102 | gray | _ | `` | background=false, outline=false |
| labelv | 125,778 | 59×102 | gray | Track | `` | background=false, outline=false |
| labelv | 67,13 | 20×102 | gray | Shift | `` | background=false, outline=false |
| push | 587,895 | 87×102 | gray |  | `/eos/key/escape` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 497,895 | 87×102 | gray |  | `/eos/key/Displays` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 394,895 | 87×102 | gray |  | `/eos/key/format` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 304,895 | 87×102 | gray |  | `/eos/key/expand` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 214,895 | 87×102 | gray |  | `/eos/key/data` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 124,895 | 87×102 | gray |  | `/eos/key/tab` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 34,895 | 87×102 | gray |  | `/eos/key/flexichannel_mode` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 620,895 | 20×102 | gray | Escape | `` | background=false, outline=false |
| labelv | 530,895 | 20×102 | gray | Displays | `` | background=false, outline=false |
| labelv | 427,895 | 20×102 | gray | Format | `` | background=false, outline=false |
| labelv | 337,895 | 20×102 | gray | Expand | `` | background=false, outline=false |
| labelv | 67,895 | 20×102 | gray | Flexi | `` | background=false, outline=false |
| labelv | 247,897 | 20×100 | gray | Data | `` | background=false, outline=false |
| labelv | 158,896 | 20×102 | gray | Tab | `` | background=false, outline=false |
| labelv | 688,10 | 30×649 | orange |  | `/eos/out/cmd` | background=true, outline=true |
| push | 692,792 | 22×102 | gray |  | `/eos/key/live` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 692,897 | 22×102 | gray |  | `/eos/key/blind` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 693,792 | 20×102 | gray | Live | `` | background=false, outline=false |
| labelv | 693,897 | 20×102 | gray | Blind | `` | background=false, outline=false |
| led | 696,796 | 14×14 | orange |  | `/eos/out/event/state` | scalef=0.0, scalet=1.0 |
| led | 696,902 | 14×14 | blue |  | `/eos/out/event/state` | scalef=1.0, scalet=0.0 |
| push | 692,673 | 22×102 | gray |  | `/eos/key/clear_cmdline` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 694,671 | 20×102 | gray | All Clear | `` | background=false, outline=false |

### Page 2 — "Attributes"

- Nombre de contrôles : 154


| type | x,y | w×h | color | texte | osc_cs | autres attrs |
|---|---|---|---|---|---|---|
| push | 349,789 | 48×88 | gray |  | `/eos/cmd/Warm_White` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 688,781 | 30×215 | orange |  | `` | background=false, outline=true |
| push | 182,377 | 126×64 | gray |  | `/eos/param/hue/min` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 190,375 | 36×54 | gray | 0 | `` | background=false, outline=false |
| push | 182,493 | 126×64 | gray |  | `/eos/param/hue/max` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 189,503 | 36×54 | gray | 360 | `` | background=false, outline=false |
| push | 182,434 | 126×64 | gray |  | `/eos/param/hue/home` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 147,376 | 165×180 | gray |  | `` | background=false, outline=true |
| labelv | 222,19 | 456×320 | gray |  | `` | background=false, outline=true |
| labelv | 27,886 | 96×110 | gray |  | `` | background=false, outline=true |
| labelv | 27,347 | 96×531 | gray |  | `` | background=false, outline=true |
| push | 182,582 | 126×64 | gray |  | `/eos/param/saturation/min` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 190,583 | 36×54 | gray | 0% | `` | background=false, outline=false |
| push | 182,699 | 126×64 | gray |  | `/eos/param/saturation/max` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 189,709 | 36×54 | gray | 100% | `` | background=false, outline=false |
| push | 182,640 | 126×64 | gray |  | `/eos/param/saturation/home` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 189,581 | 36×180 | gray | Home | `` | background=false, outline=false |
| push | 449,432 | 126×64 | gray |  | `/eos/at/home` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 449,491 | 126×64 | gray |  | `/eos/at/max` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 449,374 | 126×64 | gray |  | `/eos/at/min` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 414,375 | 173×180 | gray |  | `` | background=false, outline=true |
| push | 449,905 | 126×64 | gray |  | `/eos/param/tilt/max` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 449,846 | 126×64 | gray |  | `/eos/param/tilt/home` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 449,788 | 126×64 | gray |  | `/eos/param/tilit/min` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 414,788 | 165×180 | gray |  | `` | background=false, outline=true |
| push | 449,698 | 126×64 | gray |  | `/eos/param/pan/max` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 449,639 | 126×64 | gray |  | `/eos/param/pan/home` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 449,581 | 126×64 | gray |  | `/eos/param/pan/min` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 414,581 | 165×180 | gray |  | `` | background=false, outline=true |
| push | 413,581 | 46×181 | gray |  | `/eos/cmd/Pan` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 414,374 | 40×181 | gray |  | `/eos/cmd/Intensity` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 734,2 | 34×190 | gray | Keyboard | `` | background=false, outline=false |
| labelv | 734,390 | 34×190 | gray | Groups | `` | background=false, outline=false |
| labelv | 734,196 | 34×191 | orange | Attributes | `` | background=false, outline=false |
| labelv | 734,585 | 34×190 | gray | Fader | `` | background=false, outline=false |
| labelv | 734,780 | 34×190 | gray | Cues | `` | background=false, outline=false |
| push | 122,23 | 87×102 | gray |  | `/eos/key/cue` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 122,233 | 87×102 | gray |  | `/eos/key/enter` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 155,23 | 20×102 | gray | Cue | `` | background=false, outline=false |
| push | 586,23 | 87×102 | gray |  | `/eos/key/+` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 586,128 | 87×102 | gray |  | `/eos/key/thru` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 586,233 | 87×102 | gray |  | `/eos/key/-` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 496,23 | 87×102 | gray |  | `/eos/key/7` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 496,128 | 87×102 | gray |  | `/eos/key/8` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 496,233 | 87×102 | gray |  | `/eos/key/9` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 406,23 | 87×102 | gray |  | `/eos/key/4` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 406,128 | 87×102 | gray |  | `/eos/key/5` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 406,233 | 87×102 | gray |  | `/eos/key/6` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 316,23 | 87×102 | gray |  | `/eos/key/1` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 316,128 | 87×102 | gray |  | `/eos/key/2` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 316,233 | 87×102 | gray |  | `/eos/key/3` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 226,23 | 87×102 | gray |  | `/eos/key/clear_cmd` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 226,128 | 87×102 | gray |  | `/eos/key/0` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 226,233 | 87×102 | gray |  | `/eos/key/.` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 619,23 | 20×102 | gray | + | `` | background=false, outline=false |
| labelv | 619,128 | 20×102 | gray | Thru | `` | background=false, outline=false |
| labelv | 619,233 | 20×102 | gray | - | `` | background=false, outline=false |
| labelv | 529,23 | 20×102 | orange | 7 | `` | background=false, outline=false |
| labelv | 529,128 | 20×102 | orange | 8 | `` | background=false, outline=false |
| labelv | 529,233 | 20×102 | orange | 9 | `` | background=false, outline=false |
| labelv | 349,23 | 20×102 | orange | 1 | `` | background=false, outline=false |
| labelv | 439,128 | 20×102 | orange | 5 | `` | background=false, outline=false |
| labelv | 439,233 | 20×102 | orange | 6 | `` | background=false, outline=false |
| labelv | 439,23 | 20×102 | orange | 4 | `` | background=false, outline=false |
| labelv | 349,128 | 20×102 | orange | 2 | `` | background=false, outline=false |
| labelv | 349,233 | 20×102 | orange | 3 | `` | background=false, outline=false |
| labelv | 259,23 | 20×102 | gray | Clear | `` | background=false, outline=false |
| labelv | 259,128 | 20×102 | orange | 0 | `` | background=false, outline=false |
| labelv | 259,233 | 31×102 | gray | . | `` | background=false, outline=false |
| labelv | 454,372 | 36×54 | gray | 0% | `` | background=false, outline=false |
| labelv | 455,501 | 36×54 | gray | 100% | `` | background=false, outline=false |
| labelv | 457,582 | 36×54 | gray | Min | `` | background=false, outline=false |
| labelv | 456,708 | 36×54 | gray | Max | `` | background=false, outline=false |
| labelv | 456,580 | 36×180 | gray | Home | `` | background=false, outline=false |
| push | 413,788 | 46×181 | gray |  | `/eos/cmd/Tilt` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 457,789 | 36×54 | gray | Min | `` | background=false, outline=false |
| labelv | 456,915 | 36×54 | gray | Max | `` | background=false, outline=false |
| labelv | 456,787 | 36×180 | gray | Home | `` | background=false, outline=false |
| push | 146,377 | 46×181 | gray |  | `/eos/cmd/Hue` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 146,583 | 46×181 | gray |  | `/eos/cmd/Saturation` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 454,375 | 36×180 | gray | Home | `` | background=false, outline=false |
| labelv | 414,581 | 44×180 | gray | Pan | `` | background=false, outline=true |
| labelv | 414,788 | 44×180 | gray | Tilt | `` | background=false, outline=true |
| labelv | 147,376 | 44×180 | gray | Hue | `` | background=false, outline=true |
| labelv | 147,583 | 44×180 | gray | Saturation | `` | background=false, outline=true |
| labelv | 688,18 | 30×634 | orange |  | `/eos/out/cmd` | background=true, outline=true |
| push | 692,785 | 22×102 | gray |  | `/eos/key/live` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 692,890 | 22×102 | gray |  | `/eos/key/blind` | local_off=false, scalef=0.0, scalet=1.0 |
| led | 696,789 | 14×14 | orange |  | `/eos/out/event/state` | scalef=0.0, scalet=1.0 |
| led | 696,895 | 14×14 | blue |  | `/eos/out/event/state` | scalef=1.0, scalet=0.0 |
| push | 692,666 | 22×102 | gray |  | `/eos/key/clear_cmdline` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 694,664 | 20×102 | gray | All Clear | `` | background=false, outline=false |
| labelv | 688,662 | 30×110 | orange |  | `` | background=false, outline=true |
| push | 76,23 | 41×102 | gray |  | `/eos/wheel` | local_off=false, scalef=0.0, scalet=0.0 |
| push | 31,128 | 87×102 | gray |  | `/eos/key/sub` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 31,233 | 87×102 | gray |  | `/eos/key/group` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 86,43 | 20×82 | gray | Coarse | `` | background=false, outline=false |
| labelv | 64,128 | 20×102 | gray | Sub | `` | background=false, outline=false |
| labelv | 64,233 | 20×102 | gray | Group | `` | background=false, outline=false |
| push | 31,352 | 87×102 | gray |  | `/eos/key/record` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 31,562 | 87×102 | gray |  | `/eos/key/enter` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 65,352 | 20×102 | red | Record | `` | background=false, outline=false |
| labelv | 32,562 | 86×102 | orange | Update | `` | background=false, outline=false |
| push | 31,667 | 87×102 | gray |  | `/eos/key/group` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 31,772 | 87×102 | gray |  | `/eos/key/color_palette` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 31,890 | 87×102 | gray |  | `/eos/key/save_show` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 32,667 | 86×102 | gray | Int Plaette | `` | background=false, outline=false |
| labelv | 65,772 | 20×102 | gray | Color Palette | `` | background=false, outline=false |
| labelv | 65,890 | 20×102 | green | Save Show | `` | background=false, outline=false |
| labelv | 155,233 | 20×102 | gray | Enter | `` | background=false, outline=false |
| push | 122,128 | 87×102 | gray |  | `/eos/key/at` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 155,128 | 20×102 | gray | At | `` | background=false, outline=false |
| push | 31,457 | 87×102 | gray |  | `/eos/key/update` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 65,457 | 20×102 | red | Update | `` | background=false, outline=false |
| push | 31,562 | 87×102 | gray |  | `/eos/key/preset` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 31,667 | 87×102 | gray |  | `/eos/key/focus_palette` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 65,562 | 20×102 | gray | Preset | `` | background=false, outline=false |
| labelv | 65,667 | 20×102 | gray | Focus Palette | `` | background=false, outline=false |
| encoder | 218,376 | 180×180 | gray |  | `/eos/wheel/hue` | scalef=-1.0, scalet=1.0 |
| encoder | 485,375 | 180×180 | gray |  | `/eos/wheel/level/` | scalef=-1.0, scalet=1.0 |
| encoder | 485,581 | 180×180 | gray |  | `/eos/wheel/pan` | scalef=-1.0, scalet=1.0 |
| encoder | 485,788 | 180×180 | gray |  | `/eos/wheel/tilt` | scalef=-1.0, scalet=1.0 |
| labelv | 189,375 | 36×180 | gray | Home | `` | background=false, outline=false |
| push | 32,23 | 40×102 | gray |  | `/eos/wheel` | local_off=false, scalef=1.0, scalet=1.0 |
| labelv | 42,32 | 20×93 | gray | Fine | `` | background=false, outline=false |
| led | 88,32 | 15×15 | orange |  | `/eos/out/wheel` | scalef=1.0, scalet=0.0 |
| led | 44,32 | 15×15 | orange |  | `/eos/out/wheel` | scalef=0.0, scalet=1.0 |
| labelv | 364,790 | 20×88 | gray | Warm | `` | background=false, outline=false |
| push | 298,789 | 48×88 | gray |  | `/eos/cmd/Cool_White` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 313,788 | 20×88 | gray | Cool | `` | background=false, outline=false |
| push | 247,789 | 48×88 | gray |  | `/eos/cmd/Blue` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 262,789 | 20×88 | gray | Blue | `` | background=false, outline=false |
| push | 196,789 | 48×88 | gray |  | `/eos/cmd/Green_Cyan` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 211,789 | 20×88 | gray | Grn Cyan | `` | background=false, outline=false |
| push | 349,880 | 48×88 | gray |  | `/eos/cmd/Red` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 364,880 | 20×88 | gray | Red | `` | background=false, outline=false |
| push | 298,880 | 48×88 | gray |  | `/eos/cmd/Yellow` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 313,880 | 20×88 | gray | Yellow | `` | background=false, outline=false |
| push | 247,880 | 48×88 | gray |  | `/eos/cmd/Magenta` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 262,880 | 20×88 | gray | Magenta | `` | background=false, outline=false |
| push | 196,880 | 48×88 | gray |  | `/eos/cmd/Cyan` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 211,880 | 20×88 | gray | Cyan | `` | background=false, outline=false |
| labelv | 147,583 | 165×180 | gray |  | `` | background=false, outline=true |
| encoder | 218,583 | 180×180 | gray |  | `/eos/wheel/saturation` | scalef=-1.0, scalet=1.0 |
| labelv | 413,375 | 42×180 | gray | Intensity | `` | background=false, outline=true |
| labelv | 693,890 | 20×102 | gray | Blind | `` | background=false, outline=false |
| labelv | 693,785 | 20×102 | gray | Live | `` | background=false, outline=false |
| labelv | 26,19 | 187×320 | gray |  | `` | background=false, outline=true |
| push | 145,789 | 48×88 | gray |  | `/eos/cmd/Amber` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 160,789 | 20×88 | gray | Amber | `` | background=false, outline=false |
| push | 145,880 | 48×88 | gray |  | `/eos/cmd/CTO` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 160,880 | 20×88 | gray | CTO | `` | background=false, outline=false |
| labelv | 144,788 | 254×179 | gray |  | `` | background=false, outline=true |
| labelv | 130,347 | 548×649 | gray |  | `` | background=false, outline=true |

### Page 3 — "Groups"

- Adresse OSC de page (`osc_cs` du `tabpage`) : `/eos/ds/1/group/10`

- Nombre de contrôles : 146


| type | x,y | w×h | color | texte | osc_cs | autres attrs |
|---|---|---|---|---|---|---|
| labelv | 343,27 | 339×988 | gray |  | `` | background=false, outline=true |
| labelv | 101,27 | 245×988 | gray |  | `` | background=false, outline=true |
| labelh | 343,11 | 339×30 | gray | Groups | `/eos/out/ds/1` | background=true, outline=true |
| push | 301,826 | 31×105 | gray |  | `/eos/ds/2/fx/20` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 302,827 | 28×96 | gray | Effects | `` | background=false, outline=false |
| push | 301,923 | 31×55 | red |  | `/eos/cmd/effect enter` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 734,2 | 34×190 | gray | Keyboard | `` | background=false, outline=false |
| labelv | 734,390 | 34×192 | orange | Groups | `` | background=false, outline=false |
| labelv | 734,196 | 34×190 | gray | Attributes | `` | background=false, outline=false |
| labelv | 734,585 | 34×190 | gray | Fader | `` | background=false, outline=false |
| labelv | 734,780 | 34×190 | gray | Cues | `` | background=false, outline=false |
| faderh | 441,65 | 185×57 | gray |  | `/eos/group/1` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,65 | 45×57 | gray |  | `/eos/group/1` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,46 | 19×95 | gray |  | `/eos/out/ds/1/1` | background=false, outline=false |
| faderh | 441,160 | 185×57 | gray |  | `/eos/group/2` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,160 | 45×57 | gray |  | `/eos/group/2` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,141 | 19×95 | gray |  | `/eos/out/ds/1/2` | background=false, outline=false |
| faderh | 441,255 | 185×57 | gray |  | `/eos/group/3` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,255 | 45×57 | gray |  | `/eos/group/3` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,236 | 19×95 | gray |  | `/eos/out/ds/1/3` | background=false, outline=false |
| faderh | 441,350 | 185×57 | gray |  | `/eos/group/4` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,350 | 45×57 | gray |  | `/eos/group/4` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,331 | 19×95 | gray |  | `/eos/out/ds/1/4` | background=false, outline=false |
| faderh | 441,444 | 185×57 | gray |  | `/eos/group/5` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,445 | 45×57 | gray |  | `/eos/group/5` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,426 | 19×95 | gray |  | `/eos/out/ds/1/5` | background=false, outline=false |
| faderh | 441,540 | 185×57 | gray |  | `/eos/group/6` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,540 | 45×57 | gray |  | `/eos/group/6` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,521 | 19×95 | gray |  | `/eos/out/ds/1/6` | background=false, outline=false |
| faderh | 441,635 | 185×57 | gray |  | `/eos/group/7` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,635 | 45×57 | gray |  | `/eos/group/7` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,616 | 19×95 | gray |  | `/eos/out/ds/1/7` | background=false, outline=false |
| faderh | 441,730 | 185×57 | gray |  | `/eos/group/8` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,730 | 45×57 | gray |  | `/eos/group/8` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,711 | 19×95 | gray |  | `/eos/out/ds/1/8` | background=false, outline=false |
| faderh | 441,825 | 185×57 | gray |  | `/eos/group/9` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,825 | 45×57 | gray |  | `/eos/group/9` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,806 | 19×95 | gray |  | `/eos/out/ds/1/9` | background=false, outline=false |
| faderh | 441,920 | 185×57 | gray |  | `/eos/group/10` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=100.0 |
| push | 383,920 | 45×57 | gray |  | `/eos/group/10` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 354,900 | 19×96 | gray |  | `/eos/out/ds/1/10` | background=false, outline=false |
| push | 638,65 | 29×57 | gray |  | `/eos/ds/1/1` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 638,160 | 29×57 | gray |  | `/eos/ds/1/2` | local_off=false, scalef=0.0, scalet=2.0 |
| push | 638,255 | 29×57 | gray |  | `/eos/ds/1/3` | local_off=false, scalef=0.0, scalet=3.0 |
| push | 638,350 | 29×57 | gray |  | `/eos/ds/1/4` | local_off=false, scalef=0.0, scalet=4.0 |
| push | 638,445 | 29×57 | gray |  | `/eos/ds/1/5` | local_off=false, scalef=0.0, scalet=5.0 |
| push | 638,540 | 29×57 | gray |  | `/eos/ds/1/6` | local_off=false, scalef=0.0, scalet=6.0 |
| push | 638,635 | 29×57 | gray |  | `/eos/ds/1/7` | local_off=false, scalef=0.0, scalet=7.0 |
| push | 638,730 | 29×57 | gray |  | `/eos/ds/1/8` | local_off=false, scalef=0.0, scalet=8.0 |
| push | 638,825 | 29×57 | gray |  | `/eos/ds/1/9` | local_off=false, scalef=0.0, scalet=9.0 |
| push | 638,920 | 29×57 | gray |  | `/eos/ds/1/10` | local_off=false, scalef=0.0, scalet=10.0 |
| push | 301,66 | 31×113 | gray |  | `/eos/ds/2/ip/20` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 301,217 | 31×114 | gray |  | `/eos/ds/2/fp/20` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 301,217 | 31×114 | gray | Focus | `` | background=false, outline=false |
| push | 301,369 | 31×114 | gray |  | `/eos/ds/2/cp/20` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 301,369 | 31×114 | gray | Color | `` | background=false, outline=false |
| push | 301,521 | 31×114 | gray |  | `/eos/ds/2/bp/20` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 301,521 | 31×114 | gray | Beam | `` | background=false, outline=false |
| push | 243,65 | 44×57 | gray |  | `/eos/ds/2/1` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,46 | 19×95 | gray |  | `/eos/out/ds/2/1` | background=false, outline=false |
| push | 243,160 | 44×57 | gray |  | `/eos/ds/2/2` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,141 | 19×95 | gray |  | `/eos/out/ds/2/2` | background=false, outline=false |
| push | 243,255 | 44×57 | gray |  | `/eos/ds/2/3` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,236 | 19×95 | gray |  | `/eos/out/ds/2/3` | background=false, outline=false |
| push | 243,350 | 44×57 | gray |  | `/eos/ds/2/4` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,331 | 19×95 | gray |  | `/eos/out/ds/2/4` | background=false, outline=false |
| push | 243,445 | 44×57 | gray |  | `/eos/ds/2/5` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,426 | 19×95 | gray |  | `/eos/out/ds/2/5` | background=false, outline=false |
| push | 243,540 | 44×57 | gray |  | `/eos/ds/2/6` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,521 | 19×95 | gray |  | `/eos/out/ds/2/6` | background=false, outline=false |
| push | 243,635 | 44×57 | gray |  | `/eos/ds/2/7` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,616 | 19×95 | gray |  | `/eos/out/ds/2/7` | background=false, outline=false |
| push | 243,730 | 44×57 | gray |  | `/eos/ds/2/8` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,711 | 19×95 | gray |  | `/eos/out/ds/2/8` | background=false, outline=false |
| push | 243,825 | 44×57 | gray |  | `/eos/ds/2/9` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,806 | 19×95 | gray |  | `/eos/out/ds/2/9` | background=false, outline=false |
| push | 243,920 | 44×57 | gray |  | `/eos/ds/2/10` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 209,900 | 19×96 | gray |  | `/eos/out/ds/2/10` | background=false, outline=false |
| push | 147,65 | 47×57 | gray |  | `/eos/ds/2/11` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,46 | 19×95 | gray |  | `/eos/out/ds/2/11` | background=false, outline=false |
| push | 147,160 | 47×57 | gray |  | `/eos/ds/2/12` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,141 | 19×95 | gray |  | `/eos/out/ds/2/12` | background=false, outline=false |
| push | 147,255 | 47×57 | gray |  | `/eos/ds/2/13` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,236 | 19×95 | gray |  | `/eos/out/ds/2/13` | background=false, outline=false |
| push | 147,350 | 47×57 | gray |  | `/eos/ds/2/14` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,331 | 19×95 | gray |  | `/eos/out/ds/2/14` | background=false, outline=false |
| push | 147,445 | 47×57 | gray |  | `/eos/ds/2/15` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,426 | 19×95 | gray |  | `/eos/out/ds/2/15` | background=false, outline=false |
| push | 147,540 | 47×57 | gray |  | `/eos/ds/2/16` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,521 | 19×95 | gray |  | `/eos/out/ds/2/16` | background=false, outline=false |
| push | 147,635 | 47×57 | gray |  | `/eos/ds/2/17` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,616 | 19×95 | gray |  | `/eos/out/ds/2/17` | background=false, outline=false |
| push | 147,730 | 47×57 | gray |  | `/eos/ds/2/18` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,711 | 19×95 | gray |  | `/eos/out/ds/2/18` | background=false, outline=false |
| push | 147,825 | 47×57 | gray |  | `/eos/ds/2/19` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,806 | 19×95 | gray |  | `/eos/out/ds/2/19` | background=false, outline=false |
| push | 147,920 | 47×57 | gray |  | `/eos/ds/2/20` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 114,900 | 19×96 | gray |  | `/eos/out/ds/2/20` | background=false, outline=false |
| labelv | 300,217 | 32×114 | gray |  | `` | background=false, outline=true |
| labelv | 301,369 | 31×114 | gray |  | `` | background=false, outline=true |
| labelv | 301,521 | 31×114 | gray |  | `` | background=false, outline=true |
| push | 43,65 | 47×57 | gray |  | `/eos/cmd/effect 901 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,46 | 19×95 | gray | Circle | `` | background=false, outline=false |
| push | 43,160 | 47×57 | gray |  | `/eos/cmd/effect 902 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,141 | 19×95 | gray | Square | `` | background=false, outline=false |
| push | 43,255 | 47×57 | gray |  | `/eos/cmd/effect 903 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,236 | 19×95 | gray | Figure 8 | `` | background=false, outline=false |
| push | 43,350 | 47×57 | gray |  | `/eos/cmd/effect 904 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,331 | 19×95 | gray | Can Can | `` | background=false, outline=false |
| push | 43,445 | 47×57 | gray |  | `/eos/cmd/effect 905 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,426 | 19×95 | gray | Triangle | `` | background=false, outline=false |
| push | 43,540 | 47×57 | gray |  | `/eos/cmd/effect 906 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,521 | 19×95 | gray | Spiral | `` | background=false, outline=false |
| push | 43,635 | 47×57 | gray |  | `/eos/cmd/effect 915 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,616 | 19×95 | gray | Ramp | `` | background=false, outline=false |
| push | 43,730 | 47×57 | gray |  | `/eos/cmd/effect 918 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,711 | 19×95 | gray | Rainbow CMY | `` | background=false, outline=false |
| push | 43,825 | 47×57 | gray |  | `/eos/cmd/effect 917 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,806 | 19×95 | gray | Rainbow RGB | `` | background=false, outline=false |
| push | 43,920 | 47×57 | gray |  | `/eos/cmd/effect 914 enter` | local_off=false, scalef=0.0, scalet=100.0 |
| labelv | 10,900 | 19×96 | gray | Hue Sat Fade | `` | background=false, outline=false |
| labelv | 1,27 | 103×988 | gray |  | `` | background=false, outline=true |
| labelh | 1,10 | 103×31 | gray | Effect preset | `` | background=true, outline=true |
| labelh | 101,11 | 245×30 | gray | Palette | `/eos/out/ds/2` | background=true, outline=true |
| labelv | 301,66 | 31×113 | gray | Intensity | `` | background=false, outline=false |
| labelv | 300,66 | 32×113 | gray |  | `` | background=false, outline=true |
| push | 295,12 | 50×28 | gray |  | `/eos/ds/2/page/1` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 102,12 | 50×28 | gray |  | `/eos/ds/2/page/-1` | local_off=false, scalef=0.0, scalet=1.0 |
| labelh | 103,13 | 48×25 | gray | - | `` | background=false, outline=false |
| labelh | 295,13 | 48×25 | gray | + | `` | background=false, outline=false |
| labelv | 301,923 | 31×53 | gray | Stop | `` | background=false, outline=false |
| labelv | 301,826 | 31×152 | gray |  | `` | background=false, outline=true |
| push | 301,674 | 31×114 | gray |  | `/eos/ds/2/preset/20` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 301,674 | 31×114 | gray | Preset | `` | background=false, outline=false |
| labelv | 301,674 | 31×114 | gray |  | `` | background=false, outline=true |
| labelv | 688,10 | 30×661 | orange |  | `/eos/out/cmd` | background=true, outline=true |
| push | 692,803 | 22×102 | gray |  | `/eos/key/live` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 692,908 | 22×102 | gray |  | `/eos/key/blind` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 693,803 | 20×102 | gray | Live | `` | background=false, outline=false |
| labelv | 693,908 | 20×102 | gray | Blind | `` | background=false, outline=false |
| led | 696,807 | 14×14 | orange |  | `/eos/out/event/state` | scalef=0.0, scalet=1.0 |
| led | 696,913 | 14×14 | blue |  | `/eos/out/event/state` | scalef=1.0, scalet=0.0 |
| labelv | 688,799 | 30×215 | orange |  | `` | background=false, outline=true |
| push | 692,684 | 22×102 | gray |  | `/eos/key/clear_cmdline` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 694,682 | 20×102 | gray | All Clear | `` | background=false, outline=false |
| labelv | 688,680 | 30×110 | orange |  | `` | background=false, outline=true |

### Page 4 — "Fader"

- Adresse OSC de page (`osc_cs` du `tabpage`) : `/eos/fader/1/config/10`

- Nombre de contrôles : 103


| type | x,y | w×h | color | texte | osc_cs | autres attrs |
|---|---|---|---|---|---|---|
| labelv | 688,799 | 30×215 | orange |  | `` | background=false, outline=true |
| labelv | 12,27 | 670×988 | gray |  | `` | background=false, outline=true |
| labelh | 12,11 | 670×30 | gray | Fader page | `` | background=true, outline=true |
| push | 13,12 | 50×28 | gray |  | `/eos/fader/1/page/-1` | local_off=false, scalef=0.0, scalet=1.0 |
| labelh | 13,13 | 48×25 | gray | - | `` | background=false, outline=false |
| push | 641,68 | 29×57 | gray |  | `/eos/fader/1/1/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,68 | 20×58 | gray | Load | `` | background=false, outline=false |
| labelh | 116,11 | 561×30 | gray | 1 | `/eos/out/fader/1` | background=false, outline=false |
| labelv | 734,2 | 34×190 | gray | Keyboard | `` | background=false, outline=false |
| labelv | 734,390 | 34×190 | gray | Groups | `` | background=false, outline=false |
| labelv | 734,196 | 34×190 | gray | Attributes | `` | background=false, outline=false |
| labelv | 734,585 | 34×191 | orange | Fader | `` | background=false, outline=false |
| labelv | 734,780 | 34×190 | gray | Cues | `` | background=false, outline=false |
| labelv | 22,145 | 19×95 | gray |  | `/eos/out/fader/1/2/name` | background=false, outline=false |
| labelv | 22,242 | 19×95 | gray |  | `/eos/out/fader/1/3/name` | background=false, outline=false |
| labelv | 22,339 | 19×95 | gray |  | `/eos/out/fader/1/4/name` | background=false, outline=false |
| labelv | 22,435 | 19×95 | gray |  | `/eos/out/fader/1/5/name` | background=false, outline=false |
| labelv | 22,532 | 19×95 | gray |  | `/eos/out/fader/1/6/name` | background=false, outline=false |
| labelv | 22,629 | 19×95 | gray |  | `/eos/out/fader/1/7/name` | background=false, outline=false |
| labelv | 22,726 | 19×95 | gray |  | `/eos/out/fader/1/8/name` | background=false, outline=false |
| labelv | 22,822 | 19×95 | gray |  | `/eos/out/fader/1/9/name` | background=false, outline=false |
| labelv | 22,919 | 19×96 | gray |  | `/eos/out/fader/1/10/name` | background=false, outline=false |
| faderh | 200,68 | 422×57 | gray |  | `/eos/fader/1/1` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 631,12 | 50×28 | gray |  | `/eos/fader/1/page/1` | local_off=false, scalef=0.0, scalet=1.0 |
| labelh | 632,13 | 48×25 | gray | + | `` | background=false, outline=false |
| push | 52,68 | 59×58 | gray |  | `/eos/fader/1/1/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,68 | 59×59 | gray |  | `/eos/fader/1/1/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,68 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 22,49 | 20×95 | gray |  | `/eos/out/fader/1/1/name` | background=false, outline=false |
| labelv | 688,10 | 30×661 | orange |  | `/eos/out/cmd` | background=true, outline=true |
| push | 692,803 | 22×102 | gray |  | `/eos/key/live` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 692,908 | 22×102 | gray |  | `/eos/key/blind` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 693,803 | 20×102 | gray | Live | `` | background=false, outline=false |
| labelv | 693,908 | 20×102 | gray | Blind | `` | background=false, outline=false |
| led | 696,807 | 14×14 | orange |  | `/eos/out/event/state` | scalef=0.0, scalet=1.0 |
| led | 696,913 | 14×14 | blue |  | `/eos/out/event/state` | scalef=1.0, scalet=0.0 |
| push | 692,684 | 22×102 | gray |  | `/eos/key/clear_cmdline` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 694,682 | 20×102 | gray | All Clear | `` | background=false, outline=false |
| labelv | 688,680 | 30×110 | orange |  | `` | background=false, outline=true |
| labelv | 71,69 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,164 | 29×57 | gray |  | `/eos/fader/1/2/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,164 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,164 | 422×57 | gray |  | `/eos/fader/1/2` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,164 | 59×58 | gray |  | `/eos/fader/1/2/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,164 | 59×59 | gray |  | `/eos/fader/1/2/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,165 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,165 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,261 | 29×57 | gray |  | `/eos/fader/1/2/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,260 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,261 | 422×57 | gray |  | `/eos/fader/1/3` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,261 | 59×58 | gray |  | `/eos/fader/1/3/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,261 | 59×59 | gray |  | `/eos/fader/1/3/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,262 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,261 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,357 | 29×57 | gray |  | `/eos/fader/1/4/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,357 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,357 | 422×57 | gray |  | `/eos/fader/1/4` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,357 | 59×58 | gray |  | `/eos/fader/1/4/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,357 | 59×59 | gray |  | `/eos/fader/1/4/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,358 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,358 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,454 | 29×57 | gray |  | `/eos/fader/1/5/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,454 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,454 | 422×57 | gray |  | `/eos/fader/1/5` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,454 | 59×58 | gray |  | `/eos/fader/1/5/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,454 | 59×59 | gray |  | `/eos/fader/1/5/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,454 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,455 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,550 | 29×57 | gray |  | `/eos/fader/1/6/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,551 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,550 | 422×57 | gray |  | `/eos/fader/1/6` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,550 | 59×58 | gray |  | `/eos/fader/1/6/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,550 | 59×59 | gray |  | `/eos/fader/1/6/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,551 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,551 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,647 | 29×57 | gray |  | `/eos/fader/1/7/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,647 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,647 | 422×57 | gray |  | `/eos/fader/1/7` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,647 | 59×58 | gray |  | `/eos/fader/1/7/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,647 | 59×59 | gray |  | `/eos/fader/1/7/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,647 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,648 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,743 | 29×57 | gray |  | `/eos/fader/1/8/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,743 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,743 | 422×57 | gray |  | `/eos/fader/1/8` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,743 | 59×58 | gray |  | `/eos/fader/1/8/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,743 | 59×59 | gray |  | `/eos/fader/1/8/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,744 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,744 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,840 | 29×57 | gray |  | `/eos/fader/1/9/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,840 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,840 | 422×57 | gray |  | `/eos/fader/1/9` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,840 | 59×58 | gray |  | `/eos/fader/1/9/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,840 | 59×59 | gray |  | `/eos/fader/1/9/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,841 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,841 | 20×58 | green | Play | `` | background=false, outline=false |
| push | 641,937 | 29×57 | gray |  | `/eos/fader/1/10/load` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 645,937 | 20×58 | gray | Load | `` | background=false, outline=false |
| faderh | 200,937 | 422×57 | gray |  | `/eos/fader/1/10` | response=absolute, inverted=false, centered=false, scalef=0.0, scalet=1.0 |
| push | 52,937 | 59×58 | gray |  | `/eos/fader/1/10/fire` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 123,937 | 59×59 | gray |  | `/eos/fader/1/10/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 142,937 | 20×59 | red | Stop | `` | background=false, outline=false |
| labelv | 71,937 | 20×58 | green | Play | `` | background=false, outline=false |

### Page 5 — "Cues"

- Adresse OSC de page (`osc_cs` du `tabpage`) : `/eos/reset`

- Nombre de contrôles : 68


| type | x,y | w×h | color | texte | osc_cs | autres attrs |
|---|---|---|---|---|---|---|
| labelv | 688,768 | 30×215 | orange |  | `` | background=false, outline=true |
| labelv | 70,369 | 557×614 | gray |  | `` | background=false, outline=true |
| labelv | 564,396 | 40×123 | gray |  | `` | background=true, outline=true |
| labelv | 734,2 | 34×190 | gray | Keyboard | `` | background=false, outline=false |
| labelv | 734,390 | 34×190 | gray | Groups | `` | background=false, outline=false |
| labelv | 734,196 | 34×190 | gray | Attributes | `` | background=false, outline=false |
| labelv | 734,585 | 34×190 | gray | Fader | `` | background=false, outline=false |
| labelv | 734,780 | 34×192 | orange | Cues | `` | background=false, outline=false |
| push | 427,570 | 80×200 | gray |  | `/eos/key/stop` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 306,570 | 80×200 | gray |  | `/eos/key/go_0` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 447,570 | 60×200 | gray | STOP | `` | background=false, outline=false |
| labelv | 427,570 | 60×200 | gray | BACK | `` | background=false, outline=false |
| labelv | 447,569 | 60×200 | gray | _ | `` | background=false, outline=false |
| push | 536,48 | 87×102 | gray |  | `/eos/key/7` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 536,153 | 87×102 | gray |  | `/eos/key/8` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 536,258 | 87×102 | gray |  | `/eos/key/9` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 446,48 | 87×102 | gray |  | `/eos/key/4` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 446,153 | 87×102 | gray |  | `/eos/key/5` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 446,258 | 87×102 | gray |  | `/eos/key/6` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 356,48 | 87×102 | gray |  | `/eos/key/1` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 356,153 | 87×102 | gray |  | `/eos/key/2` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 356,258 | 87×102 | gray |  | `/eos/key/3` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 266,48 | 87×102 | gray |  | `/eos/key/clear_cmd` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 569,48 | 20×102 | orange | 7 | `` | background=false, outline=false |
| labelv | 569,153 | 20×102 | orange | 8 | `` | background=false, outline=false |
| labelv | 569,258 | 20×102 | orange | 9 | `` | background=false, outline=false |
| labelv | 389,48 | 20×102 | orange | 1 | `` | background=false, outline=false |
| labelv | 479,153 | 20×102 | orange | 5 | `` | background=false, outline=false |
| labelv | 479,258 | 20×102 | orange | 6 | `` | background=false, outline=false |
| labelv | 479,48 | 20×102 | orange | 4 | `` | background=false, outline=false |
| labelv | 389,153 | 20×102 | orange | 2 | `` | background=false, outline=false |
| labelv | 389,258 | 20×102 | orange | 3 | `` | background=false, outline=false |
| labelv | 299,48 | 20×102 | gray | Clear | `` | background=false, outline=false |
| push | 163,48 | 87×102 | gray |  | `/eos/key/go_to_cue` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 196,48 | 20×102 | gray | Go to cue | `` | background=false, outline=false |
| labelv | 200,486 | 42×448 | gray |  | `/eos/out/active/cue/text` | background=false, outline=true |
| labelv | 130,487 | 42×447 | gray |  | `/eos/out/pending/cue/text` | background=false, outline=true |
| labelv | 200,417 | 42×84 | gray | Active: | `` | background=true, outline=true |
| labelv | 130,417 | 42×84 | gray | Pending: | `` | background=true, outline=true |
| labelv | 306,570 | 80×200 | gray | GO | `` | background=false, outline=false |
| push | 74,49 | 87×102 | gray |  | `/eos/key/shift` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 74,154 | 87×206 | gray |  | `/eos/key/enter` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 107,156 | 20×204 | gray | Enter | `` | background=false, outline=false |
| push | 562,870 | 42×84 | red |  | `/eos/key/blackout` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 562,870 | 42×84 | gray | Blackout | `` | background=false, outline=true |
| labelv | 107,49 | 20×102 | gray | Shift | `` | background=false, outline=false |
| push | 266,153 | 87×102 | gray |  | `/eos/key/0` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 266,258 | 87×102 | gray |  | `/eos/key/.` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 299,153 | 20×102 | orange | 0 | `` | background=false, outline=false |
| labelv | 299,258 | 35×102 | gray | . | `` | background=false, outline=false |
| push | 163,153 | 87×102 | gray |  | `/eos/key/out` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 163,258 | 87×102 | gray |  | `/eos/key/\` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 196,153 | 20×102 | gray | Out | `` | background=false, outline=false |
| labelv | 196,258 | 20×102 | gray | / | `` | background=false, outline=false |
| labelv | 688,44 | 30×597 | orange |  | `/eos/out/cmd` | background=true, outline=true |
| push | 692,772 | 22×102 | gray |  | `/eos/key/live` | local_off=false, scalef=0.0, scalet=1.0 |
| push | 692,877 | 22×102 | gray |  | `/eos/key/blind` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 693,772 | 20×102 | gray | Live | `` | background=false, outline=false |
| labelv | 693,877 | 20×102 | gray | Blind | `` | background=false, outline=false |
| led | 696,776 | 14×14 | orange |  | `/eos/out/event/state` | scalef=0.0, scalet=1.0 |
| led | 696,882 | 14×14 | blue |  | `/eos/out/event/state` | scalef=1.0, scalet=0.0 |
| push | 692,653 | 22×102 | gray |  | `/eos/key/clear_cmdline` | local_off=false, scalef=0.0, scalet=1.0 |
| labelv | 694,651 | 20×102 | gray | All Clear | `` | background=false, outline=false |
| labelv | 688,649 | 30×110 | orange |  | `` | background=false, outline=true |
| timev | 564,456 | 39×63 | gray |  | `` | seconds=false, background=false, outline=false |
| labelv | 569,398 | 30×67 | gray | Time: | `` | background=false, outline=false |
| labelv | 262,44 | 365×320 | gray |  | `` | background=false, outline=true |
| labelv | 69,44 | 186×320 | gray |  | `` | background=false, outline=true |

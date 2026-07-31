# EOS OSC Support — Supported OSC Commands (ETC Labs, 2017)

- Source : PDF officiel « EOS OSC Support / Supported OSC Commands », publié via `ETCLabs/EosSyncLib`
  (organisation GitHub officielle d'ETC, dépôt marqué « unofficial » mais maintenu par ETC), 2017-09-06.
- Fichier source : [`source/Supported_OSC_Commands.pdf`](source/Supported_OSC_Commands.pdf)
- Confiance : A (document ETC/ETCLabs). **Antérieur** au manuel v3.2.0 déjà importé (`manuals/operations-manual/31-show-control.md`) —
  en cas de divergence, le manuel v3.2.0 (2023) fait foi comme source la plus à jour. Ce document reste
  utile pour la colonne **« Min Eos Version »**, absente du manuel récent, qui précise depuis quelle
  version chaque commande OSC est disponible.
- Note de conversion : la table d'entrée (« Supported OSC Input ») est préservée en blocs de texte alignés
  (colonnes du PDF conservées telles quelles) pour garantir une fidélité totale — c'est une table dense
  à 4 colonnes (OSC Method / Arguments / Examples/Comments / Min Eos Version) que la conversion en tableau
  Markdown pipe aurait pu déformer. La section de sortie OSC (Explicit/Implicit Output) est en Markdown
  normal, sa structure d'origine étant déjà simple.

---

## Supported OSC Input

Tous les commandes OSC doivent commencer par `/eos/...` ou `/eos/user/<number>/...`. Par défaut,
l'utilisateur OSC est le même que l'utilisateur console courant. Il peut être fixé explicitement via
une commande OSC contenant une méthode `user` ; une fois fixé, il reste tel quel jusqu'à changement
explicite.

Exemples :
```
OSC Method
/eos/chan/<channel number>
/eos/user/<number>/chan/<channel number>
```

## Supported OSC Input — table complète des commandes

Format : blocs de texte alignés (préserve la structure en colonnes du document original : OSC Method | Arguments | Examples/Comments | Min Eos Version). Colonne « Min Eos Version » vide = disponible depuis toujours / non spécifiée.

### Absolute Levels

```text
 /eos/at                                               number for the          /eos/at=75
                                                       level                   (useful for mapping to an OSC slider)

                                                       number for the
                                                       button edge
 /eos/at/out                                                                   /eos/at/out
                                                       1.0=down, 0.0=up
                                                       (optional)

                                                       number for the
                                                       button edge
 /eos/at/home                                                                  /eos/at/home
                                                       1.0=down, 0.0=up
                                                       (optional)

                                                       number for the
                                                       button edge
 /eos/at/remdim                                                                /eos/at/remdim
                                                       1.0=down, 0.0=up
                                                       (optional)

                                                       number for the
                                                       button edge
 /eos/at/level                                                                 /eos/at/level
                                                       1.0=down, 0.0=up
                                                       (optional)

                                                       number for the
                                                       button edge
 /eos/at/full                                                                  /eos/at/full
                                                       1.0=down, 0.0=up
                                                       (optional)

                                                       number for the
                                                       button edge
 /eos/at/min                                                                   /eos/at/min
                                                       1.0=down, 0.0=up
                                                       (optional)
                               number for the
                               button edge
/eos/at/max                                       /eos/at/max
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/at/+%                                        /eos/at/+%
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/at/-%                                        /eos/at/-%
                               1.0=down, 0.0=up
                               (optional)

/eos/at/dmx                    number for the     /eos/at/dmx/128
                               DMX level          (useful for mapping to an OSC slider)

/eos/param/<parameter>         number for the     /eos/param/pan=270
                               level              (useful for mapping to an OSC slider)

                               number for the
                               button edge
/eos/param/<parameter>/out                        /eos/param/pan/out
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/param/<parameter>/home                       /eos/param/pan/home
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/param/<parameter>/level                      /eos/param/pan/level
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/param/<parameter>/full                       /eos/param/pan/full
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/param/<parameter>/min                        /eos/param/pan/min
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/param/<parameter>/max                        /eos/param/pan/max
                               1.0=down, 0.0=up
                               (optional)

                               number for the
                               button edge
/eos/param/<parameter>/+%                         /eos/param/pan/+%
                               1.0=down, 0.0=up
                               (optional)
                                             number for the
                                             button edge
/eos/param/<parameter>/-%                                          /eos/param/pan/-%
                                             1.0=down, 0.0=up
                                             (optional)
```

### Variations

```text
/eos/param/<parameter 1>/<parameter 2>/...   number for all        /eos/param/pan/tilt=45
                                             parameter levels      (set pan & tilt to 45)

                                             multiple numbers      /eos/param/pan/tilt=45,90
                                             for each parameter    (set pan to 45 & tilt to 90)
                                             level
```

### Color

```text
/eos/color/hs                                Argument 1: Hue
                                             (0.0-360.0)
                                                                   /eos/color/hs=330.0, 75.0
                                             Argument 2:                                                          2.6.0
                                                                   (pink color with 75% saturation)
                                             Saturation (0.0-
                                             100.0)

/eos/color/hsxy                              Argument 1: X (0.0-   For simulating the Hue/Saturation wheel
                                             1.0)                  in a 2D XY graph where bottom-left
                                             Argument 2: Y (0.0-   corner is (0.0, 0.0) and top-right corner it
                                             1.0)                  (1.0, 1.0)                                     2.6.0

                                                                   /eos/color.hsxy=0.82, 0.31
                                                                   (pink color with 75% saturation)

/eos/color/rgb                               Argument 1: Red
                                             (0.0-1.0)
                                             Argument 2: Green     /eos/color/rgb=1.0, 0.25, 0.63
                                                                                                                  2.6.0
                                             (0.0-1.0)             (pink color with 75% saturation)
                                             Argument 3: Blue
                                             (0.0-1.0)

/eos/color/xy                                Argument 1: x (0.0-   For setting (x, y) chromaticity point in the
                                             1.0)                  CIE 1931 xyY color space
                                             Argument 2: y (0.0-                                                  2.6.0
                                             1.0)                  /eos/color/xy=0.464, 0.254
                                                                   (pink color with 75% saturation)

/eos/color/xyz                               Argument 1: X         For setting (X, Y, Z) color point in XYZ
                                             Argument 2: Y         color space
                                             Argument 3: Z                                                        2.6.0
                                                                   /eos/color/xyz=0.851, 0.466, 0.516
                                                                   (pink color with 75% saturation)
```

### Pan/Tilt

```text
/eos/pantilt/xy                              Argument 1: X (0.0-   For 2D Pan/Tilt graph where bottom-left
                                             1.0)                  corner is (0.0, 0.0) and top-right corner if
                                                                                                                  2.6.0
                                             Argument 2: Y (0.0-   (1.0, 1.0)
                                             1.0)
```

### Wheel

```text
/eos/wheel/level                                       number for wheel        /eos/wheel/level=1.0
                                                       ticks for the           (increase value)
                                                       specified wheel
                                                       mode (positive or       /eos/wheel/level=-1.0
                                                       negative)               (decrase value)

                                                                               /eos/wheel/level=4.0
                                                                               (increase valid rapidly)

                                                                               (defaults to Coarse mode, but wheel
                                                                               mode can be changed with
                                                                               the /eos/wheel command below)

                                                       number for wheel
/eos/wheel                                             mode: 0=coarse,         /eos/wheel=1.0
                                                       1=fine

                                                       number for wheel
/eos/wheel/<parameter>                                 ticks (positive or      /eos/wheel/pan=1.0
                                                       negative)

                                                       number for wheel
/eos/wheel/<parameter 1>/<parameter 2>/...             ticks (positive or      /eos/wheel/pan/tilt=1.0
                                                       negative)

                                                       number for fine
/eos/wheel/fine/<parameter>                            wheel ticks (positive   /eos/wheel/fine/pan=1.0
                                                       or negative)

                                                       number for fine
/eos/wheel/fine/<parameter 1>/<parameter 2>/...        wheel ticks (positive   /eos/wheel/fine/pan/tilt=1.0
                                                       or negative)

                                                       number for coarse
/eos/wheel/coarse/<parameter>                          wheel ticks (positive   /eos/wheel/coarse/pan=1.0
                                                       or negative)

                                                       number for coarse
/eos/wheel/coarse/<parameter 1>/<parameter
                                                       wheel ticks (positive   /eos/wheel/coarse/pan/tilt=1.0
2>/...
                                                       or negative)
```

### Switch

```text
NOTE: "switch" is a variant of "wheel" with the added functionality of continuously repeating wheel ticks until a
subsequent OSC switch command sets the wheel ticks to zero.
This may be used to continuously tick a wheel while a button is held down, for example. The expected argument range
is -1.0 to 1.0, which affects the tick rate accordingly, but can be a smaller or larger range for more subtle or rapid
movement.

/eos/switch/level

/eos/switch

/eos/switch/<parameter>

/eos/switch/<parameter 1>/<parameter 2>/...

/eos/switch/fine/<parameter>

/eos/switch/fine/<parameter 1>/<parameter 2>/...
/eos/switch/coarse/<parameter>

/eos/switch/coarse/<parameter 1>/<parameter 2>/...
```

### Active Parameters

```text
NOTE: <index> is a 1-based index referencing the list of current parameters for the selected channel(s).
Eos will send the parameter name and current value for each active parameter, so that the wheels on your OSC-enabled
device may be labeled appropriately...
See the OSC output section below for details.

/eos/active/wheel/<index>                            number of wheel          /eos/active/wheel/1=1.0
                                                     ticks for the specific   (increase value)
                                                     wheel
                                                     mode (positive or        /eos/active/wheel/1=-1.0
                                                     negative)                (decrease value)

                                                                              /eos/active/wheel/1=4.0
                                                                              (increase value rapidly)

                                                                              (defaults to Coarse mode, but wheel
                                                                              mode can be changed with
                                                                              the /eos/wheel command)

                                                     number of fine
/eos/active/wheel/fine/<index>                       wheel ticks (positive    /eos/active/wheel/fine/1=1.0
                                                     or negative)

                                                     number of coarse
/eos/active/wheel/coarse/<index>                     wheel ticks (positive    /eos/active/wheel/coarse/1=1.0
                                                     or negative)

/eos/active/switch/<index>                           number of wheel          /eos/active/switch/1=1.0
                                                     ticks for the specific   (increase value)
                                                     switch
                                                     mode (positive or        /eos/active/switch/1=-1.0
                                                     negative)                (decrease value)

                                                                              /eos/active/switch/1=4.0
                                                                              (increase value rapidly)


                                                                              /eos/active/switch/1=0.25
                                                                              (increase value slowly)

                                                                              (defaults to Coarse mode, but wheel
                                                                              mode can be changed with
                                                                              the /eos/switch command)

                                                     number of fine
/eos/active/switch/fine/<index>                      wheel ticks (positive    /eos/active/switch/fine/1=1.0
                                                     or negative)

                                                     number of coarse
/eos/active/switch/coarse/<index>                    wheel ticks (positive    /eos/active/switch/coarse/1=1.0
                                                     or negative)
```

### Subscribe to Specific Parameters

```text
NOTE: once subscribed, Eos will reply with an osc packet per parameter as they change. Ex: /eos/out/param/pan See
                                                                                                                            2.6.0
output section below for details.

                                                        1=subscribe,
/eos/subscribe/param/<parameter>                                               /eos/subscribe/param/red=1                   2.6.0
                                                        0=unsubscribe

/eos/subscribe/param/<parameter 1>/<parameter           1=subscribe,
                                                                               /eos/subscribe/param/pan/tilt=1              2.6.0
2>/...                                                  0=unsubscribe
```

### OSC Output Filter

```text
NOTE: used to limit OSC traffic to devices that only need specific OSC messages from Eos                                    2.6.1

/eos/filter/add                                         one or more string     When one or more filters are set, then
                                                        arguments,             Eos will only send OSC messages to the
                                                        representing           device that match the filters.
                                                        filters(s) that may
                                                        contain "*"            Ex:
                                                                                                                            2.6.1
                                                        wildcards              /eos/filter/add=/eos/out/param/*

                                                                               (Eos will only send OSC messages to this
                                                                               device that start with
                                                                               "/eos/out/param/")

/eos/filter/remove                                      one or more string     Remove an existing filter
                                                        arguments,
                                                        representing           /eos/filter/remove=/eos/out/param/*
                                                                                                                            2.6.1
                                                        filters(s) that may
                                                        contain "*"
                                                        wildcards

/eos/filter/clear                                                              Clear all filters, so that the device will
                                                                                                                            2.6.1
                                                                               receive all OSC messages from Eos
```

### Direct Select Banks

```text
NOTE:

<index> is a 1-based index of any number of OSC direct select banks you wish to create.

<target type> may be one of the following:
chan
group
macro
sub
preset
ip (intensity palette)
fp (focus palette)
cp (color palette)
bp (beam palette)
ms (magic sheet)
curve
snap (snapshot)
fx (effects)
pixmap

Eos will send the description and button labels for all OSC direct select banks. See the OSC output section below for
details.
/eos/ds/<index>/<target type>/<button count>                                    /eos/ds/1/chan/10
                                                                                (create OSC direct select bank #1 with 10
                                                                                channel buttons)

                                                                                /eos/ds/2/group/25
                                                                                (create OSC direct select bank #2 with
                                                                                25 group buttons)

/eos/ds/<index>/<target type>/flexi/<button count>                              /eos/ds/1/chan/flexi/10
                                                                                (create OSC direct select bank #1 with 10
                                                                                channel buttons, in flexi mode)

/eos/ds/<index>/<target type>/<page                                             /eos/ds/1/chan/3/10
number>/<button count>                                                          (create OSC direct select bank #1 with 10
                                                                                channel buttons on page 3)
                                                                                Can also be used to quick jump to a
                                                                                specific page

/eos/ds/<index>/<target type>/flexi/<page                                       /eos/ds/1/chan/flexi/3/10
number>/<button count>                                                          (create OSC direct select bank #1 with 10
                                                                                channel buttons on page 3, in flexi mode)
                                                                                Can also be used to quick jump to a
                                                                                specific page

/eos/ds/<index>/page/<delta>                            number for page         /eos/ds/1/page/1
                                                        delta                   (page down by 1)

                                                                                /eos/ds/1/page/-1
                                                                                (page up by 1)

                                                                                /eos/ds/1/page/10
                                                                                (page down by 10)

/eos/ds/<index>/<button index>                          number for button       /eos/ds/1/1=1.0
                                                        edge: 1.0=down,         (press first button of OSC direct select
                                                        0.0=up (optional)       bank #1)

                                                                                /eos/ds/1/1=0.0
                                                                                (release first button of OSC direct select
                                                                                bank #1)
```

### Fader Banks

```text
NOTE: <index> is a 1-based index of any number of OSC fader banks you wish to create.
NOTE: use an <index> of zero to reference the master fader

Eos will send the description and fader labels for all OSC fader banks. See the OSC output section below for details.

/eos/fader/<index>/config/<fader count>                                         /eos/fader/1/config/10
                                                                                (create OSC fader bank #1 with 10 faders)

/eos/fader/<index>/config/<page number>/<fader                                  /eos/fader/1/config/2/10
count>                                                                          (create OSC fader bank #1 with 10 faders
                                                                                on page 2)
                                                                                Can also be used to quick jump to a
                                                                                specific page
/eos/fader/<index>/page/<delta>                                                 /eos/fader/1/page/1
                                                                                (page down by 1)

                                                                                /eos/fader/1/page/-1
                                                                                (page up by 1)

                                                                                /eos/fader/1/page/10
                                                                                (page down by 10)

/eos/fader/<index>/<fader index>                         floating point         /eos/fader/1/2=0.75
                                                         number to set sub      (set the second fader in OSC fader bank
                                                         percent to             #1 to 75%)

/eos/fader/<index>/<fader index>/load                    number for button
                                                         edge: 1.0=down,        /eos/fader/1/2/load
                                                         0.0=up (optional)

/eos/fader/<index>/<fader index>/unload                                         /eos/fader/1/2/unload

/eos/fader/<index>/<fader index>/stop                    number for button
                                                         edge: 1.0=down,        /eos/fader/1/2/stop
                                                         0.0=up (optional)

/eos/fader/<index>/<fader index>/fire                    number for button
                                                         edge: 1.0=down,        /eos/fader/1/2/fire
                                                         0.0=up (optional)

/eos/fader/<index>/<fader index>/out                                            /eos/fader/1/2/out

/eos/fader/<index>/<fader index>/home                                           /eos/fader/1/2/home

/eos/fader/<index>/<fader index>/min                                            /eos/fader/1/2/min

/eos/fader/<index>/<fader index>/max                                            /eos/fader/1/2/max

/eos/fader/<index>/<fader index>/full                                           /eos/fader/1/2/full

/eos/fader/<index>/<fader index>/level                                          /eos/fader/1/2/level

/eos/fader/<index>/<fader index>/+%                                             /eos/fader/1/2/+%

/eos/fader/<index>/<fader index>/-%                                             /eos/fader/1/2/-%
```

### Cue List Banks

```text
NOTE: <index> is a 1-based index of any number of OSC cue list banks you wish to create.
                                                                                                                               2.6.0
Eos will send the cue list label and cue information for all OSC cue list banks. See the OSC output section below for
details.

/eos/cuelist/<index>/config/<cue list                                           /eos/cuelist/1/config/2/3/6
number>/<num prev cues>/<num pending cues>                                      (create OSC cue list bank #1 for cue list 2,
                                                                                showing 3 previous cues, the current cue,
                                                                                and 6 pending cues)                            2.6.0

                                                                                NOTE: set <cue list number> to zero to
                                                                                follow the current cue list
/eos/cuelist/<index>/config/<cue list                                         /eos/cuelist/1/config/2/3/6/10
number>/<num prev cues>/<num pending                                          (create OSC cue list bank #1 for cue list 2,
cues>/<offset>                                                                showing 3 previous cues, the current cue,
                                                                              and 6 pending cues, starting at offset 10
                                                                              into the cue list)

                                                                              offset is a zero-based index into the          2.6.0
                                                                              entire cue list, where each cue counts as
                                                                              one item and each cue part counts as
                                                                              one item

                                                                              NOTE: set <cue list number> to zero to
                                                                              follow the current cue list

/eos/cuelist/<index>/page/<delta>                                             /eos/cuelist/1/page/1
                                                                              (page OSC cue list bank down 1 row)

                                                                              /eos/cuelist/1/page/-1
                                                                              (page OSC cue list bank up 1 row)              2.6.0

                                                                              /eos/cuelist/1/page/0
                                                                              (jump back to the current cue and follow
                                                                              it)

/eos/cuelist/<index>/select/<cue number>                                      /eos/cuelist/1/select/100.4
                                                                                                                             2.6.0
                                                                              (jump to cue 100.4)
```

### Key

```text
NOTE: for a list of supported key names - in the magic sheet editor select "Console Button" magic sheet item, and see
the list of [Hard Keys] options

/eos/key/<name>                                        number for button      /eos/key/select active=1.0
                                                       edge: 1.0=down,        (press [Select Active] button)
                                                       0.0=up (optional)
                                                                              /eos/key/select active=0.0
                                                                              (release [Select Active] button)

                                                                              /eos/key/go 0
                                                                              (press & release [Go] button)

                                                                              NOTE: for the slash key use a backslash:
                                                                              "/eos/key/\"
```

### Softkey

```text
NOTE: <index> is 1-based index into the softkey list. There are 6 softkeys and 2 pages, so valid <index> numbers are 1-
12.
                                                                                                                             2.6.0
Eos will send out softkey labels as /eos/out/softkey/<index>. See the OSC output section below for details.

                                                                              /eos/softkey/1=1.0
                                                       number for button      (press 1st softkey)
/eos/softkey/<index>                                   edge: 1.0=down,                                                       2.6.0
                                                       0.0=up (optional)      /eos/softkey/1=0.0
                                                                              (release 1st softkey)
```

### Address

```text
                                       number for address
/eos/addr                                                     /eos/addr=513
                                       to select

/eos/addr/<address>                    number for level to    /eos/addr/513=100
                                       set address to         (useful for mapping to an OSC slider)

/eos/addr/<address>/dmx                number for DMX
                                                              /eos/addr/513/dmx=255
                                       level to set address
                                                              (useful for mapping to an OSC slider)
                                       to
```

### Chan

```text
                                       number for channel
/eos/chan                                                     /eos/chan=1
                                       to select

/eos/chan/<number>                     number for channel     /eos/chan/1=75
                                       level                  (useful for mapping to an OSC slider)

                                       number for button
/eos/chan/<number>/out                 edge: 1.0=down,        /eos/chan/1/out
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/home                edge: 1.0=down,        /eos/chan/1/home
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/remdim              edge: 1.0=down,        /eos/chan/1/remdim
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/level               edge: 1.0=down,        /eos/chan/1/level
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/full                edge: 1.0=down,        /eos/chan/1/full
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/min                 edge: 1.0=down,        /eos/chan/1/min
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/max                 edge: 1.0=down,        /eos/chan/1/max
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/+%                  edge: 1.0=down,        /eos/chan/1/+%
                                       0.0=up (optional)

                                       number for button
/eos/chan/<number>/-%                  edge: 1.0=down,        /eos/chan/1/-%
                                       0.0=up (optional)

                                       number for channel
/eos/chan/<number>/dmx                                        /eos/chan/1/dmx=255
                                       DMX level

/eos/chan/<number>/param/<parameter>   number for             /eos/chan/1/param/pan=90
                                       parameter level        (useful for mapping to an OSC slider)
/eos/chan/<number>/param/<parameter                 number for all
                                                                         /eos/chan/1/param/pan/tilt=90
1>/<parameter 2>/...                                parameter levels
                                                                         (set channel 1 pan & tilt to 90)
                                                    multiple numbers
                                                                         /eos/chan/1/param/pan/tilt=45,90
                                                    for each parameter
                                                                         (set channel 1 pan to 45 & tilt to 90)
                                                    level

                                                    number for
/eos/chan/<number>/param/<parameter>/dmx            parameter DMX        /eos/chan/1/param/pan/dmx=255
                                                    level

                                                    number(s) for
/eos/chan/<number>/param/<parameter
                                                    parameter DMX        /eos/chan/1/param/pan/tilt/dmx=255
1>/<parameter 2>/.../dmx
                                                    level(s)
```

### Group

```text
NOTE: same syntax and behavior as /eos/chan/... above

/eos/group

/eos/group/<number>

/eos/group/<number>/out

/eos/group/<number>/home

/eos/group/<number>/level

/eos/group/<number>/full

/eos/group/<number>/min

/eos/group/<number>/max

/eos/group/<number>/+%

/eos/group/<number>/-%

/eos/group/<number>/dmx

/eos/group/<number>/param/<parameter>

/eos/group/<number>/param/<parameter 1>/<parameter 2>/...

/eos/group/<number>/param/<parameter>/dmx

/eos/group/<number>/param/<parameter 1>/<parameter 2>/.../dmx
```

### Macro

```text
                                                    number for macro
/eos/macro                                                               /eos/macro=1
                                                    to select

                                                    number for macro
/eos/macro/fire                                                          /eos/macro/fire=1
                                                    to run

                                                    number for button
/eos/macro/<number>/fire                            edge: 1.0=down,      /eos/macro/1/fire=1.0
                                                    0.0=up (optional)
Sub

                            number for sub to
/eos/sub                                          /eos/sub=1
                            select

/eos/sub/<number>           floating point
                                                  /eos/sub/1=0.75
                            number to set sub
                                                  (useful for mapping to an OSC slider)
                            percent to

                            number for button
/eos/sub/<number>/out       edge: 1.0=down,       /eos/sub/1/out
                            0.0=up (optional)

                            number for button
/eos/sub/<number>/home      edge: 1.0=down,       /eos/sub/home
                            0.0=up (optional)

                            number for button
/eos/sub/<number>/level     edge: 1.0=down,       /eos/sub/1/level
                            0.0=up (optional)

                            number for button
/eos/sub/<number>/full      edge: 1.0=down,       /eos/sub/1/full
                            0.0=up (optional)

                            number for button
/eos/sub/<number>/min       edge: 1.0=down,       /eos/sub/1/min
                            0.0=up (optional)

                            number for button
/eos/sub/<number>/max       edge: 1.0=down,       /eos/sub/max
                            0.0=up (optional)

                            number for sub to
/eos/sub/fire                                     /eos/sub/fire=1
                            bump

/eos/sub/<number>/fire      number for button     /eos/sub/1/fire=1.0
                            edge: 1.0=down,       (bump sub 1 on)
                            0.0=up (optional)
                                                  /eos/sub/1/fire=0.0
                                                  (bump sub 1 off)
```

### Preset

```text
                            number of preset to
/eos/preset                                       /eos/preset=1
                            select

                            number of preset to
/eos/preset/fire                                  /eos/preset/fire=1
                            recall

                            number for button
/eos/preset/<number>/fire   edge: 1.0=down,       /eos/preset/1/fire
                            0.0=up (optional)
```

### Intensity Palette

```text
                            number of intensity
/eos/ip                                           /eos/ip=1
                            palette to select
                                      number of intensity
/eos/ip/fire                                                /eos/ip/fire=1
                                      palette to recall

                                      number for button
/eos/ip/<number>/fire                 edge: 1.0=down,       /eos/ip/1/fire
                                      0.0=up (optional)
```

### Focus Palette

```text
                                      number of focus
/eos/fp                                                     /eos/fp=1
                                      palette to select

                                      number of focus
/eos/fp/fire                                                /eos/fp/fire=1
                                      palette to recall

                                      number for button
/eos/fp/<number>/fire                 edge: 1.0=down,       /eos/fp/1/fire
                                      0.0=up (optional)
```

### Color Palette

```text
                                      number of color
/eos/cp                                                     /eos/cp=1
                                      palette to select

                                      number of color
/eos/cp/fire                                                /eos/cp/fire=1
                                      palette to recall

                                      number for button
/eos/cp/<number>/fire                 edge: 1.0=down,       /eos/cp/1/fire
                                      0.0=up (optional)
```

### Beam Palette

```text
                                      number of beam
/eos/bp                                                     /eos/bp=1
                                      palette to select

                                      number of beam
/eos/bp/fire                                                /eos/bp/fire=1
                                      palette to recall

                                      number for button
/eos/bp/<number>/fire                 edge: 1.0=down,       /eos/bp/1/fire
                                      0.0=up (optional)
```

### Cue

```text
                                      number of cue to
/eos/cue                                                    /eos/cue=1.5
                                      select

                                      number of cue to
/eos/cue/<list number>                select (in the        /eos/cue/1=1.5
                                      specified cue list)

                                      number of cue part
                                      to select (in the
/eos/cue/<list number>/<cue number>                         /eos/cue/1/1.5=2
                                      specified cue list
                                      and cue number)

                                      number of cue to
/eos/cue/fire                                               /eos/cue/fire=1
                                      run
                                            number for button
/eos/cue/<cue number>/fire                  edge: 1.0=down,       /eos/cue/1.5/fire
                                            0.0=up (optional)

                                            number for button
/eos/cue/<list number>/<cue number>/fire    edge: 1.0=down,       /eos/cue/1/1.5/fire
                                            0.0=up (optional)

                                            number for button
/eos/cue/<list number>/<cue number>/<part
                                            edge: 1.0=down,       /eos/cue/1/1.5/2/fire
number>/fire
                                            0.0=up (optional)
```

### Magic Sheet

```text
                                            number of the
/eos/ms                                                           /eos/ms=1
                                            magic sheet to open

                                            number of the
/eos/<ms number>                            magic sheet view to   /eos/ms/1=2
                                            open (optional)
```

### Other Targets

```text
                                            number of curve to
/eos/curve                                                        /eos/curve=1
                                            select

                                            number of effect to
/eos/fx                                                           /eos/fx=1
                                            select

                                            number of snapshot
/eos/snap                                                         /eos/snap=1
                                            to recall

                                            numer of pixel map
/eos/pixmap                                                       /eos/pixmap=1
                                            to select
```

### Command Line

```text
/eos/cmd                                    string with           /eos/cmd="Chan 1 At 75"
                                            command line text     (unterminated command)

                                                                  /eos/cmd="Chan 1 At 75#"
                                                                  (terminated command)

                                                                  /eos/cmd="Chan 1 At 75 Enter"
                                                                  (terminated command)

/eos/cmd                                    in-line command       /eos/cmd="Chan 1 At %1#", 75
                                            line arguments        (results in command line "Chan 1 At 75#"

                                                                  /eos/cmd="Chan %1 At %2#", 1, 75

/eos/cmd/<text>/<text>/<text>/...           in-line command
                                                                  /eos/cmd/Chan/1/At/75
                                            line arguments
                                                                  /eos/cmd/Chan/%1/At/%2#=1, 75
                                            (optional)

/eos/newcmd                                 same behavior as /eos/cmd, but reset the command line first

/eos/event                                  same behavior as /eos/cmd, but treated as console event

/eos/newevent                               same behavior as /eos/event, but reset the command line first
 User

 /eos/user                                               number for OSC        /eos/user=1
                                                         user ID               (set OSC user ID to 1)

                                                                               /eos/user=-1
                                                                               (set OSC user to match console)

                                                                               /eos/user=0
                                                                               (set OSC user as background user)
```

### Other

```text
 /eos/reset                                                                    /eos/reset

                                                                               clears any active switches
                                                                               resets all persistent OSC settings (like
                                                                               OSC user ID & wheel modes)
                                                                               send ALL implicit OSC output commands
```

---

## Explicit OSC Output

OSC output exactement comme une sortie Serial String, mais la chaîne doit commencer par une adresse
OSC (ex : `/device/fader`). Il est possible d'ajouter des arguments en ajoutant `=` à la chaîne, suivi
d'une liste d'arguments séparés par des virgules.

- Arguments numériques avec décimale → traités comme des nombres flottants 32 bits
- Arguments numériques sans décimale → traités comme des entiers 32 bits
- Arguments non numériques → traités comme des chaînes

Exemples :
```
"/device/command"
"/device/command=1"
"/device/command=1.5"
"/device/command=1.5,3.0"
"/device/command=1.5,3.0,text"
```

## Implicit OSC Output

Quand la transmission UDP est activée, certaines commandes OSC sont émises automatiquement :

### Command Lines

```
"/eos/out/user/<number>/cmd", <string argument with current command line text>, <int32 argument 1=error, 0=no error (Eos 2.6.0+)>
"/eos/out/cmd", <string argument with current command line text for the current console user>, <int32 argument 1=error, 0=no error (Eos 2.6.0+)>
```

### Softkeys

```
"/eos/out/softkey/<index>", <string argument with softkey label>
```
- `<index>` est en base 1, plage valide 1-12 (2 pages de 6 softkeys)
- Nécessite Eos 2.6.0

### OSC Settings

```
"/eos/out/user", <integer argument with current OSC user ID>
"/eos/out/wheel", <float argument with current OSC wheel mode: 0.0=Coarse, 1.0=Fine>
"/eos/out/switch", <float argument with current OSC switch mode: 0.0=Coarse, 1.0=Fine>
"/eos/out/show/name", <string argument with show title>
```

### Active Channels and Parameters

```
"/eos/out/active/chan", <string argument with active channels and current value from the 1st channel>
"/eos/out/active/wheel/<number>", <string argument with parameter name and current value from the 1st channel>, <uint32 argument for parameter category, Eos 2.6.0+>
```
- Permet de créer une interface façon ML-Controls via OSC (ex : 10 molettes `/eos/active/wheel/<1-10>` avec libellés correspondants)
- Si utilisé avec `/eos/active/switch/<number>`, utiliser quand même `/eos/out/active/wheel/<number>` pour le feedback de ce switch

Table des catégories de paramètre (confirme et recoupe le corpus, entrée déjà connue) :

| Category | Number |
|---|---|
| Intensity | 1 |
| Focus | 2 |
| Color | 3 |
| Image | 4 |
| Form | 5 |
| Shutter | 6 |

```
"/eos/out/color/hs", <float argument: hue (0.0-360.0)> <float argument: saturation (0.0-100.0)>
```
- Si la sélection de channels ne contient pas de couleur, la commande est quand même envoyée, sans argument
- Nécessite Eos 2.6.0

```
"/eos/out/pantilt", <float argument: pan range min> <float argument: pan range max> <float argument: tilt range min> <float argument: tilt range max> <float argument: pan level> <float argument: tilt level>
```
- Si la sélection ne contient pas de paire pan/tilt, la commande est quand même envoyée, sans argument
- Nécessite Eos 2.6.0 — **confirme et recoupe** le mécanisme `parsePanTiltRange` déjà documenté dans
  `reference/JOURNAL_observations_nomad.md` (2026-07-19)

### Parameter Subscriptions

Après abonnement à un ou plusieurs paramètres via `/eos/subscribe/param/<parameter>`, Eos envoie un
paquet OSC pour chaque paramètre à chaque changement :

```
"/eos/out/param/<parameter>", <float argument: level>, <float argument: range min>, <float argument: range max>
```
- Si la sélection ne contient pas le paramètre, la commande est quand même envoyée, sans argument
- Nécessite Eos 2.6.0

### Active Cue

Mise à jour une fois par seconde.

```
"/eos/out/active/cue/<cue list number>/<cue number>", <float argument with percent complete (0.0-1.0)>
"/eos/out/active/cue", <float argument with percent complete (0.0-1.0)>
"/eos/out/active/cue/text", <string argument with descriptive text about the active cue, ex: "1/2.3 Label 0:05 75%">
"/eos/out/pending/cue/<cue list number>/<cue number>"
"/eos/out/pending/cue/text", <string argument with descriptive text about the pending cue, ex: "1/2.4 Label 0:30">
```

### OSC Direct Select Banks

```
"/eos/out/ds/<index>", <string argument with descriptive text for the OSC direct select at <index>: target name, page number, and mode>
"/eos/out/ds/<index>/<button index>", <string argument with button label for OSC direct select at <index> for button <button index>>, <string argument for direct select tile number (Eos 2.6.0+)>
```

### OSC Fader Banks

```
"/eos/out/fader/<index>", <string argument with descriptive text for the OSC fader bank at <index>>
"/eos/out/fader/<index>/<fader index>/name", <string argument with fader label for OSC fader bank at <index> for fader <fader index>>
"/eos/fader/<index>/<fader index>", <floating point number for fader percent: 0.0-1.0>
```
- **Note officielle confirmant le comportement déjà observé au banc et documenté dans le corpus** :
  Eos retarde l'envoi des niveaux de fader modifiés via OSC de **3 secondes**. Si un fader est déplacé
  depuis une télécommande OSC, Eos envoie le niveau réel 3 secondes plus tard.
  ⚠️ Ce délai de 3 s est la valeur **documentée officiellement (2017)** ; le journal terrain
  (`reference/JOURNAL_observations_nomad.md`, 2026-07-03) avait mesuré un écho réel à **~522 ms** sur
  nomad 3.3.5.69 en 2026 — écart significatif entre la doc de 2017 (~Eos 2.x) et le comportement mesuré
  sur une version bien plus récente. Cohérent avec la fenêtre anti-écho de 4 s déjà retenue dans ce
  projet pour couvrir les deux cas.

### OSC Cue List Banks

```
"/eos/out/cuelist/<index>", <string argument with cue list label>, <uint32 argument with total # of cues>, <int32 argument with cue list follow time (ms)>
"/eos/out/cuelist/<index>/<cue index>", <string argument with descriptive label including cue number, label, time remaining, state>, <string argument cue number>, <string argument label>, <string argument notes>, <string argument scene>, <bool scene end>, <int32 argument duration(ms)>, <int32 argument remaining(ms)>
```
- `remaining (ms)` : -1 = cue inactive, 0 = cue terminée (orange), positif = cue en cours d'exécution (rouge)
- Nécessite Eos 2.6.0

### OSC Show Control Events

```
"/eos/out/event/cue/<cue list number>/<cue number>/fire", <string argument with cue label (Eos 2.6.0+)>
"/eos/out/event/cue/<cue list number>/<cue number>/stop"
"/eos/out/event/cue/<cue list number>/0/resume"
"/eos/out/event/sub/<sub number>", <integer argument, 0=Bump Off, 1=Bump On>
"/eos/out/event/macro/<macro number>"
"/eos/out/event/relay/<relay number>/<group number>", <integer argument, 0=On, 1=Off>
"/eos/out/event" (used for time code learn)
```

### Misc. Console Events

```
"/eos/out/event/show/saved", <string argument with file path>
"/eos/out/event/show/loaded", <string argument with file path>
"/eos/out/event/show/cleared"
"/eos/out/event/state", <integer argument, 0=Blind, 1=Live>
```

### Other

Quand Eos reçoit la commande `/eos/ping`, il répond par `/eos/out/ping`. Il est possible d'ajouter
n'importe quel nombre d'arguments ; Eos répond avec les mêmes arguments — utile par exemple pour
mesurer la latence.

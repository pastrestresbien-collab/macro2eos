# Eos Family User Manual v3.2.0 — Chapitre 08 : Fan

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 8
## Fan
### About Fan

Fan provides the ability to spread parameter and timing values in a range across a channel selection set and have those values be evenly spaced. Fan is applied by channel selection or group order. By default, fan operation is from the start channel.

> **Note:** *[Fan] is used in the examples below. Ion Classic and Element Classic users will need to use {Fan}.*

When [Fan] is pressed after a channel selection, the softkeys will repaint to the following fan styles:

-   {Center} - The middle channel in the order is set as the start and will remain unchanged, and the first and last channels will change in different directions. The level wheel will decrease the lower number channels and increase the higher number channels.

-   {Reverse} - The selected channel order is reversed before applying the fan.

-   {Mirror Out} - The middle channel in the selected order is used as the starting channel and the first and last channels in the order are the end channels.

-   [1] [Thru] [1][0] [At] [1][0] [Thru] [3][0] [Fan] {Mirror Out} [Enter] - sets channel 1 to 30%, 2 to 20%, 3 to 10%, 4 to 20%, and 5 to 30%.

-   {Repeat} - The number of channels that are fanned before the pattern is repeated.

-   [1] [Thru] [1][2] [At] [5][0] [Thru] [7][0] [Fan] {Repeat} [3] [Enter] - sets channels 1,4,7,

> and 10 at 50%, 2,5,8, and 11 at 60%, and 3,6,9, and 12 at 70%.

-   {Cluster} - The channels are put into collections, which contains channels with all of the same value.

-   [1] [Thru] [1][2] [At] [5][0] [Thru] [8][0] [Fan] {Cluster} [4] [Enter] - sets channels 1

> through 3 at 50%, 4 through 6 at 60%, 7 through 9 at 70%, 10 through 12 at 80%.

-   {Random} - The selected channels are put in a random order before fan is applied.

### Fanning Parameter Data

> **Note:** *[Fan] is used in the examples below. Ion Classic and Element Classic users will need to use {Fan}.*

Fan values can be adjusted with encoders (if available), ML Controls, or via the keypad. To adjust the fan values with an encoder, select the required channels and provide a baseline, if necessary, followed by [Fan].

If no value is entered, the current values will be used. If using physical or virtual encoders to adjust fan, it is not necessary to specify the parameter to be fanned. This is determined by the encoder used.

-   [1] [Thru] [5] [Fan] [Enter] - selects the channels 1 through 5 and puts encoders and level wheel into fan mode.

-   [1] [Thru] [5] [At] [5] <0> [Fan] [Enter] - selects the channels 1 through 5, sets a start level of 50% and puts encoders and level wheel into fan mode.

-   [1] [Thru] [5] [Fan] {Mirror} [Enter] - selects the channels 1 through 5 and puts encoders and level wheel into fan mode with mirror style.

### Fan From the Command Line

> **Note:** *[Fan] is used in the examples below. Ion Classic and Element Classic users will need to use {Fan}.*

A level or time command that uses [Thru] or a list of references is a command line fan command. Using the [Fan] key is not necessary unless a fan style other than the default is needed.

To adjust the fan values from the command line:

-   [1] [Thru] [5] [At] [1] <0> [Thru] [5] <0> [Enter] - sets channel 1 to 10%, 2 to 20%, 3 to 30%, 4 to 40%, and 5 to 50%. This is the default fan adjustment and the [Fan] command is not necessary.

-   [1] [Thru] [5] [At] [1] <0> [Thru] [3] <0> [Fan] {Mirror} [Enter] - sets channel 1 to 30%,

> 2 to 20%, 3 to 10%, 4 to 20%, and 5 to 30%.

### Fanning References

When fanning references, such as palettes, if there are more than 2 reference lists are used then the data will be referenced data. The fan will be repeated if there are more channels than references.

-   [1] [Thru] [5] [Int Palette] [1] [Thru] [3] [Enter] - sets channel 1 to IP1, 2 to IP2, 3 to IP3, 4 to IP1, and 5 to IP2.

If the list contains 2 or less references, fan will be set to the levels between the references as absolute data.

-   [1] [Thru] [5] [Int Palette] [1] [Thru] [2] [Enter] - (Intensity palette 1 is all channels at 0%

> and Intensity palette 2 is all channels set to 100%.) sets channel 1 to 0%, 2 to 25%, 3 to
>
> 50%, 4 to 75%, and 5 to 100% as absolute data.

### Fanning Timing and Delays

Fanning timing and delays work exactly like fanning parameters.

-   [1] [Thru] [5] [Time] [6] [Thru] [1] [0] [Enter] - sets the discrete times for channel 1 to 6

> seconds, 2 to 7 seconds, 3 to 8 seconds, 4 to 9 seconds, and 5 to 10 seconds.

-   [Cue] [1] [Thru] [5] [Time] [6] [Thru] [1] [0] [Enter] - sets the times for cue 1 to 6

> seconds, 2 to 7 seconds, 3 to 8 seconds, 4 to 9 seconds, and 5 to 10 seconds.

-   [Cue] [1] [Part] [1] [Thru] [3] [Time] [6] [Thru] [8] [Enter] - sets the times for cue 1\'s parts to part 1 to 6 seconds, part 2 to 7 seconds, and part 3 to 8.

-   [1] [Thru] [5] [Delay] [6] [Thru] [8] [Fan] {Mirror} [Enter] - sets the discrete delays of channel 1 to 8 seconds, 2 to 7 seconds, 3 to 6 seconds, 4 to 7 seconds, and 5 to 8 seconds.

    -   Ion Classic and Element Classic users will need to use {Fan}

### Using Subgroups with Fan

*Subgroups (on page 275)* can be used with the Fan feature. Channels in the same subgroup will act as a single channel when fanned.

> Group 1 is made up of channels 120 -130. Channels 120 - 123 are one subgroup, channels 124 - 126 are not in any subgroup, and channels 127 - 130 are another subgroup.

-   [Group] [1] [Fan] [Enter]

> Selects group 1 and puts it into fan mode. Increasing the intensity overall would result in channels 120 - 123 sharing an intensity, channels 124 - 126 each at different intensities, and channels 127 - 130 sharing an intensity.
>
> Ion Classic and Element Classic users will need to use {Fan}.

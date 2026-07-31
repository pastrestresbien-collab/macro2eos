# Eos Family User Manual v3.2.0 — Chapitre 19 : Park

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 19
## Park
### About Park

The park instruction allows you to set a channel or parameter to a specific value and have it remain at that level on stage (live mode), prohibiting manual control override, cue or submaster playback modification. Park may also be used to place a scaling instruction on the intensity output of a channel.

> **Note:** *A parked channel intensity is not impacted by grandmaster or blackout operations.*

Parked values are withheld from all record targets, but you can manually set levels for parked channels and parameters and store those values into record targets. Keep in mind that the values set and stored in live do not actually output to the system if the parameter is parked.

When channels or parameters are parked, the LED on the [Park] button illuminates and the live display will indicate "Parked Channels" or "Parked Dimmers" in the top right corner. In addition, any parked channel or parameter will be indicated with a white channel number and a "P" will be visible in the channel. When the parked channel or parameter is unparked, it reverts to the level the console is currently providing, or its default value if there is no current instruction.

Park instructions are not subject to partition control. Any programmer/ operator may park and unpark channels/ parameters as needed. Parked parameters set by radio focus remotes (RFR) will automatically unpark when the associated device goes offline.

Channels, parameters and outputs can be parked and unparked from live and from the park display.

> **Note:** *Output from parked channels or parameters is not displayed in Augment3d* *(on page 495).*

### Park Display

You can access the park display by pressing [Park] [Park] or [Tab] [2][0]. Element Classic users will need to use {Park}.

The park display shows all parked channels and parameter values on the top half of the screen and all parked addresses (dimmers) on the bottom half of the screen. Parked channels displayed on the top of the screen can be displayed in the summary and table views seen in Live or Blind by using the [Format] key.

When a channel intensity is parked, the parked value will be indicated in white text. When a channel has a non-intensity parameter that is parked, that parameter will also be indicated with white text. The display also provides detail of which user parked the channel and /or parameter (when multiple users are on the system).

When an address is parked, it will appear in the bottom half of the park display. The address, parked value, affected channels and parameters are indicated.

### Parked Values in Live

Channels and parameters may be parked and unparked from the live display. Following are some examples:

> **Note:** *To park a channel to a specific dimmer intensity level must be accomplished from the Parked Channel display. Access the Parked Channel display by pressing [Tab] [2][0] or {Park}[Park][Park] twice.*
>
> **Note:** *Parked values will be displayed in the park display and in [About] & [Park].*

To park a channel, parameter, or group from live:

-   [2] [At] [5] [0] [Park] [Enter] - parks channel 2 intensity at 50%

-   [2] {Intensity} [Park] [Enter] - parks the intensity of channel 2 at its current value

-   [2] [Park] [Enter] - parks all parameters of channel 2 at their current settings

> **Note:** *If a channel list is constructed in which some channels are parked and some are unparked, [Park] [Enter] will unpark them all. A confirmation will be required.*

-   [2] [At] [Park] [Enter] - if channel 2 is unparked, this command parks intensity at the current value. If the intensity for channel 2 is parked, this command unparks intensity.

-   [2] [Color Palette] [8] [Park] [Enter] - parks the color for channel 2 in color palette 8.

-   [Group] [Cue] [6] [Park] [Enter] - parks all the channels stored in cue 6 at their current levels.

-   [Park] [Enter] - clears all parked channels and scaled park instructions (see *Scaled Parked Values in Live*). A confirm is required. When a channel is unparked, it reverts to the level the console is currently providing, or its default value if there is no current instruction. A confirmation will be required.

> You can use [Recall From] [Park] to set a channel or parameter to the same level as the current park value. See *Recall From Park (on page 368)*.

### Scaled Parked Values in Live

A scaled parked value allows the intensity output (only) to be modified proportionally in live. Scaled park values are ignored when storing a record target. The setting on the display indicates what should be stored, not the actual scaled value. An example of how to set a scaled parked value in live includes:

-   [3] [At] [/] [1] [2] [5] [Park] [Enter] - sets a scaled value of 125% on channel 3 intensity. In other words, whenever channel 3 is active, it will be active 25% higher than its current setting.

-   [3] [At] [/] [8] [5] [Park] [Enter] - sets a scaled value for channel 3. Whenever channel 3 is active, it will playback 15% lower than its current setting.

Remove the scaled parked value:

-   [3] [Park] [Enter] - unparks a scaled intensity for channel 3.

-   [Park] [Enter] - unparks all parked channels.

A channel can have both a scaled parked value and a parked intensity value. Keep in mind that the parked intensity has priority over (and overrides) scaled park values.

### Parked Addresses in Live

DMX addresses can be parked in Live. Below are some examples of parking an address in Live.

> **Note:** *[Address/Patch] is used in the examples below. Ion Classic users will need to use {Address}. Element Classic users will need to use [Dimmer/Address].*

-   [Address/Patch] [5] [At] [5] [0] [Park] [Enter] - parks output 5 at 50% intensity.

-   [Address/Patch] [5] [Park] [Enter] - unparks output 5.

-   [Address/Patch] [Park] [Enter] - unparks all parked outputs.

### Park Values from the Park Display

You can park and unpark channel parameters or addresses from the park display. Open the display by pressing [Park] [Park] or [Tab] [2] [0]. While in this display, it is assumed that you want to park channels or parameters, therefore the use of the [Park] key is not necessary when parking, but is used for unparking. You can also use [At] [Enter] to unpark.

![](media/media/image288.png){width="4.559010279965005in" height="2.1454166666666667in"}

> **Note:** *[Color Palette] is used in the examples below. Element Classic users will need to use {Color Palette}.*

Following are examples for parking channel parameters from the park display:

-   [3] [At] [4] [5] [Enter] - parks channel 3 at 45%.

-   [3] [Color Palette] [4] [Enter] - parks color for channel 3 at color palette 4.

You can use the {Offset} softkey to aid in channel selection. For a list of the {Offset} options, see *Offset (on page 242)*.

Following are examples for clearing parked values while in the park display:

-   [Select Active] [Park] [Enter] - clears all parked channel parameter values.

-   [channel list] [Park] [Enter] - unparks channels in the list.

-   [channel list] [At] [Enter] - unparks channels in the list. Below are examples for parking addresses in the park display:

-   [Address/Patch] [5] [At] [5] [0] [Enter] - parks address 5 at 50% intensity.

-   [Address/Patch] [5] [At] [Enter] - unparks address 5.

> **Note:** *When parking a range of addresses in Park, using [Thru] will only park the intensities. If you want to park all of the addresses and parameters within the selected range, you will need to use [Thru] [Thru].*

# Eos Family User Manual v3.2.0 — Chapitre 22 : Curves

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 22
## Curves
### About Curves

A curve is a relationship between the timing of a fade and the output level of a cue, cue part or dimmer at each point of time during that fade. By using a non-linear curve, you can create of variety of effects, accommodate variations and deficiencies in your lighting equipment, alter the transition ramp and protect equipment from stress.

You may apply curves to dimmers in patch. Curves may also be applied to cues, to cue parts, and to scroller fans. When applied to a cue, the curve impacts only the intensity moves in that cue. When applied to a cue part, the curve impacts all parameter moves stored in that cue part.

When applied in patch, the intensity transition will follow the ramp defined by the curve during its fade. This value is determined by referencing the output value of the curve at that percentage and outputting the curved level rather than the percent level. Up to 100 points of delineation can be established in a curve, each with its own intensity value if desired.

When applied to a cue, the "percent completion" of the cue is determined by applying the curve's output level as the percent completion for all fade calculations. For single-part cues, the calculation applies only to intensity. For multipart cues, however, the curve applies to all parameters in the part.

When applied to a scroller fan, the output of the fan will be controlled by the intensity of the channel.

Curves can also be applied to fixtures with non-intensity parameters (NPs). When a channel with NPs is selected in Patch > Attributes > Curve, individual buttons for each available parameter will be displayed in the CIA. Click one or more buttons to apply a curve to the desired parameter(s).

*(figure omise)*{width="4.175651793525809in" height="1.4340616797900263in"}

Eos provides 11 pre-programmed, commonly used curves. They can be edited or copied to a new curve location. When a pre-established curve is deleted, it will return to its original state.

The curve editor can be accessed by pressing [Tab] [2] [1] or [Displays] {Curve} or from the browser, Browser > Record Target Lists > Curves. When selected, the curves list will open as a separate tab and the CIA will show the graphical output of the first curve in the list.

You can scroll through the list using the [Next] and [Last] keys, or you can specify a curve in the command line.

-   {Curve} [9] [0] [4] [Enter] - selects curve 904 from the list and displays its shape in the CIA.

> *(figure omise)*{width="4.175651793525809in" height="1.4340616797900263in"}

### Creating a Curve

> When you have opened the curves display (see *About Curves (on the previous page)*), you can select a curve or create a new curve by pressing:

-   {Curve} [x] [Enter]

If the curve is already stored, the contents are displayed in the CIA. If this is a new curve, a linear curve is displayed.

### Editing Curves

#### Using the Keypad

Once selected and displayed in the CIA, you can edit a curve from the keypad. Points are established in increments of five. You can add more points from the keypad.

-   [3] [At] [1] [Enter] - adds control input point "3" and sets its curve level at 10%.

-   [7] [7] [At] [Full] [Enter] - adds control input point "77" and sets its curve level at full.

You can specify points and adjust their levels in the command line or you may use the keys below to alter the curve:

-   [Page ▶] - selects the next fade completion point

-   [Page ◀] - selects the previous fade completion point

-   [Level Wheel] - adjusts the output level of the selected point

-   [Page ▲] - raises the selected point's output by 1%

-   [Page ▼] - lowers the selected point's output by 1%

-   [Full] - sets the selected point's output to full

-   [Out] - sets the selected point's output to zero

-   [+%] - raises the selected point by the amount for [+%] established in setup

    -   Ion Classic and Element Classic users will need to use [At] [+] [+]

-   [-%] - lowers the selected point by the amount for [-%] established in setup

    -   Ion Classic and Element Classic users will need to use [At] [-] [-]

#### Using a Touchscreen

Once a curve is displayed in the CIA, you can press {Edit} to edit the curve in the editor display.

In the curve editor you can trace the desired shape of the curve using your finger or a mouse on the touchscreen. As you progress through drawing the curve, intensity values will be added for existing points on the curve. If you add points to the curve (from the keypad) those points will be adjusted as well.

You can also toggle between an "interpolated" or "stepped" curve shape. Eos defaults to "interpolated". To switch to "stepped", press the {Stepped} softkey. Once pressed, this softkey changes to {Interpolated}, which allows you to switch back.

Below are two examples of the same curve. The first is stepped and the second is interpolated.

> *(figure omise)*{width="4.9698031496062995in" height="2.640207786526684in"}

#### Clearing the Curve

At any time, you can clear a curve from the curve editor display by pressing the {Clear Points} softkey. This will return the curve to its original linear shape or to its default shape if it is a pre-established curve.

### Applying a Curve To Channels In Patch

Curves can be applied to any intensity parameter in patch. Once added, the curve number appears in the channel's "Curve" column of the patch display. Pressing {Curve} in Patch > Attributes will display a list of available curves.

-   [Patch] {Attributes} [1] {Curve} [9] [0] [1] [Enter] - applies curve 901 to channel 1 intensity.

-   [Patch] {Attributes} [2] [Thru] [8] {Curve} [2] [Enter] - applies curve 2 to intensity for channels 2 thru 8.

-   [Patch] {Attributes} [1] {Curve} [At] [Enter] - removes the curve from channel 1.

When a curve is applied to a Focus, Color, or Beam parameter, an F, C, or B indicator will appear.

### Curves Applied to Cues

Curves can also be applied to cues or cue parts in Live/ Blind. This affects the percent completion of the cue/ part by applying the curve's output level as the percent completion for all fade calculations. Once added to a cue, the curve number appears in the cue's "Curve" column of the cue list in the playback status display.

-   [Cue] [5] {Attributes} {Curve} [4] [Enter] - applies curve 4 to cue 5.

-   [Cue] [4] [/] [6] [Thru] [9] {Attributes} {Curve} [9] [0] [6] [Enter] - applies curve 906 to cues 4/6 through 4/9.

-   [Cue] [5] {Attributes} {Curve} [At] [Enter] - removes any curve from cue 5.

-   [Cue] [8] [Part] [3] {Attributes} {Curve} [6] [Enter] - applies curve 6 to part 3 of cue 8.

### Applying a Curve To Scroller Fans

Curves can also be applied to a scroller fan. When applied to a scroller fan, the output of the fan will be controlled by the intensity of the channel. To apply a curve to a scroller fan, go to Patch>Attributes>{Fan Curve}. See *Scroller Fan Curves (on page 179)*

### Deleting Curves

While in the curve display, you can delete a curve in the following ways:

-   [Delete] {Curve} [3] [Enter] [Enter] - deletes curve 3 from the list.

-   [Delete] {Curve} [9] [0] [1] [Enter] [Enter] - since curve 901 is a pre-established curve, this command will return curve 901 to its default state, thereby removing any edits to it.

-   [Delete] [Enter] - deletes the currently selected curve.

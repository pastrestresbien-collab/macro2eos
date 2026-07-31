# Eos Family User Manual v3.2.0 — Chapitre 21 : Using About

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 21
## Using About
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
| [[About]](#_bookmark437)         | 444 |                        |                                                           |
+====================================+======================+========================+===========================================================+
| {What\'s New}     |                      | > 445 |                                                           |
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
| [[About] Cue](#_bookmark443)     |                      | 451   |                                                           |
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
+------------------------------------+----------------------+------------------------+-----------------------------------------------------------+
### About [About]

[About] provides detailed information regarding selected elements.

Pressing [About] puts the console in about mode, which allows you to examine about information indefinitely, simply by selecting the element you are interested in. When opened, it appears in the CIA and remains open until closed or until another action forces it to close.

You can also open an About display in a tab by using [Tab] [2][9].

Press the Link icon to break the link to the command line for the current About display. When the link is broken, the About display will be forced to keep showing the type of information currently being displayed, such as channel, address, or presets. When linked, the About display will be linked to the command line, and will updated based on which target is selected.

![](media/media/image294.png){width="3.0611679790026245in" height="0.47895778652668414in"}

Press {.a[A]} to zoom. There are three zoom sizes: small, medium, & large. Medium is the default size.

When in about mode, selecting a channel will reveal information about that channel. Below are examples of the Current Values view (see below) of information that is presented when selecting conventional or automated fixtures. For more information about the About Channel display, see [*[About] Channel (on page 447)*](#about-channel)

![](media/media/image295.png){width="2.9505872703412073in" height="2.2799989063867017in"}

> About can also be used to display additional information in Live and Blind. See *About and* *Display Toggles (on page 107)*.

### [About]

When [About] is pressed when the command line is clear, the CIA presents the following information:

-   System address count

-   Software version

-   Fixture library version

-   Copyright notifications

-   Device name

-   Assigned as (Primary/Backup/Client/Offline)

-   User ID

-   Priority (ACN and Net2)

    -   Not available on Element Classic

-   IP Address(es)

-   Number of defined parameters

-   Number of patched addresses

-   Number of unpatched defined parameters

-   Number of pixel mapping addresses

-   Number of patched channels

-   Number of cues

    -   This includes all cues from all cue lists. Multipart cues are only counted once.

-   Allowed output addresses

> There are also buttons for *{What\'s New} (below)* and [*[About] System (below)*](#about-system).

#### Parameters and Addresses

The defined parameters field references the number of parameters that have been defined in patch. This includes parameters that have been patched to output addresses and those that have not.

The field below defined parameters, patched addresses, only calculates the number of addresses that have been used in patch (which counts toward available outputs).

The unpatched defined parameters field is useful because even unpatched, but defined, parameters must be displayed and calculated in the fade engine. If you are running a large show, it is helpful to delete defined, but unpatched channels. This is where the [Query]

{Unpatched} command is helpful.

#### Allowed Output Addresses

Allowed Output Addresses is a range or ranges of addresses that can be assigned to limit the number of output addresses. Allowed Output Addresses is a setting in the ECU. Go to Settings>Network>Output Protocols>Allowed Output Addresses to make changes if needed.

> **Note:** *If you have created ranges for the Allowed Output Addresses, those will* *display in [About] as well.*

### {What\'s New}

In the [About] display, tap on the {What\'s New} button to open the user documentation on the console. The documentation will open in Tab 100.

> **Note:** *Only one instance of the documentation can be open at a time.*

### [About] System

When {About System} is pressed, the CIA displays a list of all network devices that are connected to Eos. These network devices may include:

-   Consoles

-   RPU and RPU3

-   Net3 RVI and RVI3

-   ETCnomad and Eos Puck

-   Net3 Show Control Gateways

-   Net3 I/O Gateways

-   Legacy Unison CMEi processors

-   Unison Paradigm processors

-   CEM+, CEM3, FDX 2000/ 3000

-   Net3 Gateways

-   ETCNet2 Nodes

Each network device will display the following information:

-   Device Type

-   Name/Component

-   Status

-   Connected

-   IP Address

> **Note:** *Devices may appear more than once in this list if they have multiple roles on the network.*
>
> **Note:** *If any errors or warnings are present at the rack, the CEM+ / CEM3 will display in red.*

Clicking on a CEM+ / CEM3 in the {About System} list will open the About Rack display, which shows the following information about the rack:

-   Rack Name (displays as the title)

-   Type

-   Ambient Temperature

-   Phase A,B,C Voltages

-   Frequency

-   System Number

-   IP Address

-   Software Version

-   Rack Errors

> **Note:** *Clearing CEM+ / CEM3 errors from Eos will be temporary unless the errors have been fixed at the CEM+ / CEM3. Errors displayed on Eos will clear on their own once they have been cleared from the CEM+ / CEM3. Some CEM+ / CEM3 errors can only be cleared at the CEM+ / CEM3.*

Clicking on a FDX rack in the {About System} list will open the About Rack display, which shows the following information about the rack:

-   Rack number

-   Rack Type

-   Phase A,B,C Voltages

-   Frequency

-   System Number

-   IP Address

-   Software Version

Buttons available in the About Rack screen are {Activ. Preset}, {Deactiv. Preset}, and {Clear Errors}.

### [About] Channel

Press [About] to put the CIA into About mode. When a channel is selected, the information below is displayed. You can select the information you wish to view from the buttons located on the right side of the CIA. The buttons are:

{Current Value} displays information that indicates:

-   Channel number

-   Device Type

-   Most recent intensity move (cue number)

-   Next intensity move

-   What the channel is inhibited by (if anything)

-   Keywords

-   Notes

-   A list of all parameters on the channel showing the current value and its source, the DMX value, the absolute value, delay and timing information, marking information, and any parked values.

{Background} displays similar information:

-   Channel number

-   Device Type

-   Keywords

-   Notes

-   A list of all parameters on the channel showing the background value and its source, which shows what the parameters will go to if the current control source is removed. The background data will be represented by the standard color coding scheme.

{Moves} displays information that shows:

-   Parameters

-   Previous move in the cue list that currently has ownership

-   Value of the previous move (preset, palette, or absolute data)

-   Next move

-   Value of the next move (preset, palette, or absolute data)

{Usage} displays information on how the channel is used, such as:

-   Maximum Intensity

-   Cue lists it is used in, if available

-   Total number of cues it appears in (based on intensity)

-   Total number of intensity moves

-   List of submasters that include the channel

-   List of cues that have move instructions for the channel

-   List of cues with dark moves for the channel

-   List of cues that the channel is active in

-   List of groups that include the channel

> **Note:** *While in the {Usage} screen for About Channel, if another channel is selected, you will need to hit the {Refresh Usage} button to see the information for the new channel.*

{Patch} displays the following information:

-   Address range

-   Proportional patch level

-   Curve (if any)

-   GM exempt

-   Preheat information (if any)

-   Swap / invert the pan / tilt status

-   Keywords

-   Notes

-   List of all parameter values with their address, home value, snap parameter, DMX value, and parked value (if any)

![](media/media/image296.png){width="5.032257217847769in" height="1.9499989063867016in"}

{Fixture Notes} displays information found in the fixture library such as:

-   Revision Number

-   Release Date

-   Alternate Names

-   Usage Notes

{Lamp Controls} displays controls for the lamp, available RDM commands, or other parameters of the device (if it is an automated fixture).

### [About] Address

Press [About] to put the CIA into About mode. When an address is selected, the information below is displayed. You can select the information you wish to view from the buttons located on the right side of the CIA. Additional buttons may display based on RDM and Sensor Feedback if enabled. The buttons are:

{Address} displays the following information:

-   Address number (displayed as straight address and port/ offset)

-   Dimmer label (if any)

-   Associated channel number, which is a hyperlink to the [About] channel display.

-   Part number (if any)

-   Notes

-   Output value (sACN, Net2, Art-Net, AVAB UDP, or DMX)

-   Current output value and source of output

-   Parameter controlled by the address

-   Home Value

-   Basic patch information

-   Extended patch information (if available)

-   If it is a scroller, color/ gobo wheel, the assigned scroll or wheel is indicated

-   Information stored in the Text 1 through10 and the Notes fields in Patch > Database

{Next Part} and {Last Part} will advance to the next part or go back to the previous part. This only displays for addresses with parts.

{Go To Patch} is a shortcut to edit the patch for the address selected. This will open up the patch display.

{Fixture Notes} displays the following information:

-   Revision number

-   Release date

-   Open issues list (if available)

-   Usage notes including switch settings and configuration (if available)

-   Alternate fixture names (if any)

{Lamp Controls} displays controls for the lamp or other parameters of the device (if it is an automated fixture).

{Next/ Last Unpatched} will allow you to see what addresses closest to the current address are currently unpatched.

> {Dimmer Feedback} - appears when the current address is patched to a dimmer in an ETC Sensor rack with a CEM+ or CEM3. Sensor feedback must be enabled. See *Interface Protocols (on page 587)* and *Errors and Warnings (on page 192)*.
>
> **Note:** *For Sensor feedback, the CEM+ must be running software version 3.0 or later.*

{Dimmer Feedback} displays the following information:

-   Name (dimmer name)

-   Module type

-   Rack/Position

-   Rack dimmer level (displayed as a percentage)

-   Rack dimmer source

-   Recorded load

-   Actual load

{Dimmer Feedback} displays the following information, which can be modified by clicking on the value and entering in a new value:

-   Firing Mode

-   Control Mode

-   Curve

-   Threshold

-   Scale Minimum

-   Scale Maximum

-   Preheat Enable

-   Preheat Timing

-   Advanced Features (AF) Enable

The following softkey commands are supported from this display:

-   {Ignore Errors}

-   {Clear Errors}

> **Note:** *Clearing CEM+ or CEM3 errors will be temporary unless the errors have been fixed at the CEM+ or CEM3. Errors displayed will clear on their own once they have been cleared from the CEM+ or CEM3. Some CEM+ or CEM3 errors can only be cleared at the Sensor rack.*
>
> {Device Details} - appears when the current address is patched to a RDM device. RDM devices must be enabled through the ECU and discovered through the patch. See *Network RDM (on page 588)* , *Patch > Patch (on page 181)*, and *Errors and Warnings (on page 192)*.

{Device Details} displays the information that it receives from the device and allows some changes to be made to:

> **Note:** *Changes may take a few seconds to make. They will propagate to the RDM device and then back to the console's patch and about displays.*

-   Device Label (displayed at the top by the address number)

-   DMX Address (can be changed in this display by clicking on the property or value)

> **Note:** *Changing the address can not cause any part of the fixture to move to a different universe or communication with the device may be lost. The universe is set into the gateways port configuration.*
>
> **Note:** *Details displayed will vary based on the device.*

-   DMX Label (same as the device label, but the label can be changed here by clicking on the property or value)

-   Type

-   Manufacturer

-   Device ID

-   Footprint

-   Version

-   Lamp State

-   Lamp Hours

-   Head DC Voltage

-   Lamp On/Off

-   Gel Distance Traveled

-   Gel2 Distance Traveled

-   Fan RPM

-   Ambient Temperature

-   Gel Temperature

-   Device Errors (will only display if there are current errors)

-   Clear Errors

Device Errors are displayed in four different colors depending on severity.

> **Note:** *Color severity is determined by the device manufacturer.*

-   Gray - unknown or not an error

-   White - Advisory

-   Yellow - Warning

-   Red - Error

### [About] Cuelist

> **Note:** *Not available on Element Classic.*

The following information will be displayed when a cue list is selected:

-   Cue List Attributes

-   Active Cue

-   The number of cues in the list (Multipart cues are only counted once)

-   First cue in the list

-   Last cue in the list

-   Partition

-   Playback number and physical fader location of the cue list

-   Channels currently controlled in live by the cue list

-   Channels with any intensities above 0 in the cue list

-   Channels with Parameters stored in the cue list but no intensities

### [About] Cue

![](media/media/image297.png){width="4.972042869641295in" height="1.9266666666666667in"}

The following information will be displayed when a cue is selected:

-   The cue number

-   Timing data for the cue (including discrete timing)

-   Flags

-   Attributes

-   Number of moves per IFCB provided by the cue

-   Current status of the cue

-   Intensity moves

-   Live NPs moves

-   Dark NPs moves.

-   Effects running

-   External links

-   All channels in that cue that have discrete or delay times

### [About] Curves

When a curve is selected, the following information will be displayed:

-   Curve number

-   Curve label (if any)

-   Channels that use the curve in patch

-   Channels that use the curve as a fan curve

-   Cues or cue parts that use the curve

### [About] Effects

When an effect is selected, the following information will be displayed:

> **Note:** *To view About Effect in live, the effect must be running.*

-   Effect number

-   Effect label (if any)

-   List of submasters that use the effect

-   List of cues that use the effect

> **Note:** *Any cues or submasters that have overrides, such as rate, for the effect will* *display an *.*

### [About] Groups

When a group is selected, the following information will be displayed:

-   Group number

-   Group label (if any)

-   Channels in the group

The {Ordered} and {Numerical} softkeys can be used to change the display view in About Groups.

### [About] Submaster

The following information will be displayed when a submaster is selected:

-   Submaster number

-   Label (if any)

-   Current value

-   Mode (additive, inhibitive, or effectsub)

-   Fader (proportional or intensity master)

-   HTP or LTP

-   Exclusive

-   Priority

-   Timing

-   Fader Pages

-   Channels in submaster

-   Effects assigned

### [About] Macro

[About] Macro display shows a list of cues that will execute a selected macro. To view this display, you must be in the Macro Editor Display. While in that display, press [About] and then select the macro by using a mouse or touchscreen.

### [About] IFCB Palettes

The following information will be displayed when an intensity, focus, color, or beam palette is selected:

-   Number of cues the palette is used in

-   Number of presets the palette is used in

-   Number of channels

-   First cue the palette is used in

-   Last cue the palette is used in

-   Number of cue lists the palette is used in

> {Usage} displays the following information about palettes:

-   Number of cues that move

-   List of channels that use the palette in a cue

-   List of channels stored in the palette that are not used in a cue

-   List of cues in which the palette have a move instruction

-   List of effects that use the palette

-   List of presets that the palette is stored in

### [About] Presets

When a preset is selected, the following information will be displayed:

-   Number of channels

-   First cue the preset is used in

-   Last cue the preset is used in

-   Number of cue lists the preset is used in

> {Usage} displays the following information about presets:

-   Number of cues that move

-   List of channels that use the preset in a cue

-   List of channels stored in the preset that are not used in a cue

-   List of cues in which the preset have a move instruction

-   List of effects that use the preset

### [About] Color Path

The following information will be displayed when a color path is selected:

-   Color path number

-   Label (if any)

-   Channels that use the color path

-   Cues that have moves that use the color path

-   Number of cue lists the color path is used in See *Color Path (on page 257)*.

### [About] Live

Pressing [Live] while holding [About] will display currently active DMX values, instead of a percentage value.

Double-tapping [Live] while holding [About] will latch this view. Press [About] to disable it again.

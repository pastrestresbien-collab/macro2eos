# Eos Family User Manual v3.2.0 — Chapitre 10 : Palettes

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 10
## Palettes
### About Palettes

> Palettes are building blocks that can be used to create presets (*About Presets (on page 306)*), cues (*About Cues & Cue Lists (on page 320)*), and effects (*About Effects (on page 400)*).

Palettes are referenced data. This means that when included in presets, cues, or effects, changes to the contents of the palette are propagated into all of the places the palette is stored.

> Four types of palettes are available. See *Palette Types (below)*.

Palettes are a critical component when using automated fixtures and can save considerable programming time when editing show data.

> When recording palettes, three softkey options are available. See *Palette Options (on the facing page)*.

Eos supports up to 1,000 palettes of each of the four types, which can be recorded as decimal (up to three places, 0.001) or whole number (up to 9,999.999). Palettes are automatically filtered into IFCB categories. Color data cannot be placed in beam palettes, intensity cannot be included in focus palettes, and so forth. This makes the process of creating palettes easier, faster and less work. If you need to create a reference that will include a mix of IFCB information, presets can be used. See *About Presets (on page 306)*.

> Palettes can be mapped to faders. See *Preset and Palette Fader Properties (on page 313)*.

### Palette Types

There are four types of palettes.

#### Intensity Palettes

Intensity palettes can be created for use with all channels that have intensity parameter data.

#### Focus Palettes

Focus palettes can be created for all channels that have any focus parameter data.

Focus palettes store focus data including Pan and Tilt or XYZ Position. Use {Enable/Disable XYZ Format} to toggle the format of data stored.

> Focus palettes can be assigned to track a specific *Scenic Element Movable (SEM) (on*

*page 537)*. This will override the pan / tilt values in the palette to aim at the XYZ location of the SEM.

#### Color Palettes

Color palettes can be created for all channels that have any color parameter data. Color palettes store any combination of color data, including CMY, RGB, and HS settings, color scrollers and color wheels.

You will find that [Record Only], filter settings and selective store commands will be very useful when storing color palettes. Element Classic users will need to use [Record][Record].

#### Beam Palettes

Beam palettes can be created for all channels that have any beam parameter data. It is rare when storing beam palettes that you will wish to include all of the beam parameters for channels. Therefore, [Record Only], filters and selective store commands will be very useful when storing beam palettes. Element Classic users will need to use [Record][Record].

### Palette Options

When recording palettes, there are three softkey options.

#### {By Type} Palettes

By Type palettes are created with \'default\' channels which contain values that can be assigned to any other channel within the same fixture type. By Type palettes can also contain discrete channel values.

By Type palettes will display a 'T' in the lower corner of the direct selects and in the palette lists. A '+' will display after the 'T' if there are channels stored with discrete data. For more information on by type palettes, see *Using By Type Palettes (on page 301)* .

#### {Absolute} Palettes

Absolute palettes are palettes that when recalled the data is displayed and treated like absolute data applied to a channel. The data is never referenced.

An absolute palette will display with an 'A' in the lower corner of the direct selects and in the palette lists.

#### {Locked} Palettes

Locked palettes are palettes that are protected from being accidentally changed in Live.

A locked palette will display a "L" in the lower corner of the direct selects and in the palette lists.

Locked palettes can be updated by specifically calling the channels and the record target, [channel list] [Update] [Record target] [Enter]. You cannot update a locked color palette directly in Live. However, locked palettes are not protected in Blind.

### Storing Palettes Live

Palettes may be stored in live or blind. There are a variety of methods for determining what data is stored into a palette but [Record], [Record Only] and using filters are the most common ways.

When [Record] is used, Eos will store the relevant parameter category data (intensity, focus, color or beam) for all channels that are not currently at their default value.

[Record Only] is a type of selective store that can be used to store only the relevant parameters that have manual data. Filters and selective storing provide additional methods to control what is stored into a palette.

On Element Classic, double pressing [Record] will post Record Only to the command line.

#### Storing Palettes with [Record]

The most common method to create palettes is to store them from Live. Palettes can be numbered from 0.001 through 9999.999, and each can be given a label. [Record] will store the relevant current parameter data for all channels with non-default data for the appropriate palette type, as modified by the filter settings.

> On Element Classic, the easiest way to access palettes is via [ML Control]. See *Moving Light Controls (on page 128)*.
>
> Assume you want to create a custom color using the color picker and store that data to a custom color palette. First you must select channels.

-   [1] [Thru] [1] [1] [Enter]

> Using the color picker, adjust the hue and saturation levels to the desired look. When the color is selected, store the palette.

-   [Record] [Color Palette] [4] [Label] <FOH Blue> [Enter]

> Notice that when you recorded the color palette, all of the color data for channels 1 through 11 is displayed in live with the reference "CP 4". Because [Record] was used, it stored all of the color parameters for those channels.
>
> Element Classic users will need to use {Color Palette}.
>
> **Note:** *[Record] will store the entire parameter category into a palette. [Record Only] stores just the values you have adjusted manually to the target palette. See Storing [Palettes with [Record Only] (on the facing page)](#storing-palettes-with-record-only).*

When a palette is created, the channels and the parameters involved in the record action are automatically set to the palette reference ("CP 4" in this instance). To view the absolute data for those channels, press and hold the [Data] key.

The following methods can be used to store palettes using [Record]:

-   [Record] {Color Palette 1} - records all color parameter data to color palette 1 and shows it as the first color palette direct select. See *Storing Palettes to Direct Selects (on the facing page)*.

-   [Record] [Focus Palette] [2] [Label] <name> [Enter] - records focus parameter data for all channels not at their default state and adds a label to focus palette 2.

-   [Record] {Color Palette} [Next] [Enter] - records data to the next sequential color palette number.

##### Selective Storing Palettes with [Record]

> **Note:** *[Focus Palette] and [Beam Palette] are used in the examples below. Element Classic users will need to use {Focus Palette} and {Beam Palette}.*

Palettes can also be created using selective storing, which allows you to specify only the channels and or parameters that you want to store.

The following examples illustrate various methods of selectively storing palettes using [Record]:

-   [1] [Thru] [3] [Record] [Intensity Palette] [2] [Label] <name> [Enter] - records the intensity data for selected channels 1 through 3 and adds a label to intensity palette 2.

-   [Group] [2] [Record] {Beam Palette} [Next] [Enter] - records the beam parameter data for Group 2 to the next sequential beam palette number.

-   [-] [9] [Record] [Focus Palette] [5] [Enter] - stores the focus data to focus palette 5, excluding the group or channels specified.

-   [1] [Thru] [9] {Iris} {Zoom} [Record] [Beam Palette] [5] [Enter] - stores all zoom and iris data for channels 1 through 9 to beam palette 5.

-   [-] [5] [Record] [Beam Palette] [Next] [Label] <name> [Enter] - stores to the next sequential beam palette, withholding the group or channels specified and adds a label.

> **Note:** *When using a selective store, you must specify the channel list to be included or excluded, identified by the [+] [-] modifier, as part of the [Record] command.*
>
> *Otherwise all channels with appropriate non-default data will be stored in the new palette.*
>
> **Note:** *Selective storing is useful when you are doing a "one-time" selective store action. If you are recording a series of palettes with only specific parameters, it will save you time to set a record filter (see Using Filters with Palettes (on the next page)).*

#### Storing Palettes with [Record Only]

> **Note:** *[Record Only] is used in the examples below. Element Classic users will need to use [Record] [Record].*

[Record Only] is a selective record process that stores only manual parameter data. When used to record palettes, only the manual parameter data for channels will be stored in the palette. As with record, filters can further restrict stored data if they are enabled when using [Record Only]. See *Storing Palettes Live (on page 293)*.

> **Note:** *If you use [Record Only] to record to an existing palette, the data will be added to that palette. The original palette will not be completely overwritten. Only manual changes will be stored to the palette.*
>
> **Note:** *It is possible to [Update] to add specific changes to the record target. See Update (on page 298).*

The following methods can be used to selectively store manual parameter data to palettes using [Record Only]:

-   [Record Only] [Color Palette] [2] [Enter]- records only the manual color parameter data to color palette 2.

-   [Record Only] [Beam Palette] [5] [Label] <name> [Enter] - records manual beam parameter data for all channels and adds a label to beam palette 5.

-   [-] [9] [Record Only] [Color Palette] [Next] [Label] <name> [Enter] - stores manual data to the next sequential color palette, withholding the group or channels specified and adds a label.

-   [select channels] [Record Only] [Focus Palette] [2] [Enter] - stores focus palette 2, but only includes the manual data for the specified channels and parameters.

-   [1] [Thru] [9] {Iris} {Zoom} [Record Only] [Beam Palette] [5] - stores only manual zoom and iris data for channels 1 through 9 to beam palette 5.

#### Storing Palettes to Direct Selects

You can store palettes efficiently using the direct selects by simply touching the desired direct select for that palette from the touchscreen.

> If you want to store color data to color palette 4, press:

-   [Record]

> and then press the button in the bank of color palette direct selects that is labeled in the lower right corner with a light gray "4".

-   {Color Palette Direct Select Button 4}

> "Color Palette 4" will appear in the direct select, indicating a successful store.
>
> For more information on direct select mapping, see *Direct Selects (on page 113)*.

#### Using Filters with Palettes

Filters can be used to modify what data is stored to a palette by a record action. The parameters that are active or filtered allow those parameters to be stored to record targets.

To filter a parameter:

1.  Press the {Filter} button in the CIA. The {Filter} button will flash.

2.  Press the touchbutton for the parameter you wish to store.

3.  Press the {Filter} button to release. "Filter On" appears next to the parameter category button.

To determine which parameter is filtered in the category:

1.  Press the {Filter} button. All actively filtered parameters are highlighted in gray. You may need to press the arrow softkey for that parameter category to page additional parameters in the category.

Filters are a toggle state. To remove filters, press {Filter} and then press the highlighted parameter buttons in the CIA to deactivate the filters, or use {Clear Filters}.

> For more information on filters, see *About Filters (on page 356)*.

### Recalling Palettes

> **Note:** *[Palette] and [Beam Palette] are used in the examples below. Element Classic users will need to use {Palette} and {Beam Palette}.*

Palettes may be recalled from the control keypad, from direct selects, or from ML Controls (see

> *Moving Light Controls (on page 128)*)

When palettes are recalled, all data is manual and will display in red. Recalled palettes are applied only to selected channels, therefore you must select channels before recalling a palette. If a selected channel or parameter has no stored value in the recalled palette, it remains in its current state. Palettes on direct selects will be highlighted if they are applicable for the current channel selection.

You can select all the channels included in a palette by pressing [Group] [Palette] [x] [Enter]. You can also recall an entire palette by pressing [Recall From] [Palette] [x] [Enter].

> **Note:** *If enabled in Setup, you can double click on a palette direct select button to quickly recall from the selected palette and put its content on stage. See Device > Displays (on page 233) for additional information.*

Recalled palettes will appear as manual data for the specified channels. That data will appear as abbreviations of the palette type (IP3 = Intensity Palette 3, FP8 = Focus Palette 8, and so on), or as the palette label if defined/enabled in the displays settings in Setup (see *{Show Ref Labels} (on page 234)*). To see the numeric values behind any palette (or other referenced value), press and hold the [Data] key. To see the palette number behind the label, press [About] + [Label].

When palettes are recalled, channels with stored data in the palette will follow that data according to manual time settings. A manual time master fader can also affect the timing. See *Manual Time Master (on page 134)*.

Palettes may also be recalled using a time specified using [Sneak] [Time]. For examples on using [Sneak] [Time], see *Sneak (on page 267)*

You may also use groups to recall palettes. For example:

-   [Group] [1] [1] [Beam Palette] [5] [Enter]

-   [Group] [5] {Color Palette 6}

Palettes may also be recalled from the direct selects which automatically terminates the command line. To recall only specific parameters of a palette, select channels and the required parameters (or those not required, using the [-] key) in the command line.

The following are methods that can be used to recall palettes.

-   [selected channels] {direct select} - recalls the associated (IFCB) palette data for the selected channels.

-   [selected channels] [Palette] [n] [Enter] - recalls the associated IFCB palette for selected channels.

-   [Channel List] {edge} [Beam Palette] [n] [Enter] - recalls only the edge data from the specified beam palette for the selected channels.

-   [Group] [n] [Palette] [z] [Enter] - recalls all of the data in the palette and applies it to the selected group.

-   [Intensity Palette] [y] [At] [z] [Enter] - recalls the intensity palette for selected channels and sets all recalled intensity values to a proportioned level of their recorded states.

> **Note:** *The above example breaks the referenced link to the intensity palette. To maintain the link, the palette must be recalled without a modified intensity value. Calling back the intensity palette at full will also break this link.*

When recalling palettes, only channels that are selected at the point of recall will be affected by the palette recall. The data recalled from a palette is referenced. To break the reference you may use {Make Absolute}.

-   [Channel List]{Edge} {Beam Palette} [n] {Make Abs} [Enter] - recalls only the edge data from the specified beam palette for the selected channels and makes that absolute data.

#### Palettes On Faders

> Palettes can be mapped to faders. See *Preset and Palette Fader Properties (on page 313)*.
>
> Presets and palettes can be used to create a temporary list of content that can be played back on a fader. See *Temporary Fader Mapping (on page 317)*.

### Editing Palettes Live

> **Note:** *[Palette] and [Color Palette] are used in the examples below. Element Classic users will need to use {Palette} and {Color Palette}.*

If a palette is already recorded, [Record] replaces all existing data, unless channels have been excluded. [Record Only] is a selective store, therefore it adds data. Recording over a previously existing palette requires a confirmation, if confirmations are enabled in Setup. See *Record Defaults (on page 220)* It is also possible to [Update] to add manual changes to the record target.

#### Rerecord

Rerecording follows the conventions illustrated in the [Record] and [Record Only] sections detailed earlier in this chapter. The only exception is that a confirmation is required to record over an existing palette.

There are two different methods for rerecording:

-   [Record] [Palette] [5] [Enter] [Enter] - overwrites the content completely.

-   [Channel List] [Record] [Palette] [5] [Enter] [Enter]- merges the data.

#### Update

Live changes can be updated to both active and inactive palettes. When updating a parameter in an active palette, that parameter will no longer be absolute data, but will now be in the updated palette on stage.

The following illustrates how to update color palette 2 when no cues are active and you have recalled channels within that palette.

-   <channel list> [Update] [Color Palette] [2] [Enter] - any manual changes for channels originally in the palette are updated in color palette 2.

-   [1] [Update] [Color Palette] [2] [Enter] - adds channel 1's manual data to color palette 2.

-   [-] [3] [Update] {Color Palette 2} - withholds manual changes for channel 3 from the update to Color Palette 2 using the direct selects.

If a channel or parameter does not have data in the palette being updated, it will not be added to that palette unless the user specifically requests it, by specifying the channel.

### Editing Palettes in Blind

> **Note:** *[Palette] is used in the examples below. Element Classic users will need to use*
>
> *{Palette}.*

All palettes can be viewed and edited in Blind. To open a palette in Blind, you can do any of the following:

-   [Blind] [Palette] [Enter] - pressing this will display the first recorded palette of the selected type (Intensity, Focus, Color or Beam) in Blind or return to the last palette of this type viewed in blind.

-   [Blind] {Palette Select 3} or [Blind] [Palette] [3] [Enter] - pressing this will display the specified palette in Blind.

-   [Palette] [Palette] {Edit} - opens the list view of the palette type and then opens Blind palette. You can also use the tab number to open the list view. See *Editing Palettes in List View (on page 300)* for a list of tab numbers.

> **CAUTION:** *When editing palettes in Blind, changes to palettes are automatic, therefore no update or record command is required.*

Palettes can be viewed and edited in blind in the table and spreadsheet views. In Blind, the following softkeys are available when editing palettes:

-   *{By Type} Palettes (on page 293)*

-   *{Absolute} Palettes (on page 293)*

-   *{Locked} Palettes (on page 293)*

-   *Editing By Type Palettes in Blind (on page 302)*

-   *Offset (on page 242)*

-   *Make Null (on page 369)*

-   *Make Absolute (on page 371)*

-   *Replace With (on page 345)*

-   *Query (on page 372)*

#### Entering Blind Palette from Live

> **Note:** *[Palette] is used in the examples below. Element Classic users will need to use*
>
> *{Palette}.*

-   [Blind] [Palette] [Enter] - pressing this will display the first recorded palette of the selected type (Intensity, Focus, Color or Beam) in blind or return to the last palette of this type viewed in blind.

-   [Blind] {Palette Select 3} or [Blind] [Palette] [3] [Enter] - pressing this will display the specified palette in blind.

-   [Palette] [Palette] {Edit} - opens the list view of the palette type and then opens blind palette.

#### Viewing Palettes From Blind

While in any blind mode, when no channels are selected, you can enter a palette from the command line or direct selects. This will take you into blind channel mode for that palette.

-   [Color Palette] [n] [Enter]

    -   Element Classic users will need to use {Color Palette} [n] [Enter] You may also step through the available palettes using [Next] and [Last].

#### Editing in Blind

The following are representative methods used for editing palettes in Blind:

-   [2] {Iris} [At] [Enter] - removes the current parameter value from channel 2.

-   [1] {Iris} [5] [0] [Enter] - selects channel 1 and sets iris value to 50.

-   [2] [Copy To] [5] [Enter] - copies the information from channel 2 to channel 5.

-   [6] [Recall From] [Focus Palette] [1] [Enter] - recalls the values for channel 6 from Focus Palette 1 but not the reference.

    -   Element Classic users will need to use {Focus Palette} You may set Blind levels with encoders, if available.

When editing in Blind, it is possible to remove an instruction from any palette by selecting the channel and parameter and pressing [At] [Enter] or {Make Null} [Enter].

> [Recall From], [Copy To], Move To (accessed by pressing [Copy To] [Copy To]), and {Replace With} may be used to create and edit palette data. See *About Advanced Manual Control (on page 366)*.
>
> **Note:** *While editing palettes in blind, hitting [Recall From] [Recall From] will put [Recall From] [Palette] on the command line.*

Palettes can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Icons (on page 120)*.

#### Editing Palettes in Spreadsheet View

> **Note:** *[Color Palette] and [Beam Palette] are used in the examples below. Element Classic users will need to use {Color Palette} and {Beam Palette}.*

Blind Spreadsheet view shows a range of palettes along the Y axis and channel parameters along the X axis. Viewing palettes in spreadsheet view is useful when you want to compare data between palettes. While in blind, press [Format] to access the spreadsheet. See *Spreadsheet (Blind Only) (on page 101)*.

After selecting a palette, you may use the [Next] or [Last] keys to move through the list or you may select the exact palette from the keypad. You may also select a range of palettes to edit at once. You can make changes to the palette(s) by selecting channels and altering parameter values. In addition to normal editing functions, you may also use the following commands in this view: [Copy To], {Make Absolute}, {Make Null}, Move To(accessed by pressing [Copy To] [Copy To]), and {Replace With}.

The following are representative methods used for editing palettes in blind spreadsheet:

-   [Color Palette] [1] [Thru] [9] [Enter] - selects color palettes 1 through 9.

-   [1] {Scroller} {Make Null} [Enter] - sets channel 1 scroller value null in the selected color palette(s).

-   [1] {Scroller} [4] [Enter] - sets channel 1 scroller value to frame 4 in the selected color palette(s).

Here are some examples of the additional palette editing features available in spreadsheet view:

-   [palette type] [1] [Thru] [5] {Move To} <palette type> [9] [Enter] - this will move palettes 1 through 5 to palettes 9 through 14 respectively. You do not have to supply the end value for the console to perform the move.

-   [Beam Palette] [1] [Thru] [5] [Enter] {Iris} [5] [0] {Replace With} [2] [5] [Enter] - for palettes 1 through 5, this command will replace any iris parameter values of 50 with values of 25.

#### Editing Palettes in List View

When you press the specific Intensity, Focus, Color or Beam palette button twice, a list view for the associated palette type is opened in a new tab (or brings the list view into focus if already open). You can also open the list views from the home screen. See *Workspace Layout Menu (on page 90)*.

You can also open the list views by using their tab numbers. Press and hold [Tab] and type the number to open.

-   Intensity Palette - [Tab] [2] [2]

-   Focus Palette - [Tab] [2] [3]

-   Color Palette - [Tab] [2] [4]

-   Beam Palette - [Tab] [2] [5]

Indicators for absolute (A), locked (L), and by type (T+) display to the right of the palette number.

> **Note:** *In the by type channels column, any channel number with an asterisk indicates that the channel does not have any by type data stored to it.*

From the list view, you can select a palette for editing, which changes focus to blind channel view, with the specified palette ready for editing. In addition, you can add palettes to your list and edit the labels for each palette in the list.

> In the list view, you can select palettes and relabel or move them.

-   [1] [5] [Label] <name> [Enter]

While in the specific palette category list view, the {Edit} softkey is available for use. The {Edit} softkey opens a blind channel view of the selected palette and changes focus from the palette list. You can change the blind display to spreadsheet or table view by pressing the [Format] key.

To copy a specific palette to a new palette:

You can copy palettes within the list to another location in the list using [Copy To].

-   <Color Palette> [2] [Copy To] [9] [Enter] [Enter] - copies the contents of color palette 2 to color palette 9. Color palette 2 will remain in the list. The second [Enter] is not required if you have disabled confirmations in setup.

You can also use [Copy To] from presets to palettes. To move a specific palette to a different location:

-   [1] {Move To} [3] [Enter] - moves the contents and label of the specific palette 1 to palette 3. If palette 3 is already used, you will be asked to confirm that you want to overwrite the existing recorded palette. You can hit [Copy To] [Copy To] to access

> {Move To}.

You can also move data from a preset to a palette and vice versa. It is important to remember that when using the {Move To} command that data is removed from its current location and moved to its new location.

To edit any palette data from the List View:

-   [1] [5] {Edit} [Enter] - selects palette number 15 and brings the blind display into focus, with palette 15 selected for editing. You can use the [Next] and [Last] buttons to access the other palettes, or select a new palette for editing from the keypad.

### Using By Type Palettes

#### Storing a By Type Palette

If {By Type} is used when recording, the lowest number channel of each fixture type will be the default channel. Generally, when storing by type palettes, you will want only one channel of each fixture type in use. Any additional channels in that fixture type will be recorded with discrete data.

-   [1] [Thru] [5] [Record] [Int Palette] [1] {By Type} [Enter] - Channels 1 through 5 are saved to Intensity Palette 1. Channels 1 through 5 are of the same fixture type. Channel 1 will be the default channel and channels 2 through 5 will be saved with discrete data.

-   [1] [Thru] [5] [Record] {Intensity Palette 1} [Enter] - If a by type palette is recorded without using the {By Type} softkey and the default channel is included in the record, the default channel's level will change and all other changes will be discrete.

-   [1] [Thru] [5] [Record] {Intensity Palette 1} {Discrete} [Enter] - If a default channel is included in a record where {Discrete} is used and another channel is tracking it, the default channel will be changed to having discrete data and the lowest numbered tracking channel will become the new default channel. All other channels in the record will also have discrete data.

#### Editing By Type Palettes in Blind

> **Note:** *[Color Palette] and [Beam Palette] are used in the examples below. Element Classic users will need to use {Color Palette} and {Beam Palette}.*

In Blind, the default channel's levels will display in blue, discrete data for the other channels will display in white, and any channels that are using the default channel value will display in magenta.

-   [3] {By Type} [Enter] - makes channel 3 the new default channel for that device type. If another channel for that type was the default channel, its data will now be discrete.

-   [1] [0] [Thru] [2] [0] {Discrete} [Enter] - changes the levels for channels 10 through 20 to discrete. If any of those channels are default, the lowest numbered tracking channel will become the new default channel.

-   [5] [Thru] [8] [At] [Enter] - removes the discrete data for channels 5 through 8. They will now use the default channel's values.

-   [Color Palette] [2] {Discrete} [Enter] - changes all tracking and default channels to discrete.

-   [Intensity Palette] [5] {By Type} [Enter] - makes the first channel of each device type a default channel.

-   [Beam Palette] [3] {Cleanup} [Enter] - converts palettes created in earlier versions of Eos Family software to by type palettes. If by type channels exist in this palette, {Cleanup} will convert any discrete levels that match their by type channel\'s level to tracks.

{Make Null} can be used with by type palette when you wish to withhold a channel from responding to a by type palette recall. The data will still display but will be in gray with a "N". See *Make Null (on page 369)*.

#### Updating By Type Palettes

Pressing {By Type} after an [Update] command, with a channel tracking but no default channel included in the update, will cause the lowest numbered tracking channel\'s level to be updated into the default channel. The tracking channel will remain tracking. This means that when updating a default value in a by type palette, you don't need to know the default channel number.

When a default channel is included in an [Update] command without using {By Type} and another channel is tracking it, the default channel's data will be changed to discrete. The lowest numbered tracking channel will then become the new default channel. Any other updated channels will be made discrete.

### Other Palette Edits

> **Note:** *[Color Palette] is used in the examples below. Element Classic users will need to use {Color Palette}.*

#### Removing Channels from a Palette

You can remove specific channels from a palette. This can be done from Blind.

> Open the palette in Blind:

-   [Blind] [Color Palette] [Enter] Select the palette you wish to edit:

-   [Color Palette] [5] [Enter]

> Remove channels by pressing:

-   [2] [+] [4] [+] [6] [Thru] [9] [At] [Enter]

> You may also remove a channel or parameter from a range of presets by pressing:

-   [Beam Palette] [1] [Thru] [5] [Enter] [6] [At] [Enter] You can remove channels from Live by pressing:

-   [channel list] [Delete] [Color Palette] [2] [Enter]

#### Deleting Palettes

To delete color palette 1, press [Delete] [Color Palette] [1] [Enter] [Enter]. When palettes are deleted, any references in cues will be converted to absolute data.

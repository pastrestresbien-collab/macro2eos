# Eos Family User Manual v3.2.0 — Chapitre 11 : Presets

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 11
## Presets
### About Presets

Presets are very similar to palettes in that they are collections of data for specific channels to facilitate cue creation. Presets, however, can collect all data for a given channel (intensity, focus, color, beam) rather than just one parameter category.

Eos supports up to 1,000 presets, which can be recorded as decimal (up to three places, 0.001) or whole number (up to 9,999.999). They can contain absolute data and/ or a mix of IFCB palettes. Presets can not refer to other presets.

> On most Eos Family consoles, presets can be mapped to faders. See *Preset and Palette Fader Properties (on page 313)*.
>
> Effects can be stored in presets. See *Recording an Effect to a Preset (on page 420)*.

### Preset Options

When recording presets, there are three softkey options.

#### {By Type} Presets

By Type presets are created with \'default\' channels which contain values that can be assigned to any other channel within the same fixture type. By Type presets can also contain discrete channel values.

By Type presets will display a 'T' in the lower corner of the direct selects and in the presets list. A '+' will display after the 'T' if there are channels stored with discrete data.

#### {Absolute} Presets

Absolute presets are presets that when recalled the data is displayed and treated like absolute data applied to a channel. The data is never referenced. An absolute preset will display with an 'A' in the lower corner of the direct selects and in the presets list.

#### {Locked} Presets

Locked presets are presets that are protected from being accidentally changed in Live.

A locked preset will display a "L" in the lower corner of the direct selects and in the presets list.

Locked presets can be updated by specifically calling the channels and the record target, [channel list] [Update] [record target] [Enter]. Using [Update] [Preset] [1] [Enter] would not work in Live for a locked preset. However locked presets are not protected in Blind.

### Storing Presets Live

> Presets can be recorded live using the keypad and/ or the direct selects. Both [Record] and [Record Only] can be used to record presets, with or without filters. See *Storing Data with Record Filters (on page 357)*.

[Record] will store all channels that are not at their home values, and it will record all information about those channels, including parameters that are still at default. Therefore presets can contain all of the same information as a cue, but they have no timing information or cue attributes (such as follow, delay, or cue overrides). When recorded or re-recorded, presets are automatically recalled on stage. Presets may be individually labeled.

#### Storing Presets Using [Record]

The [Record] key will store all parameter data for channels with one or more parameters not at their home values, as modified by the filter settings in the CIA. If filters are used, only the parameters enabled by the filters are stored.

When you record data to a preset live, the channels involved in that preset will then actually be in that preset.

> **Note:** *[Preset] is used in the examples below. Element Classic users will need to press [Shift] & [Intensity Palette] or use the {Preset} button in ML Controls.*

The following methods can be used to store presets using [Record]:

-   [Record] [Preset] [5] [Label] [name] [Enter] - records all parameter data for all channels not at default and adds a label to preset 5.

-   [Record] [Preset] [Next] [Enter] - records data to the next sequential preset number.

-   [-] [2] [Record] [Preset] [n] [Enter] - stores the preset, withholding the group or channels specified.

-   [channel list] [Record] [Preset] [6] [Enter] - stores the preset, but only the data for the channel list supplied.

-   [Record] {Preset 1}- records the preset and shows it as the first preset direct select.

-   [channel list] {AllNPs} [Record] [Preset] [8] [Enter] - records all non-intensity parameters for the selected channels to the preset.

> **Note:** *When using selective record, the user must specify the channel list to be included (or excluded as the case may be) as part of the [Record] command.*
>
> *Otherwise, all parameters of channels with non-home values will be stored in the preset.*
>
> **Note:** *You may also use the filters and {Make Null} as additional tools to decide what data will be stored. For more information on these features see Make Null (on page 369) and About Filters (on page 356) .*

When you re-record an existing Preset, a confirmation will be required, unless *Record Defaults*

have been disabled in Setup.

#### Storing Presets Using [Record Only]

[Record Only] is a selective record process that stores only manual parameter data. Therefore, when used to record presets, only manual data for channels will be stored in the preset. As with [Record], filters and {Make Null} can be used to further modify what information is stored. See *Storing Data with Record Filters (on page 357)*.

On Element Classic, double pressing [Record] will post Record Only to the command line. The following methods can be used to store presets using [Record Only]:

-   [Record Only] [Preset] [5] [Label] [name] [Enter] - records manual parameter data for all channels and adds a label to preset 5.

-   [Record Only] [Preset] [Next] [Enter] - records manual data to the next sequential preset number.

-   [-] [3] [Record Only] [Preset] [n] [Enter] - stores the preset, withholding the group or channels specified.

-   [Channel list] [Record Only] [Preset] [6] [Enter] - stores the preset, but only the manual data for the channel list supplied.

-   [Channel list] {Color} [Record Only] [Preset] [7] [Enter] - stores only manual color data for the specified channels to the preset.

### Recalling Presets

Channels must be selected when recalling a preset. If a selected channel or parameter has no value in the preset, it will stay in its current position. If you want to recall all channels in a preset, you can press [Recall From] [Preset] [x]. Presets on direct selects will be highlighted if they are applicable for the current channel selection.

> **Note:** *If enabled in Setup, you can double click on a preset direct select button to quickly recall from the selected preset and put its content on stage. See Device > Displays (on page 233) for additional information.*

If you only want to recall certain parameters of the preset, select channels and enter the required parameters (or those not required, using the [-] key) in the command line (see command examples below).

When a preset is recalled, parameter changes will follow the manual timing defaults, if enabled. A manual time master fader can also affect the timing. See *Manual Time Master (on page 134)*.

Presets may also be recalled using a time specified using [Sneak] [Time]. For examples on using [Sneak] [Time], see *Sneak (on page 267)*

You may recall presets using any of the following methods:

-   {Preset direct select} - recalls the associated preset data for selected channels.

-   [Preset] [2] [Enter] - recalls preset 2 for selected channels.

-   [Channel List] [Preset] [2] [Enter] - recalls the preset data for the channels in the selection list.

-   [Channel List] [Preset] [Enter] - recalls the last selected preset\'s data for the channels in the selection list.

-   [Channel List] {Color} [Preset] [5] [Enter] - recalls only the color data from the specified preset for the specified channels.

-   {Color} {Preset direct select} - recalls just the color data from the specified preset for selected channels.

-   [Recall From] [Preset] [3] [At] [5] <0> [Enter] - recalls all channels in preset 3, and sets all intensity values at 50%. The original intensity data is still linked to the preset. If the intensity change is desired, you must update the preset to maintain the change and the link. Storing the data to another record target would break the link and make the data absolute.

-   [Channel List] [Preset] [7] [Enter] [At] [5] <0> [Enter] - recalls preset 7 for selected channels. Intensity values will be recalled at 50% of their recorded state. The intensity link is maintained. If the intensity change is desired the user either needs to update the preset to maintain the change and the link. Storing the data to another record target would break the link and make the data absolute.

-   [Recall From] [Preset] [9] [Enter] - selects all channels with data stored in preset 9, and sets those channels to the values in preset 9.

-   [1] [Recall From] [Preset] [1] [At] [5] <0> [Enter] - recalls the intensity of channel 1 from preset 1 at 50% of the stored value. If channel 1 was set to 50 in preset 1, it's recalled value would be 25.

### Editing Presets Live

There are two ways to edit a preset in Live. You may rerecord the preset or you may use [Update].

#### Rerecording Presets

Rerecording follows the conventions of [Record] and [Record Only]. The only exception is that a confirmation is required to actually rerecord the preset.

Two different mode for rerecording:

-   [Record] [Preset] [5] [Enter] [Enter] - overwrites the content completely.

-   [Channel List] [Record] [Preset] [5] [Enter] [Enter] - merges the data.

#### Updating Presets

[Update] is used to record parameter modifications back to a preset. When updating, you must specify the preset to be updated. You may do this using the keypad or the direct selects.

For the purposes of the following descriptions, assume that there are no active cues on stage. Updating referenced values while cues are active is covered in [*Modifying Cues Live (page 1)*](../../../../../13_Cues_and_the_Cue_List/Modifying_Cues_Live.htm).

> To update a preset, first recall the preset for any channels you wish to edit.

-   [1] [Thru] [5] [Preset] [1] [Enter]

> -or-

-   [Recall From] [Preset] [1] [Enter]

> Make required changes to the desired parameters using the keypad, encoders, or ML Controls. Once you have achieve the desired look, update the preset.

-   [Update] [Preset] [1] [Enter]

> -or-

-   [Update] {Preset 1}

When updating a preset, only channels that are already in the preset will be updated. You need to select channels or parameters to force new data into a preset when using [Update].

### Preset List

The preset list displays all recorded presets. The Preset List only allows you to change attributes; no editing can be done directly in list view.

Press [Preset] twice to open the Preset list view. You can also open the list view from the home screen or by using [Tab] + [2][6]. Element Classic users will need to press [Shift] & [Intensity Palette] or use the {Preset} button in ML Controls. See *Workspace Layout Menu (on page 90)*.

Pressing the {Edit} softkey takes you to the blind view of the selected preset, in the last format you used in blind. This will allow you to edit the preset. You can change the blind display to spreadsheet or table view by pressing the [Format] key.

You can navigate the preset list using [Next] and [Last].

Indicators for absolute (A), locked (L), and by type (T+) display to the right of the preset number.

> **Note:** *In the by type channels column, any channel number with an asterisk indicates that the channel does not have any by type data stored to it.*

#### Copy To

You can copy presets within the list to another location in the list using [Copy To].

-   <Preset> [2] [Copy To] [9] [Enter] [Enter] - copies the contents of preset 2 to preset 9. Preset 2 will remain in the list. The second [Enter] is not required if you have disabled confirmations in setup.

You can also use [Copy To] from palettes to presets.

#### Move To

You can move presets within the preset list using Move To, which is accessed by pressing the [Copy To] button twice.

-   <Preset> [3] [Copy To] [Copy To] [8] [Enter] [Enter] - moves preset 3 to preset 8. Preset 3 will be removed from the list. The second [Enter] is not required if you have disabled confirmations in setup.

-   <Preset> [1] [Thru] [5] [Copy To] [Copy To] [6] [Enter] [Enter] - moves presets 1 through 5 to presets 6 through 10.

You can also move data from a palette to a preset and vice versa. It is important to remember that when using the Move To command that data is removed from its current location and moved to its new location.

### Editing Presets in Blind

All presets can be viewed and edited in blind. To open a preset in blind, you can do any of the following:

-   Press [Blind] {Preset x} - opens to the specific preset

-   Press [Tab] & [2][6] - opens the preset list

-   Press [Preset] [Preset] and then {Edit} when a preset is selected in the list

    -   Element Classic users will need to use [Shift] & [Intensity Palette] instead of [Preset]

> **CAUTION:** *When editing presets in Blind, changes to presets are automatically stored. Therefore no update or record command is required.*

You can change the blind display to spreadsheet or table view by pressing the [Format] key. In blind, the following softkeys are available when editing presets:

-   *Preset Options (on page 306)*

-   Cleanup (*Using By Type Presets (on the facing page)*)

-   Discrete (*Using By Type Presets (on the facing page)*)

-   *Offset (on page 242)*

-   Make Null (*Editing in Table View (below)*)

-   Make Absolute (*Editing in Table View (below)*)

-   Replace With (*Editing in Table View (below)*)

-   Query (*Query (on page 372)*)

Presets can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Icons (on page 120)*.

#### Editing in Table View

Table view shows the data for one preset at a time in a table. Channels are displayed on the Y axis and parameters are shown along the X axis. Viewing presets in the table is useful if you want to see data for numerous channels in one specific preset.

To change which preset you are viewing you may use the [Next] or [Last] keys or you may select the exact preset from the keypad or direct selects. You can make changes to the preset by selecting channels and altering parameter values. In addition to normal editing functions, you may also use the following commands in this view: [Copy To], [Recall From], {Make Absolute}, {Make Null}, {Move To}, and {Replace With}.

Here are some examples of the additional preset editing features you have while editing in table view:

-   [select channels or parameters] {Make Abs} - changes the data for any palette references within the preset into absolute data that no longer references another record target.

-   [select channels or parameters] {Make Null} - removes the data for the specified channel or parameter from the preset.

-   [select channels or parameters] [At] [Enter] - removes the data for the specified channel or parameter from the preset.

-   [Preset] [5] {Move To} [Preset] [9] [Enter] - this will move the contents of preset 5 to preset 9. Preset 9 will be created and preset 5 will be deleted.

-   [Preset] [1] [Copy To] <Preset> [5] [Enter] - this will copy the contents of preset 1 to preset 5. You may also copy ranges of presets to new locations.

-   [1][Recall From][Preset][1][Enter] - will recall the contents for channel 1 in preset 1.

> **Note:** *While editing presets in blind, hitting [Recall From] [Recall From] will put [Recall From] [Preset] on the command line.*

#### Editing in Spreadsheet View

Spreadsheet view shows a range of presets along the Y axis and channels/channel parameters along the X axis. Viewing presets in spreadsheet view is useful when you want to compare data between presets.

You may select a preset from the spreadsheet using the [Next] or [Last] keys to move through the list or you may select the exact preset from the keypad. You may also select a range of presets to edit at once. You can make changes to the preset(s) by selecting channels and altering parameter values.

In addition to the examples given in *Editing in Table View*, here are some examples of the additional preset editing features you have while editing in spreadsheet view:

-   [Preset] [1] [Thru] [5] {Move To} <Preset> [9] [Enter] - this will move presets 1 through 5 to presets 9 through 14 respectively. You do not have to supply the end value for Eos to perform the move. If presets 9 through 14 already exist you will be asked to confirm this move.

-   [Preset] [1] [Thru] [5] [Enter] {Iris} [5] [0] {Replace With} [2] [5] [Enter] - for presets 1 through 5, this command will replace any iris parameter values of 50 with values of 25. Range editing using {Replace With} is easiest done in spreadsheet view, but can be done in any Blind mode.

### Using By Type Presets

#### Storing a By Type Preset

If {By Type} is used when recording, the lowest number channel of each fixture type will be the default channel. Generally, when storing by type presets, you will want only one channel of each fixture type in use. Any additional channels in that fixture type will be recorded with discrete data.

-   [1] [Thru] [6] [Record] [Preset] [1] {By Type} [Enter] - Channels 1 through 6 are saved to Preset 1. Channels 1 through 6 are of the same fixture type. Channel 1 will be the default channel, and channels 2 through 6 will be saved with discrete data.

-   [1] [Thru] [6] [Record] [Preset] [1] [Enter] - If a by type preset is rerecorded without using the {By Type} softkey and the default channel is included in the record, the default channel\'s level will change and all other changes will be discrete.

-   [1] [Thru] [5] [Record] {Preset 1} {Discrete} [Enter] - If a default channel is included in a record where {Discrete} is used and another channel is tracking it, the default channel will be changed to having discrete data and the lowest numbered tracking channel will become the new default channel. All other channels in the record will also have discrete data.

#### Editing By Type Presets in Blind

In Blind, the default channel's levels will display in blue, discrete data for the other channels will display in white, and any channels that are using the default channel value will display in magenta.

![](media/media/image254.png){width="5.051574803149606in" height="1.3365616797900262in"}

Softkeys available for editing presets in blind are {By Type}, {Discrete}, and {Cleanup}.

-   [3] {By Type} [Enter] - makes channel 3 the new default channel for that device type. If another channel for that type was the default channel, its data will now be discrete.

-   [1] [0] [Thru] [2] [0] {Discrete} [Enter] - changes the levels for channels 10 through 20 to discrete. If any of those channels are default, the lowest numbered tracking channel will become the new default channel.

-   [5] [Thru] [8] [At] [Enter] - removes the discrete data for channels 5 through 8. They will now use the default channel's values.

-   [Preset] [2] {Discrete} [Enter] - changes all tracking and default channels to discrete.

-   [Preset] [5] {By Type} [Enter] - makes the first channel of each device type a default channel.

-   [Preset] [3] {Cleanup} [Enter] - converts presets created in earlier versions of Eos Family software to by type presets. This command will use the first channel of each type as the default, and allow other channels of the same type to use that value upon recall.

{Make Null} can be used with by type preset when you wish to withhold a channel from responding to a by type preset recall. The data will still display but will be in gray with a "N".

#### Updating By Type Presets

Pressing {By Type} after an [Update] command, with a channel tracking but no default channel included in the update, will cause the lowest numbered tracking channel\'s level to be updated into the default channel. The tracking channel will remain tracking. This means that when updating a default value in a by type preset, you don't need to know the default channel number.

When a default channel is included in an [Update] command without using {By Type} and another channel is tracking it, the default channel's data will be changed to discrete. The lowest numbered tracking channel will then become the new default channel. Any other updated channels will be made discrete.

### Removing Channels from a Preset

You can remove specific channels from a preset. This can be done from blind.

> Open the preset in blind:

-   [Blind] [Preset] [Enter] Select the preset you wish to edit:

-   [Preset] [5] [Enter]

> Remove channels by pressing:

-   [2] [+] [4] [+] [6] [Thru] [9] [At] [Enter]

> Or you can remove a specific channel parameter from the preset by pressing:

-   [5] [+] [7] {Color} [At] [Enter]

> You may also remove a channel/ parameter from a range of presets by pressing:

-   [Preset] [1] [Thru] [5] [Enter] [1] {Color} [At] [Enter] You can remove channels from live by pressing:

-   [channel list] [Delete] [Preset] [2] [Enter]

### Deleting Presets

You may delete presets in the following ways:

-   [Delete] [Preset] [1] [Enter]

-   [Delete] [Preset] [1] [Thru] [5] [Enter]

Presets can be deleted from any screen, at any time. A confirmation is required to delete, unless confirmations have been disabled in Setup. See *Record Defaults (on page 220)*

### Preset and Palette Fader Properties

Presets and palettes can be mapped to faders by using the fader configuration display. For information on how to use the fader configuration display to map faders, see *Fader Configuration (on page 129)*

The fader configuration display is found on Tab 36. The *Fader List (on page 132)*, which shows all of the faders and their assignments, can be found in Tab 35.

Click or tap the second row of the fader page to access this properties display.

The following options are available when a fader is configured as a preset or palette fader:

> ![](media/media/image255.png){width="3.4568569553805775in" height="2.18in"}

#### Mode

You may define your fader as additive (contributes to the live output), inhibitive (limits live output) or an effect fader (presets only).

#### Master

A fader can be assigned as a Master. When it is a master, its behavior as a Proportional Master or Intensity Master (I-Master) is drawn from this setting.

#### HTP

Intensity playback behavior can be set to HTP (highest takes precedence) or LTP (latest takes precedence).

#### Restore

Faders can be placed into restore modes of minimum or background, which is the default. When a fader is in the restore to background mode, the restore column of the fader list display will be blank. When in minimum mode, \'Min\' will display in the restore column.

The restore mode of background means that when the fader is returned to zero, control will be restored to the background value, such as another fader or a cue.

The restore mode of minimum means that when the fader is faded down, control does not go to the previous background state but to the parameters' minimum value.

#### Priority

The Independent setting for faders has been changed to priority. There are 10 levels of priority for faders. 1 is the lowest and 10 is the highest. faders can still be shielded, which means that their content is automatically made exclusive and can\'t be controlled by anything other than that fader and park, including by manual control. Shielded has a higher priority than 10.

#### Background

Faders can have their background states disabled. Background states are enabled by default. When enabled, the content of the fader will act as a background or previous state for other cues and faders.

#### Background Priority

Background can have a priority assigned to it.

In previous software releases, when content was released, it always returned to the last fader that owned it. Background priority releases to the highest priority content that previously had ownership, provided that content has not be turned off or released.

There are 10 levels of background priority for faders. 1 is the lowest and 10 is the highest. When LTP content is released to background, it will go to the background state with the highest available priority.

#### Up Time

This is the time for the fader to fade from its home position to its target position (0 to Full if additive, Full to 0 if inhibitive). The default time is 0.

#### Dwell Time

This is the time the fader look will hold before starting the downfade. This can be set to a specified time, or to "Hold" or "Manual". "Hold" time maintains the fader values until the bump is pressed a second time. "Manual" time applies the fader values only as long as the bump is held. The default is "Manual".

#### Down Time

This is the time for the content on a fader to fade from its target position to its home position. The default time is 0.

#### Stomp Mode

Stomp happens when all the content owned by a fader is now being controlled by other targets. The fader is being removed from the background , and once that happens, it would not be eligible to fade back. You can assign behavior that will happen when a fader is stomped.

-   Off When Stomped - puts the content into an off state, the same behavior encountered when pressing [Off] + [Load].

-   Unload When Stomped - unloads the fader.

-   Nothing When Stomped - no action happens to the fader.

-   Release When Stomped -This function behaves the same as Off When Stomped.

#### Unmark at 0 % 

When this option is on, marked content controlled by the fader will automatically be released when the fader reaches 0%. When the bump button is next pressed, the fader will fire. If this option is off, you would need to first press the bump button to reset the fader before pressing the bump again to fire it.

> **Note:** *This option is for faders that are set to Intensity Master.*

#### Exclusions

Those exclusions include:

-   Exclude From Record - output is not recorded into any other record target.

-   Exclude From Grandmaster - content cannot be mastered by a grandmaster.

-   Exclude From Inhibitive Sub - content cannot be mastered by an inhibitive submaster

-   Exclude From Solo - content will ignore solo. See *Fader and Button Configuration (on page 353)*.

#### Channel and Parameter Filters

Channel and Parameter Filters can be used to allow only specified data to be played back. These are playback filters, and do not impact how data is recorded.

Tap or click on {Chan Filter} to assign channels or groups. Tap or click on {Param Filter} to open a list of available parameters that you can filter.

When a filter has been applied, an indicator will display in the fader ribbon. C will display for channel filter, and F is for parameter filter.

Press the red [X] to clear the channel or parameter filters listed.

#### Fader and Button Configuration

Click or tap on the virtual buttons or fader to see a list of available configuration options.

##### Button Options

The following options are available for fader buttons:

-   Bump - plays back the content at 100% of the recorded level. It will continue to do so until released, unless the fader has a time assigned or the {Hold} property set.

-   Group/ Assert - selects all the channels associated with the fader, if the fader is inactive. If active, the contents of the fader will be asserted.

-   Assert - regains control of all of the channels associated with the fader.

-   Group Select - selects the channels stored in the fader. This is the same as [Group] [Sub] [n].

-   Freeze - halts all effect activity on the fader.

-   Off - removes the content and if the fader is set to Master, the fader will remain where it currently is.

-   Release - removes the content and if the fader is set to Master, the fader will reset to 0.

-   Start Stop Effect -starts the effect while ignoring dwell times. Will stop effects if any are running.

-   Button Disabled - no action is assigned to the button.

-   Solo - suppresses any intensity values not provided by the associated content while the solo button is held down. When the button is released, intensity values are restored. Priority and HTP are ignored. Shielded, park and pixel mapping outputs are not affected by the solo button.

-   Back - fades to the previous cue when fader is assigned to a cue list.

-   Macro - allows you to assign a macro as a button action.

##### Fader Options

The following options are available for a fader:

-   Master - fader will be a proportional master, a manual master, or an intensity master.

-   Effect Rate - fader centers to home. It controls the rate of any running effects (same behavior as using rate via the Effect Status Display). The adjusted setting from this control cannot be stored.

-   Effect Size - similar to Effect Rate but for effect size.

-   Rate Master - homes to center. It adjusts the cue rate, just like rate and load.

-   Fader Disabled - no action is assigned to the fade.

-   Master Only - fader is used to set a level for content to fade to. The slider can be used to live adjust levels when the fader has been activated via the bump button. See *Master Only (on page 134)*.

-   Effect Master - masters the entry/exit mode of the effects (size, rate or both).

-   Levels Only - masters the levels without mastering the effect.

#### Temporary Fader Mapping

Presets and palettes can be used to create a temporary list of content that can be played back on a fader.

> **Note:** *This list is not recorded. If the fader is unloaded, the list cannot be recalled.*

To create a list, press the [Load] button of an unmapped fader. You can then select presets or palettes to add to your list either by the command line or from the direct selects.

-   [Load] {DS 1} {DS 2} {DS 2} [Enter]

-   {Fader} [1][0] [Preset] [1] [Preset] [2] [Preset [3] [Enter]

Once mapped, the fader will default to Master Only mode. See *Master Only (on page 134)*. The list will use the timing assigned to the fader.

> A fader with temporary mapping will have the cue list options for Back From First and Go From Last. See *Cue List Properties (on page 349)*.

The list of targets will display in the Fader Configuration List (Tab 36), in the Fader List (Tab 35), and in the Fader Ribbon.

# Eos Family User Manual v3.2.0 — Chapitre 15 : Advanced Manual Control

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 15
## Advanced Manual Control
>
>
### About Advanced Manual Control

This section describes some advanced features for manual control functions. These features can save you valuable programming time.

> For additional manual control functions, see *About Manual Control (on page 240)* .

### Using [Copy To]

[Copy To] allows you to copy all data from one channel to another, either within the current working mode or to a different record target. [Copy To] works much like [Recall From], but in the opposite direction, [Copy To] forces data to a channel from the selected channel, whereas [Recall From] pulls it from a channel to the selected channel. For information on using [Recall From], see [*Using [Recall From] (on the facing page)*](#_bookmark352)

By using the IFCB category buttons in the ML Controls display or the parameter buttons, you may copy subsets of channel data. Entire cues, cue ranges, and cue lists can be copied to other locations. To only copy over intensity and parameter levels, use the {Only Levels} softkey. This will exclude discrete timing information.

To copy over data from only active channels, use the {Only Active} softkey.

When referenced data is copied, if the copy target also has data in the reference that is being copied, the target will be placed in that reference (such as, color palette 1), at its stored values. If the copy target is not included in the reference, absolute data will be copied to the target, and not the reference.

Below are some examples of copy commands from record targets. This command is very versatile and the following list is far from exhaustive:

-   [2] [Copy To] [Cue] [5] [Enter] - copies all information for channel 2 to cue 5.

-   [2] [-] {Focus} [Copy To] [Cue] [5] [Enter] - copies all parameter data for channel 2, other than focus, to cue 5.

-   [Group] [3] [Copy To] [Preset] [6] [Enter] - copies current information for group 3 to preset 6.

-   [3] [Copy to] [6] [Cue] [8] [Enter] - copies the data from channel 3 to channel 6 in cue 8.

-   [3] [Copy to] [4] [Thru] [9] [Enter] - copies the data from channel 3 to channels 4 through 9.

-   [3] [Copy to] [8] [Cue] [2] [/] [1] [Q Only / Track] [Enter] - copies the data from channel 3 to channel 8 in cue 2/1 and takes exception to the track/ cue only settings in regard to subsequent cues in cue list 2.

-   [Cue] [2] [/] [Copy to] [Cue] [7] [/] [Enter] - copies all of the contents of cue list 2 to cue list 7.

-   [Cue] [1] [/] [1] [Thru] [1] [0] [Copy To] [Cue] [5] [/] [5] [Enter] - copies cues 1 through

> 10 from cue list 1 to cue list 5, starting with cue 5.

-   [1] [Copy To] [2] [0] {Only Levels} [Enter] - copies only the intensity and parameter information from channel 1 to channel 20.

-   [1] [Copy To] {DMX} [2] - copies the DMX value from channel 1 to channel 2.

-   [1] [Copy To] [2] {From Absolute} [Enter] - sets channel 2 to channel 1\'s absolute level.

-   [1] [Copy To] {Live} [Enter] - copies channel 1\'s level to the live output. In Live, you can use [Sneak] with [Copy To] to fade in the change.

    -   [1][2] [Copy To] [2] [Sneak] <Time> 7 [Enter]

> Copies the recorded data from channel 12 to channel 2 and sneaks it in 7 seconds.

Using the {HTP} softkey with [Copy To] will cause any intensity levels to be ignored if they are less than or equal to the copied value.

> Channels 1 and 2 are at 50% in cue 10, and in cue 11 channel 1 is at 10% and channel 2 is at full. If you are in cue 11, and use the syntax:

-   [1] [Thru] [2] [Copy To] [Cue] [1][0] {HTP} [Enter] Channel 1 will remain at 50% and channel 2 will go to full.

#### Using Move To

While technically not a manual control instruction, Move To will be very useful when managing record target data stored from manual control.

When a Move To command is given, data is removed from its current location and moved to its new location. If the new location already contains data, a confirmation is required by Eos (unless disabled in Setup). See *Record Defaults (on page 220)*. Existing data in the new location will be completely overwritten if a Move To command is confirmed.

Press [Copy To] [Copy To] to access Move To. The following are examples of using Move To:

-   [Color Palette] [1] Move To <Color Palette> [5] [Enter]

-   [Preset] [3] Move To <Preset> [8] [Enter]

-   [Cue] [9] Move To <Cue> [2] [Enter]

-   [Snapshot] [4] Move To <Snapshot> [7] [Enter]

-   [Preset] [1] Move To [Color Palette] [3] [Enter]

    -   Element Classic users will need to use [Shift] & [Int Palette] instead of [Preset]

-   [Int Palette] [5] Move To [Preset] [1] [0] [Enter]

When using Move To to convert a preset into a palette, all information not relevant for that palette will be removed.

#### Copy To and Move To for Labels, Scenes, and Notes

The [Copy To] and Move To ([Copy To][Copy To]) commands can be used to copy or move labels between any target types that can have labels. A {Labels Only} softkey will display.

-   [Sub] [1] [Copy To] [Sub] [3] {Labels Only} will copy submaster 1\'s label to submaster 3.

Labels, scenes, and notes can be copied or moved between cues. The {Labels Only}, {Scene Only}, and {Notes Only} softkeys will display.

-   [Cue] [3] Move To [Cue] [6] {Notes Only} will move the note from cue 3 to cue 6.

### Using [Recall From]

[Recall From] is similar to [Copy To], except that it retrieves data from other locations, and can be used only for a channel list recalling from the same channel list but in a different location (for example, a cue). [Recall From] is essentially a "copy from" command. For information on

> using [Copy To], see [*Using [Copy To] (on page 366)*](#_bookmark349)

All parameter data for selected channels will be recalled, or by using the IFCB category buttons or parameter buttons, you may recall subsets of channel data. To recall only levels and not effect, timing, mark or other non-level data, use the {Only Levels} softkey.

To recall data from only the active channels, use the {Only Active} softkey. In Live, you can use [Sneak] with [Recall From] to fade in the change.

Below are some examples of recall commands from record targets:

-   [2] [Recall From] [Cue] [5] [Enter] - recalls all recorded data from cue 5 for channel 2.

-   [2] [-] {Focus} [Recall From] [Cue] [5] [Enter] - recalls all data for channel 2 from cue 5, except focus (pan/tilt - XYZ) data.

-   [Group] [3] {Color} {Focus} [Recall From] [Preset] [6] [Enter] - recalls the color and focus information from preset 6 for the channels in group 3. Could also be used with a channel selection set instead of a group.

-   [Group] [3] {Color} [Recall From] [Cue] [7] {Make Absolute} [Enter] - recalls color data for group 3 from cue 7 and breaks any references to record targets.

-   [2] [Recall From] [Sub] [4] [Enter] - recalls all recorded parameter data from sub 4 for channel 2.

-   [Recall From] [Intensity Palette] [1]- recalls all of the values stored in intensity palette 1.

-   [1][0] [Recall From] [Cue] [2] [Sneak] <Time> 7 [Enter] - would recall the recorded data that cue 2 has for channel 10 and sneak it in 7 seconds when used in live.

-   [Recall From] [Cue] [1][0] {Only Active} [Enter] - recalls data from only the active channels, which are those channels with intensities above 0, if no channel selection had been previously made.

-   [Recall From] [Cue] [2] [Enter] - would result in a selection of the channels used in that cue and their values. Any channels that are used in the cue list but do not currently have an intensity in the recalled from cue will be set to zero. Pressing [At] afterwards would post a numeric list of those channels to the command line.

In Live or Blind, hitting [Recall From] [Recall From] will put [Recall From] [Cue] on the command line.

Using the {HTP} softkey with [Recall From] will cause any intensity levels to be ignored if they are less than or equal to the recalled value.

> Channels 1 and 2 are at 50% in cue 10, and in cue 11 channel 1 is at 10% and channel 2 is at full. If you are in cue 10, and use the syntax:

-   [Recall From] [Cue] [1][1] {HTP} [Enter]

> Channel 1 will remain at 50% and channel 2 will go to full.

#### Recall From Park

You can use [Recall From] [Park] to set a channel or parameter to the same level as the current park value.

> Channels 1 through 5 are parked at 55. To recall that level to channels in live or blind, use the following syntax:

-   [1] [Thru] [1][5] [Recall From] [Park] [Enter]

> Channels 1 through 5 will be set to 55 and channels 6 through 15 will be unaffected.
>
> For more information about using Park, see *About Park (on page 426)*
>
> **Note:** *This does not release the Park buffer.*

### Make Null

The {Make Null} softkey can be used to withhold parameter data from record or update actions in live, and remove parameter data from record targets in Blind. {Make Null} is applied using channel selection and can impact entire channels, individual parameters, or parameter categories.

#### Make Null In Live

When you apply a {Make Null} instruction to channels or parameters in Live, channel data is still visible onstage, but that data is essentially rendered invisible to record commands. Similar to filters (see *Record Filters (on page 356)*), {Make Null} acts as an "ignore" instruction in Live, not a remove instruction. When channel data is nulled, the values for that data in the live display turn grey and an "N" appears next to the data field.

{Make Null} differs from Park in that you can still manipulate data onstage (through manual control or through playback) but that data will be unavailable for record actions.

Some examples of using {Make Null} in Live are:

-   [1] [Thru] [5] {Make Null} [Enter] - converts all parameters of channels 1 through 5 into null data.

-   [2] {Color} {Make Null} [Enter] - changes only color data for channel 2 to null data.

-   [9] [Thru] [5] {Pan} {Make Null} [Enter] - changes only the pan data for channels 5 through 9 to null.

Null instructions are lifted in two different ways. First, as {Make Null} is a toggle state, it is possible to reselect the channel and parameter followed by {Make Null} [Enter]. This lifts the null state.

Additionally, a [Go To Cue] instruction will remove the null state.

#### Make Null In Blind

When applied in Blind, {Make Null} can be used to mask instructions in a cue after it has already been stored. A {Make Null} instruction can also be applied to channels/ parameters in palettes, presets, and submasters, thereby removing the data from the target entirely, in the same way that [At] [Enter] does.

When applied to channels/ parameters in cues, {Make Null} doesn't remove the data from the cue, it simply makes it unavailable for playback. It has the same effect on move instructions that it has on tracked values.

Some examples of using {Make Null} in Blind are:

-   [Color Palette] [1] [Enter] [3] {Magenta} {Make Null} [Enter] - removes all magenta parameter data for channel 3 from color palette 1.

    -   Element Classic users will need to use {Color Palette}

-   [Preset] [5] [Thru] [9] [Enter] {Intensity} {Make Null} [Enter] - removes all intensity data for all channels in presets 5 through 9.

-   [Cue] [8] [Enter] [2] [Thru] [7] {Make Null} [Enter] - nulls all data for channels 2 through 7 in cue 8.

-   [Cue] [9] [Enter] {Intensity} {Make Null} [Enter] - nulls all intensity data for all channels in cue 9.

In the cue scenarios above, {Make Null} differs from using [At] [Enter] in that instead of allowing values established in previous cues to track in, {Make Null} both restricts the recorded data from playing back and prevents other values from tracking in. Therefore, if the cue were executed as an out-of-sequence cue, no data would play back or track in for any nulled values.

#### Release

Release is an extension of the {Make Null} command in Blind. When Release is used, it behaves like Make Null, but it also releases the channel and parameter data to its background state, if one is available, or fades out the intensity instead.

Release can be used to mask instructions in a cue after it has already been stored. The data is not removed from the cue.

Release is applied in Blind via the {Release} softkey, or the [Release] hardkey if available.

-   [Cue] [3] [Enter] [2] {Release} [Enter] - releases all data for channel 2 in cue 3.

-   [Cue] [2] [Enter] [3] {Color} [Release] - releases the color data for channel 3 in cue 2.

> **Note:** *Release tracks forward through a cue list until the Release command is removed or a move instruction happens.*

When release has been applied, the released content will display in gray with a R in Blind.

![](media/media/image263.png){width="1.799080271216098in" height="0.9099989063867017in"}

A Release flag will also appear in the Playback Status Display and the Cue List Index.

### Make Manual

The {Make Manual} softkey can be used to convert cue or submaster data into manual values, allowing it to be included in [Record], [Record Only], and [Update] operations.

-   [5] {Make Manual} [Enter] - selects channel 5 and makes all of its current parameter settings manual data.

-   [8] {Focus} {Make Manual} [Enter] - selects channel 5 and makes all of its focus data manual.

-   [9] [Thru] [3] {Color} {Intensity} {Make Manual} [Enter] - selects channels 3 through 9 and makes their color and intensity values manual.

### Make Absolute

Referenced data can be transformed into absolute data using the {Make Absolute} softkey. This softkey is available in Live or Blind. Referenced data is channel/ parameter data that is derived from a palette or preset. {Make Absolute} can be used to leave a parameter unchanged, but break its palette or preset reference.

The following examples illustrate how to change referenced data into absolute data.

-   [4] {Make Absolute} [Enter] - selects channel 4 and makes any referenced data for that channel absolute data.

-   [7] {Color} {Make Absolute} [Enter] - selects channel 7 and makes its color data absolute.

-   [3] [Thru] [9] {Color} {Intensity} {Make Absolute} [Enter] - selects channels 3 through 9 and makes their color and intensity data absolute.

In each of these examples, the channel display will change to show the result of the command. Wherever the reference was previously indicated (IP, FP, CP, BP, Pr), an absolute value (numerical) will be seen.

In Live, data that is changed to absolute is also made manual, thereby requiring a record or update instruction if the results are to be maintained.

{Make Absolute} can also be used in conjunction with an update command, allowing a cue to be updated while also breaking the reference to palettes or presets that were manually modified.

### Capture

-   [Update] {Make Absolute} [Enter]

Updates the active record target. Any manual values that were modifications to a palette or preset stored in the cue will be updated as absolute data in the cue. The reference will be discarded.

> **Note:** *Not available on Element Classic.*

Capture is a manual priority state. Any captured channel parameter data will be unaffected by playback, but will respond to manual control operations.

When channels are selected, [Capture] [Enter] captures all parameters of those channels. They will remain unavailable for playback or submaster override until they are released from the captured state. Capture is a toggle state, so to release parameters from a captured state, press [Capture] [Enter] again.

-   [1] [Thru] [9] [At] [Full] [Capture] [Enter]

> A "C" is displayed next to the captured parameters (intensity) in the channel display. The selected channels are now captured and are unavailable for playback or submaster instructions until they are released from capture.

You may also capture specific parameters of a channel using the parameter buttons in the CIA.

-   [7] {Focus} [Capture] [Enter]

If a group of channels are selected, and some of those channels are captured and some are not, the first press of [Capture] releases all channels from the captured state and the second press captures all manual settings for the selected channels.

Uncaptured channels remain at their current values until restored to previous values or a new instruction is provided. You may restore channels to their background or default state using the [Sneak] [Enter] feature (see *Sneak (on page 267)*). Or you may leave them in a manual state until a new instruction is received.

It is also possible to latch capture on. This will automatically capture all manual changes as they are made. Pressing [Capture] [Capture] [Enter] automatically captures subsequent manual changes. The command line will read "Capture Enable \" and the Capture hardkey will illuminate. To remove the capture latch, press [Capture] [Capture] [Enter] again. Capture latch works on a user by user basis.

### Query

> **Note:** *[Query] is used in the examples below. Ion Classic and Element Classic users will need to use {Query}.*

[Query] is used to select channels that meet criteria specified by you. These selections are conditional, based on what type of fixture a channel is or what that channel is doing, isn\'t doing, can do or cannot do. These criteria are established in the command line using the softkeys, the keypad, and the direct selects.

#### Query Softkey Options

When [Query] is used, the following softkey conditions are available:

-   Is In

-   Isn't In

-   Can Be

-   Can't Be

-   Or

-   Moves Only

-   Unpatched

-   Mark (cue where the intensity is active)*

-   Less Than (includes equal to)

-   Greater Than (includes equal to)

-   Broken Mark*

-   Marking (future cue)*

-   Track

-   Up Moves

-   Down Moves

-   Live Moves

-   Dark Moves

-   Autoblock

-   Block

-   Assert*

-   Part

-   Park

-   Time

-   Delay

-   Capture*

* Not available on Element Classic.

> **Note:** *Unless otherwise specified, Eos assumes that a query will apply to current output. Therefore use of the {Is In} softkey is optional.*

The CIA also repaints to display all of the available softkeys by which you can search. These can be used in defining your query criteria.

##### Default

![](media/media/image264.png){width="1.9855850831146107in" height="1.1479155730533683in"}

Includes the query softkeys along with additional query conditions.

##### Text

![](media/media/image265.png){width="2.4477340332458444in" height="1.151874453193351in"}

-   {Keywords} - displays buttons for all the text used in the text 1 through 10 fields and all of the default keywords in Patch.

-   {Gel} - displays all of the gels used in the current show file.

-   {Text 1} - {Text 10} - displays only the text used in that text field. See also *Renaming Text Fields in Patch (on page 185)*.

##### Fixture Types

![](media/media/image266.png){width="2.736827427821522in" height="1.1360411198600175in"}

Displays buttons for all of the fixture types used in the current show file.

#### Using Query

As a query is defined in the command line, channels will be specified in the Live/ Blind display. When an [Enter] command is used to end the query, the remaining channels of the query will be selected.

> You wish to find channels which are in color palette 2 and have an intensity of 50%:

-   [Query] <Is In> [Color Palette] [2] [At] [5] [0] [Enter]

> In the Live/ Blind display, any channels meeting this criteria will be selected.
>
> You may use [Next] and [Last] to cycle through the query selection, one channel at a time to control only a specific channel.

Other examples of using a query are:

-   [Query] {Isn't In} [Beam Palette] [2] [5] [Enter]

-   [Query] {Accessory} {Can Be} [Color Palette] [8] [Enter]

-   [Query] {Unpatched} [Delete] [Enter] [Enter](Only works while in Patch.)

-   [Query] {Fixture Type} {Revolution} {Can Be} [Focus Palette] [6] {Isn't In} [Cue] [4] [Thru] [9] [Enter]

-   [Next] [Next] [Enter] - selects one channel from the query result

> Additionally, in Patch you can define up to ten query keywords for each channel. These keywords can be used to create a query condition as well (See *Adding Keywords in Patch (on page 185)*).

Keywords defined in Patch will appear in the CIA when [Query] is pressed. They can then be used in a query like this:

-   [Query] {Your keyword} {Can't Be} {Beam Palette 5} [Enter]

Hardkeys on the face panel, such as [Time] can also be used to construct a query.

### Undo

Undo is a method to revert certain operations performed in the software. You can use [Undo] to reverse any command that results in a change to data that would be saved to the show file or any command that changes manual levels in Live.

If there are any commands in the command line, pressing [Undo] once clears the command line. Once the command line is empty, pressing [Undo] will start the undo process.

When [Undo] is pressed from an empty command line, the command history display will open in the CIA and the most recent completed command is highlighted in gold. If you press [Enter], you will undo your last command. [Shift] & [Clear] can be used to clear the command line as well. If the most recent completed command is grayed out, it cannot be undone. Pressing [Undo] again will select the first command which can be undone.

![](media/media/image267.png){width="4.938863735783027in" height="2.35625in"}

You may use the page arrow keys or a mouse to select multiple commands. When [Enter] is pressed, an advisory is posted. When [Enter] is pressed again, all highlighted commands will be undone and subsequently removed from the command history. When removing more than one command, a confirmation is required.

After an Undo has been performed, a {Redo} button will appear in the command history. You may press this button followed by [Enter] and the last undo will be "redone" to reinstate the removed commands

In a multiple user environment, each user is only able to undo the changes that they made. In the undo command history, the user will only see the commands that they used.

> **Note:** *Not all commands can be undone including playback actions, manual attributes placed on channels or encoder actions, and Augment3d model edits.*

#### Command History

Command histories are kept for each editing session, which begins when a new show file is created or when an existing show file is opened, merged, or imported.

Each user builds an individual command history, specific to the commands entered by their user number.

You can open the command history at any time by pressing [Displays] <More Sk> {Cmd History}.

> **Note:** *Commands that do not affect manual input or record targets (loading a cue, running a cue, or moving a submaster) are not included in the command history.*

Pressing [Undo] [Undo] will scroll to the most recent undo-able command in the command history display. To undo the command, press [Enter].

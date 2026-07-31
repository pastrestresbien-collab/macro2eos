# Eos Family User Manual v3.2.0 — Chapitre 12 : Cues & the Cue List

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 12
## Cues & the Cue List
### About Cues & Cue Lists

A cue is a record target comprised of channels with associated parameter data, discrete (channel/parameter level) timing, cue timing, and cue attributes (such as preheat, follow or hang instructions).

When cues are created, they are stored in a single cue list by default, identified as cue list 1. While cues can be recorded to multiple lists, this section deals primarily with working in a single cue list.

> For more information on multiple cue lists, see *About Working With Multiple Cue Lists (on page 360)*

**Note:** *Multiple cue lists are not available on Element 2 and Element Classic.*

### Basic Cueing

In Setup, you determine if Eos will operate in a Cue Only or Tracking mode. See *Tracking vs. Cue Only (on page 7)* By default, the system is set to tracking, therefore this section primarily addresses working in tracking mode. The current mode is displayed in the upper left corner of the live/blind display. It is important to know which mode you are working in, as it impacts how cues are edited.

-   If your console is set in Track mode (default), changes move forward through the cue list until a block or a move instruction is encountered.

-   If your console is set in Cue Only mode, changes to cues have no impact on subsequent cue data.

#### Cue Numbering

Cues can be numbered from 0.001 - 9999.999. You can have up to 10,000 cues.

Eos provides you with multiple ways to number your cues. The most common methods are listed below:

-   After pressing record, enter a cue number which can be a whole number (1) or a decimal number (1.1).

-   After pressing record, rather than entering a cue number you may press [Next], which will automatically number the cue with the next sequential number in the same cue list. For example, the current cue is numbered cue 1.1, pressing [Record] [Next] will automatically number the new cue 1.2.

-   When recording decimal cues, it is not necessary to specify the leading cue number if a cue has already been recorded. For example, if the current cue is numbered 5, when you enter the next record command, you can just enter [.] [5] to record cue 5.5.

-   Whole numbered cue - [Next] increments the next whole numbered cue.

-   Tenths numbered cue (.1) - [Next] increments in tenths.

-   Hundredths (.01) numbered cue - [Next] increments in hundredths.

-   Thousandths (.001) numbered cue - [Next] increments in thousandths.

### Recording Cues in Live

When using [Record], all parameters of any fixtures that have non-home values, either from manual control, other cues, or submaster playback are stored in the target cue.

Channels that have all home values, meaning they have never been changed, are not included in the record action, unless you specifically select the channel and press {Make Manual}. See *Make Manual (on page 370)*.

Possible exclusions are parameters categories or individual channel parameters withheld by use of filters (see *About Filters (on page 356)* ). You can also select individual parameters of individual channels (such as Cyan and Iris) and place them in a null state using the {Make Null} button if the values are not needed in the cue you are recording. See *Make Null (on page 369)*.

You could also use {Release}. Release is an extension of the {Make Null} command in Blind. When Release is used, it behaves like Make Null, but it also releases the channel and parameter data to its background state, if one is available, or fades out the intensity instead.

Release can be used to mask instructions in a cue after it has already been stored. The data is not removed from the cue. See *Release (on page 370)*.

Eos consoles are tracking, meaning once something is recorded into the cue list, the cue list will always contain information about that channel/ parameter unless it is nulled, by using the

{Make Null} command, released by using the {Release} command, or filtered using the parameter filters.

When cues are recorded they are automatically played back and manual values are released, unless auto playback on record has been disabled in setup. See *{Auto Playback} (on page 220)*. Upon playback, displayed parameter levels will be color coded for clarification of the record action:

-   Blue - intensity has increased from the previous cue or a non-intensity parameter has changed

-   Green - intensity level has decreased from the previous cue or a non-intensity parameter has marked

-   Magenta - level has tracked from a previous cue

-   White - level has been blocked (see *Block (on page 332)*)

#### Using Record in Live

When the [Record] button is pressed the keypad defaults to cue mode; use of the [Cue] button is optional. The following are representative examples of recording cues in Live. Once the cue record has been specified, cue attributes such as timing can be combined and entered in any order you wish.

-   [Record] <Cue> [5] [Enter] - records all parameters of any channels with non-default data into the specified cue number 5.

-   [Record] <Cue> [5] [Label] [name] [Enter] - records the specified cue and provides an alphanumeric label.

> **Note:** *When using the console in tracking mode or when using track editing, it is important to understand the concept of Blocking. A cue containing a Block flag will stop edited levels from tracking through that cue. Blocks are often placed on the cue at the top of an act or scene, or anywhere you want to protect cues from levels that may track in from upstream cues. Block flags should also be set on cues that you want to have behave as blackouts (see Block (on page 332)).*
>
> **Note:** *[+] can be used with [Record] to specify a range of cues for recording. See Update [+] (on page 343).*

#### Using Record Only in Live

> **Note:** *[Record Only] is used in the examples below. Element Classic users will need to use [Record] [Record].*

[Record Only] is similar to [Record] except that it selectively stores only manually set values, preventing unwanted levels (such as from a submaster or another cue list), from being recorded into the cue. Therefore, when used to record a cue, only the manual data for channels will be stored in the cue. Any values in the previous cue that were unchanged will track into the new cue.

All of the same commands used for [Record] may also be used for [Record Only].

-   [Record Only] <Cue> [Next] [Enter] - stores only the manually set values into the next cue in the list.

-   [Record Only] [Cue] [3] [Enter] - stores only the manually set data into cue 3.

> As with [Record], filters can further restrict stored data if deployed when using [Record Only]. See *About Filters (on page 356)*
>
> **Record and Record Only [+]**

[+] can be used to specify a range of cues when using [Record] and [Record Only].

> To record only cues 5, 10, and 15:

-   [Record] <Cue> [5] [+] [1][0] [+] [1][5] <CueOnly/Track> [Enter] To update the current cue and cue 7:

-   [Record Only] [+] <Cue>[7] <CueOnly/Track> [Enter]

> **Note:** *If no cue number is entered before the [+], the current active cue will be used.*

### Cue Only / Track

> **Note:** *For a more detailed summary of Cue Only and Tracking modes, see Tracking vs. Cue Only (on page 7).*

#### In Track Mode

When you create a new cue, any channel parameter data from the previous cue is tracked into the new specified cue. Any changes in this new cue will also track forward into subsequent cues until a move instruction is encountered. The [Q Only/Track] key is an exception to this behavior. When you record a cue in the middle of an existing cue list, using the [Q Only] button will prohibit new information from tracking into the subsequent cue. When you rerecord or update a cue, the modifications will not track forward.

> **Note:** *In the following examples, the command [Q Only] indicates the same key hit of [Q Only/Track] which is a single button on the keypad. The system setting determines the actual context of the button depending on the mode in which the system is operating. For clarity, only the contextual function of the button is used in the examples.*

With system set to Track

-   [Record] <Cue> [5] [Q Only] [Enter] - records cue 5. New values or changes will not track into the subsequent cue.

-   [-] [Color] [Record] <Cue> [5] [Q Only] [Enter] - as above the recorded data will not track forward and all color data is excluded from the record operation.

-   [Record Only] <Cue> [5] [Q Only] [Enter] - records all manual data, but doesn't allow it to track into subsequent cues.

-   [-] [5] [Record] <Cue> [6] [Q Only] [Enter] - records the specified cue, except the contributions from channel 5. The stored data will not track forward in the list.

On Element Classic, double pressing [Record] will post Record Only to the command line.

#### In Cue Only Mode

When you create a new cue, any channel parameter data from the previous cue is tracked into the new cue. The [Q Only/Track] key can be used as an applied exception to the cue only/ track system setting.

> **Note:** *In the following examples, the command [Track] indicate the same key hit of [Q Only/Track] which is a single button on the keypad. The system setting determines the actual context of the button depending on the mode the system is operating. For clarity, only the contextual function of the button is used in the examples.*

With system set to Cue Only

-   [Record] <Cue> [5] [Track] [Enter] - records cue 5. This data will track forward in the list until the next move instruction or block.

-   [-] [5] [Color] [Record] <Cue> [6] [Track] [Enter] - records the specified cue, except the color data from channel 5. The data will track forward in the list until the next move instruction or block.

-   [Record Only] <Cue> [2] [Thru] [7] [Track] [Enter] - stores all manual data. The stored data will be forced to track from cue 2 through 7 through any blocks or move instructions. After cue 7, values will continue to track until a move instruction or block is encountered.

### Selective Storing Cues in Live

Cues can also be modified using selective storing, which allows you to specify only the channels and or parameters that you want to store. When using a selective store, you must specify the channel list to be included or excluded, identified by [Thru], [+], [-], as part of the [Record] or [Record Only] command.

#### Using Selective Store

You may use the [-] button to withhold information from a cue or use the [+] button to specify a particular channel/ parameter to be included in the record action. These actions are both selective stores.

> For information on a selective store using filters see *Partial Filters (on page 356)*.

Since Eos consoles are tracking, any channels not included in the selective store, but that do have values in the previous cue will track into the recorded cue. This is true even when the console is in Cue Only mode. To remove intensity values that would otherwise track when on a selective store, the rem dim command can be used. See *Remainder Dim (on page 264)*.

##### Using a Positive Selective Store

You may record only specified parameters into cues. If the cue has already been stored, this action adds the specified channel parameters to the existing cue data.

To record only specific channels into a new target cue:

-   [1] [Thru] [5] [Record] <Cue> [4] [Enter] - records only channels 1 through 5 into cue 4.

-   [channel list] [Record] <Cue> [5] [Rem Dim] [Enter] - stores the selected channels into the target cue. Any channels active in the previous cue that are not in the selected channel list will be set to zero in cue 5.

-   [2] [Thru] [8] [Record Only] <Cue> [9] [Enter] - stores only the manually set data for channels 2 through 8 into the target cue 9.

-   [Group] [2] [Record Only] [Cue] [5] [Enter] - stores only the manual data from group 2 into cue 5.

To record only specific parameters into a target cue:

-   [1] [Thru] [5] {Focus} {Color} [Record] <Cue> [4] [Enter] - records the focus and color data for channels 1 through 5 into cue 4. Any other data on stage would not be stored in the target cue.

-   [selected channels] {Color} [Record Only] <Cue> [4] [Enter] - stores only the color data for the selected channels into cue 4.

Using a selective store for a new record target will track in values from the previous cue that are not included in the record action.

Using a selective store for an already existing cue will modify the selected data only, leaving the rest of the cue untouched. This does not overwrite the whole cue.

##### Using a Negative Selective Store

It is possible to withhold data from a cue by using the [-] key as follows:

-   [-] [Group] [3] [Thru] <Group> [6] [Record] <Cue> [9] [Enter] - records the specified cue, with the exception of any channels associated with groups 3 through 6.

-   [-] [3] [Thru] [6] [Record] <Cue> [9] [Enter] - records the specified cue, with the exception of channels 3 through 6.

-   [-] [Sub] [7] [Record] [Enter] - records the selected cue, without the input from submaster 7.

-   [-] [Sub] [Record] [Enter] - as above, except withholds the contents of all submasters.

-   - {Color} [Record] <Cue> [8] [Enter] - records cue 8 without any color data.

### Timing

Cue timing can be applied in a variety of ways. At a cue level, timing categories are provided for intensity up, intensity down, focus, color and beam transitions. Each of these times can have an associated delay. Timing can also be applied directly to a channel or a specific parameter. This is called discrete timing.

Time can be entered in minutes and seconds (example 10:15) with valid fade times from zero to 99:59 ( 99 minutes and 59 seconds), or seconds and tenths of seconds (example 1.3), or 100ths of seconds (example 1.35) with valid fade times from zero to 99.99. When no time is applied at a cue level, the defaults established in Setup are used. See *Cue Settings (on*

> *page 214)*
>
> You want the time for cue 1 to be 10 minutes and 15 seconds.

-   [Cue] [1] [Time] [1][0][1][5] [Enter]

> The command line will show the time as Cue 1 Time 10:15.
>
> If you want the time for cue 1 to be in seconds and tenths of a second, like 1.3 seconds, you will type using a decimal.

-   [Cue] [1] [Time] [1][.][3] [Enter]

> The command line will show the time as Cue 1 Time 0:01.3.

#### Setting Cue Level Timing

Unless you specify otherwise, Eos assigns default fade times to any cue you record. Default timing is designated in Setup (*Cue Settings (on page 214)*). Cue level timing can be applied when a cue is recorded or can be added or modified later.

Following are some examples of record commands with cue level timing:

-   [Record] <Cue> [5] [Time] [9] [Enter] - puts a time of 9 seconds on all parameter timing categories.

-   [Record] <Cue> [6] [Time] [3] [Time] [9] [Enter] -specifies the intensity up, focus, color, and beam times at 3 seconds and the down time at 9 seconds. The first instance of [Time] is used for intensity up fade (meaning intensity value is fading to a higher level than previously set) and the second instance of [Time] is used for intensity down fade time (intensity values fading to a lower level than previously set).

-   [Record] <Cue> [2] [Time] [Enter] - resets time to default value defined in Setup.

> **Note:** *Unless FCB timing is specifically set, it always defaults to the up fade time value.*

##### Manual Timing at a Cue Level

It is possible to assign a time of manual, for manual parameter transition through the associated fader. See *Manual Timing Control (on page 389)*. Manual times are assigned by using the {Manual} softkey that displays after [Time] is pressed when recording a cue.

-   [Record] <Cue> [4] [Time] {Manual} [Enter] - applies a manual time. If the cue had previously been given split times, would apply a manual to the up fade, focus, color, and beam times. If the cue had a single time, all of the timing would be manual and controlled by the fader.

-   [Record] <Cue> [4] [Time] [Time] {Manual} [Enter] - applies a manual intensity time to the down fade.

-   [Record] <Cue> [4] {Color} [Time] {Manual} [Enter] - applies a manual time to any color data changes in cue 4.

#### Non-intensity Parameter Category Timing

Timing can be also applied for Focus, Color and Beam parameter categories at a cue level. By default, FCB timing is the same as intensity upfade time. Once FCB timing is different than intensity upfade time, those times are no longer affected by intensity upfade changes.

When you apply a time to an individual parameter category and that category has no movement, the time is displayed in gray. The specified timing will remain in gray until that category is provided with a move instruction, at which point it the timing will display in white.

-   [Record] <Cue> [2] {Color} [Time] [7] [Enter] - records cue 2 with a cue level color time of 7.

-   [Record] <Cue> [2] {Color} [Time] [Enter] - resets the color time of cue 2 back to the default value.

-   [Record] <Cue> [2] [Time] [Time] [Time] [7] [Enter] - records cue 2 with a cue level focus time of 7. In this example, each press of the [Time] key steps through each timing value (up time, down time, focus time, color time and beam time).

-   [Record] <Cue> [2] [Time] [7] [Enter]- records cue 2 and puts a time of 7 on all parameter categories. This only works if FCB timing was previously untouched. If

> FCB timing had been changed, this syntax example would change just the upfade time to 7.
>
> **Note:** *It is not necessary to rerecord a cue to alter stored timing data. You can simply redefine the time by specifying the cue and re-entering the time value(s).*

-   *[Cue] [5] [Time] [8] [Enter] -redefines the all category times to 8 seconds. This only works if FCB timing was previously untouched. If FCB timing had been changed, this syntax example would change just the upfade time to 8.*

-   *[Cue] [2] {Color} [Time] [5] [Enter] - redefines color time to 5 seconds.*

-   *[Cue] [3] {Focus} [Time] [-] [2] [Enter] - removes 2 seconds from the current time.*

-   *[Cue] [7] {Beam} [Time] [+] [3] [Enter] - adds 3 seconds to the current time.*

#### [Time][/]

The [/] key can be used with [Time] to control the intensity upfade and downfade times, and delays.

-   [Cue] [1] [Time] [/] [5] [Enter] - places a downfade time of 5 on the cue, while splitting the upfade, which preserves its current value.

-   [Cue] [2] [Time] [/] [Enter] - removes the downfade time and makes the downfade match the upfade.

-   [Cue] [3] [Time] [4] [/] [Enter] - sets the upfade time, and splits the downfade without splitting the FCB times.

-   [Cue] [5] [Time] [4] [/][3] [Enter] - sets the upfade and the downfade times.

-   [Cue] [4] [Time] [2] [/] [/] [Enter] - changes only the intensity upfade time and splits the downfade and FCB times preserving their current value.

#### Discrete Channel and Parameter Timing

Rather than using cue times, timing can be applied directly at a parameter or channel level. This is referred to as discrete time.

Discrete timing can be applied to a specific channel or parameter. You must select the channels that you want to apply the time to, otherwise the system assumes you are addressing the selected cue.

Following are some examples of use:

-   [channel list] {Color} [Time] [3] [Enter] - adds a time of 3 seconds to all of the color parameters of the channel list that have a move instruction.

-   {Focus} [Time] [7] [Enter] - assigns a time of 7 seconds for the focus attribute of all selected channels.

-   [Select Manual] {Beam} [Time] [7] [Enter] - selects channels with manual data and applies a time of 7 to any manual beam values.

    -   Ion Classic and Element Classic users will need to use {Select Manual} Discrete delay times can also be placed on a channel parameter.

-   [1] {Color} [Time] [4] [Delay] [3] [Enter] - places a time of 4 seconds and a delay of 3 seconds on all color parameters of channel 1.

The [+] and [-] hardkeys can be used to increase or decrease discrete timing values.

-   [channel list] [Time] [+] [3] [Enter] - increases the discrete timing values by 3 seconds.

-   [channel list] [Delay] [-] [1] [Enter] - decreases the discrete delay value by 1 second.

When timing has been applied to a channel parameter in live, a small red "t" will be displayed with the channel. This indicates the timing must be stored or updated to the required cue.

When this is done, the "t" is displayed in blue. In the Playback Status Display, a "+" is displayed in the associated parameter category time field, indicating that not all of the parameters in the cue will use the cue timing.

[About] & [Time] can be held down to see the discrete delay /time information for channels in Live /Blind. Delay is displayed first, followed by the timing value.

> **Note:** *Any conditions placed on channels or parameters in Live (discrete timing, asserts, blocks, etc) must be stored or updated to the cue.*

##### Discrete Time as a Percentage

Discrete times can be entered as a percentage of the cue time.

-   [channel list] [Time] [/] [5] [Enter] sets the time to 50% of the cue time.

-   [channel list] {Focus} [Time] [/] [7][5] [Enter] - sets the discrete focus timing to 75%.

### Assigning Cue Attributes

> You can record cues with specific attributes to affect how cues behave when executed. Cue attributes include *Follow / Hang*, *Link / Loop*, *Delay Time*, *Rate*, *Curve*, *Cue Notes*, *Cue Label*, and *Scenes*. Cue attributes can be entered when the cue is initially recorded, or they can be added or modified at a later date.

When [Cue] is pressed, the {Attributes} softkey will display. Press {Attributes} to access the following softkeys:

-   {Rate}

-   {Note}

-   {Scene}

-   {Curve}

-   {Preheat}

-   {AF/MF} (Allfade/ Move Fade)

-   {Scene End}

> **Note:** *Preheat and Allfade are flags. See Preheat (on page 335) and AllFade (on page 335).*

#### Follow / Hang

A follow automatically activates the next cue in the sequence when the follow time of the associated cue has elapsed. The follow time begins counting from the moment the cue is executed.

The hang time is also an auto-follow, but rather than counting from the moment the cue is executed, it is calculated from the completion of the cue. You can assign a negative value to a hang time, allowing a subsequent cue to overlap an active cue.

You can assign either a follow time or a hang time, but not both. Both features are accessed using the [Shift] & [Delay] keys on the console or the softkey {Fw/Hg}. [Shift] & [Delay] or

{Fw/Hg} will put Follow on the command line, and [Shift] & [Delay] [Delay] or double pressing

{Fw/Hg} will put Hang.

> In the Playback Status Display, any cue that will be triggered by a follow or hang will have an arrow before the cue number. See *Indicators in the Playback Status Display (on page 110)*. This indicator can be disabled in the *Playback Status Display Configuration (on page 112)* menu.

Following are some examples of use:

-   [Record] <Cue> [5] [Shift] & [Delay] [8] [Enter] - records cue 5 and provides a follow time of 8 seconds which impacts the start of the next cue in the list. The following cue will automatically initiate on the same fader when the follow time has elapsed. The follow time will begin counting down when the associated cue (Cue 5) is executed.

-   [Record] <Cue> [5] [Shift] & [Delay] [Delay] [8] [Enter] - records cue 5 and provides a hang time of 8 seconds which impacts the start of the next cue in the cue list. The following cue will automatically initiate on the same fader when the hang time has elapsed. The hang time will begin counting down when the associated cue (Cue 5) is complete.

-   [Record] <Cue> [5] [Shift] & [Delay] [Delay] [-] [5] [Enter] - records cue 5 and provides a hang time of negative 5 seconds.

To remove a Follow /Hang time:

-   [Cue] [x] [Shift] & [Delay] [Enter]

> Cues with follow / hang times cannot also have associated *Cue Alerts (on page 390)*.

#### Link / Loop

##### Link

Link allows cues to be run out-of-sequence, by causing a different cue number to be loaded into the pending file of the playback fader when the cue that carries the link instruction is activated. If a follow or hang time is included with the cue attributes, the activation of the linked cue will occur when the follow or hang time has elapsed.

The link can be within the cue list or to a cue in another cue list, if available.

> Cues that link to other cues will display this information in a row under the cue in the Cue List Index and the Playback Status Display. This can be suppressed in the PSD configuration. See *Playback Status Display Configuration (on page 112)*.
>
> **Note:** *If a linked cue has a label, the label will be displayed in the link cue indicator.*

Following is an example of using link:

-   [Record] <Cue> [2] {Link/Loop} <Cue> [8] [Enter] - records the specified cue 2 and provides a link to cue 8 in the cue list. When cue 2 is played back, the linked cue is loaded into the pending queue of the associated fader.

##### Loop

Loop is provided as a method to link a series of cues and loop them a number of times in a sequence. Once the sequence of cues has played back the first time, the system recognizes the loop command and plays the sequence again, provided the target of the link is a previous cue.

If the first cue in the sequence is a cue with an assert attribute or has move instructions for channels, values from the last cue are not allowed to track through into the first cue when it is looped back. But without a move or assert in the first cue, values from the last cue will track into the first cue when it loops back.

A loop specified with "0" loops the sequence indefinitely. Following is an example of using loop:

-   [Cue] [2] {Link/Loop} <Cue> [1] {Link/Loop} [3] [Shift] & [Delay] [4] [Enter] - records a link from cue 2 back to cue 1. Because there is a follow time, cue 1 will automatically trigger 4 seconds after cue 2. If cue 1 also has follow time, it will automatically trigger cue 2. This sequence will run 4 times (once plus 3 loops) and then stop in cue 2. The loop value specifies the number of times the loop instruction will be performed. Since the sequence has run once prior to the loop command, the total number of passes will be the specified number of loops +1.

> You could apply {Go After Loop} on cue 2 to execute the next cue after a follow link/ loop sequence has ended. See *Cues & Triggers (on page 335)*
>
> **Note:** *All cues in a looping sequence must have Follow or Hang times in order for the loop to play uninterrupted.*

#### Delay Time

Delay can be useful when you do not want a parameter to change (for example - intensity down) until other changes have begun or completed their transition.

Delay times can be added to any cue or to any specific parameter category within the cue, which will postpone the parameter transition until the delay time has elapsed.

Following are some examples of recording with a delay:

-   [Record] <Cue> [2] [Delay] [5] [Enter] - stores cue 2 with a 5 second delay on intensity.

-   [Record] <Cue> [2] [Time] [9] [Delay] [3] [Enter] - records cue 2 with a 9 second fade for all parameter categories, delayed from Go by 3 seconds.

-   [Record] <Cue> [2] [Time] [7] [Delay] [Enter] - records cue 2 with a 7 second fade, and removes delay time.

-   [Record] <Cue> [2] [Delay] [/] [5] [Enter] - records cue 2 with a 5 second delay on the downfade.

Delay can be used to affect only the parameters in the specified category.

-   [Record] <Cue> [2] {Color} [Delay] [8] [Enter] - records cue 2 with a delay time of 8 seconds for the color category.

-   [Record] <Cue> [2] [Time] [Time] [Time] [Delay] [7] [Enter] - records cue 2 with a cue level focus delay time of 7. In this example, each press of the [Time] key steps through each timing value (up time, down time, focus time, color time and beam time.

#### Rate

The {Rate} softkey can be used to apply a rate adjustment to all timing in the cue. The default rate is 100%, which is real time. To slow a cue down, set the rate below 100%. To speed the cue up, set the rate above 100%. The range rate for a cue is 0 - 2000%. A timing value of 5, with a rate of 50% will replay in 10 seconds. A timing value of 5, with a rate of 200% will replay in 2.5 seconds.

Following is an example of using rate:

-   [Record] <Cue> [4] {Attributes} {Rate} [1] [2] [5] [Enter] - records the specified cue, and places a rate override instruction on all timing values. The cue would now be played back at 125% of recorded time values.

> **Note:** *You can use the playback rate override function to determine the rate at which you want to play the cue back, and then apply that rate to the cue. This eliminates the need to adjust all of the timing in the cue if you only need to speed it up or slow it down. See Rate Override (on page 388).*

#### Curve

{Curve} is used to affect the percent completion of a cue or part by applying the curve's output level as the percent completion for all fade calculations.

When a curve is applied to cue, it impacts only the intensity transitions in that cue. When applied to a cue part, it impacts any parameters moving in that part. For more information on creating and using curves, see *About Curves (on page 456)*

Following is an example of how to assign a curve to a cue:

-   [Cue] [6] {Attributes} {Curve} [5] [Enter] - applies curve 5 to cue 6.

#### Cue Label

[Label] is used to attach an alphanumeric label to a cue or cue part. Following is an example of how to apply a label to a cue:

-   [Record] <Cue> [7] [Label] <name> [Enter] - records cue 7 and applies the label as entered on the alphanumeric keyboard.

-   [Record] <Cue> [8] [Label] [Block] [Enter] - records cue 7 and applies the name of the hardkey as the label

Pressing [Label], when a label has already been applied to a cue, will display the label on the command line for editing. Pressing [Label] a second time will clear the label, or you can press [Clear] to remove the label one character at a time.

#### Cue Notes

Cues can have notes attached to them.

These notes can be viewed in the Playback Status Display and the Cue List Index by hovering a mouse over or tapping on the + in the Label column.

> You can also select to view the notes or the notes for the pending cue in a horizontal bar at the bottom of the PSD. See *Playback Status Display Configuration (on page 112)* for these additional display options.

To add a note to a cue:

-   [Cue] [n] {Attributes} {Notes}

To add a note to the currently selected cue, you can use [Shift] & [Label].

You can use the virtual alphanumeric keyboard or an external keyboard to enter the desired text.

> See *Copy To and Move To for Labels, Scenes, and Notes (on page 367)*.

#### Scenes

Scenes are a cue organization tool that provide a visual identifier for breaks in your show and allow for quick cue list navigation.

*(figure omise)*{width="5.488077427821523in" height="1.1903116797900262in"}

Scenes display in the cue list index and the playback status display as a green bar above the cue they are associated with in the list. An end of scene can also be created, and those display as a green bar under their associated cue.

You can recall a scene to quickly jump to a cue without needing to remember its number. To recall a scene, use the [Go to Cue] button and select the {Scenes} softkey.

This will open up the scene selection display in the CIA. The scene\'s label and cue will display. Press or click on the scene to select it.

*(figure omise)*{width="1.1653116797900263in" height="0.39187445319335085in"}

> Scenes can also be recalled by using the direct selects. See *Using Direct Selects (on page 113)*.

##### Creating a Scene Break

You can add a scene break by using the {Scene} softkey. For example, [Cue] <1 > {Attribute}

{Scene} will add a scene to cue 1.

The virtual alphanumeric keyboard will open. You will need to label the scene before it is created.

> See *Copy To and Move To for Labels, Scenes, and Notes (on page 367)*.

##### Creating a Scene End

You can specify where a scene ends by using the {Scene End} softkey. For example, [Cue] <5 >

{Attribute} {Scene End} will add a scene end to cue 5.

You can create a scene and a scene end at the same time by using [Thru]. For example, [Cue]

[1] [Thru] [5] {Scene} will add a scene to cue 1 and a scene end to cue 5.

##### Update Using Scene End

The {Scene End} softkey can also be used when updating the cues in a scene. For example, [Update] <Cue> [1] [Thru] {Scene End} will put the last cue of that scene on the command line.

> **Note:** *Tracking / cue only rules still apply. If your console is in tracking mode, and you want the update to stop at the scene end, you will need to use the [Q Only] command.*

##### Deleting Scenes

To delete a scene or scene end, you will need to use the following syntax:

-   [Cue] [n] {Attributes} {Scene} [Label] [Enter] - deletes the scene.

-   [Cue] [n] {Attributes} {Scene End} [Enter] - deletes the scene end.

If a cue with an attached scene break is deleted, the scene break will move to the subsequent cue.

#### Clearing Cue Attributes

To clear attributes from a cue:

-   [Cue] [n] [Shift] & [Delay] [Enter] - removes the follow or hang time from the specified cue "n".

-   [Cue] [n] [Label] [Label] [Enter] - removes the label from the specified cue "n".

-   [Cue] [n] {Link/Loop} [Enter] - removes the link instruction from the specified cue "n".

-   [Cue] [n] [Thru] [y] {Attributes} {Rate} [Enter] - removes the rate instruction in cues "n" through "y".

You may combine these to remove multiple attributes at once:

-   [Cue] [n] [Shift] & [Delay] {Link/Loop} [Enter] - removes the follow time and link instruction.

### Flags

> Flags can be applied to cues to change specific behaviors. Flags can be set for *Block*, *Assert*, *AllFade*, *Mark*, and *Preheat*.

#### Element Classic Flags

> On Element Classic, flags can be set for *Block (Element Classic)*, *Preheat*, and *Moves (Element* *Classic)*.

#### Block

You can apply a block to a cue, a cue part, to any channel (or group of channels), or parameter (or group of parameters) within a cue. Block is an editing function. It has no impact on how the data is played back.

> **Note:** *Block functions differently on Element Classic consoles. See Block (Element Classic) (on the facing page).*

##### At a Cue Level

A cue level block causes all tracked values in the cue to be treated as move instructions from an editing standpoint, which prohibits any data changes from tracking into the cue.

Parameters that are not included in the cue are not impacted by the block instruction.

Blocks do not protect a cue, channel or parameter from being modified by a range edit, nor are they protected from a trace instruction (see *Update Using Trace (on page 342)*). It is assumed that if you use the trace instruction, then you really want the initial value to change. A block will stop the trace from moving any further backwards through the cue list.

-   [Cue] [5] [Block] [Enter] - "B" is displayed in the flags field, indicating a cue level block. When this cue is recalled, all data that would otherwise appear as a tracked value, will be displayed in white. Any changes upstream in the cue list will not impact this blocked cue data.

-   [Cue] [6] {Intensity} [Block] [Enter] - "I" is displayed in the flags field, indicating a cue level intensity block. You could also use [Shift] & [Block] to put Intensity Block on the command line.

##### At a Channel / Parameter level

Blocks can also be applied to a channel or a channel parameter. This can be done in live or blind. When applied in live, the block instruction must be stored or updated to the appropriate cue.

-   [9] [Block] [Enter] - applies a block to channel 9. A red "B" appears near the channel in the live display, indicating a block has been applied but is not yet stored.

-   [Group] [5] {Color} [Block] [Enter] - applies a block to all of the color parameters for group 5.

When the block instruction has been stored or updated, any tracked values the block was applied to will be displayed in white.

Channel level blocks are indicated in the cue list by a "b" and auto-blocks are indicated in the cue list by a "[b]{.underline}", representing a partial block. To remove auto-blocks, see *Auto-Block Cleanup* *(on page 348)*.

#### Auto-Block

> **Note:** *Not available on Element Classic.*

Eos also supports an auto-block function. Auto-block can protect your cue data from unwanted changes. For example, in cue 5 you set channel 1 to 50%. It is stored as a move instruction. Then, you later go back to an earlier cue and set channel 1 to 50% and it tracks forward to cue 5. Channel 1 will be auto-blocked in cue 5. Even though it is now at the same value as the previous cue, the original concept of a move instruction is maintained.

Auto-blocks are displayed in white, with a white underscore.

#### Block (Element Classic)

Block flags prevent edited levels from tracking into a cue, and force a move instruction on any tracked value in that cue. For example, if channel 1 is at full in scene 1 and scene 2, and you want to make sure it stays at full in scene 2 when you edit scene 1, place a block flag on the cue at the top of scene 2. A block also forces a move instruction on playback (blackout cues typically get blocked to ensure that they fade any moving levels from the previous cue to zero.)

You can apply a block to a cue, a cue part, to any channel (or group of channels), or parameter (or group of parameters) within a cue.

> **Note:** *On other Eos Family consoles, the block command is split into block for editing and assert for playback. See Block (on the previous page) and Assert (on the next page).*

##### At a Cue Level

A cue level block causes all tracked values in the cue to be treated as move instructions for editing and playback purposes, which prohibits any data changes from tracking into the cue. Parameters that are not included in the cue are not impacted by the block instruction.

Blocks do not protect a cue, channel or parameter from being modified by a range edit, nor are they protected from a trace instruction (see *Update Using Trace (on page 342)*). It is assumed that if you use the trace instruction, then you really want the initial value to change. A block will stop the trace from moving any further backwards through the cue list.

Blocks that you have applied will display parameter data in white.

-   [Cue] [5] [Block] [Enter] - "B" is displayed in the flags field, indicating a cue level block. When this cue is recalled, all data that would otherwise appear as a tracked value, will be displayed in white. Any changes upstream in the cue list will not impact this blocked cue data.

##### At a Channel or Parameter Level

Blocks can also be applied to a channel or a channel parameter. This can be done in live or blind. When applied in live, the block instruction must be stored or updated to the appropriate cue.

-   [9] [Block] [Enter] - applies a block to channel 9. A red "B" appears near the channel in the live display, indicating a block has been applied but is not yet stored.

-   [Group] [5] {Color} [Block] [Enter] - applies a block to all of the color parameters for group 5.

-   [1][0] {Intensity} [Block] [Enter] - applies a block to the intensity of channel 10. You could also use [Shift] & [Block] to put Intensity Block on the command line.

-   [Cue] [n] {Intensity} (from the ML controls) [Block] [Enter] - blocks all the intensities in the cue, but not the NPs. I is displayed in the Block field.

##### Auto-Block

Element also supports an auto-block function. Auto-block can protect your cue data from unwanted changes. For example, in cue 5 you set channel 1 to 50%. It is stored as a move instruction. Then, you later go back to an earlier cue and set channel 1 to 50% and it tracks forward to cue 5. Channel 1 will be auto-blocked in cue 5. Even though it is now at the same value as the previous cue, the original concept of a move instruction is maintained.

When the block instruction has been recorded, updated, or stored while in blind, any tracked values the block was applied to will be displayed in white. Auto-blocks are displayed in white, with a white underscore.

Channel level blocks are indicated in the cue list by a "b" and auto-blocks are indicated in the cue list by a "[b]{.underline}", representing a partial block. To remove auto-blocks, see *Auto-Block Cleanup* *(on page 348)*.

#### Moves (Element Classic)

There are two types of moves, live and dark. A live move is a NPs move in a channel with an intensity that is zero in the previous cue, that moves above zero in the current cue. A dark move is a NPs move in a channel that is at an intensity of zero in the previous and current cue.

> In the *Playback Status Display (on page 107)* and *Cue List Index (on page 347)*, there is a MV column for displaying live and dark move flags. A live move will be indicated with a "L" and a dark move is indicated with a "D". A "+" is used to show that both types of moves are in that cue.

#### Assert

Assert is a way to make a tracked or blocked value act as a move instruction on playback. It is often used in a multiple cue list environments, or to assure that a transition happens in the desired time. See *Using Assert (on page 361)* on asserts in multiple cue lists and *Assert (Fader Control) (on page 386)* on using assert for playback.

Assert can be useful in a single cue list.

> Cue 10 is a blackout with a zero count. It is common practice to block blackout cues. Let's say though that some of the lights were fading to zero in cue 9. You hit [Go] for cue 10 before cue 9 is finished. The lights that were fading to zero in cue 9 will continue their downfade in the timing for cue 9 since cue 10 doesn't provide them with a new move instruction. If you assert cue 10, the lights will bump to black as expected.

#### AllFade

Any cue can have an allfade flag applied. An allfade sends the intensity for all channels not included in the cue to zero. Submasters, any captured channels and the contribution from any faders that are set to priority are unaffected, unless the cue executing the allfade is also set to priority. An allfade flag "*" is identified in the cue list index and the playback status display for the specified cue.

-   <Cue> [5] {Attributes} {AF/MF} [Enter] - sends intensity for all channels not included in the allfade cue to zero.

The allfade instruction is useful as a quick cleanup, to get back to a known state on stage, without having to worry about what channels need to be set to zero.

#### Mark

> **Note:** *This option is not available on Element 2 and Element Classic.*

The Mark flag is used to relay information about either automarks or reference marks. When using automarks, an "M" will display in the flags field for the specific cue that will execute an automark. A "D" is displayed when automark has been disabled for a cue or a cue part.

When using reference marks, an "M" will display in the flags field for any cue that will execute a referenced mark. An "R" displays when a cue is the source of a mark. See *About Mark (on* *page 284)*.

#### Preheat

Preheat can be used to warm filaments in the cue immediately preceding an intensity upfade from 0. Preheat values can be assigned to channels individually in patch (see *Patch > Attributes (on page 182)*).

Preheat is assigned on a cue (or cue part) basis. If assigned, any channel in that cue with a preheat value assigned in patch will fade to that intensity in the cue immediately preceding the cue with the preheat flag. Cues with a preheat flag will display an "P" in the preheat flag column (indicated by a "P" at the top of the column) in the PSD and Cue List Index.

When a channel is in a preheat state, a "Ph" is displayed in the intensity field of that channel. When a preheat is executed, the preheat value is established using the upfade time of the associated cue. It is possible to hold the [Data] key to see the actual preheat values.

### Cues & Triggers

Triggers can be used to tie actions such as macros, show control, or snapshots to cue playback. You can also trigger the playback of additional cues or cue lists, if available.

#### {Execute}

When used after selecting a cue on the command line, {Execute} will open a trigger display in the CIA.

*(figure omise)*{width="5.83323053368329in" height="2.0795833333333333in"}

Buttons for common targets are available on the left. These options are also available below as softkeys.

The table on the right lists all triggers associated with the selected cue, along with their reference labels. You can remove individual triggers using the delete icon on each line.

##### Syntax

A variety of command line syntax is available when working with triggers:

+-------------------------------------------------------------+----------------------------------------------------------+
| Action                                                      | Syntax                                                   |
+=============================================================+==========================================================+
| Add a trigger to a cue                                      | > [Cue] [#] {Execute} [+] {Target} [#] [Enter] |
+-------------------------------------------------------------+----------------------------------------------------------+
| Remove a trigger from a cue                                 | [Cue] [#] {Execute} [-] {Target} [#] [Enter]   |
+-------------------------------------------------------------+----------------------------------------------------------+
| Remove all triggers from a cue*                            | [Cue] [#] {Execute} [Enter]                        |
+-------------------------------------------------------------+----------------------------------------------------------+
| > Replace all triggers in a cue with the one specified*    | [Cue] [#] {Execute} {Target} [#] [Enter]         |
+-------------------------------------------------------------+----------------------------------------------------------+
| > Remove all instances of the specified target from a cue* | [Cue] [#] {Execute} {Target} [Enter]               |
+-------------------------------------------------------------+----------------------------------------------------------+
| ** Confirmation required*                                  |                                                          |
+-------------------------------------------------------------+----------------------------------------------------------+

Buttons for common targets are available on the left. These options are also available below as softkeys.

When cue list triggers are set, the system will automatically execute same numbered cues on the associated cue list. For example, assume that the last instruction above was applied to cue list 1, cue 1. When cue 1/1 is executed, any cues numbered "1" in cue list 2 will be executed accordingly. If there is not a cue 1 in that list, no action is taken. If there are cue numbers on secondary cue lists that are not in cue list 1, those cues are skipped and the subsequent cue taken as an "out-of-sequence" cue when triggered.

When cues are taken on the primary list out of sequence, only like-numbered cues on the secondary lists will be replayed. For example, if you go to cue 12 on the primary list, and there is a cue 12 on the secondary list, cue 12 on all lists is executed. However, if cue 12 does not exist in the secondary list, that list will be unaffected by the go to cue command. Out of sequence sync can be enabled to make sure secondary lists assume the same position in the show as they would on linear playback.

#### OOS Sync

> **Note:** *Not available on Element Classic.*

{OOS Sync} can be used to change that behavior per cue list.

When OOS Sync is enabled, any out of sequence cue fired from a cue list that is synced with another cue list will trigger the earliest cue that exists if the correct cue does not.

{OOS Sync} is disabled by default. When enabled, OOS Sync will display in the cue list index\'s external links column. {OOS Sync} should be enabled in the secondary lists, not on the list that contains the execute command.

> Cue list 1 is synced with cue list 2. Cue 1/3 is fired. Since cue 2/3 does not exist, cue 2/2 will fire instead. If OOS Sync was disabled, a cue in cue list 2 would only fire if it has the same cue number as cue list 1.

#### OSC Cue Receive & Send

##### OSC Cue Recieve String

Allows the user to specify a different incoming OSC string format for integration with other applications. Use %1 in the string format as cue number and %2 as the cue list number.

##### OSC Cue Send String

Allows the user to specify a different outgoing OSC string format than the standard Eos implicit string for integration with other applications. The following options can be used:

-   %1 - cue number

-   %2 - cue list number

-   %3 - cue whole number

-   %4 - cue point number

-   %5 - cue label

#### Go After Loop

{Go After Loop} will execute the next cue after a follow link/loop sequence has ended. By default, the loop will end with the last cue in the sequence. {Go After Loop} will use the follow time assigned to the last cue in the sequence.

-   [Cue] [5] {Execute} {Go After Loop} [Enter] - assigns the {Go After Loop} command to cue 5. Go After Loop will display in the Ext Links Column of the Cue List index and the PSD. After Cue 5 has completed all loops, it will execute the next cue.

### Modifying Cues Live

Recorded cues can be modified live. *Assigning Cue Attributes (on page 327)* (such as link, loop, label and so on) may be edited as well. The cue does not need to be active (played back) to change cue attributes. You may also change cue attributes for a range of cues if you wish.

[Recall From], [Copy To], and Move To may be used to create and edit cue data.

> See *Using [Recall From] (on page 367)*, *Using [Copy To] (on page 366)*, *Move To (on page 345)*.

#### Using [At] [Enter]

[At] [Enter] allows you to select any channel or parameter, or several of them, and remove their move instructions, allowing the value from the previous cue to be manually recalled.

[At] [Enter] is essentially a "recall from the previous cue" command.

> Cue 5 is active in Live.

-   [Group] [1] [Focus] [At] [Enter]

> This command lifts the current move instructions for Group 1 focus, and recalls the focus data for those lights from the immediately preceding cue. It is now manual, and can be stored or updated as required.

You may use [At] [Enter] to affect only certain channels or parameters by selecting them specifically:

-   [2] [At] [Enter] - this will remove the changes for channel 2 only.

-   [2] {Color} [At] [Enter] - this will remove only the color data changes for channel 2.

-   [2] [Thru] [5] [+] [9] [+] [1] [1] [Thru] [1] [5] [-] [1] [2] [-] {Zoom} [At] [Enter] - removes

> the changes for only the selected channels for all parameters except zoom.

#### Modifying Using Record

You may modify a cue by re-recording it entirely. After making changes to channels/ parameters:

-   [Record] [Enter] [Enter] - will replace any data in the active cue with the current stage settings.

-   [Record] [Cue] [x] [Enter] [Enter] - will replace the any data in cue "x" with the current stage values.

> Using selective storing will modify the existing cue without overwriting it. For more information, see *Selective Storing Cues in Live (on page 323)*

-   [1] [Record] [Cue] [2] [Enter] [Enter] - will only record the changes to channel 1.

> **Note:** *Using [Record] will store all parameters of all non-default channels onstage. This means that all other cue data and submaster data will be included in the record action. This is a common method when working with a single cue list. When working with multiple cue lists and/ or submasters, [Record Only] is a useful tool.*

#### Modifying Using Record Only

> **Note:** *[Record Only] is used in the examples below. Element Classic users will need to use [Record] [Record].*

Modifying existing cues using [Record Only] is considered a "selective store" function. As such, it adds or modifies only manual data to the target cue, but leaves any other data that was already in the cue intact and does not include playback values from other cue lists or submasters. [Record Only] is a good way to modify existing cues without including contributions from other playbacks in the cue. In that way, it is very similar to *[Update] (on the facing page)*.

All of the same commands used for Record may also be used for Record Only.

-   [Record Only] [Enter] [Enter]- adds the current manual data to the selected cue.

-   [Record Only] [Cue] [x] [Enter] [Enter] - adds the current manual data to cue "x".

### [Update]

Update is a powerful feature, and also very versatile. Using a combination of [Q Only], [Track], [Trace], and {Make Absolute}, the number of ways you can update specific information and manual data is virtually endless. Data can be updated to various record targets either at once, or individually.

#### Update Dialogue Box

When you press [Update], a dialogue box will open in the CIA. Update styles and modifiers for those styles will be divided in the Update Dialogue Box.

> **Note:** *Default Update Modes are set in Setup > User > Record Defaults. See Record Defaults (on page 220).*
>
> **Note:** *{By Type} is available as a softkey. See Updating By Type Presets (on page 312).*

##### Update Styles

-   {All} - this button will update the target cue and all references stored to that cue (nested and otherwise).

-   {Make Absolute} - this button will update the target cue and convert all levels to absolute values, thereby removing any references.

-   {Ref Only} - this button will only update the palettes or presets used in the cue, but will not update the cue itself. If a manual reference was used before using {Ref Only}, the last manual reference will be updated.

##### Update Modifiers

-   {Last Ref} - updates using the last reference that was applied via the command line, rather than the original reference for the values present in the cue.

-   {Break Nested} - updates the target cue and any presets used, but breaks the reference to any palettes nested in a preset. For example, if cue 1 channel 1 references preset 3, and preset 3 was built using color palette 5. When updated with this option, preset 3 would be updated, color palette 5 would not, and the reference to CP5 would be broken in preset 3.

-   {Reset Update} - clears any commands after the [Update] command to quickly undo pending changes before [Enter] is pressed.

*(figure omise)*{width="4.986045494313211in" height="2.2333333333333334in"}

The dialogue box also provides you with a listing (by record target) of what channels/parameters will be impacted by the update instruction. If the channel contains a reference in the cue, it is indicated. Channels that have been manually added to the stage output, but are not overrides of an active cue will update to the selected cue list.

Once you have made a selection from the available options, press [Enter] and the target will be updated.

Targets may be deselected from the dialogue box, excluding them from the update without specifying the target number, for example, [Update] [Color Palette] [Enter]. Selecting a line by clicking or pressing it can also be used to deselect a target. Element Classic users will need to use {Color Palette}.

On Eos Family devices that do not have a [Snapshot] hardkey, there is a {Snapshot} softkey available in the Update display.

#### Updating to References

When a cue is active, it is possible that various record targets (palettes or presets) will be played back within that cue. As changes are made to the data in that cue, as well as to the individual palettes or presets, updating both the cue and references within that cue is simple. When you have overridden a reference in a cue, the data is displayed in red with a red "R" in superscript next to the channel's intensity.

By default, Eos updates any referenced data that was included in the cue.

> Cue 5 is recalled Live. It contains references to color palette 1 and preset 2. You make changes to channels included in these record targets. To update both the cue and the palettes/presets, press:

-   [Update] [Enter]

> This will automatically take the manual changes and update them to color palette 1 and preset 2. Therefore cue 5 now references these new values, and the modifications to CP1 and PR2 have propagated through all of the show data.
>
> If you had made changes to other channels that were not included in the palettes/presets used in cue 5, those values would also be updated to the cue as absolute data.

#### Updating Without References (Make Absolute)

If you want to record your changes to the cue without updating the references, you may use

{Make Absolute} to break the association to the reference. The {Make Absolute} command can be applied to the channels/parameters required before the update instruction, or they can be applied during the update.

-   [Update] {Make Absolute} [Enter] - this will break the references for any parameters which have been changed and update the cue with the changes. The referenced target will no longer be displayed in the channels which were made absolute. All of the data updated in cue 5 will now be shown as absolute data.

-   [5] [Thru] [9] [Update] {Make Absolute} [Enter] - this will break only the references for channels 5-9 and record their manual values to the cue. Other manual values will not be included in this update.

You may also use [Record Only] to break references.

> Cue 5 is active and onstage. Channels 5 through 20 are currently referencing preset 1. You make changes to channels 5 through 9. The data for these changes is now manual. Press:

-   [Record Only] [Enter] [Enter]

> If there were other changes on stage, you could have used:

-   [5] [Thru] [9] [Record Only] [Enter] [Enter]

> Only the manual data will be recorded as an update to cue 5. The reference to preset 1 for channels 5 through 9 is broken and now the cue will display the absolute data rather than the reference indicator.

#### Update Using Cue Only/Track

The [Q Only/Track] key can be used as an applied exception to the cue only/track system setting. Therefore if the system is set to Cue Only, the key behaves as a [Track] command. Alternatively, if the system is set to Track, the key behaves as a [Q Only] button.

> For a more detailed summary of Cue Only and Tracking modes, see *Tracking vs. Cue Only (on page 7)*.

[Q Only/Track] can be used in conjunction with record or update functions. Following are some examples of use:

> **Note:** *In the following examples, the commands [Q Only] and [Track] indicate the same key hit of [Q Only/Track] - a single button on the keypad. The system setting determines the actual context of the button. For clarity, only the contextual function of the button is used in the examples.*

##### With system set to Track

-   [Record] <Cue> [5] [Q Only] [Enter] [Enter] - rerecords cue 5. This will make the changes to cue 5 only. The changes will not track forward through the list.

-   [-] [Color] [Record] <Cue> [5] [Q Only] [Enter] [Enter] - as above, but changes to color parameters will not be included in the record and all data that was included will not track forward. Color data in the cue remains unchanged.

-   [Update] <Cue> [5] [Q Only] [Enter] - updates cue 5 with only those manual parameters that were receiving their instructions from that cue. The changes will not track forward in the list. Note that if the data being updated were referenced, this action updates the referenced target as well.

-   [-] [5] [Record] <Cue> [7] [Q Only] [Enter] [Enter] - rerecords the specified cue, except the contributions from channel 5. The changes will not track forward in the list.

##### With system set to Cue Only

-   [Record] <Cue> [5] [Track] [Enter] [Enter] - rerecords cue 5. This will force the changes to track forward in the list until the next move instruction or block.

-   [-] [5] [Color] [Record] <Cue> [7] [Track] [Enter] [Enter] - rerecords the specified cue, except the color data from channel 5. The recorded changes will track forward in the list.

-   [Update] <Cue> [3] [Thru] [7] [Track] [Enter] - updates cues 3 through 7. Range updates are subject to the normal rules of track/cue only in determining impact on subsequent cues.

#### Update Using Trace

> **Note:** *[Trace] is used in the examples below. Ion Classic and Element Classic users will need to use {Trace}.*

[Trace] works just as Track does, except it allows changes to be tracked backwards through the cue list, until it sees a move instruction. A trace will track into, but not beyond, a blocked instruction.

> For a more detailed summary of Trace, see *Using Trace (on page 8)*

Following are some examples:

-   [Update] <Cue> [5] [Trace] [Enter] - updates cue 5, and tracks changes backward until a move instruction is encountered. If the system is in tracking mode, the change will track forward in the cue list until the next move instruction or block. If in cue only mode, this has no impact on subsequent cues.

-   [Update] [Trace] [Q Only / Track] [Enter] - updates the selected cue and tracks changes backward until a move instruction is encountered. If the system is in tracking mode, the change is prohibited from tracking forward in the list. If in cue only mode, the change is allowed to track forward.

> When a channel that is inactive (at zero or null) in the cue list receives an active level, if update trace is used, that channel will not trace the current setting into previous cues. To force that channel\'s new value to go backward in the cue list, [Trace] [Trace] can be entered.

#### Updating the Current Cue

The current cue is updated by simply pressing [Update] [Enter].

When only one cue list is active, this update will include any changes to all channels.

#### Updating a Source Cue

> **Note:** *[Trace] is used in the examples below. Ion Classic and Element Classic users will need to use {Trace}.*

To update the source of a level in the current cue (therefore, a move instruction in a prior cue) you must specify a trace for the desired channel(s). See *Update Using Trace (above)*

-   [5] [Update] [Trace] [Enter] - Updates any manual changes for channel 5 in the current cue. Any tracked values for channel 5 are traced back to the source of the value (the original move instruction) and changed to the new value. The value for traced changes in the current cue will be magenta indicating it is a tracked value.

-   [Trace] [Trace] - If a channel was inactive in the cue (either because it had not previously been used in the cue list, or it was a tracked zero) and is set to a new level, by default the new level will not track back. You can force it by pressing [Trace] twice.

#### Updating a Non-Active Cue

It is possible to use the same update commands as current (*Updating the Current Cue (above)*) and source cues (*Updating a Source Cue (above)*) to update inactive cues (cues not live onstage). In these situations, if the updated cue is not the source of a channel's live value, manual data will remain manual. If the updated cue is the source of the current value, the values will change to magenta (indicating tracked) when the update is completed.

#### Update [Thru]

Using [Update] [Thru] allows you to update from a current cue to a destination cue without first entering the current cue\'s number.

> If you are currently in cue 5 and you want to update through cue 10, you would use the following syntax:

-   [Update] [Thru] <Cue> [10] <CueOnly/Track> [Enter]

> **Update [+]**

[+] can be used to specify a range of cues for updating. [+] can also be used with [Record] and [Record Only].

> To update only cues 5, 10, and 15:

-   [Update] <Cue> [5] [+] <Cue> [1][0] [+] <Cue> [1][5]

<CueOnly/Track> [Enter]

To update the current cue and cue 7:

-   [Update] [+] <Cue>[7] <CueOnly/Track> [Enter]

> **Note:** *If no cue number is entered before the [+], the current active cue will be used.*

#### Update Intensity Cue Only

This option allows you to update intensity cues only, and all other parameters according to your console\'s current tracking settings in Setup > User > *Record Defaults (on page 220)* or manual use of CueOnly / Track.

### Recording and Editing Cues from Blind

When you press blind, the selected cue will be displayed. You can make changes to cues in the blind display using either the summary, table, or spreadsheet views.

> **CAUTION:** *Edits in blind take effect immediately. **[Record]** or **[Update]** commands are not required in blind.*
>
> **Note:** *To force blind to the selected cue, press [Blind] [Blind].*

If changes are made in the blind display to an active cue, these changes will not impact the current stage state. To make blind changes active you can press [Assert] & {Load} button for the fader associated with the cue, or you can use [Go To Cue] [Enter].

Move instructions can be removed from a cue by selecting the channel and pressing [At] [Enter]. This allows all values from the previous cue to track into the current cue. You can also use this command for specific parameters as well.

> Suppose you are in blind cue 5 and you make changes to channels 1 through 5:

-   [1] [Thru] [5] [At] [5] <0> {Iris} [3] [5] [Enter]

> Intensity goes to 50% and Iris to 35%. You decide to remove the Iris instruction:

-   {Iris} [At] [Enter]

> The Iris value from the previous cue tracks in. Then you remove the intensity change as well:

-   {Intensity} [At] [Enter]

> All values from the previous cue track in.
>
> Instead of using multiple commands, you can, in one command, return the channels to their values from the previous cue:

-   [1] [Thru] [5] [At] [Enter]

The impact of blind edits on subsequent cues is determined by the default setting of Track/ Cue Only mode. In track mode any changes will track forward until the next move instruction, unless [Q Only] is pressed. In cue only mode any changes will apply only to the selected cue. If you want values to track forward, the [Track] button will allow it. The track/cue only instruction must be applied when a value is entered. [Trace] can also be used to have changes trace back to the initial move instruction. Such as:

-   [1] [Thru] [5] [At] [5] <0> [Q Only/Track] [Enter]

-   {Intensity} [At] [Q Only/Track] [Enter]

-   [1] [Thru] [5] [At] [5] <0> [Q Only/Track] [Trace] [Enter]

#### To Live From Blind

From blind, a softkey {Live} is posted when you press [Recall From] or [Copy To] to allow you to copy to or recall information from live. The following examples only work with the {Live} softkey, not the [Live] hard key.

-   [1] [Recall From] {Live} [Enter]

-   [2] [Copy To] {Live} [Enter]

#### Editing From Summary or Table Views

Use the [Format] key to cycle through the available views.

Summary view allows you to see the greatest number of channels at once, though parameter data is somewhat truncated. Channels with focus, color, or beam data are indicated with + symbols beneath the level data. This view is useful for viewing lots of channel data at once or for editing primarily intensity values.

Table view grants you greater visibility of parameter data and a reduced number of visible channels. This view displays channels along the y axis and parameters along the x axis.

Parameter categories are always visible (I, F, C, and B).

You can also view specific parameters by pressing and holding the [Params] button and then pressing the category softkey(s) for the parameters you wish to view. Ion Classic and Element Classic users will need to use [Data]. This will expand the category to show any parameters used in the show. You can also deselect the parameters you do not wish to see. This is remembered the next time you go to table view.

Both summary and table views allow you to make changes to channels/parameters.

#### Editing From the Blind Spreadsheet

> The Blind spreadsheet is another useful blind view of cue data. While in Blind, press [Format] to access the spreadsheet. See *Spreadsheet (Blind Only) (on page 101)*.

In spreadsheet view, cues are listed on the y axis and channels/ parameters are displayed on the x axis. This view is useful for showing a limited number of channels over a span of numerous cues. This is the only view where channel data of multiple cues can be viewed at once. This makes spreadsheet view useful for viewing overall trends in channel and parameter data.

Pressing [Params] & {parameter tiles} will expand or collapse information shown. Ion Classic and Element Classic users will need to use [Data] to access the parameter tiles.

Editing cue ranges is possible in spreadsheet view. To select all of the cues, you can press [Cue] [Home] [Thru] [Enter].

##### Replace With

{Replace With} is used to select channels that have certain specified values and then provide new instructions for those values.

> Select a range of cues:

-   [Cue] [1] [Thru] [9] [Enter]

> Select a range of channels that are used throughout these cues and enter a change instruction:

-   [1] [Thru] [7] <At> [Color Palette] [5] {Replace With} <Color Palette>

> [3] [Enter]
>
> This instruction finds all instances of channels 1 through 7 in cues 1 through 9 that are in color palette 5 and replace Color Palette 5 with Color Palette 3. Be aware of the track/ cue only settings when using this command.
>
> **Note:** *[Cue] [Home] [Thru] [Enter] will select all stored cues within the selected cue list. [Thru] [Enter] can be used with all record targets. See Home (on page 259).*

The range of possibilities of potential {Replace With} commands is virtually endless and can be applied to single cues or channels, ranges of cues or channels, parameters of any type, or timing data.

##### Move To

Move To is used to move cues from one location in a cue list to another location in the same or a different cue list. To put Move To on the command line, press [Copy To] twice.

> **Note:** *On Element 2 and Element Classic, Move To is used to move cues from one location in a cue list to another location in the list.*

When cues are moved, values that were tracks or move instructions and now match the previous cue will be auto-blocked by the system. The impact on subsequent cues is based on track/cue only settings as described above. Below is an example of Move To:

-   [Cue] [2] Move To <Cue> [9] [Enter] - the contents of cue 2 moves to cue 9. Cue 2 is deleted. If cue 9 already existed, a confirmation will be required (unless confirmations have been disabled in setup). Any contents of cue 9 will be replaced entirely.

In the above example, if running in cue only mode, any tracked values in cue 2 become blocks (see *Block (on page 332)*) or moves in cue 9, as well as any move instructions which now match the previous cue. Cues after cue 9 are affected based on the default setting of track/ cue only. Any values in the cue after cue 2 that tracked from moves in cue 2 are changed to move instructions.

Ranges of cues can be moved as well. You can also move cues to other cue lists. In either of these situations if any cue is to be overwritten, a confirmation is required.

> See *Using Move To (on page 367)*.

#### Using Encoders in Blind

If your console has encoders, they are disabled by default in blind. Press an [encoder paging key] prior to moving the encoders, and they will function while you remain in Blind.

When a cue is specified, you can select channels and alter parameters using the encoders. [Q Only/Track] can be placed on the command line after a selection to determine how these changes will impact subsequent cues.

### Deleting Cues

Cues, ranges of cues, or lists of cues (if available) can be deleted. When deleting cues, the track/ cue only setting of the console will determine how subsequent cues are affected. The [Q Only /Track] button can be used to modify the default behavior as needed.

Some examples of cue deletion are:

-   [Delete] <Cue> [5] [Enter] [Enter] - deletes cue 5. Subsequent cues in the list are affected depending on the console default setting.

-   [Delete] <Cue> [6] [Q Only/Track] [Enter] [Enter] - deletes cue 6, making exception to the default setting.

-   [Delete] <Cue> [7] [Part] [1] [Enter] [Enter] - deletes part 1 of cue 7. Deleting a part does not delete any move instructions. Those will be moved to the main cue. See *Deleting Parts from Multipart Cues (on page 397)*

-   [Group] [1] [Delete] <Cue> [2] [Enter] - deletes any channels in group 1 from cue 2. Cue 2 remains in the cue list and any channels not in group 1 are unaffected.

-   [Delete] <Cue> [2] [Thru] [8] [Q Only/Track] [Enter] [Enter] - deletes cues 2 through 8, making exception to the default setting.

#### Deleting In Track Mode

When the console is in track mode, deleting a cue also removes any move instructions provided by the cue. For example, assume you have stored cues 1 through 10 and cue 5 contains move instructions for channels 1 through 5. If cue 5 is deleted, the move instructions are deleted as well and the values from cue 4 will track directly into cue 6 and beyond.

In this instance, if you used the [Q Only] button in the delete instruction, cue 5 would be deleted, but the tracked values in cue 6 that originated in cue 5 would remain and be converted to move instructions.

#### Deleting In Cue Only Mode

When the console is in cue only mode, any subsequent tracked values are not eliminated, but are converted to move instructions instead.

In the example above, deleting cue 5 (in cue only mode) would result in any tracked values in cue 6, that originated in cue 5, being converted to move instructions.

If you apply the [Track] button to the delete instruction, the move instructions from cue 5 are deleted and the values from cue 4 would then track into cue 6 and beyond.

### Cue List Index

The cue list index is a Blind display list which shows the cue list you are working with, the cue status, cue list properties, and, if available, any other stored cue lists, and what (if any) faders the lists are loaded onto.

#### Opening the Cue List Index

You can access the cue list index by pressing [Cue] [Cue],[Tab] [1][6], or you can navigate within the browser to Record Target Lists > Cue List Index and press [Select].

Cue list properties determine how the cue list will interact. Assigned properties will display at the top of the cue list as well as any currently active show control triggers.

The top half of the cue list index displays all stored cues, including cue list properties, for the selected cue list. The bottom half of the cue list index displays one or more stored cue lists and their properties. The selected cue list is highlighted.

Using the mouse, you can move the barrier between the stored cue display (top) and the stored list display (bottom). Hover the mouse arrow over the list boundary until it changes to the move boundary icon. Then click and drag the boundary up or down to the desired height.

##### Command Line Behavior for Cue List Index

The command line while in the Cue List Index defaults to cue list selection. The softkeys that display will default to cue list control.

[Next] and [Last] will select the next or last cue list if no cue list or a cue list but no cue is on the command line.

When a specific cue is selected, [Next] and [Last] will move through the cues in that same list, and the softkeys will change to be for a single cue control.

#### Partitions on Cue Lists

A partition (*About Partitioned Control (on page 562)*) may be assigned to a cue list. If a partition has already been applied to a cue list, any channels not in the cue list\'s partition will not be included in cues when they are stored or replayed.

Any data for a cue list that already existed before a partition is applied, will be maintained, including data for channels not included in the partition. If data existed before the partition was assigned, in blind, channels that are not in the partition will display without a channel graphic, any levels will be in gray, and a small superscript N will display with it.

Assigned partitions will display at the top of the cue list index and in the PSD. To assign a partition to a cue list:

-   [Cue] [n] [/] {Partition} [n] [Enter] To remove a partition from a cue list:

-   [Cue] [n] [/] {Partition} [Enter]

#### Solo Mode

> **Note:** *This option is not available on Element 2 and Element Classic.*

The {Solo Mode} softkey is useful in multiple programmer situations. {Solo Mode} is used to pull a cue list out for editing purposes after it has been synced with other cuelists.

> Cue List 1 is being used by one programmer and Cue List 2 was programmed by a second programmer. For the run of the show, the lists are synced so they run together. But if changes need to be made to Cue List 2 and not be affected by the playback of Cue List 1, {Solo Mode} can be used.

-   [Cue] [2] [/] {Solo Mode} [Enter] - places Cue List 2 into solo mode.

{Solo Mode} is a toggle state. So if Cue List 2 is already in solo mode, and [Cue] [2] [/] {Solo Mode} [Enter] is used again, that list will no longer be in solo mode.

#### Auto-Block Cleanup

{Autoblock Clean} is used to remove all auto-blocks from a single cue, cue range or entire cue list. {Autoblock Clean} is a softkey that will be posted when a cue list and / or cue number are on the command line in the Cue List Index, Live, and Blind. A range of cues or a cue list can be specified with this command. For more information about auto-blocks, see *Auto-Block (on page 333)*

-   [Cue] [1] [/] {Autoblock Clean} [Enter] - clears all auto-blocks from cue list 1. Only blocks displayed with the white underscore are removed. If the [Block] key was previously used, this command will not unblock it.

-   [Cue][1] [/] [1][0] [Thru] [1][0][0] {Autoblock Clean} [Enter] - clears the auto-blocks just from cues 10 through 100 of cuelist 1.

#### Edit

The {Edit} softkey opens a blind channel view of the selected cue and changes focus from the cue list index. You can change the blind display to spreadsheet or table view by pressing the [Format] key. You can edit any of the cue attributes for the cue selected in the index, but the cue contents must be edited in the blind display. See *Recording and Editing Cues from Blind (on page 343)*.

#### Cue List Index Configuration

The Cue List Index has a configuration menu, which is accessed by first selecting the Cue List Index tab and then double clicking on the tab to open the menu. With the Cue List Index selected, you can also select the gear icon, which is located by the tabs, to open the configuration menu.

> *(figure omise)*{width="3.958499562554681in" height="2.625in"}

The following options are available in this configuration menu:

-   Display Cue Parts - displays the individual parts of a part cue. When not enabled, the number of parts for that cue will display as a superscript number beside the cue\'s number.

-   Display Cue Links - displays the *Link / Loop* information.

-   Display Scenes - displays cue *Scenes*

-   Display PSD Time Countdown - displays the cue category times countdown in the PSD as a cue is fading.

-   Display Cues - displays the top half of the cue list index, which shows all the stored cues.

    -   Not available on Element 2 or Element Classic

##### Reorder Columns

Reorder columns allows you choose what data displays in the top and bottom halves of the Cue List Index and what order it displays in. To make changes to the top half, select {Cues}. To make changes to the bottom half, select {Cue List}.

By default, all columns except notes will be displayed. The arrow keys on the right can be used to move columns around. Columns with multiple options are moved in groups. To select a column header to move, click or tap the name. The check boxes suppress or enable. When an item is enabled to display, a check mark will be in the corresponding box.

##### Default

> The Cue List Index takes its default settings from the Playback Status Display. The default is identified with parentheses. See *Playback Status Display Configuration (on page 112)*.

-   Reset to Default - returns the settings to the default state that you created.

-   Reset to Eos Default - returns all settings to the Eos defaults.

#### Cue List Properties

> **Note:** *The examples below mention multiple cue lists and mapping them to faders. Element 2 and Element Classic consoles have a single cue list which can only be loaded to the main fader pair.*

When the cue list index is open, the cue list properties dialogue box will display in the CIA. The cue list properties determine how the cue list will interact.

> *(figure omise)*{width="4.953845144356955in" height="1.3416666666666666in"}

Cue list properties include:

-   Master type (Proportional, Manual Master, or Intensity Master)

-   Intensity HTP or LTP setting (default is LTP)

-   Assert

    -   Not available on Element Classic

-   Priority

-   Background

-   Background Priority

-   Phantom

-   Back from 1st

-   Go from Last

-   Stomp

-   Exclude

-   Channel Filters

-   Parameter Filters

A cue list can be mapped to any fader via the fader configuration display or by using [Load] (see *Selected Cue*). If a fader has been configured for default mapping ( see *Fader Configuration (on page 129)*), the fader will receive its configuration from the Cue List Index. Changes made to a cue list in the cue list index will be shared with any default mapping faders loaded with that cue list. If changes are made to a fader set to default mapping in the fader configuration display, those changes will also happen in the Cue List Index. If set to Local, any changes made in the fader configuration display will impact only that instance of the content.

##### Master

When a fader is a ssigned as a master, its behavior as a Proportional Master, Manual Master or Intensity Master (I-Master) is drawn from this setting.

-   Proportional faders, when the slider is set to zero prior to the execution of a cue, will withhold playback of intensity data until the fader is raised. Intensity data will then be played back proportionally according to the level of the fader. Once the fader reaches full, the cue is considered complete and the cue is released from the manual fader. If the fader is at any value other than zero when the cue is executed, intensity values will play back normally. If the slider is returned toward zero, intensity in the cue will fade to the previous level.

-   Intensity Masters will master the intensity level for cues during playback. Therefore, intensity masters set below 100% will proportionally limit playback of intensity data relative to the level that the fader is set. All non-intensity parameters are unaffected by the fader. Once the fader has reached full, control of intensity is retained. If the fader is moved toward zero, intensity will proportionally fade toward zero (not the previous state as per proportional faders).

-   In Manual Master mode, cues are triggered manually by faders without using the [Go] button. With a cue list on a fader set to manual master, a cue will fire in manual time when the fader is moved from 0% or from Full. Timing is scaled. So, if color has a 5 count delay, and the duration of the cue is 10, the color transition will not begin until the faders manually reach 50%. Follow and hang times will be ignored when firing a cue with a manual master fader.

##### HTP

Intensity playback behavior can be set to HTP (highest takes precedence) or LTP (latest takes precedence). For cues, it defaults to LTP.

###### HTP & LTP on Element Classic

The {HTP/LTP} softkey is a toggle state between LTP (latest takes precedence) and HTP (highest takes precedence). For more information on HTP/LTP see *HTP vs. LTP (on page 10)*.

All parameters other than intensity are LTP.

Intensity, by default, is also LTP. The cue list can be set with an HTP intensity override. When the cue list is set to HTP, intensity values provided will override the LTP value (of which there can be only one), provided the HTP instruction is higher than the LTP value. When a cue from an HTP cue list is executed, the console determines if the intensity value when the cue is complete will be higher than the current setting. If so, the intensity will begin to fade from its current value to the required value in the incoming cue using the cue\'s upfade time.

> **Note:** *This behavior is relevant only to cues. If a submaster is going to provide a higher level, Element Classic will wait until the value is matched before assuming control of the intensity.*

The following example illustrates the use of the {HTP/LTP} softkey in the cue list index:

-   [Cue] [1] [/] {LTP/HTP} [Enter] - toggles the selected cue list between HTP/LTP behavior.

##### Assert

> **Note:** *Not available on Element Classic.*

Assert can be turned on or off at the fader level. This property sets the entire cue list to be asserted on playback (even track instructions are replayed).

##### Priority

> **Note:** *Priority was previously called Independent.*

Priority is used to protect values from being affected by submasters or playback faders that have a lower priority level. They will, however, still be impacted by manual control, grandmaster, blackout, park instructions, or other playback faders and submasters at the same or higher priority.

There are 10 levels of Priority that cue lists can have. 1 is the lowest level and 10 is the highest. The default priority level is 4.

-   [Cue] [1] [/] {Priority} [5] [Enter] - sets the priority of the cue list to 5.

##### Background

Background can be enabled or disabled at the fader level. When enabled, the content of the cue list will act as a background or previous state for other cues and submasters. When a cue list has its background state disabled, a "D" will display in the Cue List Index background column.

###### Background on Element Classic

The {Background} softkey is a toggle state for enabling and disabling the background state of a cue list. When a cue list has its background state disabled, "Background Disabled" will display at the top of the cue list.

###### Background Priority

Background can have a priority assigned to it.

In previous software releases, when content was released, it always returned to the last fader that owned it. Background priority releases to the highest priority content that previously had ownership, provided that content has not be turned off or released.

There are 10 levels of background priority. 1 is the lowest level and 10 is the highest. The default background priority level is 4.

##### Phantom

When a cue list is set to Phantom, pressing [Go] will not change the selected cue on the command line, or an unlocked playback status display.

##### Back From First

Back From First controls the behavior that happens when you press the [Back] button while in the first cue.

The following are Back From First options:

-   Do Nothing - keeps the first cue active

-   Cue Out - default setting. Only fades out channels in that cue list. Other channels will remain. Intensity and non-intensity parameters will be homed. This setting uses the Back time for fading.

-   Wrap - puts the last cue in the list in pending, and fires said cue

-   Restore Background - any background cue, submaster, and effect levels are restored following background priority. Manual levels will not be restored. This setting uses the Release time set in Setup. See *Manual Control (on page 221)*.

##### Go From Last

Go From Last controls the behavior that happens when you press the [Go] button while in the last cue.

The following are Go From Last options:

-   Do Nothing (Default Setting) - keeps the last cue in the list active.

-   Cue Out - only fades out channels in that cue list. Other channels will remain. Intensity levels will go out. Non-intensity parameters will remain. This setting uses the Go to Cue timing for fading.

-   Wrap - puts the first cue into pending, and fires it.

-   Restore Background - any background cue, submaster, and effect levels are restore following background priority. Manual levels will not be restored. This setting uses the Release time. The pending cue will be set to the first cue in the list. If there is no background state, the non-intensity parameters will not fade.

##### Stomp Mode

Stomp refers to when all the content owned by a cue is now being controlled by other targets. The cue is being removed from the background, and once that happens, it would not be eligible to fade back. You can assign behavior that will happen when a cue is stomped.

The following are Stomp Mode options:

-   Off When Stomped - puts the content into an off state, the same behavior encountered when pressing [Off] + [Load].

-   Unload When Stomped - unloads the fader.

-   Nothing When Stomped (Default Setting) - nothing happens.

-   Release When Stomped - resets a cue list to the top of the list.

##### Exclusions

Those exclusions include:

-   Exclude From Record - output is not recorded into any other record target.

-   Exclude From Grandmaster - content cannot be mastered by a grandmaster.

-   Exclude From Inhibitive Sub - content cannot be mastered by an inhibitive submaster

-   Exclude From Solo - content will ignore solo button mode. See *Fader and Button Configuration (below)* on solo.

##### Channel and Parameter Filters

Channel and Parameter Filters can be used to allow only specified data to be played back. These are playback filters, and do not impact how data is recorded.

For cue lists, channel and parameter filters can be set in the following areas:

-   Cue List Index using the {Properties} softkey

-   In Fader Configuration (Tab 36)

-   In Live using the {Properties} softkey

Tap or click on {Chan Filter} to assign channels or groups. Tap or click on {Param Filter} to open a list of available parameters that you can filter.

> **Note:** *Filters will travel with their assigned cue lists wherever they are mapped.*

When a filter has been applied, an indicator will display in the fader ribbon. C will display for channel filter, and F is for parameter filter.

Press the red [X] to clear the channel or parameter filters listed.

#### Fader and Button Configuration

Click or tap on the virtual buttons or fader to see a list of available configuration options.

> *(figure omise)*{width="0.7537314085739283in" height="1.8791655730533683in"}

##### Button Options

The following options are available for playback buttons:

-   Go - executes the cue currently in the pending file of the associated fader.

-   Stop Back - instantly stops all fader activity. Pressing twice will fade to the previous cue on that fader.

-   Assert - can be used to re-run the active cue on that fader, to regain control of all cue contents, to apply a newly set higher priority state to the associated fader, or make any changes in Blind to an active cue on stage.

    -   Not available on Element Classic

-   Group Select - selects the channels stored in the cue.

-   Freeze - halts all effect activity on the fader. Press Freeze again to resume effect activity.

-   Off - removes the content and if the fader is set to Master, the fader will remain where it currently is.

-   Release - removes the content and if the fader is set to Master, the fader will reset to 0.

-   Start Stop Effect - starts the effects while ignoring dwell times. Will stop effects if any are running.

-   Button Disabled - no action is assigned to the button.

-   Solo - plays back the content and suppresses any intensity values not provided by the associated content while the solo button is held down. When the button is released, intensity values are restored. Priority and HTP are ignored. Shielded, park and pixel mapping outputs are not affected by the solo button. This is unrelated to *Solo Mode*.

-   Back - fades to the previous cue.

##### Fader Options

The following options are available for a playback fader:

-   Master - fader will be a proportional master, a manual master, or an intensity master, depending on the cue list property.

-   Effect Rate - fader centers to home. It controls the rate of any running effects (same behavior as using rate via the Effect Status Display). The adjusted setting from this control cannot be stored.

-   Effect Size - similar to Effect Rate but for effect size.

-   Rate Master - homes to center. It adjusts the cue rate, just like rate and load.

-   Down Fade - same as the default behavior of the master option.

-   Fader Disabled - no action is assigned to the fader.

-   Master Only - fader is used to set a level for content to fade to. The slider can be used to live adjust levels when the fader has been activated via the bump button. See *Master Only (on page 134)*.

-   Effect Master - masters the entry/exit mode of the effects (size, rate or both).

-   Levels Only - masters the levels without mastering the effect.

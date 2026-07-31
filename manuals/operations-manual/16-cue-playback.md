# Eos Family User Manual v3.2.0 — Chapitre 16 : Cue Playback

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 16
## Cue Playback
### About Cue Playback

All Eos Family consoles have a single master fader pair, along with a varying number of motorized or non-motorized faders with multiple pages for configurable cue lists, submasters, grandmasters, IFCB palette and preset lists, or individual instances.

The master playback fader pair is located to the right of the motorized fader array, near the control keypad. The master is a split crossfader pair. The left fader controls the intensity upfade, while the right fader controls all intensity downfade actions. The two buttons beneath the master fader pair are [Go] and [Stop/ Back]. The [Load] button is located directly above the fader pair. You cannot page the master fader as it is permanently paired and always available for use.

You can define how each of the faders will function. There is no default setting for faders, which allows you the freedom to define each fader\'s function in *Fader Configuration (on page 129)* or you can configure them while programming, as the contents of those targets are stored.

The two buttons beneath the master fader pair are [Go] and [Stop/ Back]. The [Load] button and playback display are located just above the faders.

> **Note:** *On some consoles, the [Load] button for the master playback fader pair is actually labeled as [Master].*

You can page the motorized faders using the [Fader Page] button alone, combined with the numeric keypad, or with the wheel directly below the [Fader Page] button. As pages are changed, the faders will reset to the last position they were in on the associated page. Also, each individual fader is provided with a [Load], [Go], and a [Stop/Back] button for operation and playback. These buttons behave differently when the fader is a submaster or grandmaster, and can be changed in the fader configuration display.

#### Cue Playback on Element 2 and Element Classic

The single cue list on Element 2 and Element Classic consoles cannot be assigned to a fader. It can only be loaded to the master playback fader pair.

#### Cue Playback on Ion Classic

Cues may be played back using the master playback fader pair or by using a playback fader. While any cue list can be loaded to these faders, the first cue list you record to will automatically load to the master fader pair.

> To use playback faders, you can either use a fader wing or virtual faders. See *Fader Configuration (on page 129)* and *Virtual Fader Module (on page 136)*.

#### Fader Display and Ribbon

> **Note:** *On Element 2 and Element Classic, this information is displayed in the fader status display. See Indicators in the Element 2 & Element Classic Fader Status Display (on page 131).*

The fader display is located on the bottom of the PSD, and the fader ribbon is located directly above the faders. Both areas provide information about each fader including the fader designation (S = submaster with the designation of the submaster number, L = playback with

designation of the cue list and cue number that is loaded, GM = grandmaster, PR = preset with designation of the preset number, and IP, FP, BP, CP = palettes with designation of the palette number).

Each area uses the fader color coding that is used in the fader configuration tools.

Grandmasters and inhibitive submasters are in red, additive submasters are yellow, playback faders display in green, and presets and palettes are orange.

### Selected Cue

When in Live or Blind, if you press [Live] or [Blind] respectively, the last executed cue will be selected and appear on the command line.

When working in Live, the selected cue is always the last cue you recorded, edited, updated or played back. When entering Blind for cues, the selected cue will be selected and displayed.

Changing the selected cue in Blind will cause the playback status display to change as well, unless {Preserve Blind Cue} has been enabled in Setup > *User > Displays (on page 223)*, which will not synchronize the Blind display to the currently selected cue but rather shows the last cue selected in Blind. When you return to Live, the selected cue is synchronized to the currently active cue.

*(figure omise)*{width="4.58622375328084in" height="0.6296872265966754in"}

The attributes of the selected cue (such as timing, attributes, label and external links) are shown at the bottom of the Live / Blind display. For more information, see *Assigning Cue Attributes (on page 327)*.

#### In Live

To load a new cue to a fader, place the cue on the command line and press [Load] for the desired playback. When the [Go] button is pressed, the activated cue is the selected cue.

> Assume you have cue list 1 already loaded to the master playback faders. Now you want to load cue 2/1 to a fader.

-   [Cue] [2] [/] [1] [Load]

> If you press the [Load] button above the master playback fader, it will load cue 2/1 into the pending file. You could also press the [Load] button above any other playback fader to load the cue into that fader's pending file.
>
> In this example, the last cue executed from cue list 1 is still the active cue, while cue 2/1 is pending. When [Go] is pressed, 2/1 will be executed.
>
> You can also load cue list 2 by pressing [Cue] [2] [/] [Load]. This will load the first cue of list 2 into pending.

The selected cue is changed by go, record, or update instructions as well as cue modification and selecting a cue on the command line. When you execute a cue that has a follow or hang time, the next cue will become the selected cue when activated.

#### In Blind

While in Blind, changing the selected cue will change the playback status display to show information surrounding that cue.

> **CAUTION:** *When editing in Blind, changes to cues are automatically stored, therefore no update or record command is required.*

While working in Blind mode, cues can be executed in Live using [Go], [Back], [Stop/Back], and [Go to Cue], but this does not change the cue you are working with in Blind.

#### Loading a Cue With Temporary Time

A cue can be loaded with a temporary time.

-   [Cue] [3] [Time] [6] [Load] - loads cue 3 with the manual time of 6.

> **Note:** *For multipart cues, the temporary time will be applied to the entire cue, not just the part on the command line. For cues with discrete timing, its parameters will* *use the temporary time instead of the assigned discrete timing.*

### Out-of-Sequence Cues

An out-of-sequence cue is any cue that is played back in one of the following ways:

-   Cue is executed using a [Go To Cue] command. (*Go To Cue (below)*)

-   Cue is executed by a link instruction. (*Link / Loop (on page 328)*)

-   Cue is loaded into a fader's pending file. (*Selected Cue (on the previous page)*)

-   Cue is re-executed using [Assert] & [Load] or is asserted from the command line. (*Assert (Fader Control) (on page 386)*)

    -   Ion Classic users will need to use {Assert}

Generally, when an out-of-sequence cue is executed, the entire contents of the cue will be played back (move instructions and tracked values).

> Cue 1 sets channel 1 to full. That value is tracked forward until cue 10. The programmer plays back cue 1. She then sets channel 1\'s intensity to 50% manually. If she executes cue 2, channel 1 remains at 50%, as it is a channel parameter that is not receiving a move instruction from the incoming cue.
>
> However, if she presses [Go to Cue] [5] [Enter] (an out-of-sequence execution), even though the value for channel 1 in Cue 5 is a tracked value, channel 1 will fade from the manual value of 50%, to full in the Go-to-cue time.

#### Go To Cue

[Go to Cue] instructions can be executed from any operating mode. By default, a [Go to Cue] instruction is an out-of-sequence cue and will follow the rules of such (see *Out-of-Sequence Cues (above)*).

Following are examples of [Go To Cue]:

-   [Go To Cue] [5] [Enter] - all parameters with values in cue 5 are faded to those values, even if they are tracked.

-   [Go to Cue] [6] [At] [5] [Enter] - takes you to cue 6 at 50% of its fade completion. Hitting [Go] would finish the cue.

-   [Go To Cue] [Next] [Enter] - takes you to the next cue in the active list.

-   [Go To Cue] [Last] [Enter] - takes you to the previous cue in the active list.

When a [Go To Cue] instruction is executed, any null states applied with {Make Null} are removed. To maintain the make null setting, you should use [Capture] for the required channels. For more information, see *Make Null (on page 369)* and*Capture (on page 371)*.

#### Go To Cue Timing

[Go To Cue] uses go-to-cue timing established in Setup *Manual Control (on page 221)*. You can use a [Go To Cue] instruction with different timing options as follows:

> **Note:** *A cue can be loaded with a temporary timing. See Loading a Cue With Temporary Time (on the previous page).*

-   [Go To Cue] [2] [Time] [1] [Enter] - this command would take you to cue 2 in one second.

-   [Go To Cue] [3] [Time] [4] [/] [3] [Enter] - this command would take you to cue 3 and all up fades and NP moves would have a time of four seconds and down fades of 3.

-   [Go to Cue] [Next] [Time] [3] [Enter] - this command would take you to the next cue in the selected list in three seconds.

-   [Go to Cue] [Last] [Time] [2] [Enter] - this command would take you to the previous cue in the selected list in two seconds.

-   [Go To Cue] [8] [Time] [Enter] - this command would take you to cue 8 using all timing values stored in cue 8.

#### Other Go To Cue Options

When [Go to Cue] is pressed, the softkeys in the CIA change to provide Go to Cue modifiers to enhance your playback ability.

From these softkeys, you can specify that when going to a cue, only some elements of that cue will be played back. Specifically you can choose to play back:

-   Manual control using a fader

    -   [Go to Cue] [6] {Manual} [Enter]

-   Scenes opens the *Scenes (on page 331)* selection display.

    -   [Go To Cue] {Scenes} - press or select a scene to go to that cue.

-   Move instructions only

-   [GoTo Cue] [3] {MovesOnly} [Enter]

-   Withhold any links (follow, hang, execute instructions)

-   [GoTo Cue] [4] {MinusLinks} [Enter]

-   Use marks

-   [GoTo Cue] [5] {Use Marks} [Enter] - delays channels from marking until their intensities have reached zero.

-   Not available on Element Classic

-   Complete a cue

-   [Go To Cue] [4] {Complete} [Enter] will go to cue 4 and if that cue has a follow/ hang, any following cues in the sequence will also fire. This may look like you are going straight to the last cue in the sequence but each cue will fire to make sure that any external links are fired.

-   [Go To Cue] [2] [At] [5][0] {Complete} [Enter] will go to cue 2 at 50% of its completion.

-   [Go to Cue] [5] [Time] [Go to Cue] will go to cue 5 using cue times, and append [Complete] to the command line.

-   Single parameter channels only (conventionals)

-   [GoTo Cue] [1] {SingleParam} [Enter]

-   Multiple parameter channels only (automated fixtures)

-   [GoTo Cue] [2] {MultiParam} [Enter]

> **Note:** *Double pressing [Go To Cue] will post Go To Cue Complete to the command line. You can then select the appropriate cue number and level of completion.*

The following are additional modifiers that can be used with [Go To Cue]:

-   Homes a cue list to its first cue

-   [Go to Cue] [Home] [Enter] homes the currently selected cue list to its first cue. [Go to Cue] [x] [/] [Home] [Enter] homes a cue list to its first cue.

-   

-   Takes a cue list to its last cue

-   [Go to Cue] [Shift] [Home] [Enter] homes the currently selected cue list to its last cue. [Go to Cue] [x] [/] [Shift] [Home] [Enter] will take you to the last cue in a cue list.

-   Go to Cue Out

-   [Go to Cue] [x] [/] [Out] [Enter] allows you to use the [Go to Cue] [Out] command on a list specific basis. [Go to Cue] [Out] continues to affect all active cue lists.

> **Note:** *[Go to Cue] [x] [/] [Out] is similar to [Go to Cue] [x] [/] [0] except that any NPs on the fader will fade to their home level.*

-   Time

-   [Go to Cue] [5] [Time] [Enter] will go to cue 5 using cue times, and also uses any associated follow/hang times to automatically trigger the subsequent cue. To go to a cue in cue time, but not trigger the follow/hang, you would use [Go to Cue] [5] {Minus Links} [Time] [Enter].

> **Note:** *If you want to specify a time or use the cue time, the [Time] command must always be entered after any other commands, such as {Minus Links} or {SingleParam}. The exception to this rule is {Manual}.*

These can be combined within the command line as well:

-   [Go To Cue] [1] {MultiParam} {MovesOnly} [Enter]

### Assigning Faders

> **Note:** *Additional virtual faders are available on [Tab] [2][8]. See Virtual Fader Module (on page 136).*

Cue playbacks, submasters, grandmasters, palettes, and presets are targets that can be assigned to faders.

Faders can be assigned in a number of different ways.

-   The *Fader Configuration* display

-   The *Fader List*

-   The *Cue List Properties* index

-   The *Submaster Properties* display

-   Manually using the [Load] button

The single cue list on Element 2 and Element Classic consoles can only be loaded to the master playback fader pair, and cannot be assigned to a fader.

#### With Auto Playback Enabled

> **Note:** *Not available on Element Classic.*

Auto Playback is a record function enabled in Setup > User > *Record Defaults*, that automatically executes cues recorded in live on playback faders. When the cue is executed on the playback fader, any manual parameters involved in the record operation are automatically released to the cue and all other values stored in the cue are owned by that cue.

When the first cue is stored on Eos, the cue list of that cue automatically loads on the master fader. Any subsequent cue lists stored will load to the next available fader.

#### Assigning Faders Manually

The location of playbacks, submasters, palettes, and presets on faders can also be defined as the contents of those targets are stored.

> **Note:** *Grandmasters must be defined in fader configuration display or the fader list. See Grandmaster (on page 134).*

If a fader is unmapped, a target can be loaded to that location by selecting the target from the command line and pressing the associated [Load] key. The fader will then be automatically assigned that target.

Once a cue list is loaded to a fader, storing to that cue list automatically plays the cue back on the appropriate fader, when auto playback on record is enabled in Setup > User > *Record Defaults*.

If a fader has been configured for default mapping ( see *Fader Configuration*), the fader will receive its configuration from the Cue List Index. Changes made to a cue list in the cue list index will be shared with any default mapping faders loaded with that cue list. If changes are made to a fader set to default mapping in the fader configuration display, those changes will also happen in the Cue List Index. If set to Local, any changes made in the fader configuration display will impact only that instance of the content.

To load a new cue into the pending file of a playback fader, when auto playback is disabled in setup, or when you want to move a cue list to a different fader, first place that cue or list number on the command line then press the associated [Load] button for the destination playback fader.

-   [Cue] [4] [Load] - changes the selected cue and loads it to the associated fader. This action assumes cue 4 is from the same cue list as is currently selected.

-   [Cue] [3] [/] [Load] - changes the selected cue list and loads it to the associated fader.

-   [Cue] [5] [/] [6] [Load] - changes the selected cue list and loads it to the associated fader with cue 6 as the pending cue.

### Changing Fader Pages

> Navigation changes to fader banks and wings in the same paging group will advance all the fader pages in the group. See *Wing Paging Groups (on page 231)*.

When fader pages are changed, motorized faders assume the last position the faders were in on that page. This includes homing submasters to their required home position if needed.

#### Paging Forwards

Pressing [Fader Page], or [+] on an external wing, will advance through the available pages of faders.

If pressed on a fader page with content, the pages will advance through subsequent pages with content until a blank page is reached. After that blank page, the remaining blank pages will be skipped, and the next page with content will be displayed. Pages will loop infinitely.

#### Paging Backwards

Pressing [Shift] & [Fader Page], or [-] on an external wing, will decrement through fader pages using the same logic as above. The first blank page chronologically after a page with content will still be used in reverse order. Pages will loop infinitely.

> **Example:** Pages 1, 5, 6, and 8 are populated on a 1x10 fader wing. From page 1 , pages will decrement in the order 1, 9, 8, 7, 6, 5, 2, back to 1, and so on.

#### Accessing Specific Pages

You can access a specific fader page at any time, by holding [Fader Page] and pressing the number of the page you wish to access.

Specific pages can also be accessed by holding [Fader Page] and using the bump buttons on an external wing.

#### Apex Fader Wheel Paging

Apex fader wheels are paged independently from the faders in the slots below them. Press and hold either [Page +] or [Page -] and move the wheel you wish to page.

#### Element 2, Element Classic, & Ion Classic Paging

On Element 2 and Element Classic, you can page the faders by holding down the {Page Subs} softkey in the Live display. The bump buttons will light up in green, and the bump buttons that correspond to the currently selected pages will flash. Press the corresponding bump button to go to that page. The fader status display will change to show the fader pages. See *Paging Submasters on Element 2 and Element Classic (on page 430)*.

On Ion Classic, holding down [Fader Control] to use the bump buttons on an external wing.

### Playback Fader Controls

A variety of buttons are found in the Master Fader controls or in the Fader Page controls area of your console.

On Ion Classic and Element Classic, many of these buttons exist as softkeys. In order to access these keys, press [Fader Control] (Ion Classic) or [Live] {Fader Control} (Element Classic). The softkeys will change to display the fader control keys. You may press [More SK] if the green LED is illuminated, to view additional fader control buttons.

#### Go

The [Go] button is used to execute the cue currently in the pending file of the associated fader. When [Go] is pressed, all parameters assume their required positions in the recorded times, unless they have been recorded with manual timing. When a cue has manual timing values stored with it, the fader will set itself to zero when [Go] is pressed, or you may set the fader to zero before you press [Go].

If a channel parameter is in a transition state when a new cue is activated on the same playback fader, that parameter will continue its initial instruction in its remaining time unless it receives a new move instruction in the incoming cue. If a new instruction is provided, the parameter will calculate its new target and the time to get there for a seamless course adjustment. If a parameter in transition has no new instruction in the incoming cue, it will continue its fade, using the original timing provided.

If a channel parameter is in a transition state when a new cue is activated on a different playback fader, and that parameter receives a move instruction, even if it is exactly the same instruction the parameter currently has, it will recalculate the destination and arrival time according to the information from the new cue.

> For information on manual timing, see *Manual Timing Control (on page 389)* and for manual master, see *Master (on page 350)*

##### [Go] on Element Classic

The [Go] button is used to execute the pending cue. When [Go] is pressed, all parameters assume their required positions in the recorded times, unless they have been recorded with manual timing.

#### Stop / Back

All fader activity can be instantly stopped mid-transition by pressing the [Stop/Back] button for the required fader. To resume the cue, press the [Go] button. To fade to the previous cue on that fader, using default "back" timing, press the [Stop/Back] button again from this state.

When you have gone to the previous cue using the [Stop/Back] button, the cue should look just like it did before you hit the [Go] button, if the cue still has ownership of all of its channels. If a different cue list has taken ownership of some of the channel parameters within that cue in the interim, those specific channel parameters will not respond to the [Stop/Back] command.

If a cue is recorded or rerecorded when a fade is stopped, the contents of that fader will be recorded as absolute data in the new record target. If a cue is updated with the fader in a stopped state, all references in the cue will be updated accordingly.

When a cue on the playback fader is complete, pressing [Stop/Back] will step backwards sequentially through the cue list from that point. [Stop/Back] uses default back time as established in Setup, see *Manual Control (on page 221)*. Or you can back into the previous cue using specific timing with [Go to Cue] [Last] [Time] [n] [Enter].

##### [Stop /Back] on Element Classic

When a cue is complete, pressing [Stop/Back] will step backwards sequentially through the cue list from that point. [Stop/Back] uses default back time as established in Setup, see *Manual Control (on page 221)*. Or you can back into the previous cue using specific timing by pressing:

-   [Go to Cue] [Last] [Time] [n] [Enter]

#### Blackout and Grandmaster

Blackout is a console function allowing you to immediately set all lighting levels to zero.

A grandmaster is type of fader that inhibits all live intensity values. Any fader on an Eos Family console or connected wing can be configured as a grandmaster. See *Grandmaster (on*

> *page 134)*.
>
> **Note:** *Ion Classic and Element Classic have physical grandmasters.*

If a grandmaster is set to a value other than 100%, a grandmaster button with the set value will be shown at the top of each display. If blackout is currently on, a blackout button will be shown at the top of the displays.

*(figure omise)*{width="2.6964162292213474in" height="0.15437445319335083in"}

Clicking on either button will open a new display which will allow you to turn off blackout and set the grandmaster to a different level.

*(figure omise)*{width="4.9756091426071745in" height="1.275in"}

#### Go To Cue 0

> **Note:** *[Go To Cue 0] is used in the examples below. Ion Classic users will need to use [Fader Control] {Go To Cue 0}.*

You can use [Go To Cue 0], located with the playback controls, in conjunction with a fader load button to send a specific cue list to cue 0. This action does not use the command line. Simply press [Go To Cue 0] & [Load] for the desired fader.

On Element 2 and Element Classic, you can use the [Go To Cue] [0] [Enter] command to send the cue list to cue 0. This drives all cue intensities to zero, while leaving non-intensity parameters as currently set but no longer under cue control.

> See *Using Go To Cue 0 (on page 363)*

#### Assert (Fader Control)

> **Note:** *There are two [Assert] buttons. The [Assert] button in the fader controls area is used in the examples below. Element 2 and Element Classic users will need to use*
>
> *{Fader Control} {Assert}. Ion Classic users will need to use [Fader Control] {Assert}.*

Use [Assert] & [Load] for the associated fader to re-run the active cue in that fader, following the same rules as [Go To Cue]. Assert can be used to regain control of all cue contents, apply a newly set priority state to the associated fader, or make any changes in blind to an active cue on stage.

When [Assert] & [Load] are used together, the entire contents of the cue are replayed. You can assert just certain elements of a cue by using the command line. See *Using Assert (on page 361)*

#### Timing Disable

> **Note:** *[Timing Disable] is used in the examples below. Element 2 and Element Classic users will need to use {Fader Control} {Timing Disable}. Ion Classic users will need to use [Fader Control] {Time Disable}.*

[Timing Disable] used with [Load] causes timing data to be ignored for any cues that are activated on the associated playback fader. When a playback fader is in timing disable mode, you will notice "TD" in the associated fader display, and the [Timing Disable] button will be red.

To release the playback fader from time disable mode, press [Timing Disable] & [Load] again. You can also cut the next cue in by pressing [Timing Disable] & [Go] or the last cue by pressing [Timing Disable] & [Back].

On Element 2, {Timing Disable} is a softkey accessed via [Live] {Fader Control}.

> **Note:** *[Shift] & [Go] and [Shift] & [Back] can be used to cut to the next cue in the same way as [Timing Disable] & [Go] and [Timing Disable] & [Back].*

Cues will snap from move instruction to the next move instruction in a time of zero, which is the default time. To set a different time for Timing Disable, go to Setup>User>Manual Control>Timing Disable. See *Manual Control (on page 221)*.

#### Freeze

> **Note:** *[Freeze] is used in the examples below. Element 2 and Element Classic users will need to use {Fader Control} {Freeze}. Ion Classic users will need to use [Fader Control] {Freeze}.*

[Freeze] can be used to halt all effect activity on any active faders. To activate a freeze for only a specific fader, press [Freeze] & [Load].

There are two ways to remove the freeze command:

-   Press [Freeze] & [Load] again for the specific faders to unfreeze the activity.

-   Press [Assert] & [Load] or [Go] or [Stop/Back] for the specific faders to resume the activity.

You may freeze and unfreeze effects from the command line.

-   [Effect] [2] [Freeze] [Enter] - to freeze effect 2. Freezing a specific effect is different from stopping an effect. Freeze will stop the effect exactly where it is.

-   [Effect] [6] [Thru] [9] [Freeze] [Enter] - to freeze a specified range of effects.

-   When an effect is in freeze mode, you can use the same command to unfreeze:

-   [Effect] [2] [Freeze] [Enter]

-   [Effect] [6] [Thru] [9] [Freeze] [Enter]

#### Stop Effect

> **Note:** *[Stop Effect] is used in the examples below. Ion Classic users will need to use [Fader Control] {Stop Effect}. Element Classic users will need to use {Fader Control}*
>
> *{Stop Effect}.*

The [Stop Effect] button can be used to stop all effects from operating on any or all faders, or it may be used with the control keypad to stop a specific effect.

-   To stop all effects on a fader, press [Stop Effect] & [Load] of the associated fader.

-   To stop a specific effect regardless of the fader it is operating on, press [Stop Effect] [2] [Enter].

-   To stop an effect on a specific channel, press [5] [Stop Effect] [Enter].

When an effect is stopped, all impact of the effect is removed and the stage output is as though the effect has never been activated. This behavior is influenced by the exit behavior of the effect. See *Exit (on page 404)*

#### Rate Override

> **Note:** *[Rate] is used in the examples below. Element 2 and Element Classic users will need to use {Fader Control} {Rate}. Ion Classic users will need to use [Fader Control]*
>
> *{Rate}.*

To collect a playback fader for rate control, press [Rate] & [Load] for the required fader. When [Rate] is pressed without [Load], it always collects the master fader for rate control. A subset of faders can be collected by pressing and holding [Rate] while pressing the [Load] button for the associated faders you would like to add.

On Element 2 and Element Classic, rate control only applies to the master fader pair.

If a cue is complete, any rate adjustment applied affects the cue in the pending file. When that cue is subsequently activated, the adjusted rate is used to direct timing. Pressing [Rate] again will turn rate control off and reset to 100%.

#### Using Manual Control

There are four types of manual control for playbacks:

-   Cues can be stored with manual timing. When cues have stored manual timing, the default behavior of the fader is to control those manual values.

-   Cues can be captured for manual intensity control only. This is possible only when the associated cue has no manual timing values.

-   Cues can be manually overridden using the [Man Override] & [Load] feature which captures all parameter transitions.

    -   Element 2, Ion Classic, and Element Classic users will need to use [Live]

> {Fader Control} {Man Override}

-   The fader can be set to manual master mode. See *Master (on page 350)*.

In each of these cases, follow time counts down from [Go]. The hang time will be kicked off when the fader reaches full or when the last parameter reaches its end state from timing, whichever comes last.

> **Note:** *The Fader Ribbon and the Fader Display Format of the Playback Status Display are useful displays when using manual control. These displays are not available on Element 2 and Element Classic.*

##### Manual Timing Control

Manual timing can be set for any parameter or group of parameters. A fader is then used to control the progress of a transition.

> Assume the active cue contains an instruction to set red at 40 for channel 1.
>
> The pending cue contains an instruction to set color for channel 1 to blue and the color parameter has a manual time. Press [Go] to activate the cue.
>
> Channel 1 color does nothing.
>
> As you move the fader up manually, channel 1 color moves proportionally from red to blue. Any parameters with timing will start their moves at the press of [Go] and be unaffected by the manual control.

To program a channel manual time:

-   [1] {Color} [Time] {Manual} [Enter] - assigns a manual time to channel 1. This must be recorded or updated to a cue, when in Live.

Manual timing can also be set at a cue level:

-   [Record] [Cue] [5] [Time] {Manual} [Enter] Manual timing can also be set at a cue category level:

-   [Record] [Cue] [6] {Color} [Time] {Manual} [Enter]

##### Manual Intensity Override

An intensity transition may be taken over manually and the transition captured by dropping the fader down until it reaches the percentage of cue completion (i.e. if the cue is 50% complete, when the fader is manually dropped to 50%, the intensity transitions will be captured and the intensity portion of the cue completed by moving the fader manually between 50% and full or anywhere in between). If the fader is dropped below 50%, the fader will fade all intensity values proportionally from their captured values to their previous values.

If a fade is captured and the faders are not reset to 100% prior to the next press of the [Go] button, the fader will automatically reset to 100% upon cue execution. Alternatively, you can set the fader to 0% before executing the next cue to capture the cue for manual intensity control when the [Go] button is pressed if the fader is set to proportional control. Intensity control is released from the fader when the cue is considered complete (when the fader is brought back to 100%). If the fader is set as an Intensity Master, the intensity control is maintained, even when the cue has completed.

If a pending cue has any manual control properties, you may either preset the fader to zero or the console will automatically set the fader to zero when the [Go] button is pressed.

Manual intensity override is not possible if there is any manual timing in the cue, as the fader is already occupied with that control.

##### Manual Override

> **Note:** *[Man Override] is used in the examples below. Ion Classic users will need to use [Fader Control] {Man Override}. Element Classic users will need to use {Fader Control} {Man Override}.*

Manual override allows the associated fader to control all parameters in a transition state on that fader. When [Man Override] & [Load] are pressed, all activity on that fader is frozen and the motorized faders move to match the current fade progression.

The fader is used to manually complete the cue transition for all parameters. If the fader is operating in a paired mode, the left fader controls the intensity upfade and all non-intensity parameters, while the right fader controls all intensity downfade actions. Manual control override automatically releases when the cue is complete.

A group of faders can be collected for manual override by pressing [Man Override] & [Load] (continue adding faders by pressing the associated [Load] buttons).

#### Releasing Content From a Fader

> **Note:** *[Off] and [Release] are used in the examples below. Element 2 and Element Classic users will need to use {Fader Control} {Off} and {Fader Control} {Release}. Ion Classic users will need to use [Fader Control] {Off} and [Fader Control] {Release}.*

There are a few ways to release content from a playback fader:

-   [Off] & [Load] - returns control to the background fader, either a cue or a submaster, and stops any effects that are running on that fader. If there is no background value, the intensities will just fade out.

> **Note:** *Associated pending and current cues will remain when using [Off] & [Load].*
>
> **Note:** *Pressing [Go] will run the cues in their current sequence.*

-   [Release] & [Load] - behaves like [Off] & [Load] except that it sets the pending cue to the first cue in the list and removes the active cue. On Element 2, press {Fader Control} to see {Release}.

-   [Shift] & [Load] - behaves like Release & [Load] except that it additionally removes the content entirely from the fader. Pressing [Shift] & [Load] on an empty playback fader will unmap the fader.

-   [Escape] & [Load] - unmaps all instances of the target (cue list, submaster, palette, or preset) on a selected fader.

The [Go To Cue] [Out] [Enter]command can be used to fade out all intensities, reset all cue lists to the top, and to clear out all background LTP fader values.

### Cue Alerts

Eos can learn the time between manual [Go] commands in the same cue list and, in future runs, display a cue alert timer counting down to the next expected [Go]. The cue alert timer is informational only and is not a follow time (see *Follow / Hang (on page 327)*).

#### Learning Alerts

From Live, use [Learn] {Learn Alert Time} to start learning alert timings. [Learn] will flash and \"Learning Alerts After GO\" will display above the command line. Use [Learn] again to stop learning alert timings.

##### Alerts in the Playback Status Display

> The Alert column can be enabled in the PSD via the *Playback Status Display Configuration (on page 112)* menu.

*(figure omise)*{width="5.866816491688539in" height="2.3843744531933506in"}

When alerts are being learned, a count-up timer appears in red in the Alert column after each manual [Go] command. After the next [Go], the time is stored and the process repeats.

Once alerts have been learned, after a manual [Go], the recorded time in the Alert column will begin counting down.

*(figure omise)*{width="5.851054243219598in" height="0.5006244531933508in"}

When the countdown is below 5 seconds, the time will change to gold, and the alert advisory sound will play.

*(figure omise)*{width="5.8518099300087485in" height="0.3024989063867017in"}

When the countdown reaches 0, the time will change to green and display until the next manual [Go].

##### Alert Sounds

The alert advisory sound can be enabled and adjusted in volume, or disabled via Setup

-   Device > Face Panel > *Sounds (on page 230)*.

#### Editing Alerts

{Alert Time} appears as a softkey option when one or more [Cue] is on the command line in Live or Blind. Times can be entered directly or adjusted with [+] and [-].

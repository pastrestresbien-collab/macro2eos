# Eos Family User Manual v3.2.0 — Chapitre 20 : Submasters

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 20
## Submasters
### About Submasters

Submasters can store any parameter data for channels. When storing from Live, Record Only and Record can both be used to determine what contents are stored. You can copy cues, presets, or palettes to a submaster as well. Channels running effects can be loaded onto a submaster. See *Effects on Faders (on page 420)*

Submasters can be controlled by faders or by the keypad. Faders can be configured as submasters (see *Submaster Properties (on page 432)* ) or they can be defined while programming.

> **Note:** *You can record up to 1000 submasters.*

In Blind, submasters can be created by using the [Thru] [Thru] syntax.

-   [Sub] [1] [Thru] [Thru] [1] [0] [Enter] - will create subs 1 through 10.

> When set as a submaster, the bottom buttons beneath the fader can be configured for different functions. See *Submaster Fader and Button Configuration (on page 436)*.
>
> It is possible to program upfade, dwell, and downfade times in association with the submaster bumps. See *Submaster Properties (on page 432)*.

#### What does a Blinking LED Mean?

When a submaster bump LED is blinking, it means that the submaster must be homed due to either changes to its content or to its mode. In either case, reset the submaster by dropping it to zero and the moving it back to the desired position. The LED will also blink when the submaster is in a "Hold" state via bump button timing.

### Paging Submasters on Element 2 and Element Classic

#### Element 2

Element 2 has a total of 1000 submasters. The fader position switch can be placed in faders 1-40 or 41-80 modes. Element 2 will default to the first 80 faders. To page through the available submasters, hold down the {Page Subs} softkey in the Live display. The bump buttons will light up in green, and the bump buttons that correspond to the currently selected pages will flash. Press the corresponding bump button to go to that page. The fader ribbon will change to show the submaster pages.

#### Element Classic

Element has a total of 1000 submasters. With the fader position switch in submaster mode, an Element 60 will display 60 submasters, and an Element 40 will display 40 submasters at a time. Element will default to the first 40 or 60 submasters. To page through the available submasters, hold down the {Page Subs} softkey in the Live display. The bump buttons will light up in green, and the bump buttons that correspond to the currently selected pages will flash. Press the corresponding bump button to go to that page. The fader ribbon will change to show the submaster pages.

![](media/media/image289.png){width="5.001851487314085in" height="0.2813538932633421in"}

There are 20 pages available on Element 40 for a total of 800 submasters

> **Note:** *Submasters 801-1000 can only be controlled by the keypad on Element 40.*

![](media/media/image290.png){width="5.035in" height="0.4195833333333333in"}

There are 17 pages available on Element 60 for a total of 1000 submasters.

### Recording a Submaster

You can record current stage contents directly to a submaster. To do this, set levels in live as needed then record them to the submaster. See the following examples:

-   [Record] [Sub] [5] [Enter] - records all current values to submaster 5.

-   [Record Only] [Sub] [5] [Enter] - records the manual values of the current stage state to submaster 5.

-   [Record Only] [Sub] [5] [Label] [xxxx] [Enter] - as above, with a label.

-   [Record] [Sub] [5] {Properties} - opens the *Submaster Properties* window so you can select properties while recording your submaster.

-   [Record] [Load] - for devices with a single load button per fader. Records all current values to the fader associated with the load button. Submaster will be stored with the number associated with the chosen fader.

-   [Record] [Both Bump Buttons] - for devices with two bump buttons per fader. Records all current values to the fader associated with the bump buttons. Submaster will be stored with the number associated with the chosen fader.

-   [Record] [Bump] - for devices with a single bump button per fader. Records all current values to the fader associated with the bump button. Submaster will be stored with the number associated with the chosen fader.

You can also record selected channel data to submasters as well.

-   [Channel List] [Record] [Sub] [5] [Enter] - records all data for the channel list to submaster 5.

-   [Channel List] [Record Only] [Sub] [5] [Enter] - records manual data for the channel list to submaster 5.

Submasters can also be recorded using selective storing, which allows you to specify only the channels that you want stored.

-   [6] [Thru] [1][0] [Record] [Sub] [3] [Enter] - records only channels 6 through 10 to

> submaster 3.

-   [1] [Thru] [5] {Blue} [Record] [Sub] [6] [Enter] - records only the blue color for channels 1 through 5.

-   [1] [Thru] [1][0] {Offset} {Odd} [Record] [Sub] [4] [Enter] - records channels 1, 3, 5, 7, 9 into submaster 4. For more information on using {Offset}, see *Offset (on page 242)*

If a submaster already has data stored to it, selective store will act as a merge function. Using the above example of channels 6 through 10 stored to submaster 3, if you were to then store channel 5 to submaster 3, that would be added to the current content so that channels 5 through 10 are now stored.

If you don\'t want the data to merge, you can either first delete the submaster to remove the original content (see *Deleting a Submaster (on page 441)*), or you can selective store while using [Rem Dim].

-   [5] Record] [Sub] [3] [Rem Dim] [Enter] - records channel 5 to submaster 3 and removes any previous data from the submaster.

### Submaster List

You can access the submaster list by pressing [Sub] [Sub], [Tab] [1][5] or through the browser (Record Target Lists>Submaster List>[Select]). Either of these commands will open a new tab for the submaster list or if it is already open on a tab, will bring focus to the list.

The list view includes a list of all submasters including their labels and all properties. You can navigate within the list by using the [Next] and [Last] buttons or by selecting the desired submaster from the command line.

### Editing Submasters

While in the Submaster list, if you want to edit the contents of the submaster, you can select the submaster and press {Edit}. This changes focus to the Live/ Blind tab and places you into the Blind edit mode for the specified submaster. You may also press [Blind] and select the required submaster from the command line.

Any changes made in this screen are automatically stored. A [Record] or [Update] command is not required.

### Submaster Properties

> Faders can be mapped to a submaster in the fader configuration display, or by recording or loading a submaster. See *Fader Configuration (on page 129)*, *Recording a Submaster (on the previous page)*, or *Loading Faders (on page 437)*.

If a fader has been configured for default mapping in the fader configuration display, the fader will receive its configuration from the *Submaster List (above)*. Changes made to a submaster in the submaster list will be shared with any default mapping faders loaded with that submaster. If changes are made to a fader set to default mapping in the fader configuration display, those changes will also happen in the Submaster List. If set to Local, any changes made in the fader configuration display will impact only that instance of the content.

![](media/media/image291.png){width="5.046025809273841in" height="1.5873950131233596in"}

The following options are available for submaster faders:

#### Mode

You may define your submaster as additive (contributes to the live output), inhibitive (limits live output) or an effect submaster. Eos defaults to submasters being additive.

Additive submasters are indicated by a green LED and a yellow fader icon in the fader ribbon.

Inhibitive submasters display these indicators in red. Channels mastered by an inhibitive submaster are indicated with an "I" next to the intensity value in the channel display in Live. Inhibitive submasters do not provide levels to the stage picture, they limit them (similar to a grandmaster). It is possible to put non-intensity parameters onto an inhibitive submaster, but it must be done from Blind.

> For more information about effect submasters, see *Effects on Faders (on page 420)*.

#### Master

A fader can be assigned as a Master. When it is a master, its behavior as a Proportional Master or Intensity Master (I-Master) is drawn from this setting.

##### Proportional Master

When a submaster is proportional, the slider will control all contents of the submaster (intensity and non-intensity parameters) when moved from zero. When a proportional sub is returned toward zero, channel will be returned to their previous level.

The bump button can be used to bump all values to their recorded levels in the submaster, or, by assigning timing values, fade the contents of the submaster up or out. Eos defaults to submasters as proportional.

##### Intensity Master

When set to intensity master, the slider will control intensity only. The bump button can be used to preset (mark) non-intensity parameters stored to the submaster. If the bump is not pressed before the slider is moved, the slider will snap the non-intensity-parameters to their target values. Once the non-intensity-parameters are at their end state, the slider only controls intensity. When dropped toward zero, controlled intensities will be faded toward zero.

When non-intensity parameters on a intensity master submaster have been marked using the bump button, the LED on its bump button will blink to tell you that the non-intensity parameters have been marked.

Pressing the bump button for an intensity master submaster that is currently bumped will release the non-intensity parameters using the bump button timing. Its bump button LED will also be turned off.

> **Note:** *For channels that have been set to GM Exempt in Patch, Intensity Master control will not impact the intensity of those channels. See Patch > Attributes (on page 182).*

#### HTP

Intensity playback behavior can be set to HTP (highest takes precedence) or LTP (latest takes precedence). Non-intensity parameters are always LTP. Eos defaults all submasters to HTP. For more information on HTP and LTP see *HTP vs. LTP (on page 10)*.

#### Restore

Submasters can be placed into restore modes of minimum or background, which is the default. When a submaster is in the restore to background mode, the restore column of the submaster list display will be blank. When in minimum mode, \'Min\' will display in the restore column.

The restore mode of background means that when the submaster is returned to zero, control will be restored to the background value, such as another submaster or a cue.

The restore mode of minimum means that when the submaster is faded down, control does not go to the previous background state but to the parameters' minimum value.

#### Priority

There are 10 levels of priority for submasters. 1 is the lowest and 10 is the highest. The default priority level is 4.

##### Shielded

Submasters can be shielded, which means that their content is automatically made exclusive and can\'t be controlled by anything other than that submaster and park, including by manual control. Shielded has a higher priority than 10.

Channels stored to shielded submasters will display in yellow with a superscript 's' beside it.

If channel parameters stored to shielded submasters were previously stored to cues or other submasters, those instructions will be ignored on playback.

If the same channels are assigned to more than one shielded submaster, control of those channels will be shared on either a LTP or HTP basis depending on the settings for the submasters.

#### Background

Submasters can have their background states disabled. Background states are enabled by default. When enabled, the content of the submaster will act as a background or previous state for other cues and submasters.

When a submaster has its background state disabled, a "D" will be displayed in the Submaster List background column.

> Cue 1 has channel 10 at 25%. Submaster 1 is raised and has channel 10 at 50%. Submaster 2 is then brought up and has channel 10 at Full. When submaster 2 is lowered to zero, control will be returned to submaster 1. If submaster 1 is lowered to zero, control will return to cue 1.
>
> Using the above example, if submaster 1 has its background state disabled, which makes its content unavailable as a background state, then when submaster 2 is lowered to zero, control would return to cue 1 and not to submaster 1.

#### Background Priority

Background can have a priority assigned to it. Background priority releases to the highest priority content that previously had ownership, provided that content has not be turned off or released.

There are 10 levels of background priority for submasters. 1 is the lowest and 10 is the highest.

#### Up Time

This is the time for the submaster to fade from its home position to its target position (0 to Full if additive, Full to 0 if inhibitive). The default time is 0.

#### Dwell Time

This is the time the submaster look will hold before starting the downfade. This can be set to a specified time, or to "Hold" or "Manual". "Hold" time maintains the submaster values until the bump is pressed a second time. "Manual" time applies the submaster values only as long as the bump is held. The default is "Manual".

#### Down Time

This is the time for the submaster to fade from its target position to its home position. The default time is 0.

#### Stomp Mode

Stomp happens when all the content owned by a submaster is now being controlled by other targets. The submaster is being removed from the background , and once that happens, it would not be eligible to fade back. You can assign behavior that will happen when a submaster is stomped.

The following are Stomp Mode options:

-   Off When Stomped - puts the content into an off state, the same behavior encountered when pressing [Off] & [Load].

    -   Ion Classic and Element Classic users will need to use {Off}

-   Unload When Stomped - unloads the fader.

-   Nothing When Stomped - no action happens to the submaster.

-   Release When Stomped -This function behaves the same as Off When Stomped.

#### Unmark at 0 % 

When this option is on, marked content controlled by the submaster will automatically be released when the fader reaches 0%. When the bump button is next pressed, the submaster will fire. If this option is off, you would need to first press the bump button to reset the submaster before pressing the bump again to fire it.

> **Note:** *This option is for submasters that are set to Intensity Master.*

#### Exclude

Those exclusions include:

-   Exclude From Record - output is not recorded into any other record target.

-   Exclude From Grandmaster - content cannot be mastered by a grandmaster.

-   Exclude From Inhibitive Sub - content cannot be mastered by an inhibitive submaster

-   Exclude From Solo - content will ignore solo. See *Submaster Fader and Button Configuration (on the next page)* on solo.

#### Channel and Parameter Filters

Channel and Parameter Filters can be used to allow only specified data to be played back. These are playback filters, and do not impact how data is recorded.

For submasters, channel and parameter filters can be set in the following areas:

-   Submaster List

-   In Live using the {Properties} softkey

Tap or click on {Chan Filter} to assign channels or groups. Tap or click on {Param Filter} to open a list of available parameters that you can filter.

> **Note:** *Filters will travel with their assigned submasters wherever they are mapped.*

When a filter has been applied, an indicator will display in the fader ribbon. C will display for channel filter, and F is for parameter filter.

Press the red [X] to clear the channel or parameter filters listed.

#### FX Off 0

Starts the effect when master fader is moved from 0, stops the effect when it is moved to 0. This is enabled by default.

### Submaster Fader and Button Configuration

Click or tap on the virtual buttons or fader to see a list of available configuration options.

![](media/media/image292.png){width="0.7537314085739283in" height="1.8791666666666667in"}

#### Button Options

The following options are available for submaster buttons:

-   Bump - plays back the submaster at 100% of the recorded level. It will continue to do so until released, unless the submaster has a time assigned or the {Hold} property set.

-   Group/ Assert - selects all the channels associated with the submaster, if the submaster is inactive. If the submaster is active, the contents of the submaster will be asserted.

-   Assert - regains control of all of the channels associated with the submaster.

-   Group Select - selects the channels stored in the submaster. This is the same as [Group] [Sub] [n].

-   Freeze - halts all effect activity on the fader.

-   Off - removes the content and if the fader is set to Master, the fader will remain where it currently is.

-   Release - removes the content and if the fader is set to Master, the fader will reset to 0.

-   Start Stop Effect -starts the effect while ignoring dwell times. Will stop effects if any are running.

-   Button Disabled - no action is assigned to the button.

-   Mark NPs - If no non-intensity parameters are owned by the submaster, it will fade the parameters on any dark channels in bump up time. If any non-intensity parameters are owned by the submaster, it releases the non-intensity parameters in bump down time. Dwell time and mode are ignored.

-   Solo - suppresses any intensity values not provided by the associated content while the solo button is held down. When the button is released, intensity values are restored. Priority and HTP are ignored. Shielded, park and pixel mapping outputs are not affected by the solo button.

-   Back - fades to the previous cue when fader is assigned to a cue list.

-   Macro - allows you to assign a macro as a button action.

#### Fader Options

The following options are available for a submaster fader:

-   Master - fader will be a proportional master, a manual master, or an intensity master.

-   Effect Rate - fader centers to home. It controls the rate of any running effects (same behavior as using rate via the Effect Status Display). The adjusted setting from this control cannot be stored.

-   Effect Size - similar to Effect Rate but for effect size.

-   Rate Master - homes to center. It adjusts the cue rate, just like rate and load.

-   Fader Disabled - no action is assigned to the fader.

-   Master Only - fader is used to set a level for content to fade to. The slider can be used to live adjust levels when the fader has been activated via the bump button. See *Master Only (on page 134)*.

-   Effect Master - masters the entry/exit mode of the effects (size, rate or both).

-   Levels Only - masters the levels without mastering the effect.

### Submaster Information

In the display for any programmed submaster, you will see the following:

On Element 2 and Element Classic, you will see this information in the fader status display. See

> *Indicators in the Element 2 & Element Classic Fader Status Display (on page 131)*

**Note:** *Inhibitive submasters display in red and additive submasters in yellow.*

-   Submaster number

-   Submaster label (if any)

-   Priority flag (if any)

-   I-Master flag (if any)

-   Current submaster value

### Labeling Submasters

Submasters can be labeled using the [Label] key.

-   [Sub] [6] [Label] [xxxx] [Enter] - labels submaster 6.

-   [Sub] [6] [Label] [Label [Enter] - removes the label.

If you would like your label to wrap, use CTRL+J or type || to create a line break between words.

### Loading Faders

> **Note:** *Consoles a single cue list cannot map cues to faders.*

Faders can also be loaded with cues, presets, or palettes. You can convert an empty fader to a submaster without configuring it in fader configuration display. Any fader can be configured and loaded with a submaster if the fader is not configured, the fader is configured as a playback but has no cue list loaded to it, or the fader is configured as a submaster, but that submaster is empty.

Regardless of the fader configuration, if the above conditions are met, the fader can be loaded with the submaster or target specified on the command line.

> If data already occupies the fader, that fader must be unloaded before another target can be loaded. See *Releasing Content From a Submaster (on page 440)*

-   [Sub] [5] [Load] - loads submaster 5 to the fader associated with the load button.

-   [Int Palette] [1] [Load] - loads intensity palette 1 to the fader associated with the chosen load button.

-   [Cue] [5] [Load] - loads cue 5 to the fader associated with the chosen load button.

### Using Bump Button Timing With Submasters

Each submaster bump can have three different timing values: Up fade, Dwell, and Down fade (see *Submaster Properties (on page 432)*). The default timing is set so that the bump functions as an "on" flash key for additive submasters and an "off" flash key for inhibitive submasters. Effects on submasters will follow submaster timing, unless timing has been placed in the effect itself.

> **Note:** *At any time, the fader can be used to manually override fade progression or a submaster triggered with time.*

To add bump button timing live:

-   [Sub] [8] [Time] [3] [Time] [4] [Time] [3] [Enter] - adds a 3 second up fade, 4 second dwell and 3 second down fade to submaster 8.

-   [Sub] [2] [Time] [Time] {Manual} [Time] [3] [Enter] - adds a manual dwell time and a 3 second down fade time to submaster 2. When the bump is pressed and held, it will flash on and stay on until the button is released. It will then begin the down fade.

-   [Sub] [4] [Time] [3] [Time] {Hold} [Enter] - adds a 3 second up fade time, and a hold dwell time. When the bump is pressed, the up fade starts. Once at the target value it will remain there until the button is pressed again. The down fade will bump to zero.

-   [Sub] [3] [Time] [Enter] - resets all time for submaster 3 to default (Up = 0, Dwell = Manual, Down = 0).

### Controlling Subfades Manually

It is possible to take control of submasters even if they have recorded time. To capture the fade, you must push the fader past the current fade level. Once this is done, control is transferred to the fader for full manual control.

You may then use the fader to increase or decrease the submaster level as needed.

### Submasters & Triggers

Triggers can be used to tie actions such as macros, show control, or snapshots to sub playback.

#### {Execute}

When used after selecting a sub on the command line, {Execute} will open a trigger display in the CIA.

> ![](media/media/image293.png){width="5.83323053368329in" height="2.0795833333333333in"}

Buttons for common targets are available on the left. These options are also available below as softkeys.

The table on the right lists all triggers associated with the selected sub, along with their reference labels. You can remove individual triggers using the delete icon on each line.

##### Syntax

A variety of command line syntax is available when working with triggers:

Buttons for common targets are available on the left. These options are also available below as softkeys.

+-------------------------------------------------------------+----------------------------------------------------------+
| Action                                                      | Syntax                                                   |
+=============================================================+==========================================================+
| Add a trigger to a sub                                      | > [Sub] [#] {Execute} [+] {Target} [#] [Enter] |
+-------------------------------------------------------------+----------------------------------------------------------+
| Remove a trigger from a sub                                 | > [Sub] [#] {Execute} [-] {Target} [#] [Enter] |
+-------------------------------------------------------------+----------------------------------------------------------+
| Remove all triggers from a sub                              | [Sub] [#] {Execute} [Enter]                        |
+-------------------------------------------------------------+----------------------------------------------------------+
| Replace all triggers in a sub with the one specified*      | [Sub] [#] {Execute} {Target} [#] [Enter]         |
+-------------------------------------------------------------+----------------------------------------------------------+
| > Remove all instances of the specified target from a sub* | [Sub] [#] {Execute} {Target} [Enter]               |
+-------------------------------------------------------------+----------------------------------------------------------+
| ** Confirmation required*         |                                                          |
+-------------------------------------------------------------+----------------------------------------------------------+

### Freeze and Stop Effect on Submasters

#### [Freeze]

> **Note:** *Element 2 and Element Classic users will need to use [Live] {Fader Control}*
>
> *{Freeze}. Ion Classic users will need to use [Fader Control] {Freeze}.*

[Freeze] can be used to halt all effect activity on any active submaster. To activate a freeze for only a specific submaster, press [Freeze] & [Load].

There are two ways to remove the freeze command:

-   Press [Freeze] & [Load] again for the specific faders to unfreeze the activity.

-   Press [Assert] & [Load] or [Go] or [Stop/Back] for the specific faders to resume the activity.

#### [Stop Effect]

> **Note:** *Element 2 and Element Classic users will need to use [Live] {Fader Control}*
>
> *{Stop Effect}. Ion Classic users will need to use [Fader Control] {Stop Effect}.*

The [Stop Effect] button can be used to stop all effects from operating on any or all faders, or it may be used with the control keypad to stop a specific effect.

To stop all effects on a fader, press [Stop Effect] & [Load] of the associated fader. To stop a specific effect regardless of the fader it is operating on, press [Effect] [2] [StopEffect] [Enter].

When an effect is stopped, all impact of the effect is removed and the stage output is as though the effect had never been activated.

### Moving and Copying Submasters

You can move a submaster using Move To. Press [Copy To] twice to put Move To on the command line.

-   [Sub] [2] Move To [Sub 9] [Enter][Enter] - moves the contents, label, and timing data from submaster 2 and places it in submaster 9. Submaster 2 is removed.

You can copy the contents of a submaster by using the [Copy To] button.

-   [Sub] [2] [Copy To] [Sub 9] [Enter][Enter] - copies the contents, label, and timing data from submaster 2 and places it in submaster 9.

-   [Sub] [2] [Copy To] [Sub 9] {Attrs Only} [Enter][Enter] - copies all of the submaster properties from submaster 2 and places it in submaster 9. Levels, effects, and labels are not copied when using the {Attrs Only} softkey.

-   [Sub] [2] [Copy To] [Sub 9] {Labels Only} [Enter][Enter] - copies only the label from submaster 2 and places it in submaster 9.

### Releasing Content From a Submaster

> **Note:** *[Off] and [Release] are used in the examples below. Element 2 and Element Classic users will need to use {Fader Control} {Off} and {Fader Control} {Release}. Ion Classic users will need to use [Fader Control] {Off} and [Fader Control] {Release}.*

To release content from a submaster, use one of the following methods.

-   [Off] & [Load]- stops any running effects and fades out according to the {Restore} mode of the submaster.

-   [Release] & [Load] - behaves in the same way as [Off]. [Release] no longer unmaps the fader.

-   [Shift] & [Load] - behaves like [Off] and [Release] except that it will also unmap the fader.

> **Note:** *When a submaster on a motorized fader is released or turned off, the fader will home.*

### Updating a Submaster

It is possible to make changes to a submaster in Live mode. [Update] is used to store changes to a submaster.

-   [Update] [Sub] [5] [Enter] - updates submaster 5 to include changes in live output only for channels already in submaster 5. You can also press the bump button for submaster 5 to select it.

-   [Channel list] [Update] [Sub] [5] [Enter] - adds only the specified channels to submaster 5.

### Deleting a Submaster

You can delete a submaster using the [Delete] key. When a submaster is deleted, the fader remains configured as a submaster, but it will be empty, unless the {Unmap Faders} softkey is used.

-   [Delete] [Sub] [5] [Enter] [Enter] - deletes the contents of submaster 5.

-   [Delete] [Sub] [5] {Unmap Faders} [Enter] [Enter] - deletes the contents of submaster 5 and unmaps any faders that are currently mapped to submaster 5.

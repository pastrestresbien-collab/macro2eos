# Eos Family User Manual v3.2.0 — Chapitre 18 : Effects

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 18
## Effects
  -----------------------------------------------------------------------------------------------
  ---------------------------------- ------------------------------------------------------------
  -----------------------------------------------------------------------------------------------
  -----------------------------------------------------------------------------------------------
  ------------------------------------ ----------------------------------------------------------
  -----------------------------------------------------------------------------------------------
### About Effects

Effects are a method within Eos to provide dynamic, repetitive action to channels.This chapter explains the different types of effects, and how to use them.

Effects are manual control functions that can be applied to a channel parameter and then included in presets, cues, or submasters. Cues can contain both standard transitions for some channels/parameters and effects for the same or other channels/parameters.

Intensities can have different effects running at the same time but they must be from different sources. You can have an intensity effect running on a cue and those same channels can be impacted by an intensity effect on a submaster. See *Multiple Intensity HTP Effects (on*

> *page 415)*

Effects have user defined properties and attributes which are applied to the effects whenever they are used in cues. Effects also have cue level overrides, which allow you to use an effect in multiple locations, and modify its size, shape and / or rate in individual cues. See *Effect Channel Display (on page 407)*.

Effects are broken up into three fundamental behavior types:

-   Step Effects - are chases for one or more parameters. Intensity is the default. Step effects are On/ Off behavior. The ON value determines what the associated channel should do when the step is active, while the OFF value determines what the channel should do when the step is not active. See [*Step Effects (on page 1)*](19_Effects/02_Step_Effects/About_Step_Effects.htm)

-   Absolute Effects - are progressive behavior, rather than on/ off states of step effects. However, unlike relative effects, which are also progressive, you are determining exactly the behavior that you want to have for each transition in the effect. See *Absolute Effects (on page 410)*

-   Relative Effects - are math based effects that provide a continuous offset from the current parameter value. There are three different types of relative effects: Focus, Linear and Color. See *Relative Effects (on page 415)*

There are four different displays for viewing and editing effects:

-   Effect List - displays all of the recorded effects. See *The Effect List (below)*

-   Effect Editor - displays in the CIA when the Effect List is open. The editor will display the attributes and properties of a selected effect for editing. See *Effects Editor (on the facing page)*

-   Effect Status - displays information in the CIA about the currently running effects. See

> *Effect Status Display (on page 405)*

-   Effect Channels - displays all of the channels in the currently running effects so you can override certain effect properties. The effect status display will also open while in the effect channel display. See *Effect Channel Display (on page 407)*

### The Effect List

At any time you may press [Effect] [Effect] or [Tab] [1][3] to view the effect list. Any recorded effects will be displayed here. The effect list is a blind view and any changes made in this view are automatically stored; a record command is not required.

> You can also use the command line search to see a list of effect names while in live or blind. See *Command Line Search (on page 81)*.

Notice that there are effects existing in this list prior to any being recorded. Effects 901-918 are preprogrammed relative effects that are automatically available to you (see *Relative Effects (on page 415)*).

To navigate this list use the navigation keys as described in *Display Control and Navigation (on page 89)* or select the effect number you wish to work with. Notice that when you select the effect list, the CIA changes to display the information for the currently selected effect.

Effects can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Icons (on page 120)*.

*(figure omise)*{width="5.062657480314961in" height="3.3329166666666667in"}

#### Effect List Navigation

Using the [Next]/ [Last] keys will only move between effects in the effect list display. To navigate the effect editor, you will need to use the page arrow keys.

You can use [Page **◀**] or [Page **▶**] when in the effect list display to begin navigating in the effect editor. This only works for step or absolute effects. You can press [Escape] to return focus to the effect list display.

### Effects Editor

When viewing the effect list, the selected effect is displayed in the CIA. The effect properties/attributes are shown in categorized buttons in the CIA. To change any property/attribute, press the corresponding button and enter data as required.

> **Note:** *Some effect properties, such as rate and size, can only be modified in the Effect Status Display and in the Effect Channel Display.*

The properties display of the effects editor is shown below and definitions of properties follow:

> *(figure omise)*{width="2.8176115485564304in" height="1.5491655730533684in"}

#### Type

Defines the effect type: step-based, absolute, or relative (linear, focus, or color). To change the type, press {Type} and then press the desired effect type in the buttons to the left.

-   <Effect> [1] {Type} {Step based} [Enter]

#### Scale

Applies only to relative effects. This modifies the amount the pattern is offset from the current parameter values. The scale is expressed as a percentage increase or decrease (25 = 25% of the programmed value).

-   {Scale} [3] [0] [Enter] or you may adjust this using the scale encoder, if available.

#### Cycle Time

Provides a cumulative time to complete one full iteration of an effect. In relative effects, the cycle time determines the length of time required for one channel to complete the cycle.

In absolute and step-based effects, the cycle time determines the time required to complete one full iteration of the effect. In these effect types, modifying the cycle time changes the timing values proportionally within the effect itself.

To change the cycle time, press {Cycle Time} and then enter the desired time (in minutes and seconds) from the keypad, followed by [Enter]. This can also be adjusted from the encoder, if available.

#### Duration/Cycle

This determines the length of time an effect will run. To specify, press {Duration/Cycle} and then choose the desired method from the buttons that appear to the left. The options are:

-   {Infinite} - for step and absolute effects, the effect will run until the channel is provided a new instruction or the effect is stopped,. Relative effects with an infinite duration will run until a stop flag is applied.

-   {Duration} - the effect will run for a set amount of time given in minutes and seconds. Enter the time from the keypad.

-   {Num cycles} - the effect will run for a set number of iterations. Enter the number using the keypad.

-   {Duration/Cycles} {Num Cycles} [1] [0] [Enter]

When an effect with duration is running in a cue, the effect will display in light blue while it is running and dark blue when it has finished. This is only displayed in the Live Summary View.

#### Parameters

This allows you to select which parameters will be involved in the selected effect, by default. By entering a value here, you do not need to specify the required parameter when placing an effect on a channel group.

To add/ remove parameters to the effect, press {Parameters} and then select the desired parameters from the buttons that appear to the left.

-   {Parameters} {Iris} [Enter]

#### Attributes

These determine the basic behavior of the effect. Attributes include behaviors such as forward, reverse, bounce, positive, negative, and random grouping/ random rate. The attributes are slightly different between step, absolute, and relative effects.

-   Bounce - effect will run first in forward, then in reverse. Subsequent passes alternate between forward and reverse.

-   Forward - the effect will run in the programmed direction (the arrow on the pattern editor indicates "forward" for pattern effects, and step/ absolute effects will follow numerical order).

-   Reverse - effect will run in the opposite direction of forward or reverse numerical direction. Forward and Reverse are mutually exclusive settings.

-   Random Group- channel distribution or step order (depending on the type of effect) is applied in a continuously random fashion. Enables *Random Modifier (below)*.

-   Random Rate - This overrides the cycle time of the effect. Random Rate is applied in a range (for example 5 through 150). Enables *Random Modifier (below)*.

-   Continuous Run - the effect will keep running until there is a stop effect command. By default, {Continuous Run} is disabled for all step and absolute effects. It is enabled by default for relative effects. For more information, see *Stopping Effects (on page 418)*.

-   Repeat on Go - the effect will not restart unless {Repeat on Go} is used.

-   Build - keeps values at their on-state, even when the step is no longer active.

-   Positive - effect will run the steps (on state and off state) as programmed. Step effects only.

-   Negative - inverts the on state and off state for the effect. Step effects only.

-   Break Mode - mimics a scroll across a static background. All but the last action scroll one channel at a time across the selection. The final action appears on all channels not affected by the other actions. Absolute effects only.

-   Bounce Channels - runs the effect on the channels first in forward, then in reverse. Play with these behaviors to see how they alter your effect.

##### Random Modifier

Random Modifier is an optional parameter that offers additional control over the behavior of effects that have Random Group or Random Rate attributes applied.

-   Continuously Random - a \"true random\" option, which selects a different random modifier value each time the effect plays back.

-   1 - 9999 - each value provides a unique random behavior that is preserved between effects. This value can also be modified in Live to audition different random behaviors.

#### Entry

Establishes at what time and how channels will enter the effect. To change the entry method press {Entry} and then choose a method from the buttons to the left. Entry modes vary by effect type. The options are:

-   {Cascade} - channels enter the effect according to the trail and cycle time values (if applicable).

-   {Immediate} - all channels enter the effect instantaneously.

-   {Fade by Size} - The effect will achieve its full value as allowed by the pattern or step/absolute values using the In Time.

-   {Fade by Rate} - increases the rate of the effect as it enters. If an effect submaster has an entry mode of {Fade by Rate}, the submaster will control the rate between 0 to 100.

-   {Fade by Size and Rate} - the effect will achieve its full value as allowed by the pattern or step/absolute values and ramp up to full speed using the In Time.

#### Exit

Establishes at what time and how channels will exit the effect. To change the exit method press {Exit} and then choose a method from the buttons to the left. Exit modes vary by effect type and how the effect is stopped. The options are:

-   {Fade by Size} - when the effect is exited, values will return to their background state while still running using the exit time.

-   {Fade by Rate} - decreases the rate of the effect as it exits.

-   {Fade by Size and Rate} - when the effected is exited, channels will stop running the effect and return to their background state using the exit time.

-   {Stop and Fade} - when the effected is exited, channels will stop running the effect and return to their background state using the exit time.

-   {Stop and Hold} - when the effect is exited, channels will halt exactly where the effect left them.

#### Time (Entry or Exit)

These fields establish the length of time for channels to enter/exit the effect. It can be entered in minutes and seconds from the keypad. These timing values are applied to the entry and exit modes. Cue level timing is the default for these. Press {EnterTime} [Enter] or {Exit Time} [Enter]. To reset to defaults, press [Time] [Enter].

#### Grouping

Grouping is used only in relative and absolute effects. This determines how channels currently running the effect will be grouped throughout the pattern. To change this press {Grouping} and then enter the number of lights you want grouped together.

Grouping defaults to {Spread}. This means that every light the effect is applied to will act as an individual element, moving through the effect sequentially based on the channel selection order, cycle time, and trail times. You can enter any number from 1 through 2000. A grouping of 2 means that every other light in the selection list when the effect is applied will move together through the effect. Grouping of three means every third light, and so on.

Your options are 1 through 84 or {Spread} which will distribute each channel in the effect evenly and treat it as a separate group.

-   {Grouping} [2] - every other channel (in a range of channels) will be grouped when running the effect.

When an effect is applied to a group in live, that group is distributed by order, using this grouping function. If a group list is created and an effect applied, each group is considered an individual element within the effect.

#### Trail

Trail is applicable to relative and absolute effects. Trail determines how channels are to follow each other through the effect; it is a percentage of the cycle time. Trail can be any value from 0-200%, even, or solo. The default is even. For example:

-   {Even} - The groups will be distributed evenly throughout the pattern. This is calculated by dividing the cycle time of the effect by the number of groups of channels.

-   {10%}-{200%} - When the first group is 10% through the effect, the second group will start the effect, and so on through the remaining groups. Therefore, the groups will trail n% behind each other, as a percentage of the cycle time.

-   {Solo} - The first group will execute the entire pattern. When done, the second group will execute the entire pattern, and so on.

#### Effect Editor Navigation

To navigate the effect editor, you will need to use the page arrow keys.

You can use [Page **◀**]or [Page **▶**] when in the effect list display to begin navigating in the effect editor. This only works for step or absolute effects. You can press [Escape] to return focus to the effect list display.

#### Confirming Effect Changes

When using [Page ▼ ] to create a new effect step/ action in the Effects Editor display, you will first be asked to confirm the new step/ action number before continuing. This is to prevent new step/ action from being created by mistake.

#### Using Encoders With the Effect Editor

> **Note:** *This option is not available on Element 2 and Element Classic.*

When any effect is specified in the command line, the encoder display automatically repaints to display the following properties:

-   Cycle Time - Default is 5 seconds for relative effects

-   Scale

-   Shape (Vertical or Horizontal as defined by the {Mode} button)

-   Axis

At any time, you may use the encoders to adjust these properties within the effects editor for the specified effect.

### Effect Status Display

To view the effects currently running, you may press [Displays] > {Effect Status} to open the effect status display in the CIA.

This display shows you any currently running effects and gives you the ability to edit the effect while running.

If your console has encoders, when an effect is selected, the encoders and encoder screen change to allow you to manipulate the effect according to rate, size, horizontal form, vertical form, and axis.

> To edit an effect, select the effect using the command line or select it directly from the CIA.

-   [Effect] [9] [0] [2] [Enter]

> The encoder screen and softkeys will repaint so that they now control the five attributes in the columns of the effect status display:

-   Rate - modifies cycle time. Default is 100% and can be modified from 0%-2000%.

-   Size - modifies scale. Default is 100% and can be modified from 0%-2000%.

-   Shape (Vertical or Horizontal as defined by the {Mode} button) - Default is 100% and can be modified from 0%-2000%.

-   Axis - Default is 0° and can be modified by +/- 180°.

> Use the encoders or softkeys to adjust the effects while watching the effect on stage.
>
> Effect 1 is a step effect with the On State set to 50 and the Off State set to 10. If Size is set to 50, the On State will be set to 50% of 50 and the Off State will be 50% of 10. So On would be 25 and Off would be 5.

*(figure omise)*{width="5.020182633420823in" height="1.1399989063867018in"}

The effect itself can be accessed for editing from this display by pressing {Edit} - any changes made directly in the effect status display are made to the effect itself and must be stored. Cue level overrides also must be stored or updated to the required cue, but do not impact the basic effect itself.

Effect attributes modified in the effect status display can be reset to their previous values using the softkeys:

-   {Rate} [Enter] - resets the rate to the previous value.

The properties of an effect that can be modified at a cue or sub level will display at the bottom of the Effect Status display and in the *Effect Channel Display (on the facing page)* (which is access by pressing [Shift] & [Effect]). Click on a column to make changes from a list of available options.

Several color indicators are used in the Effect Status Display. Those colors and their meanings are:

-   Grey - property is drawn directly from the effect.

-   Red - property has been manually modified but not stored.

-   Blue - property is an override to the saved effect.

-   Magenta - property is tracking from a previous cue.

Clicking on the Attributes column will open the Effect Attribute Override display. From that display, you can access most of the same properties as those found in the Effect Editor. This display allows you to make modifications to properties, and store those modifications in a cue or submaster.

> *(figure omise)*{width="5.378811242344707in" height="3.2916666666666665in"}
>
> {Restart Effect} is an atrribute that can only be accessed from this display. When enabled,

{Restart Effect} will cause an effect to restart whenever the cue is fired. This attribute is applied to the cue that the effect is stored in and not in the effect itself.

> **Note:** *{Repeat on Go} is similar to {Restart Effect} but it is applied to the effect. For* *more information on {Repeat on Go}, see Effects Editor (on page 401).*

### Effect Channel Display

In the Effect Channels Display, you can override certain effect properties per channel at the cue level. To open this display, press [Expand] [Effect], [Tab] [8], or select the effect channel icon from the display management home screen.

*(figure omise)*{width="5.061659011373578in" height="2.6679166666666667in"}

The following properties can be overridden:

-   Rate

-   BPM

-   Size

-   Axis (Focus Effects Only)

-   H Form (Focus Effects Only)

-   V Form (Focus Effects Only)

> **Note:** *To add a channel level override, first you will need to be in the Effect Channel display with the effect running.*

[2][6]<Effect><1>{Rate}[6][Enter] - to change the rate for just channel 26. With the effect running, the console will default to the running effect number. You may need to select the effect first ([Effect] [n] [Enter]). This will open the effect status display, and you will have access to the effect softkeys.

In the effect status display, an "+" will display by any effect property that has a channel level override.

You can then store these channel overrides in a cue by using [Record] or [Update].

### Step Effects

In step effects, each step contains an on-state and an off-state. The on-state is the action the channels in the step should take when the step is active. The off -state is the action the channels in the step should take when the step is not active. Step effects are a quick and easy way to build simple chases.

When building step effects, channels must be defined for each step. This is different from absolute and relative effects.

Once complete, you may play back the effect on all channels embedded in it by pressing [Recall From] [Effect] [x] [Enter]. Or you may specify only certain channels to play back from the embedded channel list.

A step effect is displayed in a chart with the following columns:

-   Step - indicates the step numbers.

-   Channels - displays the channel(s) in the step.

-   Param - displays the parameter (if other than intensity) controlled by the step.

-   Step Time - time from triggering the associated step to triggering the next step.

-   In Time - the length of time for the channels to fade to the "on-state".

-   Dwell Time - the length of time the step remains in an "on-state".

-   Decay Time - the length of time it takes for the channels to fade to the "off-state".

-   On State - the parameter level (in%), or referenced data to be used for the on-state.

-   Off State - the parameter level (in%) or referenced data to be used for the steps off-state. If you want the "off-state" to be the background state from playback, select the column and press [At] [Enter].

All times are entered from the keypad in minutes and seconds, tenths and hundredths.

*(figure omise)*{width="4.8962806211723535in" height="1.2342705599300088in"}

If an effect step is on the command line or indicated in the blue text to the left of the command line, entering a number on the command line will default to selecting a step for the current selected effect.

If no step is displayed, the command line will default to an effect number.

#### Programming Step Effects

> To open the effects list press:

-   [Effect] [Effect]

> Establish the number of the effect by pressing:

-   <Effect> [1] [Enter]

> The CIA will repaint with unpopulated fields for the new effect. Assign the effect as "step" by pressing:

-   <Type> {StepBased}

> The effect will appear in the list and the CIA will repaint with the default entries for the effect and a step chart for the effect. Define the number of steps by pressing:

-   {Step} [1] [Thru] [6]

> The steps will populate the chart and will remain selected. To make identical changes to all steps at once, you may now use the page arrow keys to navigate the chart. To make changes to only a single step, specify only one step in the command line, default values are drawn from the previous step.
>
> After paging to the "Channels" column, specify the channels for the effect.

-   [1] [Thru] [1] [2] [Enter]

> Channels 1 through 12 will be broken up and distributed through the steps in the chart. Choose the parameter you would like in the effect by pressing:

-   {Parameters} <Intensity> (Intensity is assumed unless another parameter is specified)

> All steps are now intensity based. Use the page arrows to access the "Step time" column. Enter the desired step time:

-   [1]

> Page arrow to the Dwell Time (In time is left at 0) column and enter a dwell time:

-   [1]

> Page arrow to the Decay Time column and enter a decay time:

-   [.] [2] [5]

> Page arrow to the On State column and enter the on state percentage:

-   [1] [0] [0]

> Page arrow to the Off State column, or use the softkeys to go to the desired field, and enter the off state percentage:

-   [5]

> Adjust any of the effect details on the right side of the CIA by pressing the appropriate detail button and making changes (see *Effects Editor (on page 401)*).
>
> **Note:** *The cycle time is an aggregate of all of the timing in the effect and indicates how long it will take to make one full pass through the effect. If the cycle time is modified by the keypad or encoders, it proportionally adjusts all of the timing within the effect.*

##### Range for On State and Off State

You can apply a range of levels to the on state and off state for the steps. You can either apply a range using the percentage or by using a palette.

> Using the above example, select steps 1 through 6.

-   {Steps} [1] [Thru] [6] [Enter]

> Page arrow to the On State column and enter the on state range:

-   [1][0] [Thru] [1][0][0] - assigns the range starting at 10 and ending at 100 to steps 1 through 6. The range between 10 and 100 will be evenly divided between the available steps.

> -or-

-   [Intensity Palette] [1] [Thru] [5] - assigns intensity palettes 1 through 5 to the steps 1 through 6. Steps 1 through 5 will be assigned to palettes 1 through 5. Step 6 will be assigned to intensity palette 1. The range will wrap to fill any available steps.

##### Inserting a Step

To insert a step anywhere in the effect, specify the step you wish the new step to be inserted before.

-   [Effect] [1] {Step} [4] {Insert} [Enter] - Inserts a new step before step 4. If step four does not exist, it also creates the steps necessary to have "step 4" and then places a step ahead of it as well.

Inserted steps result in all succeeding steps to be bumped one place lower in the effect. In the above example, by inserting before step 4, step 4 would become step 5, step 5 would become 6 and so on. The inserted step would become the new step 4.

##### Deleting Steps

To delete a step from a step-based effect, specify the effect in the command line and press delete:

-   [Effect] [1] {Step} [4] [Delete] [Enter] [Enter]

-   [Effect] [1] {Step} [4] [Thru] [8] [Delete] [Enter] [Enter]

### Absolute Effects

Absolute effects are a listing of sequential actions that channels are to take. They differ from step effects in that there is no on/ off state, rather they define progressive behavior from one action, to the next, to the next, and so on. The best example of this is that palettes and presets can be used as actions in absolute effects.

Absolute effects differ from relative effects (which are also progressive) in that you are specifying exactly what actions you want the lights to take, rather than mathematical offsets from the current state (relative effects).

Absolute effects also do not contain an embedded channel list. Therefore, the effect must be applied to channels in order to be played back.

Absolute effects are displayed in a chart with the following columns:

-   Action - displays the action number.

-   Param - displays the parameter (if other than intensity) controlled by the action.

-   Step Time -time from triggering the associated action to triggering the next action.

-   Time - the time for the action to fade in.

-   Dwell - the duration of the action before moving to the next action.

-   Level - indicates either the level of the parameter specified in the effect, or the referenced value for the channel(s) to perform (Palette or preset as defined in the command line).

*(figure omise)*{width="5.0614752843394575in" height="1.2864577865266842in"}

In the above image, actions 1 through 7 indicate referenced values in the "Level" column (palettes or presets), though these values can be absolute data as well.

If an effect action is on the command line or indicated in the blue text to the left of the command line, entering a number on the command line will default to selecting a action for the previous selected effect.

If no action is displayed, the command line will default to an effect number.

Default step times will display in gray and in parentheses, and assigned step times will display in white without parentheses.

> **Note:** *The default step time is the time value plus the dwell value.*

If no step time has been assigned, the action will begin once the fade and dwell times for the previous action have completed. If a step time has been assigned, the next action will begin after that set amount of time has elapsed.

You can also define specific parameters for Absolute effect actions. To apply a parameter to a specific action, click in the Param column and select the desired parameter.

#### Programming Absolute Effects

> To open the effects list press:

-   [Effect] [Effect]

> Establish the number of the effect by pressing:

-   [Effect] [8] [Enter]

> The CIA will repaint with unpopulated fields for the new effect. Assign the effect as absolute by pressing:

-   <Type> {Absolute}

> The effect will appear in the list and the CIA will repaint with the default entries for the effect and an action chart for the effect. Define the first action by pressing:

-   {Action} [1] [Enter]

> The action will populate the chart and will remain selected. You can also create a range of actions at once, using the [Thru] button, if desired. Use the page keys to navigate to the different columns
>
> After arrowing to the "Time" column (or using the softkeys), specify the fade in time for the actions.

-   [5] [Enter]

> Page arrow to the Dwell column and enter a dwell time:

-   [5] [Enter]

> Page arrow to the Level column and enter the desired referenced target:

-   [Color Palette] [5]

> Page arrow down and a new action will be created. All fields default to the values in the previous action. Page to the next action in the Level column and enter the referenced target:

-   {Color Palette 8}

> Page arrow down to the next action in the Level column and enter the referenced target:

-   [Color Palette] [2]

> Page arrow down to the next action in the Level column and enter the referenced target:

-   {Color Palette 4}

> Adjust any of the effect details on the right side of the CIA by pressing the appropriate detail button and making changes (see *Effects Editor (on page 401)*).

##### Range for Level

You can apply a range of levels to the actions. You can either apply a range using the percentage or by using a palette.

> Using the above example, select actions 1 through 6.

-   {Actions} [1] [Thru] [6] [Enter]

> Page arrow to the level column and enter the range:

-   [1][0] [Thru] [1][0][0] - assigns the range starting at 10 and ending at 100 to actions 1 through 6. The range between 10 and 100 will be evenly divided between the available actions.

> -or-

-   [Color Palette] [1] [Thru] [3] - assigns color palettes 1 through 3 to the actions 1 through 6. Actions 1 through 3 will be assigned to palettes 1 through 3. Action 4 will be assigned to color palette 1. The range will wrap to fill any available actions.

### Effect Background Value Modification

For Step and Absolute effects, you can use [+], [-], and [/] to adjust the background value .

> **Note:** *When using [-], you will need to preface the command with [+] if you want to remove from the current value.*

**Note:** *[/] is used to scale the value by a percentage. See the example below.*

-   Effect 1 is a step effect with the on state set to 100 and the off state set to - 50% for all steps. To set the step off state to -50%, you would use the following syntax [Effect][1] [Step] [1], click on the Off State column in the Effects editor, then type [+] [-] [/] [5] <0> [Enter]. If the channels in the effect have a background value of 50, the off state for each step would be 25.

-   Effect 2 is an absolute effect. To set a level at + 20 of the background, you would use the following syntax, [Effect][2] {Action} [1], click the Level column in the Effects editor, then type [+] [2]<0> [Enter]. If the channels in the effect have a background value of 50, the level 1 in the effect would be at 70.

### Beats Per Minute

For step-based and absolute effects, you can set a beats per minute (BPM). For step-based effects, BPM affects the Step, In, Dwell, and Decay times, and for absolute effects, this affects the time/ dwell. Note that BPM impacts the effect directly.

There are two different ways for assigning BPM to effects:

#### Setting BPM

If you know the BPM, you can assign that directly to the effect by using the {BPM} softkey, which is available when in the effect editor display.

-   [Effect] [1] {BPM} [1][9][0] [Enter] - sets the BPM of effect 1 to 190. The step times will be adjusted for step-based effects, or the time/ dwell will be adjusted for absolute effects.

The BPM will display on the right side of the effect editor beside the effect number/ label. Editing the cycle time, the step time for a step-based effect, or the time/ dwell for an absolute effect will remove the BPM.

#### Learning BPM

If you don\'t know the desired BPM, you can learn the BPM. From Live, with the effect running:

-   [Effect] [1] [Learn] [Time] - posts Effect 1 Learn Time Sample BPM to the command line, and opens the effect editor display.

While in this mode, press [Enter] to establish the BPM. The console will use an average of the last three times you press [Enter] in this mode to calculate the BPM. Pressing [Learn] again will stop this mode.

In this mode, every time the BPM changes, a live running effect will be modified accordingly without stopping.

#### Learning Discrete Step Time

In learning discrete step time mode, every time you press [Enter], the time since the last press of [Enter] is used to set the next step\'s step time for a step-based effect, or the next step\'s fade/ dwell time of an absolute effect.

-   [Effect] [1] [Learn] [Time] [Time] - posts Effect 1 Learn Time Discrete Steps to the command line, and opens the effect editor display.

Pressing [Learn] again will stop this mode.

Instead of pressing [Enter], you can press [At] while in this mode to add new steps to the end of the effect. Pressing [Enter] will send you back to the first step in the effect.

#### BPM as a Cue Level Override

BPM can be applied to an effect or individual channels as only a cue level override in Live and Blind. As a cue level override, the effect step/ action times will not be affected.

> **Note:** *The effect editor cannot be open when applying a cue level override. The effect status display does need to be open though. You can open the effect status display from the home screen or by pressing [Effect] while in live.*

With an effect recorded into a cue and playing back in live, [Effect] [1] {BPM} [3][0] [Enter] will change the BPM of the effect running. This change will happen immediately but the step or action times will not change. You can see the BPM value, which will be in red, in the Effect Status display.

When the cue is updated or recorded with the new BPM, an "*" will appear next to the effect number in the Ext Links column of the PSD and the cue list. The BPM value in the effect status display will now be displayed in blue.

[1] [Effect] [1] {BPM} [3][0] [Enter] will only change the BPM for channel 1. A "+" will display in the BPM column of the effect status display, and the BPM will display in red in the effect channel display.

Once the cue is updated or recorded, the BPM will display in blue in the effect channel display. The "+" will still be displayed in the effect status display, and an "*" will appear next to the effect number in the Ext Links column of the PSD and the cue list.

### Multiple Intensity HTP Effects

Multiple intensity HTP effects are either step or absolute effects running on HTP submasters or cue lists. For multiple intensity HTP effects to run correctly, they must be recorded and played back from different sources.

For example, you create three separate step effects. Each effect impacts the same channels. For the three separate effects to run correctly you need to record them to three separate effect submasters or cues in separate cue lists. Either method will allow for each effect to run together according to the rules of HTP. But, for example, if you were to have three separate effects running on three separate effects submasters and you try to record that into one cue, the cue will only run the effects that were currently at the highest level at the moment of the record.

### Relative Effects

> A relative effect is an offset from the current state of a channel parameter. There are three different types of relative effects: *Focus Effects (below)*, *Color Effects (on the next page)* , and *Linear Effects (on the next page)*. Each of the these effect types have a graphic editor designed specifically for the parameters involved.

Relative effects have many of the same properties and attributes as step-based and absolute effects.

Eos Family consoles are preprogrammed with relative effects which represent some of the most commonly used patterns and parameters. These are automatically visible in the effects list and can be manipulated using the encoders to conform to your needs. You may also custom build relative effects.

> **Note:** *As you learn to use the effects editor with relative effects, it is recommended that you experiment with the preprogrammed effects until you understand the fundamentals and how effects can be altered.*

#### Focus Effects

Focus effects are designed to impact a channel's pan and tilt parameters. These are represented in the horizontal and vertical axes of the graph in the effects editor. They can be created from live or blind and the properties can be set in the effects editor as any other effect (see *Effects Editor (on page 401)*).

New focus effects default to a circle. You can clear this and draw your own shape by pressing

{Edit}>{Clear} and drawing on the graph with your finger or the mouse. Press {Apply} when you are done. Other pre-made focus effects can be modified in the same manner. The green arrow indicates default direction of motion, which can be modified in attributes.

*(figure omise)*{width="4.9764698162729655in" height="1.2337489063867018in"}

You can adjust the vertical form of a focus effect by holding hold down [Shift] while using the horizontal encoder, if available.

#### Color Effects

Color effects impact only color parameters. Hue and saturation offsets can be used which are represented in the horizontal and vertical axes of the graph in the effects editor. The

{Parameters} key within a color effect displays the various color mechanisms used in any patched channels.

New color effects default to a circle. You can clear this and draw your own shape by pressing

{Edit}>{Clear} and drawing on the graph with your finger or the mouse. Press {Apply} when you are done. Other pre-made color effects can be modified in the same manner. The green arrow indicates default direction of color shift, which can be modified in attributes.

*(figure omise)*{width="4.9785706474190725in" height="1.5246872265966753in"}

#### Linear Effects

A linear effect does not have to be parameter specific. Rather it can simply be a reference to a linear diagram which can be applied to any parameter. You can redraw the linear diagram for an existing linear effect by pressing {Edit}>{Clear} and then tracing the diagram on the graph with the mouse or your finger. Press {Apply} when you are done.

*(figure omise)*{width="4.963636264216973in" height="1.25125in"}

#### Define a Pattern Shape

Shapes can be defined for any relative effect (focus, color, or linear). You can either draw a pattern from scratch or use one of preexisting patterns as a starting point.

To define a shape, press the {Edit} softkey beneath the pattern editor. The softkeys will change to {Apply}, {Restore}, {Clear}.

1.  Press {Clear} to clear the pattern.

2.  Draw a new pattern using your finger (or the mouse), or select a preexisting pattern. If you want to return to the original pattern, press {Restore} before pressing apply.

3.  When you have the proper pattern drawn, press {Apply}. The pattern will be applied to the effect.

> **Note:** *If you delete a preprogrammed effect (for example, after making changes to it) the effect will return to its default value. You can also copy effects to another effect location and modify them from there. This will leave the original effect untouched.*

-   *[Effect] [904] [Copy To] [8] [Enter]*

> *(figure omise)*{width="4.995145450568679in" height="2.14375in"}

The following tools are also available to edit the curve with the mouse or touchscreen:

-   Draw - draw a new line for linear effects or append points to focus effects

-   Select - select points of the curve (if no points are selected, all are changed)

-   Move - move selected points, can also phase-shift the curve of linear effects in steps of 30 degree (only if no partial selection was made)

-   Form - freehand scale the curve horizontally and / or vertically

-   Scale - proportionally scale the curve (focus effects only)

-   Gamma - apply a log function to the curve (linear effects only)

-   Size - scale focus effects on both axis

-   Rotate - rotate focus effects around the center of the selected points The following actions are available when editing the curve:

-   Clear Selection - selects all points at once

-   Smooth - smooths the selected points

-   Mirror Hor. / Vert. - mirrors the curve

-   Subdivide - adds one point on each selected segment (useful to move that point or change the behavior of smooth)

-   Remove - removes the selected points

-   Undo - undoes the last operation

-   Redo - redoes the last operation

#### Programming a New Relative Effect

Below is the process used to program a new relative effect.

> To open the effects list press:

-   [Effect] [Effect]

> Establish the number of the effect by pressing:

-   [Effect] [4] {Type} {Linear/Focus/Color} [Enter]

> The effect will appear in the effect list and the CIA will repaint with the effect details visible. Manipulate the effect using the encoders, effect graph, and / or property fields so that the effect meets your needs (see *Effects Editor (on*
>
> *page 401)* for details on effect properties and encoders).

### Preprogrammed Rainbow Effects

Two preprogrammed rainbow linear effects are available in the effect list. Effect 917 is a Rainbow RGB effect, and effect 918 is a Rainbow CMY effect. These effects are for a rainbow on native color parameters that will fade hue from 0 to 360 with saturation at full, when the parameters are at their default levels. 0 is the default for CMY, and Full is the default for RGB.

### Apply an Existing Effect

Once an effect has been created, it will appear in the effects list. To apply an existing effect, press:

-   [Select Channels] [Effect] [x] [Enter] or using the direct selects

-   [Select Channels] {Effect x}

The selected channels will begin their changes as programmed in the effect.

> **Note:** *Since step based effects have an embedded channel list, those effects can be* *recalled by [Recall From] [Effect] [n] [Enter] without selecting channels.*

### Editing Effects Live

To edit an effect while it is running, press:

-   [Displays] {Effect Status}

The effect status display will open in the CIA and any currently running effects will be visible in the display. Selecting the effect number in the status display will select the effect for editing. Select the effect you want to edit live by pressing:

-   [Effect] [x] [Enter]

Adjust the attributes as described in *Effect Status Display (on page 405)*. Adjustments are cue overrides and don't impact the core effect. Changes made to effects in the effect status display impact only that instance of the effect. The changes will then need to be recorded or updated.

To edit other properties of the effect in live, press {Edit} and the effects editor will open (See *Effects Editor (on page 401)*. Changes made in the editor will impact the effect itself and all instances in which the effect is used.

### Stopping Effects

> **Note:** *[Stop Effect] is used in the examples below. Element 2 and Element Classic users will need to use {Fader Control} {Stop Effect}. Ion Classic users will need to use [Fader Control] {Stop Effect}.*

Pressing [Stop Effect] [Enter] will stop all running effects.

To stop a specific effect, press: [Stop Effect] [x] [Enter] or [Effect] [x] [At] [Enter]. You may also stop effects on specific channels by [selecting channels] [Effect] [Enter].

You may also remove an effect instruction by [selecting channels] [Effect] [At] [Enter]. This command will work in live or blind. You can also stop the whole effect by pressing [Effect] [x] [At] [Enter].

#### Assigning a Stop Effect Command

> A [Stop Effect] command can be assigned to a list of channels in a cue without an effect tracking into it, or to a list of channels in a submaster. See *Freeze and Stop Effect on Submasters (on page 439)*.

-   <channel> [1] [Stop Effect] [Enter] - will create a stop effect instruction for all selected parameters, if there isn\'t an effect running on any of the parameters.

-   <channel> [1] [Effect] [Enter] - will only stop the currently running effect.

##### Stop All

A stop all command can be used to place stop flags in cues and subs on channels/parameters that are not currently running effects, allowing subs and cues to stop other souces effects even if continuous run is enabled. Stop all can be accessed by double-pressing [Stop Effect].

-   <channel> [1] [Stop Effect] [Stop Effect] [Enter] - will stop any effects that might be running when that cue plays back

### Query and Group Effect

> **Note:** *[Query] is used in the examples below. Element 2, Ion Classic, and Element Classic users will need to use {Query}.*

You can use [Query] [Effect] [n], [Query] [Effect], and [Group] [Effect] [n] to select the channels currently running in the selected effect.

Using [Query] will select the channels in numeric order. [Group] will select the channels in the order that they were originally selected.

[Query] [Effect] will select all channels currently running effects.

-   [3][1] [+] [2][6] [+] [3][0] [+] [2][7] [+] [2][9] [+] [2][8] [Effect] [1] [Enter]

> Using [Query] [Effect] [1] will select the channels currently running effect 1. Using [Next], the channels will be selected in numeric order starting with channel 26.
>
> Using [Group] [Effect] [1] will select the channels currently running effect 1. However, pressing [Next], the channels will be selected in the order they were originally selected. In this example, channel 31 would be first, then channel 26.

### Replace With

{Replace With} allows you to replace an effect with another one. All overrides will be preserved.

-   [Effect] [1] {Replace With} <Effect> [2] - all channels that were running effect 1 will now be running effect 2.

### Deleting Effects

To delete an effect, press [Delete] [Effect] [n] [Enter] [Enter]. If you delete one of the default effects (901 through 918), that effect will return to its default values.

### Recording an Effect to a Preset

> **Note:** *[Preset] is used in the examples below. Element Classic users will need to press [Shift] & [Intensity Palette] or use the {Preset} button in ML Controls.*

Effects can be stored in a preset, and those presets can be used to create submasters and cues. However, the effect\'s data is only copied to the submaster or cue, and is no longer referenced through the preset. If changes are made to the effect in the preset, the effect saved to the submasters and cues will remain unchanged.

To apply an existing effect, press:

-   [Select Channels] [Effect] [x] [Enter] Recording to a preset, press:

-   [Record] [Preset] [x] {Plus FX} [Enter]

Pressing [Effect] after [Record] [Preset] [x] will append {Plus FX} to the command line.

-   [Record] [Preset] [x] [Effects] [Enter]

Effects are also included in Blind preset [Copy To] and [Recall From] commands.

### Recording an Effect in a Cue

To apply an existing effect, press:

-   [Select Channels] [Effect] [x] [Enter] Recording to a cue, press:

-   [Record] [Cue] [x] [Enter] Recording to a cue part, press:

-   [Record] [Cue] [x] [Part] [x] [Enter]

### Effects on Faders

Channels running effects can be loaded onto a submaster. By default pressing the bump button of the submaster starts or stops the effect.

For the submaster to control the rate and/ or size of the effect, it can be configured as an effects submaster. To configure an effects submaster, see *Submaster Properties (on page 432)*.

> **CAUTION:** *When a submaster is defined as effect, only the effect information is stored.*
>
> There are several submaster button and fader configuration options that affect how effects run. See *Submaster Fader and Button Configuration (on page 436)* about those options.

#### Configuring an Effect Submaster

To configure an effect submaster, press:

-   [Sub] [x] {Properties} [Enter]

> **Note:** *The {Properties} softkey will open the submaster properties display in the CIA. For more information, see Submaster Properties (on page 432).*

#### Recording an Effect to a Submaster

To apply an existing effect, press:

-   [Select Channels] [Effect] [x] [Enter] Recording to a submaster, press:

-   [Record] [Sub] [x] [Enter]

A submaster can be configured to be an effect submaster. You can configure at the same time as you record the submaster. Before you hit [Enter], hit the softkey for {Properties} to open the submaster properties display in the CIA. Select Effect as the mode. For more information, see *Submaster Properties (on page 432)*.

#### Running an Effect from a Submaster

The way effects are played back from a submaster depends on its mode, and whether the submaster is set to be a proportional fader or an intensity master.

Below is an example of four different submasters, in different modes, with the same effect stored to them.

##### Effect on an Additive/ Proportional Submaster

The submaster contains the intensity, pan/tilt data, along with the effect. Pressing the bump button starts the effect. The fader controls values not affected by the effect. Pressing the bump button again stops the effect.

##### Effect on an Additive/ Intensity Master Submaster

Pressing the bump button marks the lights, and starts the effect. The fader brings up any intensities stored in the submaster. Pressing the bump button again stops the effect.

##### Effect on an Effect/ Proportional Submaster

Pressing the bump button starts the effect. The fader controls the rate and/ or size based on the effect's entry behavior. Pressing the bump button again stops the effect.

##### Effect on an Effect/ Intensity Master Submaster

Pressing the bump button starts the effect. The fader controls the rate and/ or size based on the effect's entry behavior. Pressing the bump button again stops the effect.

In other words, there is no difference between a proportional fader and an intensity master when the submaster is configured to be an effect submaster.

#### Global Effects Fader

A fader can be mapped as global effects in *Fader Configuration*, [Tab] [3][6]. This fader type is used to master all effects or specific effects based off of the current filtering applied to the fader.

> **Note:** *You can use multiple global effects faders.*

The following filters can be applied to effects running on:

-   Cue lists - you can specify certain cue lists or select {All} or {None}.

    -   Not available on Element 2 or Element Classic.

-   Submasters - you can specify certain submasters or select {All} or {None}.

-   Channels - you can specify certain channels that will be affected by the global effects fader. See *Channel and Parameter Filters on Faders (on page 135)*

-   Parameters - you can specify certain parameters that will be affected by the global effects fader. See *Channel and Parameter Filters on Faders (on page 135)*

-   Effects - you can specify certain effects or select {All} or {None}.

-   Manual - when on, the global effects fader will only affect manually run effects. By default, this is off.

> **Note:** *If no filters have been applied, the fader will master all effects.*

##### Fader Options

The following fader options are available for a global effects fader:

-   Effect Rate - fader centers to home. It controls the rate of any running effects (same behavior as using rate via the Effect Status Display). Min is 0, and Max is 200.

-   Effect Size - similar to Effect Rate but for effect size. Min is 0, and Max is 200.

-   Fader Disabled - no action is assigned to the fader.

-   Effect Master - masters the entry/ exit mode of the effects (size, rate or both).

##### Button Options

The following options are available for global effect buttons:

-   Bump - plays back the effect at 100% of the recorded level. It will continue to do so until released.

-   Freeze - halts all effect activity on the fader.

-   Start Stop Effect -starts the effect while ignoring dwell times. Will stop effects if any are running.

-   Button Disabled - no action is assigned to the button.

-   Macro - allows you to assign a macro as a button action.

### Delaying Effects

A delay can be placed on an effect in a cue or submaster by using the syntax [Effect] [n] [Delay] [n] [Enter]. [Effect] [n] [Delay] [Enter] removes the delay.

> **Note:** *If an effect delay is set in live, the cue or submaster must be recorded to include the delay.*

The Effect Status display has a delay column to show when a delay has been applied to an effect. When an effect is in delay mode, the column will display the countdown for the delay.

When an effect is delayed, a "*" will display by the effect number in the playback status display FX column.

### Effects Variables

Variables give additional options for altering StepBased and Absolute effects on the fly.

#### Using Variables in Effects

First, insert one or more variables into a StepBased or Absolute effect using the {Variable} softkey. Available fields are Timing, On State, and Off State for StepBased effects, and Level and Timing for Absolute. A maximum of ten variables can be used.

> *(figure omise)*{width="3.267671697287839in" height="0.6016666666666667in"}

Variables can be substituted for any number in an effect, including for relative timing, and to define the number of a target, such as a Color Palette. Variables can also be used more than once in the same effect, or applied across multiple steps.

Variables need to be defined before the effect can be run. This can be done in the Effects editor by selecting the Attributes field.

*(figure omise)*{width="4.19451334208224in" height="1.1439577865266841in"}

Define your variables by selecting each one and giving them a value.

#### Altering Effects in Progress

Variables can also be defined in the Effects Status Display (ESD) before an effect is run, or redefined after an effect is already running.

*(figure omise)*{width="5.060211067366579in" height="1.1439577865266841in"}

Select {Attributes} to define or redefine variables. If variables are redefined in an already-running effect, the ESD will show the effect in red, with an asterisk (*) next to the effect number to indicate that it was modified. Store any manual changes using [Record] or [Update] as normal.

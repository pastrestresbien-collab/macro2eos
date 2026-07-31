# Eos Family User Manual v3.2.0 — Chapitre 06 : Manual Control

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 6
## Manual Control
> l
### About Manual Control

Eos provides a variety of different ways to select and command control channels. This chapter identifies the many basic ways you can select channels and manipulate show data within Eos.

> For additional methods, see *About Advanced Manual Control (on page 366)*.

### Using Channel Faders On Element 2 & Element Classic

One way to bring up channel levels with Element is using the channel faders. The fader position switch is used to select between channels 1 through 40, channels 41 through 80, or channels 81 through 120. Element will ship with the fader position switch in channels 1 through 40 mode.

With the fader position switch in channels 1 through 40 mode, channel 1 will be controlled by the leftmost fader in the first bank of faders. Channel 40 will be controlled by the rightmost fader in the second bank. When the fader position switch is in channels 41 through 80 mode, channel 41 will be controlled by the leftmost fader in the first bank of faders. Channel 80 will be controlled by the rightmost fader in the second bank.

> **Note:** *If you have an Element Classic 60 console, the third bank of faders are always in submaster mode.*
>
> **Note:** *Channel faders will only control the first 120 channels. Channels 121 and above must be controlled via the keypad. See Selecting Channels (below)*

Raising a channel fader will bring up the corresponding channel's level. This will be reflected on Element's live display. The channel intensity level will appear in red to indicate the level is being set manually. See *Color Indicators (on page 103)*

Element's fader status display will also show the channel's level. For more information, see

> *Indicators in the Element 2 & Element Classic Fader Status Display (on page 131)*

Element's channel faders are LTP or Latest-Takes-Precedence, which means that you can take control of a channel simply by moving the fader to match the current output level. Channel faders, like the keypad and level wheel, can then take levels above or below the current playback level. See *HTP vs. LTP (on page 10)*.

Holding down [Shift] while moving the channel faders, will allow them to move without changing the channel levels. This is helpful when you have used your channel faders to record a cue. This allows you to restore your faders to zero, while leaving the cue values on stage. If you don't do this, the LTP behavior will drive the channels toward zero.

### Selecting Channels

There are multiple ways to select channels including the control keypad, direct selects, and groups.

Selected channels are available for manual control through keypad commands, level wheel, and / or ML controls.

Channels are deselected when any action is taken on the keypad that is unrelated to manual control, such as recording groups and cues, or updating a record target, etc. You can also press [Clear] after a terminated command line to clear the channel selection.

> **Note:** *When manual channels are used, there will be an advisory that says \"Manual Channels\" in red in the upper left hand corner of any Live display.*
>
> **Note:** *Selecting channels from the summary or table displays will start a new command line.*

#### Select Channels From the Keypad

The keypad defaults to selecting channels. Channels may be selected on the control keypad using the [+] and / or [-] and [Thru] keys for consecutive or non-consecutive channel selection.

The following examples illustrate various methods of selecting channels from the control keypad:

-   [5] [Enter] - selects channel 5.

-   [5] [+] [7] [Enter] - selects non-consecutive channels 5 and 7.

-   [5] [Thru] [9] [Enter]- selects channels 5 through 9.

-   [2] [Thru] [8] [-] [5] [Enter] - selects a range of channels 2 through 8, except channel 5.

-   [-] [6] [Enter] - removes channel 6 from the current selection list.

-   [+] [1] [Enter] - adds channel 1 to the current list of channels.

> **Note:** *You may use [+] and / or [-] multiple times to add or remove multiple channels from the selection. [Thru] lists may be entered in ascending or descending order.*
>
> **Note:** *The [Thru] command uses the current flexichannel state. Channels not included in the flexichannel mode (except selected channels mode) are not collected in a thru range. [Thru] [Thru] can be used to collect all channels in the range, even if they are not in the current flexi mode. See Using Flexichannel (on page 106).*

##### Modifying a Terminated Channel Selection

It is possible to add or remove channels from a previously terminated command line. You will need to first press [+] or [-] and then you can add to or remove from your current channel selection. This includes selecting channels from the direct selects, summary view, and Magic Sheets.

##### [Next] and [Last]

The [Next] and [Last] buttons increment and decrement channel selection. If only one channel is selected, [Next] increments the channel selection to the next sequential channel, while [Last] decrements the channel selection by one.

> Select channel 10 then change the selection to channel 11 using the [Next] key:

-   [1] [0] [Enter]

> Channel 10 is selected with a gold outline around the entire channel and the channel number is indicated in white.

-   [Next]

> Channel 11 is now selected with a gold outline and white channel number while channel 10 is no longer selected.

When a group of channels is selected, pressing [Next] or [Last] selects the first or last channel in the channel list.

> Channels 11 through 20 are selected:

-   [Next]

> Channels 11 through 20 are still the specified channel list but only channel 11 is selected for control. You can now sequentially press [Next] or [Last] to cycle through the list. Press [Select Last] to reselect the entire range.
>
> **Note:** *[Next] and [Last] work with the current flexichannel state. See Using Flexichannel (on page 106)*

#### Using Groups as a Channel Collector

[Group] can be used as a quick way to collect channels from submasters, cues, palettes, or presets. See*About Groups (on page 274)*.

The following actions are possible:

-   [Group] [Cue] [1] - selects all the channels in cue 1.

-   [Group] [Sub] [3] - selects all the channels in submaster 3.

-   [Group] [Int Palette] [5] - selects all the channels in intensity palette 5.

#### Offset

> **Note:** *On non-Apex Eos Family consoles, {Offset} is a softkey.*

[Offset] can be used to select a range of channels from a broader channel selection prior to storing groups, submasters, presets, palettes, effects, and using park.

##### Options

When [Offset] is pressed, a channel distribution display will open.

![](media/media/image228.png){width="3.6886712598425198in" height="1.405207786526684in"}

The following options are available as extensions of [Offset]. Options can be used together. These extensions can be used to create *Subgroups (on page 275)*. To close the offset display, press {Close}.

###### Direction

-   {Reverse} creates a group with the channels in the reverse order that they were selected in.

-   {Mirror In} creates subgroups of channels that mirror inward.

    -   [1] [Thru] [8] {Mirror In} [Enter] would create 4 subgroups in this order: (1,8) (2,7)

> (3,6) (4,5)

  -----------------------------------------------------------------------
  Ch 1     Ch 2     Ch 3     Ch 4     Ch 5     Ch 6     Ch 7     Ch 8
  -------- -------- -------- -------- -------- -------- -------- --------
  X                                                              X

           X                                            X        

                    X                          X                 

                             X        X                          
  -----------------------------------------------------------------------

-   {Mirror Out} creates subgroups of channels that mirror outward.

    -   [1] [Thru] [8] {Mirror Out} [Enter] would create 4 subgroups in this order: (4,5) (3,6)

> (2,7) (1,8)

  -----------------------------------------------------------------------
  Ch 1     Ch 2     Ch 3     Ch 4     Ch 5     Ch 6     Ch 7     Ch 8
  -------- -------- -------- -------- -------- -------- -------- --------
                             X        X                          

                    X                          X                 

           X                                            X        

  X                                                              X
  -----------------------------------------------------------------------

-   {Random} creates a random order to the channels.

###### Grouping

-   {Chan Per Group} creates a specified cluster of channels.

    -   [1] [Thru] [1][2]{Chan Per Group} [3] [Enter] would create these 4 subgroups of 3 channels each: (1,2,3) (4,5,6) (7,8,9) (10,11,12).

-   {InterLeave} creates a number of distributed sets of channels, that are not clustered together.

    -   [1] [Thru] [1][2]{Chan Per Group} [4] {InterLeave} [Enter] would create these 4 subgroups: (1,4,7,10) (2,5,8,11) (3,6,9,12).

    -   [1] [Thru] [5] [+] [1][1] [Thru] [1][5] [+] [2][1] [Thru] [2][5] {Chan Per Group} [3]

> {InterLeave} [Enter] would create these 5 subgroups: (1,11,21) (2,12,22) (3,13,23)
>
> (4,14,24) (5,15,25).

-   {Num Groups} creates a specified number of subgroups.

    -   [1] [Thru] [1][2]{Num Groups} [3] [Enter] would create these 3 subgroups: (1,2,3,4)

> (5,6,7,8) (9,10,11,12).

###### Spacing

-   {Jump} is used to skip over a specified number of channels.

    -   [1] [Thru] [1][2]{Chan Per Group} [3] {Jump} [1] [Enter] would create these 3 subgroups of 3 channels each: (1,2,3) (5,6,7) (9,10,11). Channels 4, 8, and 12 will be jumped over and will not be in the subgroups.

-   {Odd} selects only the odd numbered channels.

-   {Even} selects only the even numbered channels.

-   {Reorder} is used to reorder the channels of a group into numeric order.

##### Using Offset

For the offset feature to function, you must first select multiple channels, then press [Offset]. Choose from the options described above to modify your channel selection.

-   [1] [Thru] [10] [Offset] {Even} [Enter] - selects channels 2, 4, 6, 8, 10.

-   [1] [Thru] [2] [0] [Offset] [3] [Enter] - from the selected group, this syntax would select channels 1, 4, 7, 10, 13, 16, 19 which is an offset of every third channel from the selection.

-   {Group 5} [Offset] {Random} [Enter] - selects all channels in Group 5 and places them in random order. This selection may be used only temporarily or it may be recorded to a new Group.

-   [1] [Thru] [2] [0] [Offset] {Even} {Random} [Enter] - selects all even channels within the range and puts them in random order.

-   {Group 3} [Offset] {Reorder} [Enter] - reorders the channels in group 3 so they are in numeric order.

-   [Offset] [4] [Enter] - selects every fourth channel in the current channel selection.

-   [1] [Thru] [2] [4] [Offset] [4] [/] [4] [Enter] - selects channels 4, 8, 12, 16, 20, and 24. You can select to offset by 2/2, 4/4, 3/3 etc.

-   [Record] <Cue> [1] [Thru] [Thru] [1] [0] [0] [Offset] [10] [Enter] -

> records cues with numbers between 1 and 100, offset by 10 (cue 1, 11,
>
> 21, 31\... 91).

[Offset] can be used more than once to apply different offset commands to different channel selections on one command line.

-   [1] [Thru] [20] [Offset] [Even] [+] [60] [Thru] [80] [Offset] [3] [Enter] - selects all even channels between 1 and 20, and all odd channels between 60 and 80.

-   [1] [Thru] [10] [Offset] [2] [+] [20] [Thru] [30] [Offset] [Jump] [1] -

> channels 1-10 are offset by 2 (1,3,5,7,9) and 20-30 are jump 1 (20, 22,
>
> 24, 26, 28 ,30).

[Offset] can also be used to select steps and actions in an effect.

-   [Effect] [1] [Step] [1] [Thru] [20] [Offset] [Even] - selects all even steps between 1 and 20 in stepbased effect 1.

-   [Effect] [2] [Action] [1] [Thru] [7] [Offset] [Odd] - selects all odd actions between 1 and 7 in absolute effect 2.

#### Select Channels From the Direct Selects

Direct selects provide one-touch selection of channels, groups, palettes, presets, effects and macros. You can configure an array of channels on direct select that display with paging buttons provided for easy scrolling. See *Direct Selects (on page 113)*

Open a direct select display by selecting {Direct Selects} from the Home Screen and then select the {Channels} button. When channels are posted to the direct selects, you can select one simply by pressing the channel's touchbutton. The command line will show the appropriate channel and the selected direct select will be outlined in yellow.

> ![](media/media/image229.png){width="5.003333333333333in" height="3.5961450131233597in"}

Channel selection from the direct selects is an additive process. When a channel is selected, it is added to the current selection set. To select only one channel and deselect all others, double-press the channel touchbutton.

-   If channels [1] [Thru] [5] are selected from the keypad, pressing

> {Channel 6} from the direct selects adds channel 6 to the current channel selection.

-   If channels [1] [Thru] [5] are selected from the keypad, pressing

> {Channel 6} {Channel 6} deselects channels 1 through 5 and selects
>
> channel 6.

The following examples illustrate the various methods of selecting channels using the direct selects:

-   {Channel 1} - adds channel 1 to the currently selected channels, if not currently selected.

-   This is similar to pressing [+] [1] [Enter] from the keypad. However if channel 1 were currently selected when you pressed {Channel 1}, this would deselect channel 1 from the channel selection.

-   {Channel 5} {Channel 6} - adds channels 5 and 6 to the current channel selection.

-   This is similar to pressing [+] [5 [+] [6] [Enter] from the keypad.

-   {Channel 5} {Channel 5} - selects channel 5 and deselects all other channels.

-   This is similar to pressing [5] [Enter] on the keypad, when the previous instruction is terminated.

#### Deselecting Channels

Channels are deselected when any action is taken on the keypad that is unrelated to manual control, such as recording groups and cues, or updating a record target, etc. You can also press [Clear] after a terminated command line to clear the channel selection.

> **Note:** *[Select Last] is a fast way to regain your last channel selection. See Select Last (on page 269). Not available on Element Classic.*

Any manual control action taken while record or update is on the command line will automatically reselect your last channel selection.

### Setting Intensity

Channel intensity may be manually entered from the keypad, set with an intensity palette (if programmed) or set with a level wheel. Pressing [At] after channel selection assumes an intensity value will be added to the selected channels. You may also use the [Full] button to bring the selected channels to their full intensity or you may use the [Out] button to fade the intensity out.

Use the [Level], [+%], and [-%] keys to affect the intensity value of selected channels. Each of these keys are set at a specific value established in the Setup (*Manual Control (on page 221)*).

-   [Level] is set by default to 80%.

-   [+%] and [-%] are each set by default value of 10 points.

The following examples illustrate the various methods of setting intensity:

-   [1] [+] [3] [At] [5] <0> [Enter] - selects channels 1 and 3, and sets an intensity level of 50%.

-   [1] [Thru] [5] [-] [4] [Full] [Enter] - selects a range of channels 1 through 5, except channel 4, and sets the intensity to full.

-   [1] [Thru] [8] [At] [+] [3] <0>[Enter] - adds 30% to all intensities in the channel selection. If they were at 50, they will now be at 80. If channels 1, 3 and 5, were at 30 and 4 was at 50, they would be 60% and 80% intensity, respectively.

-   [5] [Thru] [8] [At] [/] [3] <0> [Enter] - scales the intensities of the selected channels in the list down 30% of their current values.

-   [1] [Thru] [4] [At] [/] [1] [3] [0] [Enter] - scales the intensities of the selected channels in the list up 30% of their current values. If channels 1 through 4 were at 40% intensity, this would scale them up by 30% to a value of 52.

-   [2] [+] [5] [level wheel] - roll the wheel up for greater intensity or down for less intensity.

-   [1] [Level] - selects channel 1 and sets it to the level as established in Setup.

-   [Group] [9] [Out] - selects all channels in Group 9 and sets the intensity values for those channels to zero.

-   [1] [0] [At] [At] - selects channel 10 and sets an intensity level as established in Setup.

-   [1] [Full] [Full] - selects channel 1 and sets it to full and self terminates the command line.

-   [1] [At] [/] [/] [2][3][9] [Enter] - puts channel 1 at DMX value 239.

    -   [1] [Thru] [5] [Full] [Enter]

> The selected channels are highlighted in gold, with white channel text and red intensity values (indicating manual data). You may continue to modify channels 1 through 5 since they are still selected and displayed on the command line.

-   [-%] [-%]

> This command would reduce the intensity of channels 1 through 5 by 20%. This command is self-terminating.
>
> On Element Classic, you will need to use [Shift] & [-] [Shift] & [-].

You can continue manipulating the selected channels so long as the channels are selected and displayed on the command line.

### Manual Control of Non-Intensity Parameters

Non-intensity parameters (NPs) can be set with a variety of controls including the control keypad, buttons on the central information area (CIA), and encoders or ML Controls.

#### Using the Parameter Display

The parameter display in the CIA is populated with only those parameters that are found in the patched devices. As channels are selected, the parameter display will change to show only parameters relevant to the selected channels.

The parameters are divided into the following categories: Intensity, Focus, Color and Beam. Each parameter category is represented with buttons in the parameter tiles. These buttons allow you to select the entire collection of all parameters within that category. You can also select a single parameter from a category using that parameter's button in the parameter display.

Beam has three subcategories: {Form}, {Image}, and {Shutter}. These subcategories are represented with buttons in the CIA. Pressing these buttons allows you to select all parameters within those subcategories. On consoles with encoders, these subcategories correspond to the way the encoders are mapped.

![](media/media/image230.png){width="3.380272309711286in" height="2.0467705599300086in"}

Within the CIA, in the upper left corner, notice the {All NPs} button. When pressed, this collects all non-intensity parameters for further editing.

Some examples of using parameter touchbuttons are:

-   [1] {Iris} [5] [Enter] - Places the iris parameter of channel 1at 50%.

-   [Group] [4] {Zoom} {Edge} [Out] [Enter] - Sends any zoom and edge values for all fixtures in group 4 to their home value.

-   [1] [Thru] [3] {All Speed} [At] [2][5][Enter] - Sets all the available speed parameters for channels 1 through 3 to 25.

#### Setting Parameters with the Keypad

When the CIA is placed in parameter mode, all parameters of selected channels may be given numeric values through the keypad.

When no channels are selected, the CIA shows all of the parameters that are available in the lighting system. When channels are selected, the CIA condenses to show only the parameters that are appropriate to the selection set. If channels are selected that have different device types, such as spot and wash lights, the CIA will show all of the available parameters.

The following examples illustrate how to set parameter values with the keypad:

-   [5] {Iris} [5] {Zoom} [6] [5] {Edge} [5] [Enter] - sets channel 5 to an iris value of 50%, a zoom value of 65%, and an edge value of 50%.

> **Note:** *Pressing [Shift] & [Encoder Paging Key] will place the associated parameter onto the command line for numeric entry. Not available on Element Classic.*

Using [At] [/] [/] will place the direct DMX value on the command line. For example, [1] [At] [/] [/] [2][3][9] [Enter] would put channel 1 at DMX value 239.

You can also set a channel\'s parameter levels with the DMX value by using [/][/].

-   [1] {Pan} [/][/] [2][5] [Enter]

You can add or subtract from the DMX value by using [+] or [-].

-   [1] {Pan} [/][/] [+] [5] [Enter]

-   [1] {Pan} [/][/] [-] [7][5] [Enter]

> **Adjusting Parameters Using [+] and [-]**

[+] and [-] can be used to adjust parameters from the command line. When using [-], you will need to preface the command with [+] if you want to remove from the current value.

-   [Channel List] {Pan} [1][0] - sets to 10 degrees.

-   [Channel List] {Pan} [+] [1][0] - adds 10 degrees.

-   [Channel List] {Pan} [-] [1][0] - sets to -10 degrees.

-   [Channel List] {Pan} [+] [-] [1][0] - removes 10 degrees.

#### Setting Non-Intensity Parameters with the Encoders

> **Note:** *On Eos Family consoles without physical encoders, virtual encoders can be accessed via the ML controls display. See Moving Light Controls (on page 128).*

Encoders provide a quick method to adjust current values for non-intensity parameters. See

> *Encoders (on page 122)* .

-   Eos Apex and Eos Ti - the bottom two encoders always control pan and tilt functions. The four vertical encoders are pageable using the encoder page buttons near the encoder LCD.

-   Gio, Gio @ 5, and Ion Xe - the four horizontal encoders are pageable using the encoder page buttons directing under the encoders

-   Ion Classic - the four encoders are pageable using the six encoder page hardkeys to the upper right of the encoder LCD

Form, Image, and Shutter are subcategories within the broader parameter category of Beam.

-   Custom - includes intensity and intensity MSpeed

-   Color - includes all color mixing controls (CMY, RGB, HS), as well as scrollers, color wheels, and color effects

-   Form- includes parameters that affect the quality or size of the light output, such as edge, zoom, iris, IMF, frost, etc

-   Image - includes anything that drops into the gate, such as gobos, effects wheels, etc

-   Shutter - includes all of the framing devices for the luminaire

> **Note:** *Pressing [Shift] & [Encoder Page Key] will post that parameter to the command line. For example, pressing [Shift] & [Color] would place Color on the command line.*

##### Encoder Display

> **Note:** *On Eos Family consoles without physical encoders, virtual encoders can be accessed via the ML controls display. See Moving Light Controls (on page 128).*

On Eos Apex and Eos Ti consoles, the encoder display LCD to the left of the encoders indicates the parameters they control and provides additional information about the current status of those parameters. See *Eos Ti Encoder Display (on page 122)*.

On Gio, Gio @ 5, and Ion Xe consoles, the *Mini Encoder Display* indicates the parameters the encoders control and provides additional information about the current status of those parameters. To see additional encoder information, use the [Encoder Display] button to open the encoder display. See *Encoder Controls Display (on page 124)*.

On Ion Classic, the encoder LCD displays the active parameter category loaded on the encoders, as selected by the page buttons. To see additional encoder information, open the Encoder Display by using CTRL + ALT + \ on an alphanumeric keyboard. ALT + , can be used to change encoder pages.

> **Note:** *For ETCnomad, RPU, and RVI, the encoder display can be accessed by using CTRL + ALT + \ on an alphanumeric keyboard. ALT + , can be used to change encoder pages.*

Encoder pages populate with parameters relevant to fixtures in the show patch. When you access a parameter page, controls that are not available for selected channels are suppressed.

> **Note:** *Flexi encoders is used to suppress parameters not applicable to the selected channels. This is used by default for the encoder display. See Flexi Encoders (on page 126)*

Each encoder has an associated control section that provides visual indication of:

-   the parameter it controls.

-   the current setting (value) of the parameter.

-   and the current mode if the encoder controls more than one function.

###### Coarse/ Fine

Allows for control of "coarse" (8 bit) or "fine" (16 bit) control. Default is coarse control. You may toggle between the two by pressing [Shift] while moving the encoder.

-   Coarse - provides larger changes for non-segmented parameters and advances/decrements full frames for segmented parameters. The encoder is clutched in this mode, meaning you will feel each frame change distinctly.

-   Fine - provides unlimited, high granularity control. When used in this mode the encoder is not clutched, allowing you smooth and detailed control.

###### Encoder paging

The number of encoder pages for each category will display.

-   Eos Apex and Eos Ti - displayed in blue at the top of the LCD display.

-   Gio, Gio @ 5, and Ion Xe - displayed at the bottom of the parameter category softkeys.

-   Ion Classic - the number of pages for each category is displayed at the right of the LCD.

You can go directly to the page required by pressing the encoder page button and a page number. For example:

-   [Form] & [3] - this will take you to the third page of the form category.

Information in the encoder display is only as accurate as the patch information for that channel. For example, when you are working with color scrollers, the standard manufacturer color frames will be displayed for scroller controls unless you have created a custom scroll for the selected channel in patch using the Scroll Editor.

When you have created a new scroll or wheel in patch for any channel and that channel is selected, that information will be displayed in the associated encoder display. See *Using the Editor (on page 176)*

When you access a parameter page, the encoders will automatically load and display the first page that has a valid parameter for the selected channels.

##### Encoder Softkeys

A series of buttons are included in each of the four encoders sections of the display including

{Home}, {Last}, and {Next} or {Min} and {Max}, and depending on the type of parameter, a

{Mode}, {Expand}, or {Calibrate} button.

> **Note:** *To access these softkeys at any time, press down on an encoder.*

###### Home

Each parameter has an associated {Home} key in the encoder LCD. This accesses any parameter and returns it to its default position. Additionally, the control keypad has a [Home] key located below [Sneak]. See *Home (on page 259)*.

###### Min and Max

{Min} and {Max} are displayed when the parameter is linear, such as a shutter. Use these keys to set a minimum and a maximum setting for a parameter.

###### Next and Last

{Next} and {Last} are displayed when the parameter is segmented such as a fixed gobo or color wheel or a color scroller. Use these keys to increment or decrement in full frames.

###### Mode

The {Mode} key is provided to select different modes for the encoder wheel such as rotate, index, or special effects.

-   When more than two modes are available, the {Mode} key can be pressed repeatedly, advancing through the various modes. Each mode will display beneath the current parameter setting.

-   When only two modes are available, the alternate mode is indicated instead of a {Mode} key. Toggling that button switches the encoder wheel to the alternate mode.

###### Expand

Some parameters will have an {Expand} button, which indicates that this parameter has "Expanded" functions. When that button is pressed, the display repaints to display all the media settings available for the specific wheel.

###### Flip

The {Flip} button, as displayed in the Pan/Tilt section of the encoder LCD, is used to flip the unit into its exact same position, but from the other direction. Depending on the current values of pan and tilt, there may be multiple flips.

This allows you to correctly focus a fixture that may be at the end of its pan or tilt range or to correct a fade that may be moving in an undesired direction.

The following example illustrates the use of {Flip}:

-   [channel list] {Flip}

###### Trackball On/Off

The {Trackball On/Off}, as displayed in the Pan/Tilt section of the encoder LCD, is used to give pan and tilt functionality to a mouse or trackball device.When this function is turned on, above the CIA will be a message saying "Cursor as Pan/Tilt".

Left-clicking the mouse will exit trackball mode.

###### XYZ Format Enable / Disable

Toggles between storing position data in pan / tilt format and XYZ format for use with Augment3d.

##### Form Control

> **Note:** *Not available on Element Classic.*

Form (a subcategory of Beam) collects the parameters that affect the quality of the beam, including the iris, edge, frost, etc. 'Shutter' and 'Image' are the other two subcategories of Beam

When the form encoder page button is selected, the LED will illuminate and the encoders automatically populate with the "Form" parameters as specified in the show patch. If there are more parameters in the show patch than will fit on the first page of the encoders, press the [Form] button again to page through the remaining parameters in the category or press [Form] and a page number to jump to a specific page.

The form parameters may include:

-   Edge - controls the hard/soft qualities of a spot luminaire. While some fixtures may call this parameter "focus", it is always represented as "edge" in Eos, to avoid confusion with "Focus" which refers to pan and tilt data. These values are set to the system default value for the selected luminaire, but may be modified as required on a per fixture basis

-   Iris, Zoom, Strobe and IMF- each parameter has in/out, narrow/wide, or fast/slow settings. Iris and Zoom also have programmable limits, called in/out and narrow/wide respectively. The strobe mode setting varies based on the fixture type.

##### Image Control

Image is the collection of parameters that affect the contents of the beam (gobo, prism, effects wheel, etc.).

##### Shutter Control

Pressing the [Shutter] button displays shutter controls, if there are any fixtures with framing devices patched.

> **Note:** *For Ion, ETCnomad, RPU, and RVI, the encoder display can be accessed by using CTRL + ALT+ \ on an alphanumeric keyboard. ALT + ,can be used to change encoder pages.*

###### Shutter Graphic

Tap or click on the shutter graphic to open up the shutter controls window.

The shutter controls window allows you to move individual shutters by holding down one of the letters inside of the shutter graphic. To rotate the shutters, use the <A>, <B>, <C>, or

<D> buttons around the outside of the shutter graphic.

![](media/media/image231.png){width="3.8713845144356958in" height="1.605207786526684in"}

###### Encoder Buttons

> **Note:** *The encoder buttons are used with the encoders for shutter control. These buttons do not work with the shutter graphic control.*

The following buttons are available for shutter control:

-   Angle Home - sets the angle of all of the shutters to their home position.

-   Thrust Home - sets the thrust (how far in or out of the beam the shutter travels) of all of the shutters to their home position.

-   Pair AC - pairs the A and C shutters together so they move together.

-   Pair BD - pairs the B and D shutters together so they move together.

-   Pair All - pairs all of the shutters so they move together.

-   Inverse AC - pairs the A and C shutters so they move in the opposite directions from each other.

-   Exceed Limits - ignores the limits angle and thrust place on each other, prioritizing whichever parameter is adjusted, regardless of the impact on the other.

-   Inverse BD - pairs the B and D shutters so they move in the opposite directions from each other.

-   A>D - sets the encoders to use the custom encoder pages for the shutters. Thrust for all of the shutters is on one page, Angle for all is on another page.

##### Color Control

Depending upon the specific device, color can be established manually with the encoders using:

-   CMY color-mixing

-   Hue and saturation color mixing

-   RGB color-mixing

-   Selection from a color wheel or scroller

-   CIE color picker tool

> ![](media/media/image232.jpeg){width="5.799040901137358in" height="1.7159372265966755in"}
>
> You may also specify color by using the full color picker on [Tab] [2] [7]. See *Using the Color Picker (below)*.

It is also possible to set non-intensity parameter data with direct entry using the control keypad and using the parameters on the CIA.

-   [1] [At] [4] <0> {Cyan} [5] [5] [Enter]

The first page of the color encoder will provide some scroller control, such as frame selection, on the top encoder. The next three encoders will control HS, CMY, or RGB color mixing. There will be buttons on the first page for switching between HS, CMY, and RGB. The HS controls will include buttons for {Home}, {Min}, and {Max}. The CMY and RGB controls include buttons for {Home} and {Max} for each of the parameters. No {Min} button will be displayed.

> **Note:** *Color scroller data will display on the encoders and displays as frame numbers, F1, which would be frame 1, F2 for frame 2, etc. F1.5 is halfway between 1 and 2. F2+ will display if the frame is less than 2.5 and F2- if the frame is greater than*
>
> *1.5. After the frame number, the gel number will also be displayed. This is also true for color and gobo wheels.*
>
> **Note:** *Frame numbers can be used from the command line. [2]{Scroller}[5][Enter] will send channel 2's scroller to frame 5. Frames can also be selected by using the DMX value for that frame. Pressing [/] twice will post DMX to the command line. [3]*
>
> *{Scroller} [/][/][2][5][5] [Enter] will send channel 3's scroller to the frame with the DMX value of 255.*
>
> **Note:** *Dual scroller fixtures are addressed as 0-100% instead of by frame numbers. You may need to update your fixture before this feature will work. See Update Profile (on page 193)*

##### Custom Control

Pressing the {Custom} button enables custom encoder mode. For more information, see

> *Custom Encoder Maps (on page 126)*.

#### Using the Color Picker

> The color picker can be opened from the *Workspace Layout Menu (on page 90)* or by using [Tab] [2][7].
>
> With the color picker open, you have the choice between six different *Color Spaces*, a *Gel Picker*, *Color Path*, *Tinting Tools*, and *Spectrum Tools*.
>
> ![](media/media/image233.jpeg){width="2.162269247594051in" height="1.6783333333333332in"}

Settings can be enabled or disabled for this tab via the gear icon at the left of the tab bar, or via the tab\'s submenu at the bottom of the *Tab Tools (on page 88)* context menu.

##### Color Spaces

When the color picker is first opened, the CIE xy color space and the gel picker will open by default. You can select other color spaces and tools via the display configuration tool (the gear icon) in the bottom left corner of the tab bar, or by right-clicking on the tab.

> **Note:** *Multiple color picker tabs with different color spaces can be opened at the same time. Multiple color spaces can be opened on the same tab.*

The available color spaces are:

![](media/media/image234.jpeg){width="4.997229877515311in" height="3.7583333333333333in"}

> **Note:** *When a fixture is in HS mode, the brightness control is not provided. Intensity controls the brightness.*

The cone in the CIE xy (CIE 1931) and CIE uv (CIE 1976) spaces represents the color spectrum that we can see.

###### Color Space Controls

Each color space has three virtual encoders, a vertical encoder, a {?} button, and a {\^} button.

The encoders will change based on the color space selected. Double tapping in a virtual encoder will cause it to jump to the location of your finger. Pressing and holding will cause the encoder to fade toward your finger.

Tapping anywhere in the color space will cause the crosshair to move to that location. Press and hold, then move your finger to fade the crosshair toward that location.

The {\^} button will create the brightest version of the selected color. Press the {?} button to display labels on all of the controls.

![](media/media/image235.png){width="3.1351706036745406in" height="1.9079166666666667in"}

For the RGB and CMY color spaces, you can change which color control is on the vertical encoder. Touch the label of the virtual encoder to change which color control is located on the vertical encoder. In the following graphics, Red is on the vertical encoder in the first one and green is on the vertical encoder in the second one. This is also indicated by the highlighted encoder name.

The vertical encoder in the HS Wheel and HSB color spaces always controls brightness.

####### CIE xy Control

CIE xy control is available via virtual parameters. \"CIE X\" and \"CIE Y\" can be put on the command line either via the associated parameter tiles or the {x} and {y} buttons in the CIE xy color space. This allows you to define specific values for x and y.

> **Note:** *CIE x and y are measured from 0-1. If whole-number values are entered, they will be automatically translated to the relative decimal amount; for example, \"43\" would become \"0.43.\"*

###### Automatic Color Control

Eos automatically creates a virtual control gamut for any additive color parameters contained in a fixture profile, including virtual hue and saturation (see {Create Virtual HSB} under Setup

-   System > *System (on page 212)*). This means a fixture with any emitter combination can be used with the controls available in the above color spaces; for example, two-color warm and cool white light fixtures.

Regardless which of the six color spaces you work in, Eos will translate the information to work with your fixtures.

##### Gel Picker

When the gel picker is opened up with a color space, dots will display on the color space. These dots represent the gels in the currently selected gel book. Hovering over a dot with a mouse will display the gel\'s name and a color swatch.

![](media/media/image236.png){width="3.9617661854768156in" height="2.5689577865266844in"}

The following buttons are also available:

-   {Brightest} - determines the color match used. This is helpful when working with fixtures that have more than three color components, such as RGBA, RGBWm or ETC\'s fixtures. Pressing {Brightest} or [Shift] +a gel from the picker will cycle through the three modes.

    -   {Brightest} - matches to the brightest match of that chromaticity.

    -   {Spectral} -matches to the best spectral match chromaticity. However, this mode can remove a lot of the intensity. This is based off of a 575w long life Source Four^®^.

    -   {Hybrid} - halfway between the brightest and the best spectral match. In the channel display, a single dot shows best spectral match, 2 dots indicates hybrid, and no dot shows brightest.

-   {Sort Hue} - takes the selected gel library and sorts it by hue instead of by gel number.

-   {Similar} - will show gels that are in the same selected area of the color picker. Only gels in the same selected gel book will display. You can switch to another gel book though to discover gels in that area.

-   {Show Gels as Gel Against White Background} displays the raw gel color as it would look against a white background. This option toggles with {Show Gels as Gel + Lamp Output}.

-   {Show Gels as Gel + Lamp Output} displays the gel swatch color as if it was being used with a tungsten lamp.

-   {Show} - displays all of the static gels in the show file. This populates from Patch.

-   {Standard Colors} - shows a range of White Point from 2700K to 6500K. Also shown are colors located around the cone and variations of those colors at 25% increments.

###### How the Gel Picker Affects Scroller and Color Wheel

When possible the gel picker will select the closest gel as defined in a scroller or color wheel.

> **Note:** *Some devices contain manufacturer specified gel mixes, and will only allow selection from the Gel Picker of the exact gels in their list.*

The channel display will show the frame number and the corresponding label that is defined for that frame.

##### Tinting Tools

> The Tinting Tools option is found by right-clicking on the Color Picker tab (*Using the Color Picker (on page 253)*).

![](media/media/image237.png){width="1.0588648293963254in" height="1.9723950131233596in"}

Tint allows you to easily adjust color regardless of the color space that you\'re working in.

You can increase or decrease the saturation and brightness. You can make a color warmer or cooler, and you can add or remove colors.

##### Color Path

Color path is a option for controlling color fades between cues. By default, color fades happen in the native space of the fixture. If you want a fade that resembles a fade in a different color space, you can do that using color paths. There are eight preprogrammed color paths, and you can also record your own . Up to 1000 color paths are supported.

To open the color path display, click on the gear icon in the color picker display and select Fade. You can open the color path list display by pressing [Path] [Path] (if available), by pressing the {Color Path} icon in the home screen, use [Tab] [3][3], or from the CIA by going to Browser > Record Target List > Color Path.

Color paths are selected either by clicking on the drop down above the color path or by using [Path] [n]. Ion Classic and Element Classic users will need to use {Color Path}.

> **Note:** *Channels involved in the fade have to be selected before you can choose or modify a color path.*

The color path display has a drop down list of the available paths, a color path preview bar, and control buttons. An indication line will display on the color space to show the color fade.

![](media/media/image238.jpeg){width="5.11055227471566in" height="2.181457786526684in"}

Available control buttons are:

-   ![](media/media/image239.jpeg){width="0.8645833333333334in" height="0.3020833333333333in"}

    -   replays the color fade using the cue time.

-   ![](media/media/image240.jpeg){width="0.875in" height="0.2916666666666667in"}

    -   replays the color fade using the Go to Cue time from Setup.

-   ![](media/media/image241.png){width="0.875in" height="0.2708333333333333in"}

    -   replays the color fade in five seconds.

-   ![](media/media/image242.png){width="0.875in" height="0.2604166666666667in"}

    -   replays the color fade in ten seconds.

-   ![](media/media/image243.png){width="0.875in" height="0.28125in"}

    -   pauses the color fade.

-   ![](media/media/image244.png){width="0.875in" height="0.28125in"}

    -   plays / resumes the color fade.

-   ![](media/media/image245.png){width="0.875in" height="0.2708333333333333in"}

    -   skips to the end of the color fade.

You can also click on the color path preview bar to scrub to any point along the fade.

Additional controls may be available based on the color path selected. For example, Color Path 7 has additional controls for Hue, Saturation, and Brightness. You can move those controls to adjust the fade, and you\'ll see a representation of those changes in both the color path preview bar and in the color space.

![](media/media/image246.jpeg){width="5.189430227471566in" height="2.2404166666666665in"}

Changes can be stored in the destination cue as absolute data by using [Update] or [Record]. When there\'s a change to the color path information, a red c will display next to the channel number and the color path\'s name will display in red in the color path display. When that data has been saved, a blue c will display. The color path\'s name will also display in blue in the color path display.

You can save changes to a new color path by using [Record] [Path] [n]. Ion Classic and Element Classic users will need to use {Color Path}.That data will then be referenced, and any changes made to that path will be used anytime that path is used. Press [Shift] & [Path] to see the values behind the referenced data, or [About] & {Path} for Ion Classic and Element Classic users.

> **Note:** *If multiple channels are selected that have different color paths assigned to them, a + will display by the color path name in the color path preview bar.*
>
> See *[[About] Color Path (on page 453)](#_bookmark451)* and *Patch > Attributes (on page 182)*.

##### Spectrum Tools

The Spectrum option is found by clicking on the display configuration tool (the gear icon) in the bottom left corner of the display tab bar.

This option displays all the color parameters across the color spectrum, and allows for individual control of each parameter. Press a color point to move it.

This display is a good visual of what the fixture is outputting.

The following screenshots show a 7 color fixture. This display will change based on the type of fixture being used.

> **Note:** *The gray line shows the composite color of the fixture. If multiple fixtures are selected, the gray line represents the first channel selected.*

![](media/media/image247.jpeg){width="3.1106496062992126in" height="1.4340616797900263in"}

With the *Gel Picker* open and a gel selected, a dotted line will appear in the Spectrum display. That line represents the selected gel.

![](media/media/image248.jpeg){width="4.8812390638670164in" height="2.5847911198600175in"}

{Hold Color Point} allows you to adjust individual emitters and the other emitters will automatically adjust to hold the color selected. This can only be used with fixtures that have more than three color parameters.

If you are working outside of this display, holding down [Color] while adjusting the encoders will cause Hold Color Point behavior.

### Home

As with the {Home} touchbutton on the Encoder Display (see *Home (on page 250)* ), the [Home] hardkey allows you to home a specific parameter. Additionally, you may home all of a channel's non-intensity parameters or home only a specific category (I, F, C, B).

Element Classic users will need to use the {Home} softkey located in the ML Controls. Homing a channel, category, parameter, or submaster will return it to the default value.

-   [1] [Home] [Enter] - homes all parameters for channel 1, except intensity.

-   [1] [Color] [Home] [Enter] - homes all color parameters for channel 1.

-   [Group] [1] [Color] [Focus] [Home] [Enter] - homes the color and focus parameters of all channels in group 1.

-   [Sub] [1] [Home] [Enter] - homes submaster 1.

-   [Sub] [1] [Thru] [Home] [Enter] - homes all submasters.

#### Home Preset

You can select a preset to provide home values for all non-intensity parameters (instead of fixture library default values) when home commands are used. Store a preset with modified home values for only the channel parameters you would like at a different value than default, and then assign that preset to Home in Setup (see *Home Preset (on page 213)*). Any channels that are not included in the preset assigned to Home in Setup will use their library defaults.

### Multiple Intensity Channels

When a fixture with multiple intensity parameters is patched, Eos assigns it a master intensity. The master intensity can be used to control the multiple intensities together. The master intensity is handled in the same way as the intensity of a single intensity channel.

Levels can be set via the level wheel, from the keypad, and the encoders (if available). The other intensities will default to 100%.

> Control of the individual intensities of a multiple intensity channel is handled using the parameter buttons in the CIA (see *Manual Control of Non-Intensity Parameters (on page 247)*) or the encoders (see *Custom Control (on page 253)*). Levels assigned to the individual intensities will act independent of each other and the master intensity.

-   [1][0][0] {Intens 3} [At] [5][0] - sets intensity 3 of channel 100 to 50% intensity.

-   [1][0][0] [At] [7][5] - sets the master intensity of channel 100 to 75% intensity. All intensities for channel 100 will be mastered to 75% unless they have a separate intensity set.

In Table view, Eos will default to showing all intensity parameters associated with the channels.

In summary view, the master intensity is shown. If one of the multiple intensities has a value, an '+' will display beside the master intensity.

### Multicell Fixtures

> Fixtures that have multiple same-type parameters can have a multicell profile assigned to them, as designated by MC in the fixture editor. See *Patching Multicell Fixtures (on page 173)*.

Multicell fixtures have a master channel with a whole number for a channel number and the appropriate number of additional cells, which will have point numbers for their channel numbers.

To control the whole fixture (master + cells), select the channel number. To control individual cells, use [.] to put {Cell} on the command line.

To control just the master, use [Shift] & [.] to put {Minus Cells} on the command line. You can also use the syntax [1] [.] [0] or [1] {Cell} [0] to only control the master.

To select the master and any or all of the cells, you can use the following syntax examples: [n] [.] [0] [Thru] [n], [n] [.] [0] [+] [n], or [n] [.] [0] [Thru] [n] [-] [n]. The {Cell} softkey can be used instead of the [.] hardkey.

> Channel 1 is a multicell fixture with four cells.

-   [1] [At] [Full] [Enter]

> Sets the intensity of the master channel to full. Note that the intensity parameter for cells defaults to full.

-   [1] [.] [1] [At] [5] [0] [Enter]

> Sets only cell one at 50% of the intensity of the master. Cells are a percentage of the master level. [.] puts cell on the command line.

This can be especially useful when applying effects or palettes.

> Channel 1 through 4 are multicell fixtures with four cells.

-   [1] [Thru] [4] [Color Palette] [1] [Enter]

> Sets channels 1 through 4 to color palette 1. All four cells of each fixture are set to color palette 1, which is red.

-   [1] [Thru] [4] [Color Palette] [1] [Thru] [4] [Enter]

> Channel 1 with its four cells will be set to color palette 1, channel 2 will be set to color palette 2, and so on.

-   [1] [Thru] [4] [.] [Color Palette] [1] [Thru] [4] [Enter]

> For each of the channels, cell 1 will be in color palette 1, cell 2 in color palette 2, cell 3 in color palette 3, and cell 4 in color palette 4.

With a cell selected you can apply data to the master channel as long as the cell does not also have that parameter. When you have selected a cell, if you apply data that does not apply to the master, Eos understands to apply it to the cells instead. In the example above, IF the master had color parameters, this action would apply color data ONLY to the master.

Cells will not send data to other cells. Table view is helpful for seeing which cells control what parameters.

> ![](media/media/image249.png){width="4.974757217847769in" height="3.2025in"}
>
> Cell 2 of a fixture is currently selected. You can adjust the encoders for pan and tilt even if the master actually controls those parameters. The cell will send that information to the master. This allows for greater ease of control.

The following are additional multicell syntax examples:

-   [5] [.] [2] [+] [+] - pressing [+] twice will put channel on the command line.

-   [5] [.] [Thru] - automatically puts the first cell\'s number on the command line before the [Thru] command.

-   [5] [.] [1] [Thru] [Enter] or [5] [.] [1] [Thru] [At] - automatically puts the last cell\'s number on the command line before a [Enter] or [At] command.

-   [5] [.] [-] [4] [Enter] - selects all of the cells except cell 4.

-   [1] [+] [+] [2] [.] [3] [Enter] - selects all of channel 1, and only cell 3 of channel 2.

-   [1] [+] [3] [.] [2] [Shift] & [.] - appending [Shift] & [.] after a cell number will post [All Cells] to the command line, selecting all cells of channel 1, and only cell 2 of channel 3.

> Offset can be very useful when applied to multicell fixtures, and can be useful for creating subgroups. See *Offset (on page 242)* and *Subgroups (on page 275)*.

### Lamp Controls

Lamp Controls (Tab 31) allow you to execute control functions of selected fixtures such as calibrate, douse lamp, strike lamp and reset. Each fixture type has its own set of lamp control options which are available to you when you select the fixture from Live and press the {Lamp Ctrls} softkey. This information is also available using [About] (see *Using About (on*

> *page 443)*).

-or-

-   [1] [1] [Enter] {Lamp Ctrls}

-   [1] [1] [Enter] [About] {Lamp Controls}

If the channel is a conventional (intensity-only) fixture, no control options will be displayed. When the selected channel is an automated fixture, options specific to the fixture type will display for use. Available RDM functions will also display here.

![](media/media/image250.png){width="2.1767727471566056in" height="2.197603893263342in"}

Pressing any of these control options will affect the selected channel after a confirmation.

### Using [+ % ] and [- % ]

Use [+%] and [-%] keys to incrementally change parameter values. Element Classic users will need to use [Shift] & [+] or [Shift] & [-].

> By default, the [+%] and [-%] keys are assigned a value of 10. This can be changed in Setup. See *Manual Control (on page 221)*.

#### Channel Intensity

> **Note:** *[+%] and [-%] are used in the examples below. Element Classic users will need to use [Shift] & [+] and [Shift] & [-].*

When channels are selected, pressing [+%] increments the intensity level by 10 (or by the value established in Setup, see *Manual Control (on page 221)*. Alternatively, you may press

[-%] to decrement the intensity level by 10. You may use these keys consecutively to "add to" or "subtract from" the intensity level.

> Select channels 1 through 10 and set them to an intensity level of 45% from the keypad.

-   [1] [Thru] [1] [0] [At] [4] [5] [Enter]

> Change the intensity level to 65% using the [+%] key, which is set to its default value of 10% in the setup menu.

-   [+%] [+%]

#### Non-Intensity Parameters

> **Note:** *[+%] and [-%] are used in the examples below. Element Classic users will need to use [Shift] & [+] and [Shift] & [-].*

The [+%] and [-%] keys may be used to incrementally adjust non-intensity parameters as well.

-   [1] {Iris} [+%] [+%]

-   {Zoom} [-%] [-%]

### Remainder Dim

> **Note:** *By default, [Rem Dim] will set to zero. In Setup, you can assign a remainder dim value of something other than zero. See Manual Control (on page 221). For the purposes of this discussion, the default value of zero will be used in examples.*

[Rem Dim] temporarily provides a zero intensity to all channels except those that are currently selected, those that are parked, or those with intensity contributions from submasters. If the remainder dim command is reversed, the stage returns to its previous state. You may use the following commands for remainder dim:

-   [Next] and [Last]- moves through the channel list.

-   [select channels] [Rem Dim] [Enter] - sets all non-selected channels to zero.

-   [1] [At] [6] <0> [Rem Dim] [2][0] [Enter] - sets channel 1 to 60% and all non-selected channels active over 20% to a rem dim level of 20.

-   [Rem Dim]- clears the rem dim function and returns the stage to its previous state

Pressing [Rem Dim] again releases all channels from rem dim mode and restores the stage to its previous state. Using the [Next] and [Last] buttons releases the current selected channel from remainder dim mode and sets its intensity to zero, while selecting the next or last channel and continuing rem dim operation.

> Assume channels 5 through 9 are selected and set at an intensity level of 50% and channels 10 through 15 are selected and set at an intensity level of 70%. Select channel 9 and dim the remaining channels.

-   [9] [Rem Dim] [Enter]

> Channel 9 is set at an intensity level of 50% and all remaining channels are dimmed to zero.

-   [Next]

> Selecting [Next] changes the channel selection to channel 10 which is set at an intensity level of 70%, the level set in the previous state, and all remaining channels including channel 9, are dimmed to zero.

-   [Rem Dim]

> Pressing [Rem Dim] again will return all channels to their previous levels.

[Rem Dim] can be used in groups including the use of [Next] and [Last] buttons to progress through the channels within the selected group.

> Assume you have group 1 selected (includes channels 1 through 10) with an intensity value of 50%, group 5 selected (includes channels 11 through 20) with an intensity value of 70%, and group 7 selected (includes channels 21 through 30) with an intensity value of 100%

-   [Group] [1] [At] [5] [Enter]

-   [Group] [5] [At] [7] [Enter]

-   [Group] [7] [At] [Full] [Enter]

> Select only Group 1 and dim the remaining Groups using the [Rem Dim] feature.

-   [Group] [1] [Rem Dim] [Enter]

> Channels 1 through 10 are selected with an intensity value of 50%, and all remaining channels are at a 0% intensity. You may progress channel by channel through the selected group (Group 1, channels 1 through 10) using the [Next] or [Last] key. Each press of the [Next] or [Last] key cycles you through only the channels of the selected group.
>
> Pressing any other key terminates the [Rem Dim] mode and leaves channels at their remainder dim value.

You can set the dim level for all remainder dim commands in Setup (see *Manual Control (on page 221)*). When set to a value other than zero, all rem dim commands will bring intensity to this level instead. However it won't bring an intensity up. For example, if the rem dim level in setup is set to 50%, [Rem Dim] will drop any value above 50% to 50%, but not add intensity to any channels below 50%.

It is possible to override the dim level temporarily by specifying a level after the [Rem Dim] command.

[Rem Dim] can also be used to remove channels from a submaster or cues during a [Record].

> Using [Rem Dim] You can modify which channels are recorded in the submaster. For this example, assume that channels 1 through 10 are at full. You've recorded that to submaster one.
>
> Using [Rem Dim], you can modify the record so only channels 1 through 5 are recorded to the submaster.

-   [1] [Thru] [1] [0] [At] [Full] [Enter]

-   [Record] [Sub] [1] [Enter]

-   [1] [Thru] [5] [Record] [Sub] [1] [Rem Dim] [Enter]

A [Rem Dim] command can also be used on a selective cue record. It will force any channels not included in the record, but that are tracking forward from a previous cue, to zero.

#### Rem Dim Values

Rem Dim levels can either be an absolute value, such as Full or 50%, or a proportional value, which would set the levels to a percentage value of their current levels. To use a proportional value, press [/] before entering the percentage value.

> Assume that channels 1 through 10 are selected and set to an intensity level of 60. Select channel 1 and dim the remaining channels.

-   [1] [Rem Dim] [/] [5][0] [Enter] Channels 2 through 10 will be dimmed to 30.

### Highlight and Lowlight

> **Note:** *[High] is used in the examples below. Ion Classic and Element Classic users will need to use {Highlight}.*

Channels selected while in highlight mode will either go to a default setting, or to a value provided by a highlight preset (established in setup, *Manual Control (on page 221)*).

Modifications can then be made to those channels. Any changes will be maintained when the highlight mode is removed.

To place Eos in highlight mode, press [High] [Enter]. The command line will show that highlight is currently in use.

If no highlight preset is established, or for channels that have no value stored in the highlight preset, the following values will be applied to channels as they are selected:

-   Intensity - full

-   Focus parameters - no change from present state

-   Color parameters - home value

-   Shutter parameters - no change from present state

-   Image parameters - home value

-   Form parameters - no change from present state

    -   [1] [Thru] [5] [High] [Enter] Places channels 1 - 5 in highlight.

    -   [Next]

> Specifies channel 1, which is now at the highlight value. Channels 2 - 5 are in the lowlight value. All other channels go to the defined rem dim level.
>
> You may assign both a highlight and a lowlight preset in setup (see *Manual Control (on*

*page 221)*). Any preset may be used. Channels with only one parameter included in the preset assigned to Highlight and Lowlight will not reset other parameters back to their default highlight values (see above).

On a command line with a channel selection, you can use [Shift] & [High] to go into Highlight mode and send the selected channels to the default Highlight setting. This command will self terminate the command line.

If you just use [High] , the command line will be cleared.

#### Lowlight Preset

The {Lowlight Preset}, which is set in Setup> User> Manual Control >Lowlight Preset, is used to define the behavior of specified but not selected channels while using [Next]/[Last] in highlight mode. When in highlight mode, [channel list] or [Group] [n] [Enter] [Next] will select the channel list or group and isolate the first channel.

-   [High] [Enter] [6] [Thru] [1][5] [Enter] [Next]

> Specifies channels 6 through 15 with channel 6 the only channel selected. 6 is at the highlight level and 7 through 15 are at their lowlight levels. Pressing [Next] again will put channel 7 at the highlight level and 6 plus 8 through 15 at their lowlight levels. If there is no lowlight preset, these channels are not affected.
>
> Ion Classic and Element Classic users will need to use {Highlight}.

#### Temporary Highlight Level

> **Note:** *[High] is used in the examples below. Ion Classic and Element Classic users will need to use {Highlight}.*

The highlight preset can be overridden by setting a temporary highlight level. Using [High] [At] [5][0] [Enter] overrides the highlight preset and sets the highlight level to 50. Non-intensity parameters are not affected and will use the default highlight setting or the highlight preset.

The temporary highlight level will remain until [High] is pressed again or the channel is no longer selected.

#### Highlight/Lowlight Rem Dim

In addition to the highlight and lowlight presets, there is also a setting for {Highlight Rem Dim} in Setup. See *Manual Control (on page 221)*. When enabled and highlight mode is active, the intensity for all non-selected channels are automatically set to the Rem Dim value established in setup, if that Rem Dim value is lower than the channel's current intensity. This can be used to help further isolate the channels you are working with in Highlight Mode

If you do not wish to enable Rem Dim globally in Setup, you can specify a rem dim on the command line for temporary use. Rem Dim will use the {Live Rem Dim}, as specified in setup. See *Manual Control (on page 221)*.

-   [High_Low] [Rem Dim] [Enter]

To temporarily override the {Highlight Rem Dim} option in Setup, you can use either of the following syntax examples:

-   [channel list] [Highlight] [Rem Dim] [n] [Enter]

-   [channel list] [Highlight] [Rem Dim] [/] [n] [Enter]

### Sneak

The [Sneak] command (when a destination is not provided) removes manual changes from selected channels and allows the channels to sneak back to their background states (cue or submaster instruction, if any).Sneaking channels to their previous state is similar to the Expression release function, except sneak has the ability to release in time.

If there is no background state from the playbacks, the channel parameters will be set to their home position. The sneak command follows the sneak timing default established in Setup (see *Manual Control (on page 221)*), unless a timing value is provided as part of the sneak command.

> The playback status display will show a red counter for sneak time. If multiple sneak times are being used, the most recently fired sneak time will be displayed. For an example of the sneak counter, see *Indicators in the Playback Status Display (on page 110)*.

The sneak command can also be used to send a channel parameter to a specific destination, either with or without timing. The following examples illustrate the various methods of using the sneak command:

-   [channel list] [Sneak] [Enter] - releases manual control, setting parameters to their background state. If there are current values for those parameters from a playback, those are the values that will be restored. If there are no values from a playback, the parameters are set to home (or default) position.

-   [channel list] [Color] [Sneak] [Enter] - sneaks color of the selected channels to the default or background state.

-   [5] [At] [5]<0> [Sneak] [8] [Enter] - sneaks channel 5 to 50% in 8 seconds.

-   [Sneak] [Enter] - when no channels are selected, restores all channels with manual values to their background state.

-   [Sneak] [Sneak]- puts {AllNPs} [Sneak] on the command line, which sneaks out all non-intensity parameters. [Sneak] [Sneak] is a self-terminating command.

-   [Sneak] <Time> [3] [Enter] - restores all channels with manual values to their background state in 3 seconds.

-   [Select Active] [Sneak] [Enter] - selects all channels with intensity above zero and restores them to their background state, using default sneak times.

-   [Group] [5] <Color Palette> [9] [Sneak] [Enter] - selects group 5 and sneaks it to color palette 9 using default sneak time.

-   [Group] [3] [At] <Color Palette> [1] [Sneak] <Time> [7] [Enter] - selects group 3 and sneaks it to color palette 1 in 7 seconds.

-   [Sub] [4] [At] [5] [0] [Sneak] [2] [Enter] - selects submaster 4 and sneaks it to 50% in 2 seconds.

> **Note:** *When recalling a reference from the direct selects to use with the sneak command, the sneak command has to be entered before the reference.*

-   [Chan][1] [Sneak] {Preset 1}- selects channel 1 and sneaks it to preset 1 using default sneak time.

-   [Chan][2][Sneak]<Time>[2]{Intensity Palette 3}- selects channel 2 and sneaks it to intensity palette 3 in 2 seconds.

-   [Shift] & [Sneak] - makes any manual data unmanual. The values will remain but they will no longer be available for [Update] or [Record Only] operations. When used with an empty command line, this will affect any and all manual data. When used with a channel selection, only those channels will be affected.

-   [1] [At] [5]<0> [Sneak] <Time> [8] [Delay] [5] [Enter] - sneaks channel 5 to 50% in 8 seconds after a delay of 5 seconds.

### Staging Mode

Staging Mode allows you to preview changes temporarily, and then either commit them to Live or Blind, or revert them.

#### Using Staging Mode

In either Live or Blind, enter Staging Mode by pressing [Staging Mode] or [Stage]. The command line will append \"Staging Mode.\" Make the desired changes. Staged data will display in orange.

> ![](media/media/image251.png){width="4.555845363079615in" height="2.082082239720035in"}

If an Augment3d tab is open, staged data will also preview there (for more information, see *Augment3d (on page 495)*). The physical [Stage] key LED will illuminate when in Staging Mode.

##### Committing Staging Mode Changes

Press [Copy To] [Enter] to commit changes to either Live or Blind. Additional modifiers can optionally be added to the syntax (for example, [Copy To] <Sneak> <5> [Enter]).

Pressing [Staging Mode] or [Stage] again will place \"Clear Staging Mode\" on the command line. Exiting Staging Mode will preserve the changes without committing them. Staging Mode changes preserved without committing them are stored in a buffer for use when Staging Mode is reentered. If the buffer has content when exiting Staging Mode, the [Stage] key LED will blink.

> **Note:** *Staging Mode changes committed to Live will display as manual data (red), and will still need to be recorded or updated into a cue.*

#### Staging Mode & Highlight

Highlight (see *Highlight and Lowlight (on page 266)*) can be used in Staging Mode in both Live and Blind. To enable, simply press [Highlight] while already in Staging Mode. To disable, select [Highlight] again, or exit Staging Mode.

### Select Keys

A number of select functions are available.

#### Select Last

The [Select Last] key allows you to reselect whatever the previous channel selection was. This includes multiple channel selections, groups, etc. Using [Select Last] , Eos will recall your last selection and leave it unterminated for further operation. This will work for a loop of the last five selections.

> **Note:** *On Ion Classic and Element Classic, {Select Last} is a softkey.*
>
> **Note:** *If any manual control action is taken immediately after a [Record], [Record Only], or [Update] command, the previously selected channels will automatically be reselected.*

##### [Shift] & [At] and [Shift] & [Enter]

-   [Shift] & [At] - recalls last channel(s) and parameters without terminating; does a loop of last five commands.

-   [Shift] & [Enter] - reselects the last command and leaves it unterminated; does a loop of last five commands.

#### Select All

Pressing [Shift] & [Select Last] will give the additional softkey option, {Select All}. {Select All} will select all channels.

#### Select Active

The [Select Active] key is used to select all channels that currently have intensity levels above zero. Pressing [Select Active] once will capture all active levels. Pressing [Select Active] twice will capture all active manual levels and those from playbacks except for submasters. Select NonSub Active will post to the command line.

The following examples illustrate the how to select channels using [Select Active]:

-   [Select Active] [Enter] - selects all active channels with intensity levels above zero.

-   [Select Active] [Record] [Group] [x] [Enter] - records active channels to the target group.

-   [Select Active] [Sneak] [Enter] - selects all channels with intensity above zero and restores manual control to the background state, using default sneak time, if enabled.

-   [1] [Thru] [1] [0] [0] [Select Active] [Enter] - selects channels between 1 and 100 with intensity levels above zero.

On a completed command line, using [At] or [Select Last] after [Select Active] or [Select Manual] will post the numeric channel list to the command line.

For example, cue 1 is active, and has channels 1 through 5 at full. Using the syntax, [Select Active] [Enter] [At] will post channels 1 through 5 onto the command line.

Another example, Channels 10 through 20 have a manual level of 75. Using [Select Manual] [Enter] [Select Last] will put channels 10 through 20 onto the command line.

> **Note:** *On Ion Classic and Element Classic, {Select Active} is a softkey.*

#### Select Manual

The [Select Manual] key is used to select all channels that currently have manual data. You may use [Select Manual] combined with the parameter control keys to capture only certain parameters of a channel with manual data.

The following examples illustrate the various methods to select channels using [Select Manual]:

-   [Select Manual] [Enter] - selects all channels with manual data.

-   [Select Manual] [Color Palette] [1] [Enter] - selects all channels with manual levels and sets them to color palette 1.

-   [Color] [Select Manual] [Color Palette] [1] [Enter] - selects only channels with manual color values and sets them to color palette 1.

-   [1] [Thru] [1] [0] [0] [Select Manual] [Enter] - selects channels between 1 and 100 with manual data.

-   [Select Manual] [Record] [Group] [n] Enter] - records channels with manual data to the target group.

> **Note:** *On Ion Classic and Element Classic, {Select Manual} is a softkey.*

#### [-] Select Manual or Select Active

[-] [Select Manual] or [-] [Select Active] can be used to modify channel selections. Using [-] [Select Manual] will select all of the channels in the list except those that have manual data. Using [-] [Select Active] will select all of the channels in the list except those that are active.

-   [1] [Thru] [2] [0] [-] [Select Manual] [Enter] - selects channels 1 through 20 except any channels that currently have manual data.

-   [1] [Thru] [2] [0] [-] [Select Active] [Enter] - selects channels 1 through 20 except any channels that are currently active.

### Channel Check

Channel check allows you to quickly step through all of your patched channels. This is useful for checking lamps or checking focus.

**Note:** *Parked addresses will not be affected by the channel check feature.*

The following examples illustrates how to use the channel check feature:

-   [1] [At] [7] <0> {Chan Check} [Enter] - brings channel 1 to 70% intensity.

-   [Next] - channel 1 returns to its background state and channel 2 is set to 70% intensity.

-   [Next] - channel 2 returns to its background state and channel 3 is set to 70% intensity.

Use [Next] or [Last] to progress through the channel list to complete the channel check. Any other key press other than [Next] or [Last] will terminate channel check mode.

### Address at Level

> **Note:** *[Address/Patch] is used in the examples below. Ion Classic users will need to use {Address}, and Element Classic users [Dimmer/Address].*

The [Address/Patch] key in Live is used to send level information directly to an output address.

-   [Address/Patch] [5] [Full] [Enter] - sets output address 5 to full. It will return to its previous level once the command line changes.

-   [Address/Patch] [2] [/] [1] [At] [/] [2][3][0] [Enter] - sets universe 2, address 1 at DMX value 230.

With [Address/Patch] on the command line, you can use the level wheel to adjust the level.

After using the [Address/Patch] command, [Next] and [Last] may be used to increment the address number and set it to the same level.

Addresses return to their previous level once the command line is cleared, or [Next] / [Last] is used to increment to the next address.

> **Note:** *This feature is useful when you want to perform an address or dimmer check.*

### Address Check

Address check allows you to quickly step through all of your patched addresses.

Address check differs from *Address at Level (on the previous page)* because it skips non-intensity parameters of patched addresses. Since address check follows the current flexichannel state, it can be used with all channels to identify unpatched channels, or with flexi-patched to only show the intensity addresses of patched channels.

> Use the appropriate hard or softkey to select addresses based on your console: [Address/Patch], {Address}, or [Dimmer/Address].Then, add the syntax [1] [At] [Full]
>
> {Check} [Enter] to bring address 1 to full intensity.

Use [Next] or [Last] to progress through the address list to complete the address check. Any key press other than [Next] or [Last] will terminate address check mode.

### Flash

Using the {Flash} softkey in Live will bring a channel or address to full, and then every other second the level will move to 15%. That will hold for 1 second, and then the level will return to full. The channel or address will keep flashing until either the command line is cleared, or [Next]/[Last] is used to increment to the next channel or address.

-   [1]{Flash} - will bring channel 1 to full, then to 15%.

    -   [Next] - channel 1 returns to its previous state and the intensity for channel 2 will flash.

-   [Address/Patch][1][0]{Flash} - will bring address 10 to full, then to 15%.

    -   Ion Classic users will need to use {Address}. Element Classic users will need to use [Dimmer/Address].

#### Flash On & Flash Off

Pressing [Shift] & [Full] together will put all the selected channels at full and "Flash On" will be posted to the command line.

Pressing [Shift] & [Out] together will put all the selected channels to out and "Flash Off" will be posted to the command line.

Releasing the keys will return the channels to their previous state.

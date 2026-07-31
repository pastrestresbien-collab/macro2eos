# Eos Family User Manual v3.2.0 — Chapitre 14 : Multiple Cue Lists

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 14
## Multiple Cue Lists
### About Working With Multiple Cue Lists

> **Note:** *This option is not available on Element 2 and Element Classic.*

Eos provides many useful tools to allow you to work efficiently and simultaneously with multiple cue lists. These topics focus on the features and methods used when working with more than one cue list.

> *Solo Mode* and *Cue List Properties* are topics covered in the Single Cue List chapter that are also useful when working with multiple cue lists. Additional information about working with a cue list can be found in *About Cues & Cue Lists (on page 320)*.
>
> Partitions can be especially useful when working with multiple cue lists. See *About Partitioned* *Control (on page 562)*.

### Recording to a New Cue List

When recording cues, cue list 1 is initially used as the default cue list. Cue list 1 is displayed with only the cue number. It does not have a lead cue list number or a "/". To record to another cue list, that list must be specified. Cues will then be recorded to that cue list until another list is specified, or until the selected cue is changed in Live.

You may record up to 999 cue lists in an Eos show file.

The cue list that you are storing to is always determined by the selected cue, unless you specify a different cue list. The selected cue is displayed in the command line, in the PSD, and at the bottom of the Live/ Blind screen.

The selected cue is the last cue that you affected in Live. This includes a record, an update, a playback action such as [Go], [Back], a [Go To Cue] instruction, or simply changing a cue attribute.

> **Note:** *It is very useful to keep an eye on the selected cue.*

Pressing [Live] will resync to the active cue.

#### Using Record

[Record] will record all parameters of any channels that have non-home values to a specified cue.

To record to a new cue list press:

-   [Record] <Cue> [2] [/] [5] [Enter] - this will create cue list 2 and will record the data to cue 5 in that cue list.

Any cues recorded after this will automatically record to cue list 2 until another cue list is specified or the selected cue changes the cue list number.

#### Record Via Load

You can record a cue 1 to the next unused cue list by using the [Load] button for an unmapped fader. [Record] [Cue] [Load] will create a cue 1 in a new cue list and will map that cue list to the fader. Subsequent cues can also be recorded with [Record] [Load], which will record to the next available cue within that cue list

#### Using Record Only

[Record Only] can be used to create a new cue list instead of [Record]. [Record Only] stores only manual data to the specified cue.

To record to a new cue list press:

-   [Record Only] <Cue> [2] [/] [5] [Enter] - this will create cue list 2 and will record all manual data to cue 5 in that cue list.

The cue list display will change to show only data from cue list 2. Any cues recorded after this will automatically record to cue list 2 until another cue list is specified or the selected cue changes the cue list.

##### Make Manual

This softkey can be used to convert live cue or submaster data into manual values, allowing them to be included in the [Record Only] operation. Therefore data from other cues or lists can be selectively converted to manual data and then stored to another cue/list using [Record Only].

> For more information on {Make Manual}, see *Make Manual (on page 370)*.

#### Using Assert

> **Note:** *There are two [Assert] buttons. The [Assert] button in the main keypad area is used in the examples below. Ion Classic users will need to use {Assert}.*

By default, channel parameters only respond to move instructions during playback . The [Assert] function allows tracked or blocked data from a cue to be replayed, even when another cue list has taken control of that channel/ parameter (see *Cue List Ownership (on page 9)*).

Assert can be applied to cues, cue parts, channels, channel parameters, or to entire cue lists. Asserted channels will play back their tracked and blocked values, regardless of cue list ownership, when the associated cue is replayed.

##### At a Cue Level

When applied at a cue level, [Assert] ensures that all data in the cue, both moves and tracks, will be played back at their stored values.

To place an assert on a cue:

-   [Cue] [x] [/] [y] [Assert] [Enter] - the cue will assert all of its channels upon playback. An "A" will be displayed in the "A" column of the cue attributes (cue index, playback status, and so on); indicating the cue has been asserted.

Assert can also be used from the command line to manually replay portions of a cue without having to replay the entire cue. Assert in this mode can only be used with cues that are currently active.

To place an assert on a portion of a cue:

-   [Group] [6] [Assert] [Enter] - asserts the instructions for the channels in group 6 in cue 4.

This would then need to be stored using either [Record] or [Update].

##### At a Cue List Level

When applied at the cue list level, [Assert] ensures that all values in all cues in that list are asserted on playback. When a cue list has been asserted, the playback status display will show an \"A\" in the assert column for every cue in that list.

To place an assert on a cue list:

-   [Cue] [x] [/] [Assert] [Enter]

##### At a Channel Level

When applied at a channel or parameter level, assert ensures that the entire channel or the specified parameter will be played back at its stored value.

To place an assert on a channel or group of channels:

1.  [select channels] [Assert] [Enter] - a red "A" will appear next to all of the channels' parameters in the Live/ Blind display. This indicates the assert is placed, but not yet recorded to a cue.

2.  [Record] <Cue> [x] [Enter] - the red "A" turns to blue in the Live/ Blind display, indicating the assert has been recorded. In the cue x row of the playback status display or the cue list index, a lower case 'a' appears in the "A" column, indicating that a partial assert is included in cue x.

You may also store this assert using [Update] or you can apply it in Blind. To place an assert on specific parameters:

1.  [select channels] {Intensity / Focus / Color / Beam} or {parameter buttons} [Assert] [Enter] - places an assert on the specific parameters of the selected channels.

2.  [Record] <Cue> [x] [Enter] - the assert is recorded to cue x. In the cue x row of the Playback Status Display or Cue List Index, a lower case "a" appears in the "A" column, indicating that a partial assert is included in cue x.

Assert is a very useful tool allowing channels that have been seized by other cue lists to be repossessed by the associated cue list, while still allowing the asserted channel data to be treated as tracked instructions.

#### Using Allfade

Allfade is a cue attribute (see *Assigning Cue Attributes (on page 327)*) that commands any intensity values on stage that are not provided by the associated cue to fade to zero intensity when the cue is played. The allfade will adhere to the downfade time of the associated cue.

> This is useful when *Using Assert (on the previous page)*, so you can regain control of channels from other cue lists and fade other channels from that cue list out.
>
> **Note:** *Channels with tracked values in the associated cue will not fade out in response to an allfade. These tracked values are part of the associated cue and therefore will be played back.*

To assign an allfade to a cue:

-   [Record] <Cue> [2][/][5] {Attributes} {AF/MF} [Enter] - records cue 2/5 as an allfade cue, thereby forcing any channels not in the cue to fade to zero on playback.

Like many other cue attributes, allfade is a toggle state. To remove the allfade flag, specify the cue and press {Attributes} {AF/MF} [Enter].

> See *AllFade (on page 335)*

#### Changing the Active Cue List

The active cue list will be displayed in detail on the Playback Status Display and the Cue List Index.

This view is changed by the following actions:

-   Recalling another cue list in the command line - [Cue] [3] [/] [Enter]

-   Recording a cue to another cue list - [Record] <Cue> [3] [/] [8] [Enter]

-   Playing back a cue from the fader of another cue list - press [Go] for the associated fader.

> **Note:** *The split Playback Status Display allows detail for two cue lists. Both or either of these can be locked. Playback Status Display (on page 107)*
>
> **Note:** *For information on using out of sequence sync, {OOS Sync}, see OOS Sync (on page 337).*

#### Most Recently Activated Cue

Use [Cue] [n] [/] [Enter] to select the most recently activated cue from that cuelist. If there is no active cue from that list, the first cue in the cuelist will be used.

### Using [Go To Cue] with Multiple Cue Lists

[Go To Cue] defaults to the currently selected cue list. [Go to Cue] is a live function. It can not be used to change cues in blind. [Go to Cue] instructions can be executed from any operating mode, without returning to live.

> By default, a Go to Cue instruction is an out-of-sequence cue and will follow the rules of such (see *Out-of-Sequence Cues (on page 380)*).
>
> For examples of how to use [Go To Cue] in playback, see *Go To Cue (on page 380)*.

#### Using Go To Cue 0

[Go To Cue] [0] is a command line instruction that resets all intensity values not owned by another fader to default, including any manual values that are not an override to another active fader value. [Go To Cue] [0] [Enter] also resets the selected cue list to the top of the list, with the first cue pending.

To [Go To Cue] [0] on another cue list, press:

-   [Go To Cue] [2] [/] [0] [Enter]

> **Note:** *Eos has an added intensity parameter for LED fixtures, that by manufacturer default have only RGB parameters but no intensity parameter. With this added control, the LED fixture will respond to the [Go To Cue] [0] command.*

Captured channels, priority values and values from other faders running a different cue list are not affected by a [Go To Cue] [0] command.

When [Go To Cue] [0] is executed, any intensity values owned by the associated cue will fade out, while all non-intensity parameters remain in the current state. A [Go To Cue] [0] instruction does not impact the input from other programmers using partitioned control, unless the channels/parameters are shared.

##### [Go To Cue 0] & [Load]

The [Go To Cue 0] , located with the playback controls, in conjunction with a fader load button to send a specific cue list to cue 0. This action does not use the command line. On the desired fader, simply press [Go To Cue 0] & [Load]. Ion Classic users will need to use {Go To Cue 0}.

#### Using Go To Cue Out

To reset all parameters to their default state (unless they are controlled by a submaster) and reset all cue lists that are loaded to faders so that the first cue of each list is pending, press:

-   [Go To Cue] [Out] [Enter]

> **Note:** *The [Go to Cue] [Out] command will not affect a cue list that is in Solo Mode (on page 347)*

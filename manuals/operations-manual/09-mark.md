# Eos Family User Manual v3.2.0 — Chapitre 09 : Mark

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 9
## Mark
>
### About Mark

Mark is an instruction that automates the process of presetting automated fixtures to their required state in a cue, prior to fading intensity up. This allows your automated fixtures to unobtrusively perform non-intensity parameter transitions in an inactive (darkened) state.

Most Eos Family consoles provide two different methods to mark lights:

-   *AutoMark (below)*

-   *Referenced Marks (on the facing page)*

### AutoMark

The AutoMark feature is a system default setting and can be turned on or off at a global level. The system default for this setting is off. To change the default settings see *Cue Settings (on page 214)*

With AutoMark enabled, non-intensity parameter transitions occur in the cue immediately preceding the cue in which the changes are stored, if intensity in that cue is moved from zero to any active level. Therefore, the preceding cue executes the AutoMark.

> AutoMark information only applies to cues or cue parts, and is not a channel instruction. AutoMarked cues are indicated by an "M" in the M column of the PSD (see *Indicators in the Playback Status Display (on page 110)*).

AutoMarks will execute using the time of the cue in which the moves occur. This cue will be indicated by M in the Live / Blind display (see *Text Indicators (on page 103)*). The exceptions to this are the mark time in setup, or if discrete timing is stored with the move instruction, in which case the discrete time will be used.

AutoMarks will display the same way in Live and in Blind.

#### AutoMark on Element 2 and Element Classic

AutoMark is the only mark option available for Element 2 and Element Classic consoles, and defaults to enabled.

#### Conditions Triggering an AutoMark

The following rules determine which channels AutoMark is applied to and how it is deployed:

-   The marked cue must have a move instruction for intensity of automated fixtures above zero or null.

-   The marked cue must have a move instruction for non-intensity parameters of those channels.

-   AutoMark will not occur if the channel is receiving an intensity instruction from another source (such as a submaster or HTP fader).

-   AutoMark must be enabled for an AutoMark to occur. AutoMark is based on the current setting of the default during playback. It does not matter what the setting is at the point of record.

-   On a "per channel" basis, an AutoMark does not occur until:

-   Any parameter delay time has elapsed and

-   The intensity has reached zero and the parameter has completed any previous movement.

#### Allowing a Live Move

> **Note:** *Not available on Element Classic.*

It is possible to override AutoMark on a per cue (or cue part) basis. The override is available through a softkey, {AutoMark Off}. This softkey is not visible when AutoMark is disabled in Setup.

When enabled, the cue that executes the mark will have an "M" in the flags field. If AutoMark is disabled, allowing a live move, a "D" is displayed in the flags field of the cue or cue part where the data is stored.

> By using AutoMark with multipart cues, it is possible to have some parameters mark and others move live. See *About Multipart Cues (on page 394)*.

#### AutoMark and Timing

> **Note:** *Not available on Element Classic.*

An AutoMark will happen in the time of the cue in which is moving (the "M" cue), unless the channel has discrete timing or the mark time is disabled via the {Mark Time} setup option.

Discrete timing would override the mark time option in setup. See *Mark Time (on page 214)*. In which case, the discrete timing will apply to the moves. Discrete timing is applied in the cue where the move instruction is stored.

### Referenced Marks

Referenced marks are user-specified marks that are manually applied to specific channels or parameters.

AutoMark and referenced marks cannot be used simultaneously. Referenced marks are not available on Element 2 and Element Classic.

> **Note:** *If you begin programming with AutoMark enabled, and then disable the feature, all of the AutoMarks in the show are converted to referenced marks.*

There are essentially two parts to a successful referenced mark. The first part is the cue with the mark flag (set by the user). This is the cue in which any non-intensity parameters will change. This cue is referred to as the marked cue.

The second part is the cue with intensity value for the channels in question. This is referred to as the source cue. This is also the cue where the non-intensity moves are stored.

In order to use mark properly, you must specify channels to be marked in the source cue. Eos will not assume all automated fixtures apply to any given mark.

There are two ways to apply a referenced mark. You can apply a mark flag at a cue level and then subsequently reference that flag in a later cue, or you can apply a mark in a cue and reference back to an earlier cue.

Referenced marks are useful because the non-intensity parameter data is stored in the cue that actually fades the lights up. Therefore, any changes to the non-intensity parameter data is modified in the source cue. You do not need to worry about changing it in the marked cue.

> **Note:** *When bringing up the intensity of a fixture that is in a marked state, all the parameters of that fixture will be made manual and the current NPs settings will display. This is done so you won't need to use {Make Manual} when storing to a cue.*

#### Setting Referenced Mark Flags

You can apply a mark flag by pressing:

-   [Cue] [n] [Mark] [Enter]

This sets a flag (M) on a cue for later marking activity. In subsequent cues, when channels are marked, they will preset for movement in this cue (unless told to mark elsewhere).

When you are building a cue containing channels that you want to mark, do the following:

-   [select channels] [Mark] [Enter]

-   Store the cue, following normal procedures. Eos will automatically look backwards in the cue list for the first mark flag it encounters.

> Assume you had placed a mark flag on Cue 10 (this becomes the Marked Cue).

-   [Cue] [10] [Mark] [Enter]

> Later you store Cue 12 with a mark instruction on channels 1-10 (this becomes the Source Cue).

-   [1] [Thru] [10] [Mark] [Enter] - Note that channels 1-10 are displayed with a red "M" in the upper right corner.

-   [Record] <Cue> [1] [2] [Enter]

> Since no specific mark instruction was given to the channels in cue 12, the channels will mark back to the first "M" encountered in the preceding cues of the cue list, provided that the intensity for those channels is "out" throughout the duration of the mark.
>
> When Cue 10 is played back, the non-intensity parameters of channels 1-10 will fade to the values stored in Cue 12. Then in Cue 12, the intensity will fade up on those channels.

##### Mark Display Indicators

In the previous example, indications that a mark had been placed are as follows. Cue 10 would be shown with a mark flag (M) in the cue list. In addition, when cue 10 is played back, channels 1-10 will show a green "MK" in the intensity field, while the non-intensity parameters would show the source cue number in green "Q12" (the MK in the intensity field is green if, in cue 10, the lights are fading to zero and then the NPs are marking. If, in cue 10, channels 1-10 were already at zero, a magenta "MK" will be displayed).

The source cue (cue 12) would include a green "M" next to the intensity level and any non-intensity parameter values would be displayed in green. Also, in the cue list, cue 12 would have an "R" in the mark flags field. If a mark has been placed on a cue, but that cue is not yet marking any lights, the "M" will be represented as "m". You will also see an "m" if the mark is no longer in tact.

#### Priority Mark

When setting mark cues, you assign a priority marking using the softkeys {High Priority} and

{Low Priority} . When marking, channels will attempt to mark to high priority cues first. Cues that are flagged with just Mark are considered normal priority. Channels will attempt to mark

to them second if a high priority cue can not be used. Low Priority cues will be used last if a high or normal priority cue could not be used.

> Priority marked cues display indicators in the PSD. See *Mark Symbols (below)*.

#### Applying Flags as Channels are Marked

You may also apply a mark flag to a previous cue by doing the following:

-   [select channels] [Mark] [Cue] [5] [Enter]

-   [Record] [Cue] [8] [Enter]

This would mark cue 5 to perform any non-intensity moves stored in cue 8. The display indicators for this mark would be the same as shown in the previous example. As long as intensity is at zero within the cue range, if there are any non-intensity move instructions for these channels between these two cues, they will be removed.

It is also possible to mark only certain parameters for marked moves, while allowing live moves for other parameters.

> If you wanted to mark only focus, and allow all other parameters to transition while the light is fading up, you can press:

-   [1] [Thru] [10] [Focus] [Mark] [Enter]

#### Mark Earliest

The {Earliest} command can be used with [Mark] to mark the channel into the cue after the last intensity moved from a nonzero level to 0. The mark is stored and behaves exactly as if you had typed the cue number instead of {Earliest}. This works in blind, or in live if you record afterwards.

> Cue 2 moves the intensity for channel 1 to 0, Cue 3 thru 4 have no intensity for channel 1, and Cue 5 has the intensity move to full. From Cue 5:

-   [1] [Mark] {Earliest} [Enter]

> This will work the same as [1] [Mark] [Cue] [3] [Enter], and will mark from cue 3 to cue 5.
>
> **Note:** *[Mark] {Earliest} will mark through block cues or blocked intensity moves of 0, until it finds the earliest intensity move to 0. If the cue immediately before the cue being marked is the earliest intensity move to 0, it will mark in that cue.*

{Earliest M} will mark to the earliest cue that already has a mark flag. If a mark cue doesn\'t exist, {Earliest M} will behave like {Earliest} and will mark to the earliest possible cue.

> **Note:** *{Emergency Mark} can be used to automatically set a mark flag if you had not previously done so. If using {Earliest M} and no cue with a mark flag has already been set, {Emergency Mark} will set a mark flag. See Record Defaults (on page 220).*

#### Mark Symbols

A variety of symbols appear in the Mark flag columns of the Cue List Index and Playback Status Display.

##### Cue List Index

-   MK - Indicates the channel is marked for a later cue. The cue number is indicated in the other categories (see "Q" below).

-   Q - Found in the non-intensity categories of a marked channel. The "Q" is followed by a number indicating which cue the mark is in preparation for.

-   M - Indicates a mark is placed, but manual, and must be stored. Is blue when stored."m" indicates cue is not marking.

##### Playback Status Display

-   D - AutoMark is disabled.

-   M or m - Indicates a marked cue. "M" indicates an AutoMark or a reference mark that is used by a subsequent cue. "m" indicates a reference mark that is currently unused by any subsequent cue. Found in the "Flags" area.

-   R - Indicates the source cue which refers back to an earlier mark. Found in the cue display "Flags" area.

> • + - Indicates a cue is both a marking and reference cue when displayed in the mark flag.

-   - - Indicates a dark move, a cue that has any non-intensity parameters moving on channels whose intensity is at 0.

-   x - Indicates that a mark has been placed, but the mark has been broken. If possible, Eos will AutoMark the lights.

-   mh - Indicates that a cue has been flagged as high priority mark, but nothing is marking to it yet.

-   Mh - Cue has been flagged as high priority, and lights are marking to it.

-   ml - Indicates that a cue has been flagged as low priority mark, but nothing is marking to it yet.

-   Ml - Cue has been flagged as high priority, and lights are marking to it.

#### Reference Marks and Timing

Movement of non-intensity parameters in conjunction with a mark will adhere to the following timing rules.

If discrete timing is used for non-intensity parameters:

When channels execute a mark, the moves will use the discrete time(s) assigned to them in the source cue.

> A mark is applied to Cue 5, making it the marked cue.

-   [Cue] [5] [Mark] [Enter]

> Later, channels 1-10 are assigned discrete timing and a mark instruction:

-   [1] [Thru] [1] [0] {Focus} [Time] [8] [Mark] [Enter] Then, those channels are recorded into Cue 10:

-   [Record] <Cue> [1] [0] [Enter]

> In this instance, when Cue 5 is executed, channels 1-10 will perform their focus parameter moves in 8 seconds, as specified in Cue 10 (the source cue, which is the source of their move instruction).

If no discrete timing is used for non-intensity parameters or mark time is disabled:

When channels execute a mark, the moves will use the time recorded in the marked cue.

> Cue 5 is recorded with a time of 10 seconds.

-   [Record] <Cue> [5] [Time] [1] [0] [Enter] A mark is applied to Cue 5 as above.

-   [Cue] [5] [Mark] [Enter]

> Later, channels 1-10 are assigned a mark instruction and then recorded into Cue 10 with no discrete timing:

-   [1] [Thru] [1] [0] [Mark] [Enter]

-   [Record] <Cue> [1] [0] [Enter]

> When Cue 5 is executed, channels 1-10 will perform their non-intensity parameter changes in 10 seconds, as specified in Cue 5 (the marked cue).
>
> Marked cues that are played out of sequence will fade to their marks immediately. When firing a cue that has a linked cue, the cue will mark like the linked cue is the next cue.The marks will fade using the active cue's timing.

#### Mark Time

> See *Mark Time (on page 214)*

#### Removing Referenced Marks

Mark is a toggle state. Therefore, the first mark command sets a mark. The second removes it. To remove a mark flag from a cue, press:

-   [Cue] [n] [Mark] [Enter]

To remove a mark from a channel:

-   [select channel] [Mark] [Enter]

> **Note:** *If a mark is removed from a channel in live, the corresponding cue must be updated.*

It is also possible to mark to a cue that doesn\'t exist, and when the mark is stored, Eos will automatically create the cue to mark to.

> If cue 2 does not exist yet:

-   [select channels] [Mark][2] [Enter]

> The command line will display, "Create Mark Cue?"

-   [Enter]

> When the cue is stored, the system will automatically create a cue 2 and mark the lights to it.

If a light is marked and that mark is later broken (for example being used by a move instruction stored in the mark range), Eos will attempt to repair the mark. This is done by automatically marking in the cue previous to intensity fading up, if possible. This will be indicated in the cue list by a "*" in the cue immediately preceding the "R" cue.

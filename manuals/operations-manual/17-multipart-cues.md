# Eos Family User Manual v3.2.0 — Chapitre 17 : Multipart Cues

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 17
## Multipart Cues
### About Multipart Cues

Cues can be divided into up to 20 parts. Each part can have its own channels or parameters, levels, and timing information. Multipart cues can be stored in Live or Blind using the same conventions to record a standard cue.

There are three basic ways to create a multipart cue:

-   Building a multipart cue part-by-part in Live

-   Breaking an existing cue into multipart cues in Live

-   Breaking an existing cue apart in Blind.

Multipart cues can be used to organize automated fixture data so that you can apply different times to different moves (focus moves slowly, but color snaps after a short delay). You can also use multipart cues instead of many individual cues triggered by wait times to create a series of fades.

A channel or parameter can only be provided an instruction once in a multipart cue. For example, it isn\'t possible to adjust color for channel 1 in cue 1 part 1 and then also provide a different instruction for channel 1 color in cue 1 part 8.

Default part timing is drawn from the cue level timing defaults established in Setup ( see *Cue Settings (on page 214)*); you may also assign discrete timing to channels in each part as you would for a single part cue.

### Record a Multipart Cue in Live

Storing a multipart cue in Live is accomplished in similar fashion to storing a single part cue. However, rather than storing the entire cue, you select and store just the channels that you want in each part.

> **Note:** *There are a variety of different ways and different orders to go about creating a multipart cue. The examples in these topics represent some, but not all, of those ways.*

#### Creating a New Multipart Cue in Live

There are two ways to create a multipart cue in Live. You can either build it part-by-part, or by building parts from the cue end state.

##### Build Part-By-Part

Make desired changes to the stage state. If all of the changes that you have made are to go into a part, press:

-   [Record Only] [Cue] [2] [Part] [1] [Enter] Continue making changes and storing parts as you go. ***Build Parts From Cue End State***

In most instances, you will create the end state of the cue and then break it into parts. To do

this, you use selective storing commands, as follows:

-   [channel/parameter selection] [Record] (or [Record Only]) [n] [Part] [a] [Enter]

-   [channel/parameter selection] [Record] (or [Record Only]) [Part] [b] [Enter]

> **Note:** *Element Classic users will need to press [Record] twice to post Record Only to the command line.*

Each part can contain its own cue level timing and other attributes. Follow/Hang, Link and Loop, and Allfade commands can only be placed at the cue level, not on a part. Via channel selection, you can put channel parameters into different parts.

Also, you can put channel parameters into different parts by including them after the channel selection but before the [Record] command.

-   [1] [Thru] [1] [0] {Focus} [Record] [Part] [3] [Enter] - places pan and tilt parameters for channels 1 through 10 into part 3.

Part 1 of any multipart cue is where all unassigned move instructions will reside. Therefore, if the body of the cue (which is the normal behavior) is to be in part 1, you can simply select the channel/parameter list that you wish to place in parts 2 and higher.

#### Setting Multipart Attributes and Flags

> Cue attributes include *Follow / Hang*, *Follow / Hang*, *Link / Loop*, *Link / Loop*, *Delay Time*, *Rate*, *Curve*, *Cue Notes*, *Cue Label*, and *Scenes*. They are stored and function exactly as they do in single part cues.
>
> Flags can be set for *Block*, *Assert*, *AllFade*, *Mark*, and *Preheat*.
>
> On Ion Classic, flags can be set for *Block*, *Assert*, *AllFade*, *Mark*, and *Preheat*.
>
> On Element Classic, flags can be set for *Block (Element Classic)*, *Preheat*, and *Moves (Element Classic)*.
>
> For more information, see *Assigning Cue Attributes (on page 327)* and *Flags (on page 332)*.

Cue part attributes can be defined as the parts are recorded, or they can be added after the part has been created.

-   [Record] [Cue] [2] [Part] [1] [Delay] [8] [Enter]

-   [Cue] [4] [Part] [3] {Color} [Time] [6] [Enter]

-   [Cue] [8] [Part] [9] {AutoMark Off} [Enter]

-   [Record Only] [Cue] [5] [Part] [2] [Assert] [Enter]

#### Using Update in Live for Multipart Cues

Updating a multipart cue is generally the same process as updating a single part cue, except you will provide a specific part cue number in the update command.

Various referenced data, such as palettes or presets, can be assigned to build a multipart cue. If you have made changes to referenced data within a multipart cue, thereby creating manual data, pressing [Update] [Enter] updates both the multipart cue and any referenced data with the new levels, as it does with single part cues.

You can update a part of a multipart cue with only selected parameters as well.

> You have written cue 1, which is a multipart cue and is active. Part 2 includes channels 1 through 5 referencing intensity palette 2 which is set at 25%.
>
> Select channels 1 through 5 and change the intensity value to 21%. The data in Live will indicate the new levels in red, and an "R" is displayed to indicate the reference has been broken.
>
> To update cue 1 part 2, including the new intensity levels, breaking the reference to the intensity palette, press:

-   [1] [Thru] [5] {Make Absolute} [Enter]

-   [Update] <Cue> <1> [Part] [2] [Enter]

> To update cue 1 part 2 and the referenced palette with the new levels:

-   [1] [Thru] [5] {Intensity} [Update] <Cue> <1> [Part] [2] [Enter]

> When cue 2 is active, select channels 1 through 5 and set new levels for the color scrollers. Update only part 4 of the multipart cue 2 with the new scroller levels.

-   [1] [Thru] [5] [Scroller] [Update] [Part] [4] [Enter] Element Classic users will need to use {Scroller}.

### Storing a Multipart Cue in Blind

> **CAUTION:** *Edits in Blind take effect immediately, they do not require a **[Record]** or [**Update]** command.*

#### Changing a Single Part Cue to a Multipart Cue

When working in Blind, often you will be breaking a single part cue into a multipart cue.

It is quite possible to create a new cue in Blind and follow the exact same process, except in addition to pulling channel parameters into parts, you will also be providing them with move instructions or block commands. It is worth noting that tracked instructions do not belong to any specific part of a multipart cue.

Select the cue you wish to break apart and specify the first part you wish to create. Part 1 is generally where the body of the cue resides. Therefore, if you specify any part other than part 1, all of the move instructions in the cue are placed in part 1.

Begin by selecting any channels that you wish to move into some part other than part 1.

-   [1] [Thru] [5] [Part] [2] [Enter]

-   [6] [Thru] [1] [0] {Intensity} [Part] [3] [Enter]

-   [6] [Thru] [1] [0] {Color} [Part] [4] [Enter]

As you create each part, that part is now selected. It is possible to select the channel parameter you want and press [Part] [Enter] to pull that data into the selected part.

> **Note:** *When breaking a cue into a multipart cue in blind, the [Part] button is a required instruction. Channel selection will not automatically assign a channel into a part. Use of the [Part] key allows you to add only specific channel parameters to the part. For example: [5] [Thru] [9] {Color} [Part] [Enter].*

#### Changing a Multipart Cue to a Standard Cue

To change a multipart cue to a standard cue, delete all of the parts of the cue.

> Cue 4 is a 3 part cue that include channels 1 through 20. To change cue 4 back to a standard single cue:

-   [Delete] [Part] [1] [Thru] [3] [Enter]

#### Creating Multiple Cue Parts in a Range

[Thru] [Thru] can be used in blind to create multiple cue parts in a range.

-   [Cue] [1] [Part] [1] [Thru] [Thru] [4] [Enter] will create parts 1 through 4.

If you were to use just [Thru] instead of [Thru] [Thru], you would create parts 1 and 4.

### Deleting Parts from Multipart Cues

When you delete parts of a multipart cue, any move instructions in the deleted part are moved to the first available part. If you want to delete move instructions out of a cue part, you have to select the channels and [At] [Enter] or null them.

-   [Delete] <Cue> [1] [Part] [1] [Enter] [Enter]

-   [Delete] <Cue> [6] [Part] [1] [Q Only / Track] [Enter] [Enter]

-   [Delete] [Part] [1] [+] [2] [Enter] [Enter]

-   [Delete] [Part] [1] [Thru] [3] [Enter] [Enter]

# Eos Family User Manual v3.2.0 — Chapitre 23 : Snapshots

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 23
## Snapshots
### About Snapshots

Snapshots are record targets that store the current state of your console\'s control surface and external monitor configuration. These can then be recalled to instantly reset the console and displays to the state stored in the snapshot. You can choose which parts of the front panel and displays you wish to store as a part of the snapshot.

When you record a snapshot, aspects of the Eos user-interface, based on user-preference, are stored so that you can recall them in the future. This allows you to bring the console back to a desired state quickly.

Snapshots can be used on RPUs or RVIs to change what is currently displayed on the external monitors and how that information is displayed.

Snapshot contents are global. They can be stored and recalled on any control interface, other than Net3 RFRs. When recorded, they store the relevant settings of the device initiating the record. When recalled, they recall only the controls that are appropriate on the device the snapshot is recalled.

> **Note:** *Snapshots that store the faders do not include the active cue in a fader. They only include pending cues and fader attributes.*
>
> Snapshots of just a single monitor can also be recorded. See *Recording Snapshots (below)*.

### Recording Snapshots

**Note:** *On Element 2 and Element Classic consoles, {Snapshot} is a softkey.*

To store the current state of the console, record a snapshot.

-   [Record] [Snapshot] [1]

When recording a snapshot, you will see a preview of all of the displays as they will be recorded in the snapshot. You can choose to select/ deselect various components, monitors, frames, etc from your snapshot.

*(figure omise)*{width="5.7952012248468945in" height="2.6858333333333335in"}

From the snapshot menu, the following options are available:

-   Visible Workspaces - includes only the visible workspaces.

-   All Workspaces - include all workspaces, including those not visible at the time of recording.

-   Faders - captures the current content or state of the faders including: fader page mapping, position of all submasters, and pending cues based on configuration.

-   Encoders - records the current page of the encoders.

-   Filters - records the current setting of the record filters.

-   Direct Selects - when used without visible workspaces selected, this option will recall all direct select tabs and their settings.

-   Favorite - the snapshot will display in the quick access window. See *Quick Access*.

-   Color - assign colors ({Red}, {Green}, or {White}) or {Dark} to a snapshot. {Dark} assigns no color to the snapshot. The colors will display beside the snapshots name in a direct select, and / or if that snapshot has been assigned to one of the customizable hardkeys on Eos Ti, Gio, Gio @ 5, and RPU.

-   Reset - sets the menu back to its defaults.

> **Note:** *The Faders and Encoders options are not available on Element 2.*

*(figure omise)*{width="3.125in" height="2.4270833333333335in"}

You may also check or uncheck to include or exclude any of the following:

-   Monitors - any of your console\'s internal or external monitors

    -   Frames - any of the open frames on that monitor

        -   Tabs - any of the open tabs in that frame

-   Master Fader Pair - the two master playback faders

    -   Content Mapping - the page and location of the content assigned to the faders

    -   Content State - the state or level of the content

-   Faders - any other internal or external faders

    -   Content Mapping

    -   Content State

    -   Wing Group - which page the wing group is currently displaying

-   Top Bar Timecode List - which timecode list is currently displayed in the top bar display

When one or more sublevel items are excluded, a minus (-) icon will appear next to the top level item to indicate that not every available option will be saved. A checkmark icon will display when every sublevel item will be saved.

Monitors and frames can also be selected or deselected in the preview area. Use

{Frames/Monitors} in the top right to toggle between monitor or frame numbers. Deselected monitors and frames will be greyed out. Deselected frames will also display a slashed red circle icon.

### Recalling Snapshots

**Note:** *On Element 2 and Element Classic consoles, {Snapshot} is a softkey.*

When snapshots are recorded, you can view them in the snapshot list. To view the list:

-   Press [Snapshot] [Snapshot]

-   Press [Tab] [1] [9]

-   Navigate to Browser > Record Target Lists > Snapshots.

-   Select the Pop-up Snapshot Browser from the top-right menu icons Snapshots can be recalled in the following ways:

-   From the keypad/ command line - [Snapshot] [5] [Enter]

-   From cues using the execute list

-   From a recorded macro instruction

-   From the direct selects - {Snapshot 4}

Since snapshots can be recalled from any device (except RFRs) on the Eos Family network, snapshots may be affected by the type of device they are recalled on. If the recalling device does not have the same physical layout or has other limitations that differ from the recording device, Eos will map the snapshot to the best of its ability.

> **Note:** *In a system with multiple users, it is recommended that you allot discrete snapshot numbers for each user. Since snapshots are global and can be recorded/ recalled from most devices, assigning numbers for each user will ensure their* *snapshots are stored and edited properly for their device.*

### Editing Snapshots

> **Note:** *On Element 2 and Element Classic consoles, {Snapshot} is a softkey.*

To edit or preview the contents of a snapshot, open the snapshot list by selecting [Snapshot] [Snapshot], opening [Tab] [1] [9], navigating to Browser > Record Target Lists > Snapshots.

You can use [Next] and [Last] to navigate the list or you may specify a snapshot in the command line.

Once a snapshot is specified, the list displays five columns, one for each element. You may change the enabled elements by pressing the CIA buttons or the softkeys found beneath the CIA. If an element is added to the command line using the softkeys, it will be enabled when [Enter] is pressed. All other elements will be disabled.

Snapshots can be labeled in the snapshot list by selecting the snapshot and pressing [Label] or by selecting the Label column.

-   <Snapshots> [3] {Monitors} [Enter]

> This command will enable the monitors for snapshot 3 and disable any other elements.

Snapshots can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Icons (on page 120)*.

### Deleting Snapshots

**Note:** *On Element 2 and Element Classic consoles, {Snapshot} is a softkey.*

You may delete snapshots using the following syntax:

-   [Delete] [Snapshots] [2] [Enter] / [Delete] {Snapshots} [2] [Enter]

-   [Delete] {Snapshot 5} - selects a snapshot from the direct selects to delete it.

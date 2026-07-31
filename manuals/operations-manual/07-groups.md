# Eos Family User Manual v3.2.0 — Chapitre 07 : Groups

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 7
## Groups
### About Groups

Groups are channel selection devices used for fast recall of specific channels. Once recorded, they are accessible from the keypad, direct selects, and through the displays.

### Recording Groups Live

Record groups of channels that you want to have available for fast recall later. Groups can be stored as whole numbers (such as Group 5) or as decimals of tenths, hundredths, or thousandths (such as Group 2.5, Group 7.65, Group 3.131). Only whole number groups can be stored using the direct selects; any decimal designations for groups must be stored using the keypad.

All groups may be labeled. These labels are then displayed on the direct selects as well as in the group list. Group numbers will not display in either until the groups have been created.

The following syntax examples illustrate the various methods and features available when recording groups:

-   [1] [Thru] [5] [Record] [Group] [7] [Enter] - records only channels 1 through 5 to group 7.

-   [4] [Thru] [8] [.] [Record] [Group] [2] [Enter] - records only the cells of the selected multicell fixtures, channel 4 through 8, to group 2.

-   [Record] [Group] [7] [Enter] - records all channels with non-home values to group 7.

-   [5] [Thru] [9] [Record] {Group 7} - records channels 5 through 9 to group 7 using the direct selects.

-   [3] [Thru] [8] [Record] [Group] [8] [.] [5] [2] [Enter] - records channels 3 through 8 to

> group 8.52.

-   [-] [3] [Record] [Group] [7] [Enter] - records all channels, except channel "3," to group 7.

-   [Group] [7] [+] [5] [Record] [Group] [9] [Enter] - records groups 7 and 5 into group 9.

-   [Group] [8] [Group] [9] [Record] [Group] [1] [0] [Enter] - records groups 8 and 9 into

> group 10.

-   [Record] [Group] [7] [Label] [name] [Enter] - records as above and adds a label to the group.

-   [Record Only] [Group] [7] [Enter] - records channels with manual data to group 7.

-   [Record Only] {Group 7} - records channels with manual data to group 7 using the direct select.

On Element Classic consoles, Record Only is accessed by pressing [Record] twice.

#### [Thru] and [Thru] [Thru]

[Thru] can be used to select existing cues, presets, palettes, and groups between two numbers.

[Thru] [Thru] syntax will error instead of creating targets between two numbers.

Decimal targets will only be created with [Thru] [Thru] if the start and end target have the same number of decimal places. Zeroes at the end of decimal target numbers are ignored. As the target lists in the browser are limited to 10,000 items, [Thru] [Thru] syntax that would create more than 10,000 targets is ignored.

-   [Group] [1] [Thru] [Thru] [Enter] - syntax error.

-   [Group] [1.001] [Thru] [Thru] [11.001] [Enter] - 10,000 groups with 3 decimal places are created from 1.001 to 11.001.

-   [Group] [1.001] [Thru] [Thru] [11.002] [Enter] - 10 whole-number groups are created from 2 to 11.

-   [Group] [1] [Thru] [Thru] [11.001] [Enter] - 11 groups are created: 1.001, 11.001, and

> whole-number groups from 2 to 11.

#### Ordered Channels

When recording groups, channels are ordered in the group based on their selection order when the group is stored. This ordering is useful when combined with [Next] and [Last] functions, and when applying effects to groups.

> If you record a group by selecting channels in the following order:

-   [1] [+] [3] [+] [5] [Thru] [9] [Record] [Group] [1] [Enter]

> Later you select Group 1 and press [Next], the channels will be accessed, one at a time, in the same order in which they were initially selected.

If new channels are added to an ordered group using an update command, those channels are added to the end of the channel list from an ordering perspective.

When a group is previewed using the Group List, the display defaults to showing the ordered view. Channels can be reordered as needed from this list. Use the [Format] key to change to a numeric listing of channels.

-   [1] [0] [Thru] [2] [Record] [Group] [1] [Enter]

> This will record channels 10 through 2 to Group 1, and then if you select the group you can cycle through the channels using [Next] starting with 10, then 9, then 8, and so on.

The following softkeys are available:

-   {Insert Before} - use to insert a new channel after the specified channel within a group.

-   {Insert After} - use to insert a new channel before the specified channel within a group.

-   {Reverse} - use to place a group\'s channels in reverse order.

-   {Random} - use to place a group\'s channels in a random order.

-   {Reorder} - use {Reorder} to rearrange the channels to numeric order in a group.

-   {Offset} - See *Offset (on page 242)*.

#### Subgroups

You can create subsets of channels within a group by using [Shift] & [/] to create parentheses. The subgroups will display within those parentheses.

These subsets of channels or subgroups are treated as a single channel in the following ways:

-   When applying absolute or relative effects from live, the subgroups are treated as a single channel by the effect.

-   When setting a range of step\'s channels on a step based effect, the subgroup will not be spread out amongst multiple steps.

-   When the group is selected and next/last is pressed, each subgroup is traversed.

-   When a group has subgroups, {Reverse}, {Reorder}, and {Random} in the group editor will affect the subgroups instead of the channels in each subgroup. {Reorder} will order the groups based on the first channel in each subgroup.

-   Subgroups can be created either in the group list or Live.

> ![](media/media/image252.png){width="4.144889545056868in" height="0.9770833333333333in"}

To create a subgroup in Live:

-   [Shift] & [/] [1] [Thru] [4] [Shift] & [/] [Record] [Group] [2] [Enter] To create a subgroup in the group list index:

-   [Group] [2] [Enter] [Shift] & [/] [1] [Thru] [4] [Shift] & [/] [Enter]

#### Editing and Updating Groups in Live

Existing groups can be updated or re-recorded in Live. If you re-record an existing group, a confirmation is required (unless disabled in Setup). By re-recording a group, you replace the contents of the group, you do not add to it. Updating a group does not require a confirmation and adds channels to the group, rather than replacing them.

Other editing or updating examples are:

-   [Group] [x] [Label] [Label] [Enter] - clears the label.

-   [Group] [x] [Label] [name] [Enter] - stores a new label.

-   [1] [Thru] [5] [Update] [Group] [n] [Enter] - adds channel 1-5 to existing Group n. For record examples, see *Recording Groups Live (on page 274)*.

#### Multicell Fixtures in Groups

There are multiple different ways to create groups using multicell fixtures.

> **Note:** *The following examples are created in the group list. Groups can also be recorded in Live. See Recording Groups Live (on page 274)*

To create subgroups of the whole multicell fixtures:

-   [Group] [3] [1] [Enter] [5] [0] [0] [Thru] [5] [0] [3] [Enter]

To create a group with only the cells of the selected multicell fixtures:

-   [Group] [3] [2] [Enter] [5] [0] [0] [Thru] [5] [0] [3] [.] [Enter]

To create a group with only certain cells of multicell fixtures:

-   [Group] [3] [3] [Enter] [5] [0] [0] [Thru] [5] [0] [1] [.] [1] [Thru] [2] [Enter]

To create a group with only the master cells:

-   [Group] [3] [4][Enter] [5] [0] [0] [Thru] [5] [0] [3] [Shift] & [.] [Enter] To create subgroups with only specific cells:

-   [Group] [3] [5] [Enter] [5] [0] [0] [.] [1] [Shift] & [/] [5] [0] [1] [.] [1] [Enter]

![](media/media/image253.png){width="4.563345363079615in" height="1.0014577865266843in"}

You can also use the {Offset} softkeys to aid in create of groups and subgroups. See *Offset (on* *page 242)*.

### Selecting Groups

Groups may be selected from the control keypad or the direct selects. To select a group:

-   [Group] [1] [Enter] - selects all channels in Group 1

-   [Group] [1] [At] [5] <0> [Enter] - selects Group 1 and places all channels within at 50%

-   {Group 1} - Selects all channels in Group 1

If [Next] is used after a group selection, it accesses the first ordered channel in that group. Pressing it again accesses the second ordered channel in that group, and so on. [Next] - used after the last channel in the group - accesses the first channel in the group again.

[Last] may be used with group selects similar to [Next]. Press [Select Last] to reselect the entire group.

### Deleting Groups

When you delete a group, the group number and all contents from the Group List Index and Direct Selects are deleted. Delete commands require a confirmation by default. This can be altered in the default settings. If you disable confirmations, the second enter is not required in the following examples:

Group deletion features include:

-   [Delete] [Group] [5] [Enter] [Enter] - deletes group 5.

-   [Delete] [Group] [3] [+] [Group] [5] [Enter] [Enter] - deletes groups 3 and 5.

-   [Delete] [Group] [3] [Thru] [9] [Enter] [Enter] - deletes groups 3 through 9.

-   [2] [Delete] [Group] [7] [Enter] - deletes channel 2 from group 7.

### Group List

The group list allows viewing and editing of groups. To open the group list you can:

-   Press [Group] [Group]

-   Press [Tab] [1] [7]

You can navigate within the group list using [Next] and [Last] or by selecting the group you want to work with.

#### Ordered View and Numeric View

By default, grouped channels will be displayed in ordered view. Therefore, grouped channels will appear in the order they were added to the group (see *Ordered Channels (on page 275)*). If you wish to view the channels in numeric view, press the [Format] key and the view will be switched (channels will appear in numeric order from lowest to highest).

This setting defines how channels are displayed in Group List. If left in numeric format, group selection channels will be displayed in chronological order. If left in ordered view, they will be displayed based on their order of being stored to the group.

#### Editing Groups from the Group List

An existing group can be modified without the need for recording or updating, as follows.

-   Select the required group by pressing [Group] [n] [Enter], or using [Next] and [Last] to navigate through the list.

The selected group is highlighted in gold. The following actions are possible:

-   [Label] [name] [Enter] - adds or modifies a group label.

-   [Copy To] [Group] [7] [Enter] - copies the contents of the selected group to group 7.

-   [2] {Insert Before} [9] [Enter] - inserts channel 2 into the group, placing it before channel 9 in the ordered view.

-   [2] {Insert After} [5] [Enter] - inserts channel 2 into the group, placing it after channel 5 in the ordered view.

-   [2] [Delete] [Enter] - removes channel 2 from, the group.

-   [+] <Chan> [1][0] [Enter] - adds channel 10 to the selected group.

-   [-] <Chan> [5] [Enter] - removes channel 5 from the selected group.

-   [+][Group] [1][0] [Enter] - adds group 10 to the selected group.

-   [-] [Group] [5] [Enter] - removes group 5 from the selected group.

-   {Random} [Enter] - rearranges the channels in the group randomly.

-   {Reverse} [Enter] - reverses the order of the channels within the group.

-   {Reorder} [Enter] - reorders the channels to numeric order in the group selected.

-   {Offset} - see *Offset (on page 242)*.

Groups can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Icons (on page 120)*.

### Using Groups as a Channel Collector

[Group] can be used as a quick way to collect channels from submasters, cues, presets, and palettes.

The following actions are possible:

-   [Group] [Cue] [1] - selects all the channels in cue 1.

-   [Group] [Sub] [3] - selects all the channels in submaster 3.

-   [Group] [Int Palette] [5] - selects all the channels in intensity palette 5.

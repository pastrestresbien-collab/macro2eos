# Eos Family User Manual v3.2.0 — Chapitre 28 : Partitioned Control

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 28
## Partitioned Control
### About Partitioned Control

Partitioned control allows discrete control and programming of channels between multiple programmers.

When multiple programmers are working on an Eos Family system, partitioned control can be used to restrict a specific user's access to certain channels. This can help avoid overlapping control of channels by multiple programmers at once.

Channels can be included in more than one partition.

### How to Use Partitions

The primary use of partitioned control is to allow more than one programmer to work on a show file at the same time without the risk of one user storing data for another user's partitioned channels.

The most common example of this situation is when one user is programming automated fixtures while another user programs conventional fixtures. Partitioned control allows these users to divide the channels between them so they may work simultaneously. If one user stores data using record or record only, partition control will guarantee that only data for their partitioned channels will be stored. Data for channels not in their partition will be ignored when performing any store commands.

### Setting Up Partitioned Control

Partitioned Control is enabled or disabled in Setup>System>Partitions (see *System (on page 212)*.) Partition defaults to "Disabled". Enabling or disabling partitioned control is a system-wide setting.

### Partition List

To view the partition list display, press the {Partitions} button in Setup>System. This display lists all existing partitions. There are four pre-programmed partitions in Eos, they are:

-   Partition 0 - No channels and no fader control. This is the default for all users when partitioned control is enabled for the first time on a show. To gain control, you must select a different partition.

-   Partition 901 - All channels. Allows the user access to all channels.

-   Partition 902 - Single Parameter Channels. Allows the user access to only channels with a single parameter.

-   Partition 903 - Multiple Parameter Channels. Allows the user access to only channels with multiple parameters.

To select a partition in the list, enter it in the command line.

-   {Partition} [9][0][2] [Enter]

If partitioned control is enabled, this will now be your assigned partition.

### Creating New Partitions

To create a new partition, press:

-   {Partition} [x] [Enter] - where "x" is a number that does not yet exist in the partition list.

This will create a new partition, highlight it in the list, and (if partition is enabled) assign it as your partition.

To assign channels to that partition, enter them in the command line:

-   [1] [Thru] [9] [6] [Enter]

You can also use [+], [-], and [Group] to further modify the channels in the partition. When adding/ subtracting channels to a partition, if you do not use [+] or [-] before channel numbers, the numbers will replace the channels in the partition, rather than adding to or subtracting from them. This overwriting does require a confirmation (if enabled in setup).

### Deleting Partitions

To delete any partition, simply type the syntax in the command line:

-   [Delete] {Partition} [5] [Enter] [Enter] - deletes partition 5 from the list. Preprogrammed partitions cannot be deleted.

### Using Partitions

> Partitions are set on a user level. See *User ID (on page 568)*.

When partitions are enabled and a partition is selected, you may only control and record data for the channels included in the partition, with the exception of parking and unparking channel parameters or playing back cues. If you try to control a channel that is not in your partition, Eos will post an advisory that this channel is outside of the partition, and you must confirm that you want to control that channel. You will not, however, be able to store information for that channel.

When you record a target (cue, preset, palette), only those channels that are partitioned to you are recorded. Other programmers' record actions to the same target can add to it (they do not replace it) unless channels are shared. When shared, the last value provided at the point of the record action will be stored.

### Partitions in Playback

In Eos, how faders are configured and what is loaded to those faders is shared across all control devices, with the exception of the master playback. As such, if the leftmost fader on page 1 is configured as submaster 1, all devices will display and control submaster 1 on that fader.

When content is played back from any device, it will be recalled in its entirety. If you wish to limit playback on cues, partitions can be assigned to cue lists. See *Partitions on Cue Lists (below)*. Additionally, filters can be placed directly on the playbacks to restrict what is recalled on that fader. Filters are system wide.

Eos allows each user to assign different cue lists to their master fader pair. Using this feature, programmers can work within their partitions, using the master fader pair for their specific cue list, without affecting the cue list that is loaded to the master fader of another user.

**Note:** *Element 2 and Element Classic consoles are limited to a single cue list.*

### Partitions on Cue Lists

A partition may be assigned to a cue list. If a partition has already been applied to a cue list, any channels not in the cue list\'s partition will not be included in cues when they stored or replayed.

Any data for a cue list that already existed before a partition is applied, will be maintained, including data for channels not included in the partition. If data existed before the partition was assigned, in blind, channels that are not in the partition will display without a channel graphic, any levels will be in gray, and a small superscript N will display with it.

Assigned partitions will display at the top of the cue list index and in the PSD.

To assign a partition to a cue list:

-   [Cue] [n] [/] {Partition} [n] [Enter] To remove a partition from a cue list:

-   [Cue] [n] [/] {Partition} [Enter]

### Flexichannel in Partitioned Control

> When partitioning is enabled, a flexi mode, "Partitioned" is available as a softkey. When this is enabled, the flexi mode is limited to only those channels defined in the current partition. This mode may be further modified by use of the remaining flexi states. See *Using Flexichannel (on page 106)* and *Flexichannel Views in Patch (on page 165)*.

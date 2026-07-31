# Eos Family User Manual v3.2.0 — Chapitre 29 : Multi-Console

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 29
## Multi-Console
  ----------------------------------------------------------------------------------------------------------------------------
  --------------------------------------------- ---------------------- -------------------------------------------------------
  ----------------------------------------------------------------------------------------------------------------------------
### About Multi-Console

This chapter outlines the procedures required to use multiple Eos Family control devices simultaneously on a network. It outlines the setup, configuration, and behavior that is entailed in an Eos Family multi-console scenario.

> **Note:** *Only Intel-based Macs can connect as clients.*

Multi-console functionality is also used to provide synchronized backup of your show while running multiple devices on the network. The backup on the system will receive all show data updates and stage levels so that, in the event of a primary failure, the backup will be capable of taking control of the system without a loss of show data or live output. Saving occurs across the whole network.

### Multi-Console Terms

Familiarize yourself with these terms prior to setting up a multi-console system.

-   Primary - When an Eos Family console is configured as a primary, other Eos devices can connect and synchronize with it. If using a backup processor, the primary is the console that will be backed up. By default, all Eos Family consoles will start up as a primary. Should a primary fail and a backup takes control, then the backup will be acting as the primary.

-   Backup - The console capable of taking control of the system if the primary fails. You may input data and run your show from a backup. There can only be one backup in an Eos network and you must specify which primary it is backing up.

-   Client - Any online console that is not the primary or backup is a client. Client data is sent and received over the network, and clients will synchronize with a designated primary.

-   Offline - Any console that is disconnected from the Eos network. Changes to show data performed on an offline console will not affect the rest of the Eos network or the lighting system.

-   Tracking - Any device that is synchronized with a primary is tracking. Once a backup takes control it becomes a primary and is no longer tracking.

-   User - A user is a console defined by a user ID. If it has a unique user ID, the console will operate separately from other Eos devices on the network, but still track show data. If it shares a user ID, Eos will synchronize with like IDs. See *User ID (on page 568)*

-   System - One primary, one backup, and (if available) multiple synchronized clients.

-   Mirror Mode - A mode for mirroring the displays of another device. See *Mirror Mode (on page 569)*

-   Dongle - an internal component of Eos Family consoles that enables ouput and communication with other devices. Dongles are also provided as external USB keys for use with ETCnomad systems.

> **Note:** *Net3 RVIs can not be configured as primaries or backups.*

### Multi-Console Setup

When using multiple Eos devices on the network, you should adjust some of the settings to ensure optimal functionality.

Additional requirements for multi-console setup include:

-   Software versions must match exactly between all devices.

-   All devices have to use the same fixture library. See *Update Profile (on page 193)*.

-   The language settings in the ECU must match. See *Language (on page 578)*

-   The keyboard language setting in the ECU must match. See *Keyboard (on page 578)*

> **Note:** *It is recommended that you perform the following setting changes before connecting your device(s) to the network. After the changes are complete, connect to the network and reboot the device.*

#### Designate Primary

By default, all Eos devices will boot as a primary. When using multiple Eos devices on the network, only one should be designated as a primary. Other Eos devices should be configured as the backup (only one per system) or clients.

To change this setting, you must exit the Eos software (Browser>Exit) and then designate the Eos device as primary, backup, or client in the ECU Welcome Screen (see *ECU Welcome Screen (on page 576)*).

#### DHCP Server

DHCP server supplies IP addresses to network devices. Only one Eos device (typically the Primary) on the network is necessary to do this properly. Therefore you should disable the DHCP server on all Eos devices except for the intended primary.

To disable the DHCP server on your Eos device, go to ECU > Settings > Network > DHCP Service. See *Device (on page 584)*.

#### Change Device Name

To easily identify your Eos on the network, change the device name to be representative of the device (such as "Booth Primary" or "Tech Backup"). This is done in ECU > Settings > General. See *Device Name (on page 577)*.

#### Backup Auto Take Control

Switches to the backup automatically if the primary should go offline. This is enabled in Setup

-   System > *Session (on page 213)*.

#### Backup at Higher Priority

This enables the backup device in a multi-console system to take over at one priority higher than the primary if the primary goes offline. This is enabled in Patch > Protocols > *sACN (on* *page 186)*

#### Network Type

This setting adjusts the timeout period before a backup device will take control from the primary. This is done in ECU > Settings > Network > Interface Protocols. See *Network Type (on page 587)*.

-   Standard - after five seconds of no response from the primary, the backup will assume the primary has disconnected and will then take control.

-   Engineered - after 1.6 seconds of no response from the primary, the backup will assume the primary has disconnected and will then take control.

#### Change IP Address

Each Eos device on the network should be given a unique IP address. If running multiple devices of the same type (for example - two consoles, or two RPUs), you must alter the default static IP addresses to ensure proper functionality. For a list of the default IP addresses for Eos devices, see *Network (on page 224)*

> Changing the static IP address is done through the ECU (see *Settings > Network (on page 583)*

). Manually change the IP address of any non-primary Eos device by clicking in the IP Address field and entering the new number from the keyboard. When done, press [Enter].

> **Note:** *It is recommended that you alter the very last digit of the static IP address by an increment of one for each additional Eos device on the network. Therefore, if the primary ends in "101", change the backup to end is "102", a client to end in "103" and so on.*

#### Output in Client Mode

Consoles in client or backup mode by default will not output on their local DMX ports. This option is found in Setup > System > Output. Click on {Output in Client mode} to enable the ability to output.

### User ID

When multiple users are on an Eos Family network, they can all act as one combined user, all as separate users, or any of the varying degrees between.

Any Eos Family console can be a separate user on an Eos Family network. Certain devices work well as independent users while others are intended to share a user ID with another device. For example, consoles and RPUs are likely candidates for working with a unique user ID while RVIs and client PCs can be useful sharing an ID with another device to track programming information from a second location.

Set in the Setup (see *Users (on page 219)*), User ID is a console-specific identifier that can be set uniquely for each Eos device or can be shared between multiple devices allowing for certain data to be shared between consoles. The user ID can be set anywhere from 1 to 99.

The decision to share a user ID is based on the desire to share a common work environment and command line. It is often common for a designer to be the same user as a programmer so his displays and operating modes follow a programmer, and his command line mimics the programmer\'s. Alternatively, mirror mode of a user can be called. It is also possible to set the designer up as a completely separate user, adding a command line object to a magic sheet to allow a view into programming activities.

#### Assigning User ID

> User ID can be defined in Setup > System > Users. See *Users (on page 219)*.

To quickly change the User ID, you can click on the User ID displayed above the CIA. A pop-up window will open with the available User ID options.

When multiple programmers are working on the system, partitioned control can be used to restrict a specific user's access to certain channels. This can help avoid overlapping control of channels by multiple programmers at once.

> For more information on partitioned control, see *Using Partitions (on page 563)*

#### Data Sharing & User ID

Data shared between Eos Family devices with the same User ID:

-   Command line

-   Null channels in live

-   Selected channels

-   Filters

-   Selected cue

-   Live / Blind mode

-   Setup > User

Data specific to the Eos Family device, regardless of User ID:

-   current fader page

-   current encoder page

-   focus on displays without command line

-   display configuration (layout, format, visible parameters, flexichannel)

-   paging without changing selected target or channels

Data identical between all Eos Family devices, regardless of User ID:

-   all stage levels and edits

-   all data stored in the show file

-   playback, fader and grandmaster contents and progress

The default User ID for any Eos Family device is 1. You may change this based on your preference to allow/ restrict the functionality described above.

> **Note:** *After you have completed the setting changes described above, connect your* *Eos device to the network and reboot the device.*

### Mirror Mode

Mirror mode is used to mirror the external displays of another device. It can be used on any device on the network, including the primary processor. Any device being mirrored is referred to as the host. The is no limit to the number of mirrored devices a host can have. A console currently in mirror mode cannot be mirrored.

> **Note:** *Desk settings are not mirrored.*

When a device is in mirror mode, the only action allowed from that device is paging via the page keys and shutdown / startup. When a device in mirror mode pages, it also pages the host. A device can select which user number it is mirroring by using the alphanumeric keyboard shortcut ALT +F1. ALT + F2 can be used to leave mirror mode.

> **Note:** *If a device is not currently in mirror mode, pressing M on an alphanumeric keyboard will post Macro to the command line.*

#### Mirror Mode Displays

When a device is placed in mirror mode, external monitors on the mirroring device will match the external monitors of the host. A client will mirror as many monitors as it has available.

All formats used on the host device are shown on the mirroring device including flexichannel states, column widths, chosen parameters, and pages.

The CIA will open on monitor 1. The CIA on the device in mirror mode can be locked open or closed. When left unlocked, the CIA will expand and close as normal. Not all CIA displays shown on the device in mirror mode. The following CIA displays are synchronized:

-   About

-   Effects

-   Effects Status

-   Color Picker

-   Curves

-   Undo

The CIA can be completely hidden when locked by pressing the [Displays] key. Pressing [Displays] again will display and unlock the CIA.

#### Configuring Mirror Mode

Configuring a device to connect in Mirror mode is done from the Displays menu in the Browser. When [Displays] is pressed, a {Mirror} softkey will be displayed. Pressing {Mirror} will open up a list of potential hosts in the CIA.

The mirror display can be navigated using the arrow keys or a mouse. When the required host is highlighted, press [Enter] or double click with a mouse to confirm the selection. This display can also be opened with the keyboard shortcut of ALT + F1.

> **Note:** *While in Mirror mode, the display will also have options for exiting and powering off the device.*

#### Exiting Mirror Mode

Exiting mirror mode can be done by selecting {Stop Mirroring} in the mirror display or using the keyboard shortcut ALT + F2. When exiting mirror mode, the device will return to its normal, working state.

> **Note:** *Clients without a dongle cannot exit mirror mode.*

#### Start in Mirror Mode

When a device is shut down in mirror mode, it will restart in mirror mode mirroring the same host as before. If the host has changed settings, mirror mode will need to be reselected on startup.

#### Mirror Mode Macros

Macros can be created to configure a device for mirror mode and to exit the mode.

If your console has dedicated macro hardkeys, the face panel button configuration in the ECU allows setup of these buttons.

> **Note:** *An alphanumeric keyboard will be needed to create this macro.*

To create a macro to place a device in mirror mode:

1.  Set the User ID of all devices to match the Primary.

2.  Press ALT + F1 to open the mirror mode display.

3.  Highlight the device to mirror.

4.  Press [Learn] [x] [Enter] to record the macro. To create a macro to exit mirror mode:

    1.  With the console in mirror mode, press [Learn] [x] [Enter]

    2.  Press ALT + F2.

    3.  Press [Learn] to finish recording the macro.

Once the macros are created, you should save the show and set all User IDs back.

#### Using Mirror Mode on a Client without a Dongle

A client without a dongle can connect to the network. When this is done, the client can only operate in mirror mode, and it will always connect to the primary processor. No other options will be available.

### Synchronized Backup

Once you have changed settings to facilitate a multi-console system on the network, you may activate synchronized backup to ensure show data security.

Eos synchronized backup is designed so that during normal operation the primary device controls the lighting system, and any device configured as backup or client synchronize with the primary. The following activities will synchronize between consoles when operating in a backup system:

-   Playback

-   Record operations

-   Manually set data

-   Show file and data

#### Setting Up Synchronized Backup

Before backup is possible, you must have at least two non-RVI Eos devices connected to the network. One must be assigned as primary and one as a backup.

To assign a backup to a primary:

1.  Exit the Eos environment (Browser> Exit Eos) on the console you wish to act as the backup. This will send you to the ECU welcome screen.

2.  Touch or click on the {Backup} button in the welcome screen. The console will then startup the Eos software, this time in backup mode. Eos will try to connect to a primary console. The CIA will say "Waiting for Master. One moment please\...".

3.  If the backup doesn't connect after a few moments, press the {Troubleshoot} touchbutton in the CIA. This will open the network configure screen in the CIA.

> **Note:** *If this is the first time that a backup is connecting to this master, you will need to press {Troubleshoot} and select the master.*

4.  Select a primary console from the list on the right. If no masters are available in the list, a primary console is not connected to the network.

5.  Press {Change Master}. The backup Eos will synchronize with the master. You will see the console\'s current status above the softkeys display.

If the primary goes offline for any reason, the backup will automatically takeover as the master if backup auto switch has been enabled (see Setup > System > Session > *Backup Auto Take Control (on page 213)*. Whenever master control changes between the primary and the backup, there will be a dialog window that will be displayed that must be dismissed by the user.

When master control moves between the primary and backup device, any clients in the system will automatically connect to the current master. Clients will also display a message, but the message will be dismissed after a short period of time. The device status above the CIA icons will also change.

> **Note:** *A backup may take up to 5 seconds to determine that connection with the master has been lost. This timing can be adjusted based on network type selected in the ECU. See Network Type (on page 567).*

If you enter the Network > Configure screen, it will have changed to show that your backup is now acting as the master and is controlling the lighting system.

> **Note:** *If the primary comes back online, it will not retake control of the lighting system. The primary will wait until it is re-designated as the master and the backup is reassigned to it. You can force the backup to release control back to the primary by going to Browser > Network > Configuration and pressing {Release Control}. You can also force the primary to take control away from a backup by going to Browser > Network > Configuration and pressing {Take Control}.*

#### Backup Scenarios

##### Two Consoles

Two consoles can be used to provide backup. Either can be configured as the primary or the backup. If the primary console fails, the second console will take control with full show data intact.

This is a useful scenario for touring multi-user applications.

##### Console and RPU

One RPU and one console can be used as a backup option. In this configuration, it is recommended that you set the RPU as the primary and the console as the backup. In this scenario, should the RPU go offline, you will still have the full functionality of the console user-interface at your disposal.

##### RPU and RPU

Two RPUs may serve as primary and backup also. A backup system of this type can support many client consoles at once, which you may turn on and off as needed without the need to reset to a different master each time.

This application is ideal for permanent installations requiring synchronized backup.

#### Remote Software Installation

Within a multi-console system, you can remotely install software to all devices.

> **Note:** *All devices must be upgraded to version 1.9 before remote software installation is available.*

In the ECU, go to Setting> General> Automatically Update Software to enable. Once enabled, the devices can be remotely updated with the next version of software. Devices will receive the software update from the Primary. When you install software on the Primary, the software will first be copied to its hard drive.

With the devices synchronized with the Primary, install the new version of software onto the Primary. All devices will lose their connection with the Primary at that time. When the Primary comes back online after installing the software, all the connected devices will be forced to update their software before they can reconnect with the Primary.

#### Remote Power On/Off

In a multi-console system, it is possible to power on and off devices remotely. Remote Power On and Remote Power Off must be enabled on each device before it can receive the power on and off commands. In the ECU go to Settings> Network> Enable Remote Power Off and Enable Remote Power On. The default setting for both is "Disabled".

> **Note:** *Original Eos consoles cannot be remotely powered on.*

The Remote Power commands are sent from the browser. The command for Power On is sent from Browser> Network> Power On MultiConsole System, and the command for Power Off is from Browser> Network> Power Off MultiConsole System.

> **Note:** *Only devices that synchronize with the Primary will be available for Remote Power On and Off.*

# Eos Family User Manual v3.2.0 — Chapitre 05 : Setup

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 5
## Setup
### About Setup

This section describes the processes involved in changing your system, user, and device settings to meet your preferences.

To enter the setup screen, select [Displays], then {Setup}, or navigate to Setup via the browser. Apex and Element Classic console users can also use the dedicated [System] and [Setup] hardkeys.

The CIA will repaint to display the following setup sections and their subsections:

-   *Setup > System (below)*

-   *Setup > User (on page 220)*

-   *Setup > Device (on page 223)*

Selecting a subsection will display any associated settings fields. To change the setting for any of these fields, press the field in the CIA to activate it. If the field requires data, enter it from the keypad, pop-up, or dropdown menu. If the field is a toggle state, one press of the button will switch the field to its other state.

> Additional settings not found in Setup may be found in the ECU. See *About the Eos* *Configuration Utility (on page 576)*.

### Setup > System

This section provides settings for the entire system. Changes to these settings are system-wide and will impact all connected consoles and clients connected to the system.

#### System

##### Num of Channels

You may use this field to set the number of channels in your console to the number of channels in your system. Eos supports a maximum of 99,999 channels. The default is 5,000. Only 32,768 channels can exist in the patch, but they can be distributed throughout the entire 99,999 channel count. Enter the number of channels for your system using the keypad. This entry must be confirmed with the [Enter] key.

> **Note:** *Every part in a multipart channel will count as an additional channel for the channel count total.*

Element Classic consoles are limited to either 250 or 500 total channels, which can be numbered up to 10,000.

##### Dim. Dbl. Offset

This allows you to set the address offset for dimmer doubling. The default for this is 20000, to match the Net3 standard offset, including Sensor dimming software. For dimmer doubling over Local DMX, this value should be set to 256.

##### {Create Virtual HSB}

Allows you to disable creation of virtual hue and saturation parameters. Disabled by default.

When Virtual HSB controls are disabled, the hue and saturation columns will not display in Table view. You will not be able to record just the Hue or Saturation values into a cue, submaster, preset, or palette, and you cannot apply an effect to Hue and Saturation. You will still be able to control Hue and Saturation from the encoders, ML Controls, Color Picker, and the command line.

##### {Display Colors In D65}

Displays colors of gels and current light output on the encoder display, color picker, pixel map, and magic sheet link to channel color using a D65 white point. Enabled by default.

Disabling this option switches Eos back to using a D50 white point, as in software versions prior to v3.0.0.

##### {Zones}

> Enables or disables *Augment3d Zones (on page 537)*. Enabled by default.

##### Home Preset

Allows you to specify a preset that will be used as the home level for all non-intensity parameters in the preset, instead of the fixture library defaults. This preset will be applied for all "Go to Cue Out" and home commands. Channels not included in the assigned home preset will continue to home to their library defaults.

##### Preheat Preset

Allows you to specify an intensity preset that will be used as the preheat level for all channels assigned to use \"Preset\" as a preheat value in Patch. See *Patch > Attributes (on page 182)*.

##### Metric / Imperial

Specifies the units used for distance measurements. Choose between Meters, Feet, or Feet/Inches. Defaults to Metric.

##### System Startup Macro

This field allows you to set up a startup macro that will trigger after the console initialization has completed.

##### System Shutdown Macro

This field allows you to set up a shutdown macro that will trigger at power off.

> **Note:** *The system shutdown macro does not trigger when the primary console exits to the welcome screen (shell).*

##### Disconnect Macro

> **Note:** *Not available on Element Classic.*

This field allows you to set up a disconnect macro that will trigger when the primary disconnects from its backup, or when a backup disconnects from the primary.

#### Session

This section controls your system\'s ability to receive FDX2000 dimmer feedback over the network.

##### Backup Auto Take Control

When enabled, if the primary is not seen on the network for a few seconds, the backup becomes the new primary. Disabled by default. Starting a new show file will also disable this setting.

##### {FDX2000}

Enables or disables FDX2000 reception. Disabled by default.

##### FDX2000 Broadcast Mode

Choose between Directed or Limited broadcast. Defaults to Directed.

##### FDX2000 Subnet

Assign a particular subnet for FDX2000 transmission.

#### Cue Settings

##### {Auto-Mark}

> **Note:** *This option is not available on Element 2 and Element Classic.*
>
> Enables or disables AutoMark. Disabled by default. See *AutoMark (on page 284)*.

##### Mark Time

This field allows you to set the time that mark instructions will use, and is disabled by default. When disabled, mark instructions will use cue timing unless overridden with discrete timing.

When you enter a mark time in setup, all NPs that mark (either via referenced marking or AutoMark) will use this time. The only way to override the mark time in Setup is to use discrete timing.

Select {Mark Time}[Enter] to clear the field and disable the default mark time. See *Mark (on page 283)*.

##### Preheat Time

If this option is disabled, the cue's up intensity time will be used when preheating. The default setting is "Disabled".

##### Cue Default Times

This area allows you to set the default cue times for the parameter categories of your system. To change a time, touch the parameter category button in the CIA and enter the desired time on the keypad. To set a time for all categories at once, select the first category and press [Thru]. Pressing [At] selects manual times.

The categories for which you may set default times are:

-   Intensity Up

-   Intensity Down

-   Color

-   Focus

-   Beam

> **System > Show Control**

This section allows you to adjust settings for MIDI show control, time code (MIDI or SMPTE), analog, and serial functions. For more information on using show control with your system, see *About Eos Family Show Control (on page 596)*

##### SMPTE

###### {SMPTE Time Code Rx}

Allows your console to receive SMPTE time code. Disabling this setting will disable all time code lists that have a SMPTE source. Enabled by default.

###### Resync Frames

Allows you to configure how many frames between 1 and 30 need to be synced before time code starts running. Defaults to 2 frames.

##### MIDI

###### {MSC Receive}

Toggles whether the console can receive MIDI Show Control from an external source. Disabled by default.

###### {MSC Transmit}

Allows the console to send MSC messages for actions taken on the console, such as cue actions, macros firing, and submaster bumps. Disabled by default.

###### MSC Rx Device ID

Configures the MIDI channel for the console to receive MIDI Show Control information. Only MSC data with the same device ID will be received. A device ID can be from 0-126. MSC commands can be sent to ID 127, which is the All Call device ID. While Eos cannot be set to ID 127, it will respond to commands sent to the All Call device ID.

-   MSC Rx Device ID [5] [0] [Enter]

###### MSC Tx Device ID

Choose the devices through which the console will send MIDI data. When set, the console will transmit MIDI data to any Net3 Show Control or Response MIDI gateway that has a matching "ACN MIDI Tx ID." The console will send the MIDI data over an ACN connection to the gateways.

-   MIDI Tx Source ID [2][5] [Enter]

###### MIDI Cue List

Specifies the cue list that the console will use to send MSC data. If left blank and MSC Tx is enabled, all cue lists will generate MSC events. Otherwise, only the particular list (or lists) selected will fire MSC events. Multiple cue lists can be selecting using [Thru] and [+].

###### MIDI Rx Source ID

Choose the devices from which the console will receive MSC. When set, the console will respond to MSC data from any Net3 Show Control or Response MIDI gateway that has a matching "ACN MSC Rx ID." Gateways will send the MIDI data over an ACN connection. The setting needs to match or at least contain the MSC Rx ID of built-in MIDI ports to enable them.

-   MSC Rx Source ID [2] [5] [Enter]

-   MSC Rx Source ID [1] [Thru] [1][0] [Enter]

###### MIDI Tx Source ID

Allows you to choose the device which the console will send MSC to.

###### {Network List Receive}

Enables or disables whether the console can receive incoming MIDI, UDP, and OSC. Enabled by default.

###### {MIDI Time Code Rx}

Enables or disables whether the console can receive MIDI Time Code. Enabled by default.

###### {MIDI Raw Send}

Enables or disables whether the console can send raw MIDI strings. Enabled by default.

###### {MIDI Ignore Active Sensing}

Enables or disables whether Eos ignores incoming active sense MIDI. Active sense messages (hex 0xFE) may be sent by MIDI-capable musical instruments to indicate they are still active in the system. Eos cannot respond to these messages, but will include them in logs if not ignored. Enabled by default.

###### {MIDI Ignore Beat Clock}

Enables or disables whether Eos ignores incoming beat clock MIDI. Beat clock messages (hex 0xF8) may be sent by MIDI-capable musical instruments to synchronize tempo between devices. Eos cannot respond to these messages, but will include them in logs if not ignored. Enabled by default.

##### OSC

###### {OSC RX}

Globally enables receiving OSC, excluding third party OSC connections. Enabled by default.

###### {OSC TX}

Globally enables transmitting OSC, excluding third party OSC connections. Enabled by default.

###### OSC UDP RX Port

Specifies the UDP port that the console will listen to for OSC receiving strings. Multiple ports can be assigned. A space needs to be used to separate the addresses.

###### OSC UDP TX Port

Sets the UDP destination port to which the console will send OSC strings. Multiple ports can be assigned. A space needs to be used to separate the addresses.

> **Note:** *ETC recommends using 8000 and 8001 respectively for port numbers. Remember that when setting port numbers on your external device that they should be set to the opposite of what Eos is set. For example, if {OSC UDP TX Port} on Eos is set to 8000, then the RX (incoming) port on your external device needs to be set to 8000, and vice versa.*

###### OSC Cue Recieve String

Allows the user to specify a different incoming OSC string format for integration with other applications. Use %1 in the string format as cue number and %2 as the cue list number.

###### OSC Cue Send String

Allows the user to specify a different outgoing OSC string format than the standard Eos implicit string for integration with other applications. The following options can be used:

-   %1 - cue number

-   %2 - cue list number

-   %3 - cue whole number

-   %4 - cue point number

-   %5 - cue label

###### OSC TCP Server Ports

Allows the user to specify custom port numbers for multiple OSC TCP connections. Multiple ports can be entered, separated by a comma or a plus.

###### OSC UDP TX IP Address

Sets the destination IP address or addresses to which the console will send OSC strings. Multiple ports and IP addresses can be entered, separated by either a space, comma, or semicolon.

> **Note:** *Be careful when using a network with a DHCP server. If your external device reboots or is issued a new IP address from a DHCP server, it will no longer receive OSC strings from Eos until you change this setting to match your new IP address at your external device.*

###### OSC TCP Mode

Choose between Packet Length (v1.0) and SLIP (v1.1).

##### UDP Strings

###### {String RX}

Enables or disables receiving strings on all Serial RX formats. Enabled by default.

###### {String TX}

Enables or disables sending strings on all serial TX formats. Enabled by default.

###### {String MSC TX}

When enabled, this setting will cause the console to send serial strings when certain actions happen at the console. See *Sending From User Events*.

###### String RX Source IDs

Choose the Net3 I/O or Response Serial gateways through which the console will receive serial strings. When set, the console will receive serial from any Net3 I/O or Response Serial gateway that has a matching "ACN Serial Group ID." The gateway will send serial data over an ACN connection to the console. This only affects serial traffic from gateways and not network UDP messages, ACN strings, or OSC. Source IDs can be from 1-32. Multiple group IDs can be selected by using [Thru] and [+].

###### String TX Source IDs

Choose the Net3 I/O or Response Serial gateways through which the console will transmit serial string data. When set, the console will transmit serial to any Net3 I/O or Response Serial gateway that has a matching "ACN Serial Group ID." The console will send the serial data over an ACN connection to the gateways. This only affects serial traffic to gateways and not network UDP messages, ACN strings, or OSC. Serial Group IDs can be from 1-32. Multiple group IDs can be selected by using [Thru] and [+].

###### String RX Source Name

Allows the user to specify a comma separated list of names for receiving strings (from Paradigm, for example).

###### String TX Source Name

Allows the user to specify a list of specific comma-separated names of devices to send strings to (for use with Paradigm, for example).

###### String RX Port

Specifies the UDP port that the console will listen to for receiving strings.

###### String TX Port

Setting for the UDP destination port that the console will send strings to.

###### String TX IP Address

Sets the destination IP address that the console will send UDP strings to. Multiple IP addresses can be entered, separated by either a space, comma, or semicolon. Port numbers can also be appended to IP addresses with a colon to send UDP strings specifically to that port (10.101.2.99:8001, for example).

A combination of UDP and ACN devices is not supported. See *String Interface* for more specific configuration information.

##### Contacts

###### {Analog Inputs}

This is a master setting for receiving analog inputs from a Net3 I/O or Response Analog I/O Gateway, or the built-in I/O port when available. When disabled, it will no longer trigger any analog input actions on any event lists. Enabled by default.

###### {Relay Outputs}

This is a master setting for triggering external relays from a Net3 I/O or Response Analog I/O Gateway, or the built-in I/O port when available. When disabled, it will no longer affect any external relays normally triggered from the console via cues, submasters, or macros. Enabled by default.

#### Mobile Apps

##### {Allow App Connections}

Allows Net3 RFR, aRFR, iRFR, SpaceBuilder, and third-party OSC applications to connect to Eos. Enabled by default.

##### {Visible to Mobile Apps}

Allows your console to be automatically detected by WiFi mobile RFR applications. If disabled, you will need to manually configure a connection to your console. Enabled by default.

> **Note:** *The application will identify the consoles by their name and IP address, so it is useful to know the device names and addresses to ensure that you are connecting to the right one.*

#### Partitions

This display shows any recorded partitions, including the four default partitions, and controls for enabling or disabling partitioned control. For more information, see *Using Partitions (on* *page 563)*.

#### Users

In this display, you can set the user ID for the console under User ID by entering a number from the keypad.

The table displays all current users IDs and their online status. Selecting a user number allows you to select the user, or set them as the current user. Augment3d can be enabled or disabled per user. Name fields can also be edited from this screen.

Users can be added, copied, and deleted with the softkeys on the right. For more information on user ID see *User ID (on page 568)*.

##### Recall User Settings

When multiple users are in a system, this option allows you to select a user from which to recall the following settings:

-   Manual Time

-   Sneak Time

-   Go to Cue Time

-   Back Time

-   Assert Time

-   Timing Disable Time

-   Off Time

-   Release Time

-   Record Confirm

-   Delete Confirm

-   Cue Only

-   Auto Playback

-   Plus %

-   Minus %

-   Level

-   Update Defaults (all)

-   Partition

-   Highlight

-   Lowlight

-   Highlight Remdim

-   Live Remdim Level

-   Preserve Blind

-   Encoder Degrees Per Rev

-   Encoder Percent Per Rev

-   Preserve Native (Patch Setting)

-   Gel Match Type (Color Picker Setting)

-   Gel Swatch Type (Color Picker Setting)

-   Pop-up Magic Sheet

-   Pop-up Nav Lock

### Setup > User

This section provides settings for a specific user. Changing these settings does not impact other users on the network.

To change the setting for any of these fields, select the button in the CIA to activate it. If the field requires data, enter it from the keypad. If the field is a toggle state, one press of the button will switch the field to its other state.

#### Record Defaults

##### Track

> Switch between Tracking and Cue Only Modes (see *Tracking vs. Cue Only (on page 7)*). Defaults to Tracking Mode.

##### {Record Confirm}

Enable or disable the confirm action when storing over a previously recorded target. Enabled by default.

##### {Delete Confirm}

Enable or disable the required confirmation before any delete command is executed. Enabled by default.

##### {Auto Playback}

When enabled, this feature automatically plays back cues and submasters as they are stored and releases manual control. For submasters to automatically play back, the slider must be at full. When auto playback is disabled, all manual levels are maintained and cues must be loaded and executed on playbacks. Enabled by default.

##### {Record Effects In Presets}

Enables or disables whether running effects are recorded into presets. Disabled by default.

##### Update Mode

> This field allows you to select a default update mode (see *Update Dialogue Box (on page 339)*). The default is "Make Absolute".

##### {Break Nested}

This setting allows you to enable/ disable the update modifier break nested. Enabled by default.

##### {Update Last Ref}

Enable or disable the update modifier update last ref. Enabled by default.

##### {Intensity Cue Only}

Enable or disable intensity cue only. When enabled, intensity updates will be cue only, regardless of the tracking mode of the desk. Non-intensity parameter updates will continue to follow tracking vs cue only. Defaults to disabled.

##### Emergency Mark

> **Note:** *This option is not available on Element 2 and Element Classic.*

Can be used to automatically set a mark flag if you had not previously done so. If using Earliest and no cue with a mark flag has already been set, Emergency Mark will set a mark flag.

Emergency Mark can be set to either Earliest or Latest. Latest is the default setting.

-   If set to Earliest, Emergency Mark will set the mark flag on the earliest cue after the cue which fades the intensity out for the selected channel.

-   If set to Latest, Emergency Mark will not set a mark flag. It will instead create a broken mark, which will display an x in the previous cue in the Playback Status Display.

#### Manual Timing

##### Manual Timing

In this section you may change the default times for manual changes to occur in live. Times can be set for each parameter category (Intensity Up, Intensity Down, Focus, Color, and Beam).

You may use the [Thru] key to enter a value for all categories.

-   {Int Up} [Thru] [9] [Enter]

The default for each of these is 0 seconds.

##### Default Times

In this section you may change the default times for sneak commands and the respective feature response times based upon parameter category. The default for these is 5 seconds, except for back time, which uses a default of 1 second. You can assign separate timing values to the Release and Off functions.

You can assign [Cue] as a timing value for the {Go to Cue Time} and {Back Time} The syntax,

{Go to Cue Time} [Cue] [Enter] or {BackTime} [Cue] [Enter] will assign cue as the timing value.

When [Go To Cue] [n] [Enter] or [Back] is used, the fade will happen in the time set in the destination cue.

You can assign a separate time value for [Timing Disable]. When a fader has been set to timing disable mode, cues will use the time set in Setup. The default time is 0.

#### Manual Control

##### Encoders

This section allows you to define how much a parameter changes when an encoder is rotated one full revolution.

> **Note:** *Hold down [Shift] while moving the encoder for fine control. Releasing the [Shift] key will restore the encoder to its default mode.*

###### Percent Per Rev

How much any associated parameters (excluding pan and tilt) change in one full revolution of an encoder. Measured in a percentage of the parameter\'s entire range. Defaults to 35.

###### Degrees Per Rev

How much the pan and tilt parameters change in one full revolution of an encoder. Measured in degrees. Defaults to 30.

###### Mini Percent Per Rev

> **Note:** *This option is only applicable to Eos Apex consoles.*

How much any associated parameters change in one full revolution of a mini encoder. Defaults to 35.

###### Scroll Percent Per Rev

> **Note:** *This option is only applicable to Eos Apex consoles.*

How much any associated parameters change in one full revolution of an endless fader wheel. Defaults to 125.

##### Button Values

This section allows you to specify the values for certain buttons or settings used in manual control. The following settings are available:

-   Level - sets the value for the [Level] key. Any value between 0-100 may be entered. Defaults to 80.

-   Plus% - sets the level for the [+%] key, which will increase the selected channel by the set percentage. You can assign +% to values that have up to five digits. Defaults to 10%.

-   Minus% - sets the level for the [-%] key, which will decrease the selected channel by the set percentage. You can assign -% to values that have up to five digits. Defaults to 10%.

-   {Live RemDim Level} - enables or disables RemDim. Disabling RemDim causes [Rem Dim] to return an error when used in Live. Enabled by default.

-   Live RemDim Level - allows you to set the level for all remainder dim commands in live. Defaults to 0. An intensity level or a preset can be assigned in this field.

##### Highlight

This section allows you to specify highlight preferences. The following settings are available:

-   Highlight Preset - the preset that will be used for any highlight commands.

-   Lowlight Preset - the preset that will be used for any lowlight commands.

-   Highlight Rem Dim - enables a remainder dim when in highlight mode, thereby temporarily dimming any channel not participating in the High/Low. An intensity level or a preset can be assigned in this field. Channels not in highlight or lowlight that are not included in the preset are not affected.

##### Encoder Map

This section allows you to specify a custom encoder mapping to be used as the default for all fixtures. If left blank, any fixture types without a custom map assigned will use the default Eos encoder mapping.

> For more information on custom encoder maps, see *Custom Encoder Maps (on page 126)*.
>
> **User > Displays**

##### {Preserve Blind Cue}

This enables the console to display the last selected cue in blind when you return to blind. Disabled by default.

##### {Blind Next/Last Affects Target}

When enabled, in Blind the Next and Last commands will always apply to channels, if a channel selection is on the command line. Disabled by default.

##### Popup Magic Sheet

> Assigns a magic sheet (see *About Magic Sheets (on page 476)*) that can be accessed via the
>
> *Quick Access (on page 95)* tools.

##### {Popup Nav Lock}

> Enables or disables the zoom and scroll navigation for your *{Popup Magic Sheet} (on page 95)*. Enabled by default.

##### {Augment3d Display Behavior}

The following Augment3d display behaviors are available:

-   Normal Display - the display will behave the same as a display tab.

-   A locked tab will not be skipped.

-   A single click on the tab will draw focus to that tab.

-   Channel Display - this mode uses the following rules:

    -   When focus is drawn to the playback status display, an Augment3d channel display will be brought to the front.

    -   [Shift] & [Live] will cycle through Augment3d channel displays alongside Live channel displays.

    -   Pressing [Live] or bringing a Live tab into focus will restore your last focused Augment3d channel display.

    -   Augment3d channel displays in the locked frame will not be skipped when using the [Tab] key to cycle through tabs.

-   Control - the display will behave the same as a controls tab.

-   Locked tabs will be skipped.

-   A single click will not draw focus.

-   A double click will draw focus to the tab.

##### {Display Fader Ribbon}

Element Classic only. Enables or disables the ribbon display showing the status of the faders. When disabled, the fader ribbon will not display. Enabled by default.

### Setup > Device

This section provides settings for the specific device being used. Changing these settings does not impact other controllers on the network.

To change the setting for any of these fields, select the button in the CIA to activate it. If the field requires data, enter it from the keypad. If the field is a toggle state, one press of the button will switch the field to its other state.

#### Config

##### Device Name

> **Note:** *Changes to this setting will require a restart. A warning message indicating a needed restart will display.*

This specifies the name the console will use to identify itself on the network to other devices. Examples might be Booth Desk and Tech Table. This setting is also available in the ECU.

#### Network

> **Note:** *Additional network settings are available via Settings > Network (on page 583) in the ECU. Additional output protocol settings are available via Patch*

-   *Protocols (on page 186).*

*(figure omise)*{width="5.816278433945757in" height="2.4260411198600176in"}

These are the settings that determine the method to get an IP address and / or the actual IP address information that Eos uses for network communication.

On ETCnomad, these settings are determined by Windows or macOS, and cannot be edited here.

> **Note:** *Consoles with more than one network interface card (NIC) should avoid connecting more than one port to the same network or subnet.*

##### Status

A port is \"online\" in green if it is configured, connected to a network and operational. If any of those conditions is not true, it reports as "offline\" in red.

##### IP Address

Allows you to assign a static IP address if \"Obtain IP Automatically\" is disabled. Select the field to open a pop-up allowing you to enter the address.

> *(figure omise)*{width="3.3125in" height="3.25in"}

The following is a list of the default IP addresses:

+-----------------+----------------+-----------------+----------------+--------------+
| > Console       | Port 1         | Port 2          | Port 3         | > Port 4     |
+=================+================+=================+================+==============+
| Apex 20         | 10.101.190.101 | 192.168.190.101 | 172.16.190.101 | 10.0.190.101 |
+-----------------+----------------+-----------------+----------------+--------------+
| Apex 10         | 10.101.192.101 | 192.168.192.101 | 172.16.192.101 | 10.0.192.101 |
+-----------------+----------------+-----------------+----------------+--------------+
| Apex 5          | 10.101.191.101 | 192.168.191.101 | 172.16.191.101 | 10.0.191.101 |
+-----------------+----------------+-----------------+----------------+--------------+
| Eos Ti          | 10.101.92.101  | 192.168.92.101  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Gio             | 10.101.91.101  | 192.168.91.101  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Gio @ 5         | 10.101.98.101  | 192.168.98.101  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Ion Xe          | 10.101.100.20  | 192.168.100.20  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Ion Xe 20       | 10.101.100.30  | 192.168.100.30  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Ion Xe RPU      | 10.101.96.201  | 192.168.96.201  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Element 2       | 10.101.99.101  | 192.168.99.101  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| ETC Puck        | 10.101.185.101 | 192.168.185.101 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| RPU3            | 10.101.93.101  | 192.168.93.101  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| RVI3            | 10.101.86.101  | 192.168.86.101  |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Ion Classic     | 10.101.100.101 |                 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Ion RPU         | 10.101.96.101  |                 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Element Classic | 10.101.97.101  |                 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Eos Classic     | 10.101.90.101  |                 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| Eos Classic RPU | 10.101.95.101  |                 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+
| RVI             | 10.101.85.101  |                 |                |              |
+-----------------+----------------+-----------------+----------------+--------------+

If \"Obtain IP Automatically\" is enabled, this field will display the IP address that is being used by the console (whether it is served via DHCP or a self-generated link-local IP address and subnet mask).

##### Subnet Mask

Allows you to assign a static subnet mask if \"Obtain IP Automatically\" is disabled. The default subnet mask is 255.255.0.0.

If \"Obtain IP Automatically\" is enabled, this field will display the subnet mask that is being used by the console (whether it is served via DHCP or a self-generated link-local IP address and subnet mask).

##### Default Gateway

Allows you to assign a static gateway IP address if \"Obtain IP Automatically\" is disabled.

Eos consoles controlling a Net2 system should use their IP address as the default gateway. All other consoles should default to 10.101.1.1.

If \"Obtain IP Automatically\" is enabled, this field will display the gateway IP address that is being used by the console (whether it is served via DHCP or a self-generated link-local IP address and subnet mask).

##### Obtain IP Automatically

> **Note:** *ETC recommends the use of a static IP address for compatibility with other ETC devices, though the needs of your particular installation may vary.*

When enabled, this allows the console to request an IP address from a DHCP server during startup. If one responds, it will use the assigned IP address.

If no DHCP server is available, the console will default to a self-generated link-local IP address in the range of 169.254.X.X. The IP address used by the console in this configuration may change dynamically as needed. A change should typically only occur when there are changes to the network configuration or to resolve an IP address conflict.

Enabling or disabling this setting will require you to reboot the console for the new setting to take affect.

> **Note:** *You cannot set the console to receive an IP address via DHCP and act as a DHCP server at the same time. It can either send dynamic addresses or receive them, but not both at the same time.*

##### Physical Address

The physical address is the MAC address, a unique device identifier that cannot be modified.

##### Network Interface Delay (Required)

> **Note:** *This option is not available on ETCnomad.*

When {Required} is enabled, the console will wait for the network connection to be fully initialized before launching the Eos application.

When enabled, a launching window will display on start-up. If a network connection is not made, you will have the option to {Start Anyway}, {Start Offline}, or to {Cancel}.

-   {Start Anyway} - launches without a network interface. Only User 1 is displayed above the CIA.

-   {Start Offline} - starts in offline mode.

-   {Cancel} - remains in start-up without launching into the Eos application.

#### Output Protocols

*(figure omise)*{width="5.812665135608049in" height="0.9739577865266842in"}

> **Note:** *Apex consoles, Windows 10 consoles, and ETCnomad software do not support Net2 or AVAB UDP output protocols.*
>
> For additional protocol settings, see *Patch > Protocols (on page 186)*.

##### sACN

Enables or disables output of the sACN protocol.

##### ArtNet

Enables or disables output of the Art-Net protocol.

#### Interface Protocols

*(figure omise)*{width="5.814990157480315in" height="1.9797911198600175in"}

##### FDX2000 Feedback

Allows your console to receive FDX2000 dimmer feedback over the network. Disabled by default.

##### Mobile Apps

Enables or disables the connection of WiFi mobile RFR applications to Eos. Enabled by default.

##### UDP Strings and OSC UDP

Allows the selected port to send and receive UDP and OSC strings. Enabled by default.

##### OSC TCP

Allows the selected port to send and receive OSC via TCP port 3032. Select the OSC TCP format. Defaults to OSC 1.0.

> **Note:** *Check the documentation for the OSC device you wish to use over a TCP connection to see which mode it supports.*

-   OSC 1.0 (packet-length headers)

-   OSC 1.1 (SLIP)

##### Third Party OSC

Enables or disables dedicated server port 3037 for use with third-party OSC applications. Enabled by default.

##### Restore Defaults

*(figure omise)*{width="5.866733377077865in" height="2.499374453193351in"}

Selecting the title header of each port allows you to access a restore defaults overlay, displaying a comparison of the current settings, those saved in the show file, and the defaults, allowing you to choose which to keep.

#### Local Output

> **Note:** *Changes to these settings may require a restart. When required, a warning message will display.*

The table displays all connected device names and their port, address, RDM, doubling, and speed information. The following settings can be edited by selecting a cell:

-   Address - sets the starting address for the port.

-   RDM - enables RDM on the port.

-   Doubled - enables dimmer doubling on the port.

-   Speed - choose a port speed from maximum, fast, medium, or slow. The speed may need to be adjusted for certain devices. Defaults to Maximum.

##### {Output In Client Mode}

When enabled, all client consoles will calculate and output DMX levels through their local DMX ports, including DMX ports provided by Gadget / Gadget II / Programming Wing. Defaults to disabled.

##### Dim. Dbl. Offset

> See *Dim. Dbl. Offset (on page 212)*.
>
> **Device > Show Control**

##### USB MIDI/SMPTE

The table displays all connected device names and whether they are receiving or transmitting. In the right two columns, this behavior can be toggled enabled or disabled, and the displayed timecode source ID can be edited.

###### {Local MIDI/SMPTE Rx}

Enables or disables the console\'s ability to locally receive MIDI or SMPTE. Enabled by default.

###### {Local MIDI Tx}

Enables or disables the console\'s ability to locally transmit MIDI. Enabled by default.

###### {USB MIDI/SMPTE}

Enables or disables local USB connection to supported MIDI or SMPTE devices. Disabled by default.

**Note:** *This setting must be enabled for virtual MIDI devices on ETCnomad.*

##### Contacts

Contact closures require DC voltage, which is supplied by the console on pins 14 and 15.

*(figure omise)*{width="0.6729407261592301in" height="0.53625in"}*(figure omise)*{width="1.3367465004374453in" height="0.92625in"}

###### In Source Id

Specifies which analog input group ID the console should receive contact closures from.

###### In Address 1-4

Specifies up to four contact addresses within the analog input group to monitor for closures.

###### Relay Out Source Id

Specifies the source ID for the relay output.

###### Relay Out Address

Specifies the address for the relay output.

##### USB Serial

The table displays all connected device names and their baud rates, parity, and stop bits.

###### {Response Serial USB}

Enables or disables local USB connection to Response MIDI and SMPTE devices. Enabled by default.

##### OSC

Enables or disables use of OSC USB devices, such as Lighthack. Enabled by default. Disabled by default on macOS.

#### Face Panel

##### Input Devices

###### {Swap Pan/Tilt}

Trackball settings to swap the pan and tilt parameters. Defaults to disabled.

###### {Reverse Pan}

Reverses the range of the pan parameter. Defaults to disabled.

###### {Reverse Tilt}

Reverses the range of the tilt parameter. Defaults to disabled.

###### {Spacebar [Go]}

Allows you to enable the spacebar on an external keyboard as the hotkey for [Go]. Defaults to enabled.

###### {Use Shift as Eos Shift}

Allows the SHIFT key on an alphanumeric keyboard to be used as the console\'s [Shift] key. The Z key on an alphanumeric keyboard will function as the [Shift] key. Defaults to enabled.

###### {Hide Mouse}

With hide mouse enabled, if the mouse is left idle for 10 seconds, the cursor will go away. Once the mouse is used again, the cursor will return. Defaults to disabled.

###### Delay

Sets the delay for keystroke input from an external device.

###### Speed

Sets the keystroke speed from an external device.

##### Sounds

Disabled by default. When enabled, allows you to adjust the volume level of the following system alert sounds:

-   Error

-   Advisory

-   Click

-   Cue Alert 5s Warning All sounds default to 0. ***Haptics***

> **Note:** *This option is only applicable to Eos Apex consoles.*

Allows you to enable or disable haptic feedback.

#### Fader Wing Layout

> **Note:** *This option is not available on Element 2.*

This screen allows you to manually configure the positions of fader wings connected to your console. The console will default to configuring the wings on its own. To manually configure, you must click on the {Manual Config. Off} softkey.

Clicking on the {Manual Config. Off} button turns manual configuration on and displays the Fader Wing Configuration screen.

Clicking {Identify} will display numbers on each wing's display to aid in configuration. The numbers do not identify the wings as to their actual order. Order is determined from left to right. The left most wing will contain the first faders.

*(figure omise)*{width="5.015624453193351in" height="2.340624453193351in"}

Click and drag the wings to match your physical layout. Click {Apply} to save the changes. Clicking {Reset} will restore to the last saved configuration. Clicking {Manual Config. On} will turn off manual configuration and will require a restart of the application before the console will automatically configure the wings.

#### Wing Paging Groups

This screen allows you to organize both internal and external faders into wing paging groups. All configuration and navigation settings are applied to any fader wings or banks included in a group.

-   ID - a unique identifier assigned to all connected internal and external faders, which appears on the fader bank displays while in this menu.

-   Type - information about the connected fader wing or bank.

-   Group - select in this column to edit the group number for a wing or bank.

**Note:** *Internal banks default to Group 1. External wings default to Group 2.*

When advancing fader pages by group, Group 1 is the default used with [Fader Page] or [+]. To control a specific group, you can use [Fader Page] [Group] and the paging group number.

#### Brightness Settings

*(figure omise)*{width="3.9544706911636047in" height="1.2666666666666666in"}

This menu allows you to adjust the brightness and contrast settings for your console\'s face panel, as well as any internal monitors, supported external monitors, fader wings, and task lights. All sliders have a range from 0% (dimmest) to 100% (brightest).

At any time, holding [Displays] will display a pop-up of this menu on your console screen.

##### Main

The Main brightness slider can be used to set an overall limit to the brightness of any other linked brightness settings, and defaults to 100%. This slider can also be controlled by holding [Displays] and scrolling the level wheel.

###### Show All

Brightness sliders not pertinent to your console\'s hardware setup are disabled and grayed out by default. {Show All} enables control of all sliders, regardless of your console, allowing you to record presets for specific hardware.

###### Presets

Up to three brightness presets can be recorded, containing any combination of brightness levels from this menu. To record a preset, hold down the preset button you wish to overwrite until it displays Hold to Record. Continue holding until the preset button displays Recorded.

Presets are stored in the show file with the device configuration.

###### Extinguish

This button instantly sets all brightness settings to 0%, and darkens all console screens and buttons (excepting the power button). [Displays] pulses to indicate this mode is enabled. Click or tap onscreen, or press [Displays] to exit extinguish mode.

###### Link to Main

This option allows you to link any combination of sliders to the Main slider. Linked sliders display a link icon underneath. Unlinked sliders is display a slashed link icon.

*(figure omise)*{width="3.9544706911636047in" height="1.2666655730533682in"}

When {Link to Main} is selected, any linked brightness sliders are outlined in yellow. Unlinked sliders are not outlined, and display a broken link icon underneath. Click the icon to toggle between linked and unlinked. LCD Contrast sliders cannot be linked.

###### {Control External Monitors}

Enables or disables control of external monitors that support Display Data Channel / Command Interface (DDC/CI) via Display Port.

##### Monitors

The Internal slider controls the brightness of any internal console monitors.

If Control External Monitors is enabled, the External slider will control the brightness of any connected external monitors that support Display Data Channel / Command Interface (DDC/CI) via Display Port.

Both sliders default to 100%.

##### Face Panel

These sliders control the brightness of your console\'s face panel backlit keys, and any built-in displays or faders. All default to 50%.

##### Task Lights

This slider controls the level of any task lights connected to your console, such as Littlites, and defaults to 50%.

##### USB Wing Displays

These sliders control the brightness, backlight level, and contrast of the displays of any connected USB fader wings. Selecting {Invert} will invert the LCD. All sliders default to 55%.

> **Note:** *Additional sliders may appear to control brightness settings for any additional detected displays.*

##### Ion/Xe Display

These sliders control the backlight level and contrast of any internal Ion Xe and Ion Classic LCDs.

##### Apex Rackmount

These sliders control the display brightness and highlight level of any Apex rackmount devices.

#### Augment3d

The table displays the status of running Augment3d instances, and associated information.

To select which instance of Augment3d the console uses, highlight the desired instance and click the {Connect to Server} button. To switch from a tethered computer back to the console, highlight the instance with address \"Local\" and select {Connect to Server}.

> For more information on Augment3d Tether, see *PC / Mac (Tether Mode) (on page 496)*.

##### Device Enable A3D

Enables or disables Augment3d on the current device. Enabled by default.

> **Device > Displays**
>
> See *Live and Blind Configuration Menu (on page 104)* and *Playback Status Display Configuration (on page 112)* for additional display settings.

##### {Show Ref Labels}

When enabled, referenced record targets (such as presets or palettes) with labels will have their labels displayed rather than their target type and number. Enabled by default.

{Show Reference Labels} is a global setting that will affect all displays. For some displays such as live and blind, {Show Reference Labels} can be enabled at the individual tab level by accessing the tab\'s configuration menu. This will override the setting in Setup.

##### Default Display Order

> Determines the appearance of the *Workspace Layout Menu (on page 90)*.

##### {In-Cell Editing}

When disabled, this setting prevents changes to be made to the cells in the Live/Blind and Playback Status Displays. {In-Cell Editing} is enabled by default.

> **Note:** *Options in the CIA are not affected by this setting.*

##### {DirSel.Dbl Clk}

When enabled, double clicking a direct select button will act as [Recall From] [Record Target] to place the entire contents of that preset, palette, or step-based effect on stage. Disabled by default.

##### {Force Hide Encoder Ribbon}

> **Note:** *This option is only available on ETCnomad.*

When enabled, forces the encoder ribbon to stay hidden. Disabled by default.

##### Record Target Color Brightness

Sets the brightness of record target colors. Defaults to 50%.

#### Device Profiles

The configuration settings of any device that has joined your Eos system are saved in your show file as device profiles. You can select a profile to overwrite your current device\'s settings entirely, or select partial settings from a profile to copy.

> *(figure omise)*{width="5.850880358705162in" height="3.0766666666666667in"}

The table displays all device profiles saved in the show file, including the online status, name, and type of the associated device in the system.

Device profiles are updated automatically whenever the associated device syncs with the system. The date and time of the most recent update are also displayed in the table.

##### {Bind To Device Profile}

Binds your current device to the profile selected in the table. The associated device must be offline. This will overwrite your current configuration data, including network interface settings, device name, and local output settings, with that from the offline device\'s profile.

After binding your device to a profile, it must be restarted.

> **Note:** *ETCnomad devices cannot be bound to another profile, and may only copy settings.*

##### {Copy From Device Profile}

Choose individual settings from the selected profile to copy to your current device. The following settings can be copied:

-   Network (Protocols) - sACN and Art-Net settings for any Ethernet ports.

    -   These settings can only be copied between like devices, and cannot be copied from ETCnomad to a console or vice versa.

-   Local Output (DMX) - DMX and RDM settings for any DMX ports or Gadgets.

-   Show Control - all settings from *Device > Show Control (on page 229)*.

-   Face Panel - all settings from Device > *Face Panel (on page 230)*.

-   Fader Wing Layout* - all settings from Device > *Fader Wing Layout (on page 231)*.

-   Brightness Settings (Presets) - presets 1, 2, and 3 from Device > *Brightness Settings (on page 232)*. No current brightness levels will be modified.

-   Displays - all settings from *Device > Displays (on page 233)*.

-   Saved Shell Settings* - all settings not migrated from the shell (ECU). See *About the Eos Configuration Utility (on page 576)*.

    -   These settings can only be copied between like devices, and cannot be copied from ETCnomad to a console or vice versa.

Any settings marked with an asterisk (*) will require a restart to apply. Certain settings may be unavailable to copy while the device is online.

##### {Delete Device Profile}

Removes the selected profile from the show file. The associated device must be offline. If the device rejoins your system, its profile will reappear in the list.

#### PDF Settings

##### Paper Orientation

Choose a portrait or landscape PDF orientation.

##### Paper Type

Choose a PDF page size from Letter, 11x17, A2, A3, and A4.

### Diagnostics

This display shows diagnostic information about the console. Diagnostics can be opened via Browser > Setup, or via [Tab] [9][9].

*(figure omise)*{width="5.790242782152231in" height="3.302811679790026in"}

All logged internal and external actions appear in the scrollable command feed at the top of the display, which can be filtered by typing in the box at the top. Additional software, hardware, and network information is displayed in the live-updating fields below.

The following buttons are available on the right side of the display:

-   {Clear} - clears the list of logged items.

-   {Network Info} - outputs network information to the

-   {Incoming OSC} - toggles incoming OSC on or off.

-   {Outgoing OSC} - toggles outgoing OSC on or off.

-   {Log UDP} - toggles UDP logging on or off.

### Console Status

This display shows informational, advisory, or warning messages about your console. Console Status can be opened via Browser > Setup, or through About > Console Status.

*(figure omise)*{width="5.0569816272965875in" height="2.1216666666666666in"}

The Type column displays the category of the message:

+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Informational  | > *(figure omise)*{width="0.37552055993000877in" height="0.37552055993000877in"} | > Instructional data that does not impact console functionality. |
+================+===============================================================================================+==================================================================+
| Advisory       | > *(figure omise)*{width="0.37552055993000877in" height="0.37552055993000877in"} | > Console operation can continue, but with caution.              |
+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Warning        | > *(figure omise)*{width="0.37552055993000877in" height="0.37552055993000877in"} | > Urgent issues that require immediate attention.                |
+----------------+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------+

The Message column displays the message details, and any applicable suggested actions to help resolve the issue. The counter in the top-right displays the total quantity of each type of message. The column on the right indicates whether or not the message has been ignored.

#### Possible Status Messages

##### Hard Drives

-   ALERT / Hard Drive / Show Archive

    -   This device does not have enough available hard drive space to operate safely.

    -   Minimum amount of free space recommended.

    -   The show archive is completely full, future saves to the archive will fail.

    -   Save to an external drive and free space from the archive as soon as possible.

##### Memory Problems

-   Memory Fragmentation / System Memory

    -   Largest Free Block is under a certain amount.

    -   RAM usage is at or above a certain amount.

    -   Application memory usage is at or above a certain amount, which is close to exhausting addressable memory space.

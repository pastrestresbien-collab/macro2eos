# Eos Family User Manual v3.2.0 — Chapitre 30 : Eos Configuration Utility

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 30
## Eos Configuration Utility
>
### About the Eos Configuration Utility

This section covers the Eos Configuration Utility (ECU) and its uses for both system configuration and performing basic level test functions.

You can force the console to boot into the utility instead of the main console application. During the boot process, a countdown timer will appear. You will have 5 seconds to click the timer or to simultaneously hold down "e", "o" and "s" on a connected alphanumeric keyboard. Otherwise, you can enter the ECU from the Eos application via Browser > Exit.

> Consoles can also be assigned to always boot directly into the ECU. See *Open in \"Shell\" E.C.U.* *(on page 578)*.

### ECU Welcome Screen

*(figure omise)*{width="4.984615048118985in" height="1.89in"}

This is the starting screen of the utility. From here you can choose to boot the console in one of several different modes, change various settings, or power off the console.

#### Primary

Starts the console in primary mode.

This is the mode for using a single console in non-networked or networked applications. On a system with multiple consoles, the primary is the console that client and backup consoles synchronize with, making it the source of all information a client or backup console sees on the network.

#### Backup

Assigns the console as a backup to a console in primary mode. Consoles in this mode will not have control of the lighting system unless the primary goes offline. Backup mode requires a primary device be online to synchronize. Once this is done, a backup console intakes all show data for use in the event that it needs to take control of the lighting system.

The main difference between backup and client modes is what happens in the event of primary processor failure. If the primary fails, a backup will ask if you want it to take control of the system or troubleshoot the problem. You can set the backup to automatically take control. When the primary remains in control, the backup will behave as a client would.

> For more information on backup systems, see *About Multi-Console (on page 566)*

#### Client

Assigns the console as a client to a console in primary mode.

A device set to client mode can act as a remote controller or remote video station for a system. A client device cannot output to the lighting system. Only a primary or backup processor can do this.

User ID determines some interaction between the client and other devices. If the client and the primary console have the same User ID, they will act as one. If they have different user IDs, they will have separate command lines. See *User ID (on page 568)*

Consoles in client or backup mode by default will not output on their local DMX ports. This option is found at Setup > System > Outputs. Click on {Output in Client Mode} to enable the ability to output.

> **CAUTION:** *ETC does not recommend the use of wireless networking for show critical functions.*

##### Mirror

Client mode requires a dongle. When a dongle is not detected, the option to connect in mirror mode becomes available instead. See *Mirror Mode (on page 569)*.

#### Offline

Puts the console in Offline mode. Consoles in this mode cannot connect with other devices on the same network. This mode is primarily intended for offline editing of a show file.

##### Offline w/ viz

This mode is available when running ETCnomad software without a dongle. This mode is only intended to be used with visualizer software, and does not output DMX.

#### Settings

Opens the ECU Settings.

#### Augment3d Tether

This mode is available when running ETCnomad software with or without a dongle, allowing you to run Augment3d on a computer connected to a console. See *Running Augment3d (on page 496)*.

#### Power Off

Powers the console down following a confirmation.

> **Se****ttings > General**

#### Device Name

This specifies the name the console will use to identify itself on the network to other devices. Examples might be Booth Desk or Tech Table.

#### 24 Hour Clock

The time is displayed in a 24-hour format as HH:MM:SS. Disabled by default.

#### Time

The time the console is using. Time can be changed from the shell via *Time Service (SNTP) (on page 589)*. Defaults to 12 hour format. To use 24 hour format, make sure 24 Hour Clock is enabled.

> The time can also be changed manually within Eos via the *Quick Access (on page 95)* tools.

#### Date

> The date the console is using. This can be changed manually or via SNTP (Simple Network Time Protocol) time service. See *Time Service (SNTP) (on page 589)*.

The date is displayed as DD / MM / YYYY.

#### Time Zone

The time zone the console is using. This is an offset from Greenwich Mean Time (GMT). Each setting in the pull-down list displays the offset, the name of the time zone and a couple of cities in that time zone.

#### Language

Allows you to select the display language of Eos. Choices include English, Catalan, Bulgarian, German, Spanish, French, Italian, Slovak, Turkish, Japanese, Korean, Russian, Chinese - simplified, and Chinese - traditional.

#### Keyboard

Allows you to select the language for the alphanumeric keyboard within Eos. A wide variety of keyboards are supported.

The keyboard can also be changed in the application when the virtual keyboard is open. Click on the flag icon to see a language drop-down menu.

*(figure omise)*{width="4.99117782152231in" height="1.167707786526684in"}

Press {Sym} to switch the keyboard from alphanumeric to symbols. When in symbol mode, press {Abc} to return to the alphanumeric keyboard.

#### Use Shift key as Eos Shift

Allows the SHIFT key on an alphanumeric keyboard to be used as the console\'s [Shift] key. The Z key on an alphanumeric keyboard will function as the [Shift] key.

#### Open in \"Shell\" E.C.U.

When enabled, the console will boot into the welcome screen every time instead of booting directly into the main application. When disabled, the console will boot into the mode in which it was last used in (i.e. Backup, Client, Primary).

#### Automatically Update Software

> **Note:** *This option is not available on ETCnomad.*

When this is checked, the console will receive software updates from the primary if used in a multi-console system.

#### Allow Automatic Update from Older Eos Version (v2.x)

> **Note:** *This option is not available on Windows 10 devices or ETCnomad.*

When checked, this box allows primary consoles running software v3.0 and later to update backup and client consoles running v2.x software.

#### Fullscreen ETCnomad

> **Note:** *This option is only available on ETCnomad.*

When enabled, ETCnomad will automatically launch fullscreen, on all connected monitors of your computer. Select \"1\" in the \"Windows Per Fullscreen Display\" dropdown to show a single fullscreen ETCnomad display on each monitor, or \"2\" to subdivide each fullscreen display into 2 ETCnomad windows.

*(figure omise)*{width="5.805003280839895in" height="2.8559372265966756in"}

When disabled, ETCnomad will launch in a standard windowed display. The \"ETCnomad Windows\" dropdown allows you to choose to open up to 6 separate windows.

#### Show / Media / Model Archive Path

The default location to save show files, media files, or Augment3d models. The full path must be typed in and specified in a legal Windows format.

If you decide to change this setting, it is recommended that you keep this location on the D: drive. The {Restore Default} buttons will return a changed location to the ETC default.

#### Share Show / Media / Model Archive

Enables you to share the show, media, or Augment3d model archive folders on the console with another console via Windows File Sharing (SMB).

#### Template Show

When a show file is assigned as a template, Eos will create a copy of the file in the Templates folder to be used as the default starting point for any new show files. A new option will appear in the CIA under File > New From Template (*Template Show File Name*) to create a new show file identical to the template. A blank show file can always be created with the File > New option.

Templates can be managed via the File Manager, and are unaffected by deep clears. See

> *Settings > Maintenance (on page 589)*.

#### Latitude

Allows you to select the latitude the console is using.

#### Longitude

Allows you to select the longitude the console is using.

#### {Calibrate Elo External Touch Screen}

> **Note:** *Before you calibrate your external touchscreens, you may need to first use the External Monitor Arrangement display. See {Monitor Arrangement\...} (on the facing page)*

Allows you to calibrate an Elo touchscreen. With the touchscreen connected, press the

{Calibrate Elo External Touchscreen}.

The first display will have you touch some targets, and the second will have you touch various parts of the display to make sure the cursor follows your finger. If that works fine, press the green checkbox. If you need to return to the previous display, press the blue arrow button.

#### {Monitor Arrangement\...}

*(figure omise)*{width="2.6155402449693788in" height="2.8420833333333335in"}

> **Note:** *The selected monitor will display in yellow. External monitors can be dragged to any of the surrounding black boxes to mimic actual monitor layout. Internal monitors are locked in relationship to each other and cannot be changed.*

The monitor arrangement tool will dictate how and where the pointer moves from one monitor to another. Generally speaking, you will want the logical placement on this screen to match your physical placement.

Buttons available in the monitor arrangement display are:

-   {Calibrate} - calibrates the selected touchscreen.

-   {Reset Calibration} - restores default calibration data for selected display.

-   {Identify} - displays the video ports that your monitors are connected to on the physical monitors to confirm where you have placed them.

-   {Enabled} - When checked, the monitor is available for use. The console will display the

> {Enabled} box checked for any monitors it recognizes.

-   {Primary} - selects which monitor will display the Eos Configuration Utility and Central Information Area (CIA). On consoles with internal monitors, the primary is locked to the right touchscreen on the console.

-   {Resolution} - sets how many pixels the monitor will display.

-   {Color Depth} - sets how many colors will be displayed.

-   {Refresh Rate} - sets the number of times in a second the monitor refreshes.

-   {Orientation} - sets the monitor layout.

-   {Apply} - will save and use your settings. A window will open asking if you want to {Keep Changes} or {Revert} back to the defaults. {Revert} will be selected after 15 seconds if nothing else has been selected first.

-   {Close} - will close the display. {Close} will not save any settings if {Apply} has not been used.

-   {Configure Touchscreens} - is used to map the touchscreens to the displays.

-   {Elo Monitor Settings} - opens the properties window for the monitor. See *{Calibrate Elo External Touch Screen} (on the previous page)*.

-   {ETC Monitor Settings} - opens the properties window for the monitor.

> **Note:** *Only supported options will display. Monitor options may vary. While it is possible to assign a resolution lower than the minimum (1920x1080), it is recommended to be at 1920x1080 or higher.*
>
> **Note:** *Built-in monitor settings are read-only.*

#### {Software Update\...}

Allows the installation of Eos Family software and other ETC-approved software (Concert, UpdaterAtor, GCE, and NCE). Updating Eos Family software does not affect or update the software in any other networked device such as a Net3 Gateway.

When you click on {Software Update\...}, the console looks at the root directory of any connected USB storage device for an Eos Family console software update file. You will be shown the names of any updater files found on the drive. Select the file you would like to install and click the {Install} button, or click {Cancel}. The software will first save to the hard drive before opening the installer.

You will also receive a message if no software update file can be found.

*(figure omise)*{width="1.5816316710411198in" height="1.2508333333333332in"}

##### Installer Archive

Shows the available Eos software version installers currently saved on the console\'s local hard drive. You can save multiple software versions onto your console\'s hard drive in case you wish to downgrade.

While installing the software, you can archive the installer used. Check the Archive Installer box for the selected version, and it will archive while installing the software. If you would like to archive installers without installing their software, you can do that by using the File Manager utility in ECU > Settings > Maintenance.

You can also retrieve these versions from the archive to save them to a USB drive by using the File Manager.

> **Note:** *On new consoles, some versions are preselected to be archived when initially shipped from ETC. This includes the version of software that is currently installed from the factory as well as any patches to that version (if available). For future releases, you will need to download the Eos Family software from the ETC website, [etcconnect.com](http://www.etcconnect.com/).*

##### Fixture Library Updates and Help Packs

{Software Update\...} also recognizes zipped fixture library files provided by ETC.

1.  Select the desired ZIP file from the Software Update window.

2.  You will be asked to confirm that you want to install the selected file. Click {Yes} to continue or click {No} or {Cancel} to return to the Software Update window.

3.  A window will open showing the progress of extracting the ZIP file. The installer will then launch after the file has been extracted.

#### {Switch to Eos 2.9.x}

> **Note:** *This option is not available on Windows 10 devices.*

Eos v3.0.0 introduced the ability to switch between v2.9.x and v3.0.0 and later on consoles capable of running both. If v2.9.x is already installed, installing v3.0.0 or later automatically retains the 2.9.x version of software.

*(figure omise)*{width="4.172516404199475in" height="2.2562489063867015in"}

Use the softkey to alternate between versions. A restart will be required before any changes can take effect.

> **Note:** *If a console is updated to v3.0.0 or later from a version prior to v2.9.X, you will be able to revert from v3.0.0 or later to the prior version. However, you will be unable to return to v3.0.0 or later without first updating to v2.9.X.*

#### Version Information

Key information about installed software and other components. {Extended Version Info\...} will open a window with additional details.

> **Settings > Network**

The Network page of ECU Settings provides options for various categories of network configuration settings.

> **Note:** *Some settings can also be accessed from within the Eos application via Setup*

-   *Device >Network (on page 224).*

#### Device

*(figure omise)*{width="4.152233158355205in" height="1.4012489063867017in"}

These are the settings that determine the method to get an IP address and / or the actual IP address information that Eos uses for network communication.

On ETCnomad, these settings are determined by Windows or macOS, and cannot be edited here.

> **Note:** *Consoles with more than one network interface card (NIC) should avoid connecting more than one port to the same network or subnet.*

##### Status

A port is \"online\" in green if it is configured, connected to a network and operational. If any of those conditions is not true, it reports as "offline\" in red.

##### Obtain IP Automatically

> **Note:** *ETC recommends the use of a static IP address for compatibility with other ETC devices, though the needs of your particular installation may vary.*

When enabled, this allows the console to request an IP address from a DHCP server during startup. If one responds, it will use the assigned IP address.

If no DHCP server is available, the console will default to a self-generated link-local IP address in the range of 169.254.X.X. The IP address used by the console in this configuration may change dynamically as needed. A change should typically only occur when there are changes to the network configuration or to resolve an IP address conflict.

Enabling or disabling this setting will require you to reboot the console for the new setting to take affect.

> **Note:** *You cannot set the console to receive an IP address via DHCP and act as a DHCP server at the same time. It can either send dynamic addresses or receive them, but not both at the same time.*

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

##### Physical Address

The physical address is the MAC address, a unique device identifier that cannot be modified.

##### Network Interface Delay (Required)

> **Note:** *This option is not available on ETCnomad.*

When {Required} is enabled, the console will wait for the network connection to be fully initialized before launching the Eos application.

When enabled, a launching window will display on start-up. If a network connection is not made, you will have the option to {Start Anyway}, {Start Offline}, or to {Cancel}.

-   {Start Anyway} - launches without a network interface. Only User 1 is displayed above the CIA.

-   {Start Offline} - starts in offline mode.

-   {Cancel} - remains in start-up without launching into the Eos application.

##### {Reset to Defaults}

> **CAUTION:** *This button will restore all network settings on the selected port to their ETC defaults. This includes factory-default IP addresses and settings.*

##### Remote Startup / Shutdown

It is possible to remotely power on and off some Eos devices, such as RVIs, RPUs, and client consoles. Windows or macOS with ETCnomad cannot be remotely powered on and off.

{Remote Startup} and {Remote Shutdown} must be enabled on each device before it can receive the power on and off commands. The default setting for both is Disabled.

The Remote Power commands are sent from the browser. The command for Power On is sent from Browser > Network > Power On MultiConsole System, and the command for Power Off is from Browser > Network > Power Off MultiConsole System.

> **Note:** *Only devices that synchronize with the primary will be available for Remote Power On and Off.*

##### {Ping}

Ping is used to test the network connection between two devices.

> *(figure omise)*{width="5.026666666666666in" height="2.042082239720035in"}

1.  Click the empty box on the left, and enter the IP address of the device you want to ping.

2.  Press Start. You will either see replies from the device, or \"response timed out,\" indicating the device is not responding to the ping.

#### Allowed Outputs

A range or ranges of addresses that can be assigned to limit the number of output addresses. The default setting is to allow addresses 1 through 32767488.

#### Interface Protocols

> **Note:** *Some settings can also be accessed from within the Eos application via Setup*

-   *Device >Network (on page 224).*

##### MultiConsole

> Enables multi-console communication on the selected port. Enabled by default. See [*Multi-**Console Setup (on page 566)*](#multi-console-setup).

###### Network Type

This setting adjusts the timeout period before a backup device will take control from the primary.

-   Standard- After five seconds of no response from the master, the backup will assume the primary has disconnected and will then take control.

-   Engineered - After 1.6 seconds of no response from the primary, the backup will assume the primary has disconnected and will then take control.

###### File Transfer

This setting adjusts the show file transfer speed between devices. The default setting is Fast File Transfer.

> **Note:** *If you are experiencing connection issues between devices, you can change the setting to Normal File Transfer for a slower transfer speed.*

##### Sensor/FDX3000 Feedback

> Allows your console to receive feedback over the network from CEM+, CEM3, or FDX3000. Enabled by default. See *[About] Address (on page 448)*.

##### Network RDM

Enables RDM functionality on all Ethernet ports, including device discovery. Enabled by default.

> **Note:** *RDM requires use of a Net3 or Response Gateway. Net3 Gateways must be using version 5.1 or higher.*

#### DHCP Service

> **CAUTION:** *Enabling or disabling DHCP services requires rebooting your console.*
>
> **Note:** *If this section is grayed out and you are unable to change any settings, you may need to install Net3 Services on your console. Net3 Services are installed with ETC\'s Gateway Configuration Editor (GCE) software, available for download from [etcconnect.com](https://etcconnect.com/).*

##### Enable

Enables the Eos Dynamic Host Configuration Protocol (DHCP) address server. DHCP is a TCP/IP protocol that dynamically assigns an IP address to a network device when it requests one.

The Eos DHCP server is intended to be used on non-routed networks. It will not serve IP addresses across a router.

> **CAUTION:** *While there should only be a single DHCP server active on a network, it is still possible to start more than one DHCP server at a time. This can lead to unstable conditions and network communications issues.*

The Eos DHCP server then uses the following settings to determine which IP addresses it gives out.

###### First IP Address

This sets the starting IP address of the range of IP addresses the DHCP server will give out.

###### Number of Addresses

This sets how many IP addresses the DHCP server will give out. A setting of 500 means it will give out IP addresses to the first 500 devices that ask for an IP address.

###### Subnet Mask

This sets the logical network size vs. the device address. ETC's default is 255.255.000.000 (class B). This is the subnet mask that the DHCP server will give to network devices.

###### Routed

If checked, you can use the default gateway box, below, to specify the gateway you would like DHCP devices to use. If unchecked, the DHCP server will serve the same value for both the devices IP address and gateway, which is a suitable configuration for non-routed networks.

###### Default Gateway

This specifies the IP address of a router if one is present on your network. This is the gateway IP address that the DHCP server will send to network devices to use. If you are on a flat or non-routed network, the Gateway IP address should match the IP address of the device. In order to

configure this DHCP server to send out matching gateway IP addresses, configure this gateway IP address to match the IP Address field. Then the DHCP server will give out a gateway IP address that matches the IP address.

##### Learn Network Devices

Clicking this button will trigger the DHCP service to search the network for existing devices, and add them to its table of known addresses. If you have equipment with statically assigned IP addresses in your network, this will ensure the DHCP service does not serve out any IP addresses which conflict with those devices.

#### Time Service (SNTP)

> **Note:** *Some settings can also be accessed from within the Eos application via Setup*

-   *Device >Network (on page 224).*

Enables the SNTP (Simple Network Time Protocol) service. Disabled by default. The following additional settings are available:

-   Mode - when configured as a Client, a console will attempt to synchronize its time with the rest of the devices in the system, by listening for time information and altering its own clock. When configured as a Server, a console will serve out time to other devices on the network.

-   ETC Net2 Time - with ETC Net2 Time enabled, the time server will periodically broadcast (as a server) or receive (as a client) the current time, which is required by devices running the ETCNet2 protocol, for example, Legacy Unison systems.

-   External Time Server - the External Time Server option allows you to synchronize your console to a third party time system at a specific IP address using the NTP or SNTP protocols. This allows use of a specific time clock for time sync. This requires a high accuracy time clock on your network.

-   External Server IP - if External Time Server is enabled, you will need to specify the IP address of your external NTP or SNTP time server in this field.

#### Legacy Settings

The settings in this section are only used when loading show files saved prior to Eos v3.2.0.

##### Output Protocols

> See *Patch > Protocols (on page 186)*.
>
> **Settings > Maintenance**

#### {Deep Clear\...}

Clears unsaved console data and temporary files. A deep clear is automatically performed when new software is installed. Sometimes it is useful to perform a deep clear between updates.

The advantage of deep clear is that you can clear all console data before reloading the console's current state during start-up. This is helpful if you are moving a new console onto the network and don't want it to suddenly take control of a system or if you somehow end up with a corrupt show file that is causing issues upon start-up.

> **Note:** *Deep clear does not reset any ECU settings.*

#### {Reclaim Disk Space\...}

Removes extraneous files such as temp files, logs, and diagnostics to free up disk space.

#### {Save Logs\...}

Displays a dialog box prompting you to save the console log files for troubleshooting purposes.

By clicking on the {Advanced} button, you can select or deselect any of the various individual log files to be saved.

Clicking {Next} you will be able to provide additional information, the date, and time of the issue.

Clicking {Next} again you will see a drop down menu to select the target export location from any available write-enabled removable media such as a USB drive.

> If you experience software problems with your system that we are unable to reproduce, sending these log files to ETC Technical Services (see *Help from ETC Technical Services (on page 3)*) can help us isolate the issue.

#### {Backup Show Archive\...}

Allows you to either backup the most current version of each show file or every version of each file to a USB drive.

#### {Restore Show Archive\...}

Allows you to restore show files from a USB drive.

#### {Backup System Settings\...}

Allows you to backup all ECU settings, including Net3 services. {Backup System Settings\...} will open a window that allows you to save an .ini file to a selected drive. To backup settings, select a drive from the drop down menu, and press {Accept} to save or {Cancel} to exit without saving.

#### {Restore System Settings\...}

Open a window that allows you to select a saved.ini file. Select the desired file and press {Ok} to restore settings. Press {Cancel} to close the window without restore settings.

#### {Face Panel Test\...}

Provides a way to verify the functional state of all of the keys, encoders, and faders on the console. Press/ move every key, encoder, and fader to verify that those events register on the diagnostic test screen.

#### {Classic Peripheral Test\...}

Allows you to test peripherals such as fader wings.

#### {File Manager\...}

Provides a way to manage show files, show data, and software installers. You can create and delete new folders, move, and copy files between the console and USB drives.

> *(figure omise)*{width="5.7254833770778655in" height="2.331457786526684in"}

The file manager display will show the ShowArchive folder on your console as well as any external USB drives that are detected. The display is split into two windows, so you can see two different folders at the same time for copying or moving data between them.

#### {Gateway Configuration Editor (GCE)\...}

> **Note:** *This option is not available on Windows 10 devices.*

Launches the GCE software. This softkey will only display if the software is installed on your console.

#### {Concert\...}

Launches the Concert software. This softkey will only display if the software is installed on your console.

#### {UpdaterAtor\...}

Launches the UpdaterAtor software. This softkey will only display if the software is installed on your console.

#### {Touch Screen Test\...}

Opens an application for testing your touchscreens.

#### {Upgrade Console\...}

This softkey is used for upgrading the console\'s outputs.

#### {Upgrade I/O Firmware\...}

*(figure omise)*{width="3.8322528433945755in" height="0.7474989063867017in"}

Upgrades the firmware for single-port Gadgets and consoles with I/O cards that have a phone remote connection. All other devices can use the Firmware Update window below.

When you first open the I/O Downloader, it will look for the connected console. This may take several seconds. Once the console is found, the downloader will search for the needed files. If it finds the file, it will list it and you can click {Download}. If it doesn\'t find the file, you can use

{Browse} to look for the needed file and selected it. Once finished, click {Exit}.

#### {Network Drives\...}

Allows you to select an alternative show file storage location on another console or computer. After setting this location, it will appear as an option within the save and open dialogs in Eos.

*(figure omise)*{width="4.582093175853019in" height="1.5754166666666667in"}

In the {Network Drives\...} dialog box, there is a {Add} button for mapping a network drive. In the Add Network Drive dialog box, select the drive letter that is appropriate, the network path, and the path type. The network path can use either the IP Address or the Device Name. (Example: \\10.101.90.101\ShowArchive or \\YourDeviceName\ShowArchive) The network path type should match the device. If Other is selected, you will have additional fields to fill out for Username and Password.

#### {Shared Folders\...}

Allows you to see if any folders are currently being shared by the console. You can select the folder and click {Don't Share} if you no longer want to share the folder. By selecting {Don't Share} here, you will also uncheck the box for sharing the show file archive on the General page of ECU Settings. See *Share Show / Media / Model Archive (on page 580)*

#### Firmware Update

The firmware update window will display any detected devices that use firmware and may require an update. Devices that need to be updated will display in red.

*(figure omise)*{width="1.8964282589676291in" height="0.95875in"}

When a device is selected, the {Update} button will display in yellow if the device can be updated using this window. This includes devices that do not currently need to be updated. If the button is grayed out, the device can not be updated using this window.

> **Note:** *Windows 7 consoles must be power-cycled after a firmware update. This is not necessary for consoles running Windows 10.*

### Buttons

#### RPU Face Panel Buttons

This area is for configuring the buttons on the front of a RPU or RVI. Clicking on a button will open a dialog window for selecting what type of button, macro, hardkey, or none, you wish to assign.

If hardkey is selected, a list of the various hardkeys on your console will be available to select from. If macro is selected, a macro number can be entered. Selecting none will assign no action to the selected button.

{Import} allows you to import a RPU/RVI button configuration file. {Export} allows you to export a RPU or RVI button configuration file. {Restore Defaults} will restore the factory defaults for the RPU or RVI buttons.

#### Face Panel Buttons

This area is for configuring the customizable hardkeys on the Eos Ti, Gio, and Gio @ 5 face panels.

Clicking on a button will open a dialog window for selecting what type of button, macro, hardkey, or none, you wish to assign.

If hardkey is selected, a list of the various hardkeys on your console will be available to select from. If macro is selected, a macro number can be entered. Selecting none will assign no action to the selected button.

{Import} allows you to import a button configuration file. {Export} allows you to export a button configuration file. {Restore Defaults} will restore the factory defaults for the buttons

### RFR

This screen is used for setting up the Net3 Radio Focus Remote (RFR) to work with Eos.

> **Note:** *These settings need to match between the console and the RFR.*

#### High Frequency Channel

The frequency that the RFR is using. There are 1-12 channels.

#### Network ID

The Network ID is a separate digital channel on a single high frequency (HF) setting. There are 1-99 IDs available.

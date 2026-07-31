# Eos Family User Manual v3.2.0 — Chapitre 04 : Patch

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 4
## Patch
  -------------------------------------------------------------------------------------------------
  --------------------------------------- ---------------------------------------------------------
  -------------------------------------------------------------------------------------------------
### About Patch

Eos treats fixtures and channels as one and the same, meaning each fixture is assigned a single control channel number. Individual parameters of that fixture, such as intensity, focus, color, and beam are also associated with that same channel number but as additional lines of channel information.

The Patch is used to associate a channel with addresses and device types. Once a channel is patched to an address or addresses, and the output is connected to a device (for example a dimmer, automated fixture, or accessory), the channel will then control that device.

Patching can be done via two different methods: manually entering a patch and by patching devices using RDM via the Device List. RDM allows bi-directional communication between the console and any RDM devices over RDM or Ethernet. See *Patch > Device List (on page 188)*.

For manual patching, you are required to only enter the simplest data to patch a device and begin programming your show, such as the channel number, the device type (if needed), and address. When you provide more information in the patch, you will have more detailed control and improved function during operation.

One or more devices may be patched to a single channel. For example, you may want to patch a group of dimmers to the same channel. In addition you may patch multiple devices to the same channel for building compound or accessorized fixtures. For example, a Source Four® with a color scroller and a gobo changer may be patched to a single channel. This is referred to as a compound channel. See *Creating Multipart and Compound Channels (on page 171)*.

Depending on your situation, you may need to create a custom patch, which associates certain addresses with certain channels.

> **Note:** *You can open or merge patch data from other show files, see Partial Patch Opening (on page 151) and Partial Patch Merging (on page 152).*
>
> A 1-to-1 patch can be created from the Clear display. See *Clearing the Patch (on page 193)*

#### Element 2 and Element Classic Patching

Element 2 and Element Classic can create a 1-to-1 patch when you open a new show file. This means that the patch will automatically have channel 1 patched to address 1, channel 2 to address 2, and so on up to the maximum channel count of your console. When outlined in yellow, the {Patch 1 to 1} button is selected, and a 1-to-1 patch will be created.

### Patch Main Display

To begin patching your show, you must first open the patch display. To open the patch display, use [Tab] [1] [2], press [Displays] and then {Patch}, or press [Address/Patch] twice. Ion Classic users can also press {Address} twice. Element Classic users can use [Patch].

The patch display will open in the selected tab, and the CIA will display patch controls.

From within the patch display, you can open the Device List to use RDM to patch any RDM compatible devices. For more information about Device List, see *Patch > Device List (on page 188)*.

> For patching fixtures, there are two different patch modes: *Patching By Channel (on page 166)* and *Patching By Address (on page 166)*. Eos defaults to patch by channel mode. Pressing [Format] while in the Patch display will toggle the mode between patch by channel and patch by address.
>
> ![](media/media/image169.png){width="4.563597987751531in" height="1.4764577865266841in"}

The patch screen will display the following information if available:

-   Channel - the patched channel number. In patch by address mode, channel will appear blank if not currently patched.

-   Address - the patched output address. In patch by channel mode, address will appear blank if not currently patched. Pressing [Data] toggles the display from showing address as patched by the user, output address, and the port/offset. See *Using Output Address vs Port / Offset (on page 167)*.

-   Type - device, dimmer, or scenic element type that is patched. An asterisk (*) next to the type indicates that the fixture profile needs to be updated. See *Update Profile (on*

> *page 193)*.

-   Label - displays the assigned label of the channel or address. See *Labeling (on page 175)*.

-   Interface - displays which interfaces will be used for the device. See {Interface} in *Patch*

    -   *Patch (on page 181)*.

-   Output - displays the current live intensity level. Value is displayed as 0 through 255, with 255 being full. 16 bit intensity values will display as 0 through 65535.

#### Status in the Patch Display

Status flags will display on the far left of the patch display to advise you when a channel or address requires your attention.

> A red "!" or yellow "?" will display when there is an error or warning from an RDM, CEM+, CEM3, or ACN device. See *Errors and Warnings (on page 192)*.

#### Flexichannel Views in Patch

In patch by channel mode, [Flexi] can be used to view only those channels that are currently patched. In patch by address mode, [Flexi] can be used to view only those addresses that are currently patched. By pressing [Flexi], you can toggle the view between patched channels/addresses, selected channels, and all channels/addresses.

Holding down [Flexi] will display the following softkeys:

-   {Flexi All} - displays all the channels or addresses depending on which view is used.

-   {Patch} - displays only the patched channels or addresses.

-   {Selected} - displays any selected channels or addresses.

-   {View Channels} - displays those channels selected for the View Channels flexichannel state.

-   {Partitioned} - only available when partitioning is enabled. Displays the following options:

-   Partitioned Channels

-   Partitioned Patched Channels

-   Partitioned Selected Channels

-   Partitioned View Channels

> **Note:** *Scenic Element and Scenic Element Movable channels use no addresses when patched, and will appear in the Flexi Patched display. For more information, see Scenic* *Elements (on page 537).*

### Patching Conventional Fixtures

> For patching fixtures, there are two different patch modes: *Patching By Channel (below)* and *Patching By Address (below)*. Eos defaults to patch by channel mode. Pressing [Format] while in the patch display will toggle the mode between patch by channel and patch by address.
>
> **Note:** *When working with conventional devices, you can patch in either mode easily. When working with compound channels or multiple parameter devices, such as automated fixtures, it is recommended to work in patch by channel.*

#### Patching By Channel

In patch by channel mode, [2] [0] [At] [1] [Enter] patches channel 20 to address 1. Pressing [At] will post address to the command line while patching by channel.

![](media/media/image170.png){width="1.6041666666666667in" height="1.3854166666666667in"}

Additional examples of patch by channel:

-   [5] [At] [1][0][0] [Enter] - patches channel 5 to address 100.

-   [2][0][3] [At] [1][2] [Enter] - patches channel 203 to address 12.

#### Range Patching

Range patching using the [Thru] key allows you to quickly patch a group of channels. [1][Thru] [2][0] [At] [1] [0] [Enter] patches channels 1 through 20 to addresses 10 through 29.

You can also use the [+] and [-] keys. [1] [+] [4] [+] [8] [At] [1] [Enter] patches channel 1 to address 1, channel 4 to 2, and channel 8 to 3. The [Group] key can also be used if groups have been created.

> **Note:** *Range patching only works with channels. If you try to range patch addresses, parts for the channel will be created. See Creating Multipart and Compound Channels (on page 171).*
>
> **Note:** *If you try to patch a channel or address that exceeds the console\'s output, an error message will display on the command line.*

#### Patching By Address

Pressing [Format] while in the patch display will toggle the mode between patch by channel and patch by address.

> ![](media/media/image171.png){width="1.587280183727034in" height="1.3708333333333333in"}

[2] [0] [At] [1] [Enter] patches address 20 to channel 1. Pressing [At] will post channel to the command line while patching by address.

Additional examples of patch by address:

-   [5] [At] [1][0][0] [Enter] - patches address 5 to channel 100.

-   [2][0][3] [At] [1][2] [Enter] - patches address 203 to channel 12.

> **Note:** *If, at any point, you try to patch an address that is already in use, Eos will post an advisory to indicate this, preventing you from duplicating addresses in your patch.*

#### Using Output Address vs Port / Offset

The output address is the DMX or network DMX (often called EDMX) address. Examples of output addresses are 510, 1, and 1024.

Port / offset refers to the DMX universe or port and the offset of the address. For example, since a single DMX port can transmit 512 addresses (known as a "universe"), the port / offset for address 515 would look like 2/3 because address 515 is the 3rd address of universe 2.

An example of patching by port / offset in patch by address mode is [2][/][1][0] [At] [2][0] [Enter], which patches universe 2 address 10, or 522, to channel 20.

[At] [/] [n] [Enter] can be used to patch an address on the same universe that was last used.

> **Note:** *It is possible to patch by either address or port/ offset. Pressing the [Data] key will move between showing the patch as it was originally entered, then the output address values, and last the port/ offset.*
>
> **Note:** *An address cannot be assigned to multiple channels, but a channel can have multiple addresses assigned to it.*

#### Replace

By default, if you patch an address to a channel that is already patched, Eos will create a new part for the new address. If you want to replace the current address with the new, use

{Replace}:

-   [n] {Replace} [n] [Enter] - replaces the address in part 1 of the selected channel.

-   [1] [Part] [3] {Replace} [5] [Enter] - replaces the address of part 3 with a new address of 5.

#### At Next

[At] [Next] [Enter] finds the next available address range large enough to accommodate the selected device.

Examples of [At] [Next]:

-   [At] [2] [/] [Next] [Enter] - finds the next available address range on universe 2.

-   [At] [7] [7] [7] [Next] [Enter] - finds the next available address after 777.

#### Select Full Universe

> **Note:** *[Address/Patch] is used in the examples below. Ion Classic users will need to use {Address}, and Element Classic users [Dimmer/Address].*

The syntax [Address/Patch] [n] [/] or [At] [n] [/] can be used to select a full universe in patch.

-   [channel list] [Address/Patch] [n] [/] [Enter]or [channel list] [At] [n] [/] [Enter] - changes the addresses of all the selected channels to a new universe while using the same offset.

-   [Address/Patch] [2] [/] [Copy To] [Copy To] <Address> [3] [/] [Enter] - moves all channels with addresses in universe 2 to the same offsets in universe 3.

-   [Address/Patch] [n] [/] {Unpatch} - unpatches all patched addresses in the selected universe.

#### Dimmer Doubling

You can patch channels in Eos to accommodate for dimmer doubling with Sensor dimmer racks. This is done using the softkeys available in patch ({No Dim Dbl}, {A}, and {B}).

> Let's assume you patch 96 channels of dimmers to addresses 1 through 96.

-   [1] [Thru] [9] [6] [At] [1] [Enter]

> Now you wish to dimmer double 1 through 12 of your Sensor+ rack and you want these to be channels 97 through 108. To patch this, press:

-   [9] [7] [Thru] [1] [0] [8] [At] [1] {B} [Enter]

> Channels 97 through 108 are patched to address 1 through 12 B, while
>
> channels 1 through 12 are now patched to address 1 through 12 A.
>
> To remove the dimmer doubling from these addresses, you must first press [Format] to enter Address mode and then press:

-   [1] [Thru] [1] [2] {NoDimDbl} [Enter]

> Addresses 1 through 12 have been returned to single dimmer modes and channels 97 through 108 are now unpatched.

By default, doubled dimmers start with an offset network DMX address value of 20000. Therefore, in the above example, address 1B (channel 97) is actually controlled by network DMX address 20001. Address 2B is actually controlled by network DMX address 20002 and so on. This offset matches the default offset in CEM+ / CEM3 when configuring your Sensor dimmer rack for dimmer doubling. To change the default offset value, see *Dim. Dbl. Offset (on page 212)*.

> **Note:** *For Sensor Classic racks using dimmer doubling, the offset value should be set to 256.*
>
> **Note:** *Dimmer doubling needs to be turned on per DMX port in Browser > Setup > System Settings > Output. See Local Output (on page 228).*
>
> **Note:** *There is also a Dimmer Doubling setting for Net3 Gateways with DMX outputs. This is used with Sensor racks that are connected via DMX. The Gateway must be properly configured.*

#### Moving and Copying Channels

Channels can be moved from one location to another within patch.

-   [1] [Copy To] [Copy To] [2] - moves channel 1\'s data to channel 2. Channel 2\'s data is replaced by channel 1\'s. Channel 1 is unpatched.

-   [1][Copy To] [Copy To] [2][Part][2] - creates a part 2 for channel 2 and moves channel 1\'s data to the new part. Channel 2\'s data remains in part 1. Channel 1 is unpatched.

The second press of the [Copy To] key changes the command from Copy To into Move To.

> **Note:** *Move To always impacts the entire show.*

The following options are available with [Copy To]:

-   [Copy To] - copies a channel to another location within patch.

-   [Copy To] {Plus Show} - copies a channel to another location within patch and all record targets in the show.

-   [Copy To] {Only Show} - copies a channel to another location with all record targets in the show but not the patch data.

-   [Copy To] {Only Text} - copies only the notes and keyword fields from one channel to another.

#### Swapping Channels

Channels can be swapped for each other in patch:

-   [1] {Swap} [2] [Enter]

This syntax will replace channel 1\'s data with channel 2\'s and vice versa in patch and throughout the entire show.

> **Note:** *Swap always impacts the entire show.*

The following options are available with {Swap}:

-   {Swap} - swaps only the patched address

-   {Swap} {Plus Show} - swaps all show and patch data

-   {Swap} {Only Show} - swaps only the show data and not patch data

-   {Swap} {Plus Patch} - swaps addresses and patch data but not show data

#### Unpatch a Channel

To unpatch a channel while in patch you can press:

-   [n] {Unpatch} [Enter]

The {Unpatch} softkey will reset all the properties of the channel to the default. This includes removing the device type if specified.

To retain all the elements of a channel except its address, you would instead use:

-   [n] [At] [0] [Enter]

Using [At] [0] will allow unpatched channels to still be manipulated and have data stored for them, but they do not output any information (as they are unpatched).

#### Deleting Channels

It is possible to delete channels in patch. Deleting channels is different from unpatching in that deleted channels cannot be manipulated or have data stored for them. When deleted, the channel numbers will still be visible in the live/blind display, but the channel graphic will be removed from the display.

To delete channels in the patch display, press:

-   [6] [Thru] [1] [0] [Delete] [Enter] [Enter]

> -or-

-   [Delete] [1] [Thru] [1] [0] [Enter] [Enter]

> **CAUTION:** *If a channel with programmed data is deleted, the recorded data will be lost.*

##### [Query] {Unpatched}

To quickly delete channels without addresses in the Patch display, you can use the command [Query] {Unpatched} [Delete]. This will post to the command line all channels without addresses. By pressing [Enter][Enter] you will delete them.

On Element Classic, {Query} is a softkey.

#### Using Offset in Patch

Using the offset feature in patch allows you to force a numerical offset between the starting address of channels in patch or for offsetting your channel selection. This feature is useful when you have configurable devices in your show, such as a Source Four Revolution, which has option slots for additional addresses (scrollers, indexing pattern wheels, and so on), or when your devices\' start addresses use a known multiplier.

> When patching using a fixture type, this is a two step process because the command line terminates after a fixture type has been selected.

1.  [1] [Thru] [5] {Type} {Source Four Revolution}

2.  [At] [1] [Offset] [3] [1] [Enter]

> Hitting [At] will reselect the previously selected channels. The channels can then be patched with an address offset of 31 channels, allowing you to have additional space within the patch for a given fixture type regardless of configuration or personality.
>
> **Note:** *On non-Apex Eos Family consoles, {Offset} is a softkey.*
>
> **Note:** *For multiple parameter devices, Eos will automatically offset the addresses based on the fixture type.*
>
> For more information about using offset, see *Offset (on page 242)*.

#### Creating Multipart and Compound Channels

A multipart channel is any channel that has more than one dimmer patched to it. A compound channel has multiple profiles patched to it that make up one channel, an example would be a dimmer with a scroller and auto-yoke. By default, Eos will add a part if you are trying to patch to a channel that has already been assigned an address.

To patch a multipart channel in channel format:

-   [9] [At] [5] [4] [0] [Enter]

Assuming that channel 9 is already patched to an address, this will create a part 2 and address it at 540.

-   [8] [Part] [2] [At] [5] [1] [3] [Enter]

This will create a part 2 for channel 8 and address it at 513. If you wish to patch by address while in the channel view, press:

-   [Address] [5] [1] [3] [At] [8] [Enter]

Assuming channel 8 was previously patched to an address, this will create a part 2 and address it at 513.

To patch a multipart channel in address format:

-   [5] [1] [3] [At] [8] [Enter]

This will perform the same action as the previous example, assuming channel 8 was previously patched to an address.

To select multiple parts for editing:

-   [1] [Part] [1] [Thru] [5]

This is useful for deleting or assigning new addresses to existing parts. To patch a compound channel in channel format:

-   [1] [Part] [2] [At] [5] {Type} <scroller profile>

> Creates a part 2 for channel 1 and assigns it the selected scroller profile. See *Patch > Patch (on page 181)* on using {Type}.

Use multiple parts without addresses to assign multiple fixtures in Augment3d positions that share the same channel.

### Patching Automated Fixtures, LEDs, and Accessories

The process of patching automated fixtures requires more detail than patching a dimmer. Specific information is required for more advanced control of the features offered by automated fixtures.

> **Note:** *It is recommended that when patching automated fixtures, LEDs, and accessories that you work in patch by channel mode. See Patching By Channel (on page 166).*

After you have entered the channel number, click {Type}. You will then select a device type from the fixture library.

> ![](media/media/image172.png){width="5.060937226596676in" height="1.349582239720035in"}

Notice the softkeys {Show}, {Manfctr}, and {Search} located beneath the CIA.

{Show} provides you with the option of showing only the library of fixtures or devices that are already patched in the show, your favorites, and default devices. {Manfctr} shows all fixtures or devices available in the library sorted by manufacturer.

Press {Manfctr} from the CIA to display the fixture library. The two columns on the left are pageable and show manufacturer names. Use the arrow buttons to scroll the list of manufacturers. Selecting a manufacturer repaints the device columns with all devices from that manufacturer that are available for patching.

Scroll through the device list and make your selection. If a fixture has multiple modes or types, it will display in blue text. Clicking on its name will open a list of available modes. After the selection is made, the fixture or device type will be placed on the command line after the channel number and displayed in the box beneath the {Type} button.

Press {Search} to open the search window. You will need an external alphanumeric keyboard or you can click the keyboard icon in the search window to open the virtual keyboard. You can also navigate the list as you would the browser. You can search by manufacturer name, fixture name, part of a name, and by DMX footprint. For example, if you searched for 31, you would see all of the fixtures that have a DMX footprint of 31. Double clicking on a fixture name will patch it.

![](media/media/image173.png){width="4.978321303587052in" height="1.4831244531933507in"}

In the search window, press {Parameters} to view a parameter list for a fixture, or press

{Fixture Notes} to see any notes that exist for it. You can also view this information in the Fixture Editor.

Press [At] and then enter a starting address for the selected channel or group of channels. The console will automatically offset addresses based on the fixture type selected.

Fixtures can be added to your show list without first patching them. With nothing on the command line, click {Type}. You can then select a device type from the fixture library, and click

{Add Show} to add to your show list. If you want to delete a fixture or device from the show list, click {Edit} while in the show display. Select the device you wish to remove and click

{Delete}.

> To select a device interface (optional), click {Interface}. See *Patch > Protocols (on page 186)*.

Click the {Attributes} softkey to set detailed automated fixture attributes. The following buttons may be available on this page depending on the device selected: {Preheat},

{Proportion}, {Curve}, {Fan Curve}, {LD Flags}, {GM Exempt}, {Invert Pan}, {Invert Tilt}, {Swap P/T}, {Color Path}, {Scrollers}, {Gobo Wheels}, {Color Wheels}, and {Effect Wheels}.

> Additional buttons maybe available based off of your fixture type. See *Patch > Attributes (on page 182)*.

If your automated fixture includes parameters such as a color scroller or gobo wheel and you have custom gels or non-standard patterns installed, use the Scroller/ Wheel Picker and Editor to modify the device patched. The more specific your patch data (including accurate colors and patterns), the more detailed programming and operating will be. See *Using the Scroller/Wheel* *Picker and Editor (on page 175)*.

### Patching Multicell Fixtures

Fixtures that have multiple same-type parameters can have a multicell profile assigned to them. The process for patching multicell fixtures is similar to patching automated fixtures. There are a few differences that are important to understand though.

> **Note:** *It is recommended that when patching multicell fixtures that you work in patch by channel mode. See Patching By Channel (on page 166).*

After you have entered the channel number, click {Type}. You will then select a device type from the fixture library.

Fixtures that have multicell functionality will be listed with a MC in their mode description in the device list, and in the {Show} list.

> **Note:** *When using {Search}, the number of cells for a multicell fixture will also be displayed.*

When these devices are patched, they will patch a master channel with a whole number for a channel number and the appropriate number of additional cells, which will have point numbers for their channel numbers.

-   [1][0] [At] [5] [Enter] - patches channel 10 and all of its cells starting at address 5.

-   [1][0] [.] [1][2] [Thru] [1] [At] [5] [Enter] - patches channel 10\'s cells 12 through 1 starting with cell 12\'s address beginning with address 5.

> **Note:** *If the master channel has only a virtual intensity over the cells, an address will not be displayed, as that is a virtual parameter.*
>
> In the *Fixture Editor*, you can view and edit the personality for your multicell fixture. For creating a new multicell fixture, see *Creating Multicell Fixtures (on page 207)*.

On the left of the fixture editor, you can see the fixture name, overall DMX footprint and number of cells. Click on the caret to see the DMX footprint for the master and the cells. The cells will be grouped with their profile(s).

> ![](media/media/image174.png){width="5.050928477690289in" height="2.8306244531933507in"}

On the right, you can see the full personality of the selected multicell fixture. If you have the whole fixture selected, you will be able to see all of the parameters for each cell and the master but changes cannot be made here.

> See *Editing Multicell Fixtures (below)*.

#### Editing Multicell Fixtures

> You will need to select the master or cell profile to edit parameters. In this view, you\'ll be able to edit parameters, DMX, Home, Snap, and ranges/modes. See *Creating a New Fixture (on page 194)* and *Range Editing Parameters (on page 197)*.

![](media/media/image175.jpeg){width="4.915271216097988in" height="2.4473950131233595in"}

> ![](media/media/image176.jpeg){width="5.066666666666666in" height="3.0083333333333333in"}

To change specific cell data such as DMX offset, you will need to use {Edit Multicell}. With a multicell fixture or a master cell selected in the fixture editor, press {Edit Multicell}. In the Edit Multicell window, you can edit cell numbers, DMX offset, and mastered cells for each cell.

![](media/media/image177.png){width="4.73326334208224in" height="1.5604166666666666in"}

Once you are finished editing, press {Save Fixture} to save your changes or {Cancel Edit} to remove the changes and exit the edit mode.

### Labeling

To label a channel or address, press the [Label] key with the channel or address selected on the command line. You can use the virtual alphanumeric keyboard or an external keyboard to enter the desired label text.

If you would like your label to wrap, use CTRL+J or type || to create a line break between words.

### Using the Scroller/Wheel Picker and Editor

The scroller and wheel picker allows you to choose a specific scroll, color wheel, gobo wheel, or effect wheel from standard manufacturers and associate them with fixtures. You may also create customized scrolls/wheels using the editor to match custom devices installed in your fixture.

> **Note:** *Scrollers, color wheels, gobo wheels, and effect wheels can be created without first selecting or patching a fixture.*

#### Using the Picker

Default color and pattern media for the selected fixture, as determined in the fixture library, is displayed in the {Attributes} page. Only the media attributes that are available for the selected fixture will display.

In the image below, the selected channel is a Source Four Revolution® with a color scroller and two gobo wheels. If the selected channel included other wheels, each device would be represented in the display with a button.

![](media/media/image178.jpeg){width="4.402270341207349in" height="1.35375in"}

The picker displays on the left half of the CIA when you select the specific attribute ({Scroller},

{Color Wheel}, {Gobo Wheel}, or {Effect Wheels}). The picker displayed is specific to the selected attribute (the scroll picker will display when {Scroller} is pressed, the color wheel picker will display when {Color Wheel} is pressed, and so on).

The picker displays buttons for the standard scroll or wheel type of the selected channel. The default selection is the wheel as shipped from the manufacturer (derived from the fixture library). Displayed to the left of the standard scroll/wheel selection is a list of each color/gobo as they are installed in the selected device (frame by frame). When the color or pattern image is available, it will display next to the frame name.

In the above image, {ETC Scroll} is the default scroll for the selected ETC Source Four Revolution. The list of gel colors as they are installed in the scroll are displayed to the left with a color chip for easy reference. Selecting any other type, such as {Martin Scroll 2}, updates the frame list.

The softkeys displayed beneath the picker are {Clear Calib}, {Copy Scroller}, {Clear}, {New},

{Copy}, {Edit}, and {Delete}.

-   {Clear Calib} - clears out the calibration data for the whole scroller wheel and returns to the wheel's default data.

-   {Copy Scroller} - used to copy a scroller wheel and its calibration to another channel. See

> *Scroller Calibration Column (on page 180)*.

-   {Clear} - clears the selection type from the selected channel in the picker.

-   {New} - creates a new scroll or wheel and provides additional softkeys to enable the Editor. See *Using the Editor (below)* .

-   {Copy} - makes a copy of the currently selected scroll/wheel type, which can then be edited using the editor. See *Using the Editor (below)* .

-   {Edit} - used to edit an existing scroll or wheel.

-   {Delete} - used to remove the selected frame only from a scroll or wheel that you have created.

#### Using the Editor

The editor is used to create new or edit copied scrolls and wheels. While in the picker display, you can create a new scroll or wheel by pressing the {New} softkey or make a copy of an existing scroll or wheel by selecting the source, then pressing the {Copy} softkey.

The editor does not limit how many frames you can add to the scroll or wheel for the selected fixtures. Keep in mind that any fixture has its own limitations. For example, if you have created a custom color scroll with 30 frames, your selected fixture type may only provide you access to the first 24 frames that you created. This applies to wheels as well.

> **Note:** *If you try to select an existing scroll or wheel, the console will display a warning if it has more frames than are supported by your device.*

When using the editor, the following softkeys are available for use:

-   {Insert} - inserts a new frame above the selected frame.

-   {Delete} - removes the selected frame.

-   {Edit} - changes the selected frame.

-   {Invert} - reverses the order of the frames.

-   {Done} - completes the editing process.

#### Creating a New Scroll or Wheel

When you create a new scroll or wheel, {New Wheel n} appears in the wheel list as the selected button. The frame list will be empty with only "New" displayed in frame 1.

![](media/media/image179.jpeg){width="4.343082895888014in" height="1.2864577865266842in"}

You can label the new wheel by pressing [Label] and typing the desired label on the virtual keyboard and pressing {Enter}.

To select a color or pattern for the specific frame in the scroll/wheel, select the "NEW" text and press {Edit} or click the gray box in the C/G column of the frame. The available gel, color, gobo and effect media selections will be displayed.

![](media/media/image180.png){width="4.249517716535433in" height="1.7577077865266841in"}

The media selection includes the following softkeys:

-   {Gel}, {Color}, {Gobo}, and {Effect} - each will display available media selections as they are cataloged by the associated scroll or wheel manufacturers.

-   {Open Frame} - places the frame in Open White. Generallly, the first media frame is open.

-   {Cancel} - cancels the media selection and returns to the frame editor.

When a manufacturer is selected from the list, the catalog selection changes to display only the selected manufacturer's offerings. When a specific catalog is selected, the selected media will display.

When you make a media selection, the display returns to the new wheel frame list where additional frames can be added to the scroll or wheel by selecting the next frame area to add more frames.

> **Note:** *An {Invert} softkey will display when creating or copying a wheel or scroller.*
>
> *{Invert} is used to reverse the order of frames.*
>
> **Note:** *It is possible to import custom gobo images. See Importing Show Data (on page 157).*

#### Editing a Copy of a Scroll or Wheel

If a copy has been made of an existing scroll or wheel, the copied scroll or wheel will display as

{New Wheel n} before the standard manufacturer offerings. The frame list will include an exact duplicate of the copied selection.

To make a change to a frame, first select the frame then press {Edit} or click the gray box in the C/G column to display the media selection. Or you can insert a new frame above a selected frame using the {Insert} softkey.

For example, to insert a new frame in between existing frames 2 and 3, select frame 3 and press the {Insert} key. The media selection will display.

![](media/media/image181.jpeg){width="4.628253499562555in" height="2.30375in"}

The media selection includes the following softkeys:

-   {Gel}, {Color}, {Gobo}, and {Effect} - each will display available media selections as they are cataloged by the associated scroll or wheel manufacturers.

-   {Open Frame} - places the frame in Open White. Generallly, the first media frame is open.

-   {Cancel} - cancels the media selection and returns to the frame editor.

When a manufacturer is selected from the list, the catalog selection changes to display only the selected manufacturer's offerings. When a specific catalog is selected, the selected media will display.

When you make a media selection, the display returns to the new wheel frame list where additional frames can be edited in the scroll or wheel.

#### Scroller Fan Curves

Curves can be applied to the scroller fan parameter allowing for the output of the fan to be controlled by the intensity of the channel. The curves available for this are the same used for intensity parameters and cues. See *Applying a Curve To Scroller Fans (on page 458)*.

To set a curve to a scroller fan, go to Displays>Patch>Attributes>Fan Curve for each scroller.

#### Calibrating a Scroller Using the Encoders

You can calibrate the center point of any frame in a scroller using the calibrate feature. Calibrating a scroller is normally done from the live display. You can also calibrate using the ML display. See *Calibrating a Scroller Using ML Controls (below)*.

On Element 2 and Element Classic, you will need to use the ML Controls display.

> **Note:** *It is recommended that you calibrate your scroller frames starting with the last frame and working backward to the first frame. This will help ensure a complete and accurate calibration.*
>
> **Note:** *Calibration may need to be performed when you initially patch a scroller and may need to be adjusted through the course of operation as spring tension changes in a color scroller.*

To calibrate a scroller:

1.  Select the channel of the scroller you wish to calibrate.

2.  Press the [Color] encoder button. Multiple presses may be required before the scroller encoder is visible in the encoder LCD.

3.  Use the encoder to move all the way to the last frame of the scroller.

4.  Continue adjusting the frame in fine mode until the frame is centered in the desired position.

5.  Press {Calibrate} in the encoder LCD. The new center position is now stored for the selected channel.

6.  Press {Last} in the encoder LCD to move to the center point of the previous frame.

7.  Visually verify if the center point of the new frame is accurate. If it is, press {Last} again to move to the previous frame in the scroll. If not, follow the calibration procedure again.

8.  Repeat steps 4 through 8 until you have calibrated all of the frames

#### Calibrating a Scroller Using ML Controls

You can calibrate the center point of any frame in a scroller using the calibrate feature. This will ensure that color scroll frames will be centered over the aperture of the fixture when you advance a color scroll frame-by-frame. You can do this using the ML Controls display. See *Moving Light Controls (on page 128)*.

> **Note:** *It is recommended that you calibrate your scroller frames starting with the last frame and working backward to the first frame. This will help ensure a complete and accurate calibration.*
>
> **Note:** *Calibration may need to be performed when you initially patch a scroller and may need to be adjusted through the course of operation as spring tension changes in a color scroller.*

To calibrate a scroller:

1.  In the Live display, select the scroller channel.

2.  Open the ML Controls from the home screen or by using [Tab] [5]. On Element 2 and Element Classic, you can open the ML Controls via [ML Controls]. The color category will display automatically with the Hue and Saturation and scroller encoders and a frame picker open. If the scroller encoder isn\'t open, click the {Scroller} button.

3.  To begin calibrating, use the scroller encoder to adjust the centerpoint of a frame. It is recommended that you start with the last frame in the scroll.

4.  When the frame is centered, click {Calibrate}.

5.  Repeat for any remaining frames that need to be calibrated.

#### Scroller Calibration Column

Calibration information will be displayed in the scroller calibration column. Values in gray are the default data, and the values in blue are calibrated data.

![](media/media/image182.jpeg){width="2.634666447944007in" height="1.235in"}

The displayed calibration information is the DMX level that puts the frame into its center position. Information in the calibration column can be manually edited by clicking on it and typing in a new DMX level.

> **Note:** *Calibration data will only be applied to scroller wheels that are assigned to a channel. Data will not be displayed when viewing a wheel with an empty command line.*
>
> **Note:** *Calibration data can be returned to its default by clicking on the data and pressing [Clear]. If you are entering in new data and hit [Clear], the data will return to the default and not any previously calibrated data.*

Pressing the softkey {Clear Calib} will clear out the calibration data for the whole scroller wheel, returning it to the default data.

Scroller wheels and their calibration data can be copied to other channels.

-   [1] {Copy Scroller} [2] [Enter] - copies the scroller and calibration data from channel 1 to channel 2.

Scrollers that have calibrated data will display a "\~" after their name.

The {Calibrate} button will now only appear on scroller parameters that are currently not at the center of a frame.

#### Reordering Shutters

Shutters can be reordered in the Patch {Attributes} page. Press the {Shutter Order} button to open the shutter order display. The {Shutter Order} button will only display if a channel with shutters is currently selected.

> ![](media/media/image183.png){width="3.0156572615923007in" height="1.3975in"}

In this display, you can invert the {Shutter Order} or rotate the order using the arrow buttons. After you have created the order needed, press {Apply} for your changes to take effect.

##### Invert Rack

An {Invert Rack} option is available in Patch>Attributes>Scrollers/Wheels. This option will only display when a fixture with a shutter frame assembly parameter is selected.

The shutter frame assembly parameter allows for the shutter assembly to be turned. When

{Invert Rack} is disabled, a encoder will move the frame assembly from the right. When enabled, the frame assembly will move from the left.

### Patch > Patch

With Patch open, Eos defaults to this section. It provides access to data input fields that you may use to define devices in your lighting system.

> **Note:** *The Art-Net and sACN offset will display here.*

![](media/media/image184.png){width="3.020200131233596in" height="1.859374453193351in"}

-   {Channel} - In the patch display, all channels are displayed in numerical order. When multiple devices are patched to the same channel, the channel number is only displayed in the first row, additional devices are indicated with part extensions (example P2) on the next row of the table.

-   Select the channel number using the control keypad or the direct selects.

-   {Type} - Eos defaults to patching dimmers. To specify a specific device type for the selected channel, press the {Type} button from the CIA.

-   The two columns on the left side of the CIA are pageable and show manufacturer names. The four columns to the right of the manufacturer's list are pageable devices that are available from the selected manufacturer for patching.

-   Selecting a specific manufacturer repaints the display with all devices that are available from that manufacturer. After you select a device, the fixture/ device type appears in the command line, in the {Type} box in the CIA, and in the "Type" field for that channel in the patch display.

-   {Label} - An optional user-defined label. You can use the [Label] key to display the virtual PC keyboard on the CIA. Pressing {Label} or [Label], after a label has already been assigned, will display the label on the command line for editing purposes. Pressing [Label] [Label] will clear the text.

-   [1] [At] [5] [Label] <S4 house right> [Enter] - patches channel 1 to output 5 and labels channel 1 as "S4 house right".

-   {Address} - Required for DMX control of devices. You may use the either the [At] or [Address/Patch] key instead of the {Address} button.

-   Use the keypad to define the starting address for the device (from 1 to 32,767,488) or a port and offset value.You may enter a start address without defining an end address.

-   Eos will draw this information from the library data. If you wish to leave a larger output gap than required by the library, use {Offset}. See *Using Offset in Patch (on page 170)*.

-   If you specify a start address that conflicts with other channels already patched, the conflicting channels will be unpatched after a confirmation is provided by the user.

-   {Interface} - An optional field used to specify what protocols and interfaces should be used for the output. When the field is left blank, the default data output is used as selected in *Patch > Protocols (on page 186)* or Setup > Device > *Network (on page 224)*. If an output option is not enabled, it will appear grayed out in the {Interface} list.

-   {Preserve Native} - When Preserve Native is enabled, and you make changes to patch, your cues\' real world levels (like pan degrees) will be converted so that the DMX output is preserved instead of the degrees. This is primarily useful for fixture substitutions.

-   {Flash} - will bring a channel or address to full, and then every other second the level will move to 15%. That will hold for 1 second, and then the level will return to full. The channel or address will keep flashing until either the command line is cleared or {Flash} is selected again.

### Patch > Attributes

The Attributes section provides you with optional fields for additional information and details about the configuration of your rig. Attribute settings include {Preheat}, {Proportion}, {Curve},

{Fan Curve}, {LD Flags}, {GM Exempt}, {Invert Pan}, {Invert Tilt}, {Swap P/T}, and {Color Path}.

With one or more channels selected, Scrollers / Wheels will display only the parameters that apply to those fixtures will appear. Press the desired attribute button and use the keypad to set the attribute value.

![](media/media/image185.png){width="3.1671883202099735in" height="1.9960411198600174in"}

-   {Preheat} - This field allows you to specify an intensity value or preset to preheat incandescent filaments. When a preheat flag is applied to a cue, any channels that are fading from zero to an active intensity and have been assigned a preheat value in patch will preheat in the immediately preceding cue. The preheat flag is applied to a cue as an attribute when the cue is recorded.

-   [1] {Preheat} [0] [3] [Enter] - channel 1 is assigned a patched preheat value of 3%.

-   [1] {Preheat} [Preset] [Enter] - channel 1 is assigned to use the preheat value of the preheat preset. See Setup > System > *System (on page 212)* > Preheat Preset.

-   {Proportion} - An attribute to set a modifier for the intensity of the device. For example, if the proportion is set at 90%, the actual output will always be 10% lower than the specified intensity parameter, as impacted by the various playbacks or submasters. This value is set numerically in a range of 0% to 200%.

-   [1] {Attributes} {Proportion} [1] [2] [5] [Enter] -applies a 125% proportion to channel 1.

-   [1] {Attributes} {Proportion} [Enter] - removes the applied proportion from channel 1.

-   {Curve} - Used to assign a curve to a channel in Patch. In Patch, curves can be applied to intensity and non-intensity parameters. See *About Curves (on page 456)*.

From channel view:

-   [1] {Curve} [4] [Enter] - applies curve 4 to the intensity parameter of channel 1.

-   [2] [Part] [3] {Curve} [3] [Enter] - applies curve 3 to the intensity assigned to channel 2, part 3.

From address view:

-   [3] {Curve} [3] [Enter] - assigns curve 3 to address 3.

-   [3] [/] [2] {Curve} [4] [Enter] - assigned curve 4 to universe 3, address 2.

-   {Fan Curve} - Used to assign a curve to the scroller fan parameter, which allows for the output of the fan to be controlled by the intensity of the channel. Curves available for this are the same used for intensity parameters and cues.

> **Note:** *When {Curve} or {Fan Curve} is pressed, a list of the available curves will be displayed. Clicking on an available curve will assign it.*

-   {LD Flags} - This field allows channels to contribute to live and dark move flags in the playback status display. Disabling will prohibit those channel moves from contributing to the live and dark move flags. This is enabled by default.

-   {GM Exempt} - Used to exempt the intensity of channels from grandmaster, blackout, rem dim, and go to cue 0 operations.

-   {Invert Pan} {Invert Tilt} - An automated fixture attribute used to invert the output of pan, tilt, or both. Select either the {Invert Tilt} or the {Invert Pan} button on the CIA.

-   [2] {Attributes} {Invert Pan} - inverts the output of the pan parameter on channel 2.

-   {Swap P/T} - An automated fixture attribute used to exchange pan and tilt levels. Select the {Swap} button on the CIA.

-   [2] {Attributes} {Swap} - swaps the pan and tilt parameters for channel 2.

-   {Color Path} - A default Color Path can be assigned at the channel level in Patch. That color path will be used for all of that channel\'s color fades unless overridden at the cue level. Submasters and manual transitions that use that channel will use the default color path as well. See *Color Path (on page 257)*

-   [1] [Path] [2] [Enter] - will assign color path 2 to channel 1

    -   Ion Classic and Element Classic users will need to use {Color Path}

-   {Scrollers} - An attribute used to change the scroll loaded in a scroller or automated fixture. Select the {Scrollers} button on the CIA to display the scroller picker and the scrolls available for your device. See *Using the Picker (on page 176)*

-   [2] {Attributes} {Scrollers} -opens the Scroller Picker in the CIA for scroll selection for channel 2.

-   {Color Wheels} - An attribute used to change the color wheel loaded in an automated fixture. Select the {Color Wheels} button on the CIA to display the wheel picker with the options available for your device. See *Using the Picker (on page 176)* "More" as shown in the patch display, indicates additional parameter properties are available for the selected device, such as the color and gobo wheels.

-   [4] {Attributes} {Color Select} - selects channel 4 and opens the wheel picker in the CIA for color wheel selection.

-   {Gobo Wheels} - An attribute used to change the gobo wheel loaded in an automated fixture. Select the {Gobo Wheels} button on the CIA to display the wheel picker with gobo options available for your device. See *Using the Picker (on page 176)*

-   [3] {Attributes} {Gobo Select} - selects channel 3 and opens the Wheel Picker in the CIA for gobo wheel selection.

-   {Effect Wheels} - An attribute used to change the effect wheel loaded in an automated fixture. Select the {Effect Wheels} button on the CIA to display the wheel picker with the options available for your device. See *Using the Picker (on page 176)* "More" as shown in the patch display, indicates additional parameter properties are available for the selected device, such as the color and gobo wheels.

-   [5] {Attributes} {Beam FX Select} - selects channel 5 and opens the wheel picker in the CIA for effect wheel selection.

### Patch > Database

The Database section provides you with additional fields for entering information that can be used by the Query function. See *Query (on page 372)*. These fields include {Notes} and {Text 1} through {Text 10}. Clicking on {Text 1} through {Text 10} will open up a display for selection of keywords. It will display keywords that were already created as well as showing an option for creating new keywords. Clicking on {New Keyword} will display an alphanumeric keyboard for entering in a new keyword.

![](media/media/image186.png){width="4.925597112860892in" height="3.006666666666667in"}

-   {Text} - Text fields are used to provide up to ten keywords about any channel or group of channels. These fields can be anything that you think is important about a channel, such as its location (FOH), an attribute of it (wash, spot), or other characteristics of the channel (such as gel). Select {New Keyword} and use the virtual keyboard in the CIA, or an external keyboard, to provide up to 30 characters of key words about the device.

-   [5] {Database} {Text 1} < FOH right> [Enter] - adds text to channel 5.

-   [5] {Database} {Text 2} [Label]downstage right [Enter] - adds text to channel 5.

-   {Notes} - Provides you the ability to attach a text note to a channel or group of channels. Select the {Notes} button on the CIA to display the virtual keyboard. You may type a label or any length of note regarding your channel in this space.

-   [5] {Database} {Notes} <this fixture is a backup to channel 15 for front of house right / new lamp installed on 10/4/17> [Enter] - adds a note to channel 5.

-   {Gel} - The Gel field is a dedicated location for notes about gels.

#### Adding Keywords in Patch

If you plan on being able to query channels based on a keyword association, the keyword must be defined in patch.

Keywords entered are automatically used by Augment3d as tags on the associated channel / fixture. Spaces are replaced with an underscore (_). For more information on tags, see *Hierarchy (on page 511)*.

To enter a keyword for a channel:

1.  In Patch > Database, select a channel or range of channels in the command line.

2.  Touch one of the {Text (1-10)} touchbuttons in the CIA to specify which keyword you are entering. A list of previously defined keywords will be posted. Select from these or press

> {New Keyword}. A virtual alphanumeric keyboard will appear.

3.  Type the keyword or words you wish to use.

4.  When finished, press [Enter].

Once keywords have been created, they will appear in the keyword section of the CIA when a query is performed. For more information on keyword queries see *Query (on page 372)*.

#### Deleting Keywords from the Database

Keywords can be deleted from any of the ten text fields in the database. To delete a keyword from the entire database, you would use the following syntax:

-   [Delete] {Text1} <orange> [Enter] [Enter]

This will delete orange anywhere it was used in any text field of any channel.

To just remove a keyword from a specific channel, you would use the following syntax:

-   [1] {Text1} [Enter]

That would remove the text from channel 1\'s first text field only. If you wanted to clear the second text field, you would select {Text2} and so on.

#### Renaming Text Fields in Patch

You can rename the text fields. By default, the text fields are named {Text 1} through {Text 10}. Text fields 1 through 10 display in the Patch display. Renaming those fields will rename the columns associated with them in the Patch display.

-   {Text 1} [Label] <Position> will rename the text 1 field to Position.

### Patch > Augment3d

The Augment3d section provides you with position, orientation, related properties, and FPE data for any patched items present in your Augment3d model. See *Fixtures in Augment3d (on* *page 520)*.

### Patch > Protocols

![](media/media/image187.jpeg){width="5.84536198600175in" height="1.5108322397200349in"}

The Protocols section allows you to configure settings for your console\'s data output.

> **Note:** *Protocols can also be enabled or disabled via Setup > Device > Network (on page 224).*
>
> **Note:** *Apex consoles, Windows 10 consoles, and ETCnomad software do not support Net2 or AVAB UDP output protocols.*

#### sACN

##### Enabled Protocol

Enables or disables output of the sACN protocol. Defaults to enabled.

##### Start Universe

Choose a starting sACN universe between 1 and 63,999. Defaults to 1.

Changing the start universe will offset your patch; for example, if you start at universe 3, anything patched to address 1 will actually output to address 1025 (universe 3, address 1).

##### Default Protocol

Enables or disables sACN as a default output protocol. Defaults to enabled.

##### Output Priority

Sets the sACN output priority level from 1 (lowest) to 200 (highest). Defaults to 100.

##### Backup Uses Higher Priority

This enables the backup device in a multi-console system to take over at one priority level higher than the current priority if the primary goes offline. Any per-address priority levels will also increase by one.

##### Per Address Priority

Enables or disables per-address priority for all sACN universes (commonly referred to as the \"DD packet\").

> When enabled, individual sACN output priority levels can be entered for any patched addresses via the sACN Interface column in the *Patch Main Display (on page 164)*. See *Patch*

-   *Patch (on page 181)*.

##### Per-Universe Overrides

The following options are available in the table:

-   Universe - the sACN universe number.

-   Output Universe - the universe number on which sACN outputs, based on the start universe.

-   Priority - override the default output priority level of the selected sACN universe.

-   Per Address Priority - enable or disable per-address priority for the selected sACN universe.

-   Multicast - enable or disable multicast output for the selected sACN universe.

-   Unicast - you can transmit to one or more unicast IP addresses. Enter IP addresses via the box, then select one or more addresses to enable output.

Unicast destinations can also be added from the command line with the syntax {sACN}

{Universe} [#] {Unicast Destinations} #.#.#.# [Enter], e.g. sACN Universe 1 Unicast Destinations 10.101.1.1. Additional sACN universes can be added with [Thru] and additional unicast addresses with [+].

When Eos is configured to output to unicast addresses, generally only a single universe will need to be sent to a single IP address. However, Eos can output up to 64 universes and IP addresses total. This total can be divided however you see fit; for example, you could output 64 universes to a single IP address, 16 universes each to four IP addresses, 10 universes to one IP address and the other 54 to a second IP address, and so on.

#### ArtNet

##### Enabled Protocol

Enables or disables output of the Art-Net protocol. Defaults to disabled.

##### Start Universe

Choose a starting Art-Net universe between 0 and 255. Defaults to 0 (0:0:0). Art-Net addresses can be displayed as a single number (e.g. 1) or divided into a network number, subnet number, and port number (e.g. 0.0.1).

Changing the start universe will offset your patch; for example, if you start at universe 3, anything patched to address 1 will actually output to address 1025 (universe 3, address 1).

##### Default Protocol

Enables or disables Art-Net as a default output protocol. Defaults to disabled.

##### Broadcast Mode

Choose between the following options:

-   Directed Broadcast - broadcast packets are directed to a subnet based on the IP address and subnet mask of the sender.

-   Limited Broadcast - the limited broadcast address is 255.255.255.255. Since routers will never forward datagrams with that destination address, datagrams with the limited broadcast address are confined to the particular network segment on which they originate.

##### ArtPoll

Enables or disables the sending of ArtPoll packets for device discovery via Art-Net2 and later. Currently, Eos only uses ArtPoll to identify itself on the network. Older or incompatible Art-Net devices can experience issues interpreting ArtPoll packets, which may be mitigated by disabling it. Enabled by default.

##### Per-Universe Overrides

The following options are available in the table:

-   Universe - the Art-Net universe number.

-   Output Universe - the universe number on which Art-Net outputs, based on the start universe.

-   Broadcast - enable or disable broadcast output for the selected Art-Net universe.

-   Unicast - you can transmit to one or more unicast IP addresses. Enter IP addresses via the box, then select one or more addresses to enable output.

Unicast destinations can also be added from the command line with the syntax {sACN}

{Universe} [#] {Unicast Destinations} #.#.#.# [Enter], e.g. sACN Universe 1 Unicast Destinations 10.101.1.1. Additional sACN universes can be added with [Thru] and additional unicast addresses with [+].

When Eos is configured to output to unicast addresses, generally only a single universe will need to be sent to a single IP address. However, Eos can output up to 64 universes and IP addresses total. This total can be divided however you see fit; for example, you could output 64 universes to a single IP address, 16 universes each to four IP addresses, 10 universes to one IP address and the other 54 to a second IP address, and so on.

#### Local DMX

Controls are available to enable or disable local DMX and designate it a default protocol. Both default to enabled.

### Patch > Device List

Device List is used to discover, configure, and monitor compatible Remote Device Management (RDM) and network devices. RDM allows for bi-directional communication between a RDM compatible device, such as a lighting fixture, and your console.

#### {Dimmers}

Handles setting up dimmer feedback from CEM+, CEM3, and FDX 2000/ 3000. You can also do some configuration of dimmers from this list.

#### {RDM}

Handles RDM feedback with devices. You can also do some configuration of devices from this list. Once RDM compatible devices have been patched, they keep communicating with the console to allow you to know when things like blown lamps happen or if a device goes offline for some reason. See *RDM Device List (on page 190)*

Device List displays all discovered devices during the current session and all devices that have been stored in the show file.

> **Note:** *Consoles only support RDM devices that are connected through a Gadget, Local I/O, or external ACN gateway (running version 5.1 or higher).*
>
> **Dimmer List for CEM+, CEM3, and FDX 2000/3000**
>
> **Note:** *For Dimmer Feedback, these software versions are required: CEM+ v3.0 and newer, CEM3 v1.3.1 and newer, and FDX v3.4.0 and newer.*

To use the Dimmer Feedback area of the Device List, you must first enable feedback. In the network tab of the ECU, when using CEM+ or CEM3, make sure {Sensor/ FDX3000 Feedback} is enabled, or when using FDX 2000/ 3000, make sure that {Sensor/ FDX3000 Feedback} or

> {FDX2000 Feeback} is enabled. The default setting is disabled for both. See *Interface Protocols (on page 587)*

Open the Dimmer Feedback display while in the Patch display by pressing {Device List}>

{Dimmers}. When the dimmer list is opened, the dimmers will be displayed in Patch by Address mode.

![](media/media/image188.png){width="5.059214785651793in" height="2.6877077865266843in"}

Eos will display the following information that it receives from the dimmers:

-   Address

-   Channel

-   Label

-   System

-   Rack

-   Lug

-   Module Type

-   Firing Mode

-   Control Mode

-   Curve

-   Recorded Loads

> **Note:** *The System ID number from CEM3 is not currently supported.*
>
> **Note:** *Rack numbers and dimmer numbers need to be unique for Eos to properly recognize them. For CEM+, dimmers also need to be patched to different sACN addresses.*

With a dimmer or dimmers selected, you can edit various dimmer settings in the property view, which will display in the CIA. Items with a caret (>) are editable. When multiple dimmers are selected together for editing, an "*" will show for data that is different between the selected dimmers.

![](media/media/image189.png){width="4.814755030621172in" height="2.0009372265966756in"}

FDX dimmers will not display data for the following:

-   Recorded Load

-   Actual Load

-   Rack Dimmer Source

-   Threshold

-   Scale Minimum

-   Preheat Enable

-   Preheat Timing

-   AF Enable

> **Note:** *When dimmers are discovered, they are not automatically attached to patched channels in Eos; you must attach a dimmer to a channel. See Patching Discovered Dimmers and RDM Devices (on page 192)*

#### RDM Device List

Before you can start using the RDM Device List, you must first enable {RDM} for the appropriate DMX ports in Setup > System > Output, or for the appropriate ethernet ports in the Network ECU tab. By default RDM is disabled. See *Local Output (on page 228)* or *Interface Protocols (on page 587)* If using Network RDM, this must be done via an ETC Net3 Gateway and RDM must also be enabled on the DMX ports of the Gateway. The Gateway needs to be running version 5.1 or newer.

Open the RDM Device List while in the patch display by pressing {Device List}> {RDM}. You will need to make sure that {Device Discovery} is enabled.

{Device Discovery} is disabled by default. The {Device Discovery} option will not display if

{RDM} is disabled in the ECU.

> **Note:** *{Device Discovery} will automatically disable when you leave the patch display.*

When the RDM device list is opened, the devices will be displayed in Patch by Address mode. At the top of the list is a RDM indicator. This indicator shows incoming and outgoing RDM traffic.

Eos will display the following information that it receives from the RDM devices:

-   Address (a part will be added if multiple devices are discovered with the same address)

-   Channel

-   Label

-   Manufacturer

-   Model

-   Footprint

Eos will also display what personality from the library the device matches in the Eos Type column. This information will not display until you first select the device. Once the device has been selected for the first time, Eos will extract the type information from the device and display it.

-   The following messages may display in the Eos Type column:

-   No RDM Data Available - no model specific RDM data has been extracted from the device.

-   Extracting RDM Commands - currently getting the command data from the device.

-   Extracting RDM Fixture -currently getting the data required to create a fixture definition for the device.

-   Extracting RDM Sensors - currently getting the sensor definitions from the device.

-   Offline - no model specific RDM data has been extracted from the device and it is now offline.

With a device or devices selected, you can edit various device settings in the property view, which will display in the CIA. Items with a caret (>) are editable. When multiple devices are selected together for editing, an "*" will show for data that is different between the selected devices.

![](media/media/image190.png){width="5.081275153105862in" height="1.836353893263342in"}

The following buttons will also display in the property view:

-   {Device Properties} - opens the properties list for the selected RDM device.

-   {Sensors} - displays if the selected device has sensors. Pressing {Sensors} will open the sensors list.

-   {Lamp Controls} - displays if the selected device has lamp controls.Pressing {Lamp Controls} will open the lamp controls list.

-   {Channel} - channel number of the selected device.

-   {Address} - address of the selected device.

-   {Device Discovery} - allows for discovery of RDM devices.

-   {Ignore Errors} - when enabled, errors messages will not display in the live/blind displays. They will still display in about and the properties display in patch.

-   {Reload RDM Data} - deletes the fixture data from the console and reloads it from the device.

-   {Flash} - triggers the identify function of the RDM device. The identify function may defer between different manufacturers\' devices. For example, Wybron scrollers identify

-   by wiggling their gel back and forth.

-   {!} or {?} - displays if selected device has errors. Pressing {!}/{?} will open the error list.

#### Patching Discovered Dimmers and RDM Devices

When dimmers/devices are discovered, they are not automatically attached to any patched channels in Eos. If you want the benefits of dimmer or RDM feedback, you must attach a dimmer or device to a channel.

If you patch a dimmer/device\'s address to a channel, while in the device list display, the dimmer/device will be automatically attached to that channel. However, if you patch outside of the device list, you will need to {Attach} the device to the channel.

> **Note:** *If the dimmer/device\'s address is not yet used in the patch, it is easiest to patch the address to a channel in the dimmer list or device list screen.*

<Chan> [X] {Attach} or <Address> [X] {Attach} will link that channel/address in patch and the dimmers/devices at that address.

When a channel number is attached to a dimmer/device, by patching it or using {Attach}, the channel's fixture type is changed to the dimmer or device fixture type.

The advantages of attaching a dimmer to a channel are:

-   The console warns you when a channel's attached dimmer has an error or is offline.

-   Items that are attached between patch and the device list will display a caret (>) beside their channel/address in patch.

The advantages of attaching a device to a channel are:

-   Its fixture type is copied to the channel.

-   The console warns you when a channel's attached device is offline or has an error.

-   The device will always appear in the device list display, even if the device is offline.

-   Items that are attached between patch and the device list will display a caret (>) beside their channel/address in patch.

#### Errors and Warnings

One of the advantages of using dimmer and RDM feedback is error and warning reporting. If something happens with a patched and attached dimmer/ device, you will be notified in Live, Patch, and About with an exclamation mark.

Errors can be viewed in the About Channel and About Address displays. The notifications you can see are:

-   A red "!" means that the dimmer/ device has errors, such as overtemp, breaker trip, and lamp out.

-   Yellow "?" means that the dimmer/ device has a warning message. Warning messages can include:

-   Multiple devices' addresses overlap

-   Multiple devices or different devices at this address

-   Patched fixture type mismatch

-   Patched fixture address mismatch

-   Offline

#### Detaching Devices

Pressing {Attach} twice will post the {Detach} command.

<Chan> [X] {Attach} {Attach} or <Address> [X] {Attach} {Attach} will remove the link between that channel/address and the device at that address.

### Clearing the Patch

You can clear the patch entirely by accessing the clear functions from Browser> Clear. The clear functions window will open in the CIA.

![](media/media/image191.png){width="4.196944444444444in" height="1.3885411198600175in"}

To clear the patch, click {Clear Patch}. A confirmation is required before the patch will be cleared.

To create a 1-to-1 patch, click {Patch 1 to 1}. This will remove the current patch.

To exit the clear functions screen without clearing, press the [Displays] key at any time or select a clear button and then select {Cancel} from the confirmation screen.

### Update Profile

When a new library is installed on Eos either from a software update or a separate fixture library file from the ETC website, changes in library data will not automatically update your show files. This is to prevent library changes from affecting a functional show file.

Using the {Fixtures} softkey in patch will open up the list of fixtures used in the current show file. In this view, you will be able to tell which fixtures in the currently loaded show file differ from the console's fixture library. Fixtures that have either been edited or their profile does not match the current library will display with an \"*\" beside their name. For fixtures that have a library update, the {Update Profile} softkey will display in white, and for fixtures that don't have an update, the {Update Profile} softkey will be grayed out.

> **Note:** *When updating a fixture in Patch, a warning message will display that includes what changes will be made to the fixture by updating it. Press {Ok} to update the profile or {Cancel} to return to the fixture editor.*
>
> **Note:** *For multi-console systems, all devices have to use the same fixture library. If the fixture library is different between devices, a warning will be displayed on the* *device trying to connect to the system.*

### Fixture Editor

Eos provides you with the ability to create your own fixture type within patch and store it with your show file. You can name the fixture, assign all necessary parameters, define the address and operational range of those parameters, see fixture modes and their properties, and set lamp controls.

> **Note:** *Before you create a new fixture, it is helpful to look at a few fixture personalities of similar fixtures to get an idea of how to set yours up. You may even want to look at their user manuals to see how their defined DMX footprints look as a fixture profile. This is especially helpful when creating Modes.*

The fixture creator is accessible from patch. Once a fixture has been created, it is stored in the show file. It is not added to the fixture library. If you want to use the created fixture in another show file, you will need to use merge. See *Merging Custom Fixtures into a New Show File (on page 209)*

If you would like to remove any unused fixtures from this list, press {Delete Unused}.

![](media/media/image192.jpeg){width="5.070875984251969in" height="2.2720833333333332in"}

To open the fixture editor, open the patch display and press the {Fixtures} softkey. This will open a list on the left displaying those same fixtures that are currently patched or have been added to the show, and the list on the right are the parameters for the selected fixture.

#### Creating a New Fixture

New fixtures are created from the fixture editor. You can either create a new fixture, or copy an existing fixture to edit. See *Copying a Fixture (on page 208)*

To create a new fixture, press {New}. A new fixture will be added to the fixture list.

##### Naming a New Fixture

Once the new fixture appears in the list, it is recommended that you name the fixture you are about to create.

To name a fixture in the creator list:

1.  Use the [Page] keys, mouse, or touchscreen to select the new fixture.

2.  Press [Label] or tap on the new fixture. You can press [Label] twice to clear the name. The virtual keyboard will open in the CIA.

3.  Enter the desired name for the new fixture on the virtual (or attached alphanumeric) keyboard.

4.  Press [Enter]. The name will appear in the "Type" column of the fixture list.

##### Adding Parameters

After naming the fixture, you can specify which parameters the new fixture contains.

> **Note:** *For 16b parameters, LDMX or "low-DMX" is the DMX address for the second half of any 16-bit channel. If used in Coarse/ Fine determination, the DMX channel defines the "Coarse" adjustment and the LDMX defines the "Fine" adjustment. Do not count 16-bit parameters as two parameters, this will be done in a later step.*

To add parameters to a new fixture:

1.  Use the [Page] keys, mouse, or touchscreen to select the new fixture.

2.  Select the parameter list by clicking on it or touching it.

![](media/media/image193.png){width="4.945543525809274in" height="2.08125in"}

3.  Determine the total number of parameters that your fixture has. Do not count 16-bit parameters as two parameters, this will be done in a later step.

4.  Press {New} or {+} to add parameter slots. Repeat this step until you have as many slots as are required by the number determined in step 3.

> **Note:** *When {New} or {+} is pressed, the parameter slot will appear in the list with a default name in the "Parameter" column. You may disregard these default parameters as you will redefine the designations in a later step.*

5.  Use the [Page] keys, mouse, or touchscreen to navigate to any parameter slots that you wish to alter the default parameter designations for.

6.  Click on the slot to open a dropdown list of available parameters.

![](media/media/image194.png){width="1.833096019247594in" height="1.203124453193351in"}

7.  Click on a category to open the dropdown list to see the parameters, or use the search box to find the parameter.

![](media/media/image195.png){width="1.833096019247594in" height="1.203124453193351in"}

8.  Press the desired parameter to assign it or press [Enter] when the parameter is selected.

9.  Repeat steps 5 through 8 until you have entered all of the required parameters for the new fixture.

If you are missing a parameter slot: At any point you can use the [Page] keys and {Insert}, to insert a parameter slot above the selected one.

If you want to remove a parameter: you can use the [Page] keys and {Delete}, to remove a parameter from the list.

###### Locked Value

A parameter can be assigned as a locked value. When used, the output address and value will be locked at the profile level. This option is available under Control in the parameter dropdown list.

##### Define Parameters

Once you have added and specified all of the parameters for the new fixture, you can now define the address requirements, size, and ranges for each of them.

To define the size (8-bit or 16-bit), DMX address, and LDMX address of any parameter:

![](media/media/image196.png){width="1.324876421697288in" height="1.1266666666666667in"}

You can alter the default DMX address assigned to any parameter in the list. This is not the actual address that will be used when patched, but rather it is the order of address for the parameter relative to the other parameters in the fixture.

LDMX or "low-DMX" is the DMX address for the second half of any 16-bit channel. If used in Coarse/ Fine determination, the DMX channel defines the "Coarse" adjustment and the LDMX defines the "Fine" adjustment.

1.  Use the [Page] keys to navigate to any parameter that you wish to alter the size of. The system defaults to 8-bit for any new parameter.

2.  When selected, click Size to choose between 8-bit or 16-bit. If 16-bit is selected, the system automatically displays a LDMX option. This value can be altered.

3.  Enter the desired address for the DMX and/ or LDMX addresses using the keypad. To alter the Home settings for any parameter:

You can define the value for any parameter's "home" value.

1.  Click on the "Home" column of the desired parameter.

2.  Enter the desired home value (0 through 255 for 8-bit, and 0 through 65535 for 16-bit) using the keypad.

To enable the Snap setting for parameters:

You can enable snap for parameters to exempt them from cue timing, so they snap to their new value. For more information about snap, see *Snap Parameters (on page 203)*

1.  Use the [Page] keys to navigate to the "Snap" column of the desired parameter.

2.  Click in the 'Snap" column for the selected parameter to enable.

##### Range Editing Parameters

You can enter the operational ranges for specific slots within any specific parameter (such as color scroller, color wheel, gobo wheel, and so on). You can do this by either defining each range individually or you can use the *Quick Actions (on the next page)* tools to define multiple ranges at once.

![](media/media/image197.png){width="3.2952373140857394in" height="1.3695833333333334in"}

If a parameter has only one range, the values for that range will display in the range column. If that parameter has multiple ranges, the number of ranges will be displayed. If a range is used in a *Modes*, the range will not be in bold.

For example, if the parameter were "Gobo Wheel", and the fixture included a four-slot gobo wheel, you can use ranges to determine the minimum/ maximum values for each of those slots. You can also label the slots and define the minimum/ maximum values that will appear in the channel display for that parameter.

To define the range values individually for any parameter:

1.  Use the [Page] keys to navigate to the parameter that you want to add ranges to.

2.  Click on the range. The range window will open.

3.  Determine the total number of slots required by the parameter. Be sure to include "open" slots when needed.

4.  Press {New} or {+}to add ranges. Repeat this step until you have as many slots as are required by the number determined in step 3.

5.  Use the [Page] keys to select the range and field you wish to edit. Fields are:

    -   DMX Min - enter the minimum value (0-255 8bit / 0-65,535 16bit) for the range slot you are defining.

    -   DMX Home - enter the default value (0-255 8bit / 0-65,535 16bit) for the range slot you are defining.

    -   DMX Max - enter the maximum value (0-255 8bit / 0-65,535 16bit) for the range slot.

    -   User Min- enter the value that will be displayed to users (for example, what will be displayed in the live summary view) when the slot is at its minimum value. Value can range from -32767 to 65535.

    -   User Home- enter the value that will be displayed to users (for example, what will be displayed in the live summary view) when the slot is at its default value. Value can range from -32767 to 65535.

    -   User Max- enter the value that will be displayed to users when the slot is at its maximum value. Value can range from -32767 to 65535.

6.  Press {Label} to add a label to any range slots. These will appear in the encoder display (if available) and ML Controls when the related parameter is displayed for the new fixture.

7.  Press {Patch} when you have finished editing the ranges. To delete a range value, select it and press {Delete}.

###### Quick Actions

Quick Actions provides tools that allow for the creation of multiple ranges at once according to predefined actions.

> **Note:** *Quick Actions supports 8bit and 16bit parameters.*

Click on Quick Actions to open the menu. In this menu, you select the desired action and the number of slots needed.

The following actions are available:

-   As-Is - this is the initial mode. The ranges are unchanged. This allows you to view the range as it was.

-   User Values - these actions affect the user values.

    -   Framed - enter the number of frames that you would like to have on your collection of ranges. The console then distributes the DMX values and assigns a user range exactly as any of the wheel or frame parameters are automatically created. (Frames 1, 2, 3, etc would be represented as 0.5-1.4, 1.5-2.4, 2.5-3.4, etc)

    -   Matched - the user values are set to match the DMX values. This is required for a virtual parameter (one that has no DMX address) and is used as a *Modes* for another parameter.

    -   Scaled - users can enter the minimum and maximum user value to map their DMX ranges to an arbitrary user range. This is useful when creating pan/tilt ranges (e.g., - 180 to 180), or color temperature ranges (e.g., 3000 to 15000). DMX ranges are not changed and are assumed to be as the user intends. The DMX values are scaled into the new user range.

-   DMX Values - this action affects the DMX values.

    -   Distribute - select the number of ranges you wish to create. DMX values are then evenly distributed as specified.

###### Quick Labels

Click on Quick Labels to open a dropdown menu with labeling options. These options are broken down into two categories: units and labels.

-   Units

    -   Degrees

    -   Percent

    -   (none)

-   Labels

    -   Open

    -   Open/Color N

    -   Blackout

    -   Animation

    -   Animation N

    -   Color

    -   Color N

    -   Color M/N

    -   Color N/Open

    -   Effect

    -   Effect N

    -   Gobo

    -   Gobo N

    -   (clear)

Units are used to add a degree or percentage symbol to the end of a label when it displays in the encoder display or ML controls. If you want to remove a unit, select (none).

Labels are used to replace the text for all of the ranges. Labels that have an N after them will display the appropriate number in the encoder display or ML controls. For example, Gobo N will display the number of the gobo. Select (clear) to remove the labels.

##### Modes

A mode is a collection of ranges that will display in the encoder display and in ML controls when the mode\'s conditions are true. These ranges are part of one DMX address that is used to control two or more different by related functions, such as gobo index and rotate.

Examples of mode conditions are \"When Gobo Mode is Indexed\" or \"When Strobe Mode is Random\". Multiple conditions can be assigned. An example of this would be \"When Gobo Wheel Mode is Index or Index Scan\".

![](media/media/image198.png){width="3.286946631671041in" height="1.998957786526684in"}

When viewing a fixture profile, the parameters that have modes will display the number of modes in the ranges column.

> ![](media/media/image192.jpeg){width="5.070875984251969in" height="2.2720833333333332in"}
>
> **Note:** *When adding a new mode, you will need to first add the parameter that the mode needs to be associated with before you will be able to assign the mode. See Creating Modes (on the facing page).*
>
> Modes can be edited in the range editor; see *Range Editing Parameters (on page 197)*. The following buttons are available for editing modes:

-   {New Mode} - adds a new mode.

-   {Delete Mode} - deletes the selected mode.

-   {Next Mode} - advances your selection to the new mode.

-   ![](media/media/image199.png){width="2.4251859142607173in" height="1.7337489063867018in"}{Last Mode} - returns your selection to the previous mode. Clicking a new or existing mode will open the mode selection window.

This window displays all the possible conditions that can be applied to the fixture. The active ranges for the mode will already be selected with a checkmark.

A condition can only be present on a single mode. Similarly, if a parameter has multiple ranges, and it is selected as a condition for another parameter, all ranges need to be present on some modes of the fixture. For example, if gobo wheel has ranges of index, rotate, and shake, and you place index on a parameter for a mode, rotate and shake must also be used.

Once a parameter is used as a condition, it becomes read only. Only the labels for the ranges can be added/ edited.

> **Note:** *A single range parameter is not useful as a condition so those will not be available for selection.*
>
> **Note:** *Some fixtures use virtual modes. Those are modes without a DMX address assigned to them.*

###### Creating Modes

Let\'s take a look at how to create modes for a gobo wheel. This gobo wheel can be indexed or rotated.

In the fixture\'s manual, you will see something similar to this:

+----------+----------------------+-----------------------------------+
| 16       | Gobo Function        | Index 0 127                       |
|          |                      |                                   |
|          |                      | Rotate 128 255                    |
+==========+======================+===================================+
+----------+----------------------+-----------------------------------+

The sixteenth DMX slot for this fixture is gobo function, which has two ranges for index and rotate.

In the fixture editor, you assign a parameter as gobo wheel mode. Click in the range column to open the range editor. Use {+} to add a second range slot. Assign the appropriate range values, and label each range.

> **Note:** *For this example, the DMX min and max values were entered and then the Quick Actions (on page 198) Matched function was used so the user values and DMX values match.*
>
> **Note:** *It is important to name your ranges. Without labels, only the range values will display when selecting conditions, and the mode buttons in the encoder display and ML controls will be blank.*

![](media/media/image200.png){width="3.305534776902887in" height="1.3695833333333334in"}

Back in the fixture editor, assign a parameter as gobo index/speed. Click in the range column to open the range editor. Press {New Mode} to create two modes.

![](media/media/image201.png){width="3.314286964129484in" height="1.4764577865266841in"}

Click in the mode cell to open the mode selection window.

> ![](media/media/image202.png){width="4.8527045056867895in" height="1.7872911198600174in"}

This window will display all possible conditions that can be applied to your fixture. In this case, there are only two possible.

If a parameter has multiple ranges and is selected as a condition for a mode parameter, all the ranges for that parameter must be used. The fixture editor will allow you to select a condition for a mode and it will automatically place the other range(s) on the next mode.

![](media/media/image203.png){width="3.3107830271216097in" height="1.464582239720035in"}

Assign the DMX and user values. The range values were used for the DMX values. For index, the user values were set to 0-360 degrees. The *Quick Labels (on page 198)* for degree unit was used so the degree symbol will display in the encoder display. For rotate, the user values were to 0-80 rpms.

Once the modes are created using the index and rotate ranges, the gobo wheel mode parameter will be read only. The range editor for gobo wheel mode will give an advisory saying which mode the ranges are used in. If changes are needed to those ranges, press {Remove as Mode} in the range editor. After the changes are made, you will need to reassign the modes.

![](media/media/image204.png){width="3.3024671916010497in" height="1.2112489063867016in"}

After patching the new fixture, you will be able to check your modes in the encoder display and ML controls. There are now buttons for the modes, and for index, the degree symbol is displayed with the user value.

##### Fixture Lamp Controls

For many devices, their lamp and motor control functions can be controlled remotely using DMX. These will often require use of a timed sequence of DMX levels to control various functions such as striking the lamp, resetting the fixture, and other specific actions.

To define the lamp controls for a device:

1.  With the fixture selected, press {Lamp Ctrls}. The lamp control display will open.

2.  Press {New} or {+} to add as many lamp control options as needed.

3.  Click on the name in the lamp control column to name it.

4.  Click in the Steps columns (#, Time, DMX, and Level).

    -   # - the step number. Each step is tied to a time value, and will execute in order of the step number.

5.  Press {New} or {+} to add as many steps needed for the lamp control.

6.  Select the time column to change the timing for each step.

    -   Time (seconds) - Timing is in seconds. The standard time in the Eos Family library is 12 seconds.Hold can be assigned as a timing value.

> **Note:** *It is not recommended that you set the time to Hold unless the DMX value should permanently remain at that level. In order to alter a level set with a time of Hold, another lamp control to change that DMX value would need to be created.*

7.  For each step created, click in the DMX column and press {New} or {+} to add as many DMX addresses and levels as needed. You may setup as many levels as needed for each step.

> **Note:** *While a step is active, the DMX levels for the channel will be held. When a step is no longer active, the levels will be released back to their playback levels.*

-   DMX - the DMX offset of the parameter you wish to control. DMX can be set to All Offsets, which means that all DMX parameters for the fixture will be held at the specified level.

-   Level - the 0-255 level of the parameter.

##### Snap Parameters

Certain parameters may not want to be subjected to cue timing. Those parameters can be set to snap. By default, Eos will snap the parameters listed in the following table:

+--------------------+----------------+-----------------+-------------------+
| Beam FX            | Effect Library | MSpeed          | Shutter           |
|                    |                |                 |                   |
| Index/Speed        |                |                 |                   |
+====================+================+=================+===================+
| Camera IR          | Enable         | Negative        | Shutter Strobe    |
|                    |                |                 |                   |
| Image              |                |                 |                   |
+--------------------+----------------+-----------------+-------------------+
| Clip Directory     | File           | Object          | Strobe            |
|                    |                |                 |                   |
|                    |                | Directory       | Mechanism         |
+--------------------+----------------+-----------------+-------------------+
| Color Effect       | File Type      | Object File     | Sync Source       |
+--------------------+----------------+-----------------+-------------------+
| Color Index        | Front/Rear     | Output          | Text              |
|                    |                |                 |                   |
|                    | Projection     | Command         |                   |
+--------------------+----------------+-----------------+-------------------+
| Color Mix          | Generator      | Page            | Texture           |
+--------------------+----------------+-----------------+-------------------+
| Control            | Generic        | Position Blink  | Timeline          |
|                    |                |                 |                   |
|                    | Control        |                 |                   |
+--------------------+----------------+-----------------+-------------------+
| Copy Mod           | Image Movement | Projector Input | Timeline Position |
|                    |                |                 |                   |
|                    | Speed          |                 |                   |
+--------------------+----------------+-----------------+-------------------+
| Cue                | Internal Media | Relay           | Tracking          |
|                    |                |                 |                   |
|                    | Frame          |                 | Object            |
+--------------------+----------------+-----------------+-------------------+
| Dimmer Curve       | Library        | Select          | Transition        |
|                    |                |                 |                   |
|                    |                |                 | Speed             |
+--------------------+----------------+-----------------+-------------------+
| Edge Blend Profile | Macro          | Shape           | Transition Time   |
+--------------------+----------------+-----------------+-------------------+

  -----------------------------------------------------------------------
  Effect File       Mode              Shape Library     Transition Type
  ----------------- ----------------- ----------------- -----------------

  -----------------------------------------------------------------------

In the [About] channel patch screen, the snap column shows which parameters for that channel are currently set to snap. These parameters can be edited for any profile using the Fixture Editor. See *Fixture Editor (on page 193)*

![](media/media/image205.png){width="5.035937226596675in" height="1.3429166666666668in"}

##### Save Fixture

Unsaved fixture profiles will have a red background in the fixture editor.

Press {Save Fixture} to store the new profile, or {Cancel Edit} to exit out and not save your changes.

> **Note:** *If you leave the patch display without saving or using {Cancel Edit}, an advisory will display above the command line letting you know that you have unsaved data.*

![](media/media/image206.png){width="4.945543525809274in" height="2.08125in"}

##### Color Configuration

Color configuration information is stored within fixture profiles in your show file. Fixtures with additive color properties will display a color configuration button in the fixture editor, which will open the color configuration editor window.

> ![](media/media/image207.jpeg){width="5.8406528871391075in" height="3.1441666666666666in"}

###### Editing Color Configuration

For accurate color control, each color parameter in an additive fixture profile needs an accurate definition of the correct emitter color, wavelength (in nanometers), and relative brightness compared to the brightest emitter in the fixture.

The dropdown menus on the left allow you to choose the correct wavelength for each individual color parameter. The color band sliders on the right allow you to adjust the relative brightness.

####### Excluding Parameters

The checkbox by each color parameter allows you to exclude specific colors from color mixing. You will still be able to control excluded parameters directly, and none of their stored data will be cleared.

UV parameters are excluded (unchecked) automatically.

###### Color Configuration Data

The data required for color configuration can originate from a variety of sources.

####### Calibrated

Calibrated color configuration data has been gathered using lab-quality equipment and measuring techniques. This generally provides higher quality color picking and gel matching.

> ![](media/media/image208.png){width="3.9583333333333335in" height="2.2708333333333335in"}

Fixture profiles with calibrated color configuration are indicated in the fixture profile editor with a CIE icon.

####### Manufacturer

This type of color configuration data is provided by the fixture\'s manufacturer and can be manually entered into the profile via the color configuration editor. The quality of this data, and the subsequent color performance of the fixtures that use it, will depend on the quality of the manufacturer\'s initial measurement process.

####### Field Survey

There are a variety of ways to measure a fixture\'s color information with tools in the field. The fixture profile can then be updated with the gathered configuration data.

####### Default

If a fixture profile has none of the above types of color configuration data, Eos will create an auto-generated configuration based on the fixture\'s color parameters.

###### Legacy Color Calibration

If a pre-v3.2.0 show file with additive color RGB and RGBA fixtures is opened, Eos will automatically simplify the color calculations being used for those fixture profiles. This can greatly improve fixture performance and speed for use in pixel maps.

![](media/media/image209.png){width="3.6145833333333335in" height="1.375in"}

These fixture profiles can be updated via the color configuration editor to get the full set of color configuration tools.

> **CAUTION:** *Updating a fixture profile or library will update all legacy calibration.*

#### Creating Multicell Fixtures

Multicell fixtures can be created by using the fixture editor. You can either create a new fixture, or copy an existing fixture to edit.

To create a new fixture, press {New}. A new fixture will be added to the fixture list.

##### Naming a New Fixture

Once the new fixture appears in the list, it is recommended that you name the fixture you are about to create.

To name a fixture in the creator list:

1.  Use the [Page] keys, mouse, or touchscreen to select the new fixture.

2.  Press [Label] or tap on the new fixture. You can press [Label] twice to clear the name. The virtual keyboard will open in the CIA.

3.  Enter the desired name for the new fixture on the virtual (or attached alphanumeric) keyboard.

4.  Press [Enter]. The name will appear in the "Type" column of the fixture list.

##### Create Multicell

1.  With the new fixture selected, press {Create Multicell}.

![](media/media/image210.png){width="5.060395888013998in" height="2.129583333333333in"}

2.  Press {+} to add cells. This will open a fixture list display. Only fixtures added to your fixture list will be here.

![](media/media/image211.png){width="2.6738549868766404in" height="1.5383333333333333in"}

3.  Select a fixture, a cell profile from an existing multicell fixture, or create a new cell profile by selecting + Add New Cell Profile.

4.  Select the number of cells.

5.  Press {Ok} . When selecting a fixture, you will need to select {Make Copy as Cell} or

> {Convert to Cell}.

-   {Make Copy as Cell} - makes a copy of the existing fixture profile and patches the copy as a cell. This will break any references to the original profile.

-   {Convert to Cell} - converts to the fixture into a cell. This option will not be available for any library fixture or fixture currently patched in the show file.

6.  Make any changes needed to cell numbers, DMX offset, or mastered cells. These settings can be edited later by selecting the {Edit Multicell} button. See *Editing Multicell Fixtures (on page 174)*.

7.  Press {Save Fixture} to save your changes or {Cancel Edit} to remove the changes and exit.

> **Note:** *If you need to delete a cell profile that has been accidently selected, select the cell and set the number of cells to 0.*
>
> You can now add or edit parameters as needed. See *Editing Multicell Fixtures (on page 174)*.

#### Editing Fixtures

You can view and edit existing fixtures in the Fixture Editor. Edited fixtures will display with an \"*\" beside their name.

With the fixture selected, you can change the name by pressing [Label] or tapping on the fixture. You can press [Label] twice to clear the name. The virtual keyboard will open in the CIA. The fixture\'s name as it is in the library will still display by the new name.

> **Note:** *Using [Update Profile] will remove any edits made to existing fixtures. Fixtures that have been copied will retain any edits. See Copying a Fixture (below)*

##### Physical Data Editor

The Physical Data Editor provides options for editing Augment3d-related fixture information. The following options are available:

-   Fixture Model

-   Hang to Focus Offset X

-   Hang to Focus Offset Y

-   Hang to Focus Offset Z

Fixture Model allows the selection of the model displayed in Augment3d when the fixture has position data. Selecting \"No model\" will tell Eos to use the default fixture model closest to the fixture type. Practical light emitting objects (like desk lamps) can be found in the Practicals manufacturer.

Hang to Focus Offset is the XYZ offset from the center of the base to where the fixture will pan

/ tilt. It is used when converting between a desired XYZ beam end, and pan / tilt values.

#### Copying a Fixture

It is possible to copy an existing fixture and edit its parameters. In the fixture editor, there is a

{Copy} button. Pressing {Copy} when a library fixture is selected will create a copy of that fixture and will assign it a new name.

#### Merging Custom Fixtures into a New Show File

Custom fixtures are saved with your show file and not in the fixture library. If you want to use custom fixtures in a different show file, you will need to use the advanced merge function while in the new show file.

> For more information, see *Partial Patch Merging (on page 152)*

#### Importing a Custom Fixture

> You can import custom fixtures from an ASCII show file, see *Importing Show Data (on page 157)*

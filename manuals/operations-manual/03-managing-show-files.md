# Eos Family User Manual v3.2.0 — Chapitre 03 : Managing Show Files

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 3
## Managing Show Files
### About Managing Show Files

> This section explains how to create, open, and save your show files. Each of these operations are accomplished through the *Browser (on page 82)* area in the *Central Information Area (CIA) (on page 80)*.
>
> Show files can also be managed from the shell via the Eos Configuration Utility (ECU) File Manager. See *{File Manager\...} (on page 590)*.

### Creating New Show Files

To create a new show file, navigate within the browser to File > New and press [Select].

You will be prompted for confirmation that you want to create a new show. Any unsaved show data will be lost. Press {OK} to confirm or {Cancel} to discontinue the operation.

If you want your Augment3d model to be included in the new show, check the box labeled \"Preserve Augment3d Model.\" For more information, see *Augment3d (on page 495)*.

Ion Classic users can select a 1-to-1 patch by pressing the {Patch 1to1} option. A new show created with {Patch 1to1} selected will have a 1-to-1 patch and 1-to-1 channel to sub assignment. On Element Classic, this option is enabled by default.

#### Template Show Files

> A template show file can be assigned in the ECU via *Settings > General (on page 577)*.

When a show file is assigned as a template, Eos will create a copy of the file in the Templates folder to be used as the default starting point for any new show files. A new option will appear in the CIA under File > New From Template (*Template Show File Name*) to create a new show file identical to the template. A blank show file can always be created with the File > New option.

Templates can be managed via the File Manager, and are unaffected by deep clears. See

> *Settings > Maintenance (on page 589)*.

### Opening Existing Show Files

Names of show files may appear in the browser list in normal text or in bold text. Files in normal text indicate that there is only one show file stored by that name.

Bold show names indicate that there are several versions of the show file stored under that name, the bold one being the most recent. To access the most recent show file, simply select the bold name. You may right arrow from the bold name to expand a list of previous versions beneath it in the browser. Select the desired show from the expanded list.

To open an existing Eos Family show file, navigate within the browser to: File > Open and press [Select].

![](media/media/image156.png){width="3.3910925196850394in" height="1.1479166666666667in"}

Eos provides you with multiple locations to retrieve an Eos Family show file including:

-   Show File Archive - This is the default storage location for show files when a show file is created and saved. Older versions of the show file will be listed under the most current version.This allows you the ability to open the latest version or an earlier version of a show file if desired.

-   Network Drive- if one is connected. When there is no network drive connected, it will not display in the Browser.

-   USB device - When a USB device is connected and an Eos Family show file is available on the device, you will notice the USB is displayed in white text and is expandable.

Open the desired location:

-   To open a show file from the Show File Archive, navigate within the Browser to: File> Open> Show File Archive and press [Select].

-   To open a show file from the network drive, navigate within the Browser to: File > Open> Name of Network Drive> and press [Select].

-   To open a show file from a USB device, navigate within the Browser to: File> Open> Name of Drive and press [Select].

Select the specific show file

-   Navigate within the specified storage location and select the show file you wish to open, press [Select].

-   If the selected show has multiple time stamps and you wish to load an older version, navigate to the desired revision and press [Select].

This will open the partial show loading screen in the CIA.

From this screen you can select which components of the show file you wish to load. The buttons at the center of the CIA represent all of the show components that you can choose to load. By default all components are selected (gray) and will be loaded. To withhold any show components from loading, simply deselect them in the CIA by touching the respective button.

To reselect all show components, press the {Reset} button and all buttons will return to gray (selected). To stop the show load process, press the {Cancel} button.

When you have selected/deselected all of the show components you require, press the {OK} button.

Eos loads the selected show to the console.

> **CAUTION:** *On a partial show open, if any record targets are not opened, any existing data of that type will be cleared from the console.To merge show data, merge should be used. See **Merging Show Files (on page 151)***

#### Selective Partial Show Opening

If you select the {Advanced} button in the partial show opening screen, you will have the opportunity to load partial components from the show file and be able to specify the desired location of those partial components in the new show file.

> **CAUTION:** *On a partial show open, if any record targets are not opened, any existing data of that type will be cleared from the console. To merge show data, merge should be used. See **Merging Show Files (on page 151)** .*

For example, you could specify specific cues and load them to a different range of cue numbers in the new show. You could also specify only specific palettes, presets, effects, and so on. To see the complete list of show components, press the {Advanced} key in the partial show loading screen.

> ![](media/media/image157.png){width="5.4535553368328955in" height="1.3581244531933507in"}

As you specify components, they are added to a table in the CIA. In the table, fields with a dark background may be edited, fields with a light gray background do not apply to that component. For each component in the list, you can specify the desired range by pressing the proper area in the table and entering numbers from the keypad. The columns in the table are:

-   List - The list you are taking data from (such as a cue list).

-   List Target - The list you are adding the data to.

-   Start - The first in a range of components (such as a range of cues).

-   End - The last in a range of components.

-   Target - The desired location of the components in the new show file (for ranges, this will be the location in the new show of the first component in the range, the others will follow in order).

> **Note:** *In the {Advanced} view, you can use the [Thru] key to jump to the End column and [At] to jump to the Target column.*

To open only partial components from a show file:

1.  From the browser, navigate to the desired show file. See *Opening Existing Show Files (on page 148)*.

2.  When the partial show load screen appears, press the {Advanced} button. The partial components selection screen will appear in the CIA.

3.  Select the show components that you wish to load by pressing on their respective buttons on the left side of the CIA. The components will appear in the list to the right as you select them.

4.  Press any fields for which you want to enter specific numbers. The field (if editable) will highlight in gold.

5.  Enter the numbers using the keypad to specify the desired cues / groups / effects and so on.

6.  Press {OK} to load the components to the new show.

You may exit the partial show load screen at any time by pressing the {Cancel} button. This will return you to the browser.

You may clear all selected components from the table at any time by pressing the {Reset} button.

You may exit the advanced loading screen at any time by pressing the {Return} button. This will return you to the general partial show load screen.

> **Note:** *Media is imported gobo and magic sheet images, and will be included by default when you select Patch, Fixtures, or Magic Sheets.*

##### Partial Patch Opening

You have the option to selectively open partial patch information or fixtures into a show file by selecting the {Advanced} button in the partial show opening screen. Select {Patch} or

{Fixtures}.

> **Note:** *It is important to remember that on a partial patch open, if any record targets are not opened, any existing data of that type will be cleared from the console. To keep that data, merge should be used.*

You can specify the desired range by selecting the proper area in the table and entering numbers from the keypad. The columns in the table that relate to patch are:

-   Start - The first in a range of components.

-   End - The last in a range of components.

-   Target - The desired location of the components in the new show file (for ranges, this will be the location in the new show of the first component in the range, the others will follow in order).

#### Show File Advisory

If the loaded show file exceeds the console's output capacity, an advisory will display in the CIA. You will need to dismiss the advisory by pressing {Ok} before continuing. To see the capacity of the console, press [About].

#### Park Buffer

The contents of the Park buffer are saved with show files. By default, the park buffer will not open with a show file.

You can load the park buffer, but it requires an additional step of confirming that you want to open the park buffer. You will need to click or press the check box by the text Yes, Include the Park Buffer.

> For more information about park, see *About Park (on page 426)*

### Merging Show Files

All Eos family consoles support the merging of other Eos family show files.

> **Note:** *Merging show files is different from opening show files. When you do a partial open of show components, untouched record targets are cleared. When you do a merge, those record targets remain.*

To merge a show file, navigate within the Browser to: File > Merge. Navigate to the desired storage location and press [Select]. When using merge, Eos displays only the available files. Navigate to the specific file and press [Select].

This will open the merge screen in the CIA. From this screen you can choose which aspects of the show file you want to merge. By default all aspects are unselected (black). Selected show aspects will appear in gray.

> **Note:** *Media is imported gobo and magic sheet images, and will be included by default when you select Patch, Fixtures, or Magic Sheets.*

If you select the {Advanced} button in the merge show loading screen, you will have the opportunity to load partial components from the show file and be able to specify the desired location of those partial components in the current show file.

For example, you could specify only cues 5-10 and load them as cues 20-25 in the current show. You could also specify only specific palettes, presets, effects, and so on. To see the complete list of show components, press the {Advanced} key in the merge show loading screen.

![](media/media/image158.jpeg){width="5.065357611548556in" height="1.250832239720035in"}

As you specify components, they are added to a table in the CIA. In the table, fields with a dark background may be edited, fields with a light gray background do not apply to that component. For each component in the list, you can specify the desired range by pressing the proper area in the table and entering numbers from the keypad. The columns in the table are:

-   List - The list you are taking data from (such as a cue list).

-   List Target - The list you are adding the data to.

-   Start - The first in a range of components (such as a range of cues).

-   End - The last in a range of components.

-   Target - The desired location of the components in the new show file (for ranges, this will be the location in the new show of the first component in the range, the others will follow in order).

> **Note:** *In the {Advanced} view, you can use the [Thru] key to jump to the End column and [At] to jump to the Target column.*
>
> To merge channels, see *Partial Show File Channel Merge (on the facing page)*

To merge only partial components:

1.  From the browser, navigate to the desired show file (see *Opening Existing Show Files (on page 148)* ).

2.  When the merge show load screen appears, press the {Advanced} button. The partial components selection screen will appear in the CIA.

3.  Select the show components that you wish to merge by pressing on their respective buttons on the left side of the CIA. The components will appear in the list to the right as you select them.

4.  Press any fields for which you want to enter specific numbers. The field (if editable) will highlight in gold.

5.  Enter the numbers using the keypad to specify the desired cues/groups/effects and so on.

6.  Press {OK} to load the components to the current show

#### Partial Patch Merging

You have the option to selectively merge partial patch information or fixtures into a show file by selecting the {Advanced} button in the partial show merge screen. Select {Patch} or

{Fixtures}.

You can specify the desired range by selecting the proper area in the table and entering numbers from the keypad. The columns in the table that relate to patch are:

-   Start - The first in a range of components.

-   End - The last in a range of components.

-   Target - The desired location of the components in the new show file (for ranges, this will be the location in the new show of the first component in the range, the others will follow in order).

Checking the \"Only Merge Augment3d XYZ Location\" box will merge only the Augment3d position information of the selected range without merging any additional patch data.

#### Partial Show File Channel Merge

![](media/media/image159.png){width="2.8039107611548557in" height="1.045in"}

When Merge Channels is selected, channels from cues, submasters, groups, and other channel targets will be added to any existing channel targets of that same type.

With Merge Channels not selected, those channels will override any existing channels in the channel targets of the same type.

> In a show file 1, group 1 has channels 1 through 5. In show file 2, group 1 had channels 6 through 10. With Merge Channels and Groups selected for the merge, show file 2\'s group 1 will merge with show file 1\'s group 1. Group 1 will then have channels 1 through 10. If Merge Channels was not selected, group 1 would just have channels 6 through 10.
>
> **Note:** *It is important to remember that if the same channels exist in both show files, the data merging in will override the existing data for those channels.*
>
> **Note:** *Scenic Element and Scenic Element Movable Channels with nested items in an Augment3d model will import without their model items if the Augment3d model is* *not also merged.*

### Printing Show Files

Eos provides you with the ability to save a show file or aspects from a show file to a PDF file for printing. Eos has three locations to save the PDF files including the Show File Archive, the File Server (if connected), or a USB device (if connected). Saving the PDF file to a USB (F:) device, allows you to then print the PDF from a personal computer. Printing directly from Eos is not supported.

> In Setup, you can select the page orientation and paper size for these PDF files, see *PDF Settings (on page 236)*.

To save a PDF of an Eos Family show file, navigate within the browser to Print.

This will open the printing screen in the CIA. From this screen you can choose which aspects of the show file you want to save to PDF. By default all aspects are selected (gray) and will be saved. To withhold any show aspects from printing, simply deselect them in the CIA by touching the respective button. Deselected show aspects will appear in black.

![](media/media/image160.png){width="5.395833333333333in" height="1.4791666666666667in"}

To reselect all show aspects, press the {Select All} button and all buttons will return to gray (selected). To stop the show file from being saved to a PDF and return to the browser, press the {Cancel} button. When you have selected/deselected all of the show aspects you require, press the {Ok} button to create the PDF file.

There are three additional options on the far right side of this display:

-   Tracked Levels - prints all of the moves and tracked values.

-   Color Printout - prints the cue data using the same color indicators as the console\'s displays use. See *Color Indicators (on page 103)*

-   Summary View - prints cues without non-intensity parameter information.

You can also choose to print specific portions of show aspects. To select this information, press the {Advanced} button. The buttons at the center of the CIA will again represent all of the show aspects that you can choose. By default all aspects will be deselected (black).

![](media/media/image161.png){width="5.437846675415573in" height="1.375207786526684in"}

As you select aspects, they will be added to the table in the CIA. For each component in the list, you can specify the desired range by pressing the proper area in the table and entering numbers from the keypad. The columns in the table are:

-   List - The list you are taking data from (such as a cue list).

-   Start - The first in a range of components (such as a range of cues).

-   End - The last in a range of components.

> **Note:** *In the {Advanced} view, you can use the [Thru] key to jump to the End column.*

To deselect all show aspects, press the {Reset} button and all buttons will return to black (deselected).

To return to the main print screen, press the {Return} button. To stop the show file from being saved to a PDF file and return to the browser, press the {Cancel} button. If you are ready to save the file, press the {Ok} button. You will be prompted to name the file.

The PDF will have the show name, date and time it was created, and date and times for when the show file was last saved. It also gives the Eos Family software version information. If multiple aspects were selected to save to the file, there will be hyperlinks at the top of the PDF so you can quickly jump to a section.

> **Note:** *If you have cues selected, cue notes and scenes will display along with* *additional cue information.*

### Saving the Current Show File

To save the current show data, navigate within the browser to: File>Save> and press [Select]. A green \"Success\" message should appear when the file has finished saving. If a red \"Failed\" error appears, attempt to save to a different location, or exit and / or restart Eos as soon as possible.

The Show File Archive is the default storage location for show files when they are saved. The new time stamp located beneath the show file name on the CIA indicates that the show file has been saved.

All previous saves are stored in the Show File Archive with the time stamp following the file name.

#### Show File Indicator

An asterisk (*) will display beside the show file name to indicate when a show file has been modified but not saved.

An asterisk beside the word \"Augment3d\" in parentheses indicates there are unsaved changes in the Augment3d model.

#### Save Show File Warning

If there is unsaved data in the current show file, a save warning will display when you attempt to open a new or existing show file.

![](media/media/image162.png){width="3.086029090113736in" height="1.8433333333333333in"}

The following options will be available:

-   Save - saves the current show file, and opens a new or existing show file.

-   Save as - saves the current show file to a different location or with a different name, and opens a new or existing show file.

-   Continue without Saving - opens the new or existing show file without saving any changes to the current show file. Changes will be lost.

-   Cancel - returns to the current show file without saving changes or opening a different file.

#### Using Quick Save

To save the current show data to the Show File Archive on the internal drive without having to navigate to the browser, hold down [Shift] & [Update].

#### Using Save As

To save an existing Eos Family show file to a different location or with a different name, navigate within the Browser to: File > Save As > and press [Select].

![](media/media/image163.jpeg){width="3.3132392825896764in" height="1.1215616797900263in"}

Eos provides you with three locations to save an Eos Family show file, including the Show File Archive, the File Server (if connected) or a USB device (if connected).

Navigate to the desired storage location and press [Select]. When using "Save As" to save the show file to a specific location, the alphanumeric keypad will display on the CIA. Name the show file and press [Enter]. The show file will be saved in the specified location with the show file name you entered with a time stamp suffix.

By default, the current show file name will be used. Pressing [Label] or [Delete] on the console, or DELETE on an alphanumeric keyboard will remove the default show label when doing a Save As.

> **Note:** *When using Save As to save to a location outside of the Show File Archive, the unsaved show indicators and old show file name will still appear. Save into the Show File Archive to remove these indicators and update the file name displayed.*

#### Show File Formats

The Save and Save As dialogs include a variety of options for saving show files.

> ![](media/media/image164.png){width="4.691161417322834in" height="4.003124453193351in"}

##### ESF3D

This format includes your show data and your Augment3d model, and is only compatible with Eos versions 3.0.0 and higher.

##### ESF2

This format excludes Augment3d model, and is only compatible with Eos versions 2.9.0 and higher.

##### ESF

This is a legacy format for compatibility with Eos versions prior to 2.9.0.

### Importing Show Data

Eos supports the import of show data from a variety of sources.

> **CAUTION:** *The way data is stored and used is often different between different consoles. Imported data may not playback exactly the same between consoles. Not all data (such as effects and macros) may be imported. This varies by product.*

#### USITT ASCII

You can import ASC files, either in the standard USITT ASCII format or from Lightwright. When importing, choose from the following options:

-   Import as Library Fixtures - allows Eos to try to match the fixtures in the file with fixtures in the Eos library.

-   Import as Custom Fixtures - brings the fixtures in as they are in the file. Recommended.

Once a file is chosen, you can choose aspects of the file to import, similar to *Merging Show Files (on page 151)*. By default, the ASCII data will overwrite your current show data. If {Merge Data?} is selected, the ASCII data will be merged into your show instead.

> **Note:** *Eos supports ASCII show file import from a number of other control consoles, including the Congo/Cobalt, Obsession, Expression and Emphasis product lines, as well as the Strand 500 Series. Please note that all show files must be saved in an ASCII format prior to importing them into Eos.*

#### Other Formats

-   Stamp - import show data files output from the Stamp software.

-   CSV - import CSV spreadsheets of show data.

-   Lightwright - import TXT files from the Lightwright software. Lightwright ASC files must be imported using the USITT ASCII option.

-   Pixel Map Media - import additional media for use with pixel maps. See *Pixel Map Media (on page 548)*.

    -   Show Pixel Map Media - import all media needed for the current show file used by backup and client consoles.

    -   All Pixel Map Media - import all media.

-   Gobo Images - supports all standard image formats except SVG for import as custom gobo images. Imported gobo images can be deleted via Browser > Import > Gobo Images > Imported Gobos, choosing the image, and selecting [Delete] [Enter].

After choosing the appropriate option, navigate to the storage location of the file to be imported, choose the file, and press [Select]. Only files that can be imported will display.

#### Import Options and Mapping

When importing a Lightwright file, you will likely need to adjust the data before proceeding.

![](media/media/image165.jpeg){width="5.080823490813648in" height="1.1439577865266841in"}

##### Options

The following options are available:

-   Starting / Ending Channel - defines a specific range of channels to be imported.

-   Overwrite - overwrites the data in the show file when enabled, and merges the data when disabled. Disabled by default.

-   Update fixture types - enables or disables the update of fixture types in the show file. Enabled by default.

-   Only import Augment3d XYZ location - enables import of just Augment3d location data. Disabled by default.

-   Only Import Text/Notes/Labels/Gels - enables import of just the patch database text. Disabled by default.

##### Mapping Fields

You can map Eos patch fields to fields in the source file being imported. Channel and Address are required; any other field can be ignored if desired. Options can be selected again for placement in multiple fields.

> The text fields in the Patch display and database will rename based off of the Lightwright imported fields. See *Renaming Text Fields in Patch (on page 185)*.
>
> **Note:** *Eos does not currently support multiple gels per fixture from Lightwright.*

###### Address Formats

Eos will accept multiple address formats for importing. Examples of those formats are 2/3, 2.3, 2,3, 2-3. Eos will convert all formats to n/n.

##### {Map Devices}

You can also map Eos fixture library devices to devices in the source file.

![](media/media/image166.png){width="5.13340113735783in" height="1.3220833333333333in"}

1.  Select {Map Devices} to open the mapping utility.

2.  Select a device from the Source File column and choose its matching Eos fixture profile. Multiple devices can be selected at a time.

![](media/media/image167.png){width="4.7091447944007in" height="1.1281244531933508in"}

3.  Select {Link Devices}.

![](media/media/image168.png){width="4.7091447944007in" height="1.1281244531933508in"}

4.  Repeat steps 2 and 3 until all devices have been associated with fixture profiles. To unlink a device, select it in the Mapping column and select {Unlink Device}.

5.  When complete, select {Done}, then {OK}.

Device mapping and import fields are saved with the show file.

#### Importing Augment3d Data

File > Import also contains options for importing data for use with Augment3d.

-   Augment3d (From Vectorworks) - legacy import from versions of Vectorworks prior to 2023, Service Pack 2. See *Vectorworks Augment3d Plug-in (on page 702)*.

-   MVR / Capture Model - single-file import of models and fixtures. See *Importing Augment3d Fixtures (on page 523)*.

-   Augment3d Scenic Models - import models. See *Importing Augment3d Objects (on page 541)*.

-   Augment3d Scenic Materials - import materials. See *Importing Materials (on page 506)*.

### Exporting Show Data

Eos show files can be exported to a wide variety of formats.

To export your Eos Family show file in ASCII format, navigate within the Browser to: File > Export > USITT ASCII and press [Select].

You have the option of exporting your show file in ASCII format to the Show File Archive, to a File Server (if connected) or to a USB device.

Navigate to the desired storage location and press [Select]. The alphanumeric keypad will display on the CIA. Name the show file and press [Enter]. The file will be saved in the specified location with the file name you entered with a ".asc" file extension.

You can export Eos Family show files as a .csv format by navigating within the browser to: File> Export> CSV and select the location for the export, the Show File Archive, a File Server (if connected), or to a USB device.

> **Note:** *Not all show data is saved to .csv files. ETC recommends first exporting your show as a .csv file, modifying the file as needed, and then import. See [Exporting a](04_Managing_Show_Files/Exporting_Show_Files.htm) [Show File (on page 1)](04_Managing_Show_Files/Exporting_Show_Files.htm).*

Files can be exported in a Focus Track or Fast Focus Pro format by going to File > Export > Fast Focus Pro or Focus Track and select the location for the export, the Show File Archive, a File Server (if connected), or to a USB device.

Files can be exported in a Moving Light Assistant (MLA) format by going to File > Export > Moving Light Assistant.

This will open the export screen in the CIA. From this screen, you can choose which aspects of the show file you want to export. By default all aspects are selected and will be exported. To withhold any show aspects from exporting, simply deselect them in the CIA by clicking on the respective button. Deselected show aspects will appear in black.

You can also choose to export specific portions of show aspects. To select this information, press the {Advanced} button. In the Advanced screen, all aspects are deselected (black) by default.

To stop the show file from being saved for export, press the {Cancel} button. If you are ready to save, press {Ok}. You will be prompted to name the file. A .csv file will be created.

### Exporting Logs

Logs are useful tools for diagnosing issues. ETC Technical Services may request that you email logs if they are assisting you with an issue. See *Help from ETC Technical Services (on page 3)* for information about contacting Technical Services.

If you are experiencing an issue, press [Displays] & [Record] to put a marker in the log file. This marker along with any other additional information you provide will assist us in reproducing your issue.

> **Note:** *Logs can also be created from the ECU. If created through the ECU, you will have the option to add additional information to the file. See {Save Logs\...} (on page 590).*

Logs can be exported by going to the Logs option in the Browser. Select the location for the export, the Show File Archive, a File Server (if connected), or to a USB device, and press [Select].

An exporting logs message will appear while the log files are being created.

### Deleting Show Files

Eos provides you with the ability to delete show files from the Show File Archive and the File Server from within the Browser.

#### Deleting Show Files

Navigate within the Browser to: File> Open and press [Select]. Navigate to the desired show file and press [Delete]. Press [Enter] to confirm or any other key to abort the deletion process.

##### Deleting Folders

The folder must first be empty.

Navigate within the Browser to: File> Open and press [Select]. Navigate to the desired folder and press [Delete]. Press [Enter] to confirm or any other key to abort the deletion process.

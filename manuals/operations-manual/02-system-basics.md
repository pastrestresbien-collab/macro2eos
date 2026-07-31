# Eos Family User Manual v3.2.0 — Chapitre 02 : System Basics

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 2
## System Basics
  -------------------------------------------------------------------------------------------------------
  ----------------------------------------------- -------------------------------------------------------
  -------------------------------------------------------------------------------------------------------
### About System Basics

This section explains the base level procedures for setting up, navigating, and understanding how to operate your console.

### Power Up the Console

1.  Attach the appropriate power cable to the IEC connector on the rear of the console.

2.  Press the I/O switch (I is "on") next to the IEC connector on the rear of the console to turn power on. This will provide power to all internal electronics.

3.  Press the power button, located on the face panel. The button LED will illuminate blue to indicate the console is running. The console will boot to the launch screen. The system is now ready for use.

> **Note:** *You can go straight to the welcome screen by adjusting a setting in the ECU.* *See Open in \"Shell\" E.C.U. (on page 578) in the ECU appendix.*

### Power Down the Console

1.  After saving your show (see *Saving the Current Show File (on page 155)*), in the browser menu select Power Off Device. A dialogue box opens asking you to confirm.

2.  Confirm this command by pressing {OK} in the dialog box. The console will power down.

> **Note:** *These are persistent storage systems. Therefore if you shut down your system without saving the show file, you will return to the same place in your show when you reboot.*
>
> **Note:** *The console will display an improper shutdown message on the next power* *up if the console was not powered down from the browser menu or welcome screen.*

### Central Information Area (CIA)

The Central Information Area (CIA) is the lower portion of the screen. By default, the CIA consists of three primary areas: the command line, the parameter display, and the browser. Softkeys are also contained within the CIA.

> **Note:** *Gio and Gio @ 5 have a mini encoder display as part of their CIA. See Mini Encoder Display (on page 125).*

*(figure omise)*{width="4.948465660542432in" height="1.6804166666666667in"}

#### CIA Icons

There are three icons located above the CIA.

> *(figure omise)*{width="0.9288888888888889in" height="0.12666666666666668in"}

##### Favorite CIA Display

You can select a favorite default display for the CIA that will show when [Displays] is pressed. The standard default display for the CIA is the Browser.

The favorite display will show a gold star icon at the top of the CIA by the arrow and lock icons. Displays that can be selected as a favorite, but are currently not, will show a gray star at the top of the CIA. Click on the gray star to make that display your favorite. That display will now be the new default display for the CIA. Displays that show up in the CIA but cannot be the default display will not show the star icon.

##### Collapse/ Expand the CIA

It is possible to collapse the CIA from view. To do this, you can click the arrow icon above the CIA. The CIA will collapse from view, exposing a larger viewing area of whatever display is visible above the CIA. The arrow will move to the bottom of the screen.

To expand the CIA into view again, click the arrow at the bottom of the screen. The CIA will reopen.

##### Lock the CIA

You can lock the CIA in place to prevent it from being collapsed or viewed. To lock the CIA, click on the lock above the browser. The lock will "lock". To unlock the CIA, click the sunken lock again.

> **Note:** *While locked, the CIA can still be collapsed or expanded by clicking the arrow icon. You can also use [Displays] & [Page* ▲ *] to expand or [Displays] & [Page* ▼ *] to collapse.*

#### The Command Line

This is the area where commands appear when entered. When in Live, this line is bordered in gold. The command line will display in blue when in Blind.

> **Note:** *Press [Clear] to remove commands from a terminated command line. Use [Shift] & [Clear] to remove commands from a command line that is not terminated.*
>
> See *Syntax Structure (on page 6)* on using the command line.

##### Command Line Prompt

> **Note:** *This feature is only available on Element 2 and Element Classic.*

Directly above the command line, you will see gold text that will prompt you for an action. The prompts will change between different displays and actions, and provide useful information to aid you in programming.

> Command line prompts can be disabled in Setup. See *Device > Displays (on page 233)*.

##### Command Line Search

Command line search allows you to search your recorded targets, effects, and channels. The search window will display the object, it\'s number, and any label you have given it.

Press the Search icon at the end of the command line or use [Shift] & [About] to open the command line search window.

*(figure omise)*{width="5.033112423447069in" height="1.5833333333333333in"}

#### Parameter Display

This display shows the parameters available for patched channels. It is also where you can select which parameters to view in the Live and / or Blind displays, or select parameters for command line control. The parameter display will dynamically change depending on the channel (fixture) selected and its applicable parameters.

> For more information on using the parameter display, see *Using the Parameter Display (on page 247)*.

##### Parameter Category Button Labels

These labels correspond to the six parameter categories; Intensity, Focus, Color, and the three Beam categories (Form, Image, and Shutter).

##### Collapsing the Parameter Display

The parameter display can be collapsed when working with some displays that use the CIA, such as About and Query. A collapse/ expand arrow will display in the last column where this option is available.

When collapsed, only the {All NPs}, {All Speed}, and {Expand Arrow} buttons will be displayed.

#### Labeling

[Label] is used to attach an alphanumeric label to an object such as cues, channels, submasters, etc.

[Label] [Label] when appended to a record target command, clears the current label. This includes show file labels.

##### Editing Labels

The page arrow keys on the console or an external alphanumeric keyboard can be used to move the cursor within a label to aid in editing.

-   [Page Up] - takes the cursor to the beginning of the label

-   [Page Down] - takes the cursor to the end of the label

-   [Page Left] - moves the cursor to the left

-   [Page Right] - moves the cursor to the right

### Browser

The browser is the interface for numerous functions including saving a show, loading a show, opening displays, and many other functions. Press [Displays] to open the browser. See *Using the Browser (on the facing page)*.

> To learn more about saving and loading a show file, see *About Managing Show Files (on* *page 148)*.

#### Using the Browser

To use the browser, you must first draw focus to it by touching anywhere in the browser area of the CIA. If the browser is not visible, pressing [Displays] {Browser} will bring up the browser.

When focus is on the browser, the window border highlights in gold. The paging keys will now control selection in the browser.

*(figure omise)*{width="4.972042869641295in" height="1.9266666666666667in"}

-   Use the page arrow keys to move the selection bar up and down the list. You may also use the level wheel to scroll through the list.

-   When the bar highlights the desired menu, press [Page Right] to open the menu.

-   Continue pressing [Page Right] to open submenus.

-   Scroll to the item you wish to open using [Page Up] or [Page Down], or select the item by clicking or tapping. Press [Enter], [Select] , or double-click to open.

-   If you wish to close a submenu scroll to that item and press [Page Left].

-   Additional presses of [Displays] will minimize or restore the CIA.

-   To draw focus to the browser at any time, press any area within it or press the [Displays] button.

> **Note:** *File folders display with a folder icon beside their name.*
>
> **Note:** *Previous versions of a showfile will be displayed in dark gray text. To see*
>
> *previous versions of a showfile, you must click on the arrow to the left of the showfile name or use [Page* **▶***] .*
>
> **Note:** *The [Select] key can be used to confirm a choice in the browser.*

##### Browser Color Coding

The following color coding for selected items is used in the browser:

-   Save - green

-   Save As - green

-   Open - red

-   Merge - yellow

-   New - red

-   Clear - red

#### Clear Functions

You can access the various clear options from the browser by selecting {Clear} from the main browser menu. The clear functions window will open in the CIA.

*(figure omise)*{width="4.504750656167979in" height="1.546874453193351in"}

From this menu you can select one of the available clear options by clicking on the desired button in the CIA. Eos will ask you for a confirmation before performing the selected clear. For

{Clear Targets}, Eos will allow you to choose which record targets you want to clear.

> **CAUTION:** *Clear functions cannot be undone by using the Undo option.*

*(figure omise)*{width="4.490158573928259in" height="1.625207786526684in"}

From the {Clear Targets} screen you can select which record targets you wish to clear. The buttons at the center of the CIA represent all of the record targets that you can choose to clear. By default all components are selected (gray) and will be cleared. To withhold any targets from being cleared, simply deselect them in the CIA by clicking the respective button. To deselect all of the targets, click the {Deselect All} button.

To reselect all targets, click the {Select All} button and all buttons will return to gray (selected). To stop the process, click the {Cancel} button.

When you have selected or deselected all of the record targets you require, click {OK}.

After clearing, the CIA will return to the browser. If you want to perform additional clear functions, you must select {Clear} from the browser again.

To exit the clear functions screen without clearing, press the [Displays] key at any time or select a clear button and then select {Cancel} from the confirmation screen.

##### Reset System vs Clear Show

Using {Reset System} will open a new show file and reset the Setup options to their defaults. Using {Clear Show} will only open a new show file.

##### Patch 1 to 1 vs Clear Patch

Using {Patch 1 to 1} will clear your patch and set it to a 1-to-1 patch. Using {Clear Patch} will only clear out the patch.

#### Locking the Face Panel

It is possible to lock out the face panel, which prevents any actions from the command line or CIA. To lock out the face panel, press [Shift] & [Escape]. To unlock the face panel, press [Shift] & [Escape] again.

> **Note:** *This will also lock any wings or USB connected peripherals.*

### Softkeys

Some of the features and displays of your Eos family console are accessible from the softkeys, which are located under the Browser. Softkeys are indicated in documentation with bold

{braces}.

The softkeys are context sensitive, therefore they repaint to display softkeys relevant to the display or command you are working with. The white labels on the bottom row indicate the active softkeys. The gray labels in the top row indicate the second page of available softkeys, available by pressing the [More SK] button.

On Element 2, Ion Classic, and Element Classic, these softkeys correspond to buttons [S1] - [S6] and [More SK] on the face panel.

> With a channel on the command line, pressing [More SK] & [Intensity] will post Make Manual on the command line.

#### Changing Softkey Pages

When there are more relative softkeys than the six available buttons, both gray and white softkey labels will be visible. The white labels on the bottom row of the label window indicate the active softkeys. The gray labels in the top row indicate the second page of softkeys.

To access the second page of softkeys, press [More SK]. To access the previous softkeys, press [More SK] again.

### Displays

There are several terms that are useful to know when discussing the displays on your console:

-   Monitor - any physical display or touchscreen device connected to your console. The monitor number will display in the upper left corner of the screen.

-   Workspace - offers independent display control on all of your connected monitors. Every monitor can have up to three workspaces.

-   Frame - a subdivision of a workspace

-   Tab - offers the ability to view multiple displays in one frame.

-   Displays - are the individual views or tools available for use in programming your console. They are viewed in tabs.

Eos has the ability to have one of three different workspaces active on individual monitors, as well as to have up to four frames in use in any workspace. Each frame can hold multiple tabs. Each tab contains one display.

> *(figure omise)*{width="3.955661636045494in" height="2.565in"}

#### Workspaces

Workspaces offer independent display control on all of your connected monitors. Each workspace can be individually configured with any of the layout, display, and control options available in the *Workspace Layout Menu (on page 90)*.

Every monitor can have up to three workspaces, identified by the numbered workspace icons in the upper left corner of any monitor. Select an icon to open that workspace, or use [Tab] & [Page Up] and [Tab] & [Page Down] to cycle through workspaces on all monitors. A

{Workspace} softkey is available by pressing [Displays]. Hold {Workspace} and type the number of a workspace to open.

> **Note:** *From an alphanumeric keyboard, hold down either of the bracket buttons*
>
> *([ or ]) and type in the number of the workspace you wish to view. For example, hold down \ and press 2 to view workspace 2.*

#### Frames

> Each workspace can have up to 16 frames in its layout. The number and arrangement of frames can be edited in the *Workspace Layout Menu (on page 90)*.

#### Tabs

Any frame can have multiple tabs open. Tabs are broken down into two categories: Control and Display. Control tabs are the virtual control options, such as the color picker and the virtual keyboard. Display tabs are the various displays available on the console, such as the playback status display and the park display.

You can open or close tabs using the Display Icons, Control Icons, or typing the [Tab] & the tab number. Pressing [Shift] & [Tab] once will clear all tabs on the selected monitor but tabs in locked frames will remain. Pressing [Shift] and tapping [Tab]twice will clear all tabs on all monitors but tabs in locked frames will remain. Tapping [Tab] a third time will clear all tabs on all monitors including those in locked frames.

Tabs can be reordered by dragging the tab to its new location.

White text in the tab indicates a Display Tab, and magenta text indicates a Control Tab.

All Display and Control Tabs have fixed *Tab Numbers* under which they open (for example, "Live" opens under Tab 1, "Patch" under Tab 12, and "Color Picker" under Tab 27).

These numbers are identified on the Home Screen in each icon. For multiple instances of the same display, the tab number will be followed with a decimal number. Additional tabs will start their numbering with n.2. When you press [Tab], active focus will move numerically through all open tabs on active workspaces.

*(figure omise)*{width="4.790077646544182in" height="0.3325in"}

> **Note:** *Single clicking on a Controls Tab will bring it to the front of the frame but will not move focus to that tab unless the tab's frame already has focus. Double clicking on a Controls Tab will bring it to the front and grab focus. Single clicking on a Display Tab will bring it to the front and grab focus.*

##### Tab Numbers

1.  Live / Blind

2.  Playback Status Display

3.  Magic Sheet

4.  Direct Selects

5.  ML Controls

6.  Effect Status

7.  Virtual Keyboard

8.  Effect Channels

9.  Pixel Maps

10. Pixel Preview

11. Show Control

12. Patch

13. Effects

14. Magic Sheet List

15. Submaster List

16. Cue List

17. Groups

18. Macros

19. Snapshots

20. Park

21. Curves

22. Intensity Palettes

23. Focus Palettes

24. Color Palettes

25. Beam Palettes

26. Presets

27. Color Picker

28. Virtual Faders

29. About

30. Command History

31. Lamp Controls

32. Channels In Use

33. Color Path

```{=html}
<!-- -->
```
35. Fader List Display

36. Fader Configuration

37. sACN Output Viewer

38. Augment3d

39. Custom Direct Select

40. Encoder Mapping

```{=html}
<!-- -->
```
99. Diagnostics

100. User Manual

##### Display Tabs

The following displays can be selected, and they will open in a new tab in the selected frame:

*(figure omise)*{width="4.588299431321085in" height="1.7509372265966754in"}

The following displays can have multiple instances open:

-   Channel (Summary)

-   Channel (Table)

-   Playback Status Display

-   Magic Sheet Display

-   Effect Channels

-   Park

For multiple instances of the same display, the tab number will be followed with a decimal number. Additional tabs will start their numbering with #.2. If you have only one instance, there will be no decimal number.

##### Control Tabs

You can select from the following list of virtual controls, and they will open in a new tab in the selected frame:

*(figure omise)*{width="1.1458694225721784in" height="1.8168744531933507in"}

##### Tab Tools

Every frame has a tab tools menu gear icon in the lower left corner of the frame. Selecting this icon will open the tab tools menu, which provides options for opening and closing tabs in that frame.

> *(figure omise)*{width="1.849215879265092in" height="2.2799989063867017in"}

You can double-click or right-click a tab in focus to also see this menu.

The following is a list of menu options. Not all options are available for every tab.

-   Close Tab - closes the selected tab.

-   Replace Tab - allows you to close the current tab and choose from the Home Screen which display to replace it with. Pressing escape will return you to the previously selected tab.

-   Close All Tabs But This - closes all of the tabs except the selected one.

-   Close All Tabs - closes all of the tabs including the selected one.

-   Reset Columns - resets all of the column widths in the selected tab to Eos defaults. This option will only be available for displays with columns.

-   Lock Frame - prevents any additional tabs from being opened in the selected frame, unless intentionally added with the display picker.

-   Open New Tabs In This Frame - specifies that any new tabs opened will automatically open in the specified frame. Only one frame can have this option selected at a time.

-   Zoom Out and Zoom In - zooms the selected tab.

> **Note:** *If the selected display has a configuration menu, it can be accessed from the* *tab tools menu.*

### Display Control and Navigation

#### Opening and Closing Displays

Displays can be opened and closed in different ways, depending on the display. Many displays are accessible from the browser, while other displays are accessible from the softkeys. The blind displays of record targets (also called "lists") can be quickly accessed by double pressing the record target button (for example, [Cue] [Cue] opens the cue list index).

The Live/Blind display is open as tab 1. The playback status display is always open as tab 2. Neither of these displays can be closed. Multiple instances of Live/Blind and PSD can be opened.

Every display has an assigned tab number. Tab numbering is useful for navigating to views. See

> *Tab Numbers (on page 87)* for a list of displays and their tab numbers.

##### From the Home Screen

> The *Workspace Layout Menu (on the next page)* shows all of the available displays for quick selection. Click on the {+} button by the tabs to access the home screen.

##### From the Browser

Open and navigate the browser as described in *Using the Browser (on page 83)* . You can open record target lists, such as the preset list or cue list index, by navigating to Browser>

Record Target Lists.

**Note:** *Any time you wish to return to the browser, simply press [Displays].*

##### From the Hardkeys

You can open list views of any record target by double-pressing the key for the desired record target (for example, [Cue] [Cue] opens the cue list index).

##### From the Softkeys

To open any displays accessible from the softkeys, press [Displays]. The softkeys will repaint to display:

-   Effect Status

-   Color Picker

-   Patch

-   Setup

-   Browser

-   Magic Sheet

-   Workspace

-   Command History

-   Curves

-   Pixel Maps

-   Show Control

-   Mirror

Any of these softkeys will open the associated display with a single press.

##### Closing Displays

To close any tab display, select the display by using the [Tab] key or other means of navigation. When the desired display is active, press [Escape] to close it.

To close a display in the CIA, press the [Displays] key and the browser will reappear.

To close all displays except for the live/blind display and the playback status display (tabs 1 and 2), press [Shift] & [Tab].

> You can also close tabs by using the Tab Tools. See *Tab Tools (on page 88)*.

#### Workspace Layout Menu

Upon start up or creation of a new show file, any connected monitor that is not already displaying the Live (Tab 1) or Playback Status Displays (Tab 2) will show the Workspace Layout Menu. This screen will also display when a new tab is opened.

> *(figure omise)*{width="3.950716316710411in" height="2.438332239720035in"}

This screen consists of four general areas, each offering different display-related options.

##### Display and Control Icons

Clicking on an icon will open the appropriate display or control in a new tab.

> *Display Tabs Control Tabs **Layout Options***

These tools offer you greater flexibility in the number of tabs you can view in any given

workspace. A workspace can have up to 16 frames. Selecting a layout icon will assign the frame layout identified in the icon. Once a layout is assigned, you can select which displays and controls will be in which frames.

This screen also offers options for opening and closing tabs as well as resizing and resetting the monitor(s).

*(figure omise)*{width="3.9857775590551183in" height="0.467082239720035in"}

###### Resize Frames In This Workspace

Allows you to freely resize and edit the frames in any of the workspaces on the monitor. Select this option to activate the frame configuration grid.

> *(figure omise)*{width="5.82879593175853in" height="3.0858333333333334in"}

The grid includes the following tools:

> *(figure omise)*{width="0.4166666666666667in" height="0.4166666666666667in"}Adds a horizontal split, dividing the associated frame horizontally into upper and lower rows.
>
> *(figure omise)*{width="0.4166666666666667in" height="0.4166666666666667in"}Inserts a vertical split, dividing the associated frame vertically into left and right columns.
>
> *(figure omise)*{width="0.4166666666666667in" height="0.4166666666666667in"}Drag left or right to freely adjust the width of the associated frames. Double-press to reset to the default horizontal size.
>
> *(figure omise)*{width="0.4166666666666667in" height="0.4166666666666667in"}Drag up or down to freely adjust the height of the associated frames. Double-press to reset to the default vertical size.
>
> *(figure omise)*{width="0.4166666666666667in" height="0.4166666666666667in"}Eliminates a split by closing the frame to the right and merging its contents into the frame to the left.
>
> *(figure omise)*{width="0.4166666666666667in" height="0.4166666666666667in"}Eliminates a split by closing the frame below and merging its contents into the frame above.

Frames of the same size can be freely merged without altering the rest of the grid. Smaller frames can be merged with larger frames, but this may alter adjacent splits. A larger frame will absorb any smaller frames it is merged towards.

The grid is limited to a maximum of three splits in either direction, for up to 16 total frames per monitor/workspace.

###### Monitor Mapping

Change monitor arrangement without having to go into the ECU. This function allows you better control of your snapshots. For more information, see *About Snapshots (on page 462)*.

Click on a monitor to display the available numbers, and then click on the number to assign it.

> **Note:** *On-board touchscreens are locked, and their arrangement cannot be changed.*

####### Monitor Mapping

*(figure omise)*{width="2.5843657042869643in" height="1.250832239720035in"}

####### Classic Monitor Mapping

*(figure omise)*{width="1.5405325896762905in" height="1.5721872265966754in"}

###### Close All Tabs In This Workspace

Closes all of the tabs in the active workspace on the active monitor only.

###### Reset This Workspace

Closes all tabs and frames and resets the layout for the active workspace to a single frame displaying theWorkspace Layout Menu, from which you can select new tabs to open.

###### Reset ALL Monitors & Workspaces

Closes all tabs and frames on all monitors, resets all layouts to a single frame, and returns their workspaces to the Workspace Layout Menu, from which you can select new tabs to open.

###### Flip Monitors

This option is only available on Apex consoles, allowing you to temporarily flip the displays upside down if the monitors are angled to face the rear of the console.

##### Single Monitor Snapshots

The snapshots displayed here are single monitor-only snapshots recorded for the visible workspace. For information about snapshots, see *About Snapshots (on page 462)*. These snapshots can be recalled from any selected monitor from the Workspace Layout Menu. You can recall a monitor-only snapshot from the command line by using the syntax [Snapshot] [n] [Enter]. When recalled from the command line, the selected snapshot will only affect the monitor from which it was originally recorded.

To record a monitor-only snapshot, press the {New Snapshot} button on the Display Controls menu screen. [Delete] [Snapshot] [n] [Enter] [Enter] will delete a monitor-only snapshot.

All snapshots can be viewed on the snapshot list display, which can be opened by pressing [Snapshot] [Snapshot] or from the Workspace Layout Menu.

###### Updating a Single Monitor Snapshot

A single monitor snapshot can be updated or deleted by right-clicking on its icon in the Snapshot area of the Workspace Layout Menu.

#### Using Expand With Displays

[Expand] allows you to quickly create additional frames on a monitor.

-   To add frames, press [Expand] & [Page Right] or [Expand] & [Page Down].

-   To collapse frames, press [Expand] & [Page Left] or [Expand] & [Page Up].

This button will expand the Live / Blind tab from one display screen to other screens as well. This doubles the number of channels visible on any tab. Live, Blind, and Playback Status tabs may be expanded.

-   To expand the Live / Blind tab to up to two additional monitors, press [Expand] & [Page Right]. Once you are in an expanded mode, hitting [Expand] contracts the tab by one monitor.

-   To remove all displays from the monitor, press [Expand] & [Page Left].

#### Scrolling Within Displays

By default the page keys will advance / retreat a display by one page per press. However, to activate scroll lock and scroll through displays, you may press [Shift] & [Stage]. SCROLL LOCK will appear above the CIA when in scroll lock mode.

Scroll lock is a toggle state. When scroll lock is first pressed:

-   [Page Up] - scrolls table, spreadsheet and channel views up

-   [Page Down] - scrolls table, spreadsheet and channel views down

-   [Page Left] - scrolls table and spreadsheet views left

-   [Page Right] - scrolls table and spreadsheet views right

#### Selecting Displays

When a display is selected, the screen is highlighted in a gold border and the display name (such as "1. Live Channel") will be in gold as well. When a display is not selected, there is no border and the tab name is gray.

If a display is already open, it can be selected in the following ways:

-   Press [Tab] to change focus between open tabs in numerical order.

-   Press [Tab] & [n], where "n" represents the tab number of the desired tab.

-   Press [Live] or [Blind] to automatically bring Live/ Blind into focus. If there are multiple instances of Live/ Blind, pressing [Shift] & [Live] / [Blind] brings the next Live/ Blind tab into focus.

-   Double press a record target button (such as [Preset] or [Submaster]) to either open the associated display or select it if it is already open.

#### Zooming Displays

You may zoom in and out on displays. To do this, press and hold the [Format] button and scroll the Level Wheel to alter the display. Scrolling the wheel up zooms in. Scrolling the wheel down zooms out. Zooming the channel summary display when it is in 100 channel mode is not supported. You can also zoom by holding down the left mouse button and rolling the scroll wheel on a mouse.

#### Moving Displays

To move the active display from one monitor to another, press and hold the [Tab] key and use the page arrow keys to move the display in the direction of the desired screen. One press of the left or right page keys will move the display to the next screen in that direction. To move it back, press the opposite arrow key.

#### Clickable Displays

Several displays have click supported cells. Clicking on a cell will select and place it on the command line. You can click on multiple cells to select a range of items. Double-clicking a row header will select that row and deselect any other rows. In-Cell editing must be enabled in Setup > Device > Displays. See *{In-Cell Editing} (on page 234)*

*(figure omise)*{width="5.094736439195101in" height="0.6in"}

The following displays have clickable support:

-   Show Control List

-   Cue List

-   Playback Status Display

-   Palette Lists

-   Sub List

-   Preset List

-   Effect List

-   Group List

-   Snapshot List

-   Curve List

-   Partition List

-   Pixel Map List

-   Magic Sheet List

-   Park Address List

-   Patch Display

-   Spreadsheet Display

-   Macro List

#### Quick Access

Quick Access buttons are available at the top of each display, opening tools that appear in a pop-up window that overlays your current display.

*(figure omise)*{width="1.3096872265966755in" height="0.13406167979002626in"}

Select an icon to open a tool, and select again to close the pop-up window.

##### {Popup Magic Sheet}

> Allows quick access to a magic sheet (see *About Magic Sheets (on page 476)*) assigned in Setup > User > Displays > *Popup Magic Sheet (on page 223)*. If a magic sheet has not been assigned, you will be able to choose one from a list of available magic sheets when you first select the icon.

In Setup > *{Popup Nav Lock} (on page 223)* > {Popup Nav Lock}, you can enable or disable the zoom and scroll navigation for pop-up magic sheets. Enabled by default.

##### {Popup ML Controls}

> Allows quick access to the *Moving Light Controls (on page 128)*.

##### {Popup Snapshot Browser}

Allows quick access to your favorite snapshots (see *About Snapshots (on page 462)*). Snapshots can be assigned as favorites when you record them. Select a snapshot to recall it.

##### {Popup Virtual Keyboard}

Allows quick access to a keyboard which mimics the hard keys found on the physical face panel of a console. The alphanumeric keyboard shortcut for that hard key displays in the lower right hard corner.

*(figure omise)*{width="5.0362653105861765in" height="3.285416666666667in"}

The virtual keyboard is also available in a standalone tab via [Tab] [7].

##### {Time}

The time the console is using. Defaults to 12 hour format. To use 24 hour format, make sure

{24 Hour Clock} is checked.

*(figure omise)*{width="2.5104166666666665in" height="2.21875in"}

> Time can also be changed from the shell via *Time Service (SNTP) (on page 589)*.

On ETCnomad, these settings are determined by Windows or macOS, and cannot be edited here.

#### [Time] Key

Holding [About] and pressing [Time] allows you to view discrete timing data behind any channel parameter. [Time] exposes channel or parameter specific timing for any channels in the current cue. The first value is the delay time. If "--" is displayed, there is no delay. The value to the right of the / is the transition time.

You can lock this mode by holding [About] and double tapping [Time]. When in display time mode, "Display Timing" will display in the upper left of the live display. To exit this mode, press [About] again.

#### [Data] Key

Pressing and holding [Data] allows you to view the values behind any referenced or marked data. [Data] exposes the next lower reference level. So if you view a palette reference and press [Data], the absolute data will be displayed instead. If you are viewing a preset, absolute or palette data will be displayed, depending on what is contained in the preset.

You can lock this mode by pressing [Data] twice. When in display reference values mode, "Data Latched" will display in the upper left of the live display. To exit this mode, press [Data] again

#### View Reference Labels

Pressing and holding [About] & [Label] toggles the view to show reference labels or numbers depending on what display setting is being used. See *{Show Ref Labels} (on page 234)*

### Live and Blind Displays

The Live/ Blind display is open as tab 1. This display cannot be closed. Multiple instances of Live/ Blind can be opened.

When in Live, the data displayed represents the data being sent from the console at that moment. In other words, the parameter data that is "live" on stage. When you edit data in live, those changes will become active and visible on stage as soon as the command line is terminated, unless auto playback has been disabled in Setup. See *{Auto Playback} (on page 220)*.

When in Blind, the data displayed represents data from the record target you choose to view (cues, presets, palettes, and so on). When you edit data in Blind, changes will not automatically appear on stage, since the data you are modifying is not live.

While in blind, the background color of the displays will be blue, the title bar will be bright blue, and the word "Blind" will display in the top left corner of each monitor. You can click on "Blind" to go back to live.

> For more information on Live and Blind, see *Live and Blind (on page 10)*

#### Using [Format]

> Live / Blind has multiple formats. When first opened, it opens in its default view, which is the *Table View (on the next page)*. The default view can be set in the *Live and Blind Configuration Menu (on page 104)* . When the default format has been changed, those new settings will be used whenever the display is changed back to that format.

Press [Format] to rotate through any available formats.

Live and Blind share formatting. When you change from one format to another format, you are always working with the same format until you change it. The exception to this is *Spreadsheet (Blind Only) (on page 101)*, which is only available in blind. If you are working in blind spreadsheet, when you return to live you will be working with the table or summary view, based on which one you were last using.

#### Summary View

The summary view displays the largest number of channels of any of the formats. This format is best used to see large numbers of channels' intensity data and / or parameter category data. Individual parameters are not visible in this view.

> FCB icons will appear at the bottom of the channel area for channels that have those parameters patched to them. See *Indicators in the Live / Blind Display (on page 101)*.

*(figure omise)*{width="4.941742125984252in" height="2.244374453193351in"}

To collapse the summary view, hold down the [Data] or [Params] key and press any parameter category key. On Element 2, Ion Classic, and Element Classic, you will need to use [Data].

*(figure omise)*{width="5.056550743657043in" height="1.5275in"}

When the summary view has been collapsed to show only intensity data, you may include focus, color, or beam data in the summary view by holding down [Data] or [Params] and pressing any parameter category key to display all categories again.

#### Table View

Table view is available in Live or Blind. Unlike summary view, table view displays the fixture type associated with channels and details about each channel's category and parameter levels.

> *(figure omise)*{width="5.053806867891513in" height="2.0741666666666667in"}

In Live, table view displays all active channel data being output from Eos. In Blind, it will display all data for a single record target (cue, preset, palette) depending on what is viewed. In table view, focus, color, and beam information can be viewed in either a summary of these three categories or an expanded view to show all parameter data.

To expand a category to show detail, press the [Data] or [Params] key and the associated parameter key. On Element 2, Ion Classic, and Element Classic, you will need to use [Data].

For example, [Data] [Color] will change the color category from a summary view to a detailed one. To collapse a category, press the [Data] or [Params] key and the associated parameter key. You cannot hide a category from view.

When a category has been expanded, to hide or reveal only certain parameters, press and hold [Data] or [Params] and then select the parameter buttons of the appropriate parameters in the CIA. The parameters will be displayed or suppressed depending on the current view.

Notice that when you hold down the [Data] or [Params] button, the buttons of parameters that are currently selected for viewing will be highlighted in the CIA.

In the table, a slight space is provided between fixture types, giving a clear delineation between them. The name of the fixture type is displayed at the top of the section for that fixture.

Channels with only intensity parameters will display the same as in summary view.

#### Preview Mode in Live

A {Preview} softkey is available when in Live Summary.

> **Note:** *{Preview} is not available in Live Table.*

{Preview} allows you to display the intensity values for another cue under the current values in the Live Summary tab. An indicator of what Preview mode you are in will display in the upper left hand corner of the Live Summary display.

*(figure omise)*{width="4.909039807524059in" height="1.1875in"}

In {Preview} mode, the following softkeys are available:

-   {Previous} - previews the last cue run from the selected cue list.

-   {Pending} - previews the pending cue from the selected cue list.

The following examples show other functions that are available in Preview:

-   {Preview}[Next] will allow you to preview the cue higher than the one currently selected. If there is no cue already selected in preview mode, [Next] will behave the same as

> {Pending}.

-   {Preview}[Last] will allow you to preview the cue lower than the one currently selected. If there is no cue already selected in preview mode, [Last] will behave the same as

> {Previous}.

-   {Preview}<Cue>[5] will preview cue 5.

#### Channels in Use

To open the Channels in Use display, click on the {CIU} icon in the home screen or press [Tab] &[3][2].

*(figure omise)*{width="4.9764698162729655in" height="4.40625in"}

A Channels in Use display shows the following information for each channel:

-   Number of cue lists the channel appears in

    -   Not available on Element Classic

-   Number of cues the channel appears in

-   Number of cue moves from zero

-   Number of submasters that channel appears in

-   Maximum channel level

> **Note:** *Right-click on the CIU tab to limit see which channels are used with a specified cue list.*

#### Spreadsheet (Blind Only)

Spreadsheet format is available only in blind mode. It is useful for viewing channel data and trends for multiple cues, submasters, palettes, or presets at one time. Cues/ record targets are displayed on the vertical axis and channel/ parameter data is visible on the horizontal axis.

> **Note:** *Since this is a blind-only view, changes made in this view are immediate and do not require a record or update.*

As with table view, spreadsheet format allows you to choose exactly which parameters you want to view. Parameters can be expanded/ suppressed by holding [Params] or [Data] and pressing the desired parameter buttons in the CIA. Category data is not available in spreadsheet, but you may hide all parameters of a specific category by holding [Params] or [Data] and pressing the desired parameter category button. On Element 2, Ion Classic, and Element Classic, you will need to use [Data].

To toggle between viewing just the intensity information and other parameters, press [Shift] & [Format].

> The label column can be hidden by checking the Suppress Target Labels option in the Live and Blind configuration menu. For more information, see *Live and Blind Configuration Menu (on page 104)*

*(figure omise)*{width="5.042142388451444in" height="0.7353116797900262in"}

#### Indicators in the Live / Blind Display

This section identifies the conventions used to indicate various conditions in Live and Blind. This is the Live / Blind summary view. Please note examples of *Color Indicators (on page 103)*

> and *Text Indicators (on page 103)* in the following graphic:

*(figure omise)*{width="5.908641732283464in" height="1.8115616797900262in"}

> **Note:** *The color and text conventions apply regardless of the format of Live/ Blind being used (see [Using [Format] (on page 97)).*
>
> **Note:** *When manual channels are used, there will be an advisory that says \"Manual Channels\" in red in the upper left hand corner of any Live display.*

Most of the channels in the above image are conventional channels (intensity is the only available parameter).

Several channels in the image are automated fixtures (possessing more parameters than just intensity).

##### Conventionals

*(figure omise)*{width="0.3369378827646544in" height="0.5159372265966754in"}

Conventions display the channel number, intensity, and any additional data below.

##### Automated Fixtures or Multi-parameter Devices

*(figure omise)*{width="0.6539905949256343in" height="0.60125in"}

This view also has additional data fields beneath intensity (F, C, B). This information can be suppressed by pressing [Params] and any parameter category (Focus, Color, or Beam) in the CIA. Doing so will leave only the intensity field and FCB indicators at the bottom of the channel.

On Element 2, Ion Classic, and Element Classic, you will need to use [Data].

##### Multicell Devices

*(figure omise)*{width="1.2042290026246718in" height="0.5502077865266841in"}

Multicell devices display the channel number broken into decimals, based on how many cells the device has. Multicell fixtures can be controlled as an entire fixture, individual cells, or a combination of cells. Parameter data can also be suppressed in the same way as automated fixtures.

*(figure omise)*{width="1.2448512685914261in" height="0.4184372265966754in"}

> You can use flexichannel modes to hide cells or master channels. See *Using Flexichannel (on page 106)*.

When in Flexi Cells Off mode, the master channel will display its own information in the normal font size, and data indicators will be used for the cells. If all of the cells are at the same value, that value will display. If the majority of the cells are at the same value, that value will be displayed with a superscript plus sign. If there is not a majority, just a plus sign will be used.

*(figure omise)*{width="0.608089457567804in" height="0.54625in"}

> **Note:** *A decimal will display at the end of a master channel when flexi cells off is on.*

##### Color Indicators

Eos uses color to indicate information about channel and parameter levels.

*(figure omise)*{width="0.918092738407699in" height="0.34041557305336834in"}

###### Channels

-   Gray number - unpatched channel number.

-   White number - channel number.

-   Bright white number - channel is parked.

-   Gold number - channel is captured.

-   Gold outline - channel is currently selected.

-   Number with no graphic - channel has been deleted.

###### Parameters

-   Bright red - manual data (any data that has been set but not yet stored to an active cue or submaster) on all consoles using the same user ID. When manual data is used, a red advisory\"Manual Channels\" will appear in the upper left hand corner of any Live display.

-   Dark red - manual data from consoles using different user IDs.

-   Blue - intensity value is higher than in the previous cue. Non-intensity parameters (NPs) are in blue when any move instruction has occurred. Unmarked.

-   Green - intensity value is lower than in the previous cue. Also used in reference marking to indicate a channel is marked.

-   Magenta - value is unchanged from the previous cue (tracked).

-   White - value is blocked. See *Block (on page 332)*.

-   White with an underscore - value is auto-blocked. See *Auto-Block (on page 333)*

-   Gray - unowned data. This could be a default value, data not currently being controlled, or a null value (from either {Make Null} or a filter). When null, a gray "n" appears next to the value. See *Make Null (on page 369)*.

-   Yellow - data set from a submaster.

-   Orange - data set from Staging Mode. See *Staging Mode (on page 268)*.

-   Pink - override data from an Augment3d Zone. See *Augment3d Zones (on page 537)*.

> **Note:** *When data is in transition (moving), it will appear in a lighter version of its color. This includes up/down fades for intensity, non-intensity moves from cues, submaster, and timed manual changes.*

##### Text Indicators

Text indicators are used to show additional channel data.

> **Note:** *Color indicators also apply to text indicators. For example, red indicates a manual value that must be stored. See Color Indicators (above)*

-   _ Underlined value (white) indicates a system-applied block (also called an auto-block).

> • + Found in place of parameter data in summary view. Indicates that not all parameters in that category are at the same value. This indicator is found only in the summary view or in table views when the parameters are collapsed into a category view. If a majority of the values are the same, that value will be displayed along with the indicator. If there is no majority, just the indicator will be displayed.

-   ! Indicates an ACN, RDM, or dimmer warning

-   ? Indicates an ACN, RDM, or dimmer error

-   A Indicates the channel or parameter is asserted

    -   Not available on Element Classic

-   B Indicates the channel or parameter is manually blocked. This block must be stored.

-   C Captured channel if in yellow. Color Path if in any other color.

    -   Not available on Element Classic

-   I Channel is controlled by an inhibitive submaster. When displayed in the Block flag, "I" indicates a cue level intensity block.

-   IP, CP, FP, BP Indicates that the value is referenced to a palette (Intensity, Color, Focus, or Beam). This text is followed by a number, indicating which palette is being referenced. This can be substituted with the palette label if the "Show Reference Label" setting is activated (see *{Show Ref Labels} (on page 234)*). Holding down [About] & [Label] will toggle between the palette label and palette number.

-   M Indicates a mark is placed, but manual, and must be stored. Is blue when stored."m" indicates cue is not marking.

    -   Not available on Element Classic

-   MK Indicates the channel is marked for a later cue. The cue number is indicated in the other categories (see "Q" below).

    -   Not available on Element Classic

-   ND Indicates that a channel has been patched as a non-dim fixture type

-   N Indicates the value is null (from either {Make Null} or a filter)

-   P Indicates the channel is parked

-   Ph Indicates the channel is at a preheat level

-   Pr Indicates that the value is referenced to a preset. This text is followed by a number, indicating which preset is being referenced. The preset label may also be shown if this setting is enabled (see *{Show Ref Labels} (on page 234)*). Holding down [About] & [Label] will toggle between the preset label and preset number.

-   Q Found in the non-intensity categories of a marked channel. The "Q" is followed by a number indicating which cue the mark is in preparation for.

    -   Not available on Element Classic

-   t The channel has discrete (parameter/category-specific) timing

-   T The channel has a By Type palette or preset applied.

-   ◆ The channel has a Track SEM Focus Palette applied.

-   S Indicates that a channel is stored to a shielded submaster

-   R Indicates a manual reference override. Manual changes have been made that override a previously stored reference (such as to a palette or preset). Once recorded, the reference will be broken. If updated, the referenced target will be updated as well, unless otherwise instructed.

#### Live and Blind Configuration Menu

The Live/ Blind displays have a configuration menu. The configuration settings are available by selecting the display tab and then double clicking on the tab to open the menu. With the Live/ Blind display selected, you can also select the gear icon, which is located to the left of the tabs, to open the configuration menu.

> **Note:** *Each instance of Live/ Blind may be configured individually.*
>
> *(figure omise)*{width="3.1339173228346455in" height="2.192707786526684in"}

The following options are available:

-   Suppress Target Status Bar - Hides the target status bar from the display. The target status bar displays at the bottom of the Live/ Blind displays.

*(figure omise)*{width="4.592020997375328in" height="0.485in"}

-   MC Line Wrap - When enabled, this option keeps all of the cells together of a multicell fixture when viewing it in Live summary view instead of breaking them up across multiple rows.

-   Suppress Target Labels - Hides the Label column in Blind spreadsheet view.

-   Show Reference Labels - When enabled, referenced record targets (such as presets or palettes) with labels will have their labels displayed rather than their target type and number. This setting will only affect the selected instance of Live/ Blind. There is an option in setup, which determines the default that will be used when tabs are opened. It is modified from there in the configuration menu. See *{Show Ref Labels} (on page 234)*.

**Note:** *[About] & [Label] can be used to temporally toggle between views.*

-   Group Channels By 5 - When enabled, five channels are grouped together with space separating each group of five. This setting is enabled by default.

-   High Contrast - When enabled, high contrast brightens the magenta used to show tracked values. This setting is enabled by default.

-   Disable 100 Channel Display Mode - Disables 100 Channel Display Mode (default).

-   Enable 100 Channel Display Mode - 5x20 - Enables 100 Channel Display Mode, in 5 rows of 20 channels.

-   Enable 100 Channel Display Mode - 4x25 - Enables 100 Channel Display Mode, in 4 rows of 25 channels.

##### Default

You can save your settings as a default state for Live/Blind. The default is identified with parentheses.

-   Reset to Default - Will restore the settings to the default state. Live/ blind tabs will normally default to the settings for Tab 1.0, if no other tab has been assigned as default.

-   Set Current as Default - Allows you to set a Live/ Blind tab other than 1.0 as the default. The default tab will be shown in parentheses , for example (Tab 1).

-   Reset to Eos Default - Restores the settings to Eos defaults.

#### Using Flexichannel

Flexichannel (use of the [Flexi] key) allows you to view only channels meeting a certain criteria in the Live/ Blind display, therefore removing unwanted data from view. Press and hold [Flexi] to see and select from a list of available states and modes in the CIA. You can also press [Flexi] multiple times to cycle through the list of available states.

Flexichannel has several available states which include allowing you to view only:

-   All channels

-   All patched channels

-   Manual channels

-   All show channels (any channels that have data stored in a cue or submaster)

-   Active channels (channels with intensity above zero or a move instruction)

-   In Use Channels (channels with intensities that are above zero or fading to zero, running effects, non-intensity moves, or marking.)

-   Selected channels

-   Channels with discrete timing

There are three Flexichannel modes, which can be used along with the Flexichannel states:

-   Cells off (displays only the master channels for multicell fixtures. Master channels will display with a \".\" after the channel number to indicate that they have cells hidden.)

-   Masters Off (displays only the cells for multicell fixtures)

-   Partitioned (displays only those channels defined in the current partition)

> **Note:** *The multicell fixture views can be used in combination with other flexichannel states.*
>
> **Note:** *You can use [Flexi] & [.] to quickly toggle cells on and off.*

In flexi, selected channels (including the last channel selection) are always included in the view. Gaps in channel numbers are indicated by a vertical line between the channels where a gap in numbering occurs.

To change flexi states in the Live/Blind display, press [Flexi] to cycle through the views listed above. When [Flexi] is held down, the softkeys change to represent all of the available flexi states and modes. You can select the desired flexi view from those keys.

[Next/Last] can be used to select the next or last channel in the current flexi state. [Thru] can be used to view only channels in the current flexi state (except for selected

channels) as long as either the first or last channel in the [Thru] range is included in the current

flexi state. To include channels not in the current flexi state, [Thru] [Thru] can be used.

##### View Channels

You may select specific channels to appear in another flexichannel state called "View Channels". This state does not exist until you select channels to view. After view channels is activated, it will appear in the rotation of flexichannel states when [Flexi] is pressed.

To select channels to view:

1.  Select channels on the command line (do not press [Enter]).

2.  Press and hold [Flexi].

3.  Press {View Chans}. The "View Channels" flexi state will be created and the channels you selected will be visible in it.

The channels you selected will be visible in this flexi state until you select other channels and press {View Chans} again. At any time, you can access the last channels you defined for this state by pressing [Flexi] until this state is visible.

To redefine the selected channels in the state, simply follow the steps above again.

##### Flexichannel with Timing

You may also engage the "channels with timing" flexichannel state by pressing [Flexi] & [Time]. This will display all channels that have discrete timing in the current cue and will remove channels without discrete timing from view.

You may still hold [Time] on Eos or double press [Time] on Eos Ti and Gio to view the discrete time behind any parameter or category.

The display will remain in this state until you disengage it by pressing [Flexi] again.

#### About and Display Toggles

While in Live / Blind, you can use the [About] key to view additional information.

When in an [About] mode, the mode type will display in the upper left hand corner of the Live/ Blind display.

The following is a list of the [About] modes available in the Live/ Blind displays:

> **Note:** *Hold [About] and double tap the modifier key to latch the mode.*

-   [About] & [Live] - displays the DMX levels.

-   [About] & [Data] - hides manual data from the Live / Blind display.

-   [About] & [Address] - displays the DMX address for each parameter.

-   [About] & [Park] - displays the parked levels.

-   [About] & [Part] - displays the cue part number for each parameter.

-   [About] & [Cue] - displays the source target type and number. For cues, the cue list and cue number that contained the last move will display.

-   [About] & [Mark] - displays the mark cue used by the channels.

-   [About] & [Next]/[Last] - displays the next cue with that the channels move in or the last cue with that the channels moved in.

-   [About] & [Label] - displays the reference labels.

-   [About] & [Time] - displays the discrete time.

-   [About] & [Path]/{Color Path} - displays the color paths.

> **Note:** *To page while in these modes, release the modifier key while keeping [About] held down.*
>
> For more information on [About], see [*About [About] (on page 444)*](#about-about).

### Playback Status Display

The playback status display (PSD) allows you to view a range of cues in the current cue list, all cue attributes for those cues, and a view of the fader configurations for 10 pages of 10 faders each (for a total of 100 visible faders.

The PSD opens on Tab 2. This display cannot be closed, but you can have multiple instances of the PSD open on different tabs.

Holding down [Time] while a cue is fading, will display the cue category times counting down in the cue list display area. The default action is to show the total time not the countdown.

To always show the countdown, a {PSD Time Countdown} option is available in PSD configuration menu (see *Playback Status Display Configuration (on page 112)*). When the {PSD Time Countdown} is enabled, the cue category times will countdown as a cue is fading. To see the total time, hold down the [Time] key. {PSD Time Countdown} is "disabled" by default.

Most Eos Family consoles have three available formats for the playback status display:

-   *Expanded Cue List Format (below)*

-   *Split Playback Status Display (on the facing page)*

-   *Fader Display Format (below)*

Expanded cue list format is the default. When the focus is on the playback status display, press [Format] to toggle between the displays.

#### Element 2 and Element Classic PSD

> On Element 2 and Element Classic, the PSD allows you to view a range of cues in the single cue list along with the cue attributes for those cues. Fader information can be viewed in the *Indicators in the Element 2 & Element Classic Fader Status Display*.

#### Expanded Cue List Format

> **Note:** *Not available on Element Classic.*

Pressing [Format] with the playback status display active will access this format. In expanded cue list, the view of the active cue list increases to the full size of the display. The current fader page is visible at the bottom of the screen.

*(figure omise)*{width="5.342540463692038in" height="1.6708333333333334in"}

#### Fader Display Format

> **Note:** *Not available on Element Classic.*

Pressing [Format] with the playback status display active will access this format, which shows a view of the fader configurations for 10 pages of 10 faders each (for a total of 100 visible faders.

Each fader is color coded based on its assigned target type. Grandmasters and inhibitive submasters are in red, additive submasters are yellow, playback faders display in green, and presets and palettes are orange.

> *(figure omise)*{width="3.8601213910761154in" height="2.7247911198600177in"}

#### Split Playback Status Display

> **Note:** *Not available on Element Classic.*

Pressing [Format] with the playback status display active will access this format. With the playback status display split, two different cue lists can be displayed at the same time. This is set in the configuration menu (see *Playback Status Display Configuration (on page 112)*).

> **Note:** *The first time you access the split playback status display, you may need to adjust the splitter bar between the two lists to see the second list.*

*(figure omise)*{width="5.06in" height="2.0029166666666667in"}

#### Paging the Playback Status Display

[Page ▲ ] or [Page ▼ ] will page the display up or down.

> **Note:** *To page the Playback Status Display (PSD) if focus is on a Live/Blind tab, use [Shift] & [Page* ▲ *] or [Shift] & [Page* ▼ *].*
>
> **Note:** *This action will page the PSD that is showing the currently selected cue list. If there is no PSD visible showing that cue list, nothing will be paged.*

#### Indicators in the Playback Status Display

This section identifies the color and text conventions used to indicate various playback conditions.

*(figure omise)*{width="5.048962160979878in" height="2.535in"}

**Note:** *The playback status display will show a red counter for sneak time.*

> **Note:** *If any show control options are currently enabled in Setup > System > Show Control, they will display at the top of the Playback Status Display.*
>
> For more details on information contained in the playback status display, see *Playback Status Display (on page 107)*.

##### Color Indicators

###### Cue List

-   Gold - Any item (cue, list, page) highlighted in gold indicates "current".Outlined in gold indicates "selected".

-   Red - Cue fade is in progress

###### Fader Ribbon / Display

> **Note:** *This option is not available on Element 2 and Element Classic.*

-   Red - Grandmasters and inhibitive submasters

-   Yellow - Additive submasters

-   Green - Playback faders

-   Orange - Presets and palettes

##### Text Indicators

> • + (see cue 6) - Indicates that there is discrete timing within the associated cue. Found in the cue display "Timing" area.

-   * (see cue 4) - Indicates the cue has an allfade command. Found in the cue display "Flags" area.

-   * - Indicates a link to a non-existent cue. Found in the cue display \"Link\" area.

-   D - Indicates a dark move, a cue that has any non-intensity parameters moving on channels whose intensity is at 0. Found in the cue display "Flags" area in the move column.

-   x - Indicates that a mark has been placed, but the mark is broken.

-   A or a (see cues 3 & 4) - Indicates an asserted cue. "A" indicates the entire cue is asserted. "a" indicates a channel or parameter assert only. Found in the cue display "Flags" area.

-   B or b (see cues 2 & 5) - Indicates a blocked cue. "B" indicates the entire cue is blocked. "b" indicates a channel/ parameter block only. Found in the cue display "Flags" area.

-   F1 - F10 - Indicate faders numbered 1 through 10 on the console. Found at the bottom of the fader display.

-   > - Indicates a cue that will not require a Go, as the previous cue has a follow or hang time applied. Found to the left of the cue number.

-   F5 (see in cue 1) - Indicates a follow time associated with the cue (in this case, 9 seconds). Found in the cue display.

-   H3 (see cue 2) - Indicates a hang time associated with the cue (in this case 4 seconds). Found in the cue display.

-   I - Indicates an intensity blocked cue. Found in the cue display "Flags" area.

-   L - Indicates a live move. A "+" is used to show that both types of moves are in that cue.

-   M or m (see cue 1) - Indicates a marked cue. "M" indicates an AutoMark or a reference mark that is used by a subsequent cue. "m" indicates a reference mark that is currently unused by any subsequent cue (see *About Mark (on page 284)*). Found in the "Flags" area.

-   P (see cue 3) - Indicates the cue will preheat. Found in the cue display "Flags" area.

-   R (see cue 8) - Indicates the source cue which refers back to an earlier mark (see

> *Referenced Marks (on page 285)*). Found in the cue display "Flags" area.

-   Number in the FX column (see in cue 1) - Indicates a cue level effects override.

-   M1(see in cue 3) - Indicates a linked macro.

-   Q2/1 (see in cue 6) - Indicates a linked cue.

-   S1 (see in cue 1) - Indicates a linked string. The string will display here.

-   Relay 1/1 (see in cue 8) - Indicates a linked relay.

###### Element Classic Text Indicators

-   * - Indicates a link to a non-existent cue. Found in the cue display \"Link\" area.

> • + (see cue 6) - Indicates that there is discrete timing within the associated cue. Found in the cue display "Timing" area.

-   B or b (see cues 2 & 5) - Indicates a blocked cue. "B" indicates the entire cue is blocked. "b" indicates a channel/parameter block only. Found in the cue display "Flags" area.

-   F5 (see in cue 1) - Indicates a follow time associated with the cue (in this case, 9 seconds). Found in the cue display. Notice the arrow on Cue 2.

-   H3 (see cue 2) - Indicates a hang time associated with the cue (in this case 4 seconds). Found in the cue display. Notice the arrow on Cue 3.

-   M (see cue 7) - Indicates a marked cue. "M" indicates an AutoMark.

-   L - Indicates a live move. A \"D\" in the Move column would indicate a dark move. A "+" is used to show that both types of moves are in that cue.

-   P (see cue 3) - Indicates the cue will preheat. Found in the cue display "Flags" area.

-   Number in the FX column - Indicates a cue level effects override.

-   M1 (see in cue 3) - Indicates a linked macro.

-   S1 (see in cue 1) - Indicates a linked string. The string will display here.

-   Relay 1/1 (see in cue 8) - Indicates a linked relay.

#### Playback Status Display Configuration

Playback Status Display (PSD) has a configuration menu, which is accessed by double clicking or right-clicking on the PSD tab, or by selecting the gear icon, and clicking PSD.

*(figure omise)*{width="3.787332677165354in" height="2.881666666666667in"}

The following options are available in the PSD Configuration Menu:

-   Target Grid - this option is only available when the PSD is split, and is used along with the Lock Status option. Target Grid allows you to select either the top or bottom display. Press [Format] to split the PSD.

-   Lock Status - allows you to lock the PSD to a certain cue list. When the PSD is split, you will use Target Grid to first select top or bottom of the display, and then you can use Lock Status to select the cue list.

> **Note:** *Phantom cue lists will display but cannot be locked to. See Cue List Properties (on page 349) to learn more about phantom cue lists.*

-   Display Cue Parts - displays the individual parts of a part cue. When not enabled, the number of parts for that cue will display as a superscript number beside the cue\'s number.

-   Display Cue Links - displays the *Link / Loop* information.

-   Display Scenes - displays cue *Scenes*

-   Display Follow/ Hang Indicator - displays the Follow/ Hang arrow indicator before the cue number of any cue that will be triggered by a follow or hang.

-   Display PSD Time Countdown - displays the cue category times countdown in the PSD as a cue is fading.

-   Display Master Playback Status - displays the current cue\'s status information.

-   Display Fader Ribbon - displays the fader ribbon, which shows the current fader page under the Master Playback Status. Not available on Element 2, Ion Classic, and Element Classic.

*(figure omise)*{width="5.0977449693788275in" height="0.8286450131233596in"}

-   Display Notes - displays the *Cue Notes* in a horizontal bar at the bottom of the PSD.

-   Display Pending Cue Notes - displays the *Cue Notes* for the pending cue in a horizontal bar at the bottom of the PSD.

-   Break Link to Live/ Blind - When selecting the Live/ Blind display, the PSD will also come into view if it is currently hidden. This option allows you to break the link between the PSD and the Live/ Blind displays so that the PSD will no longer come into view when selecting Live/ Blind.

##### Reorder Columns

Reorder columns allows you choose what data displays in the PSD and what order it displays in. By default, all columns except notes will be displayed. The arrow keys on the right can be used to move columns around. Columns are moved in groups. To select a column header to move, click or tap the name. The check boxes suppress or enable. When an item is enabled to display, a check mark will be in the corresponding box.

##### Default

You can save your settings as a default state for the PSD. The default PSD is identified with parentheses.

-   Reset to Default - returns the settings to the default state that you created.

-   Set Current as Default - uses the current settings to create a default state. The default tab will be shown in parentheses , for example (Tab 2).

-   Reset to Eos Default - returns all settings to the Eos defaults.

### Direct Selects

Direct selects utilize lists of existing show file components (targets) and assign them to a highly-configurable grid of buttons. Direct selects can be used to quickly access those targets, allowing you to easily interact with them, including placing them on the command line.

*(figure omise)*{width="5.839420384951881in" height="1.1241666666666668in"}

To open the direct selects, use the direct selects icon on the *Workspace Layout Menu (on page 90)* or [Tab] [4]. Direct selects for specific targets can then be opened using the corresponding button.

#### Using Direct Selects

Direct selects can be used to quickly access show file targets, allowing you to easily interact with them in a variety of ways.

> **Note:** *Many buttons referenced in this section can be configured to appear or disappear from the direct select tab. For more information, see Configuring Direct Selects (on page 116).*

When you first open the direct selects tab, you will be presented with one or more banks that can be used to control specified targets.

*(figure omise)*{width="5.273307086614174in" height="0.5027077865266841in"}

Targets are specific elements of your show file that can be assigned to direct select buttons. With the exception of custom direct selects, only one target type can open in a direct select bank.

Select a target type to open direct select buttons for that target. You can then use the direct select buttons to select and control the chosen target.

###### Custom Direct Selects

Custom direct selects allow you to assign multiple target types to the same grid layout. If

{Custom} is selected on the direct selects tab, a popup will appear showing all available custom direct select lists in your show file.

*(figure omise)*{width="5.166970691163605in" height="2.2262489063867017in"}

Once a custom direct select list is open, selecting an empty button will display a popup of the *Target Selection Menu (2) (on page 118)*, allowing you to quickly assign a target or range of targets.

> **Note:** *While applying a target range will configure multiple buttons, multiple-button-selection is only available via the custom direct selects editor in Tab 39.*
>
> For more information, see *Custom Direct Selects (on page 118)*.

##### Navigating Direct Selects

To change the direct select type displayed in a bank, press the current target name, and choose the desired direct select target to display.

If there are more items in a direct select bank than can be viewed at once, you may view subsequent pages by using the {Page Up} and {Page Down} arrows. The {Jump To\...} button, when enabled via the direct selects configuration menu, can be used to jump to a specific direct select. For more information, see *Configuring Direct Selects (on page 116)*.

##### Direct Selects & the Command Line

With the exception of channels and groups, all targets selected via direct selects will post a terminated command on the command line. To post an unterminated command, hold [Shift] as you press the direct select. This allows multiple commands to be selected and executed at once, and an optional sneak time to be entered.

Channels and groups selected via direct selects will post an unterminated command by default.

###### Recording to Targets Using Direct Selects

You may store a command line selection directly to a target\'s direct selects by pressing [Record] and the desired direct select key.

You can record decimal inserts to a direct select, which will add additional buttons to your direct select grid. All recorded targets will appear in numerical order in a direct select grid, including those with decimals in their number.

> Open a color palettes direct select bank with color palette 1 on button 1 and color palette 2 on button 2. Record color palette 1.5. A direct select button will be inserted between buttons 1 and 2.
>
> Use the {Increment} setting in the *Configuring Direct Selects (on the next page)* to set the granularity for displaying empty target buttons. Stored decimal targets will always be displayed, regardless of increment setting.

###### Direct Select Button Indication

The appearance of direct select buttons will change depending on what is selected via the command line.

If a target is on the command line, the corresponding direct select tile will be outlined in gold.

*(figure omise)*{width="3.2572790901137356in" height="1.3049989063867016in"}

> Open a direct select bank displaying groups. Type [Group] [1] [Enter]. The group 1 direct select button will be outlined in gold.

If channels are selected via the command line, and any direct select targets contain all of those channels, the direct select button(s) will be highlighted.

*(figure omise)*{width="3.2572790901137356in" height="1.3049989063867016in"}

> Record preset 1, containing channels 1-10. Open a direct select bank displaying presets. Type [1] [Thru] [10] [Enter]. The preset 1 direct select button will be highlighted gray.

If channels are selected via the command line, and any direct select targets contain some but not all of those channels, the direct select button(s) will be highlighted with a gradient.

*(figure omise)*{width="3.2572790901137356in" height="1.305in"}

> Record beam palette 5, containing channels 10-20. Open a direct select bank displaying beam palettes. Type [1] [Thru] [20] [Enter]. The beam palette 5 direct select button will be highlighted with a gradient.

#### Configuring Direct Selects

The appearance of direct selects onscreen is highly customizable.

##### Direct Selects Configuration Menu

The primary way to configure direct selects is via the direct selects configuration menu. To access the menu, right-click or tap on the direct selects tab, or use the gear icon on the left of the tab bar.

*(figure omise)*{width="3.1938976377952755in" height="2.9054166666666665in"}

The following options are available:

-   # of Banks - sets the number of direct select banks that will display in the tab.

If multiple banks are selected, a drop-down menu will appear, allowing you to apply all of the additional configuration options below to a specific bank, or all open banks. Asterisks next to any of the additional configuration options indicate functions that are only enabled for specific banks.

###### Layout

This section allows you to configure the layout of the direct selects grid.

> **Note:** *If the frame or window is resized, the direct selects grid layout will responsively change size to fit onscreen.*

-   {25} / {50} / {100} / {200} - quick-select options to easily set the grid size.

-   Rows - allows you to select the number of rows in the banks.

-   Columns - allows you to select the number of columns in the banks.

###### Control Buttons

This section allows you to configure which optional control buttons will appear alongside the direct selects grid. The checkboxes on the left toggle whether a button appears in the grid.

The buttons that appear on the right allow you to use that function directly from the configuration menu without having to add the button alongside the direct selects grid.

-   Control Button Position - allows you to set the control buttons to display on the left or right side of the banks.

-   Use Record - displays the {Record} button, which posts Record to the command line.

-   Use Select - displays the {Select} button, which will display the selected direct select type. Pressing it will allow you to select a different direct select type.

-   Use Flexi - displays the {Flexi} button. See *Using Flexi Mode (below)*

-   Use Expand - displays the {Expand} button, which will temporarily cover all other banks with the expanded target.

-   Use Arrows - displays the page up and down arrows.

-   Use Millennium Buttons - displays the century and millennium buttons. These buttons allow you to jump to pages in the hundreds and thousands.

-   Use Jump To\... - displays the {Jump To} button, allowing you to jump to specific target numbers.

-   Page - allows you to jump to a specific page of direct selects.

###### Other

-   Increment - all recorded targets will display in numerical order, including those containing decimals. Increment sets the target granularity of the grid, allowing blank decimal targets to be shown between whole-number targets.

-   Icon Position - configures the location of the icon on the direct select tile. Centered will apply the icon to the entire tile. See *Icons (on page 120)* about assigning icons.

-   Icon Opacity - configures the opacity of the icon from 0-100. 75 is the default. Lower opacities may allow the direct select label to be more visible in front of the icon.

-   Skip Empty Flexi Space - removes the empty space between a range of nonsequential target buttons when in flexi mode.

-   Use Color Swatch - displays a triangular color swatch in the lower left corner of a direct select. Color swatches are available for color palettes, macros, and snapshots only.

-   Maximize Button Size - sets the size of the direct select buttons to fill the available space.

-   {Reset to Default} - will restore the settings to the default state. If no default state has been set, the Eos default settings will be used.

-   {Set Current as Default} - allows you to set the current settings to be used as a default state when opening additional direct select tabs.

-   {Reset to Eos Default} - restores the settings to Eos defaults.

-   {Reset Current Bank} - restores the settings of the currently-selected bank only.

##### Using Flexi Mode

Direct selects can be placed into a flexi mode. {Use Flexi} needs to be enabled in the direct selects configuration menu. Once enabled, the {Flexi} button will display alongside the direct selects grid. This mode removes most of the empty buttons from the grid, but leaves a single

blank tile between ranges. {Skip Empty Flexi Space} will remove this blank tile. When in flexi mode, the {Flexi} button will be outlined in gold.

#### Custom Direct Selects

Whereas direct selects display lists of specific target types, custom direct selects allow you to create a list with individual targets, regardless of type. The custom direct selects editor allows you to choose the targets used in these lists, and apply them to a configurable grid.

To open the custom direct selects editor, select the custom direct selects icon on the *Workspace Layout Menu (on page 90)*, or use [Tab] [3] [9]. You can also choose {Custom} on the direct selects tab, and then selecting {Open Custom DS Editor}.

*(figure omise)*{width="5.059909230096238in" height="3.5862489063867016in"}

The editor is divided into a preview of your custom direct selects grid, a target selection menu for configuring buttons, and an index of all custom direct select lists in your show file.

Custom direct select lists can be any number between 0.001 and 9999.999.

##### Preview (1)

This section displays the custom direct select list, laid out on a customizable grid for you to preview layouts. The options at the top allow you to adjust the number or rows and / or columns in your custom direct select grid, or choose from preset grid layouts.

##### Target Selection Menu (2)

This section allows you to configure which direct select targets are assigned to your custom direct select buttons. All buttons default to empty.

##### Custom Direct Selects (3)

This section displays an index of all the custom direct select lists in your show file. These lists can be assigned a label, as well as an icon.

> **Note:** *Custom direct selects created in Eos software prior to v3.1.0 and stored in snapshots will be automatically converted to a custom direct select list, labeled with the relevant snapshot number.*

##### Configuring Custom Direct Selects

To assign targets to your custom direct select list, select one or more buttons in the grid. You can select multiple buttons at once by selecting them sequentially, or dragging to lasso a marquee around them.

> **Note:** *The order in which the buttons are selected will determine the order that targets are applied to those buttons.*

Once the desired buttons are selected, choose a direct select target to assign to those buttons. You must define a starting number for the selected target. When a single button is selected, defining an ending number will assign that range of targets to the grid, starting with the selected button.

> Selecting Button 1 and the Channels target with a range starting at 10 and ending at 14 will assign Channels 10-14 to Buttons 1-5.

When multiple buttons are selected, the same number of targets as buttons selected will be assigned. You can define an offset instead of an end to distribute targets evenly across the selected buttons.

> Selecting Buttons 11-15 and the Presets target starting at 1 with offset 2 will assign Presets 1, 3, 5, 7, and 9 to Buttons 11-15.

Select {Apply} to assign the specified target(s) to the specified button(s). The specified target

\(s\) can also be copied to additional buttons in any custom direct select list using {Copy} and

{Paste}. Once {Copy} is selected, the targets to be copied will be noted at the bottom of the target selection menu.

Checking the \"Include Non-Existant Whole Number Targets\" box allows you to map buttons for targets that do not exist yet. If the box is left unchecked, only existing targets will be mapped. This box is checked by default.

###### Buttons on Custom Direct Selects

This target, unique to custom direct selects, allows you to place console buttons on your custom direct select grid. The following options are available:

-   Console Button - duplicates the functionality of any console hard key or soft key

-   Jump To - a button allowing you to jump to a defineable spot in any custom direct select list

    -   Type [#] to jump within the same list, or [#] [/] [#] to jump to a specific custom direct select list and button number

-   Next Page/Prev Page - a button allowing you to jump to the next or previous page in your current custom direct select list

###### Assigning Icons

Icons can be assigned via the softkey {Icon}, or by clicking on the Icon field in the target table. This opens the icon library.

Any existing icons in your library will appear first, along with stock icons. You can also access additional default icons using the additional tabs below the icon library. Common fixture icons are available in the adjacent tab to the right. Select an icon to assign it to the specified target. To close the icon library, clear the command line, or select Close.

> For more information, see *Icons (below)*.

##### Clearing Custom Direct Selects

You can clear a custom direct select by selecting the button(s) and pressing {Delete}. You can also hold down [Escape] and press the direct select that you want to clear.

To delete a custom direct select list, use [Delete] [#] [Enter] [Enter], where [#] is the list number.

#### Icons

Icons are images that can be applied in various places throughout Eos to customize your workspace.

*(figure omise)*{width="5.880543525809274in" height="2.2641655730533685in"}

Any targets that can be applied to a direct select (other than channels, scenes, and buttons) can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Custom Direct Selects (on*

> *page 118)* and *Configuring Direct Selects (on page 116)*.
>
> Icons can also be added and configured as magic sheet objects. See *Magic Sheet Icon Library (on page 487)*.

##### Importing Icons

Select the Import button to add new icons to the library. Use the pop-up menu to navigate to the appropriate folder, select one or more images, and select OK. SHIFT or CTRL can be held to select multiple consecutive or nonconsecutive images.

Accepted image formats for import are .bmp, .gif, .ico, .jpg, .pbm, .pgm, .png, .ppm, .svg,

.svgz, .tga, .tiff, .xbm, and .xpm. The maximum image size is 1920 x 1920.

##### Organizing Icons

*(figure omise)*{width="5.880543525809274in" height="2.2641655730533685in"}

Select the Organize button to enable the following additional button options:

-   Add Folder - adds a folder to the current icon library directory.

-   Delete Unused - deletes any unused icon images across all icon library folders. You can optionally delete subfolders and empty folders at the same time using the checkboxes.

Icons can be dragged in and out of folders. Selecting an image or folder in organize mode will enable the following options:

-   Replace - images only. Replaces all show file instances of the selected image with a new image of your choice.

-   Rename - changes the name of the selected image or folder.

-   Delete - after confirmation, removes the selected image or folder from the icon library. Deleting a folder will also delete all images inside it.

###### SVGs

Any SVG (Scalable Vector Graphic) file used as the icon for multiple targets can be given a unique color per instance. The files must be tagged using the same guidelines for *Importing* *Fixture Symbols (on page 486)*.

#### Target Keys

> **Note:** *Target keys are only available on Apex consoles.*

Target keys are physical buttons with a customizable surface that can be assigned to control any target via direct selects.

To edit the direct selects assigned to your target keys, hold [Displays]. Configuration button overlays will appear on each bank of keys. Use {Edit #} to open the target editor for that bank. The arrows can also be used to change the page of keys displayed on the bank.

> *(figure omise)*{width="5.842458442694663in" height="1.885in"}

From there, assign targets to the bank using the direct select controls in the editor. Once a starting target is selected for the bank, targets will be assigned consecutively from there.

### Encoders

> The encoders are one of the ways to control the non-intensity parameters (NPs) of multiple parameter devices. For more information on using the encoders, see *Setting Non-Intensity Parameters with the Encoders (on page 248)* .

On Eos Ti, the top four encoders are identified by the encoder touchscreen, just to the left of the encoders. The bottom two encoders are always in control of pan and tilt respectively from left to right.

On Gio, Gio @ 5, and Ion Xe, the four encoders are identified in two ways, by the encoder controls display and the mini encoder status display.

> On Element 2 and Element Classic, you can access encoder control by using the ML controls display. See *Moving Light Controls (on page 128)*.
>
> On Ion Classic, the four encoders are identified by the encoder LCD, just beneath the encoders. For more information on using the encoders, see *Setting Non-Intensity Parameters* *with the Encoders (on page 248)*

#### Eos Ti Encoder Display

The encoder display area will show the name of the parameter it controls, display stepped limits (if any) and also a {Home} button which allows you to set that parameter to its default position. You can also home any parameter.

> *(figure omise)*{width="2.1542027559055117in" height="3.5833333333333335in"}

Some buttons that may be available on the touchscreen are:

-   Min

-   Max

-   Next

-   Last

-   Home

-   Mode

-   XYZ Format Enable/Disable

Buttons like {Next} and {Last} are used to step through ranges (such as colors in a color scroller) one step at a time. {Min} and {Max} allow you to send a parameter to its minimum or maximum limit with one press.

Modes allows you to switch between modes of a parameter (if any exist); for example, a rotating gobo wheel. If additional modes are available, their softkeys will display near the top of the encoder display.

Encoders can be switched from course mode into fine by holding down [Shift] while using an encoder will put it in fine mode for as long as [Shift] is held down. Once [Shift] is released, the encoder will return to course mode. See *Face Panel (on page 230)* for encoder options.

Press {Expand} to see all of the information about any device with a frame table. Press again to collapse to the normal view. You may make selections from the Expand screen. The colors/images in the device are established in patch (see *Using the Scroller/Wheel Picker and Editor (on page 175)*).

{XYZ Format Enable / Disable} toggles between storing position data in pan / tilt format, and XYZ format for use with Augment3d.

To the left of the encoder touchscreen are six hardkeys (five on Eos) that are for encoder control. From top to bottom, these encoder paging keys control intensity, focus, color, shutter, image, and form. Pressing any of these will change the parameters controlled by the encoders. To view other available encoder pages, simply press the encoder paging keys to advance the pages.

[Encoder Paging Keys] & [#] will take you directly to a page. [Flexi] & [Encoder Paging Keys] will toggle the flexi encoder states.

To post a parameter category to the command line, use the parameter category buttons.

To post beam to the command line, double press the shutter, image, or form parameter category buttons.

Some fixtures have more parameters than can be displayed on one encoder page. The number of. pages for each category is displayed at the top of the encoder touchscreen. To view the other pages, simply press the encoder paging button to advance the pages or hold the button and press a number key to go directly to the page you want to access.

#### Encoder Controls Display

The encoder controls display is available on Gio, Gio @ 5, and Ion Xe consoles. Press the [Encoder Display] hardkey to open the encoder controls display.

*(figure omise)*{width="5.046874453193351in" height="1.345832239720035in"}

Directly under the middle two encoders are six hardkeys for encoder control. From left to right, these encoder paging keys control intensity, focus, color, shutter, image, and form. Pressing any of these will change the parameters controlled by the encoders. To view other available encoder pages, press the encoder paging keys to advance the pages.

On Ion Classic, the encoder LCD displays the active parameter category loaded on the encoders, as selected by the page buttons. To see additional encoder information, open the Encoder Display by using CTRL + ALT + \ on an alphanumeric keyboard. ALT + , can be used to change encoder pages.

[Encoder Paging Keys] & [#] will take you directly to a page. [Flexi] & [Encoder Paging Keys] will toggle the flexi encoder states. See *Flexi Encoders (on page 126)*.

To post a parameter category to the command line, use the parameter category buttons located in the CIA.

> **Note:** *To post beam to the command line, double press the shutter, image, or form parameter category buttons.*

Each encoder's area will display the name of the parameter it controls, display stepped limits (if any) and also a {Home} button which allows you to set that parameter to its default position.

The encoder controls display allows you to cycle through parameter steps (if available). You can also home any parameter. Some buttons that may be available are:

-   Min

-   Max

-   Next

-   Last

-   Mode

-   Expand

-   XYZ Format Enable / Disable

Buttons like {Next} and {Last} are used to step through ranges (such as colors in a color scroller) one step at a time. {Min} and {Max} allow you to send a parameter to its minimum or maximum limit with one press.

Modes allows you to switch between modes of a parameter (if any exist); for example, a rotating gobo wheel. If additional modes are available, their softkeys will display at the top of the encoder controls display.

Encoders can be switched from course mode into fine by holding down [Shift] while using an encoder will put it in fine mode for as long as [Shift] is held down. Once [Shift] is released, the encoder will return to course mode.

Press {Expand} to see all of the information about any device with a frame table. Press again to collapse to the normal view. You may make selections from the Expand screen. The colors/images in the device are established in patch (see *Using the Scroller/Wheel Picker and Editor (on page 175)*).

{XYZ Format Enable / Disable} toggles between storing position data in pan / tilt format, and XYZ format for use with Augment3d.

#### Mini Encoder Display

On Gio, Gio @ 5, Ion Xe, or ETCnomad using a Programming Wing, information on what the encoders are currently controlling can always be found in the mini encoder status display, even when the *Encoder Controls Display (on the previous page)* is closed. This display is found above the softkeys in the CIA.

Use the Parameter Category hardkeys to choose which parameters are currently available on the encoders.

*(figure omise)*{width="5.029411636045494in" height="0.35624890638670165in"}

Some fixtures have more parameters than can be displayed on one encoder page. The number of. pages for each category is displayed at the bottom of the Parameter Category softkey. To view the other pages, simply press the button to advance the pages or hold the button and press a number key to go directly to the page you want to access.

#### Encoder Navigation

Use the encoder page buttons (located to the left of the encoder LCD) to choose which parameters are currently available on the encoders. There are five usable buttons: [Color], [Custom], [Shutter], [Image], and [Form]. Ion Classic consoles have the additional [Focus] key. Pressing any of these will change the parameters controlled.

Some fixtures have more parameters than can be displayed on one encoder page. The number of pages for each category is displayed on the encoder touchscreen. To view the other pages, simply press the [Color], [Custom], [Shutter], [Image], or [Form] button to advance the pages or press the button with a number key to go directly to the page you want to access.

Encoders can be switched from course mode into fine by holding down [Shift] while using an encoder will put it in fine mode for as long as [Shift] is held down. Once [Shift] is released, the encoder will return to course mode.

#### Encoders in Blind

The encoders and the level wheel are disabled by default when in the blind display. Pressing an [Encoder Page Keys], for example [Color], will enable the encoders and level wheel. When the encoders are disabled, trackball functionality for pan and tilt will also be disabled.

#### Flexi Encoders

In Flexi mode, any empty locations for parameters not applicable for selected channels will be suppressed. By default, the encoder display will be in Flexi mode.

Holding down [Flexi] and an [Encoder Page Keys], for example [Image], can be used to exit or enter Flexi mode.

#### Locking the Encoders

It is possible to lock out the encoders. To lock out the encoders, press [Escape] & [Encoder Page Keys]. To unlock, press any of the [Encoder Page Keys].

#### Custom Encoder Maps

Custom encoder maps allow you to create and store unique parameter layouts for your fixtures. A custom map can be assigned as a console-wide default, or applied more selectively to specific fixtures, groups of channels, or console users.

> To open the custom encoder map editor, select the encoder maps icon on the *Workspace Layout Menu (on page 90)* or use [Tab] [4] [0].

*(figure omise)*{width="5.037023184601924in" height="2.719374453193351in"}

Custom mode must be enabled to use custom encoder maps, by selecting {Custom}. When custom mode is off, Eos will use the default parameter mapping.

> Custom encoder mode, map assignments, and current positions can be stored in snapshots and recalled separately or together. See *Recording Snapshots (on page 462)*.

##### Creating Custom Maps

Create a map by entering the map number and pressing [Enter], and select a parameter category (Intensity, Focus, etc) to customize.

Add parameters to the category by selecting an open encoder slot, and choosing a parameter from the list to assign to it. You can also search for specific parameters.

To edit parameters that have already been assigned, select the parameter again and choose from the following options:

-   Clear - removes the parameter assignment from the encoder slot, leaving it blank.

-   Delete - removes the parameter assignment from the encoder slot, moving all subsequent parameters to the left

-   Insert Before - inserts a blank slot to the left of the selected parameter

-   Insert After - inserts a blank slot to the right of the selected parameter

-   Change Parameter - replaces the assigned parameter in that slot

Each parameter category can be given up to 25 pages of custom encoder layouts. If a parameter category is not assigned any custom encoder layouts, the default Eos parameter mapping for that category will be used instead.

####### Defaults

These parameter slots assign default parameters to each encoder in the specified parameter category. Unless a specific parameter has been chosen for an encoder on a page, the assigned defaults will track across encoder pages, indicated with the standard Eos tracking colors.If the defaults are left unassigned, parameters must be assigned on each encoder page individually.

####### Widgets

Additional fixture control options can be assigned in the Widget column. As with parameters, widgets can be assigned a default that tracks across all pages in a parameter category, or assigned on a page-by-page basis.

###### Softkey Options

The following softkey options are available in the custom encoder maps editor:

-   {Filter To Users} - allows you to create a user-specific map

-   {Map To Fixture} - allows you to create a fixture-specific map

-   {Create From Fixture} - creates a map using the parameter layout of a specified fixture profile

###### Copying Maps

Maps may be copied using [Copy To]. This may be useful if you want to use the same map layout for multiple custom maps.

##### Custom Map Types

###### Default Map

A single custom encoder map can be assigned as the default encoder map for all devices in the show file. When custom mode is enabled, this map will be used for all patched devices.

Assigning a map as the default can be done at the top of the custom encoder map editor, or in Setup > User > Manual Control.

> **Note:** *Default maps are specific to the current user number.*

###### Single-Fixture Maps

Custom encoder maps can be created for a specific device type, and will only appear when one or more devices of that type are selected.

Assign a map to a device profile via {Map To Fixture}, or by selecting in the Map To Fixture column. When fixtures with this profile are selected, the custom encoder map will populate.

> *(figure omise)*{width="2.496496062992126in" height="1.1903116797900262in"}

If multiple fixture types are selected at once, encoder maps will stack in the encoder display, allowing you to select them individually. This includes any default maps for selected fixtures without custom maps assigned to them.

###### Multi-Fixture Maps

Maps can also be assigned to more than one device type, which can be useful if two or more separate devices are often used together. Simply assign additional device profiles when creating a fixture-specific map. Now when one or more fixture of any included type is selected, Eos will prioritize the multi-fixture map over any individual fixture maps or defaults.

> **Note:** *At least on device type included in the multi-fixture map must be selected for the map to appear.*

###### User-Specific Maps

Custom encoder maps can also be specified to the user level. When creating or editing a map, assign it to a specific user number via {Filter To Users}, or by selecting in the Filter To Users column. As with device profiles, multiple user numbers can be selected. Once specified, only matching users will have access to that encoder map.

### Moving Light Controls

A display tool for controlling the non-intensity parameters (NPs) of multiple parameter devices is the ML Controls. The ML Controls are on Tab 5.

On Element 2 and Element Classic, the display can be opened in the CIA by pressing the [ML Controls] button.

> **Note:** *A pop-up window version of the ML Controls can be opened for quick access of these controls. See {Popup ML Controls} (on page 96)*

You will need to have a multi-parameter device selected to properly view this display. The display will change based on the device selected. If you have a device that only has intensity and color parameters, the ML Control display will only show intensity and color parameters.

> **Note:** *Controls available in this display will change based on the fixture selected.*

When there is room, multiple rows of parameters will display, and you can scroll the display vertically.

There are category shortcut keys on the left side of the ML Controls display. Press a key to quickly access those controls.

> *(figure omise)*{width="5.06875656167979in" height="1.2904155730533684in"}

1.  Category button (Clicking this button will put the category on the command line.)

2.  Parameter button (Clicking the button will put the parameter on the command line.)

3.  Home button allows you to home a specific parameter or attribute of a parameter.

4.  Parameter attributes

5.  Selects the color picker.

6.  Collapses or expands categories.

7.  Gives pan and tilt functionality to a mouse or trackball.

8.  Virtual encoder (Click and hold close to the center line for slow movement, further away for faster movement.)

9.  Opens the gel picker.

### Fader Configuration

The fader configuration display is found on Tab 36 .The *Fader List (on page 132)*, which shows all of the faders and their assignments, can be found in Tab 35.

At the top of the fader configuration display, you can select the fader page, which has 100 pages of 10 faders each page.

> If your console has a main fader pair, you can configure it at the top of the display. See *Main Fader Configuration (on page 133)*.

#### Display

The fader configuration display shows a virtual mockup of each fader and its buttons. The various parts of the virtual fader can be clicked or tapped to open configuration options.

Each fader is color coded based on its assigned target type. Grandmasters and inhibitive submasters are in red, additive submasters are yellow, playback faders display in green, and presets, palettes, global effects, and manual time masters are orange.

Playback faders cannot be assigned on Element 2 and Element Classic consoles.

##### Fader Configuration

*(figure omise)*{width="4.952483595800525in" height="1.6611450131233596in"}

##### Element Fader Configuration

*(figure omise)*{width="2.0067246281714786in" height="1.0964577865266842in"}

##### Fader Display Options

Use the gear icon at the left of the tab bar or right-click on Tab 36 to choose a fader display option. Select Faders to manually hide Apex endless fader wheels from the virtual fader, or Apex Faders to make them visible.

#### Fader Configuration Window

Click on the fader header to open the fader configuration window.

*(figure omise)*{width="1.8928915135608049in" height="1.4170822397200349in"}

##### Target

This setting allows you to map a cue list, submaster, intensity, focus, color, or beam palette, preset, global effect fader, manual time master, or grandmaster to a fader.

##### ID

This sets the number of the target assigned to the fader, such as Preset 2 or Submaster 5. For a list of available Target IDs, click or press the {\...} button beside ID.

> **Note:** *Content can also be loaded to faders from Live, using the command line and load.*

##### Discrete Instance

> **Note:** *Not available on Element Classic.*

This setting defaults to Yes and applies to cue lists. When a fader is discrete, it will track other faders that are running the same cue list, BUT if a fader that it is tracking manually changes to a different cue list, a discrete enabled fader will not change its content. When set to No (or disabled), once a fader is in sync with another fader running the same cue list, it will stay in sync when content is changed. Discrete disabled is noted in the fader ribbon with a link icon.

##### Size

A fader can be mapped so its content takes up 1, 2, or 3 faders. 1x will take up 1 fader, 2x will use 2 faders, and 3x will use three.

> **Note:** *If a fader is mapped to 1x, the top button will be locked as a load button. When mapped to 2x or 3x, the top left button will be locked as a load button.*

##### Buttons & Slider

When set to Default Mapping, the button and fader configuration is drawn initially from the cue list or submaster list properties for that content. If changes are made to that mapping in Tab 36, it filters BACK to the cue or submaster list and changes any other instances where that content is mapped. If set to Local, any changes made in Tab 36 impact only that instance of the content. See *Cue List Properties* and *Submaster Properties* on default mapping.

##### Target List

> If temporary fader mapping is being used, the list of content will display here. See *Temporary Fader Mapping (on page 317)*.

#### Additional Configuration

Clicking on the configuration box will open additional configuration options that are dependent on the target type assigned to the fader.

For detailed information on these various options, see the following topics:

-   *Master Configuration (on page 133)*

-   *Cue List Properties (on page 349)*

-   *Submaster Properties (on page 432)*

-   *Preset and Palette Fader Properties (on page 313)*

-   *Global Effects Fader (on page 421)*

#### Indicators in the Element 2 & Element Classic Fader Status Display

Each fader is color coded based on its assigned target type. Channel faders are orange. Grandmasters and inhibitive submasters are in red, additive submasters are yellow, and presets, palettes, global effects, and manual time masters are orange.

> The fader status display can be disabled in Setup. See *Device > Displays (on page 233)*.

*(figure omise)*{width="5.430987532808399in" height="0.6007283464566929in"}

1.  Orange box indicates a channel fader.

2.  Current channel number controlled by fader.

3.  Label (channel and target labels will display).

4.  Current channel level. (Level will display regardless of control from fader or keypad.)

5.  Up arrow indicates that there is a higher level currently set for the channel and that the fader needs to be raised to match.

*(figure omise)*{width="5.422811679790026in" height="0.49552055993000876in"}

1.  Palette on a fader.

2.  Current submaster number controlled by fader.

3.  Red box indicates an inhibitive submaster.

4.  Effect on a submaster.

5.  Label (channel and target labels will display).

6.  Grandmaster on a fader.

7.  Up arrow indicates that there is a higher level currently set for the channel and that the fader needs to be raised to match.

8.  Down arrow indicates that there is a lower level currently set for the channel and that the fader needs to be lowered to match.

9.  Level of submaster currently.

10. *Global Effects Fader (on page 421)*

11. *Manual Time Master (on page 134)*

#### Fader List

The Fader List, which shows all of the faders and their assignments, can be found in Tab 35.

*(figure omise)*{width="5.891198600174978in" height="2.4572911198600176in"}

You can also make changes to a fader\'s configuration while in the fader list display by clicking on a column. A virtual fader will be displayed. Click on the appropriate area of the fader to access the configuration options. Selection can be done by clicking in the column or from the command line.

Range editing is possible in this display by selecting all the needed faders. Changes made to the configuration will be made to all of the selected faders.

With a fader selected, the CIA will also display a virtual fader and the configuration options for that fader.

#### Fader Ribbon

> **Note:** *Not available on Element Classic.*

The fader ribbon shows the fader color coding that is used in the fader configuration tools.

Grandmasters and inhibitive submasters are in red, additive submasters are yellow ,playback faders display in green ,and presets and palettes are orange.

*(figure omise)*{width="5.03262467191601in" height="0.5660411198600175in"}

#### Main Fader Configuration

Use {Main Fader} to open the master fader configuration window.

*(figure omise)*{width="1.6004002624671916in" height="1.5281244531933509in"}

##### Target

This setting allows you to choose a cue list to map to the main playback fader.

> **Note:** *Although all fader target options are displayed in the dropdown menu, only cue lists can be assigned to the master fader.*

##### ID

This sets the number of the target assigned to the fader, such as cue list 2. For a list of available Target IDs, click or press the {\...} button beside ID.

Element 2 and Element Classic can only map to cue list 1.

##### Discrete Instance

This setting defaults to Yes and applies to cue lists. When a fader is discrete, it will track other faders that are running the same cue list, but if a fader that is tracking manually changes to a different cue list, a discrete enabled fader will not change its content. When set to No (or disabled), once a fader is in sync with another fader running the same cue list, it will stay in sync when content is changed. Discrete disabled is noted in the fader ribbon with a link icon.

##### Size

The main playback is set to a size of 2 faders and cannot be changed.

##### Buttons & Slider

You can select to use default mapping for the fader, or you can use local mapping.

> **Note:** *When a user first joins a session, the main playback fader is unmapped. Once a cue list is established for that user, any other devices joining the user group will have the same cue list automatically mapped to their main playback fader. If a device changes its user ID, the cue list on the main playback fader will be remapped accordingly.*
>
> Additional configuration options are available. see *Cue List Properties (on page 349)*.

#### Master Configuration

There are a variety of different master configuration options for faders that have unique properties.

##### Grandmaster

When a fader is configured as a grandmaster, you can set the fader itself as a master or disable it. Fader size is set to 1x, and cannot be changed.

*(figure omise)*{width="0.5994674103237095in" height="1.11625in"}

The first button is locked as a load button, and cannot be configured. The second button is disabled and cannot be configured. The third button can be configured as a blackout button or disabled. When configured as a blackout, both buttons must be pressed to set the grandmaster to blackout.

##### Manual Time Master

> **Note:** *Manual Time Master applies to changes made manually, not to playback.*

A manual time master can be used to impact any manual control timing. For a manual time master, you need to assign a minimum and maximum time setting to the fader. By default, the minimum is set to 0 seconds when the fader is completely down, and maximum is 5 seconds when the fader is at full. To change the timing, click on the box and enter the time from the pop-up number pad.

> The fader buttons can be assigned as bump, disabled, or macro (see *Submaster Fader and Button Configuration (on page 436)*). It is recommended that the bottom button be set to bump for turning the fader on/ off. When turned on, the LED will be solid green.
>
> **Note:** *The setting of the manual time master is ignore unless turned on. Changing the manual timing master will not impact any manual changes already in motion.*

The fader ribbon will display the label of M Time to indicate a manual time master fader.

**Note:** *Channel and parameter filters can be assigned to a manual time master.*

You can override a manual time master by using a command line entered sneak time.

##### Master Only

Master Only faders are used to set a level for content to fade to. The slider can be used to live adjust levels when the fader has been activated via the bump button.

Master Only faders default to Full.

To set the fader level from the command line, use [Fader] [n] [At] [level] [Enter].

> **Note:** *If content is set to proportional, Master Only fades all content to the setting of the fader when bumped. If set to I-Master, the fader masters the intensity, but non-intensity goes to the end state in time when the content is triggered.*

##### Rate Master

Consoles with rate wheels can use them to adjust the rate dynamically. Consoles without can configure a rate master.

Rate defaults to 100%, which is real time (example: 5 seconds = 5 seconds). Decrease the percentage to slow the cue down. Increase the percentage to speed up the event.

Following are some examples of rate:

-   A 50% decrease rate applied to a 5 second event will play the cue in 10 seconds.

-   A 200% increase rate applied to a 5 second event will play the cue in 2.5 seconds.

-   Setting the rate to 0% will stop the cue.

The top rate adjustment is 2000%. All timing values associated with a cue (including any follow or hang times) are affected by the rate modification proportionally.

#### Channel and Parameter Filters on Faders

Channel and Parameter Filters can be used to allow only specified data to be played back. These are playback filters, and do not impact how data is recorded.

Channel and Parameter Filters can be associated with the following targets for playback:

-   Cue lists

-   Submasters

-   Presets

-   Palettes

> **Note:** *Channel and Parameters filters can also be used with Global Effects Faders. See Global Effects Fader (on page 421)*
>
> **Note:** *For presets and palettes, channel and parameter filters can only be assigned in the fader configuration display (Tab 36) or in the fader list (Tab 35).*

For cue lists and submasters, channel and parameter filters can be set in the following areas:

-   Cue List Index

-   Submaster List

-   Fader configuration display (Tab 36)

-   Fader list (Tab 35)

-   In Live using the {Properties} softkey

Tap or click on {Chan Filter} to assign channels or groups. Tap or click on {Param Filter} to open a list of available parameters that you can filter. Only the specified channels, groups, and parameters will be played back.

> **Note:** *Filters will travel with their assigned cue lists and submasters wherever they are mapped.*

When a filter has been applied, an indicator will display in the fader ribbon. C will display for channel filter, and F is for parameter filter.

###### Clearing Channel and Parameter Filters

Press the red [X] to clear the channel or parameter filters listed.

#### Virtual Fader Module

A virtual fader module can be opened from the home screen by selecting the Faders display button, or by pressing [Tab] [2][8].

*(figure omise)*{width="4.530094050743657in" height="1.7852077865266842in"}

The virtual fader module has a configuration menu, which is accessed by first selecting the module tab and then double clicking on the tab to open the menu. With the virtual fader module selected, you can also select the gear icon, which is located by the tabs, to open the configuration menu.

The following options are available in this configuration menu:

-   Rows - sets the number of rows used for the module. Maximum number of rows is six.

-   Columns - sets the number of columns used for the module. Maximum number of columns is six.

-   Slider Format - choose between the following options:

    -   Buttons - configurable buttons

    -   Faders - sliders and configurable buttons

    -   Apex Faders - Apex endless fader wheels, sliders, and configurable buttons

-   Display Master Fader Pair - check this box to display the virtual master fader pair. Unchecked by default.

> For information about configuring your faders, see *Fader Configuration (on page 129)*

#### Copying Faders Using Attributes Only

When copying faders, you can use {Attrs Only} to copy over all of the fader properties except levels, effects, and labels.

-   [Fader] [1] [Copy To] [Fader] [4] {Attrs Only} [Enter] [Enter] - copies all of the fader properties from fader 1 and places it in fader 4. Levels, effects, and labels are not copied when using the {Attrs Only} softkey.

### Face Panel Shortcuts

##### Overview

The following is a list of button pushes: single, maintained, or combined. It is highly recommended that you read and familiarize yourself with this list.

> See also *Keyboard Shortcuts* .

##### Displays

-   [Data] (maintained press) - toggles the display to show data living under referenced data. Keep [Data] depressed to page. [Data] & [Data] locks this display.

-   [About] & [Data] - locks the display to the absolute data display.

-   [Time] (maintained press) - toggles the display to show discrete timing. Keep [Time] depressed to page.

-   [About] & [Time] - locks the display to discrete time display. Press [About] & [Time] [Time] to unlock, or temporarily display discrete time.

-   [Data] & [Focus] / [Color] / [Beam] - to expand/ suppress categories on displays. (Ion)

-   [Data] & {Parameter Tiles} - to suppress/ display individual parameters from the display when not in summary view. (Ion)

-   [Params] & [Focus] / [Color] / [Beam] - to expand/ suppress categories on displays. (Ti/ Eos/ Gio)

-   [Params] & {Parameter Tiles} - to suppress/ display individual parameters from the display when not in summary view. (Ti/ Eos/ Gio)

-   [Displays] & [Level Wheel] - controls the Main slider in Brightness Settings.

-   [Displays] [Displays] - resets the CIA to the browser.

-   [About] & [Path]/{ Color Path} - toggles the display to show the color paths.

-   [Shift] & [Select] - reset display columns.

-   [Shift] & [Tab] - clear all tabs on the current monitor (but keep locked frames) (Does not clear tab 1 and 2).

-   [Shift] & [Tab] [Tab] - clear all tabs on all monitors (but keep locked frames) (Does not clear tab 1 and 2).

-   [Shift] & [Tab] [Tab] [Tab] - clear all tabs on all monitors (including locked frames) (does not clear tab 1 and 2).

-   [Shift] & [Label] - opens the cue note for the selected cue. Adds a note to a currently selected cue if one doesn\'t already exist.

-   [About] & [Label] [Label] - double press to lock reference labels on. Press [About] & [Label] again to unlock.

-   [Shift] & [Live/ Blind] - advances the displays to the next instance of Live or Blind.

-   [Live] (when already in Live) - resyncs the selected cue to the most recently activated cue.

-   [Blind] (when already in Blind) - resyncs the selected cue to the live selected cue (when blind cue has been changed or when preserve blind cue has been enabled).

-   [Flexi] & [Time] - to invoke flexi time view on displays.

-   [Format] & [Level Wheel] - zooms the display in focus.

-   [Tab] & [Up/Down Arrow] - cycle workspaces.

-   [Tab] & [Left/Right Arrow] - move displays.

-   [Tab] & [number] - open or focus specific displays.

-   [Flexi] & [.] - turns on Flexi multicells off mode. Press again to turn off.

-   [About] & [Live] - displays the DMX values.

-   [About] & [Mark] - displays the mark cue used by the channels.

-   [About] & [Next]/[Last] - displays the next cue that the channels move in or the last cue that the channels moved in.

-   [About] & [Park] - displays the parked levels.

-   [About] & [Part] - displays the cue part number for each parameter.

-   [Expand] & [Effect] - opens the Effect Status Display (Tab 8).

##### Face Panel

-   [Shift] & [Escape] - to lock and unlock face panel.

-   Encoder Paging Keys & [Number] - pages to the desired encoder control page.

-   [Escape] & Encoder Paging Keys - locks the encoders. Press any encoder page button to unlock.

-   [Flexi] & Encoder Paging Key - to invoke flexi encoder states.

-   [Fader Controls] & [Bump Button] - select a fader page on wings.

-   [Fader Page] & Rate Wheel - rolls the selected fader page. (Ti/Eos/Gio)

-   [Fader Page] & [number] - select a fader page on integral faders. (Ti/Eos/Gio)

-   [Fader Page] - increments the fader page by 1.(Ti/Eos/Gio)

-   [Shift] & [Fader Page] - decrements the fader page by 1. (Ti/Eos/Gio)

-   [Learn] & [Load] - opens the selected fader\'s configuration tools.

-   [Off] & [Load] - releases control of content, restoring to background and leave cue list with pending cue in tact.

-   [Release] & [Load] - releases control of content, restoring to background, and resets cue list to top.

-   [Shift] & [Go] or [Shift] & [Back] - cuts the pending cue or the previous cue.

-   [Shift] & [Load] - to remove content from a fader.

-   [Shift] & [Stage] - toggles Scroll Lock on and off.

##### Operations

-   [At] [Enter] - removes move information from selected channel/parameters.

-   [At] [At] - set to Level (as defined in Setup).

-   [Color] (Encoder Paging Key) & Encoder Movement - hold Color Point while adjusting parameters.

-   [Copy To] [Copy to] - posts Move To on the command line.

-   [Full] [Full] - sets selected channels intensity to "full" and self terminates.

-   [Label] [Label] - appended to a record target command, clears the current label, this includes show file labels.

-   [Recall From] [Recall From] - posts Recall From Cue to the command line.

-   [Record] [Record] - posts Record Only to the command line.

-   [Select Active] [Select Active] - Select Active minus submaster contributions.

-   [Shift] & [Select Active] - posts Select Non-Sub Active.

-   [Shift] & [Enter] - repeats last command line, unterminated; does a loop of last five commands.

-   [Shift] & [At] - recalls last channel(s) and parameters without terminating; does a loop of last five commands.

-   [Shift] & [Block] - posts Intensity Block to the command line.

-   [Shift] & [Clear] - clears the command line.

-   [Shift] & [Delay] - posts follow.

-   [Shift] & Encoder Paging Key - posts the category to the command line. For beam subcategories, press Image, Form or Shutter twice to post Beam. (Ion/Gio)

-   [Shift] & Encoder Movement - accesses fine mode.

-   [Shift] & Encoder Push/ Toggle - posts the parameter to the command line. (Ion)

-   [Shift] & Gel Tile - cycles through three modes of Brightness.

-   [Shift] & [Full] or [Shift] & [Out] - flash on or flash out.

-   [Shift] & [+] or [Shift] & [-] - +% or -%.

-   [Shift] & [Highlight] - appends highlight to the current channel selection.

-   [Shift] & [Select Last] - posts additional channel selection options to the softkeys.

-   [Shift] & [Sneak] - makes manual data unmanual.

-   [Shift] & [Update] - shortcut to Save.

-   [Shift] & restore manual faders - reset faders to zero without asserting control.

-   [Shift] & {Direct Select} - posts DS to the command line without terminating.

-   [Shift] & [Next] or [Shift] & [Last] - advances the cue without changing channel selection.

-   [Sneak] [Sneak] - releases NPs of selected channels and self terminates.

-   [Timing Disable] & [Go] or & [Back] - cuts the next cue or cuts the last cue.

-   [Thru] [Thru] - [Thru] command accesses only channels displayed in the current flexi-state (unless the range specified is NOT in the current display). [Thru] [Thru] selects the range regardless of the flexi mode.

-   [Trace] [Trace] - forces a previously inactive light to track its new intensity setting backwards.

-   [Undo] - clears an unterminated command line. Otherwise opens undo controls.

-   [Update] & [Sub Bump] - to update a specific submaster.

-   [n] [At] [/] [/] [m] [Enter] - sets direct DMX value (m) for channel (n).

-   [Shift] & [Delay] [Delay] - posts hang to the command line.

-   [Shift] & [About] - opens a command line search window.

-   [Shift] & [.] - posts minus cells to the command line. This is for use with multicell fixtures.

-   [.] - posts cells or cells only to the command line when used after channel number(s). This is for use with multicell fixtures.

-   [Shift] & [Int Palette] - posts preset on the command line (Element & Element 2).

-   [Displays] & [Record] - puts a marker in the log file.

### Keyboard Shortcuts

A list of common Eos functions and their associated QWERTY keyboard shortcuts.

> **Note:** *Scroll Lock must be off to use keyboard shortcuts.*

  -----------------------------------------------------------------------
  Console Function                       Windows Shortcut
  -------------------------------------- --------------------------------
  Shortcut List                          Alt /

                                         ?

  0                                      0

  1                                      1

  2                                      2

  3                                      3

  4                                      4

  5                                      5

  6                                      6

  7                                      7

  8                                      8

  9                                      9

  . (decimal)                            . (decimal)

  - (minus)                             - (minus)

  + (plus)                              =

                                         +

  +%                                     Shift =

                                         Control Alt =

  -%                                     Shift -

                                         Control Alt -

  /                                      /

  A3D Camera Up                          Up Arrow

  A3D Camera Up (Edit Mode)              W

  A3D Camera Forwards                    Shift Up Arrow

  A3D Camera Forwards (Edit Mode)        Shift W

  A3D Camera Left                        Left Arrow

  A3D Camera Left (Edit Mode)            A

  A3D Camera Down                        Down Arrow

  A3D Camera Down (Edit Mode)            S

  A3D Camera Backwards                   Shift Down Arrow

  A3D Camera Backwards (Edit Mode)       Shift S

  A3D Camera Right                       Right Arrow

  A3D Camera Right (Edit Mode)           D

  About                                  Y

  Address / Dimmer                       Alt A
  -----------------------------------------------------------------------

+--------------------------------------+-------------------------------+
| Console Function                     | Windows Shortcut              |
+======================================+===============================+
| All NPs                              | Control N                     |
+--------------------------------------+-------------------------------+
| Assert †                             | Control W                     |
+--------------------------------------+-------------------------------+
| Assert (Playback) †                  | Control Alt A                 |
+--------------------------------------+-------------------------------+
| At                                   | A                             |
+--------------------------------------+-------------------------------+
|                                      | @                             |
+--------------------------------------+-------------------------------+
|                                      | *                            |
+--------------------------------------+-------------------------------+
| Back (ECU)                           | Escape                        |
+--------------------------------------+-------------------------------+
| Beam Filter                          | Control B                     |
+--------------------------------------+-------------------------------+
| Beam Palette                         | Alt B                         |
+--------------------------------------+-------------------------------+
| Blind                                | F2                            |
+--------------------------------------+-------------------------------+
|                                      | Control 2                     |
+--------------------------------------+-------------------------------+
| Block                                | B                             |
+--------------------------------------+-------------------------------+
| Capture                              | Control Alt P                 |
+--------------------------------------+-------------------------------+
| Clear                                | Backspace                     |
+--------------------------------------+-------------------------------+
| > Clear Command Line                 | Shift Backspace               |
+--------------------------------------+-------------------------------+
|                                      | Control Alt Backspace         |
+--------------------------------------+-------------------------------+
| Clear Label                          | Control Backspace             |
+--------------------------------------+-------------------------------+
| Color Filter                         | Control C                     |
+--------------------------------------+-------------------------------+
| Color Palette                        | Alt C                         |
+--------------------------------------+-------------------------------+
| Color Path                           | Control Alt W                 |
+--------------------------------------+-------------------------------+
| Copy To                              | C                             |
+--------------------------------------+-------------------------------+
| Cue                                  | Q                             |
+--------------------------------------+-------------------------------+
| Cue Only / Track                     | X                             |
+--------------------------------------+-------------------------------+
| Data                                 | Control D                     |
+--------------------------------------+-------------------------------+
| Data Mode                            | Control Shift D               |
+--------------------------------------+-------------------------------+
| Delay                                | D                             |
+--------------------------------------+-------------------------------+
| Delete                               | Delete                        |
+--------------------------------------+-------------------------------+
| Delete (macOS)                       | Fn Delete                     |
+--------------------------------------+-------------------------------+
| Displays                             | F9                            |
+--------------------------------------+-------------------------------+
|                                      | Control 9                     |
+--------------------------------------+-------------------------------+
| Effect                               | Alt E                         |
+--------------------------------------+-------------------------------+
| Effects Softkeys †                   | Alt Shift E                   |
+--------------------------------------+-------------------------------+
| Encoder Display (Gio) †              | Control Alt \                |
+--------------------------------------+-------------------------------+
| Encoder Page Color \^†               | Control Alt [                |
+--------------------------------------+-------------------------------+
| Encode Pager Focus \^†               | Control Alt ,                 |
+--------------------------------------+-------------------------------+
| Encoder Page Form \^†                | Control Alt ;                 |
+--------------------------------------+-------------------------------+
| Encoder Page Image \^†               | Control Alt ]                |
+--------------------------------------+-------------------------------+
| Encoder Page Intensity \^†           | Alt .                         |
+--------------------------------------+-------------------------------+
| Encoder Page Shutter \^†             | Alt ,                         |
+--------------------------------------+-------------------------------+
| Enter                                | Enter                         |
+--------------------------------------+-------------------------------+

+--------------------------------------+-------------------------------+
| Console Function                     | Windows Shortcut              |
+======================================+===============================+
| Escape                               | Escape                        |
+--------------------------------------+-------------------------------+
| Expand                               | F5                            |
+--------------------------------------+-------------------------------+
|                                      | Control 5                     |
+--------------------------------------+-------------------------------+
| Fader Page †                         | V                             |
+--------------------------------------+-------------------------------+
| Fan †                                | W                             |
+--------------------------------------+-------------------------------+
| FlexiChannel                         | F3                            |
+--------------------------------------+-------------------------------+
|                                      | Control 3                     |
+--------------------------------------+-------------------------------+
| Focus Filter                         | Control F                     |
+--------------------------------------+-------------------------------+
| Focus Palette                        | Alt F                         |
+--------------------------------------+-------------------------------+
| > Follow / Hang †                    | Shift D                       |
+--------------------------------------+-------------------------------+
|                                      | Control Alt D                 |
+--------------------------------------+-------------------------------+
| Format                               | F4                            |
+--------------------------------------+-------------------------------+
|                                      | Control 4                     |
+--------------------------------------+-------------------------------+
| (Scroller) Frame                     | Control Alt C                 |
+--------------------------------------+-------------------------------+
| Freeze †                             | Control Alt F                 |
+--------------------------------------+-------------------------------+
| Full                                 | F                             |
+--------------------------------------+-------------------------------+
| Go                                   | Spacebar                      |
+--------------------------------------+-------------------------------+
| Go To Cue                            | Control G                     |
+--------------------------------------+-------------------------------+
| Go To Cue Zero                       | Control Alt G                 |
+--------------------------------------+-------------------------------+
| Group                                | G                             |
+--------------------------------------+-------------------------------+
| Help                                 | Alt /                         |
+--------------------------------------+-------------------------------+
| Highlight †                          | \                            |
+--------------------------------------+-------------------------------+
|                                      | Control Alt H                 |
+--------------------------------------+-------------------------------+
| Home                                 | Home                          |
+--------------------------------------+-------------------------------+
|                                      | Control H                     |
+--------------------------------------+-------------------------------+
| Home (macOS)                         | Fn Left Arrow                 |
+--------------------------------------+-------------------------------+
| > Intensity Block †                  | Shift B                       |
+--------------------------------------+-------------------------------+
|                                      | Control Alt B                 |
+--------------------------------------+-------------------------------+
| Intensity Filter                     | Control I                     |
+--------------------------------------+-------------------------------+
| Intensity Palette                    | Alt I                         |
+--------------------------------------+-------------------------------+
| Label / Note                         | L                             |
+--------------------------------------+-------------------------------+
| Last                                 | Page Up                       |
+--------------------------------------+-------------------------------+
|                                      | Control ,                     |
+--------------------------------------+-------------------------------+
| Last (macOS)                         | Fn Up Arrow                   |
+--------------------------------------+-------------------------------+
| Learn                                | Alt L                         |
+--------------------------------------+-------------------------------+
| Level                                | Control V                     |
+--------------------------------------+-------------------------------+
| Live                                 | F1                            |
+--------------------------------------+-------------------------------+
|                                      | Control 1                     |
+--------------------------------------+-------------------------------+
| Load                                 | Control Alt L                 |
+--------------------------------------+-------------------------------+
| Macro                                | M                             |
+--------------------------------------+-------------------------------+

+--------------------------------------+-------------------------------+
| Console Function                     | Windows Shortcut              |
+======================================+===============================+
| Macro 801*                          | Control Alt 1                 |
+--------------------------------------+-------------------------------+
| Macro 802*                          | Control Alt 2                 |
+--------------------------------------+-------------------------------+
| Macro 803*                          | Control Alt 3                 |
+--------------------------------------+-------------------------------+
| Macro 804*                          | Control Alt 4                 |
+--------------------------------------+-------------------------------+
| Macro 805*                          | Control Alt 5                 |
+--------------------------------------+-------------------------------+
| Macro 806*                          | Control Alt 6                 |
+--------------------------------------+-------------------------------+
| Macro 807*                          | Control Alt 7                 |
+--------------------------------------+-------------------------------+
| Macro 808*                          | Control Alt 8                 |
+--------------------------------------+-------------------------------+
| Macro 809*                          | Control Alt 9                 |
+--------------------------------------+-------------------------------+
| Macro 810*                          | Control Alt 0                 |
+--------------------------------------+-------------------------------+
| Magic Sheet                          | Alt M                         |
+--------------------------------------+-------------------------------+
| > Manual Override                    | Control Alt M                 |
+--------------------------------------+-------------------------------+
|                                      | Control Alt N                 |
+--------------------------------------+-------------------------------+
| Mark †                               | K                             |
+--------------------------------------+-------------------------------+
|                                      | Control Alt K                 |
+--------------------------------------+-------------------------------+
| Mirror Start                         | Alt F1                        |
+--------------------------------------+-------------------------------+
| Mirror Stop                          | Alt F2                        |
+--------------------------------------+-------------------------------+
| ML Controls                          | F7                            |
+--------------------------------------+-------------------------------+
|                                      | Control 7                     |
+--------------------------------------+-------------------------------+
| More Softkeys (More SK)              | Alt 7                         |
+--------------------------------------+-------------------------------+
| Next                                 | Page Down                     |
+--------------------------------------+-------------------------------+
|                                      | Control                       |
+--------------------------------------+-------------------------------+
| Next (macOS)                         | Fn Down Arrow                 |
+--------------------------------------+-------------------------------+
| Off                                  | Control Alt O                 |
+--------------------------------------+-------------------------------+
| Offset                               | Control O                     |
+--------------------------------------+-------------------------------+
| Out                                  | O                             |
+--------------------------------------+-------------------------------+
| Page Left                            | Left Arrow                    |
+--------------------------------------+-------------------------------+
| Page Right                           | Right Arrow                   |
+--------------------------------------+-------------------------------+
| Page Up                              | Up Arrow                      |
+--------------------------------------+-------------------------------+
| Page Down                            | Down Arrow                    |
+--------------------------------------+-------------------------------+
| Parameters (Display)                 | Control D                     |
+--------------------------------------+-------------------------------+
| Park                                 | Alt K                         |
+--------------------------------------+-------------------------------+
| Part                                 | P                             |
+--------------------------------------+-------------------------------+
| Patch                                | ;                             |
+--------------------------------------+-------------------------------+
| Pixel Map †                          | Alt X                         |
+--------------------------------------+-------------------------------+
| Preset †                             | Alt P                         |
+--------------------------------------+-------------------------------+
| Query †                              | Control Q                     |
+--------------------------------------+-------------------------------+
| Rate                                 | Control Alt R                 |
+--------------------------------------+-------------------------------+
| Recall From                          | E                             |
+--------------------------------------+-------------------------------+
| Record                               | R                             |
+--------------------------------------+-------------------------------+

+--------------------------------------+-------------------------------+
| Console Function                     | Windows Shortcut              |
+======================================+===============================+
| RecordOnly                           | Control R                     |
+--------------------------------------+-------------------------------+
| Release                              | Control Alt S                 |
+--------------------------------------+-------------------------------+
| Rem Dim                              | H                             |
+--------------------------------------+-------------------------------+
| Scroll Lock                          | Control 6                     |
+--------------------------------------+-------------------------------+
| Select                               | Control Enter                 |
+--------------------------------------+-------------------------------+
| Select (ECU)                         | Return                        |
+--------------------------------------+-------------------------------+
| Select Active                        | Control A                     |
+--------------------------------------+-------------------------------+
| Select Last                          | Control L                     |
+--------------------------------------+-------------------------------+
| Select Manual                        | Control M                     |
+--------------------------------------+-------------------------------+
| Setup                                | Alt S                         |
+--------------------------------------+-------------------------------+
| Shift                                | Z                             |
+--------------------------------------+-------------------------------+
| Snapshot                             | Control S                     |
+--------------------------------------+-------------------------------+
| Sneak                                | N                             |
+--------------------------------------+-------------------------------+
| Softkey 1                            | Alt 1                         |
+--------------------------------------+-------------------------------+
| Softkey 2                            | Alt 2                         |
+--------------------------------------+-------------------------------+
| Softkey 3                            | Alt 3                         |
+--------------------------------------+-------------------------------+
| Softkey 4                            | Alt 4                         |
+--------------------------------------+-------------------------------+
| Softkey 5                            | Alt 5                         |
+--------------------------------------+-------------------------------+
| Softkey 6                            | Alt 6                         |
+--------------------------------------+-------------------------------+
| Spacebar Disable                     | Alt G                         |
+--------------------------------------+-------------------------------+
| Staging Mode                         | F6                            |
+--------------------------------------+-------------------------------+
| Stop / Back                          | Control Spacebar              |
+--------------------------------------+-------------------------------+
|                                      | Control Alt Q                 |
+--------------------------------------+-------------------------------+
| Stop Effect                          | Shift Alt E                   |
+--------------------------------------+-------------------------------+
| Submaster                            | S                             |
+--------------------------------------+-------------------------------+
| Tab                                  | Tab                           |
+--------------------------------------+-------------------------------+
| Time                                 | I                             |
+--------------------------------------+-------------------------------+
| Time (Displays)                      | Control Alt I                 |
+--------------------------------------+-------------------------------+
| Timing Disable                       | Control Alt T                 |
+--------------------------------------+-------------------------------+
| > Toggle Hotkeys                     | F8                            |
+--------------------------------------+-------------------------------+
|                                      | Control 8                     |
+--------------------------------------+-------------------------------+
| Trace †                              | J                             |
+--------------------------------------+-------------------------------+
| Thru                                 | T                             |
+--------------------------------------+-------------------------------+
| Undo                                 | Control X                     |
+--------------------------------------+-------------------------------+
| Update                               | U                             |
+--------------------------------------+-------------------------------+
| Virtual Keyboard                     | Control K                     |
+--------------------------------------+-------------------------------+
| Workspace                            | ] or [                      |
+--------------------------------------+-------------------------------+

+-------------------------------------------------------------------------------+------------------------------------+
| Console Function                                                              | > Windows Shortcut                 |
+===============================================================================+====================================+
| Zoom selected display                                                         | > Left Mouse Button + Scroll Wheel |
+-------------------------------------------------------------------------------+------------------------------------+
| ** Some key combinations are not available on all physical keyboard layouts* |                                    |
|                                                                               |                                    |
| *\^ Alternatively use Encoder Display + category to change the encoder pages* |                                    |
|                                                                               |                                    |
| *† Commands are not available on Element Classic*                             |                                    |
+-------------------------------------------------------------------------------+------------------------------------+

> **Note:** *To enable Eos functions on macOS Function keys:*

1.  *Navigate to System Preferences > Keyboard*

2.  *Enable the "Use all F1, F2,etc\... keys as standard function keys" setting.*

> **Note:** *Some international keyboards require "Use Shift Key As Eos Shift" to be disabled in Setup > Device > Face Panel > Input Devices. Use Z as shift to* *access shortcut functions in these cases.*

### sACN Output Viewer

You can open the sACN Output Viewer by pressing [Tab] & [3][7] or selecting the sACN Output Viewer icon from the home screen.

The sACN Output Viewer is a place to check the current live outputs on a universe by universe basis.

*(figure omise)*{width="4.9921052055993in" height="2.37125in"}

The left side of the viewer is the universe grid. It displays 512 address cells. Cells outlined in a color are currently patched addresses. Each patched cell contains an address number and output value. Unpatched cells are black and only have an address level.

Output values are 0 through 255. 0 is displayed in black and 255 is in bright red. The red output value color will grow brighter as the output value increases.

If there is a channel or address selection on the command line, the appropriate address cell will be outlined in gold. You can also press on a cell to select it but it will not post to the command line. Information about the selected address will display to the right of the grid.

Any available sACN sources will be displayed in the right panel, and are color coded. The address cells will use that same color coding to indicate the device it is patched to.

#### Configuration Options

When the Follow Command Line box is checked, the viewer will follow the command line for selecting addresses. This is enabled by default.

Press {About} to open the About Address display in the CIA.

Press the left and right arrows to scroll through the available universes, or enter a specific universe number in the box.

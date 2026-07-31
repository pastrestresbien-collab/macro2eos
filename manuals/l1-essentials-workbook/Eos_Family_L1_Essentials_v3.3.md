# Eos Family Console Programming — Level 1: Essentials Workbook (v3.3C)

- Source : PDF officiel ETC, « Eos Family Console Programming Level 1: Essentials », V3.3C, publié 2026-05
- Fichier source : [`source/Eos_Family_L1_Essentials_v3.3.pdf`](source/Eos_Family_L1_Essentials_v3.3.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select


Eos Family Console Programming

             Level 1: Essentials

                        Workbook
                                      V3.3C

            www.etcconnect.com/education

                            Released: 2026-05

## Table of Contents

      ETC permits the reproduction of materials in this manual only for non-commercial purposes. All
           other rights are reserved by ETC.

## Purpose of the Class

    This class will provide an overview of the console and programming for
    conventional fixtures as well as movers and LED fixtures. If new to the
    console, then this class is perfect. Whether transitioning to an Eos family
    console or a new console owner, this class will teach the basics to get the
    programmer up and running with this versatile console.

### LEARNING OBJECTIVES:

        After completing the class, one should be able to:
            - Patch conventional and multi-parameter fixtures
             - Work with channels in Live mode
             - Work with basic display navigation
             - Record, select, and delete Groups
             - Record to, load, and clear Submasters
             - Record, play, and delete Cues
             - Understand Tracking versus Cue Only as well as Block and Assert
             - Control non-intensity parameters at a basic level
             - Apply additional cue features such as Delay, Auto-Follow and Loop
             - Use Park efficiently
             - Evaluate and make changes in Setup
             - Create simple step-based Effects

### WORKBOOK SYNTAX ANNOTATION

             - Bold             Syntax and Browser menus
             - [Brackets]       Face panel buttons
             - {Braces}         Softkeys or buttons on touchscreen
             - <Angle brackets>            Optional keys or command line text
             - [Next] & [Last]             Keys to be pressed & held simultaneously
             - «Direct Select»             Direct Select button press
             - MS Object An Object on a Magic Sheet
             - Play Icon   Link to video on ETC’s YouTube Channel –
                  ETCVideoLibrary

### HELP

        Press and hold [Help] and press any key to see:
            - the name of the key
             - a description of what the key enables you to do
             - syntax examples for using the key (if applicable)
             As with hard keys, the “press and hold [Help]” action can also be used with softkeys and
             clickable buttons.

### THE MANUAL

        The manual is available on the console, Tab #100.
          Click on Add-a-Tab (the {+} sign) , select Manual

          Hold [Tab] & press [100]
        Please note that the manual is not available on Windows XP devices but is available as a download
        from the web site.

## Hardware Overview

### EXPLORING THE BACK OF THE CONSOLE (ION XE SHOWN)

       - Hard Power Switch with IEC Receptacle – power cable included
       - Motherboard – Windows embedded, multi-point touchscreens
       - Video connections are Display Port connections. (2 or 3)
       - USB ports (4 or 6)
       - Two individually configurable Ethernet ports
       - Four DMX/RDM ports
       - Remote trigger/ contact inputs via D-Sub connector
       - 3-pin XLRs for desk work lights, dimmer control through software

       -

### EXPLORING THE FRONT OF THE CONSOLE

       - Five, ten, or twenty faders, configurable and pageable
       - Master Playback crossfade pair with 100mm faders,  Go,
           Stop/Back and Master (Load) buttons
       - Rate Wheel (also used to page faders) and fader control
           buttons
       - Keypad area – 3 sections: targets, numeric keypad, and
           level controls
       - Display & Navigation keypad – Live and Blind displays,
           format, paging, and navigation within displays
       - Level Wheel
       - Encoders – 4 on Ion Xe and Gio and 6 on Apex – the
           center of each encoder is a button
       - Soft Power Switch – used to power up the console
       - USB Port – primarily to connect any USB storage device
           (one on Ion Xe/Gio@5, two on Apex)
       - On Gio@5 and Apex – Built-in LCD touchscreens for
           display, direct select and context sensitive control

### SOFTKEYS

   On the Ion Xe face panel, you hold down [More SK] and press the Encoder
   Category button to access the softkey S1 thru S6 functions.
   Softkey functions are displayed on the monitor in the lower right hand corner
   of the monitor with the CIA/Browser. White labels on bottom indicate active
   and gray labels on top indicate a second page of softkeys.
   [More SK] will page between the two pages of softkeys.

### EXPLORING THE BACK OF THE APEX DESK

          - USB-A & USB-C (data) (2) - ports are provided to connect any USB
              storage device or connect peripherals such as an alphanumeric
              keyboard, pointing device, or touchscreen control for external
              monitors.
          - Hard power switch / IEC socket (18)
          - IO garage (19) - four input / output bays for custom configuration of
              the available data ports. Any ETC Gadget II or Response Show Control
              Gateway can be connected internally via USB for local input / output
              of DMX, MIDI, SMPTE, and other protocols.
          - Display Port (20)
          - SFP+ (21) - Enhanced Small Form Factor Pluggable ports are provided
              for direct-to-core connection, or high-speed links between session
              devices, and can take a variety of sled options. Sleds are field
              changeable for easy reconfiguration.
          - Ethernet ports (22) for connecting to a network switch, network
              gateways, and accessory devices. Each port can be run as a separate
              NIC and can be configured to directly output network-based lighting
              control protocols such as sACN or Art-Net. All ports provide PoE++,
              with up to 100W per port, and 120W total across all ports.
          - Littlite (23) - you may connect two Littlite XLR 3-Pin task lights
          - Two independently controlled work lights are available on the left and
              right sides of Apex consoles for illumination of nearby work surfaces.

### EXPLORING THE FRONT OF THE APEX DESK

      - Numeric Keypad (1) - allows you to type numbers
          for channel or target selection, along with
          modifier keys to alter your selection.
      - Level Controls (2) - provide options for altering the
          intensity levels of channels, along with other non-
          intensity parameters / targets.
      - Targets (3) - provide options for altering a variety
          of record targets, as well as shortcuts to various
          Blind displays.
      - Display & Navigation Keys (4) - provide quick
          access to common displays, formatting, paging,
          and navigation within displays.
      - Encoder Categories Keys (5) - allow navigation and paging of the
          encoders.
      - Softkeys (6) - allow control of context-based software options that
          change in response to the active display or command line syntax.
      - Fader Control Buttons (7) - provide additional options for easy local
          control of fader behavior.

### OTHER CONTROLS

      - Keypad Touchscreen - a haptic touch-enabled screen above the
          keypad that can be configured to control custom direct selects or
          magic sheets. Softkeys and a gear icon to access screen settings are
          docked at the bottom of this display.
      - Target Keys - physical buttons with built-in high-resolution displays.
          − Apex 5 - 20 target keys (2 banks of 10)
          − Apex 10 - 40 target keys (4 banks of 10)
          − Apex 20 - 50 target keys (5 banks of 10)
      - All Apex consoles also offer two target keys over the main playback
          faders for load functionality, as well as local status of playback
          content.
      - Main Playback Fader Pair - a split crossfader pair. The button or
          buttons located directly above the playbacks load content to the
          playbacks. The two buttons below control the [Go] and [Stop/Back]
          functions.
      - Motorized Faders - 5, 10, or 20 configurable motorized faders may be
          configured as playbacks, submasters, grandmasters, timing masters,
          effects masters, targets, or target lists. 100 virtual pages of 10 faders
          each are provided.
      - Load Buttons - located directly above each fader, are used to load a
          specified target to the fader, or to place special conditions on that
          fader.
      - Endless Fader Wheels - Apex consoles offer 5, 10, or 20, color-
          changing fader wheels, adding an endless fader and additional button
          to each overall fader slot. Each fader wheel and button can be mapped
          to any function for additional control before needing to expand the
          overall fader slot to double or triple density.

## Displays Overview

### LIVE AND BLIND CHANNEL DISPLAY

### PRIMARY LIVE SCREEN (CHANNEL DISPLAY)

           - Channel icon – bright white = patched, gray = not patched
           - Selected cue detail line
           - Tab area – currently Tab 1 and Tab 2
           - Command line
           - [Format] for summary or table view in Live
           - Hold [Format] and move wheel to zoom in and out
           - Left button on mouse and use mouse wheel
           - [Page▲] or [Page ▼] – scrolls full page at a time, does wrap
           - [Shift]&[Stage] – when on, scrolls one line at a time
           Red “Scroll On” appears next to Favorite Star in CIA

           [1] [Thru] [10] [Enter] and scroll the level wheel

           - Hold [Data] and roll levels up to expose real values with decimals

### BLIND CHANNEL DISPLAY

       Blind allows us to look at what is recorded without affecting what is currently
       in Live. When in Blind, you can edit any data (cues, presets, palettes, and so
       on), and changes will not automatically be output to your rig.
            - Note the background color and command line color change!
           - [Next] and [Last] navigates through targets like cues, groups…
                − There are no cues yet…
           - [Format] for summary view, table view, or spreadsheet

       ‼   When in Blind, Record is not required – changes are stored when you hit
           [Enter] and the command line is terminated.

       Note: In Live and Blind Table views, the columns can be resized and reset.
       These settings can be stored in snapshots.
               Press [Live]                                                              to go back to the Live view

### TAB NAVIGATION

Tabs are broken down into two categories: Display tabs show information,
such as Live, Blind, and the Playback Status Display (PSD) and Control tabs
are the virtual control options, such as the color picker, and ML Controls.

### TAB NAVIGATION

    Be aware of where focus is on the displays (tab highlighted in gold).
    Live/Blind display is Tab 1. Playback Status display is Tab 2. Neither can be
    closed and you can have multiple instances of either (Tab 1.2 or Tab 2.2).

### TO OPEN DISPLAYS

                                                                                       to either open the associated display or
           Press [Sub] [Sub] … [Group] [Group] … [Effect] [Effect]
                                                                                       select it if it is already open
                                                                                       opens the home screen or display and
           Press Add-a-Tab (the {+} sign) to the right of the tabs
                                                                                       control options

           Press X in upper right corner of display (under console time)               to exit Add-a-Tab display

### TO MOVE DISPLAYS

                                                                                       to move the active display from one
           Hold [Tab] and use [Page►] and [Page◄] keys
                                                                                       monitor to another

           Click/press on the tab and drag                                             to reposition tabs within a frame

### TO CLOSE DISPLAYS

           Press [Tab] until desired display is highlighted, then [Escape]             to close any tab display

### FIXED TAB NUMBERING

    All Display and Control tabs have fixed tab numbering. Patch will always be 12,
    Group List, 17. When you press [Tab] repeatedly, focus moves numerically
    through all open tabs on active workspaces.
                                                                                      to change focus from open display to the
       Press [Tab] … [Tab] … [Tab]
                                                                                      next open display (in numeric order)
       Hold [Tab] & press [12] (Patch)                                                moves focus to a specified tab

       Hold [Tab] & press [17] (Groups)                                               opens a specific tab – Groups

    You can have multiple tabs of the same type open.

       Hold [Tab] & press [1.2]          [Escape]                                     opens a secondary Live tab

       Press [Live] or [Blind]                                                        to instantly bring Live/Blind into focus

### ADDITIONAL TAB TOOLS

       Right click or double tap on the Live tab                                      to see configuration settings

        You can also click on the Gear tab for the same options. These options vary
        depending on the tab in focus.
             − {Close Tab}
             − {Replace Tab} – replace tab with a different tab
             − {Close All Tabs but This}
             − {Close All Tabs}
             − {Reset Columns}

                − {Lock Frame} – prevents other tabs from being moved to the
                  current frame
                − {Open New Tabs in this Frame}
                − {Zoom Out} and {Zoom In}

         The second menu will also vary depending on the tab selected.
         For Live Summary:
                − Show Target Status Bar
                − MC Line Wrap – keeps all cells of a multicell fixture together
                − Show Target Labels in Spreadsheet
                − Show Reference Labels
                − Group Channels by 5
                − Disable 100 Channel Display Mode
                − Enable 100 Channel Display Mode – 5x20
                − Enable 100 Channel Display Mode – 4x25

       Click or touch off the menu                                                      to close the configuration settings

       [Live]                                                                           to put all in the same display

### FLEXICHANNEL MODES              (EASIER TO SEE IN LIVE – SUMMARY)

     In Live, Flexi allows you to view only channels meeting a certain criteria,
     therefore removing unwanted data from view.
       Press [Flexi],     [Flexi],    [Flexi]                                           to change to the next state

         - All channels
         - Patched channels – channels with an address patched to them
         - Manual channels – selected channels and any channels with manual
                data (red data)
         - Show channels – any channels currently active and channels with data
                stored in a record target (cue, groups, subs, palettes…)
         - Active channels – any channels with intensity above 0 or fading to 0,
                running effects, or with non-intensity moves
         - In Use channels – exactly like Flexi Active, but also includes dark
                channels that are marking for a future cue
         - Selected channels – the channels selected on the command line

       Hold [Flexi] and use the softkeys and options in the CIA                         8 states and 2 modes appear in the CIA

     Keep in mind that you can have multiple Live tabs opened (Tab 1.2, 1.3,…)
     each in a different Flexi mode.

     When editing in Flexi, use [Thru] [Thru] to include channels not in the current
     flexi mode.
       In Flexi Patched Channels: [6] [Thru] [35] [Enter]                               see only patched channels in range
                                                                                        overrides flexi state and shows all channels
       [6] [Thru] [Thru] [35] [Enter]
                                                                                        in range

### CENTRAL INFORMATION AREA (CIA)

The Central Information Area (CIA) is the lower portion of one of the
screens. By default, the CIA consists of two primary areas: the parameter
tiles (yellow) and the browser (red).
- [Displays] will always draw focus to the CIA area or a display item set
     as a favorite (Gold highlight)
- Collapse and expand the CIA by pressing [Displays] again or using the
     triangle (△, ▽)
- Double-tap [Displays] will always bring up the browser.
- Use the Lock to prevent the CIA from being collapsed or opened

### BROWSER

    An interface for numerous functions, including saving a show, opening a show,
    changing settings, clearing targets, printing functions, and viewing record
    target lists.
        - Can use a mouse, touch or the page arrow buttons to navigate in the
              browser
        - [Page▲] [Page▼] – scrolls thru the menus
        - [Page►] opens submenus
        - [Page◄] closes submenus or collapses the menu structure
        - [Select] or [Enter] – opens the item
        -

        -

### PARAMETER DISPLAY

    This display shows the parameters available for patched channels. It is also
    where you can select which parameters to view in the Live and / or Blind
    displays, or select parameters for command line control. The parameter
    display will dynamically change depending on the channel (fixture) selected
    and its applicable parameters.

## Patch

### START IN THE LEVEL 1 COMPLETE SHOW FILE

     Double hit [Address/Patch] to get to the Patch display.
     Or press [Displays], then {S3 Patch}. Can also Add-a-Tab (the {+} sign) or
     hold [Tab] and type [12].
     By default, Patch is displayed in a channel view. You can change the display
     to sort by address by pressing [Format].

### USING OUTPUT ADDRESS VS PORT/OFFSET

                                                                                                        selects channel 601 and patches address
            [601] [At] [250] [Enter]
                                                                                                        250 to it
                                                                                                        selects channel 602 and patches the address
            [602] [At] [657] [Enter]
                                                                                                        657 to it
                                                                                                        selects channel 603 and patches the 2nd
            [603] [At] [2] [/] [146] [Enter]
                                                                                                        universe address 146 to it
                                                                                                        displays channels in output address style,
             Press [Data]
                                                                                                        note blue text in upper left corner
                                                                                                        displays channels in port/offset style, note
             Press [Data] again
                                                                                                        blue text in upper left corner

             Press [Data] again                                                                         returns to how it was originally entered

### RANGE PATCHING

                                                                                                        selects a range of channels and patches
            [604] [Thru] [610] [At] [101] [Enter]
                                                                                                        addresses sequentially from first one
                                                                                                        selects channel, patches a range of
            [611] [At] [108] [Thru] [111] [Enter]
                                                                                                        addresses to it, creating parts

            [612] [Thru] [620] [At] [201] {Offset} [3] [Enter]                                          allows for a three-cell cyclight patch

             On Apex consoles, [Offset] is a hard key (button).

### CLEAR VS. UNPATCH VS. DELETE

            [601] [At] [Enter] Please Confirm [Enter]                                                   removes the address, leaves type, etc.

```text
            [602] {Unpatch} [Enter] All Non-Intensity show data for these channels                      restores to default properties – removes
            will also be deleted. Please Confirm [Enter]                                                address, type, label, etc.
```

            [Delete] [603] [Enter] All show data for these channels will also be
                                                                                                        deletes the whole channel from the show
            deleted. Please Confirm [Enter]

                [Live] and look at the Channel View

### UNDO

         From an empty command line, [Undo] opens a command history display in
         the CIA. The most recent completed command is highlighted in gold. Use the
         page arrow keys or a mouse to select multiple commands.
            [Undo] , select last three commands, [Enter] [Enter]                                        to restore channels 601 - 603

             Not all commands can be undone such as playback actions and manual attributes placed
             on channels or encoder actions (shown in gray).
             [Shift]&[Update] and {Save} won’t clear the history. Only opening a new show or powering
             off will clear the history.

### PATCH BY ADDRESS

   Back in {Patch} and press [Format] to switch to ‘By Address’                                Addresses are on the left
                                                                                               selects one address and patches it to a
   [481] [At] [625] [Enter]
                                                                                               channel – note command line
                                                                                               selects a range of addresses and patches
   [482] [Thru] [485] [At] [630] [Enter]
                                                                                               them to one channel (parts)

   Press [Format] to switch to ‘By Channel’                                                    Channels are on the left

### PATCH A MULTI-PARAMETER DEVICE

   [651] [Thru] [656] [Enter]                                                                  selects the channels for 6 fixtures
                                                                                               notice softkeys {Show}, {Manfctr}, {Search}
   Click on {Type} in the lower right hand corner of display
                                                                                               and {Add Show}
                                                                                               left columns are manufacturers; right side
   Click on {Manfctr}
                                                                                               are their devices
    If you are using Search, type SolaFrame and look for SolaFrame Theatre.

   Find {High End Systems} in left columns
                                                                                               notice SolaFrame Theatre in blue – multiple
      Then {SolaFrame Theatre +3D}
                                                                                               modes available
    If a fixture has multiple modes or types, it will display in blue text.
                                                                                               fixture placed on the command line after
   Select {Pan 540 [47] +3D} for standard mode
                                                                                               channels
                                                                                               patches all six fixtures with a starting
   [At] [7] [/] [1] [Enter]
                                                                                               address in universe 7
   [At] [7] [/] [1] {Offset} [50] [Enter] [Enter]                                              now look at the addresses

    On Apex consoles, [Offset] is a hard key (button).
    NOTE: When in Search, the CIE icon = color-calibrated profile, 3D icon = profile with an
    associated Augment3d model.

### PATCH A COMPOUND CHANNEL

A compound channel is a channel that controls more than one device – such
as a fixture with a color scroller, a gobo rotator, and so on.
                                                                                               patches the first part of channels - the
   [641] [Thru] [645] [At] [41] [Enter]
                                                                                               dimmer
   [Part] [2] [Enter]                                                                          creates a part 2 for selected channels
                                                                                               makes part 2 a generic scroller giving the
   {Type}, {Search} Scroller, click on {Generic}, select Scroller [1]
                                                                                               channel a color parameter
   [At] [2] [/] [151] [Enter]                                                                  gives a starting address for all the part 2’s

   [Part] [3] [Enter] {Type}                                                                   creates a part 3 for selected channels
                                                                                               makes part 3 a gobo rotator giving the
   {Search} Smart Move and double click Smart Move DMX [3]
                                                                                               channel a beam parameter
   [At] [2] [/] [161] [Enter]                                                                  gives a starting address for all the part 3’s

## New Show File

     Patch Exercise - see Appendix 1 (page 42)
        Start a new show, [Displays], File> New> and press [Select]. Or click on
        {Continue without saving}. Are you sure? [OK] or press [Enter].
        Now, go to Appendix 1 – Channel Hookup in the back of the book and patch
        the entire hookup (Ignore Notes/labels).

### CHANNEL/ADDRESS CHECK

           [Live] Press [Format] to be in Summary View
                                                                                                quickly steps through all patched channels at
           [1] [Full] {Chan Check} [Enter] then [Next] … [Next] … [Last] …
                                                                                                100%
            Channel check automatically skips unpatched channels.

                                                                                                same as channel check but with output
           {Address} [1] [Full] [Enter]          then [Next] … [Next] … [Last] …
                                                                                                addresses

           Press [Clear]                                                                        to exit Channel or Address Check mode

### SAVE SHOW

        To save the current show data, navigate within the browser to: File > Save >
        and press [Select]. A green "Success" message should appear when the file
        has finished saving.

### BROWSER COLOR CODING:

### SAVE SHOW FILE WARNING

                                                                                                        Save            Green
            If unsaved data is in the current show file, a save warning will display when you
```text
            attempt to open a new or existing show file.                                                Save As         Green
            The following options will be available:                                                    Open            Red
                 − Save – saves the current show file and opens a new or existing one.                  Merge           Yellow

                 − Save As – saves the current show file to a different location or with                New             Red
```
                   a different name and opens a new or existing show file.
                 − Continue without Saving – opens the new or existing show file
                   without saving any changes to the current show file. Changes will
                   be lost.
                 − Cancel – returns to the current show file without saving changes or
                   opening a different file.

### SAVE AS

To save an existing Eos Family show file to a different location or with a
different name:
   [Displays], {Browser}, File > Save As > Show File Archive > and press                      starts the process to store as a new file
   [Select] or double-click.

   Do you really want to save? [Select] or click {OK}.

You have several formats in which you can save a show file.
    - esf3d includes your show data and your Augment3d model and is only
        compatible withEos versions 3.0.0 and higher.
    - esf2 excludes Augment3d model and is only compatible with Eos
          versions 2.9.0 and higher.
    - esf is a legacy format for compatibility with Eos versions prior to 2.9.0.
   If (untitled), “Enter new show name: Show File” appears above the
   virtual keyboard.

   Press [Label]                                                                              to clear the words “Show File.”

   Type a show name, then [Enter] on either the console or the keyboard.
    When console saves the show, it makes a new copy of the file. Each show file has a date
    and time stamp in the show file name. Always have backup copies!

   In Patch, [1] [Label] Front Light [Enter]                                                  to label a channel

   [Live]                                                                                     notice the * at the end of the filename

An asterisk (*) at the end of a filename indicates unsaved data.

### !! DON’T FORGET TO SAVE AND SAVE OFTEN!

   [Shift]&[Update]                                                                           to do a Quick Save
        Quick Save always saves back to the hard drive. To save to a thumb drive, you will
          need to go back through the Browser to Save As and select the thumb drive.

## Working with Channels

### CHANNELS IN LIVE

         [Live], if you are not already there

         [1] [At] [Full] [Enter]
                                                                                                do not have to retype the channel number if
         [At] [50] [Enter]
                                                                                                changing the same one
         [2] [+] [3] [At] [5] [Enter]                                                           sets level of 50% (use [05] for 5%)

         [4] [At] [05] [Enter]                                                                  use [05] for 5%

          Red data means modified, but not yet stored. Notice “Manual Channels” in upper left
          corner

         [31] [Thru] [50] [-] [34] [-] [35] [At] [65] [Enter]                                   using minus for individual channels

         [59] [Thru] [62] [Full] [Enter]                                                        using Full without [At]

         [55] [Thru] [58] [Full] [Full]                                                         another way to get Full

         [51] [Thru] [54] [Level] (no Enter req’d.) can also do [At] [At]                       user-definable Level – change in Setup

         [51] [Thru] [62] <Enter> level wheel                                                   proportional control if selected

         [8] [At] [50] [Enter] then [+%], [-%]          also [Shift]&[+], [Shift]&[-]           up a point, down a point (10% default)

         [5] [At] [50] [Enter] then [At] [+] [3] [Enter], [At] [-] [4] [Enter]                  add 30 more, subtracts 40

              [At] [/] [50] [Enter] [At] [/] [400] [Enter]                                      takes 50% of level, multiplies by 400%

         [1] [Thru] [35] [Out]                                                                  self-terminating, sets level to zero

         [301] [Thru] [312] [At] [0] [Thru] [Full] [Enter]                                      on cyc, called fanning intensity

              and roll the level wheel to full and then all the way out                         notice proportional control

### SNEAK

      Sneak removes manual data and allows the channels to sneak back to their
      background states, if any. A default Sneak Time can be set.
                                                                                                restores selected channel to background
         [301] [Sneak] [Enter]
                                                                                                state using default sneak fade time
                                                                                                restores all manual levels to background
         [Clear] [Sneak] [Enter]
                                                                                                states

         [1] [Thru] [5] [At] [5] [Sneak] [Enter]                                                brings channels to level in default time

         [6] [At] [75] [Sneak] [3] [Enter]                                                      brings channel to level in 3 secs

         [8] [+] [9] [Full] [Sneak] [Enter]                                                     brings channels to full

         [8] [Out]                                                                              brings channel out – notice red data (hard 0)
                                                                                                brings channels to background state in 0
         [9] [Sneak] [0] [Enter]
                                                                                                secs – removes red manual data (null)

### OFFSET

Offset is a soft key to make custom selections. When pressed, additional
options are accessible on the display and on the softkeys.

   [31] [Thru] [50] {Offset}

   {Even}                                                                             watch preview in the CIA

   [At] [80] [Enter]                                                                  puts all the even channels at a level

   [31] [Thru] [50] [Out]

   [301] [Thru] [312] {Offset} [3] [At] [75] [Enter]                                  selects an offset of every third channel

    Notice the preview of the channel selection in white under the preview graphic.

## Groups

     Groups are a channel selection tool used for quickly recalling specific
     channels. Up to 9,999 groups can be recorded—that’s a lot!
     Note that groups are only a selection and do not contain any intensity or
     non-intensity information.
     When recording groups, channels are stored in the order they are selected.

### RECORDING GROUPS IN LIVE

            [Clear] [Sneak] [Enter]

            [1] [Thru] [10] [Record] [Group] [1] [Enter]                                                   records channels to the target group

            [31] [+] [33] [+] [35] [+] [37] [Record] [Group] [2] [Enter]                                   records the selected channels to group 2

            [31] [Thru] [38] {Offset} {Even} [Record] [Group] [3] [Enter]                                  using offset to achieve the opposite

```text
            [34] [+] [31] [+] [33] [+] [35] [+] [32] [Record] [Group] [30] [Label] Effect 1                records the channels in a specific order and
            [Enter]                                                                                        gives the group a label
```

            After you press [Label], you can press [Effect] or any target button to put that target word
            on the command line.

### WORKING WITH A GROUP

            [Group] [1] [Full] [Enter]                                                                     brings group 1’s channels to Full

            Notice the group order is displayed above the CIA display, on the left side.

            [Group] [1] [At] [20] [Thru] [Full] [Enter]                                                    fanned intensity but in order this time

                                                                                                           accesses the group and then the first
            [Group] [30] [Enter] then press [Next], [Next], [Last], [Last]
                                                                                                           ordered channel in that group
                                                                                                           reselects the whole group and fans intensity
            [Select Last] [At] [10] [Thru] [Full] [Enter]
                                                                                                           across the range
            Pressing [Select Last] multiple times will loop through the last five selections.

### GROUP LIST DISPLAY (BLIND)

        The group list allows viewing and editing of groups. Use [Next] and [Last] to
        navigate within the list or or type [Group] followed by the number then
        [Enter] to jump to a specific group.
            [Group] [Group] or Add-a-Tab (the {+} sign)                                                    opens a list of all groups recorded

### CREATE OR EDIT A GROUP

               [Group] [4] [Enter], [71] [Thru] [82] [Enter], [Label] High Sides – Right
                                                                                                           creates group 4 in the Group List
               [Enter]

               [Group] [2] [Enter]           [+] [39] [Enter]       [-] [39] [Enter]                       adds or deletes channel to a group

               [Group] [1] [Enter]           [11] {Insert Before} [7] [Enter]                              watch softkeys for additional options

               [Clear]       {Reorder} [Enter]                                                             puts the channels back in numeric order

### DELETING GROUPS

            [Delete] [Group] [1] [Enter] [Enter]                            deletes group 1 (2nd enter to confirm)

            [Delete] [Group] [2] [Thru] [3] [Enter] [Enter]                 deletes groups 2 and 3

        Will still have 4 & 30 for later use

Group Exercise - Create the following new groups:
Please label them as well.

        Group #                   Label                Channels

        1                         Frontlight           1 thru 10

        2                         Downlight            31 thru 50

        3                         High Sides – Left    51 thru 62

        4                         High Sides – Right   71 thru 82

        5                         FOH Movers           101 thru 105

        7                         OS Movers – Wash     121 thru 128

        9                         Side – Mids          141 thru 148

        10                        Side – Scrollers     151 thru 158

        20                        Cyc Top              301 thru 312

        21                        Cyc Bottom           351 thru 362

        22                        All Cyc              + G20 + G21

        30                        Effect 1             34, 31, 33, 35, 32

        Group 4 and 30 will already exist.

## Submasters

     Submasters are a type of playback data that can be mapped to a fader. Subs
     can store any parameter from any channel. Current stage content can also
     be recorded directly to a Submaster. Up to 9,999 submasters can be
     recorded.

### RECORD SUBMASTER IN LIVE

            [Live]    [Clear] [Sneak] [Enter]

            [1] [Thru] [9] [Full] [Enter]                                                  set levels

            [Record] [Sub] [1] [Enter], then press [Load] for the top left fader
                                                                                           records the current stage state to sub 1
               On Ion Xe, press both buttons ( & ■) to load a fader

            [Sub] [1] [Label] Fronts [Enter]                                               displayed on LCD

            [Clear] [Sneak] [Enter]

            [51] [Thru] [53] [At] [4] [Enter],
            [54] [Thru] [56] [At] [7] [Enter],
            [57] [Thru] [59] [At] [Full] [Enter]

```text
            [Record], then [Load] the next fader, [Enter]                                  loads the fader with the submaster; note
               Can also press [Record] and double hit [Load]                               that we did not specify Sub

            [Clear] [Sneak] [Enter]                                                        to remove the manual data
```

            Submasters may be loaded to any fader if it is blank or clear.

            Run each fader up and down.                                                    look at proportional values of Sub 2

            Channel color is pale yellow as it is fading up and bright yellow when Full.

### RECORD SUBMASTER IN BLIND

        Edits done in Blind happen Live if the Sub is on.
            [Blind]     [Sub] [31] [Enter]                                                 creates sub 31 – in Blind
                                                                                           records values to sub 31 – in Blind; no need
            [71] [Thru] [79] [Full] [Enter],         [At] [75] [Enter]                     to re-specify channels; remember that all
                                                                                           changes are immediately saved

### COMMAND LINE CONTROL OF SUBMASTERS

                                                                                           brings contents of sub to 50% of their
            [Live]      [Sub] [31] [At] [50] [Enter]
                                                                                           recorded values and in yellow (sub)
            [Sub] [31] [At] [85] [Sneak] [Enter]                                           will sneak sub up in default sneak time
                                                                                           takes sub out regardless of fader position.
            [Sub] [31] [Out] [Enter]
                                                                                           [Enter] is required to confirm this action.

### CHANGE FADER PAGES

The Fader pages are set up in increments of 10. The page number is visible
below the Cue list on the left side under the word “Master”.

   Hold [Fader Page] & press [3]* and then release [Fader Page]                              advances to a specific page

   [Sub] [31] [Load] to the first fader on page 3
                                                                                             loads sub 31 on a fader on page 3
   Bring up the fader

   Press and hold [Shift] and tap [Fader Page]                                               reverses one page at a time
                                                                                             Shows direction fader must go to reset to
   Go to Page 1 – Notice the arrow in the LCD
                                                                                             current page status
    Motorized faders will reset automatically to current page status.

   Press and hold [Fader Page] and scroll the rate wheel                                     increases or decreases pages

### UNLOAD FADERS

If a submaster (or a cue list) already occupies the fader, that fader must be
cleared before another submaster or cue can be loaded.
   Press and hold [Fader Page] and press [3]                                                 to go back to page 3 (sub 31)

   Hold [Shift] and press [Load] of the fader                                                to clear sub 31, does not delete the sub

### DELETE SUBMASTERS

   [Delete] [Sub] [31] [Enter] [Enter]                                                       deletes sub 31

   [Delete] [Sub] [1] [Thru] [Enter]         Do not hit [Enter] again.                       deletes all subs    [Undo] if you do!

   [Shift]&[Clear]                                                                           will clear the command line

   [Shift]&[Fader Page]                                                                      to go back to page 1

    If you delete the subs, you will need to recreate subs for the next exercises. Or use
    [Undo] [Enter].

### APEX

On the Apex consoles, 5, 10, or 20 motorized faders are provided.
You will use the [+] [-] buttons to the left of the Master Fader Pair to change
fader pages:
                                                                                             advances to page 3 - the only way to get to a
   Hold [+] & press [3] and then release [+]
                                                                                             blank page
   Hold [-] & press [1] and then release [-]                                                 reverts to page 1

    Remember the faders are motorized so they will move automatically as you change pages.

## Cues

     Cues are single lighting looks that are stored in a list and often played back
     in order. Up to 9,999 cues can be recorded. There are various timing and
     transition options that affect how cues are played back.

### RECORD A CUE

            [Live], [Clear] [Sneak] [Enter] and bring any subs/faders down

            [Group] [2] [At] [30] [Enter],      [8] [At] [35] [Enter]                            set levels for specials

            [Record] [Cue] [1] [Enter]                                                           stores cue 1 – note channels turn blue

            [2] [+] [5] [+] [6] [At] [35] [Enter]                                                adds additional lights to look
                                                                                                 stores cue 2 – note channels colors; note we
            [Record] [2] [Enter]
                                                                                                 did not specify cue
            [2] [+] [6] [Out], [Group] [2] [At] [60] [Enter]
                                                                                                 levels going up and down in cue
            [31] [+] [32] [+] [36] [+] [37] [+] [41] [+] [42] [+] [46] [+] [47] [Out]

            [Record] [3] [Enter]                                                                 all content will be recorded in cue 3

            Run the first fader (with sub 1) up to 75%
                                                                                                 stores next cue (4) – note channels colors
            [Record] [Next] [Enter] *                                                            adds the sub values into the cue, sub values
                                                                                                 cannot be removed with fader
            Bring the first fader back down

            [1] [Thru] [9] [Out],     [8] [At] [50] [Enter]

            [Record] [Next] [Enter]                                                              stores next cue (5)
             * When you use [Record] [Next], remember what cue number your command line is on.
               If Cue 1, then Next = 2. If Cue 2.7, then Next = 2.8. If Cue 2.11, then 2.12.

### RECORD CUES WITH TIME

            [Select Last] [Out],
                                                                                                 selects channels that had been used
            [Group] [2] [At] [80] [Enter],       [Group] [10] [At] [30] [Enter]
             Remember: pressing [Select Last] multiple times loops through the last five
             selections.

            [Record] [6] [Time] [3] [Enter]                                                      stores cue 6 with 3 second up/down time

            [151] [Thru] [154] [Full] [Rem Dim] [Enter]                                          set levels using [Remainder Dim]

            [Record] [Next] [Time] [2] [Time] [7] [Enter]                                        specifies split up and down times (7)

            [36] [Thru] [50] [At] [50] [Rem Dim] [Enter]                                         set levels

            [Record] [8] [Time] [6] [/] [2] [Enter]                                              specifies split up/down time with slash (8)

### RECORD WITH TIME AND LABEL

       [32] [Thru] [34] [At] [50] [Enter], [33] [+%] [+%] [+%]
                                                                                                  set levels
       [41] [Thru] [50] [At] [25] [Enter], [3] [Full] [Full]

       [Record] [Next] [Time] [3] [/] [5] [Label] Speech [Enter]                                  stores cue, timing, and label (9)

       [Select Active]* [Out]                                                                     takes all active channels’ intensities out

       [Record] [10] [Time] [0] [Label] Blackout [Enter]                                          stores cue, timing, and label (10)

       [1] [+] [3] [+] [6] [Full] [Enter], [Group] [2] [At] [25] [Enter]                          sets levels for new cue after blackout

       [Record] [11] [Time] [2] [Label] Entrance [Enter]                                          stores cue, timing, and label (11)

       [10] [Full] [Enter]                                                                        sets levels for new cue

       [Record] [11] [.] [5] [Enter]                                                              stores a point cue
            * For Ion Classic users, Select Active and Select Manual are both softkeys when you
              hold [Shift] & press [Select Last].

### DELETE CUES

       [Delete] [Cue] [11] [.] [5] [Enter] [Enter]                                                deletes a cue, does not renumber

        Notice Cue 11.5 is still on stage although it was just deleted. The console is still
        outputting the last DMX levels.

       [Go To Cue] [Enter]                                                                        to refresh current state of the cue list

        Refreshes the DMX output of the console.

## Playback

### PLAYBACK STATUS DISPLAY (PSD OR CUE LIST)

PSD is a tab that displays a list of the cues, their timing and additional
information associated with the cues.
      Use the triangle (▽) far right                                                              to collapse the CIA for more room

      Touch/click the screen or press [Tab] until it is selected.                                 to make sure the PSD Tab is highlighted.

        - [Format] – for selecting display options:
             − Two cue lists
             − A preview of the first 10 pages of 10 faders
             − Back to default single cue list with a fader ribbon
        - [Page▲] or [Page▼] – scrolls the cue list up and down a full page
             − If in another tab, [Shift]&[Page▲] or [Page▼] will page up and
               down in the PSD without needing to focus on that tab
        - [Next] or [Last] – moves up and down through the cue list
             − In Blind, [Next] and [Last] navigate through the cues on the PSD.
               The PSD indicates the current selected cue. This has no effect on
               live output.

### BASIC CUE PLAYBACK

                                                                                                      resets the cue list to the top, clears stage,
            [Live], [Go To Cue] [Out] [Enter]
                                                                                                      and puts Cue 1 in pending
            Press [] (Go) on the Master Playback Fader pair                                          executes the pending cue (1)

        While a cue is running, both the cue line and the current cue display is red;
        when it is complete, both turn gold.
            Press [] (Go) again to go into cue 2…                                                    executes the next cue (2)
                                                                                                      fader activity is instantly paused mid-
              Then press [] (Stop/Back) while the cue is running
                                                                                                      transition
            Press [] (Go) to continue into cue 2                                                     resumes the current cue

            Press [] (Go) again to go into cue 3…                                                    executes the next cue (3)
                                                                                                      fader activity is instantly paused mid-
              Then press [] (Stop/Back) while the cue is running
                                                                                                      transition
                                                                                                      if cue paused or already complete, will play
            Press [] (Stop/Back) again to back up into cue 2
                                                                                                      the previous cue

        [] (Back) uses default Back time established in Setup. It does not use the
        timing of the cue.
            When in a completed cue, (Cue 2), press [] (Stop/Back)                                   goes back to cue 1 in the Back time

### QUICK TIME/TIMING DISABLED

                                                                                                      QuickTime - easily goes from cue to cue with
            Hold [Shift] and press [] (Go), [] (Go), [] (Go)
                                                                                                      no timing
            Hold [Shift] and press [] (Stop/Back), [] (Stop/Back)…                                  reverse cue to cue with no timing

            Hold [Timing Disable] and press [] (Stop/Back) or [] (Go)                               Same as holding Shift

### CONTROLLING PLAYBACK MANUALLY

        To manually take control of the intensity fade from the beginning of the cue,
        set the main sliders at the bottom of the run before you press [] (Go).

        Notice a red ‘Man’ in the Duration column of the PSD and in the Master Playback status bar.

        Raise the faders in the timing you desire.
        The main slider are a split crossfader pair. The left fader controls the intensity
        upfade, while the right fader controls all intensity downfade actions.

### AS A GENERAL RULE, IT IS GOOD TO MAKE SURE THAT YOUR MAIN FADER PAIR

### IS UP AT THE BEGINNING OF A SHOW.

### GO TO CUE

   [Go To Cue] uses Go-To-Cue timing established in Setup.
                                                                                         sets all values to home and resets all cue
      [Go To Cue] [Out] [Enter]
                                                                                         lists active on faders to top of the list
                                                                                         sets all current intensity values to zero, and
      [Go To Cue] [0] [Enter]                                                            resets the current cue list to top of ist,
                                                                                         without affecting non-intensity parameters

### OTHER GO TO CUE FUNCTIONS

             [Go To Cue] [Enter]                                                         refreshes current cue
                                                                                         takes you to the next or previous cue in the
             [Go To Cue] [Next] or [Last] [Enter]
                                                                                         active list (like Back)
                                                                                         all parameters with values in cue 5 fade to
             [Go To Cue] [5] [Enter]                                                     those values, even if they are tracked, in the
                                                                                         Go To Cue time
             [Go To Cue] [6] [Time] [Enter]                                              fades to cue in the timing of the cue

             [Go To Cue] [1] [Time] [2] [Enter]                                          fades to cue in 2 seconds

### LOAD A CUE ON THE MASTER PLAYBACK FADER

                                                                                         loads a specific cue to the main faders and
      [Cue] [7] [Master] (Load) *         and then press [] (Go)
                                                                                         then runs in that cue’s time
       * Look at the Pending Cue in the PSD.

### CHANNEL DISPLAY COLOR CONVENTIONS

     [Format] to be in Live Summary View

     [Go To Cue] [9] [Enter]                                                             Go to a cue

     [1] [Thru] [5] [Full] [Full],   [39] [Thru] [42] [At] [80] [Enter]                  Adds manual values

### CHANNEL OR PARAMETER LEVELS

       - Red Manual Data – has been changed but has not been saved
       - Blue          Movement – channel values are higher than in the
             previous cue. Non-intensity parameters (NPs) are blue when any move              “GREEN, GRASS…BLUE, SKY!”
             instruction has occurred.
       - Green        Movement – channel values have gone down from their
             previous level. Also used in reference marking to indicate a channel is
             marked.
       - Magenta      Tracking – value is unchanged from the previous cue
             (tracked) – not given a new move instruction.
     Bring up Sub 1

       - Yellow        Values set by a submaster. Bright at full, paler at lower
             levels
       - White         Values are blocked.

### CHANNEL NUMBERS/CHANNEL HEADERS                           CHANNEL OR PARAMETER LEVELS

```text
    White number – regular channel patched                      Red – Manual Data
    Bright White number – parked channel (small p)              Blue – Level is increasing from previous cue
    Gray number – unpatched channel                             Magenta – Level is tracked from previous cue
    Gray number with no outline – deleted channel               Green – Level is decreasing from previous cue.
    Gold number – channel is captured                           Orange – Level is owned by live playback
    Gold outline – Selected channel                             White – Level is blocked
```
                                                                Yellow – Level is set by Submaster
                                                                Pink – Override Data

     Don’t forget to bring Sub 1 down.

## Track/Cue Only

Eos is a move-fade console, meaning that only changes to channel levels are
```text
recorded. Another way to say this is that channels will stay at a given level            Check out the Bobblehead Fred video that
until they are given another move instruction. Unchanged levels will be                  helps to explain the difference in style of
tracked through cues until given a new level. When playing cues out of                   operation between tracking and preset
```
                                                                                         consoles and their origins.
sequence, Eos will play back moves and tracked levels guaranteeing the
correct stage look.
It is important to learn the rules of tracking when editing cues and recording
cues out of sequence. When editing cues with tracking, changes to a level
will propagate forward through a cue list until a move instruction or a block
is encountered. When editing cues with cue only, only the level changes in
the specific cue will change. The console may add move instructions into the
next cue to preserve the intended look.
  Go to [Blind], and press [Format]                                                   to go into Spreadsheet view

### TRACK

                                                                                      adds channel to cue 1 and tracks it
        [Cue] [1] [Enter]       [11] [At] [80] [Enter]                                through the entire cue list, including the
                                                                                      blackout cue

### CUE ONLY

                                                                                      adds channel to cue and inserts a move to
        [12] [At] [40] [Q Only/Track] [Enter]
                                                                                      restore it to zero in next cue
                                                                                      creates a move in first cue, tracks through
        [Cue] [1] [Thru] [5] [Enter]    [12] [At] [40] [Q Only/Track] [Enter]         and adds a move to zero after last cue
                                                                                      selected
                                                                                      creates a new cue, all channels track
        [Cue] [11] [.] [5] [Enter] [Enter]
                                                                                      through, note chan. 11 tracks through

### BLOCK

    A block is an editing tool that prevents changes from tracking into or beyond a
    block. Blocks can be applied at a cue level, a channel level or a parameter
    level. It will not affect the contents of the cue.
        [Cue] [10] [Block] [Enter]     Channel 11 is white (channel blocked)          applies a block to the blackout cue
                                                                                      adds channel to cue 1 and tracks it till it
        [Cue] [1] [Enter]      [13] [At] [80] [Enter]
                                                                                      reaches the block in cue 10
                                                                                      assures any lights on are set to zero as this
        [Cue] [10] [Enter]       [Select Active] [Out]                                is our blackout cue – this change will track
                                                                                      forward

    “B” is displayed in the flags field of the PSD, indicating a cue level block.

### AUTOBLOCK

     Autoblock protects your cue data in the case of a redundant level change.
        Notice in Cue 2 that channel 2 is at 35

        [Cue] [1] [Enter]           [2] [At] [35] [Enter]                                      Autoblock created in cue 2

     Now in Cue 2, the intensity level for channel 2 is displayed in white, with an
     underscore. This is the Autoblock, where the console is preserving the idea
     that this channel already has a move instruction.
                                                                                               Autoblock turns back into a move
        [2] [At] [55] [Enter]
                                                                                               instruction

        [2] [At] [35] [Enter]                                                                  puts the Autoblock back

     Autoblocks are displayed in the PSD by a “b”.

### CLEAR AN AUTOBLOCK

     If you want to remove the underlying move instruction:
        [Cue] [2] [Enter]           {AutoBlock Clean} [Enter] [Enter]                          clears an autoblock

         {Autoblock Clean} removes all auto-blocks from a single cue, cue range or cue list.

### ASSERT

     Assert is a playback condition that collects unfinished fades and puts the
     entire look of the current cue on stage. Assert is a way to regain ownership of
     a channel, or to force a new move command using the timing of that cue.
     Asserts can be placed at a cue level, channel or parameter level.
        [Live]     [Go To Cue] [9] [Enter]

        [41] [Full] [Rem Dim] [Enter]                                                          set levels

        [Record] [9.5] [Time] [20] [Enter]                                                     stores cue with long fade time

        [Go To Cue] [9] [Enter]           [] (Go) to run Cue 9.5

           [] (Go) on cue 10 before cue 9.5 has completed…                                    discuss what happens

        [Cue] [10] [Assert] [Enter]                                                            applies an Assert on the cue

         Notice an “A” in the PSD flag field for Cue 10.

           [Go To Cue] [9] [Enter]          [] (Go) on cue 9.5

           then [] (Go) on cue 10                                                             discuss what happens

     Assert plays back all values as move instructions. It collects unfinished fades
     and executes them in the time of the cue.

### IT IS GOOD PRACTICE TO HAVE BLOCK AND ASSERT ON ALL BLACKOUTS, FADES

### TO BLACK, AND CRITICAL CUES.

## Non-Intensity Parameter Control

### PARAMETER CONTROL (IFCB)

### FOUR MAJOR PARAMETER CATEGORIES (IFCB):

      - I = Intensity . . . Intensity
      - F = Focus . . . Pan and Tilt, changes to the position (X, Y or Z)
      - C = Color. . . All color parameters (Scrollers, RGB, CMY, CTO, CTB…)
      - B = Beam . . . All other parameters, divided into sub-categories:
          − Form – includes parameters that affect the quality or size of the
            light output, such as edge, zoom, iris, frost, etc.
          − Image – includes anything that drops into the gate and interrupts
            the beam of light, such as gobos, effects wheels, prisms, etc.
          − Shutter – includes all the framing parameters

### LAMP CONTROLS

  Lamp controls allow you to execute control functions of selected fixtures such
  as calibrate, douse lamp, strike lamp, and reset. Each fixture type has its own
  set of lamp control options which are available to you when you select the
  fixture from Live.
      [Clear] [Sneak] [Enter]     [Group] [5] [Enter]   [About]                        channel selection on command line

      {Lamp Controls} on the left side of the About screen

      [Group] [7] [Enter]                                                              note different lamp controls

      [About] again                                                                    will clear the About display

### COLOR CONTROLS

### COLOR CONTROL WITH SCROLLERS

     [Encoder Display]

     [Group] [10] [Full] [Full]

      - Press [Color] and then use the encoder to dial to the frame desired
      - By default, the scroller is expanded to see the individual frames
      - Hold [Shift] and dial the encoder – see the ‘+’ and ‘–’ for half frames
      - Press {Home } to take the scroller back to its starting frame

### TO GO TO A SPECIFIC FRAME USING THE COMMAND LINE

          − Tap the word ‘Scroller’ in the encoder display,
          − Use {Scroller} in the CIA parameter tiles
          − Press the button in the center of the encoder
          − Then press [8] [Enter] for frame 8.

### COLOR CONTROL WITH LEDS

        Press [Encoder Display] if not open already

        [Clear] [Sneak] [Enter]         [Group] [3] [+] [Group] [4] [Full] [Enter]             notice all colors at 100%

        Dial the encoders                                                                      easy to use two hands for color mixing

        In Red, press {Min}; Lime {Min}, Green {Min}, Blue, press {Max}                        leaves just blue

        Tap the ‘Red’ label on the touchscreen, then [Full] [Enter]                            adds 100% of red

        Press the button in the center of ‘Red’ encoder, [75] [Enter]                          back to 75% red
         Keep in mind if you have the classic encoders, the entire encoder is the button.

        Press [Displays], then tap ‘Red’ tile in CIA, [50] [Enter]                             now magenta wash
         The Parameter tiles in the CIA remap based on the channel or fixture type selected.

### COLOR PICKER

         Click on Add-a-Tab (the {+} sign) , select Color Picker Control

     When first opened, the color picker breaks down into three areas: the CIE XY
     color space, the gel library, and then, when you select a gel library, it shows all
     of the gel swatches.
          - The console will put fixture in the color as close as possible.
         - A ‘G’ will appear in the channel display that means gel match
         - Gel matches can be set from the command line also

        [Group] [3] [+] [Group] [4] [Home] [Enter]                                             notice all colors at 100%

        Tap {3 Lee}, then find {L116} - a blue-green                                           watch change color

        Tap {5 Rosco}, then find {R021} – an orange                                            watch change color
                                                                                               first # being the Gel library and second #
        [Select Last] [Shift] & [Color] [5] [/] [381] [Enter] – a blue
                                                                                               being the gel number
                                                                                               use “At” instead of “Color” – works
        [At] [3] [/] [345] [Enter] – magenta
                                                                                               anywhere in Live

        Tap {Standard Colors},           then find {Red}

        Tap {Purple 75%}

        Tap {3500K}*
         * K stands for Kelvin – measurement of Color Temperature – low Kelvin values are
           warmer whites, higher Kelvin values are cooler whites

### CONTROLLING A MOVER

                                                                                                           Tilt first! Then Pan.

### FOCUS

      Press [Encoder Display] if not open already

      [Clear] [Sneak] [Enter]

      [Group] [5] [Full] [Enter] , then [Focus] and play with encoders                              notice all five fixtures move as a group

      Hold [Shift] while using the encoders                                                         puts the encoder in Fine mode

      Press [Next], Tilt, [Next], Tilt, [Next], Tilt, aiming on Singer CS                           able to work with each light individually

      [Select Last] to reselect group and then Pan                                                  now back as a group

### FLIP

       To access {Flip}, press on the 3 vertical dots on the left. Flip will spin the unit to its
       exact same position, but from the other orientation (long path versus short path).

              [103] [Full] [RemDim] [Enter]                                                         selects one fixture

              Press {Flip} on Pan encoder                                                           and watch the fixture reset

              Press {Flip} again                                                                    and watch the fixture reset back
           Flip results in a manual value. Do not forget to update if in a cue!

### HOME

                                                                                                    returns parameter to 50/50 or Home
              Under Tilt, press {Home}
                                                                                                    position

### ALWAYS ANOTHER WAY TO DO THINGS

              Tap the encoder label on the touchscreen, {Tilt} [-50] [Enter]                        places the Tilt parameter at -50°

              [Displays], press the {Tilt} parameter tile, [Home] [Enter]                           … or homes the tilt parameter

### BEAM

   Remember: Beam divided into sub-categories: Form, Image, and Shutter
      [Clear] [Sneak] [Enter]

      [Group] [5] [Full] [Full] and tilt up on stage floor

      Make sure that [Encoder Display] is enabled

       [FORM] - ZOOM
              − Use the Zoom encoder
              − Use the touchscreen buttons: {Min}, {Max}
              − Tap the Zoom label on the touchscreen, [35] [Enter]
                 Note: Zoom is in degrees. Look at the display.
              − Notice Shutter Strobe – frames and modes are displayed above
       [IMAGE] - GOBO SELECT
              − Press the 3 vertical dots to see the thumbnail images of the gobos
                (blue is expanded, white is not)
              − Use the Gobo Select encoder, default is indexed mode
              − Tap the Gobo Select label on the touchscreen, use the encoder
                button or press the CIA Parameter tile, {Gobo Select} [3] [Enter]
                (Fracture)
       [FORM] - EDGE
              − Use the Edge encoder to make the gobo sharp

         [IMAGE] – GOBO INDEX/SPEED
             − Default is in Index Mode – statically rotate the gobo
             − Press the 3 vertical dots to see the mode option or press {Mode}
               to step through the modes for the parameter such as index, rotate
               +/-- or special effects.
              − Encoder controls the speed of the gobo based on the mode
                selected
            [Select Last] [Shift]&[Image] [Image] [Home] [Enter]                               removes the beam attributes
            To put Beam on the command line, hold [Shift] and double hit any Beam sub-
               category (Form, Image, or Shutter).
         [SHUTTER]
             − Use the shutter encoders for Thrust and Angle                                   Shutters are mapped based on Shutter Order
                - Roll Thrust A in a bit                                                      in Patch Attributes, first page: A & C
                                                                                               opposite pairs, second page: B & D
                - Tap the label and specify specific angle, {Angle} [30] [Enter]
                - Use the touchscreen buttons: {Home}, {Min}, {Max}
             − Touch the shutter graphic,           , to open a tool to use touchscreen
               controls
                - Angle Home – sets the angle of all shutters to their home position
                - Thrust Home – sets the thrust of all shutters to their home position
                - Pair All – pairs all the shutters together so they move together*
                                                                                                 * These pairings work with the encoders,
                - Pair AC – pairs the A and C shutters together so they move together*            not with graphic controls on the display
                - Pair BD – pairs the B and D shutters together so they move together*
                - Inverse AC – pairs A and C so they move in opposite directions
                - Exceed Limits – ignores the limits angle and thrust place on each other,
                   prioritizing the selected, regardless of the impact on the other
                - Inverse BD – pairs B and D so they move in opposite directions
                - A>D – switches to custom encoder pages - thrust all on one page, angle on
                   one page
             − Frame Assembly (3rd page) allows for rotation of the whole shutter
               assembly

### PAGING ENCODERS

                                                                                               takes you to third page of shutter category –
       [Shutter], [Shutter], [Shutter]       or    [Shutter] & [3]
                                                                                               see Frame Assembly Encoder
         Page number is displayed using dots in the category on the left side of the display

### HOME

     [Home] or {Home} returns the selected target or its individual parameters to
     their default position. The icon is in the Encoder Display and in ML Controls.
         [Clear] [Sneak] [Enter]

         [Group] [5] [Full] [Enter], tilt up on cyc, in orange, with gobo, zoom out,
                                                                                               set levels
         and make it sharp

         [101] [Home] [Enter]                                                                  homes all non-intensity data for channel

         [102] [Shift]&[Focus] [Home] [Enter]                                                  homes just the focus data for channel

         [103] [Shift]&[Form] [Home] [Enter]                                                   homes just the sub-category form (zoom)

         [104] {Gobo Select} [Home] [Enter]                                                    homes just the gobo for channel

### APEX MAIN ENCODERS

    On Apex consoles there is an expanded encoder area with four main encoders
    and two dedicated pan and tilt encoders – and those are all haptic as before.
    You’ll also notice that we have new navigation buttons above the screen and
    that includes a Custom key that is actually a hard key instead of just being a
    soft key on the touchscreen.

### MINI ENCODERS

    Apex consoles also offer nine RGB-backlit mini encoders to the left of the
    encoder touchscreen. Eight of the mini encoders can be fully configured for
    expanded control of the large encoder parameters or can have custom
    independent mapping. The bottom encoder is dedicated to mini encoder
    paging and configuration.
                                                                                      see 2 options in the bottom center of
     Push down on bottom mini encoder
                                                                                      screen
     Select {Extended}

     Push down on same mini encoder                                                   to exit configuration mode

    Extended mode - an extension of the main encoders. If the main encoders are
    on Page 1 of a parameter, then the mini encoders show page 2 and page 3 of
    the same parameter.
    Navigate between different categories, and see the mini encoders track with
    the main encoders.
    Independent mode - ability to change the mini encoder category separately
    from the main encoders. Main encoders can be in Color and Mini Encoders
    can be in Image.
     Push mini encoder, select {Independent}

     Turn or rotate the bottom mini encoder                                          to page through the mini encoder categories

     Push down on same mini encoder                                                  to exit configuration mode

     [101] [Enter] [Color]

     Press on {Expand} (three vertical dots) next to Yellow                          to see Min, Max, and Home

     [Image],   press on {Expand} next to Gobo Select                                to see gobo frames and modes

     Press on {Expand} again                                                         to collapse the parameter

`

### ML CONTROLS

     There is always another way of doing things!
        [Clear] [Sneak] [Enter]

        Click on Add-a-Tab (the {+} sign) , select ML Controls

     Navigation and Operation Features

             - Category shortcut keys on the left side to quickly access those controls
             - Category and Parameter buttons will post to the command line
             - Buttons to collapse or expand categories for yet more flexibility
             - Home buttons allow you to reset a specific parameter or attribute of a
                 parameter to its default setting.
             - Virtual encoders - Click and hold close to the center line for slow
                 movement, further away for faster movement or hover cursor over
                 the encoder and use the mouse scroll wheel.
             - Color picker and gel picker
             - Scroll bar – multiple rows of parameters will now display, and you can
                 scroll either horizontally or vertically depending on the frame
        The parameters displayed will change based on the device(s) selected.
         [1] [Enter]                                                                        shows just the intensity wheel
                                                                                            shows intensity and color – note scroller,
         [151] [Enter]
                                                                                            gel picker
                                                                                            shows intensity and color – note RGB&L
         [51] [Enter]
                                                                                            wheels
         [101] [Enter]                                                                      shows intensity, focus, color, and beam

### ML CONTROL POPUP

            Click on the shortcut in the upper right hand side of the monitor.              to open the ML popup window

             Scroll bar along the bottom or use the category shortcut keys.
             To close, simply touch or click anywhere off of the popup.

## Additional Cue Features

### CUE DELAY

 Delay is a timing modifier that can be placed on cues which causes them to
 wait a specified time before beginning the fade.
   [Go To Cue] [6] [Enter]

   [2] [+] [4] [+] [10] [Full] [Full]
                                                                                                       set levels
   [Group] [20] [Full] [Enter], make them pink

   [Record] [21] [Label] Pink Cyc [Enter]                                                              records the cue (21)

   [Group] [1] [-] [4] [Out],         [Group] [10] [Out]                                               set levels

   [Record] [Next] [Delay] [3] [Enter]                                                                 records cue with a delay (22)

     In the PSD, on cue 22, notice the small 3 in front of the cue time. Also notice the duration is
     8 - the total of the delay and the cue time.

                                                                                                       watch for delay countdown and then the 5
   [Go To Cue] [21] [Enter] and press [] (Go)
                                                                                                       second cue countdown

   [Group] [10] [At] [50] [Enter]            [Group] [1] [Out]                                         set levels
                                                                                                       records cue with a delay on both the up and
   [Record] [22] [.] [5] [Time] [2] [Delay] [3] [/] [5] [Enter]
                                                                                                       down times (22.5)

     Again, notice in the PSD, the small 3 and 5 in front of the cue up and down times. Also
     notice the duration is 7.

   [Group] [10] [Out], [8] [At] [50] [Enter], [Group] [2] [At] [8] [Enter]                             set levels

   [Group] [20] [Enter], make them blue                                                                select the cyc and make them blue
                                                                                                       records cue with an overall time and a color
   [Record] [23] [Time] [3] [/] [1] {Color} [Delay] [4] [Enter]
                                                                                                       delay (23)

     Again, the small 4 in front of the color time.

                                                                                                       watch the delays on both the up and down
   [Go To Cue] [22] [Enter] and press [] (Go) on 22.5
                                                                                                       fades

   Press [] (Go) to go into Cue 23                                                                    watch the delay on just the color

### CUE FOLLOW/HANG (AUTO-FOLLOWS)

     An Autofollow is when one cue automatically activates the next cue. This can
     be achieved by assigning a Follow or a Hang to the cue that will initiate the
     trigger of the next cue in a specified time.
     Follow time begins the moment the cue is executed (when the go button is
     pressed.) Hang is similar but doesn’t start till the cue is complete.
     {Fw/Hg} is a soft key; can also press [Shift]&[Delay] to access Follow and
     [Shift]&[Delay][Delay] to access Hang

       [Cue] [4] [Thru] [6] [Time] [2] [Enter]                                                        changes timing for faster playback

       [Cue] [4] { Fw/Hg } [3] [Enter]                                                                records cue with a follow time of 3 seconds

         Notice the F3 in the PSD to show you follow/hang cues, as well as the > in front of cue 5.

       [Go To Cue] [3] [Enter] and press [] (Go)                                                     watch the cue

       [Cue] [5] [Shift]&[Delay] [5] [Enter]                                                          records cue with a follow time of 5 seconds

       [Cue] [6] [Shift]&[Delay] [Delay] [3] [Enter]                                                  records cue with a hang time of 3 seconds

       [Go To Cue] [3] [Enter] and press [] (Go)                                                     watch the cues play

     To remove follow and hang times, simply type [Cue] [#] {Fw/Hg} [Enter]

### CUE LINK

     Link allows cues to be run out-of-sequence.
       [Cue] [3] {Link/Loop} [7] [Enter]                                                              links to cue 7 from cue 3

       [Go To Cue] [1] [Enter] and press [] (Go)                                                     go into Cue 2

       Press [] (Go)                                                                                 go into Cue 3
                                                                                                      go into Cue 7 (the link causes the cue list to
       Press [] (Go)
                                                                                                      skip over 4, 5, and 6)

       [Cue] [3] {Link/Loop} [Enter]                                                                  to remove link

## Update

Update is a ‘save changes’ tool. It only pertains to values that are red or
modified – values that have been changed. Update saves manual changes
back to targets such as cues, palettes, presets and submasters.

### UPDATE DEFAULT

        [Live]    [Go To Cue] [2] [Enter]                                           Look at channels 10 and 31-50

        [10] [At] [50] [Enter]                                                      makes a change to an existing cue

        [Group] [2] [Full] [Enter], make light blue

        [Update]       Notice default Make Absolute style                [Enter]    change is now stored in cue

        [Blind]    Spreadsheet view

        [10] [Enter]                                                                to clearly see channel 10

        See how channel 10 turns on in cue 2 and is tracked till the block

        [Group] [2] [Enter]                                                         notice color values track just like intensities
            To see Color Information, hold [Data] and press [{Color}] – a toggle.

### UPDATE CUE ONLY

        [Live] [51] [At] [75] [Enter]                                               makes another change in the cue

        [Update] [Cue Only] [Enter]                                                 records without tracking

        [Blind]    Spreadsheet view                                                 note changes for channel

        [51] [Enter]

         See how channel 51 turns on in cue 2 and turns off in cue 3.

### MOVE INSTRUCTIONS

    Other move instructions will stop values from tracking through.
           See how channels 3 and 4 turn on to 75% in cue 4                         note the move instruction in cue 4

        [Live], still in Cue 2, [3] [+] [4] [At] [40] [Enter]                       makes another change in the cue

        [Update] [Enter]                                                            records allowing tracking

        [Blind]                                                                     note changes for channels 3 and 4

         See how 3 & 4 turn on in cue 2 and move to 75% in cue 4                    where 75 is still a move instruction

    In Blind, remember that changes are stored immediately. In Live, Update is
    the tool that we use to store information into existing targets such as cues.

## Park

     Park locks the value of a channel or address.
     - It cannot be changed by any console operation, including subs,
         playbacks, Grandmaster or Blackout key.
     - Parked values will not be recorded.
     - You can park channels, addresses, categories, and parameters

### PARK IN LIVE

         [Live]

         [4] [+] [6] [At] [50] [Park] [Enter]                                parks channel at 50%

        Park button is now lit green.
        Any parked channel has a small “P” visible on the channel icon.
        Notice in the upper right corner of the display “Parked Channels.”

                                                                             still shows cue values even though the
         [Go To Cue] [9] [Enter]
                                                                             park value is being output

         [127] [Park] [Enter]                                                parks all parameters at current levels
                                                                             parks the color of the channel at its
         [121] [Shift]&[Color] [Park] [Enter]
                                                                             current level

         [Address] [5] [At] [75] [Park] [Enter]                              parks address at 75%

         [Go To Cue] [Out] [Enter]                                           parked values stay

        Notice the top of the display now say “Parked Channels/Addresses.”

### TO CLEAR PARKED VALUES IN LIVE:

            In Live, [4] [Park] [Enter] …[Enter]                             unparks channel

            [Clear] [Park] [Enter] …[Enter]                                  unparks all parked channels

            [Address/Patch] [Park] [Enter] …[Enter]                          unparks all parked addresses

### PARK DISPLAY (BLIND)

        [Park] [Park] or Add-a-Tab (the {+} sign)                            opens the Park display

        [2] [At] [85] [Enter]                                                parks channel at 85%
                                                                             parks address at 75% - shows chan and
        [Address/Patch] [34] [At] [75] [Enter]
                                                                             parameter

        Notice the Park key is not necessary for parking in Blind.
        [Format] will change to Table view in Park to see parameters.

### TO CLEAR PARKED VALUES IN BLIND:

            [2] [At] [Enter]                                                 unparks channel

            [Clear]                                                          removes the channel icon

            {Address} [34] [At] [Enter]                                      unparks an address

## Setup

[Displays] {Setup} or click in Browser > Setup. The three areas are:
- System – effects all users and devices and how the show functions
- User – specific to a user
- Device – specific to a device or piece of hardware

### SYSTEM – ALL DEVICES IN SYSTEM – STORED IN SHOW FILE

   These settings are shared on all consoles and users on the network.
       - System          Number of Channels, Dimmer Doubler Offset, Create
           Virtual HSB, Display Colors in D65, Zones, Home Preset, Preheat
           Preset, Metric/Imperial, Startup, Shutdown and Disconnect Macros
       - Session     Backups: Auto Take Control, Use Higher Priority (sACN),
           Expansion Processing Hold Last Look, FDX Settings, Push Pixel Map
           Archive
       - Cue Settings Auto-Mark Enable, Mark Time, Preheat Time, Cue Default
           Times
       - Show Control          Tabs for SMPTE, MIDI, OSC, UDP Strings, and
           Contacts
       - Mobile Apps Allow App Connections and Visible to Mobile Apps
       - Partitions Partitioned Control Enable, Channel Partitions for multi-
           user setups
       - Processors Expansion Processing Enable, Exceed 75k Output, Default
           Processor for New Universes, Processor Settings
       - Video Streams         Video Stream Pixel Maps Enable, Library Folder
           Video Stream Settings
       - Users      User Settings: User ID, Add, Delete, Copy User,
                                                                                   Up to 20 users
           Augment3d Enable/Disable Per User

### USER – SPECIFIC TO THE USER – STORED IN SHOW FILE

       - Record Defaults      Record Defaults: Track Mode, Record/Delete
           Confirm, Auto Playback, Record Effects in Presets, Update Defaults,
           Emergency Mark
       - Manual Timing          Manual Timing, Default Times: Sneak, Go To
           Cue, Back, Assert, Off, Release, and Timing Disable Times
       - Manual Control        Encoders: Percent or Degrees Per Revolution,
           Mini Percent Per Rev, Scroll Percent Per Rev, Button Values: Level,
           Plus/Minus %, Live RemDim Enable and Level, Highlight:
           Highlight/Lowlight Presets, Highlight RemDim Enable and Level,
           Default Encoder Map
       - Displays    Preserve Blind Cue, Blind Next/Last Affects Target, Popup
           Magic Sheet and Popup Navigation Lock, Augment3d Display Behavior

### DEVICE – SPECIFIC TO HARDWARE – BUT STORED IN SHOW FILE

         - Config        Device Name                                                           Reboot required for changes to Config,
         - Network       Network Connections Status and Configuration                          Network, or Local Output

         - Local Output Local DMX Outputs and System Dimmer Dbl offset.
         - Show Control            Tabs for USB MIDI/SMPTE, Contacts, USB Serial
             and OSC USB
         - Face Panel Input Devices: Trackball settings, Spacebar [] (Go)
             Enable, Use Shift as Eos Shift, Protect Wheels in Blind, Hide Mouse,
             Auto Repeat settings, Target Key Edit Enable, Tab for Sounds
         - Fader Wing Layout       Layout and Identify
         - Wing Paging Groups ID, Type and Group Numbers
         - Brightness Settings Show All, Presets 1-3, Extinguish, Brightness for
             Main, Monitors - External and Internal, Face Panel, Task Lights, USB
             Wing Displays, and Ion Face Panel. Also Enable Control of External
             Monitors

### RECORD A PRESET

                 Set Brightness levels for all sliders (components)

                 Press and hold {Preset #} to record

### EXTINGUISH

                 Extinguish sets all brightness settings to 0% and darkens all console screens
                 and buttons.

                  Press [Displays] to exit Extinguish mode

### ACCESS IN LIVE

                  In Live, hold [Displays] to access Brightness Settings popup

                  Hold [Displays] and run level wheel to control Main brightness level

         - Augment3d Device Enable A3D, Device Status
         - Displays      Show Ref Labels, In-Cell Editing and Direct Select Double
             Click, Default Display Sort Order, Force Hide Encoder Ribbon, Record
             Target Color Brightness
         - Device Profiles         Bind to, Copy From, or Delete Device Profile

### CLOCK FUNCTIONS

        Left click on the Time in the upper right corner of either monitor                       can reset time without going out to shell

## Introduction to Effects

### CREATING A STEP-BASED EFFECT

    [Live]          [Go to Cue] [Out] [Enter]                                           start with a clear stage

    [Effect] [Effect] or Add-a-Tab (the {+} sign)                                       opens the effects list

    [Effect] [1] [Enter]                                                                creates a new effect number

       <Type> {Step-based}                                                              assigns the effect as a step effect

       {Step} [1] [Thru] [5] [Enter]         [Enter]                                    defines the number of steps

       [Page►] to the Channels column
                                                                                        specifies the channels or group to be used
       [Group] [30] [Enter]
                                                                                        in the order of the group
         Intensity is assumed unless another parameter is specified.

### RUN THE EFFECT

    [Live]     [Group] [30] [Effect] [1] [Enter]                                        runs the effect created on group 30

         If in Live Summary, press and hold [Data]                                      to view levels as effect is running

### EFFECT ATTRIBUTES

 Play with various attributes of the effect to see how they alter your effect.
    [Effect] [Effect]                                                                   opens the effects list

    {Cycle Time} [2] [Enter]         or dial the encoder to adjust cycle time           resets overall effect time/speed

    Click on {Attributes}                                                               opens table of various attributes

 The basic behavior of the effect can include Forward, Reverse, Bounce, Build,
 Positive, Negative, and Random Group or Random Rate.
                                                                                        each cycle plays at a different rate within
    {Random Rate} [100] [Thru] [200] [Enter]
                                                                                        the range, slower or faster
    {Random Rate} [Enter]                                                               to clear the random rate attribute
                                                                                        lights are on and turn off on a step-by-step
    {Negative}
                                                                                        basis
    {Positive}                                                                          sets effect back to a positive effect

    [Clear]                                                                             to return to the effects editor

### STEP EDITING

     Remember you can edit steps individually. Just select the steps that you wish to
     change then press [Page►] to access Step Time, In Time, Dwell Time, Decay Time,
     as well as the On State and Off State columns.

### RECORDING AN EFFECT TO A CUE

           [Live],    [Go To Cue] [23] [Enter],         [Group] [30] [Effect] [1] [Enter]        reapply the effect

           [Record] [Cue] [24] [Enter]                                                           records the effect into the cue

            Notice the FX column on the Playback Status Display now shows Effect 1 in cue 24.

           [Group] [30] [Effect] [Enter]                                                         stops the effect

           [Record] [Cue] [25] [Enter]

           [Go to Cue] [23] [Enter] and press [] (Go)… and [] (Go) again                       watch how the effect starts and stops

            Remember, this effect does not work on other channels, just Group 30.

### A SIMPLE COLOR EFFECT

        Effects 901 through 918 are preprogrammed effects

### USING A PRE-PROGRAMMED COLOR EFFECT

           [Go To Cue] [Out] [Enter]

           [Group] [20] [Full] [Enter]                                                          sets starting levels

           [Select Last] [Effect] [917] [Enter]                                                 applies existing effect to selected channels

           In the Encoder Display, take Amber to 0                                              see the more saturated colors

        Effect 917 is a Rainbow Chase for RGB fixtures. It is a Relative effect –
        executes in relation to where the lights are when the effect begins

### FUN WITH THE COLOR PICKER

            Visually see the effect running in the blue area.

                [Displays] {S2 -Color Picker} or [Tab] [27]                                     opens the color picker

                Click on various colors in the color picker                                     watch cyc change colors

                In Standard Colors, {White}                                                     centers the effect to a white

                [Record] [Cue] [26] [Enter]                                                     records the effect into a cue (26)

### STOPPING AN EFFECT

                                                                                                stops effect from running on specified
           [Select Last] [Stop Effect] [Enter]
                                                                                                channels
            On Apex consoles, [Shift]&[Effect] is the Stop Effect Command. Also [Effect] [#]
            [At] [Enter] will post Stop Effect on the command line.

           [Record] [Cue] [Next] [Enter]                                                        records the stop into a cue (27)

### MULTIPLE WAYS TO STOP AN EFFECT

                [1] [Thru] [5] [Effect] [Enter]                                                 stops the effect running on channels

                Or [Stop Effect] [1] [Enter]                                                    will stop the specified running effect

                Or [Stop Effect] [Enter]                                                        will stop all running effects

                Or [Sneak] [Enter]                                                              stops effect if manual data – not recorded

## Optional Cue Writing Exercise

### RECORD CUES WITH COLOR

   [Go To Cue] [Out] [Enter] [Cue] [21] [Block] [Enter]                              start with a clean stage

   [Group] [2] [Full] [Full], make them pink                                         set levels

   [Record] [12] [Label] Pink [Enter]                                                stores cue (12)

   [Select Last], make them cyan                                                     choose colors

   [Group] [3] [Full] [Full], make them blue                                         choose colors

   [Group] [4] [Full] [Full], make them green                                        choose colors

   [Group] [9] [Full] [Enter], make them green also                                  choose colors

   [Record] [Next] [Label] Cool Look [Enter]                                         records cue 13

   [Group] [4] [Out]                                                                 set levels

   [Group] [2] [Enter], make them orange                                             set levels

   [Record] [Next] [Time] [2] [Label] Color Change [Enter]                           records cue with a 2 second fade (14)

   [Select Active] [Out]                                                             takes lights out

```text
   [Record] [15] [Time] [7] [Label] Fade to Black [Enter] [Block] [Assert]           records a fade to black with a 7 second fade
   [Enter]                                                                           (15)
```

### RECORD CUES WITH FOCUS & FORM

                                                                                     set levels, focus fixtures, set zoom level,
   [121] [Thru] [128] {Offset} {Odd} [Full] [Enter]
                                                                                     select color
   [Next] to select Ch. 121

   Use encoders to pan/tilt fixture onto lead singer on box

   [Next] to select Ch. 123   focus onto lead singer on box

   [Next] to select Ch. 125   focus onto drummer

   [Next] to select Ch. 127   focus onto drummer

   [Select Last] {Zoom} [19] [Enter],

   Make them yellow using Standard Colors
                                                                                     stores cue 16 with a 1 second intensity time
   [Record] [16] [Time] [1] [Shift]&[Color] [Time] [5] [Label] Yellow [Enter]
                                                                                     and a 5 second color time
   [Group] [2] [At] [50] [Rem Dim] [Enter]                                           set levels

   Using Standard Colors, set to 3500K                                               set as a warm white color

   [Record] [17] [Enter]                                                             stores cue 17

### RECORD CUES WITH FOCUS, FORM, AND IMAGE

       [Group] [5] [Full] [Full],                                          set levels,

       [Focus], use encoder to tilt them on stage                          pan just off proscenium

       {Zoom} [26] [Enter]

       [Image], use Gobo Select encoder to select Fracture (gobo 3)

       [Form], use Edge encoder to make gobo sharp

       [Image], use Gobo Index/Speed Mode encoder to select {Rot+}         watch the command line

          and use the encoder to make them rotate

       [Select Last] {Offset} {Even} set Gobo Index/Speed Mode to {Rot-}

       [Select Last] [Select Last] [Enter], make yellow using Std Colors   cycles through the last 5 command lines

       [Record] [Next] [Enter]                                             records cue 18
                                                                           reset to top of cue list and home all non-
       [Go To Cue] [11.5] [Enter]
                                                                           intensity properties
                                                                           use Timing Disable function to step through
       [] (Go), [Shift]&[] (Go) to Cue 15
       [] (Go) to play through the new cues

       [Go To Cue] [Out] [Enter]

### AND DON’T FORGET TO SAVE YOUR SHOW FILE!

## Appendix 1 – Channel Hookup

```text
Chan       Univ / Address   Manufacturer   Fixture                Mode                 Label
1          1        1       Generic        Dimmer                 Dimmer [1]           Frontlight - A
2          1        2       Generic        Dimmer                 Dimmer [1]           Frontlight - B
3          1        3       Generic        Dimmer                 Dimmer [1]           Frontlight - C
4          1        4       Generic        Dimmer                 Dimmer [1]           Frontlight - D
5          1        5       Generic        Dimmer                 Dimmer [1]           Frontlight - E
6          1        33      Generic        Dimmer                 Dimmer [1]           Frontlight - A
7          1        31      Generic        Dimmer                 Dimmer [1]           Frontlight - B
8          1        32      Generic        Dimmer                 Dimmer [1]           Frontlight - C
9          1        35      Generic        Dimmer                 Dimmer [1]           Frontlight - D
10         1        34      Generic        Dimmer                 Dimmer [1]           Frontlight - E

31         1        301     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - A
32         1        310     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - B
33         1        319     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - C
34         1        328     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - D
35         1        337     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - E
36         1        346     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - F
37         1        355     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - G
38         1        364     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - H
39         1        373     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - I (eye)
40         1        382     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - J
41         1        391     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - K
42         1        400     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - L (ell)
43         1        409     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - M
44         1        418     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - N
45         1        427     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - O (oh)
46         1        436     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - P
47         1        445     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - Q
48         1        454     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight – R
49         1        463     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight – S
50         1        472     ETC Fixtures   D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - T

51         2        1       ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 1  Left
52         2        7       ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 1  Mid
53         2        13      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 1  Right
54         2        19      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 2  Left
55         2        25      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 2  Mid
56         2        31      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 2  Right
57         2        37      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 3  Left
58         2        43      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 3  Mid
59         2        49      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 3  Right
60         2        55      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 4  Left
61         2        61      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 4  Mid
62         2        67      ETC Fixtures   ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 4  Right
```
     + End of range +

46   [Document title]

```text
     Chan   Univ / Address     Manufacturer       Fixture                  Mode                 Label
     71     2      73          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 1  Right
     72     2      79          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 1  Mid
     73     2      85          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 1  Left
     74     2      91          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 2  Right
     75     2      97          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 2  Mid
     76     2      103         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 2  Left
     77     2      109         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 3  Right
     78     2      115         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 3  Mid
     79     2      121         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 3  Left
     80     2      127         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 4  Right
     81     2      133         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 4  Mid
     82     2      139         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D       Hi Side Tx - Ln 4  Left

     101    2      201*        High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D    FOH Mover - Spot
     102    2      251         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D    FOH Mover - Spot
     103    2      301         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D    FOH Mover - Spot
     104    2      351         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D    FOH Mover - Spot
     105    2      401         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D    FOH Mover - Spot
```
                   * Think Offset!
```text
     121    4      1           High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     122    4      37          High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     123    4      73          High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     124    4      109         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     125    4      145         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     126    4      181         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     127    4      217         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash
     128    4      253         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D    Overstage Mover - Wash

     141    5      73          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     142    5      82          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     143    5      91          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     144    5      100         ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     145    5      109         ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     146    5      118         ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     147    5      127         ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid
     148    5      136         ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D   Side - Mid

Chan      Univ / Address   Manufacturer   Fixture             Mode                  Label
151       1         281    Generic        Dimmer              Dimmer [1]            Side - Scroller
151 P2    1         291    Generic        Scroller [1]        --                    Side - Scroller
152       1         282    Generic        Dimmer              Dimmer [1]            Side - Scroller
152 P2    1         292    Generic        Scroller [1]        --                    Side - Scroller
153       1         283    Generic        Dimmer              Dimmer [1]            Side - Scroller
153 P2    1         293    Generic        Scroller [1]        --                    Side - Scroller
154       1         284    Generic        Dimmer              Dimmer [1]            Side - Scroller
154 P2    1         294    Generic        Scroller [1]        --                    Side - Scroller
155       1         285    Generic        Dimmer              Dimmer [1]            Side - Scroller
155 P2    1         295    Generic        Scroller [1]        --                    Side - Scroller
156       1         286    Generic        Dimmer              Dimmer [1]            Side - Scroller
156 P2    1         296    Generic        Scroller [1]        --                    Side - Scroller
157       1         287    Generic        Dimmer              Dimmer [1]            Side - Scroller
157 P2    1         297    Generic        Scroller [1]        --                    Side - Scroller
158       1         288    Generic        Dimmer              Dimmer [1]            Side - Scroller
158 P2    1         298    Generic        Scroller [1]        --                    Side - Scroller

301       8         1      Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
302       8         25     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
303       8         49     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
304       8         73     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
305       8         97     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
306       8         121    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
307       8         145    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
308       8         169    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
309       8         193    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
310       8         217    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
311       8         241    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top
312       8         265    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Top

351       9         1      Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
352       9         25     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
353       9         49     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
354       9         73     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
355       9         97     Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
356       9         121    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
357       9         145    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
358       9         169    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
359       9         193    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
360       9         217    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
361       9         241    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
362       9         265    Chroma Q       Color Force II 72   RGBA x4 Off [24]      Cyc Bottom
```
  + End of exercise +

## Helpful Support and Training Links

```text
            ETC Support Website                              ETC Technical Support                           Community – ETC Consoles
  All the support and training resources you      Contact our 24/7 technical support team to            Hop on the ETC forums to ask the user
        might need in one handy place                  help troubleshoot your ETC gear                  community your questions about Eos
                                                 https://www.etcconnect.com/Contact/Technic          https://community.etcconnect.com/control_
```
    https://www.etcconnect.com/support
                                                               al-Support.aspx                               consoles/eos-family-consoles/

        Video Tutorials – Eos Family                 Support Knowledge Base Articles                                ETC Training
 Experience hands-on Eos training anywhere,
                                                 Get quick answers to your technical questions        Find in-person training opportunities near
    anytime with the series of videos and
                                                  with support articles created by ETC experts         you, as well as other learning resources
                workbooks
https://www.etcconnect.com/Support/Tutorial
                                                      https://support.etcconnect.com/ETC               https://www.etcconnect.com/Training/
      s/Eos-Family-Videos/Overview.aspx

```text
           ETC Search Manuals                                 ETC LearningStage                                ETC Custom Training
Search for manuals, datasheets, release notes,   Take part in a variety of online training courses   ETC offer multiple custom training options to
        and more on the ETC website                      for technicians and operators                               fit your needs
    https://www.etcconnect.com/Search-                                                               https://www.etcconnect.com/Support/Traini
```
                                                  https://learningstage.etcconnect.com/learn
     Documentation.aspx?DocType=137                                                                         ng-Events/Custom-Training.aspx

      Eos Family Training Materials                         Educational Resources
                                                   These free materials provide a overview of
Find all of the Eos Learning Series work books
                                                           essential lighting concepts
      and training materials in one place
                                                 https://www.etcconnect.com/Support/Training
  https://www.etcconnect.com/workbooks/
                                                       -Events/Educational-Resources.aspx

Corporate Headquarters  Middleton, WI, USA  Tel +608 831 4116  Service (Americas) service@etcconnect.com
London, UK  Tel +44 (0)20 8896 1000  Service (UK) service@etceurope.com
Holzkirchen, DE  Tel +49 (80 24) 47 00-0  Service (DE) techserv-hoki@etcconnect.com
Hong Kong  Tel + 852 2799 1220  Service (Asia) service@etcasia.com
Paris, FR  +33 1 4243 3535
Web  etcconnect.com  © 2026 Electronic Theatre Controls, Inc.  Trademark and patent info: etcconnect.com/ip
Product information and specifications subject to change. ETC intends this document to be provided in its entirety.

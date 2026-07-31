# Eos Family Console Programming — Level 2: Enhanced Workbook (v3.3C)

- Source : PDF officiel ETC, « Eos Family Console Programming — Level 2: Enhanced Workbook (v3.3C) », V3.3C, révisé 2026-05
- Fichier source : [`source/Eos_Family_L2_Enhanced_v3.3.pdf`](source/Eos_Family_L2_Enhanced_v3.3.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select

             Level 2: Enhanced

                         Workbook
                                     V3.3C

             www.etcconnect.com/education

                              Revised: 2026-05

## Table of Contents

                ETC permits the reproduction of materials in this manual only for non-commercial
                purposes. All other rights are reserved by ETC.

## Purpose of the Class

    This class will provide a more in-depth look at basic operations and
    working with multi-parameter devices on an Eos family console.

### LEARNING OBJECTIVES:

       After completing this class, one should be able to:
         - Edit device attributes
         - Understand display layouts and workspaces
         - Record and recall Snapshots
         - Create more elaborate Groups
         - Be more effective using Submaster properties
         - Record and recall Palettes and Presets
         - Set up and use Direct Selects
         - Understand and use Update, Auto-Mark, and other cue attributes
         - Take advantage of Discrete Timing and Multipart cues
         - Create and use Relative and Absolute Effects
         - Feel comfortable with configuration and test functions in the Shell
         - Create and use a basic Magic Sheet

### SYNTAX ANNOTATION

         - Bold                        Browser menus
         - [Brackets]                  Face panel buttons
         - {Braces}                    Softkeys         or buttons on touchscreen
         - <Angle brackets>            Optional keys
         - [Next] & [Last]             Press & hold simultaneously
         - «Direct Selects»            Direct Select button press
         - MS Object                 Object on a Magic Sheet

         - Play Icon                   Link to video on ETC’s YouTube Channel -
              ETCVideoLibrary

### HELP

       Press and hold [Help] and press any key to see:
         - the name of the key
         - a description of what the key enables you to do
         - syntax examples for using the key (if applicable)

         As with hard keys, the “press and hold [Help]” action can be also used with softkeys and
                 clickable buttons

### THE MANUAL

       The manual is available on the console, Tab #100.

        Click on Add-a-Tab (the {+} sign) , select Manual

        Hold [Tab] & press [100]
         Please note that the manual is not available on Windows XP devices but is available as
                a download from the web site.

## Overview of the Shell

Referred to as the Eos Configuration Utility (ECU) in the manual, this
area is used for both system configuration and performing basic level
test functions.
  [Displays], in Browser, {Exit} {Ok}.          Don’t forget to save first!                       to exit to Shell

   Note:    When you exit to the shell, the console will stop outputting to the rig (No DMX!!),

### STARTING SCREEN

### PRIMARY OR BACKUP

   Primary is a mode for using a single console on a network where the
   primary output of data is from that single console. Backup requires a
   primary console to be online to synchronize.

### CLIENT OR OFFLINE

   A Client console acts as an extension of the primary console, more like
   a remote controller, remote video station, or an expensive keyboard for a
   system. Whereas Offline mode puts the software in a state where there
   is no network activity, no control, and no connections to other consoles
   or any other network devices.

### POWER OFF

   Power Off will shut down the Eos console after confirmation.

### SHELL SETTINGS

Select {Settings} when buttons are highlighted

   General    Device Name, 24 Hour Clock*, Use Shift Key as Eos Shift,
   Template Show, Software Update
                              * Time can now be reset without going to the shell

### TEMPLATE SHOW FILE

        A template show file can be assigned in the Shell via Settings >
        General.

        When a show file is assigned as a template, Eos will create a copy of
        the file in the Templates folder to be used as the default starting
        point for any new show files. An option will appear in the Browser
        under File > New called New From Template. A blank show file can
        always be created with File > New.

### MONITOR ARRANGEMENT

         The selected monitor will display in yellow. Monitors can be dragged
         to any of the surrounding black boxes to mimic the actual monitor
         layout.
         - {Calibrate} and {Reset Calibration} for internal touchscreens
         - {Enabled} - When checked, the monitor is available for use. It
             will be checked for any monitors the console recognizes.
         - {Primary} - selects which monitor will display the Eos
             Configuration Utility and Central Information Area (CIA)
         - {Resolution}, {Color Depth}, {Refresh Rate} and
             {Orientation} will help configure the monitors appropriately.
         - {Identify} - displays the video port numbers that your monitors
             are connected to on the monitors to confirm where placed.
         - {Configure Touchscreens} and {ELO Settings} for external
             touchscreens

      Network Device Network settings, Allowed Outputs, Interface Protocols
      (MultiConsole, Sensor/FDX3000 Feedback, RDM), Legacy Settings –
      Output Protocols (sACN, ArtNet, Local DMX)
      Maintenance         Deep Clear, Save Logs, Backup/Restore Show
      Archive, Peripheral Tests, Upgrade I/O Firmware

### SAVE LOGS

          Logs are useful tools for diagnosing issues. If you experience
          software problems with your system, sending log files to ETC
          Technical Services helps us isolate the issue.
          Log files can be generated by clicking on the {Save Logs} button
          here or from within the show file by going to Displays > File >
          Export.
          When complete, email the zip file to eos@etcconnect.com.

```text
      Buttons     RPU Button Setup, Console Face panel Buttons
      RFR         USB RFR Channel and Network ID
```

      When finished reviewing the Shell:

           {Accept} to exit back to the starting screen                         to exit back to the starting screen

           {Primary}                                                            to go back into the console

## Device Attributes

Start in same show file as day before or in Level 1 Complete file.
Double hit [Address/Patch] to get to the Patch display.

  In Patch, {Attributes} on the left-hand side of the CIA display                           opens the Attributes module

   {PREHEAT}
   Preheat is used to specify an intensity value to heat the channel to
   before it comes on. When a Preheat flag is applied to a cue, any
   channels that are fading from zero to an active intensity and have been
   assigned a preheat value in Patch will preheat in the immediately
   preceding cue. This is a two-step function. You must set the preheat
   level in Patch and then add the Preheat flag to the cue in Live.
     You will see a “P” in the Flags column of the PSD for the cue.

   {PROPORTION}
   Proportion is a mathematical modifier for recorded levels or intensities
   only. This value is set numerically in a range of 0% to 200%. For
   example,
   {CURVE} & {FAN CURVE}
   A curve affects how a fade happens over time.

      [Displays] {Curves} or Add-a-Tab (the {+} sign) - #21                                 to view pre-programmed curves

      [Next]…[Next]…[Next]…                                                                 to step though the curves
        If a default curve is modified, delete the curve to restore the default.
   The control input is the level that the console is telling the fixture to go to.
   The output is the actual value that is being output via DMX.
     Note: Curve 909 (Hot Patch) is a great way to have relays powering moving lights and
           LEDs. The channel will always be on when the console is on.

     Back in Patch:

   {LD FLAGS} – A TOGGLE PER CHANNEL
   By default, Live and Dark flags are enabled. If there is a Live or Dark
   move, an ‘L’ or ‘D’ will be displayed in the move flags (MV) column in the
   PSD. This can be disabled on a channel-per-channel basis.
   {SHUTTER ORDER}
   Opens a window and allows you to invert the shutter order or rotate the
   order using arrow buttons. It can be set on a per-fixture basis, so if hung
   sideways, can still have the shutters line up and work the way you want
   them to.
      [Group] [5] [Enter]

   {GM EXEMPT} – A TOGGLE PER CHANNEL
   A toggle state, if selected, channels are exempt from a Grandmaster
   fader or Blackout button, [Rem Dim], and Intensity Master operations.

      {INVERT PAN OR TILT}
      A moving light attribute is used to invert the output of pan, tilt, or both.

        [Live], [Group] [7] [Full] [Enter], tilt them up and pan                     note how they move – all together
                                                                                     inverts the output of the pan and tilt
        Back in Patch: [Group] [7] {Offset} [2] {Invert Pan} {Invert Tilt}
                                                                                     parameters
        Back to [Live]: [Group] [7] [Enter]. Tilt, then pan                          note how they move now

          On Apex consoles, [Offset] is a hard key (button).

### USING INVERT TO SET UP ENCODERS

          To make sure your encoders work the same way your eyes do. Dial
          left, lights move left; dial right, move right.
           [Group] [5] [Full] [RemDim] [Enter], tilt them up on stage,
                                                                                     note how they move opposite of encoder
             turn Pan encoder to right

           Back in Patch: [Group] [5] {Attributes} {Invert Pan}                      inverts the output of the pan parameter

           Back to [Live]: [Select Last] [Enter], and pan                            note how they move now

### NOTE: INVERTING PAN & TILT SHOULD BE DONE BEFORE YOU

### START CUEING YOUR SHOW, OTHERWISE EVERY CUE THAT HAS

### ALREADY BEEN WRITTEN WILL BE AFFECTED BY THESE

### CHANGES.

       Back in Patch:

      {SWAP P/T}
      A moving light attribute is used to exchange pan and tilt levels, such as
      when a fixture is hung sideways on a boom. Pan becomes Tilt and Tilt
      becomes Pan.
      {COLOR PATH}
      A default Color Path can be assigned at the channel level in Patch. That
      color path will be used for all that channel’s color fades unless
      overridden at the cue level. (More on Color Paths in Level 4)
      {INVERT RACK}
      When disabled, an encoder will move the shutter frame assembly from
      the right. When enabled, the frame assembly will move from the left.

### INDEXED PARAMETERS

### CREATING A NEW CUSTOM SCROLL OR WHEEL

   Function keys are on the lower left side of the monitor, either mouse or
   touch selected. They change depending on device editing.
     - {Clear} - clears the current wheel selection
     - {New} - to create a new scroll or wheel
     - {Copy} - copy an existing and then modify
     - {Edit} - opens the editor to modify
     - {Delete} - removes the selected device
     -

### SCROLLER EXERCISE - SEE APPENDIX 1 (P. 47)

     In Patch, [151] [Thru] [158] [Part] [2] [Enter]

     In Attributes (far left), under Scrollers/Wheels (right), {Scroller}

     Press {New} on lower left side of display                                             {new wheel#1} appears in list

     [Label], [Label] to clear,      then type ‘Training’ [Enter]                          labels the new scroll

     Press {Edit} softkey on lower left side of display, then {Insert}                     available color selections displayed
                                                                                           display returns to the new wheel frame list
     Press {Open Frame} softkey on lower left side of display
                                                                                           and adds ‘Generic open open’
     Select next gray box under ‘C/G’                                                      available color selections displayed

     In the left two columns, find {Rosco}, then in the next two columns, (the
                                                                                           returns to the frame list and adds color
     subcategory) find {Roscolux}, and then {R010}

     Under Name, press ‘New’ in the next box. Type [5] [/] [27] [Enter]                    another way to add color to the scroll

Now complete the scroll in Appendix 1 of the workbook

     When the last frame has been entered, press {Done}!!                                  completes the scroll, applies to fixture

     [Live], [Group] [10] [Full] [Rem Dim] [Enter]                                         use the encoder to flip through frames

         Check the frames in the Encoder Display or ML Controls

     [Home] [Enter]
     NOTE: When creating a gobo wheel: after pressing the gray box in the C/G list, make
           sure that {Gobo} is selected.

### OTHER INDEXED PARAMETERS

                                                                                           selects channel and opens the Wheel
         Back in Patch, [101] [Enter] {Attributes}
                                                                                           Picker in the CIA for wheel selection
                                                                                           used to change the dichroics loaded in a
         {Color Select}     (Default HES Color Wheel 38)
                                                                                           color wheel for a moving light.
                                                                                           used to change the gobo wheel loaded in a
         {Gobo Select} or {Gobo Select 2}         (HES Gobo Wheel 37 & 39)
                                                                                           moving light
         {Beam FX Select}       (Acme Effect Wheel 3)

         {Animation Select}       (HES Effect Wheel 14)

## Display Layouts and Workspaces

     Upon start up or creation of a new show file, any connected monitor
     that is not already displaying the Live (Tab 1) or Playback Status
     Displays (Tab 2) will show a blank screen. This screen will also
     display when a new tab is opened.

### WORKSPACE LAYOUT MENU

          Click on the large + sign or press the monitor icon in upper left-hand
          corner of the display

        Layout options are basically different ways to split the screen. A
        workspace can have up to sixteen frames. Each frame can have multiple
        tabs open.
          Click on the 2 x 2 or 4 Frames option (2nd row, 2nd one)

          Click on the monitor icon in the upper left again (first one)

          Click on Resize Frames in this Workspace

### RESIZE FRAMES IN THIS WORKSPACE

        Allows you to freely resize and edit the frames in any of the workspaces
        on the monitor. The grid includes the following tools:
                 Adds a horizontal split, dividing the frame horizontally into
                 upper and lower rows.
                 Inserts a vertical split, dividing the frame vertically into left and
                 right columns.
                 Drag left or right to freely adjust the width of the frames.              Play with the tools!
                 Double press to reset to the default horizontal size.
                 Drag up or down to freely adjust the height of the frames.
                 Double press to reset to the default vertical size.
                 Eliminates a split by closing the frame to the right and merging
                 its contents into the frame to the left.
                 Eliminates a split by closing the frame below and merging its
                 contents into the frame above.
                  Frames of the same size can be freely merged without altering
        the rest of the grid. Smaller frames can be merged with larger frames,
        but this may alter adjacent splits. A larger frame will absorb any smaller
        frames it is merged towards.
        The grid is limited to a maximum of three splits in either direction, for up
        to 16 total frames per monitor/workspace.
                                                                                         close all the tabs and frames on all
          After playing, use the Reset all Monitors and Workspaces icon
                                                                                         monitors

### WORKSPACES

A workspace is made up of multiple frames, each with its own tabs. For
each monitor, you can have up to three workspaces.

  Press the box icon numbered 2 in the upper left-hand corner of the display                to opens workspace 2

  Click on the large gray + and add the Submaster List (Tab 15)

  Hold [Tab] & press [Page ] or [Page ]                                                   to change workspaces across all monitors
      Note: This key combination will only switch into workspaces with open tabs.

### OPTIONS

The Display Controls Screen also offers options for opening and closing
tabs as well as resizing and resetting the monitor(s).
  - Resize Frames in This Workspace - opens resizing tools between
      frames of the workspace to adjust sizing as needed.
  - Monitor Mapping - ability to configure your external monitor
      arrangement (internal displays cannot be renumbered)
  - Close All Tabs in This Workspace - close all the tabs in the active
      workspace on this monitor only.
  - Reset This Workspace - closes all the tabs and frames and resets
      the layout for the active workspace to a single frame displaying the
      Home Screen
 - Reset ALL Monitors & Workspaces - closes all the tabs and
      frames on all monitors, resets all layouts to a single frame, and
      returns their workspaces to the Home Screen
                                                                                            closes all the tabs and frames on all
  After playing, use the Reset all Monitors and Workspaces icon
                                                                                            monitors

## Snapshots

     Snapshots store layouts so that you can recall them quickly. They are
     stored in the show file, can be recalled on any device on the network.

### RECORDING SNAPSHOTS

       In [Live], be in Table View, and in Flexi - Patched Channels on one monitor
       and have the PSD & CIA on the other

       [Record] [{Snapshot}] [1] [Enter]                                                       records the snapshot

       In the upper left-hand corner, press the display controls icon

       Select the side-by-side layout

```text
       Highlight the PSD display on the right monitor.                                         move the PSD tab onto the same monitor
       Hold [Tab] and press [Page ] or [Page ]                                               as the Live display

       Press display controls icon in upper left-hand corner of right monitor                  the monitor with the CIA
```

       Select the side-by-side layout

       Select the Direct Selects display on the left side, Groups for the type                 3rd column, 4th one down [Tab 4]

       Select the Color Picker on the right side                                               3rd column, 2nd one down [Tab 27]

       [Record] [{Snapshot}] [2] [Label] Color Picker [Enter]                                  records the snapshot

### RECALLING SNAPSHOT

       [{Snapshot}] [1] [Enter]                                                                recalls the content of snapshot 1.

       [{Snapshot}] [2] [Enter]                                                                recalls the content of snapshot 2.
          NOTE: When recalling snapshot, the command does not appear on the command line, it
                appears above the command line (red text)!

       Use Snapshot Quick Access Tool (pop-up icon) to select Snapshot 1                       recalls the content of snapshot 1.

       [{Snapshot}] [{Snapshot}]                                                               opens the Snapshot list

## Groups

### SUB-GROUPS

 You can create subsets of channels within a group that are treated as a
 single channel in group/channel selection and in effects.
   [Group] [Group]       [Group] [103] [Enter]                                                creates group 103

   [Shift]&[/] [51] [Thru] [53] [Shift]&[/] [Shift]&[/] [54] [Thru] [56] [Shift]&[/]
                                                                                              puts sidelights in sub-groups
   [Shift]&[/] [57] [Thru] [59] [Shift]&[/] [Shift]&[/] [60] [Thru] [62] [Enter]
       [Shift]& [/] [/] will close one set of parentheses and open the next.
       [Enter] on the command line will close the paratheses. Last [Shift]& [/] not needed.

   [Label] Left Hi Sides [Enter]

   Back in Live, [Clear] [Sneak] [Enter]

   [Group] [103] [Full] {ChanCheck} [Enter]              [Next]…                              does a channel check with sub-groups

 Each set of three channels is treated as one channel in the channel
 check.
   [Clear]

   [Shift]&[/] [Group] [5] [Shift]&[/] [Shift]&[/] [Group] [7] [Shift]&[/] [Record]
                                                                                              creates sub-groups of movers in Live
   [Group] [23] [Label] Movers [Enter]

### CREATE GROUPS USING OFFSET

 Using Offset to create groups is a quick way to reorder channels as well
 as create sub-groups more easily. On Apex consoles, [Offset] is a hard
 key (button).
   [Clear] [Sneak] [Enter]

   [301] [Thru] [312] {Offset} {Mirror Out} [Record] [Group] [101] [Label] Cyc
                                                                                              Offset graphic displayed in CIA area
   Mirror Out [Enter]

   [Group] [Group]                                                                            Back in the Group List

   [Group] [101] [Copy To] [Group] [102] [Enter]

   {Reverse} [Enter]                                                                          Reverse is a softkey option

   [Label] Cyc Mirror In [Enter]

   [Live]    [Group] [101] [Full] [Thru] [10] [Enter]                                         Notice cyc is brightest in center

   [Group] [102] [Full] [Thru] [10] [Enter]                                                   Notice cyc is dim in center

   [Clear] [Sneak] [Enter]

### CREATING A QUICK INTENSITY EFFECT

   [Effect] [Effect]    [Effect] [99] [Enter]      <Type> {Absolute}                          Leave as the default

   In Live, [Group] [101] [Full] [Enter], [Effect] [99] [Enter]                               Mirror out Intensity Effect

   [Group] [102] [Effect] [99] [Enter]                                                        Mirror in Intensity Effect

   [Clear] [Sneak] [Enter]

### ADDITIONAL OFFSET MODIFIERS

            [71] [Thru] [82] {Offset}

            {Chan per Group} [3] … [Clear] Then [5] … [Clear] Then [4]                     Watch graphic in CIA for differences
                                                                                           Reorders the subgroups so they are not
            {Interleave}…[Clear]
                                                                                           sequential
            {Jump} [3]                                                                     Notice the gap between the subgroups

            [Shift]&[Clear]                                                                Clears the command line

            [31] [Thru] [50] {Offset} {Mirror Out} {Chan Per Group} [4] {Interleave}
                                                                                           Watch graphic in CIA as you build
            [Record] [Group] [104] [Enter]

                  Result:
            [Group] [104] [Full] {Chan Check} [Enter]… [Next]… [Next]… [Next]              Watch the viz to see sub-groups

### GROUP LIST

       All Groups should be in the show after the previous exercises.
       If not labeled, take a moment and do so.
```text
        Group #          Label                   Channels
        1                Frontlight              1 > 10
        2                Downlight               31 > 50
        3                High Sides – Left       51 > 62
        4                High Sides – Right      71 > 82
        5                FOH Movers              101 > 105
        7                OS Mover Wash           121 > 128
        9                Side Mids               141 > 148
        10               Side Scrollers          151 > 158
        20               Cyc Top                 301 > 312
        21               Cyc Bottom              351 > 362
        22               All Cyc                 301 > 312 351 > 362
        23               All Movers              (101 > 105) (121 > 128)
        30               Effect 1                34, 31, 33, 35, 32
        101              Cyc Mirror Out          (306 > 307) (305 308) (304 309) (303 310) (302 311) (301 312)
        102              Cyc Mirror In           (301 312) (302 311) (303 310) (304 309) (305 308) (306 > 307)
        103              Left Hi Sides           (51 > 53) (54 > 56) (57 > 59) (60 > 62)
        104              Offset Subgroup         (33 38 43 48) (32 37 42 47 34 39 44 49) (31 36 41 46 35 40 45 50)
```

                Note: Ctrl-J on the alphanumeric keyboard does a carriage return in
                Labels

## Submaster Properties

### TIMING ON SUBMASTERS

 Changes can be made in Live or in Sub List. The Sub bump button is
 Go.
   Be in Snapshot 1
                                                                             adds a 3 sec upfade, dwells for 4 sec and
   [Live]      [Sub] [1] [Time] [3] [Time] [4] [Time] [3] [Enter]
                                                                             3 sec downfade
   Press the bump button of fader 1 just once                                fades up, holds, then fades down

### HOLD

       [Sub] [1] {Hold} [Enter]                                              changes the dwell time to ‘hold’

       Press the bump button to start the upfade                             fades up, holds indefinitely, LED flashes

            Press the bump button to start the downfade                      fades down

### RESTORE TO DEFAULT TIME

       [Sub] [1] [Time] [Enter]                                              resets to default times (0/Man/0)

### SUBMASTER LIST

 Notice this is a Blind display, but Submasters are always Live.
                                                                             opens the submaster list - use the softkeys
   [Sub] [Sub] or Add-a-Tab (the {+} sign)
                                                                             for selection and editing

 {EDIT}
   [Sub] [1]      {Edit}    [10] [Full] [Enter]                              add a channel into this sub in Blind

   [Sub] [Sub]                                                               back to Submaster List

### PERCENT (%)

 The list shows the current level in Live of each submaster.

### FADER

 The list shows the location of the submaster – page / fader
 number.

### MODES

 Additive (contributes to the live output) is the default.
 Inhibitive (limits live output) restricts the values as the fader comes
 down, like a mini grand master for the contents of the sub.
 Effect allows the submaster to control the rate and/ or size of an effect
                                                                             makes sub 1 an inhibitive sub, LED turns
   [Sub] [1], under Mode, {Inhibitive}
                                                                             red
      Push Fader 1 up if on non-motorized hardware

   {Edit} to be in Blind                                                     notice the ‘INs’ as channel values

   [Live], [Go To Cue] [4] [Enter]                                           runs the cue
                                                                             channels go out - notice small yellow ‘I’ in
   Slowly bring the fader out
                                                                             channel display
   Bring the fader back up                                                   leave up for duration of class

   [Go To Cue] [Out] [Enter]

### FOH INHIBITIVE SUB

       A good example of using an Inhibitive Submaster is for FOH lights on
       main curtain - would never use as an additive – great for multiple curtain
       calls
         [Group] [1] [+] [Group] [5] [Full] [Enter]

```text
         [Select Last] [-] {All NPs} [Record] [Sub] [3] [Label] FOH Inhib [Enter]             select only intensity for channels, record
            [Load] to fader 3                                                                 and load the sub
```

         NPs stands for non-intensity parameters. Button is in the CIA on the far left side

         [Sub] [3], {Properties}, under Mode, {Inhibitive}                                    change to inhibitive sub

         Bring fader up                                                                       for rest of class!

### MASTER: PROPORTIONAL OR INTENSITY MASTER

       Proportional submasters control all contents of the submaster (intensity
       and non-intensity parameters). (DEFAULT)
         [Clear] [Sneak] [Enter]                                                              go to a blank stage

         [Group] [5] [Full] [Full], tilt up on cyc

         [Record] [Sub] [10] [Enter], Load to fader 10, [Clear] [Sneak] [Enter]               records sub and clears manual values

         Then bring fader up, see live changes                  Bring fader down!             shows proportional control of contents

       Intensity masters only control intensity. The bump button is used to
       preset (mark and unmark) non-intensity parameters.
         [Sub] [10], {Properties} under Master, {Int}                                         toggles the submaster to an I-Master

         With fader down, press the bottom bump button, its LED flashes                       marks the non-intensity parameters

         Bring fader up                                                                       now shows Intensity control only
                                                                                              Unmarks (resets) non-intensity
         Bring fader down and tap bottom bump button
                                                                                              parameters

### EXAMPLE WITH LED COLOR

            [Group] [20] [Full] [Full], make them blue

            [Record] [Sub] [11] [Enter], load to fader 9, [Clear] [Sneak] [Enter]             records sub and clears manual values

            [Sub] [11], {Properties} under Master, {Int}                                      toggles the submaster to an I-Master

            Press the bump button, bring fader up and down                                    only see color as fades up
           If the bump button is not pressed, when the fader moves up to 1%,
           the non-intensity parameters mark quickly. The rest of the fade is
           intensity only.
           An option in Properties called Unmark 0 releases the non-intensity
           parameters of the submaster when the fader fades down to 0%.

### EXCLUSIONS OR EXCLUDE

       Another property is Exclusions/Exclude. {Record}, where its output is
       not recorded into any other record target, then {Solo}, {Inhib}, and
       {GM}.
                                                                                              contents will not be stored in any record
         [Sub] [10], {Properties}, under Exclude, {Record}
                                                                                              targets
              Think about Houselights on a Sub that is set to Exclude from Record.

## Syntax / Command Line Filtering

### EXPECTED SYNTAX

The command line expects instructions to be entered in a specific
structure, or syntax:
Channel Selection and/or Categories & Parameters  Modifiers and/or Action

```text
 Channel or Target Selection      Categories & Parameters               Modifiers                       Action
 Chan 1                                                                                                 At Full
 Group 6                          Color                                                                 Record Preset 4
 Group 6                          Cyan                                                                  At /50
 Chan 101                         Image                                 - Gobo Select                   Sneak Enter
```
   You don’t have to use something from every column each time, but you must enter it in this
   order.

### USING SNEAK

      [Group] [5] [Full] [Enter], tilt up on cyc, in orange, with gobo, zoom out,
                                                                                                set levels
      and make it sharp (edge full)
                                                                                                sneaks all parameters including intensity
      [101] [Sneak] [Enter]
                                                                                                back to default
      [102] [Shift]&[Focus], [Shift]&[Color], [Shift]&[Beam]* [Sneak] [Enter]                   everything but intensity sneaks
            * To put Beam on the command line, double hit Form, Image, or Shutter.

      [103] [-] [Shift]&[Intensity] [Sneak] [Enter]                                             same as 102 but stating the exception
                                                                                                everything in Beam category except Gobo
      [104] [Shift]&{Beam} [-] {Gobo Select} [Sneak] [Enter]
                                                                                                Select sneaks
            Command Line filtering lets us be as broad or as specific as we need to be when
            we are modifying or storing information.

### COPY TO AND RECALL FROM

   [Copy To] takes the information from here and puts it over there.
      [101] [Thru] [104] [Sneak] [Enter]                                                        leaves 105 on stage

      [105] [Copy To] [101] [Thru] [104] [Enter]                                                copies all values to other channels

      [102] [Thru] [105] [-] [Shift]&[Intensity] [Shift]&[Focus] [Sneak] [Enter]                resets most values to background state
          Another option is to use [Sneak] [Sneak] which will take all the non-
          intensity parameters to their background level or out. It is a self-
          terminating command.
   [Recall From] takes the information from over there and brings it here.
                                                                                                pulls info from 101 and pulls into selected
      [102] [Thru] [105] [Recall From] [101] [Enter]
                                                                                                channels
      [Select Last] [Home] [Enter]                                                              resets the values to default

      [101] [Shift]&[Intensity], [Shift]&[Focus], [Shift]&[Color] [Copy to] [103]
                                                                                                copies intensity, focus & color but not beam
      [Enter]
            Copy To and Recall From also works between targets. Channel information can be
            recalled from other cues or palettes that are not currently live.

## Palettes

     Palettes are building blocks for programming. There are four types of
     palettes that correspond with the four data categories – Intensity,
     Focus, Color, and Beam. These record targets quickly recall stored
     data. Palettes can only contain information from within their category.
     For example, color palettes can only store color information – they
     cannot contain intensity, focus, or beam data.
     It is important to remember Palettes are referenced data. Changes to
     palettes will affect any place where the palette is stored: presets,
     cues…

### COLOR PALETTES

           {Snapshot} [2] [Enter]       [Clear] [Sneak] [Enter]                       clears the stage

           [Group] [2] [Thru] [9] [+] [Group] [22] [Record] [Group] [99] [Enter]      sets up a group for use with color palettes

           [Group] [99] [Full] [Enter]    {Color Picker} and select a red             notice not all the same

           [Group] [99] [Record] [Color Palette] [1] [Label] Red [Enter]              records Color Palette 1

           [Clear] [Sneak] [Enter]

           [Group] [2] [Full] [Enter]    [Color Palette] [1] [Enter]                  the downlights go to red

           [Group] [99] [Full] [Enter]    {Color Picker} and select an orange

           [Select Last] [Record] [Color Palette] [Next] [Label] Orange [Enter]       records Color Palette 2

### COLOR PALETTE EXERCISE

        Record five more Color Palettes using Group 99:
```text
               CP1           Red
               CP2           Orange
               CP3           Yellow
               CP4           Green
               CP5           Lt blue
               CP6           Dk blue
               CP7           Magenta
```

        When done…

           [Group] [22] [Full] [Enter]    [Color Palette] [1] [Thru] [7] [Enter]

           [301] [Thru] [312] [Rem Dim] [Enter] [Color Palette] [1] [+] [6] [Enter]

### LABELS

        To display labels or values:
          - Per Tab, press the Gear tab and check Show Reference Labels
          - Per Device, in Setup > Device > Displays > enable Show Ref Labels
          - [Data] – if in an active cue, displays background level data
          - [About]&[Label] – toggles the display between referenced labels
               and target numbers.
          - [About]&[Label] [Label] – double press to lock reference labels on.
               Press [About] & [Label] again to unlock.

### FOCUS PALETTES

  [Clear] [Sneak] [Enter]

  [Group] [5] [Full] [Enter]    and tilt up on stage                           brings up FOH lights

     [Next]…[Next] and focus each light on the Guitar Player

  [Select Last] [Record] [Focus Palette] [1] [Label] Guitar [Enter]            records Focus Palette 1

  [Clear] [Sneak] [Enter]
                                                                               The test – did all the lights go to the guitar
  [103] [Full] [Full]   [Focus Palette] [1] [Enter]
                                                                               player?

### FOCUS PALETTE EXERCISE

  Record four more Focus Palettes using Group 5:
        FP1             Guitar (SR)

        FP2             Singer (CS)

        FP3             Drums (SL)

        FP4             Low Platform (USR Platform) behind guitarist

        FP5             High Platform (USL Platform)

### WHEN DONE…

      [Group] [5] [Full] [Enter]      [Focus Palette] [1] [Thru] [5] [Enter]   fans the lights across all 5 palettes

      OR [Group] [5] [Focus Palette] [3] [+] [4] [Enter]                       fans lights from palette 3 to 4 in a line

### BEAM PALETTES

        Be in Snapshot 1          [Page ] to see Beam parameters                                 make sure you are in Live Table View

        [Clear] [Sneak] [Enter]            [Group] [5] [Full] [Enter]   Tilt on stage             put lights back on stage

           {Form}, {Zoom} [26] [Enter]             {Image}, {Gobo Select} {Bars 2}                zoom fixtures and in bars gobo

           Make it sharp

        [Select Last] [Record] [Beam Palette] [1] [Enter]                                         records BP info for all beam parameters
         Notice that all parameters in the Beam category have been recorded into the Beam
                 Palette (BP1). Not just zoom and gobo select.

### USING COMMAND LINE FILTERING

            [Select Last] [Shift]&[Image] [Record] [Beam Palette] [2] [Enter]                     records image category only
                                                                                                  see that just parameters from Image
            [Page ] to see Beam parameters
                                                                                                  category are stored in BP2
            [Blind], [Format] to table view,

            [Beam Palette] [1] [Enter] [Group] [5] [Enter], [Page ]                              see that BP stored data in all parameters

            [Next] to see Beam palette 2                                                          only see data for image parameters
             When applying BP2, any form or shutter parameter values will not be overridden,
             since there are no form or shutter values stored in that BP.

            [Live]

```text
            [Group] [5] {Gobo Select} [Record] [Beam Palette] [3] [Label] Bars                    see that only Gobo Select is recorded in
            [Enter]                                                                               BP3, “Bars” shows up as label
```
                                                                                                  see that only Zoom is recorded in BP4, “26
            [Group] [5] {Zoom} [Record] [Beam Palette] [4] [Label] 26 deg [Enter]
                                                                                                  deg” shows up as label

### INTENSITY PALETTES

                                                                                                  set levels, notice this selects all channels in
         [Clear] [Sneak] [Enter]          [1] [Thru] [Full] [Full]
                                                                                                  your current flexi state
             Don’t recommend doing this in a real theater!

         [Record] [Intensity Palette] [1] [Label] 100% [Enter]                                    records active channels at 100% in IP1
             After [Label], press [Full] to insert Full as the label.

         [Clear] [Sneak] [Enter]

         [Group] [101] [At] [Full] [Thru] [0] [Enter]                                             set levels, fans the intensity of the cycs
                                                                                                  records active channels in Intensity Palette
         [Select Last] [Record] [Intensity Palette] [2] [Label] Hot Center [Enter]
         [Clear] [Sneak] [Enter]
                                                                                                  brings back the levels recorded in Intensity
         [Group] [101] [Intensity Palette] [1] [Enter]
                                                                                                  Palette 1 – cyc at 100%
                                                                                                  brings back the levels recorded in Intensity
         [Intensity Palette] [2] [Enter]
                                                                                                  Palette 2 – cyc at fanned values
```text
         Press & Hold [Data]                                                                      to see actual values in Intensity Palette 2
         If press [Data] [Data] will latch,          [Data] again to unlatch                      Data Latched at top of screen
```

         [Clear] [Sneak] [Enter]
         Note: The command Recall From an Intensity Palette recalls only the values or absolute
                data from the palette.

### PRESETS – ALL PALETTES

Presets can collect all data for a given channel (intensity, focus, color,
and beam palettes as well as absolute data) rather than just one
parameter type like with a palette.
      [Clear] [Sneak] [Enter]

      [Group] [5] [IP1] [FP2] [CP1] [BP2] [Enter]                                              create look with referenced data
                                                                                               records all parameter data for all channels
      [Record] [Preset] [1] [Label] Singer Red [Enter]
                                                                                               and adds a label to preset 1
           Press and hold [Data]                                                               to view referenced palettes

      [Group] [5] [FP1] [CP6] [Enter]

      Change focus manually - tilt down, then zoom out                                         Change the focus and zoom
                                                                                               records cue with referenced data, but
      [Select Last] [-] {Intensity} [Record] [Preset] [2] [Enter]
                                                                                               selective (without intensity)
                                                                                               Pan & Tilt have absolute data, color is still
           Press and hold [Data]
                                                                                               referenced

### HOME PRESET

   Home Presets are a quick way to redefine home values of any or all
   fixtures.
      [Go To Cue] [Out] [Enter]
                                                                                               move the fixtures to a place where you want
      [Group] [5] [Full] [Full], tilt up on stage
                                                                                               them to be at their home position
      [Select Last] {Focus} [Record] [Preset] [999] [Label] Home [Enter]                       create a preset for the home value

      [Sneak] [0] [Enter]                                                                      clear the manual values

      [Displays] {Setup} {System} {System}                                                     go into setup

      {Home Preset}      Select Preset 999 from the drop-down menu                             define the home preset that you created

      [Live], [Group] [5] [Full] [Full]                                                        bring the channels to full
          Group 5 hasn’t had any move instructions since defining the home preset.

      Pan & tilt the units, drop in some color                                                 change the fixtures

      [Select Last] [Home] [ Enter]                                                            channels go back to the new home.
          Pan and Tilt have gone to new home values and are no longer manual data.

### ADD TO HOME PRESET

      [Group] [99] [Full] [Enter]                                                              bring all color changing fixtures to full

      Using the color picker, {Standard Colors} {3500K}                                        change them to warm white

      [Group] [99] [-] {Intensity} [Update] [Preset] [999] [Enter]                             update this as their new home color

      [Sneak] [0] [Enter]                                                                      clear the manual values

      [Group] [2] [Full] [Full]                                                                notice the warmer color
          A Home command will use data stored in the home preset. If there is no data stored
          for a parameter or channel, it will use the console’s default home values for that
          parameter.

## Direct Selects

      Still in Snapshot 1, on the right monitor, collapse the CIA

      Select Add-a-Tab (the {+} sign), select the DS Direct Select Module (Tab 4)      opens Direct Select display

### DIRECT SELECT LAYOUT

     When open, there are two banks of targets.
      Select {Groups} on top and {Color Palettes} on bottom

        To scroll through more Direct Selects, use the {} {} buttons.
        To change the Direct Select type, press the {Select} button. Please note
        that it may have the current target type label instead of the word ‘Select’.
        {Expand} opens the bank to a full screen of direct selects and displays
        the century and millennial buttons that allow you to jump to pages in the
        hundreds and thousands.

### TO ACCESS THE CONFIGURATION MENU FOR THE DIRECT SELECT DISPLAY:

          Press the Gear icon all the way to the left of the tabs
              Can also right click or double-left click on the tab!

### CONFIGURATION MENU OPTIONS

            # of Banks – enter the number of different target banks desired
            Current Bank – which bank are you editing
            Layout – select banks of 25, 50, 100, or 200
            - Custom Rows/Columns – can add rows or columns
            Control Buttons – select which buttons are displayed on the screen
            - Position – where do you want to place the control buttons
            - Use Record – displays the {Record} button on the display
            - Use Select – displays the {Select} button on screen, may have
                the current target type label instead of the word ‘Select’
            - Use Flexi – {Flexi} button on screen
            - Use Expand – displays the {Expand} button on screen
            - Use Arrows – displays the page up and down arrows
            - Use Jump To – displays {Jump To} button – use to jump to
                pages in same list or different list
            - Use Millennial Buttons – displays the 100/1000 target
                buttons
            - Select – to change the Direct Select target from this window
            - Flexi – toggles the Flexi state on and off from this window
            Other
            - Increment – display targets by whole number, 10ths or 100ths
            - Icon Position – drop down menu – location of icon on the tile
            - Icon Opacity – configures transparency of the image – lower
                levels allow the label to be more visible in front of the image
            - Skip Empty Flexi Space – shows a visual break instead of a
                full button space between recorded targets
            - Use Color Swatch – displays a color tag that previews the
                color recorded in the Color Palette, based on highest channel’s
                color
            - Maximize Button Size – like Fit to Screen – depending on
                layout, allows buttons to expand to fill the screen

### ICONS

You can apply and view Direct Select icons to associate images with
your targets. Go to the target’s list to apply the images.
 [Group] [Group]                                                         To open the Group List

 Select Group 3, press the {Icon} softkey or click in the Icon column    Hi Side Left group

 Click the “Import” icon to the far right next to Organize

 Double click “Stock Icons”

 Double click “Directional Arrows” folder

 Double click on “Arrow Right”                                           It now appears in the folder list

 Choose it from the folder list and make outline and fill white          Lower right, below import

 Select Group 4, press the {Icon} softkey or click in the Icon column    Hi Side Right group

 Click the “Import” icon

 Double click the “Arrow Left”                                           It now appears in the list

 Choose it from the list and make outline and fill white                 Lower right, below import

 [Live], on the Direct Select tab                                        Notice these icons are displayed

 In the Direct Select gear settings – try Icon Position as top center,
                                                                         Note that center fills the whole square
 bottom left, then center

 Change Opacity to 100, change it to 50

 Change back to Top Center, Opacity 100

### DEFAULTS

You can save your settings as a default state.
- Set Current as Default – uses the current settings to create a
   default state.
- Reset to Default – restores the settings to the default state.
- Reset to Eos Default – restores settings to Eos factory
   defaults.

### SELECTION INDICATION

Note that with Group Direct Selects, any Direct Select containing
channels within the current command line selection will highlight.
                                                                         Groups 2 + 30 are highlighted as each
 [Live] [31] [Enter]
                                                                         contains the selection of channel 31
                                                                         Groups 2, 3, + 30 are partially highlighted
 [31] [+] [51] [Enter]
                                                                         as each contains part of the selection

### ANOTHER SNAPSHOT

 On the right monitor, open the CIA

 Create two frames, side by side

 Change the existing Direct Select tab on left from 2 banks to 1 bank

 Select Groups

 On the new frame on right, open another Direct Select tab

 Select Color Palettes

 [Record] [{Snapshot}] [3] [Label] Programming [Enter]

### APEX TARGET KEYS AND KEYPAD TOUCHSCREEN

### TARGET KEYS

       The number of Target Keys on the Apex console will depend on the
       model. The APEX 5 console has 2 banks of 10 target keys while the
       larger models, the Apex 10 and the Apex 20 have 4 banks and 5 banks
       respectively.
       Target keys are OLED buttons that can be populated with existing Direct
       Selects.

### TARGET KEY EDITOR

                                                                                                    {Edit} appears on each of Target key
        Hold down [Displays]
                                                                                                    bank
        Press {Edit} on Bank 1                                                                      a pop-up appears in the CIA

       To change the target type, like Direct Select editing, the current Target
       Type is displayed on the far-right top button.
                                                                                                    Focus Palettes are populated on Target
        Press the target type and select {Focus Palettes}
                                                                                                    key bank 1

### ARROW MODES

            A drop down menu is used to select Both Top, Both Bottom, Both
            Split, Next Only Top or Bottom, or Hide them completely, allowing
            use of all 10 keys for targets.
        Using Arrow Mode, hide the arrows on Bank 1
                                                                                                    Bank 2 Target keys are populated with
        Hold down [Displays] and press {Edit} on Bank 2, select {Color Palettes}
                                                                                                    the Color Palettes
        Using Arrow Mode to hide the arrows
         If arrows are hidden, you can hold [Displays] and get temporary navigation arrows.

### STARTING TARGET NUMBER

            Select {Color Palette 5} (Lt Blue)                                                      it becomes the first target on the bank

            Select {Color Palette 1} (Red)                                                          to reset the first target

### USING TARGET KEYS

       Using Target keys is exactly like using Direct Selects on a touchscreen
       except there is a physical button.
        [Select Last] or [101] [Thru] [105] [Enter]                                                 select channels

        Press the various Target keys – Focus and Color Palettes                                    appears on command line

### ICONS

       If using icons associated with your targets, in the Editor, you can change
       how they are displayed on the Target key independently of how they are
       displayed on the Direct Selects.
       NOTE: If you want them to be large, select {Icon Center} and the icon will fill the Target
       key.

       !! Target Key Mapping is stored in Snapshots!       Remember to Record !!
       Each bank has a unique number, up to 5. The bank numbers are like
       monitor numbers and mapping. When the show file is opened on a
       different console, Bank 1 in the show file is going to be populated on
       Bank 1 of the new console.

### KEYPAD TOUCH SCREEN

The keypad touchscreen is right above the keypad and serves several
functions. Across the bottom of the screen are the standard softkeys.
They are also accessible on other monitors. Apex also has physical keys
labeled SK1 through SK6 plus a More SK button for paging the softkeys.

The other function of the Keypad Touchscreen is to display a Magic
Sheet or Custom Direct Selects.
The keypad touchscreen is a haptic touchscreen which sort of bridges
the gap between buttons and a touch screen. The screen does not react
to a light touch, but when a button is held down or given a deep press, it
reacts with a ‘thunk’. This allows for customization of a touchscreen but
still allows the programmer to keep their eyes on the stage while waiting
to engage a button.
The level of haptic feedback can be changed in Setup or even disabled
completely. (Setup, Device Settings, Face Panel, Haptics tab)

### MAGIC SHEETS OR CUSTOM DIRECT SELECTS

    Selecting what is displayed above the softkeys is simple.
    On the keypad touchscreen, press the small gear near Softkey 6 (far
                                                                                this is the Setup button
    right)

    Select {Custom DS} or {Magic Sheet}                                         screen is populated with targets

    Select the desired target                                                   screen remaps to the selected target
      Custom Direct Selects are covered in Level 3. They are a way to combine
      target types in one frame.

## Write Cues with Palettes

### USING THE COMMAND LINE

     Recall Snapshot 1

     [Go To Cue] [27] [Enter]                                                      (Last cue recorded in Level 1 class)

     [Group] [3] [Full] [Enter] [Color Palette] [7] [Enter]

     [102] [+] [105] [Full] [Enter] [Focus Palette] [1] [Enter]                    Lights on Guitar player

     [101] [+] [104] [Full] [Enter] [Focus Palette] [3] [Enter]                    Lights on Drummer

     [Group] [5] [Select Active] [–] {Intensity} [–] {Focus} [Home] [Enter]        removes Color and Beam parameters

     [Record] [Next] {Color} [Time] [1] [Enter]                                    (28)

### USING DIRECT SELECTS AND THE COMMAND LINE

     Recall Snapshot 3

     Touch «Side Mids», [Full] [Full], «Lt Blue»            (G9) (CP5)

     Touch «High Sides – Left» and «Orange»             (G3) (CP2)

     Touch «Cyc Top» and «Dk Blue»              (G20) (CP6)

     [Record] [29] [Time] [3] [Enter]                                              (29)

     [Group] [102], hold [Shift] & touch «Red», release [Shift], touch «Dk Blue»   command line shows Color Palette 1 + 6

        Holding [Shift] and pressing a Direct Select will leave the command line
        unterminated so another command can be added.
     [103] [Full] [Enter] [Focus Palette] [2] [Enter]     (Singer)

     [Select Last] [-] {Intensity} [-] {Focus} [Home] [Enter]                      removes beam parameters

     Touch «FOH Movers» [-] [103] [Out]            (G5)                            takes out group with an exception

     Touch «High Sides – Right» [Full] [Full]        (G4)

     {Color} [Recall From] «High Sides – Left»       (G3)                          brings color in from the other group

     [Record] [30] [Time] [2] [/] [7] {Color} [Time] [3] [Enter]                   (30)

## Update

Update is a ‘save changes’ tool. It only pertains to values that are red
or modified – values that have been changed. Update saves manual
changes back to targets such as cues, palettes, presets and
submasters.

### UPDATE - MAKE ABSOLUTE

   Sometimes we want to make a change to a palette in one cue and not
   change the palette itself. This is the default way that update works – it’s
   called Make Absolute, and stores changes directly to the cue rather than
   to the palette. This is useful if you need to make a one-time change to
   your palette data – for example, if a chair moves from one location to
   another for one moment in the show, you can simply update the cue for
   that singular moment.

    Be in Snapshot 1

    [Go To Cue] [28] [Enter]     and be in Live Table View
                                                                                 the guitar player is doing this part from
    [102] [+] [105] [Enter]
                                                                                 the floor
                                                                                 makes a manual change to the channels
    Tilt them downstage a bit
                                                                                 – note the red Rs in the table view
    [Update]      Notice default Make Absolute style     [Enter]                 absolute data is now stored in cue

       Notice that 102 and 105 now have absolute data, no longer
       references a focus palette

### UPDATE A PALETTE

   Other times, we want to update the palette itself. Be aware that when
   you update a palette, every place in your show that uses that palette will
   also be changed. This is useful if the idea behind the palette has
   changed – for example, if the chair is now two feet away from its original
   location for the entire show. You can update the chair focus palette and
   now every place in your show that references that palette will also be
   changed.

      [104] [Enter], tilt down a bit and pan a little                            make a change - note the red R’s
                                                                                 changes stored in FP3, but still manual
      [Update] [Focus Palette] [3] [Enter]
                                                                                 (red) in ‘old’ cue 28 on stage
      [Go To Cue] [Enter]                                                        refreshes the cue

   The console defaults to make absolute, meaning that any changes you
   make to palettes will be stored only in the cue and will not affect the
   palette as a whole. If you want to update the palette, you need to
   specifically call it out on the command line.

## Auto-Mark

### MARKS IN GENERAL

     A Mark automates the process of presetting non-intensity parameters
     to their required state in a cue, prior to fading intensity up. All move
     info about marked fixtures is stored in the reference or source cue.

        A system default setting that is turned on or off at a global level.
        When AutoMark is enabled, non-intensity parameter transitions will occur
        in the cue immediately preceding the cue in which the changes are
        stored, if intensity in that preceding cue is zero or moving to zero.
        Marked cues are indicated by an “M” in the Flags column of the playback
        status display.

           In [Live], Look at the PSD/Cue List                                                     Live moves displayed with ‘L’ flag

           [Go To Cue] [30] [Enter]

           [121] [Full] [Enter], tilt/pan the fixture onto the singer, [At] [5/385] [Enter]        (If strobing, [Home] and then refocus)

           [Record] [31] [Enter]                                                                   (31)

           Press [Back]      and then press [] (Go)                                               notice live move

           [Displays] {Setup} {System} {Cue Settings}
                                                                                                   now see ‘M’ flags and a few ‘D’ flags, but
           Click on {Auto-Mark} <Enabled>               and watch the cue list
                                                                                                   notice all the ‘L’ flags are gone
           [Live],   [Go To Cue] [28] [Enter]

           [] (Go) on Cue 29                                                                      notice Q30 in green on Ch. 103
                                                                                                   intensity of Ch. 121 says Mk and non-
           [] (Go) on Cue 30 – watch Ch. 121 marking
                                                                                                   intensity parameters show Q31 in green
           [] (Go) on Cue 31                                                                      no live move this time

        NOTE      If you begin programming with Auto-Mark enabled, and then disable the feature,
                  all the Auto-Marks in the show are converted to referenced marks.

### ALLOW A LIVE MOVE

        When you want to see a live move on stage, but AutoMark is enabled,
        you can disable AutoMark for an individual cue.
                                                                                                   notice the ‘D’ in the Flags column and L
           [Cue] [31] {AutoMark Off} [Enter]
                                                                                                   for Live move is back
           [Go To Cue] [29] [Enter]

           [] (Go) on Cue 30                                                                      notice no marking

           [] (Go) on Cue 31                                                                      watch the live move

        Go ahead and leave AutoMark on for the rest of the class.

## Cue Attributes

### CUE SOFTKEYS

 When [Cue] is pressed, a softkey {Attributes} (S1) is displayed. When
 {Attributes} is pressed, several new softkeys appear.

### SCENE

 Scenes are a cue organization tool that provides a visual identifier for
 breaks in the show. Scenes allow for quick cue list navigation without
 needing to remember a cue.

### CREATING A SCENE BREAK

      Using Snapshot pop-up, recall Snapshot 1

      [Cue] [1] {Attributes} {Scene}

      The virtual alphanumeric keyboard opens:                    Act 1 [Enter]              adds a Scene marker to cue 1

### SCENE END

      [Cue] [10] {Attributes} {More SK} {Scene End} [Enter]                                  adds an End of Scene marker to cue 10

### CUE RANGE SCENE

                                                                                             adds a Scene marker above cue 11 and an
      [Cue] [11] [Thru] [14] {Attributes} {Scene} Act 2 [Enter]
                                                                                             End of scene marker after cue 14
                 Notice the line above Cue 11 and below Cue 14
                                                                                             adds a Scene marker above cue 15 and an
      [Cue] [15] [Thru] [17] {Attributes} {Scene} Act 3 [Enter]
                                                                                             End of scene marker after cue 17
     Notice as you page up and down on the cue list (PSD), the scene
     break will stay locked as long the cue list is in that scene. Brackets
     around the label indicate that the cue at the top of the screen is not
     the first cue in that scene.

### NAVIGATION TO SCENE

      [Go To Cue] {Scenes}* {Act 2}             [Enter]                                      goes to cue at the top of that scene
       * The CIA opens and shows all the different scene breaks created.

### UPDATING A SCENE

     The {Scene End} softkey can also be used when updating the cues
     in a scene. For example, [Update] <Cue> [5] [Thru] {Scene End}
     will put the last cue of that scene on the command line.
     Don’t forget to add [Q Only/Track] to stop tracking if needed!

### REMOVE A SCENE BREAK

      [Cue] [11] {Attributes} {Scene} [Label] [Enter]                                        to remove a scene

      [Cue] [14] {Attributes} {More SK} {Scene End} [Enter]                                  to remove a scene end

### SCENES IN DIRECT SELECTS

      Add-a-Tab (the {+} sign), select Direct Selects (Tab 4), choose Scenes                 open a Direct Select Tab

      [Go To Cue] «Act 1» - self-terminating                                                 use DS to navigate to scenes
       As with all Direct Selects, if don’t want it to terminate, can press [Shift] & «DS»

### NOTES

       Cues can have notes attached to them. This is more of a long form
       phrase instead of a label which is generally a short reminder of what a
       cue is doing.
        [Cue] [11] {Attribute} {Notes}     Come back and fix red in cyc [Enter]           to add a note
                                                                                          will post notes on command line and open
        Can also do [Cue] [11] [Shift] & [Label]
                                                                                          virtual keyboard
       Notice in the label field of the PSD, a little plus (+) mark has appeared.
       Hover over that label field to see the note as a floating dialog box. OR
       click on the display gear, and under Reorder Columns, check Notes.
         Note: To see pending cue notes, both Display Cue Notes and Display Pending Cue
                Notes should be checked in the gear options.

### CUE ALERTS

       Eos can learn the time between manual [Go] commands and, in future
       runs, display a cue alert timer counting down to the next expected [Go].
       The cue alert timer is informational only and is not a follow time.
        Click on the gear on the far left of the tabs or double click on the PSD tab      to open the PSD Configuration menu

        On the right-hand side, bottom, click on Alert Time (Alert)                       enables the Alert column

        Click outside of the PSD menu                                                     closes the PSD Configuration menu

        [Go To Cue] [1] [Enter]                                                           resets the cue list to cue 1

### LEARNING ALERTS

                                                                                          "Learning Alerts After GO" appears above
            [Live]     [Learn] {Learn Alert Time}
                                                                                          the command line
                                                                                          notice countdown time in red in Alert
            [] (Go) into cue 2
                                                                                          column
            [] (Go) into cue 3                                                           the time is stored and the process repeats

            [Learn]                                                                       to stop learning alert timings

            [Go To Cue] [1] [Enter]                                                       resets the cue list to cue 1
                                                                                          notice countdown time in red in Alert
            [] (Go)
                                                                                          column
           When the countdown is below 5 seconds, the alert time will change
           to gold, and an alert advisory sound will play if enabled.

           The sound is enabled and adjusted in volume in Setup > Device >
           Face Panel > Sounds. The Ion Xe needs speakers plugged into the
           console. The Gio, Ti, and Apex consoles all have speakers.

           When the countdown reaches 0, the time will change to green and
           display until the next manual [Go].

       Instead of learning an Alert, the time can simply be entered directly.
        [Cue] [1] {Alert Time} [15] [Enter]                                               adds an Alert Time to a cue

        [Cue] [1] {Alert Time} [Enter]                                                    removes the Alert Time

### PLAYBACK STATUS DISPLAY (PSD) CONFIGURATION MENU

The following options are available in the PSD Configuration Menu:
On the left side, (Lock Status)
  - Lock Status – allows you to lock the PSD to a certain cue list.
  - Display Cue Parts – displays the individual parts of a part cue.
      When not enabled, the number of parts for that cue will display as
      a superscript number beside the cue's number.
  - Display Cue Links – displays the Link/Loop information.
  - Display Scenes – displays cue scene information.
  - Display Follow/Hang Indicator – displays the Follow/ Hang arrow
      indicator before the cue number of any cue that will be triggered by
      a follow or hang.
  - Display PSD Time Countdown – displays the cue category times
      countdown in the PSD as a cue is fading.
  - Display Master Playback Status – displays the current cue's
      status information. Current and pending cue status
  - Display Fader Ribbon – displays the fader ribbon, which shows
      the current fader page under the Master Playback Status.
  - Display Notes – displays the Cue Notes in a horizontal bar at the
      bottom of the PSD.
  - Display Pending Cue Notes – displays the Cue Notes for the
      pending cue in a horizontal bar at the bottom of the PSD.
  - Break Link to Live/Blind – When selecting the Live/ Blind display,
      the PSD will also come into view if it is currently hidden. This option
      allows you to break the link between the PSD and the Live/ Blind
      displays so that the PSD will no longer come into view when
      selecting Live/ Blind.

  - Set Current as Default – uses the current settings to create a
      default state for all other instances of the PSD.
  - Reset to Default – returns the settings to the default state that you
      created.
  - Reset to Eos Default – returns all settings to the Eos defaults.

  - On the Reorder Columns side, you can choose what data is                   Move Labels up to the top – will appear
      displayed and what order it displays in. By default, all columns           next to cue number
      except Notes and Alert Times will be displayed. The check boxes
      disable or enable the data. Click on the name and use the arrow
      keys (above right) to move columns.

Feel free to set up the PSD the way that you prefer.
 [Record] [{Snapshot}] [1] [Enter]   [Enter]                                    to re-record Snapshot 1

### DISCRETE TIMING

     Timing can be applied directly at a channel or parameter level.

### DISCRETE CHANNEL TIMING

           [Live], [Go To Cue] [31] [Enter] if not already there

           [Select Active] [Out]                                                                       fastest way to a blackout
                                                                                                       records fade to black with block, assert,
           [Record] [Next] [Time] [3] [Block] [Assert] [Label] Fade to Black [Enter]
                                                                                                       and label (32)
           [103] [Time] [10] [Enter]*         [Update] [Enter]                                         records time for channel 103 only in cue 32
              * Notice the small red “t” displayed on the channel. Reminder – manual data! When
              updated, the “t” becomes blue. A ‘+’ is also displayed on the cue in the PSD.
            Hold the Timing Displays button, [Time], (right hand side of the
            board) or hold [About]&[Time] to see the time displayed on the
            channel. It is displayed as ‘D/T’ where D is the Delay time and T is
            the Fade Time.
                                                                                                       watch channel 103 take 10 secs. to fade
           [] (Stop/Back) to cue 31          [] (Go) and watch the timing
                                                                                                       out
                                                                                                       Only channels with discrete timing are
           Hold [Flexi] and press {Time} in the CIA
                                                                                                       displayed
           [{Snapshot}] [1] [Enter]                                                                    To restore to the previous Flexi state

### DISCRETE TIMING BY RANGE

           [Group] [20] [Full] [Enter], [Color Palette] [4] [Enter]                                    set level of cyc full in green

           [Record] [Next] [Enter]                                                                     records next cue (33)
                                                                                                       adds a distributed timing of 1 to 15 secs
           [Group] [20] [Time] [1] [Thru] [15] [Enter]          [Update] [Enter]
                                                                                                       across the channel list, blue “t” and ‘+’
           [] (Stop/Back)      and hit [] (Go)                                                       watch the fade
              Fan Time of 0 thru 15 – the fades start all at the same time but complete at different
              times.

### DISCRETE TIMING WITH DELAY

           [Group] [101] [At] [50] [Enter], [Color Palette] [6] [Enter]                                set level of cyc full in blue
                                                                                                       adds a delay timing of 0 to 3 secs, blue “t”
           [Select Last] [Delay] [0] [Thru] [3] [Enter]
                                                                                                       and ‘+’ in Time column
           [Record] [Next] [Time] [2] [Enter]                                                          records next cue (34)

           [] (Stop/Back)      and hit [] (Go)                                                       watch the fade

### DISCRETE TIMING BY PARAMETER

           [Group] [5] [Full] [Enter]     [Record] [35] [Enter]                                        set levels and records cue (35)

           [Select Last] [Focus Palette] [5] [Enter]

           [Select Last] {Tilt} [Delay] [5] [Enter]                                                    adds a delay of 5 sec to tilt

           [Record] [36] [Enter]                                                                       records next cue (36)

           [] (Stop/Back)      and hit [] (Go)                                                       watch the fade

### CLEAR DISCRETE TIMING

           [Group] [5] [Delay] [Enter]          [Update] [Enter]                                       removes the discrete timing and the ‘+’
              * Notice the + on Focus time has gone away and the duration is reset.

## Multipart Cues

Multipart cues can be used to organize channels and affect their
playback attributes and timing as a group. A cue can have up to 20
parts.

### MAKE A MULTIPART CUE FROM AN EXISTING CUE IN BLIND

    [Live]     [Go To Cue] [36] [Enter]

    [Group] [3] [Full] [Full]   {Color} [Home] [Enter]                             put channels at full, set to warm white

    [Record] [37] [Enter]                                                          creates cue 37

    [Blind], [Format] to Spreadsheet view
                                                                                   switch to Spreadsheet View
         Hold [Shift]&[Format] to hide non-intensity parameters
                                                                                   moves channels into Part 2 – 2nd Enter to
    [51] [Thru] [53] [Part] [2] [Enter] [Enter]
                                                                                   confirm the break into parts
    [54] [Thru] [56] [Part] [3] [Enter]    [Time] [3] [Enter]                      moves channels into new part with time
                                                                                   moves channels into another part with time
    [57] [Thru] [59] [Part] [4] [Enter]    [Time] [4] [Enter] [Label] US [Enter]
                                                                                   and label

### MAKE A MULTIPART CUE FROM AN EXISTING CUE IN LIVE

    [Live] [Go To Cue] [2] [Enter]

    [Group] [2] [At] [Full] [Enter]       make them Magenta (CP7)

    [Update] [Enter]        [] (Go) on Cue 3

    [102] [Full] [Enter] put them on the drums in Light Blue (FP3) (CP5)
                                                                                   moves selected channels to part 2, all data
    [Select Last] [Record] [Part] [2] [Time] [1] [Enter] [Enter]
                                                                                   that has not moved is in part 1
                                                                                   takes only the color parameters of the
    [Group] [2] [Enter] and make them orange (CP2)
                                                                                   channels and moves them into part 3
    [Select Last] {Color} [Record] [Part] [3] [Delay] [5] [Enter] [Enter]          moves selected channels to part 3

    [Clear], press [Last] to see parts in PSD

### CHANGE ATTRIBUTES OF A MULTIPART CUE

    [Cue] [3] [Time] [6] [Enter]                                                   not specifying a part assumes part 1
                                                                                   changes the fade time for the channels in
    [Part] [2] [Time] [3] [Label] Drums [Enter]
                                                                                   part 2 to a time of 3 and labels part
    [Go To Cue] [2] [Enter]        [] (Go) on cue 3                               run cue, watch the fade times.

   [Delete] <Cue> [3] [Part] [3] [Enter] [Enter] deletes part 3 of cue 3.
   When you delete parts of a multipart cue, any move instructions in the
   deleted part are moved to the first available part.

### MULTIPART CUES BEST PRACTICES

     - Unlike discrete timing, Multipart cues show all their timing               Remember: You can’t change the same
          information on the surface and can have labels. This makes                 parameter of a channel twice in one cue.
          complex timing changes easier to identify and track.
     - Use parts to group like-types of data together – all channels that are
          marking, for example.
     - Display Cue Parts can be toggled on or off in the PSD Configuration
          menu.
     - Effects will always be in Part 1. They cannot be put in another part.

## Effects

### WORKING WITH A PRE-PROGRAMMED EFFECT

     Effects 901 – 918 are preprogrammed effects
     [Live], [Go To Cue] [Out] [Enter], [Group] [5] [Full] [Enter], [FP2] [Enter]

     [Group] [5] [Effect] [901] [Enter]

### EFFECT PROPERTIES

         [Effect] [Effect]                                                            to open the Effects Editor

        Effect properties include: {Type}, {Scale}, {Cycle Time}, {Duration/Cycle},
        {Parameters}, {Attributes} as well as {Entry} & {Exit} methods, {Time},
        {Grouping} and {Trail}.

### ENCODERS

            {Axis} – Rotates the shape (Watch the graph as well)
            {Horizontal} – (Default), tap encoder for vertical option
            {Scale} - Size (default 25)
            {Cycle Time} – Speed of the effect                                         Use the encoders. Watch both the viz
                                                                                       and graph on the display

### ATTRIBUTES

            {Grouping} determines how channels currently running the effect
                                                                                       Click on 1 and press [Enter].
```text
            will be distributed throughout the pattern. Grouping defaults to           Watch the effect.
            {Spread}. Every light runs individually, based on the channel order,       Click on 2, 6, 32,…
```
            cycle time, and trail times. A grouping of 2 means every other light
            will move together. Grouping of three means every third light, and so
            on.

### TRAIL

            {Trail} determines how fixtures follow each other through the effect;
            it is a percentage of the cycle time. Trail can be any value from 0-
            200%, even, or solo. The default is Even.
            - {Even} – the fixtures are distributed evenly throughout the
                  path. This is calculated by dividing the cycle time of the effect
                  by the number of channels. Will put Trail 0 on the command
                  line.
            - {Solo} – puts Trail 100 on the command line, requires an
                  [Enter]. The first fixture executes the entire path. Then the
                  second fixture does,...
            - {10%} - {90%} – when the first fixture is 10% through the
                  effect, the second fixture will start the effect. Therefore, the
                  fixtures will trail n% behind each other, as a percentage of the
                  cycle time.

### STOPPING AN EFFECT

           [Live] [Group] [5] [Out]                                                   takes out intensity, but effect still running

           [Group] [5] [Effect] [Enter]                                               stops the effect on selected channels

            OR    [Effect] [901] [At] [Enter]                                         stops selected effect

            OR    [Stop Effect] [Enter]                                               stops all effects

            On Apex consoles, [Shift]&[Effect] is the Stop Effect Command.
            Also [Effect] [#] [At] will post Stop Effect on the command line.

### COPY AN EFFECT

   You can copy effects to another effect location and modify them from
   there. This will leave the original effect untouched.

     [Effect] [Effect]

     [Effect] [901] [Copy To] [2] [Enter]                                         copies the effect to a new number

     [Label] [Label] Modified Circle [Enter]                                      can also label the new effect

### DELETE AN EFFECT

     [Delete] [Effect] [2] [Enter] [Enter]                                        deletes the effect

   If you delete one of the default effects (901 through 918), that effect will
   return to its default values.
                                                                                  deletes the effect - in this case, returning it to
     [Delete] [Effect] [901] [Enter] [Enter]
                                                                                  its default values

### CREATE A RELATIVE EFFECT

Relative effects are mathematical based effects that can run on any
fixtures that have similar parameters. A focus effect runs on any
fixtures that have pan and tilt parameters.

### FOCUS EFFECT

     [Effect] [Effect]

     [Effect] [901] [Copy To] [2] [Enter]                                         create a new effect 2

   Graph: X is Pan; Y is Tilt; center is where the light is focused.

     {Edit}, then {Clear All}, left click & drag to create a closed path          draw something – a heart, clover

   The following Tools are also available to edit the curve:
     - Draw – draw line for linear effect or append points to focus effect
     - Select – select points of the curve (if none selected, all are
         changed)
     - Move – move selected points, can also phase-shift the curve of
         linear effects in steps of 30 degree
     - Form – scale linear effects on y-axis and focus effect separately
         on x-and y-axis
     - Scale – increase or decrease overall size of the effect on both axis
     - Rotate – rotate focus effects around center of the selected points
   The following Actions are available when editing the curve:
     - Clear Selection – removes selected points, defaults to all points
     - Smooth – smooths the selected points
     - Mirror Hor. /Vert. – mirrors the curve horizontally or vertically
     - Subdivide – adds one point on each selected segment (useful to
         move that point or change the behavior of smooth)
     - Remove – removes the selected points
     - Undo – undoes the last operation
     - Redo – redoes the last operation

     Don’t forget to hit {Apply}!      {Grouping} {1} [Enter]                     easier to see them all move as one

     [Live] [Group] [5] [Full] [Enter] [FP2] [Enter] [Effect] [2] [Enter]         if not already there

### CREATE A LINEAR EFFECT

       A linear effect does not have to be parameter specific. Rather it can
       simply be a reference to a linear diagram which can be applied to any
       parameter.

         [Effect] [Effect]

         [Effect] [12] [Enter]     {Linear},   {Edit},   {Patterns}                    creates a new linear effect

         Select the NTX Flicker Pattern                                                in patterns, 2nd row, 4th one

       The tools are slightly different for a linear effect:
         - Draw – draw a new line for linear effects or append points to focus
         - Select – select points of the curve (if no points are selected, all are
             changed)
         - Move – move selected points, can also phase-shift the curve of
             linear effects in steps of 30 degree (only if there is no partial
             selection)
         - Form – scale linear effects on y-axis and focus effect separately on
             x-and y-axis
         - Gamma – apply a log function to the curve (linear effects only)

         Don’t forget to hit {Apply}!

         [Live], [Group] [5] [Home] [Enter] [At] [50] [Enter], [Effect] [12] [Enter]

         [Effect] [Enter]                                                              to stop effect

         [Effect] [Effect]

         {Duration} [3] [Enter]                                                        Short flash – maybe a lightning effect

         [Live], [Group] [5] [Effect] [12] [Enter]

         [Clear] [Sneak] [Enter]

### COLOR EFFECT

       Color effects impact only color parameters. Like Focus Effects, they
       default to a circle pattern, with hue and saturation offsets. The
       {Parameters} key within the Effects Editor displays the various color
       mechanisms used in any patched channels.

### CREATE AN ABSOLUTE EFFECT

Absolute effects are like step-based effects in that they contain a
series of sequential actions. However, unlike step-based effects,
absolute effects can be applied to any fixture that contains the
parameter(s) specified in the effect. For example, an absolute effect
that affects intensity can be applied to virtually any fixture; an absolute
effect with color palettes as actions can be applied to any fixtures that
have data stored in those color palettes.

### WITH COLOR

      [Effect] [Effect]      [Effect] [3] [Enter]                                creates a new effect

      <Type> {Absolute}                                                          selects Absolute and changes display

      {Action} [1] [Thru] [7] [Enter] [Enter]                                    creates 7 actions

      [Page►] to {Level} column,

      [Color Palette] [1] [Thru] [7] [Enter]                                     enters CP1 – 7 into the 7 actions

      [Live] [Group] [2] [Full] [Rem Dim] [Enter]       [Effect] [3] [Enter]     plays effect across downlights

      [Group] [9] [Full] [Enter] [Effect] [3] [Enter]                            effect runs on sidelights

      [Group] [101] [Full] [Rem Dim] [Enter]                                     brings up the cyc

      [Effect] [3] [Enter]                                                       plays effect running out from center

      [Group] [102] [Effect] [3] [Enter]                                         plays effect running in toward center
       Watch the effect on the color picker display too!
       Play with grouping on this effect – note that a grouping of 1 will do a
       solid color change of the whole cyc.
      [Clear] [Sneak] [Enter]

### WITH INTENSITY

      [Effect] [Effect]

      [Effect] [4] [Enter]                                                       creates a new effect

      <Type> {Absolute}                                                          selects Absolute

         Check out the default Absolute effect - intensity based
                                                                                 [At] [Enter] puts Bkgrd in the Action
         Action 1 = 0 and Action 2 = Background (Bkgrd)

      [Live], [Go To Cue] [7] [Enter]                                            bring up a cue onstage

      [Select Active] [Effect] [4] [Enter]                                       replays the effect on the cue levels

      [Effect] [Effect]

      Change Action 1 = Full and leave Action 2 = Background (Bkgrd)             see how the effect has changed

      [Live]   [Go to Cue] [Out] [Enter]                                         clears effect and cue

### WRITING EFFECTS INTO CUES

              [Go To Cue] [37] [Enter]

              [Group] [3] [Effect] [3] [Enter]     [Record] [37.1] [Enter]                          effect number shown in FX on PSD (37.1)

              [Group] [5] [Effect] [901] [Enter]     [Record] [Next] [Enter]                        see how the effect has changed (37.2)

              [Group] [5] [Focus Palette] [1] [Enter]

              [Group] [3] [Stop Effect] [Enter]      [Record] [Next] [Enter]                        clears effect and records cue (37.3)

              [Go To Cue] [37] [Enter]     and run the cues

              [Go To Cue] [Out] [Enter]

## About “About”

     “About” displays detailed information for nearly every target type.
                                                                                                    on a clear command line, About shows
       [Shift]&[Clear]          [About]
                                                                                                    information about the current device
         In the CIA, in the center, {Device} displays the following information:
```text
              System address count
              Software version
              Fixture library version
              Copyright & Licensing notifications

              Device name                                                Number of patched addresses
              Assigned as (Primary/Backup/Client/Offline)                Number of unpatched defined parameters
              User ID                                                    Number of patched channels
              Priority (ACN and Net2)                                    Number of cues
              Networks – multiple networks and IPs listed                Allowed output addresses
              Defined Parameters                                      

       In the center (left), {Session}.                                                             shows Devices types, status, and address
```

         This display shows status information and IP address for any
         devices.101

       {Processors}                                                                                 shows processor status and universes

         This display shows status information and IP address as well as
         universes and load information for any processors connected to the
         system.

       {What’s New}

         A QR code for latest software, libraires and assets as well as a quick link
         to the Manual (Tab 100).
           Please note that the manual is not available on Windows XP devices but is available as
                  a download from the web site.

       [101] [Enter]                                                                                lots of information about the channel

         Current values, Background, Moves, Usage, Patch, Fixture Notes and
         Lamp Controls
       To exit, press [About] again or [Displays]                                                   to bring back CIA/Browser

## Magic Sheets

Magic Sheets is a tool that allows you to create a custom layout to
display and to interact with your console functions in different ways.

### OPEN A NEW OR BLANK MAGIC SHEET

  Use Add-a-Tab (the {+} sign) and select the magic wand (Tab 3)

  Double click on or touch “New Magic Sheet”
OR
  [Displays] {Magic Sheet} [1] [Enter]

### GETTING STARTED

     Notice you are in Blind with the Editor open. The Editor button (< or >) on
     the right-hand side of the magic sheet display will open or close the
     editing tools. When the Editor is closed, you are back in Live.

### MOUSE NAVIGATION TOOLS

       Use your mouse wheel                                                        to zoom in and out

       Right click and hold                                                        to pan or drag the display

### UNDO AND REDO

     Use {Undo} and {Redo} to revert and restore changes while in the Magic
     Sheet Editor. Hover over it to see a description of the action to be
     undone or redone.
     Standard keyboard shortcuts work:
       - Undo - CTRL+Z or CMD+Z
       - Redo - CTRL+Y or CMD+Y
     Closing and re-opening your Editor will also create an Undo Restore
     Point.

### PLACE AN OBJECT

     We are going to make a Magic Sheet that looks something like this:

                                                               (Larger version on page
                                                               48)

### SIMPLE TOOLS

         Click in the Object Library on the rectangle      8th row, middle

         Drop it on the worksheet
          - Green Handle for proportional stretch
          - Blue handles for edge stretch
          - White dot handle for rotate
          - Pink handles for individual point move
         Leave as a rectangle, stretch it to be double the width as the height

### TARGET ASSIGNMENT

         In the Object Properties, click on the drop down menu under Target:
```text
               Address                    Beam Palette         Channel (default)
               Channel (By Address)       Color Palette        Cue
               Cue Active                 Cue Pending          Effect
               Fader                      Focus Palette        Group
               Intensity Palette          Macro                Magic Sheet
               Pixel Map                  Preset               Processor
               Response Io Relay          Scene                Snapshot
               Submaster                  User                
```
               Console Button – second field, drop down of all console buttons
               Softkey – second field, drop down of softkeys 1 - 6, including More
                Softkeys
               Command – write command in command field, label in text field
               Zoom - when clicked, the view will zoom in to show all objects within
                that object’s group.
               Selection - when clicked, all other objects within that object’s group
                will be selected.
          Make the target ‘Group’ and the target number 1

### COLOR PROPERTIES

          - Outline line weight
          - Outline color
          - Object fill color
              - Brightness (saturation) bar on right side
              - X is no fill or clear
         Select a line weight and a fill color

        {Change Shape} allows you to quickly change the object shape without
        having to drag a new object in or redo all the properties.

### FIELD SELECTION

Up to six different fields of information can be displayed. Field options
are context sensitive based on the object.
```text
         None
         Target ID
         Target Name
         Label
         Icon
```

  - Abc or Font icon - adjust the font type, size, color, style (bold, italic)
  - Alignment icon - position of the field

  Make Field 1 the Target Name, Field 2 the Target ID, and Field 3 Label

The object might look something like the image to the right.
  With the Group object selected, CTRL+C and CTRL+V                                                to copy and paste

  Select the new Group object, CTRL+X or [Delete]                                                  to remove

Below the Fields is a check box for Interactivity as well as displays of
Position, Size and Rotation
  - Interactive – toggles on or off. Objects set to not-interactive cannot
          be selected and will only display information.

### CREATE AN ARRAY

You can create multiple of the same type of object quickly, using the
Array tools.
  Select the original Group object

  Click on the Array icon

  Leave as a Rectangle, drop down shows circle option as well

  Change the number of columns to 2, rows to 5, and spacing to 15 on both

  Click OK

### AUTO-NUMBER

  Click on the Renumber Tool

  Target should be Group and Next = 2, Increment = 1

  The first object should still be 1, so click on each of the other objects
  across the first row, and then the second row, to renumber the groups
          Note that the pointer will display the target that will be assigned on the next click.

  Don’t forget to hit Done!

  Back on Layout Toolbar, change back to Normal pointer (simple arrow)

### QUICK TOOL MENU

        Right click on the Magic Sheet while in Editor mode
         - Cut and Copy
         - Paste Renumber
         - Paste Duplicate
         - Renumber by Click
         - Renumber in item
         - Group or Ungroup
         - Bring Forward or Send Backward
         - Clear Selection
         - Grid Toggle

### INSERTING CHANNEL OBJECTS

         Click on the Fixtures Library tab

         Select the Moving Wash – 3rd down on left side, drop it on the workspace

         Rotate it to face upstage

         Make the target as ‘Channel’ and the target number as 101

         On Field 1, Target ID, select Georgia as the Font, make the Font Size 25

       You can also choose a color for the font. Be aware that some fields use
       system colors like Channel Intensity levels so those will override any
       colors that are selected. There are also options for Bold, Italic or
       Underline.
         On Field 2, Intensity, set the Justification (Checkerboard icon) to behind
         the fixture (Top Center)

         Change font size to 25

         Remove Field 3 data – select None

         Click on the Object Fill Color icon

         Click on both ‘Link to Target Color’ and ‘Link to Target Intensity’

         With the fixture selected, copy, and paste it 4 more times

         Click on the Renumber Tool

         Target should be Channel and Next = 102, Increment = 1

         Renumber the 4 new fixtures and don’t forget to hit Done!

         Move an end fixture farther away from the rest

         Select all 5 fixtures

         Using the Align Tools, align Middle and then Distribute Horizontally

### FLIP

       Add a Channel object, copy and paste it 3 more times                         to copy and paste (CTRL+C & CTRL+V)

       Move them into a horizontal line

       Select all 4

       Click on Flip in the tool bar next to Mirror                                 popup appears, new position is previewed

       Select {Accept Flip} to apply or {Cancel Flip} to close without changing

       Can flip the objects horizontally or vertically

       Flip Text Position is selected by default                                    to keep text upright when flipping

       Flip Target Field Positions is also selected by default                      to keep field positions upright

       {Cancel Flip} and delete the objects

### INSERTING PALETTE OBJECTS

 Click in the Images Library, then click on Import Image icon

Images can be imported into magic sheets for two different purposes:
background images or as objects.
  - [Gobos] – a direct link to the console gobo library, populates based
        on the fixtures patched in the show
  - Accepted image formats: .bmp, .gif, .ico, .jpg, .pbm, .pgm, .png,
        .ppm, .svg, .svgz, .tga, .tiff, .xbm, and .xpm. (max 1920 x 1920)

 Select the [Gobos] folder, double click the HES Gobo Wheel 37 Fracture             to add the gobo to the Image Library

 Click on it and drop it in the Magic Sheet in the bottom left corner

 Make the target ‘Beam Palette’ and target number is 5                              to create a new Beam Palette 5

### BACKGROUND SETTINGS

 Click on the fourth tab (Gears) for the Background Settings
  - Interactive - toggles interactivity on or off for the entire magic sheet.
        If toggled on, all objects respect their per-object settings. If off, no
        objects will be interactive, regardless of their settings.
  - High Quality – Checked by default. If unchecked, optimizations will
        be made to the graphics, which may improve performance and
        reduce lag, but at the expense of image quality.
Display Behavior is similar to tab behaviors. The options are Normal,
Channel, or Control.
Live and Blind Backgrounds allows you to create different
backgrounds to be used for Live and Blind Magic Sheets.
  - Solid – use Red, Green, and Blue values to select a color or click
    on the small black square next to ‘Red’ to open a color picker,
  - Gradient – select top and bottom colors and display will scale
    between the two colors
  - Image – click on the image icon to select a background image, set
    width, height and opacity, options for inverted or normal
   - Currently accepts image files: jpg, tif, bmp, png
 Select Gradient in the pull-down menu

 Choose a top color and a bottom color

### LET’S ADD OTHER OBJECTS

        Back in the Objects Library, select the Color Palette Object – 2nd down on
        the right – and add it to the Magic Sheet below the fixtures

        Stretch it out a bit longer

        Make Field 1 the Label and set font size to 20, and leave other fields empty

        Under Color Fill, Link to Target Color                                         uses color of highest channel in Palette

        Create a rectangle array of 7 columns, 1 row with 25px spacing

        Select all 7 Color Palettes, then make the Field 1 text 20pt and black

        Select a Square object, stretch it a bit, maybe rotate it

        Target should be Focus Palette and Target number is 1

        Fields should be Target Name, then Target ID and third the Label

        Copy and paste 4 more times and arrange like stage focus areas

       Remember the Direct Select icons we added to a couple of our Groups?
       We can display those on our Magic Sheets as well.
        Select all 10 Group rectangles.

        In Field 4, change it to Icon. Leave it centered. Close the Editor             to see the icons on Groups 3 and 4.

        Reopen the editor. Font size on Field 4 adjusts the size of the Icon.

       Note that all the rectangles show the Icon symbol, but when we closed
       the Editor, we only see 2 icons – only two groups have icons assigned to
       them.
        Click in the Object Library, scroll down and select the arrow

        Add it to the Magic Sheet next to the beam palette                             puts gobo in the Image Library

        Using the pink dots to flare out the tail, white line and white fill           No properties just yet

        {Quick Save}!!

### CONSOLE BUTTONS

        Add a Square Object, make it a bit bigger

        In the Target drop down, towards the bottom, select ‘Console Button’

        Drop down menu below Target says None. Find ‘Full’

        Change Field 1 to Target Name

             Add 2 more console buttons: ‘Rem Dim’ and ‘Enter’                         use Ctrl-C and Ctrl-V again

### HOW IT WORKS IN LIVE

  Close the Editor                                                                          now in Live
      Notice all the labels are visible and the FOH lights are dark because they have no
      level. Also, the Color palettes automatically take the color that is stored in them

Use the Magic Sheet now to do the following:
  Click on Group 5 (FOH Movers) Full Enter                                            to bring FOH Movers up

  Click on the Color Palette objects - Red Orange Lt. Blue                            notice channel objects are changing color

  Click on Singer (FP2)

  Roll down intensity wheel                                                                 channel objects slowly fade to black.

The magic sheet might look like this:

                                                                                               (Larger version on page 48)

### MAGIC SHEET NAVIGATION

### MULTI-TOUCH GESTURES

       The following multi-touch gestures can be used with an external multi-
       touch touchscreen or the onboard monitors on other Eos family
       consoles.
         - Scroll – touch with two fingers to move around the page.
         - Zoom In – touch with two fingers and then move your fingers away
             from each other.
         - Zoom Out – touch with two fingers and then move your fingers
             toward each other.
         - Zoom to All – double tap with two fingers.
         - Open Magic Sheet Browser – tap with three fingers.

### DISPLAY TOOLS

        Right click or tap on the Magic Sheet tab                                 to see configuration settings

       You can also click on the Gear tab for the same options.
         - < Add View > – for each magic sheet, multiple views may be
           created, then < and > allow for scrolling through the views.
         - Save Screenshot – saves a png image of magic sheet to a USB
         - Magic Sheet Browser – opens a filmstrip view of magic strips to
           scroll through.
         - Lock / Unlock – locks the magic sheet so it cannot be zoomed or
           panned. also hides the edit chevron (to edit must unlock)
         - Zoom to All – zooms to show all objects on magic sheet
         - Zoom to Selection – zooms to show all selected objects
         - Center to Selection – centers the display on the selected objects
           without changing the zoom
         - Show Reference Labels - labels displayed rather than target
           number
         - Limited Expand Mode - also known as Full Screen Mode – hides
           the edit chevron but also suppresses the rest of the user interface.
          - Upper right corner – 3 dots flashing – console is operational
          - [Shift]&[Displays] take you back
          - Also, can {Disable Keyboard Input} and {Lock Fader Page}
             when in Limited Expand mode.

        -

## Appendix 1 – Scroll Setup

      Generic Scrollers (Channels 151 – 158)

1     Open Frame

2     R010 – Medium Yellow

3     R027 – Medium Red

4     R339 – Broadway Pink

5     R351 – Lavender Mist

6     R359 – Medium Violet

7     R370 – Italian Blue

8     R038 – Light Rose

9     R065 – Daylight Blue

10    R085 – Deep Blue

11    R090 – Dark Yellow Green

### DON’T FORGET TO HIT DONE WHEN FINISHED!

## Appendix 2 – Magic Sheet

## Appendix 3 – PSD Flags

Flags can be applied to cues to change specific behaviors. Flags
can be set for “Mark - M”, “Block - B”, “Assert - A”, “Preheat - P”,
“AllFade - AF” and “Moves - MV.”

  M - Mark (Auto Mark Disabled)

     m    A cue that has been set as a Mark cue but has nothing marking in it.

     M    A cue that has been set as a Mark cue and has channels marking in it.

     R    A Reference cue, which stores move instructions for channels that are being marked in a previous Mark cue.

     +    A cue that is both a Mark cue (with or without marking channels) AND a Reference cue.

          A broken Mark. Always appears in the cue directly before a Reference. A Mark gets broken when the
          channels become Active between their Mark cue and their Reference cue. When a Mark is broken, the
     x
          software will use Auto Mark behavior to try to get the parameters marked in the cue immediately preceding
          the Reference cue.
  M - Mark (Auto Mark Enabled)

          A cue that the software is using for an Auto Mark and has channels marking in it. The 'M' always appears in
     M
          the cue directly before the Reference (which is not indicated when Auto Mark is enabled).

     D    A cue where Auto Marks have been disabled, allowing live moves.
  B - Block
```text
     B    Cue-Level Block
     b    Discrete channel/parameter Blocks are present
     b    Auto-Blocks are present
     I    Intensity Block
```
  A - Assert
```text
     A    Cue-Level Assert
     a    Discrete channel/parameter Asserts are present
```
  P - Preheat

     P    A cue that is set for Preheating. The cue before it will use each channel's preheat value from patch.

  AF - All Fade

     *    Plays the cue in an All-Fade mode, which sends any intensities that are not owned by the cue to zero.

  MV - Moves
          A cue with Dark Moves. There are channels that have an intensity of zero and non-intensity moves stored in
     D
          this cue. This is where you might want to delete unnecessary moves.

          A cue with Live Moves. There are channels that have an intensity of zero stored in the previous cue, and an
     L    intensity above zero and non-intensity moves stored in this cue. This is where you might want to Mark
          channels to a previous cue.

     +    A cue where both Dark Moves and Live Moves are present.
  R - Release
          Like Make Null, but releases data to a background state or out. Tracks through until removed or a move
     R
          instruction happens.

### HELPFUL SUPPORT AND TRAINING LINKS

```text
         ETC Support Website                         ETC Technical Support                     Community – ETC Consoles
All the support and training resources       Contact our 24/7 technical support            Hop on the ETC forums to ask the
you might need in one handy place            team to help troubleshoot your ETC            user community your questions
                                             gear                                          about Eos
   https://www.etcconnect.com/support        https://www.etcconnect.com/Contact/Tech       https://community.etcconnect.com/con
                                                        nical-Support.aspx                   trol_consoles/eos-family-consoles/

     Video Tutorials – Eos Family               Support Knowledge Base Articles                       ETC Training
     Experience hands-on Eos training          Get quick answers to your technical          Find in-person training opportunities
    anywhere, anytime with the series of     questions with support articles created by      near you, as well as other learning
           videos and workbooks                            ETC experts                                   resources
https://www.etcconnect.com/Support/Tutori      https://support.etcconnect.com/ETC          https://www.etcconnect.com/Training/
```
   als/Eos-Family-Videos/Overview.aspx

```text
         ETC Search Manuals                            ETC LearningStage                          ETC Custom Training
 Search for manuals, datasheets, release       Take part in a variety of online training      ETC offer multiple custom training
  notes, and more on the ETC website            courses for technicians and operators              options to fit your needs
  https://www.etcconnect.com/Search-         https://learningstage.etcconnect.com/learn    https://www.etcconnect.com/Support/T
   Documentation.aspx?DocType=137                                                           raining-Events/Custom-Training.aspx

     Eos Family Training Materials                   Educational Resources
Find all of the Eos family Learning Series   These free materials provide a overview of
workbooks and training materials in one              essential lighting concepts
```
                   place
https://www.etcconnect.com/workbooks/        https://www.etcconnect.com/Support/Traini
                                               ng-Events/Educational-Resources.aspx

Corporate Headquarters  Middleton, WI, USA  Tel +608 831 4116  Service (Americas) service@etcconnect.com
London, UK  Tel +44 (0)20 8896 1000  Service (UK) service@etceurope.com
Holzkirchen, DE  Tel +49 (80 24) 47 00-0  Service (DE) techserv-hoki@etcconnect.com
Hong Kong  Tel + 852 2799 1220  Service (Asia) service@etcasia.com
Paris, FR  +33 1 4243 3535
Web  etcconnect.com  © 2025 Electronic Theatre Controls, Inc.  Trademark and patent info: etcconnect.com/ip
Product information and specifications subject to change. ETC intends this document to be provided in its entirety.

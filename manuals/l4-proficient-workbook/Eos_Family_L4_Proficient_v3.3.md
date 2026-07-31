# Eos Family Console Programming — Level 4: Proficient Workbook (v3.3C)

- Source : PDF officiel ETC, « Eos Family Console Programming — Level 4: Proficient Workbook (v3.3C) », V3.3C, publié 2026-02
- Fichier source : [`source/Eos_Family_L4_Proficient_v3.3vB.pdf`](source/Eos_Family_L4_Proficient_v3.3vB.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select


Eos Family Console Programming

             Level 4: Proficient

                        Workbook
                                     V3.3C

            www.etcconnect.com/education

                            Released: 2026-02

## Table of Contents

ETC permits the reproduction of materials in this manual only for non-commercial
    purposes. All other rights are reserved by ETC.

     Eos Family Console Programming Level 4

## Purpose of the Class

    This class is intended for people who are well versed in Eos Family terminology,
    already know the layout of the desk, and are experienced conventional and
    intelligent fixture programmers. This class is intended to build on your
    knowledge, and make you faster.

### LEARNING OBJECTIVES:

        After completing this class, users should be able to:
        - Use advanced palette and preset modifiers
        - Create more complex Macros
        - Understand and work with multiple cue lists and multiple cue list
               playback
        - Feel comfortable with the Cue List index and its properties
        - Take advantage of the three states of Capture
        - Understand Priority settings
        - Learn about Custom Encoder Mapping
        - Be more effective using Fader Configuration
        - Use the virtual faders and playback filters
        - Take advantage of additional Snapshot tools
        - Understand and use the various color spaces and tools of the Color
               Picker

### SYNTAX ANNOTATION

        - Bold Browser menus
        - [Brackets]      Facepanel buttons
        - {Braces}        Softkeys and direct selects
        - <Angle brackets>        Optional keys
        - [Next] & [Last] Press & hold simultaneously
        - «Direct Select» Direct Select button press
        - MS Object     Object on a Magic Sheet

        - Play Icon      Link to video on ETC’s YouTube Channel -
               ETCVideoLibrary

### HELP

        Press and hold [Help] and press any key to see:
        - the name of the key
        - a description of what the key enables you to do
        - syntax examples for using the key (if applicable)
        As with hard keys, the “press and hold [Help]” action can be also used with
        softkeys and clickable buttons

### THE MANUAL

        The manual is available on the console, Tab #100.

            Click on Add-a-Tab (the {+} sign) , select Manual

            Hold [Tab] & press [100]
        Please note that it is not available on Windows XP devices, but is available as a
        download from the web site.

## Palette & Preset Modifiers

Palette & Preset Modifiers                                                                   START THIS DAY IN LEVEL 3 COMPLETE!

### BY TYPE PALETTES

When building palettes, often the same information is desired for all fixtures of
the same type. By Type palettes use the information from a single fixture to
populate all other fixtures of that type.

  [Go To Cue] [104] [Enter]

                                                                                             choose a new mixed color with the FOH
  [102] [Full] [Rem Dim] [Enter], use the color picker, make it Amber                        movers

                                                                                             records the color data into a “By Type”
  [Select Last] [Record] [Color Palette] [14] {By Type} [Label] Amber [Enter]                color palette

  Recall Snapshot 4

  Double tap the next open Custom Direct Select                                              places CP14 Amber on the DS

```text
  Touch «FOH Movers» (G5) [Full] [Full],                                                     notice the colors all match even though the
  [Focus Palette] [1] [Thru] [5] [Enter]                                                     palette was created with only one of the
  «Amber» (CP14)                                                                             fixtures (102)
```

                                                                                             notice the blue default channel and all
  [Blind] [Color Palette] [14] [Enter]    Be in Table view, [101] [Enter]                    other channeles are magenta

    By Type palettes are created with “default” channels. The default contains the
    data, and all like-fixtures can follow that data to accomplish the same task, like mix
    to a color. One default per fixture type. Generally the lowest number channel of
    each fixture type will be the default channel, unless specified like above.

  [Live] [Group] [7] [Full] [Full] [Home] [Enter]
                                                                                             (on 2nd page of color encoders)
  Using the second fixed color wheel, select Amber
                                                                                             records all color data of the channels into
  [Select Last] {Color Select 2} [Record] [Color Palette] [31] {By Type} [Enter]             the color palette
        We didn’t specify a default channel, but a default was created for the
        fixture type.

    Eos Family Console Programming Level 4

### EDITING BY TYPE PALETTES IN BLIND

      In Blind, default channels are blue, all like-fixture channels are magenta, and
      discrete channels are white.
                                                                                            notice the blue default channel and the
       [Blind] [Color Palette] [31] [Enter]                                                 white channels that have discrete data

      If a single channel is not specified when recording a {By Type} palette, the lowest
      number channel of each fixture type will be the default channel.
                                                                                            removes discrete data that is the same as
       {Cleanup} [Enter]                                                                    the default channel - it leaves discrete data
                                                                                            that is different from the default
       [Label] Wheel Amber [Enter]

### DISCRETE CHANNELS

       [Color Palette] [14] [Enter]
                                                                                            makes channel 101 the new default
```text
       [101] {By Type} [Enter]                                                              channel - old default becomes discrete
       [102] [At] [Enter]                                                                   removes discrete data on this channel
```

       [Live]
                                                                                            change the color of only this fixture in the
       [104] [Enter], using encoders, add a bit of magenta                                  Color Palette
       [Select Last] [Update] «Amber» (CP14)
                                                                                            notice the discrete data (104 no longer
       [Blind] [Color Palette] [14] [Enter]                                                 follows the default channel)

### MAKE CHANNELS DISCRETE

                                                                                            convert 105 to discrete data, even though
       [105] {Discrete} [Enter]                                                             the values match the default
                                                                                            only values that match the default can be
```text
       [Clear] {Cleanup} [Enter]                                                            cleaned up, 104 magenta is still discrete
       [104] [At] [Enter]                                                                   force 104 to match the default channel
```

                                                                                            channels 131 thru 138 weren’t patched
       [Color Palette] [1] [Enter]    Scroll to see Ch. 131 thru 138                        when the palette was created
                                                                                            making it By-Type populates any matching
       {By Type} [Enter]                                                                    fixture types with color data
       {Cleanup} [Enter]
                                                                                            make all palettes By-Type and clean up
       [Color Palette] [2] [Thru] [13] {By Type} {Cleanup} [Enter]                          discrete data, notice small ‘t’s on palettes
                                                                                            see that 131 thru 138 now have data for
       [Next]… [Next]… [Next]… [Next]                                                       fixtures added after recording palettes
                                                                                            editing the default channel will change all
```text
       [Color Palette] [5] [Enter]    [141] [Enter]                                         the follower channels
       [141] {Red} [25] [Enter]                                                             see how all other channels follow

       [Undo] [Enter]                                                                       Don’t leave red in Blue Color Palette!
```

### UPDATING BY TYPE PALETTES

    When updating a By Type palette, it is not necessary to know the default channel
    number. Select any of the channels and append the {By Type} to the command
    line. The command will not work if the channel selected has discrete data already
    associated with it.

        [Live]

        [Group] [2] [Full] [Rem Dim] [Enter], using encoders to add a little red        in color palette 6 to begin with
                                                                                        notice the update window shows which
        [Select Last] [Update] [Color Palette] [6] {By Type}    [Enter]                 channel is the default and which channels
                                                                                        will be updated
    In the update dialogue box, the channel in brackets is the default channel.
                                                                                        because By Type was added to the update
        [Blind] [Color Palette] [6] [Enter]                                             command, no discrete data was created

### PALETTE MODIFIER BEST PRACTICES

    - By Type Palettes can save you time by allowing you to create content
           before your full rig is installed. Also when adding new fixtures to your
           rig, content is already created
    - With Template showfiles, saves time with each new show.

### ABSOLUTE PALETTES

When a Palette or Preset is made absolute, the values can no longer be
referenced. When recalling an absolute palette, the referenced data will not be
recorded into a cue or nested into a preset – it will always post absolute data
when recalled.
  Double tap [Intensity Palette] or Add-a-tab {+}                                       to open the Intensity Palette List

  [Intensity Palette] [1] [Thru] [2] {Absolute} [Enter]                                 makes Intensity Palettes 1 & 2 Absolute
                                                                                        applies the absolute data/values from
  [Live] [Group] [22] [Intensity Palette] [2] [Enter]                                   Intensity Palette 2 to the channels
                                                                                        clear the command line and turns off
  [Clear]        [Intensity Palette] [2] {Absolute} [Enter]                             Absolute

### ABSOLUTE PALETTE BEST PRACTICES

    - Intensity palettes are good candidates to be made absolute palettes,
           so intensity data is always stored in cues as non-referenced data
    - Great to use as “starting” point palettes, such as a quick way to get
           lights focused in the area, before tweaking them and recording
           actual focus palettes

     Eos Family Console Programming Level 4

### LOCKED PALETTES

    Once a Palette or Preset is locked, data can not be accidentally modified. It
    cannot be updated through an Update All command.
    To update a locked target from Live, you have to use channel selection and the
    target in the command line.
      [Clear]                                                                                    to clear the command line

      [Focus Palette] [11] {Lock} [Enter]                                                        makes Focus Palette 11 locked

       In the Direct Select, an ‘L’ is in the corner to indicate locked.
                                                                                                 turns on channels and places them in a
      Touch «OS Movers-Wash» (G7), [Full] [Full],                                                focus palette and color palette

      Touch «Down Center» (FP11), «Lt Blue» (CP5)
                                                                                                 records the references for the channels in a
      [Record] [117] [Time] [3] [Enter]                                                          cue

      [Select Last] , Move Pan & Tilt                                                            change the focus of the lights
                                                                                                 updates the changes to the cue, but forces
      [Update] {All} Look at the Update Dialogue Box            [Enter]                          absolute values into the cue
       Notice in the update dialogue box, the ‘L’ in parenthesis that indicates that this is a
       locked palette.

      [Select Last] «Down Center» (FP11)                                                         places fixtures back in Focus Palette 11

      Move Pan & Tilt                                                                            change the focus of the lights

       Locked palettes can be updated by specifically calling the channels and the record
       target.
                                                                                                 saves changes back to Focus Palette 11 –
      [Select Last] [Update] [Focus Palette] [11] [Enter]                                        still manual till update the cue

      [Update] [Enter]                                                                           to update cue

### LOCKED PALETTE BEST PRACTICES

       - Common use of locked palettes is locking them so that when they
            are stored in a cue or nested in a preset, they are not accidently
            recorded over when you update the cue or preset.

## Advanced Macros

### MACROS

 [Learn] [11] [Enter]
                                                                                    writes a macro to reset all faders to their
```text
 {Fader} [1] [Thru] [Home] [Enter] [Learn]                                          home positions
 [Shift] & [Clear]                                                                  clears command line
```

 Move several faders away from their current position
                                                                                    Motorized faders move automaticllay,
 [Macro] [11] [Enter]                                                               non-motorized will need to be moved
      On non-motorized faders, the flashing arrow in the display will show how to
       reset the fader.

### MACRO MODES

  Macros can be called to run on or off the command line.
  - {Foreground} – Macro commands post to the command line.
        Because devices with the same user share a command line, it will run
        on all devices with the same user.
  - {Background} – Macro commands run, but do not post to the
        command line. Only runs on the device where it is called.
  - {Default} – If called manually (by a programmer calling the macro), it
        will post as Foreground. If called by an execute or by the system (like
        a cue or via show control), it runs as Background.

### CHANGING A MACRO MODE

      Recall Snapshot 1                                                             for larger viewing screen
                                                                                    gets an error message – the macro is
      [1] [Thru] [10] [Macro] [11] [Enter],          [Shift]&[Clear]                interacting with the command line
      [Macro] [Macro]
      [11] [Enter]
                                                                                    each press of Macro Mode toggles the
      {Macro Mode} {Macro Mode} [Enter]                                             mode; change to background mode
      [Live] Move several faders away from their current position
                                                                                    macro runs behind the command line,
      [1] [Thru] [10]     [Macro] [11] [Enter]                                      not affecting the command line

### ADDITIONAL MACRO EDITOR FUNCTIONS

      [Macro] [Macro]
      [3] [Enter]
      {Macro Mode} [Enter]                                                          makes it foreground mode
      {Edit} or [Learn]
      Arrow over to “Next”, {Delete}
      {Wait for Input}, [Label]                                                     onscreen keyboard pops up
        [Escape] to go back to the macro editor
      [Enter] {Delete} to remove 
      [Learn] or {Done}                                                             Macro should look like the below

      Eos Family Console Programming Level 4

            [Live]     Recall Snapshot 4
            «OS Movers-Wash» (G7) [Full] [Full], «X Stage Look» (FP12)
            Tilt fixtures halfway up the Proscenium arch
            «Rec Next FP»                                                               watch red text above the command line
                                                                                        Wait for Input requires pushing Macro
            [21], then push [Macro] High Cross [Enter]                                  hardkey to continue the macro

### MACRO PROPERTIES

            [Macro] [Macro]
            [Next] (RFR Enable) {Color} {Green} [Enter]                                 color options are on softkeys only
                                                                                        these colors appear in direct selects and
            [Next] (RFR Disable){Color} {Red} [Enter]                                   on dedicated macro buttons if present
                                                                                        on hardware with built-in touchscreens
            [4] [+] [5] [Copy To] [Copy To] [819] [Enter]                               lines up with colors
            [11] [Label] Reset Faders [Enter]

### OTHER MACRO COMMANDS

        - {Loop Begin} – inserts a loop start command
        - {Loop End} – inserts an end command for a loop with a limited
              number of iterations. An infinite loop is assigned when you use “0”
              for the iterations.
        - {Wait} – inserts a pause for a period of time. This needs to be
              followed with a whole number of seconds.
        - {Wait for Enter} – inserts a pause in the macro that waits for the
              [Enter] key. Pressing [Enter] will resume the macro.
        - {Target Device} – A macro can have a Target Device assigned to it.
              This allows a cue to execute a macro only on a certain console. The
              Target Device can be a device name or User ID. These are assigned to
              a macro in the Macro Display by using the {Target} softkey and either
              selecting {Device} and {User}.
        - {SC Learn} – enables or disables excluding specific macros from being
              learned as show control events. (SC = Show Control)

### START UP SHUT DOWN MACROS

     [Displays] {Setup} {System} {System}

        - {System Startup Macro} – allows you to set up a startup macro that
              will trigger after the console initialization has completed.
        - {System Shutdown Macro} – allows you to set up a disconnect
              macro that will trigger at power off, not when exiting the application.
        - {Disconnect Macro} – allows you to set up a disconnect macro that
              will trigger when the primary disconnects from its backup, or when a
              backup disconnects from the primary.

     Go back to [Live]

## Multiple Cue Lists

Eos allows up to 9,999 cue lists in each show file which can be used for linear
playback, effects cue lists, and multiple programmer environments.
When the same channels are stored in multiple cue lists, the console needs to
know which cue list owns a channel at any given time. By default, cue lists are
LTP (Latest takes Precedence). That means, that whichever cue list has given a
channel its most recent move instruction owns that channel. That cue list will
remain the owner of that channel, until another cue list acts upon it with a
move instruction or until the current owner releases it.

### RECORD A NEW CUE LIST

  [Live]     Recall Snapshot 4       [Go To Cue] [102] [Enter]

  «FOH Movers» (G5) [Home] [Enter], {Make Abs} [Enter] «Guitar» (FP1)                                  removes references
                                                                                                       creates list 2 and records the data to cue
```text
  [Select Last] [Record] [2] [/] [1] [Enter]                                                           1 in that cue list
Note:      New cue lists will automatically load to the first empty fader. A list has to have a
```
           fader to run. Motorized fader moves to Full. Non-Motorized faders need to be
           moved to the full postion. The PSD is also looking at cue list 2.

  [Select Last] (G5) «Singer» (FP2)
                                                                                                       just manual values are recorded into cue
```text
  [Record Only] [2] [Enter]                                                                            2/2
Note:      Look at the command line – it is still pointed to Cue List 2, so simply recording Cue 2
```
           will add it to List 2. If you want it to appear in another list, you need to add the list
           to the command.

  [Select Last] (G5)             «Drums» (FP3)

  [Record Only] [Next] [Enter]                                                                         records cue 2/3

  [Cue] [1] [Thru] [3] [Time] [1] [Enter]                                                              changes timing on cues 2/1 thru 2/3

### CUE LIST PLAYBACK

Note:      Non-motorized faders need to be placed at Full position to run the cues.
                                                                                                       loads cue 2/1 on stage (additive to other
  On the fader with cue list 2:                                                                        cue list’s contributions)

  [] (Stop/Back)          [] (Stop/Back)                                                             top button below fader

  [] (Go)]       [] (Go)]                                                                            bottom button below fader plays cue 2/2

  [Go To Cue] [2] [/] [1] [Enter]                                                                      plays cue 2/1

  [Go To Cue] [2] [/] [0] [Enter]                                                                      sends cue list 2 to Cue 0, intensity only
                                                                                                       reloads cue 1/102, which retakes
  [Go To Cue] [1] [/] [102] [Enter]                                                                    ownership of the FOH moving lights
    [Go To Cue] [0] and [Go To Cue] [Out] are on a list-by-list basis. To reset all cue lists
    back to cue 0 and send all fixtures home, use [Go To Cue] [Out] on a clear
    command line. [Go To Cue] follows the command line, so if you are in list 2 and
    want to go to a cue in that list, you don't need to specify 2/. If you [Go To Cue] [1]
    [/] [Enter], then future [Go To Cue] commands will be in list 1.

      Eos Family Console Programming Level 4

### MANAGING CUE LISTS ON FADERS

        Note:    On non-motorized hardware, the [Load] function is achieved by pressing both
                 top and bottom bump buttons together. [[Load]]

### UNLOAD A CUE LIST

                                                                                                unloads cue list from the fader, but does
          Hold [Shift] & press [[Load]] on the fader with cue list 2                            not delete contents of the list

### LOAD A CUE LIST

          [Cue] [2] [/] [[Load]] on fourth fader                                                puts list 2 back on the selected fader
                                                                                                puts 1/13 as the pending cue on the main
          [Cue] [1] [/] [13] [Master/Load] above the main fader pair                            fader pair

### OFF AND RELEASE

        [Off] &[Load] - returns channels in cue list to previous owner, either a cue or a
        submaster. If there is no previous owner, the intensities will just fade out and non-
        intensity parameters go to home positions.

          [Off]&[Master/Load] on Master Fader pair                                              lights all fade out and return home
                                                                                                fades from a blackout back into the
          [] (Go)                                                                              pending cue 13

        [Release]&[Load] - behaves like [Off] except that it sets the pending cue to the
        first cue in the list and removes the active cue. (Cue 0 on stage and cue 1 pending)

          [Release]&[Master/Load] on Master Fader pair                                          intensities fade out

          [] (Go)                                                                              fades back to the top of the cue list

        In Setup, you can set different times for Off and Release and those times can be
        recorded into a macro to be changed quickly.

### VIEWING MULTIPLE CUE LISTS

      Recall Snapshot 1
      [Cue] [1] [/] [Label] Main List [Enter]                                                   labels cue list 1

      [Cue] [2] [/] [Label] Band Chase [Enter]                                                  labels cue list 2

      [Cue] [2] [/] [Enter]     [Cue] [1] [/] [Enter]                                           PSD follow the command line

      With the PSD in focus, hit [Format]                                                       shows two cue lists in the PSD window

      Right click or tap on the PSD tab or select the Gear                                      to see configuration settings

      Click or tap on Target Grid pull down menu, select Top                                    to first select top or bottom of the display

      Click or tap on Lock Status pull down menu, select List 1 Main List                       locks the top cue list on list 1

      Click or tap on Target Grid pull down menu, select Bottom
      Click or tap on Lock Status pull down menu, select List 2 Band Chase                      locks the bottom cue list on list 2

      Tap outside the Configuration Tools to view the PSD again                                 notice the padlocks on each cue list

        It is possible to view more than 2 cue lists – simply open another PSD. It would be
        Tab 2.2.

## Multiple Cue List Playback

### LINEAR LIST PLAYBACK

Lists can be played back linearly, like a single list. They don’t have to be played
in order. Perfect for out-of-order or multiple designer events.

  [Cue] [117] {Link/Loop} [2] [/] [1] [Enter]                                              links cue 2/1 to cue 1/117

  [Cue] [1] [/] [116] [Master] (Load)                                                      cue 117 is pending

  [] (Go)    [] (Go)     [] (Go)     [] (Go)                                           cue 2/1 is pending, then current

    Since PSD is locked, if we want to view a third cue list, you may want to leave your
    primary PSD unlocked.

  [Cue] [1] [/] [1] [Load] and then [] (Go)                                               back to the top of cue list 1

  [Cue] [117] {Link/Loop} [Enter]                                                          to remove the link

### USING A CUE LIST AS AN EFFECT

Lists can be triggered in the middle of a main cue list to run an effect.

  [Cue] [2] [/] [1] [Thru] [3] {Fw/Hg} {Fw/Hg} [1] [Enter]                                 places hang autofollows on cues in list 2

  [Cue] [3] {Link/Loop} [1] [Enter]                                                        links back to cue 2/1 creating a loop
                                                                                           when cue 1/102 is played, cue 2/1 plays
  [Cue] [1] [/] [102] {Execute} [2] [/] [1] [Enter]                                        also, then follows into 2/2, 2/3, and loops
                                                                                           indefinitely
                                                                                           when cue 1/104 is played, it plays cue
  [Cue] [1] [/] [104] {Execute} [2] [/] [0] [Enter]                                        2/0, stopping the loop

  [Cue] [1] [/] [101] [Master] (Load)

  [] (Go) on Cue 101

  [] (Go) on Cue 102                                                                      notice the effect is also running

  [] (Go) on Cue 102.5
    To check on the ownership or source of a channel, [About]&[Cue] can see which
    cue list or which cue is the source of the level.

  [] (Go) on Cue 103

  [] (Go) on Cue 104                                                                      also runs cue 2/0 as well

      Eos Family Console Programming Level 4

         [Assert] allows tracked or blocked data from a cue to be replayed, even when
         another cue list has taken control of that channel/ parameter. Asserted channels
         play back tracked and blocked values, regardless of cue list ownership, when the
         associated cue is replayed.

       [Group] [5] [Assert] [Enter]                                                              notice the red A’s

       [Update] [Enter]

       [Go To Cue] [101] [Enter]
                                                                                                 channels go back to values in first cue list
       Run the cues again                                                                        cue 104 retake ownership of chans
         Notice the small ‘a’ in the PSD Flags column indicating channels are asserted in this
         cue.

### CHANNEL LEVEL RELEASE

     Channel Level Release is an ownership tool that allows channels and individual
     parameters to be released back to their previous owner without having to
     release the entire target.

       [Blind]   [Cue] [2] [/] [3] [Enter]

       [Cue] [4] [Enter] [Enter]      [101] [Thru] [105] [Enter]                                 in cue list 2
                                                                                                 assigns a channel level release flag –
       [Group] [5] {Release} [Enter]                                                             notice the gray ‘R’s

       [Live]

       [Go To Cue] [35] [Enter]
                                                                                                 when cue 36 is played, cue 2/1 plays
       [Cue] [36] {Execute} [2] [/] [1] [Enter]                                                  concurrently, which then follows into
                                                                                                 2/2, 2/3, and loops indefinitely
```text
                                                                                                 when cue 37 is played,              cue
       [Cue] [37] {Execute} [2] [/] [4] [Enter]                                                  2/4 plays concurrently
       [Live]                                                                                    to reset the PSD

       [] (Go) in to cue 36                                                                     cue list 2 takes ownership of Group 5
```
                                                                                                 cue 2/4 release channels to values in cue
       [] (Go) in to cue 37                                                                     1/37
         To clear a Release flag, simply select the target and hit {Release} [Enter].

## Cue List Index

The Cue List Index allows you to view and manage all of the Cue Lists in a show
file, and change their behaviors.
  [Cue] [Cue] or Add-a-Tab (the ‘+’ tab)                                                      opens the Cue List Index

    Top section is the currently selected cue list; the bottom section is the list of all
    cue lists. Cue properties are also displayed in the CIA.

### MASTER

### INTENSITY MASTER (INT)

    Like a Submaster, Cue lists set to Intensity Master will master just the intensities of
    the channels on stage.
      Still in the Cue List Index
      With Cue List 1 on the command line, just tap {Int}
      [Live],   [Go To Cue] [9] [Time] [0] [Enter]
                                                                                              only intensities are changed, non-
      Move the Master Fader pair up and down, watch the levels.                               intensity parameters stay as they are

### MANUAL MASTER (MAN)

    Cue lists set to Manual Master will execute a new cue just by moving the faders in
    either direction.
      [Cue] [Cue]                                                                             opens the Cue List Index

      Click/tap {Man} under the Master column
```text
      [Live]    [Go To Cue] [1] [Time] [0] [Enter]
      Move the Master Fader pair down to run cue 2 and then up to run cue 3,                  cues run at the top and bottom of the
      watch the cues play back.                                                               fader pair
```
       Every time that you go down or up, you advance a cue.
       Timing is controlled based on how fast you move the faders

### PROPORTIONAL

    Proportional is the default fader type. With the faders at the top, pressing Go runs
    the next cue. If the faders are at 0% (bottom), and a Go is hit, then the faders need
    to be moved manually.
      [Cue] [Cue] to go back into the Cue List Index
      Click/tap {Prop} under the Master column
      [Live]    [Go To Cue] [11.5] [Time] [1] [Enter]
                                                                                              see ‘man’ in the fader preview, nothing
      Bring faders all the way to bottom and then hit [] (Go)                                runs till push faders to the top
        Allows you to control one cue at a time manually. Timing is controlled based
        on how fast you move the faders
      Run the faders up
      [] (Go) in to cue 13 using the cue timing
                                                                                              nothing happens till manually takes
      Move the Master Fader pair back down to 0% and hit [] (Go)                             control of another cue
      Run the faders up

      Eos Family Console Programming Level 4

### GO FROM LAST AND BACK FROM FIRST

### BACK FROM FIRST

        ‘Back From First’ controls the behavior that happens when you press the [Back]
        button while in the first cue. It has the following options:
        - Do Nothing – keeps the first cue active
        - Cue Out (Default Setting) – only fades out channels in that cue list.
             Other channels remain. Intensity and non-intensity parameters are
             homed. This setting uses the Back time for fading.
        - Wrap – puts the last cue in the list in pending, and fires said cue.
        - Restore Background – any background cue, submaster, and effect
             levels are restored following background priority. Manual levels are
             not restored. This setting uses the Release time set in Setup.

            [Go To Cue] [1] [Time] [0] [Enter]
                                                                                         going backwards from first cue in a list
            Press [] (Stop/Back)                                                        defaults to going to cue out
            [Cue] [Cue]
            Under the Back From 1st column, select {Wrap}
            [Live]   Press [] (Go) into cue 1
                                                                                         now the first cue wraps back to the last
            Press [] (Stop/Back)                                                        cue in the list (117)

### GO FROM LAST

                                                                                         pressing Go from the last cue in a list
```text
            Press [] (Go) from Cue 117                                                  defaults to doing nothing
            [Cue] [Cue]                                                                  back to Cue List Index
```

            Under the Go From Last column, select {Wrap}
                                                                                         now the last cue wraps around to the
            [Live]   Press [] (Go) into cue 1                                           first cue in the list
             The behavior is displayed on the PSD in the Label Column.

### OTHER CUE LIST SETTINGS

 [Cue] [Cue]          with Cue List 1 selected                                                opens the Cue List Index

### HTP/LTP

  Intensity playback behavior can be set to HTP (highest takes precedence) or LTP
  (latest takes precedence) on a cue list by cue list basis.

### ASSERT

  Just like an individual cue, a full cue list can be asserted. It will assert all channels
  owned by the cue list.

### PHANTOM MODE

  When a cue list is set to Phantom, pressing [] (Go) will not change the selected
  cue on the command line, or an unlocked playback status display.

### EXCLUDE

  - Exclude From Record – prevents content in cue list from being
         recorded into any other record target.
  - Exclude From Solo – prevents content from being affected by any
         solo commands
  - Exclude From Inhib – prevents an inhibitive submaster from
         removing any content from the cue list
  - Exclude From GM - prevents a Grandmaster from removing any
         content from the cue list

### EXECUTE SOFTKEY

  {Execute} can also trigger actions such as macros, show control, or snapshots to
  cue playback. {Execute} will open a trigger display in the CIA.

  Cue lists can trigger like-numbered cues in other cue lists.

      [Cue] [1] [/] {Execute} [2] [/] [Enter]                                                 links list 2 to follow list 1’s playback

  When cue 1/1 is played, cue 2/1 will also be played, and so on. Only identical
  numbered cues will trigger on a cue list execute command.

      [Cue] [1] [/] {Execute} [Enter] or use the delete icon on the table in the CIA          removes the external link

### AUTOBLOCK CLEANUP ON A CUE LIST

  {Autoblock Clean} is used to remove all auto-blocks from a single cue, cue range or
  entire cue list

      [Cue] [1] [/] {Autoblk Clean} [Enter] [Enter]                                           removes all the autoblocks from list 1

      Eos Family Console Programming Level 4

## Priority

     Priority is another way of managing ownership of channels. There are ten levels
     of Priority that submasters and playback faders can have. 1 is the lowest level
     and 10 is the highest. Default priority level is 4.

### CUE LIST OWNERSHIP

          [Live] [Go To Cue] [28] [Enter]
                                                                                           removes Hang flags from cues 1 thru 3 in
```text
          [Cue] [2] [/] [1] [Thru] [3] [Shift]&[Delay] [Delay] [Enter]                     cue list 2
          [101] [Thru] [105] [Enter]                                                       to look at channels 101 - 105

          Hold [Release] and press [Load] on the fader with cue list 2                     Releases channels to cue 29

          [] (Go) on Master Fader pair into cue 29                                        into cue 29
```
                                                                                           latest target to give those channels move
          [] (Go) on Cue list 2 fader                                                     instructions
                                                                                           see those channels are owned by cue list
          [About]&[Cue], look at channels 101 - 105                                        2 and all others by cue list 1
                                                                                           cue list 1 provides new move instructions
          [] (Go) on Master Fader into cue 30                                             for those channels
          [About]&[Cue] again
                                                                                           notice only focus is owned by cue list 2
          [] (Go) on Cue list 2 fader                                                     (recorded with Record Only)
          [About]&[Cue] again
             Ownership works on a parameter-by-parameter basis, not just channel
             by channel.

### SETTING A PRIORITY

        To ensure that cue list 2 is always going to take ownership of these parameters,
        change its priority.
          [Cue] [Cue]        [Cue] [2] [/] [Enter] if not selected already                 to go back into the Cue List Index

          In the Properties, select {Priority}, then {P5}                                  higher than default P4

        Any target with a higher priority always gains control of the channels it owns.
          [Live]   [Cue] [1] [/] [28] [Master] (Load)                                      load cue 1/28 on the master

          [Off]&[Load] on fader with cue list 2/ loaded                                    turns list 2/1 off

          [] (Go) on Master Fader into cue 28
          [About]&[Cue]                                                                    see channels are owned by cue list 1

          [] (Go) on Cue list 2 fader                                                     asserts ownership on the channels
                                                                                           Cue list 2 with the higher priority
          [] (Go) on Master Fader into cue 29                                             maintains ownership of the channels

### PRIORITY WITH OTHER TARGETS

 [] (Go) on Master Fader until you are in cue 32
                                                                              Sub is set for HTP, gains ownership of
```text
 Push up the fader containing Submaster 2                                     channels
 [Sub] [Sub]   [Sub] [2]      select {Priority}, then {P3}                    lower than default P4
```
                                                                              Sub can’t control channels because
```text
 [Live]    Push Submaster 2 up and down                                       priority is lower than cue list
 [Go To Cue] [Out] [Enter]        Push Submaster 2 up and down                nothing is active, sub works normally
```
    When using cue lists, it is important to know that the cue doesn’t take
    ownership of the channels until the first move instruction of the list.
 [] (Go) on Master Fader into cue 1                                          can still use Sub
                                                                              move instruction on 51 in cue, sub can’t
```text
 [] (Go) on Master Fader into cue 2                                          take control of that channel
 [Sub] [Sub]   [Sub] [2]      select {Priority}, then {P4}                    set back to default, HTP has ownership
```

      Eos Family Console Programming Level 4

## Capture

     Normally, manual channel values will be overcome by incoming move
     instructions from cues. Capture allows several ways to preserve the manual
     state of channels and parameters through playback.

### TEMPORARY (SELECTION) CAPTURE

        Anytime a channel is held on the command line as a selection, its manual values
        will be preserved in a temporary Capture.

           [Live]    Recall Snapshot 1
                                                                                              be in Summary, Flexi-Patched to see the
           [Go To Cue] [1] [Enter] [Format]                                                   following channels

           [1] [Thru] [10] [At] [30] [Enter]                                                  places manual changes on several fixtures.

           [Clear]                                                                            to clear the command line
                                                                                              incoming move instructions override
           [] (Go) on Cue 2                                                                  manual values but 1, 2 + 7 - 9 retain manual
                                                                                              values as there are no new instructions

           [Go To Cue] [1] [Enter]

           [1] [Thru] [10] [At] [30] [Enter]                                                  places manual changes on several fixtures
                                                                                              manual values of selection remain as
           Don’t clear the channel selection!!    [] (Go) on Cue 2                           channels are temporarily captured by the
                                                                                              command line

### COMMAND LINE CAPTURE

        You can select specific channels or parameters to stay Captured. These devices will
        remain captured until you release them, allowing you to do other tasks that a
        temporary capture will not allow.
           [Go To Cue] [1] [Enter]
                                                                                              places manual changes on channels and
           [1] [Thru] [10] [At] [3] [Capture] [Enter]                                         captures them. notice the yellow “C”
           [Clear] to clear the command line
                                                                                              channels’ manual values stay, even when
```text
           [] (Go) on Cue 2     [] (Go) on Cue 3                                            there is an incoming move instruction
           [Go To Cue] [Enter]                                                                the captured values remain
```
                                                                                              values are updated in Cue 3 (following
           [Update] [Enter]                                                                   standard update rules), but remain manual
                                                                                              captured channels can still have values
           [1] [Thru] [10] [At] [75] [Sneak] [Enter]                                          manually changed, and with Sneak, it can be
                                                                                              over time
           [1] [Thru] [10] [Capture] [Enter]                                                  removes the capture
                                                                                              incoming levels will now override the
           [Clear]    [] (Go) on Cue 4                                                       manual data
                                                                                              to remove manual data on channel 10, no
           [Sneak] [Enter]                                                                    incoming move instruction

### LATCH CAPTURE

   By latching Capture on, any manual values that are up, as well as changes that you
   make after will automatically be captured. Turning off Latch Capture will release all
   captured values but will leave them manual.

       [6] [+] [7] [Full] [Enter]                                                          bring up some manual values.

       [151] [Thru] [154] {Make Man} [Enter]
                                                                                           Capture Enabled on command line. LED
       [Capture] [Capture] [Enter]                                                         on Capture key lit. All manual values
                                                                                           become captured.

       Recall Snapshot 4
                                                                                           channels become captured. Capture rules
       «High Sides - Left» (G3) [Full] [Full],   touch «Lt Blue» (CP5)                     apply to non-intensity parameters as well

       [] (Go)                                                                            none of captured channels are affected
                                                                                           disables Latch Capture. All manual values
       [Capture] [Capture] [Enter]                                                         get uncaptured.

       [Sneak] [Enter]                                                                     clears all the manual data

        Or [Update] to add the data to the cue

### CAPTURE BEST PRACTICES

   - Capture is great for locking in temporary manual overrides. For
        example, adding area light for a full scene with internal cueing, or
        putting in key and fill lights over a base look. Once uncaptured, levels
        will smoothly transition back into the cue list on the next move
        instruction.

      Eos Family Console Programming Level 4

## Custom Encoder Mapping

     Custom Encoder Mapping allows you to define the placement of specific
     parameters onto specific encoders based on user, fixture type, or both.

### CREATE AN ENCODER MAP

                                                                                            Notice the List of maps at the bottom,
       Add a tab, open Encoder Maps – Tab 40                                                which can be labeled like all targets

       Type [1] [Enter]                                                                     To create the first Encoder map

         The 6 categories down the left side correspond with the 6 parameter categories
         and subcategories, which match the encoder selection buttons on the console
         keypad. Up to 25 pages of encoders per category.
         Let’s say you want access to Pan, Tilt, Zoom, and Edge on a single page, and you
         want the page to be in the focus category.
                                                                                            The box with (1) simply indicates row
       Select {Focus} on the left                                                           number or first page of parameters

       Click on the first box with a + sign in it
         A pop-up appears that lets you choose what parameter to assign to the encoder.
         Parameters can be selected from a fixture profile, from a category, from the
         Common category, or found using the search box.

       In Search, type in Pan, then double click {Pan} from the search results              Pan from Common category

         Note a second page of tiles is added below automatically.

       Make the 2nd encoder {Tilt}, the 3rd {Zoom}, and the 4th {Edge} on page 1            Notice parenthesis go away on (1)

       Click on None under Widget and choose CIE xy under Color Picker

       Click {Color} on the left side                                                       To switch to Color category

         Notice the widget in the color category defaults to the CIE XY color picker
                                                                                            Shortcut to assign multiple parameters
       Click on the first blank tile, open {Parameter Sets}. Select {RGB Group}             that go together to one page

       On the page 2, click on the first box with a + sign in it

       Open {Parameter Sets}. Select {CMY Group}

       On both page 1 and page 2, make the 4th encoder {CTO}

       [Label] Default [Enter]

### ASSIGN AS DEFAULT MAP

   A custom encoder map can be assigned as the default encoder map for all devices
   in the show file, either on the current display or in Setup. When custom mode is
   enabled, this map will be used for all patched devices.
    Click the box under Default Encoder Map at the top of the screen                  Default Encoder Map on command lin

    [1] [Enter]                                                                       Sets the Default to Amp 1

    [Displays], {Setup}, {User}, {Manual Control}
    On the right side, below Default Times, click on {Default Encoder Map}            A list of available maps appears

    Select the desired map, {1: Default}

### HOW TO APPLY CUSTOM ENCODER MAPS

[Live] [101] [Enter]
[Encoder Display] and select {Focus}                                                  Default mapping - only Pan and Tilt
                                                                                      Applies custom encoder map – with
[{Custom}]                                                                            Pan/Tilt/Zoom/Edge and CIE xy color
   Custom Map Default is displayed on the screen. This is a hard button on Apex.
{Color}                                                                               Only have CTO on the 4th encoder.

   In the map, page 1 was RGB, and this fixture doesn’t have RGB parameters.
{Color} to go to page 2 of Color                                                      Now see CMY and CTO

{Color} to go to page 3
   These parameters were not assigned to the default map, so Eos puts them at the
   end of the category. This is only true on the default map.
[51] [Enter], switch to first page of color encoders
   As this fixture doesn’t have CMY or CTO, the encoder page is blank
                                                                                      Removes custom map – back to standard
```text
[{Custom}]                                                                            maping – RBG and Lime
{Color} to go back to page 2                                                          It’s blank!

{Color} to page 3                                                                     Shows rest of parameters: lime, hue, sat
```

      Eos Family Console Programming Level 4

### USE OF DEFAULTS IN CUSTOM MAPPING

     If you are planning on having the same parameter on an encoder throughout
     the category, like we are doing with CTO, you can use the defaults on the
     Encoder Maps tab.
      Back in the Encoder Maps – Tab 40
      On Map 1, page 2, in Color, click encoder 4 {CTO} and then {Clear}                       To unmap the encoder

      Select the 4th tile in the Defaults section at the top of the screen
      Search and select {CTO}
         Defaults follow the By-Type logic and color scheme. Default at top is equivalent of
         a default (blue). If you add another page in the map, CTO will automatically be
         populated on the 4th encoder (magenta).
                                                                                               CTO is mapped to encoder 4 on the new
       On page 3, click the first tile and select {Blue}                                       page
         CTO on page 1 is white because it is a discrete value. It was there before we
         assigned it to the default.
       On page 1, click {CTO} and then {Clear} – remains CTO but changes color                 Turns magenta to match the default

       On page 3, click {CTO} and select {Shutter Strobe}                                      Can change parameter at any time

       Click on the Page 3 tile and select {Delete}                                            To delete the 3rd page
                                                                                               Toggles the 2 dedicated encoders on
       Click the {Show/Hide Dedicated Encoders}                                                consoles with 6 encoders (Ti)
         The 2 dedicated encoders default to Pan/Tilt but may be edited the same way as
         the other 4 parameter encoders.

### CREATE A MAP FOR A FIXTURE TYPE

[2] [Enter]

[Label] SolaFrame Theatre [Enter]

Use the softkey {Create from Fixture} and choose {SolaFrame Theatre}
   This pre-maps all parameters of this fixture to the standard categories that they
   would be in with the standard Eos mapping, based on the profile from Patch.
   Note that this works just like adding a new fixture in Patch. It defaults to the Show
   menu, but any fixtures from the library can be added if needed.

### MAP TO FIXTURE

   The console auto maps to the fixture type from which it was created. Fixture-
   specific maps can be added using the {Map to Fixture} softkey or deleted using the
   red trash can.

### EDIT A MAP

    Select {Intensity} on the left                                                         Only want the first intensity parameter

    Click on each of the last 3 tiles and select {Clear}
       While programming, if those parameters are needed, can easily disable the
       Custom Map and use the standard Eos map.
    Select {Form} on the left                                                              Only want the first intensity parameter

    Click on the Page 2 tile and select {Delete}                                           To delete the 2nd page

    On page 1, click {Shutter Strobe}, {Change Parameter}, select {Diffusion}

    On page 2, add {Shutter Strobe} on the first tile

      Eos Family Console Programming Level 4

### COPY/PASTE PAGES OF PARAMETERS

     [3] [Enter] [Label] ColorSource Spot [Enter]

     Use the softkey {Create from Fixture} and choose {ColorSource Spot Direct}

     Select {Color}                                                                           Only want the first intensity parameter
                                                                                              Clears the parameters but does not
     Click on the Page 1 tile and select {Clear}                                              delete the page.
                                                                                              Shortcut to assign multiple parameters
     Click on the first box, then open {Parameter Sets}. Select {RGB Group}                   that go together to one page

     Select the 4th tile on page one and make it {Lime}

     Click on the Page 2 tile and select {Delete}                                             To delete the 2nd page

### ASSIGN THE PAGE TO EVERY CATEGORY

        Since the ColorSource Spot doesn’t have any Focus, Shutter, or Image parameters
        those encoder pages would be blank. By assigning the color page to each category,
        any time the fixtures are selected, no matter what category page is selected, color
        control is at your fingertips.

          In {Color}, select the Page 1 tile and select {Copy}

          Select {Focus}, select the page number and {Paste}

          Select {Shutter}, select the page number and {Paste}

          Select {Image}, select the page number and {Paste}
        {Form} has the Shutter Strobe parameter on it, so let’s not paste there.

### CREATE A MAP FOR MULTIPLE FIXTURES

     [2] [Copy To] [4] [Enter] [Label] SF Theatre & CS Spots [Enter]

     Touch the {Map to Fixture} softkey                                                       Notice SF Theatre was carried over

     Select {ColorSource Spot Direct} to add to the Map

        Note: If you add a fixture type that you don’t want, simply click on the red trash
        can to remove the type.

     In {Color}, click the Page 1 tile and select {Insert Before}                             Adds a page at the top

     [Last] to select the ColorSource Spot Map, click Page 1 tile, select {Copy}

     [Next] to SF Theatre & CS Spot Map, click the Page 1 tile and select {Paste}             Can copy/paste between maps

     [Live] [51] [Enter]                                                                      Just ColorSource Spot selected

     [Encoder Display] and select {Color}                                                     Default mapping – 4 colors, Hue/Sat

     [{Custom}] - applies map 3 – ColorSource Spot                                            See RGB Lime on all pages

[51] [+] [101] [Enter]                                                                   Both Fixture types selected

   With Custom maps still enabled, the console will use Custom Map 4 because both
   fixture types are in the selection. RGBL is on the first page.
                                                                                         SF Theatre parameters are on the
{Color}, {Color}                                                                         subsequent pages

[101] [+] [121] [Enter]
   Selecting a fixture with a custom map and selecting a fixture without a custom
   map, Eos will stack the maps. In this case, it is stacking Map 1 and Map 2. You can
   select (or deselect) which map to use in the encoder display.

[121] [Enter] – a SolaWash 2000
   With Custom maps still enabled, the console will use the Default Encoder Map.
   Page 1 of Color, which is just CTO, because the map’s first page is setup with RGB.
   If multiple maps meet the same criteria, then the lower map number will be used.
                                                                                         To disable the custom maps and return to
[{Custom}]                                                                               standard mapping

### FILTER TO USERS

Back in the Encoder Maps – Tab 40

[2] [Copy To] [2.1] [Enter]

[2] [Enter] and touch the {Filter to Users} softkey, [1] [Enter]                         Assigns the map to user 1

[Next], {Filter to Users} [2] [Thru] [3] [Enter]                                         Assigns the map to users 2 and 3

   This allows each user to layout the encoders the way that they would like to see
   the parameters. In Custom mode, if user 1 selects SolaFrame Theatre fixtures, the
   console will use map 2. If user 2 or 3 selects SolaFrame Theatres, the console will
   use map 2.1. If another user, user 4, selects SolaFrame Theatres, the console will
   default back to map 1 as there is not a map currently mapped to user 4 for that
   fixture type.

{Filter to Users} [Enter]                                                                Restores a map’s User Filter to “All”

      Eos Family Console Programming Level 4

## Fader Configuration

     The Eos Fader Configuration display is where one can set up the mapping and
     configuration of the faders. Various targets, including cue lists, submasters, and
     palettes can be assigned to faders.

### COLOR PALETTE ON FADER

         Recall Snapshot 4

         [Live]   [Go To Cue] [104] [Enter]       [Clear]

         Hold [Fader Page], type [3], let go of Fader Page                                       takes you to page 3 which is open
             Fader Page button only advanced to pages with content.
         [Load] button of first fader on page 3
                                                                                                 posts Fader 3 / 1 to the command line
            On Ion Xe, press both buttons ( & ) for the fader to load
                                                                                                 command line reads “Mapped to Color
         «Red» (CP1) [Enter]                                                                     Palette 1”
             Playback data is shown on the screen in an orange color.
                                                                                                 every channel in that palette is faded to
         Run the fader up                                                                        that palette color
         Even though 51 through 85 are not on, the fader still controls their non-intensity
         parameters because they are stored in that palette.
                                                                                                 adds channels – notice already in the
```text
         [Group] [3] [Thru] [4] [Full] [Full]                                                    color on the fader
         [Clear] [Sneak] [Enter] and run the fader down                                          to clear both intensity and playback data
```

### FOCUS PALETTE LIST ON FADER

         Load button of second fader            (Ion Xe) Two ( & ) buttons                     posts Fader 3 / 2 to the command line
                                                                                                 command line reads “Mapped to Focus
```text
         [Focus Palette] [1] [Thru] [5] [Enter]                                                  Palette 1 Thru 5”, moves to Full
         Note:    Non-motorized faders need to be placed at Full position to run the cues.
```
                                                                                                 watch as you step through each Focus
         Hit [] the bump button of the fader, again, again, again, again                        Palette on the selected channels
         Notice that, after the 5th Focus Palette, the fader is released, sending the channels
         to their background state (in this case, it’s Cue 104).
         Pressing the bump button again starts the list again, with Focus Palette 1

### FADER CONFIGURATION DISPLAY

  Recall Snapshot 1

  Click on Add-a-Tab (the {+} sign), then on the Fader Config icon (#36)               opens Fader Config display (Tab 36)

### FADER PROPERTIES

      Scroll down to page 3

            Or use the Page Selection tools to select Fader Page 3;

      Click on the large box of the 2nd fader on that page

      Select Wrap for both Back from 1st and Go from Last

      Change the Dwell time to 1

                                                                                       watch and see the difference from above
      Hit bottom bump button of fader                                                  example, runs indefinitely

### NOW HOW DO I STOP IT?

      Notice in the Fader Config tab, looking at the fader, the buttons are
      defaulted as a Bump Button and a Release Button.
      Hit the top button just once, (Release)                                          stops the cycle

### MANUAL TIME FADER

  Can easily create a fader that makes it possible to change Manual time on the fly.

   On the 5th fader, at the top, click on {Unmapped}

   Under Target, click on {Man Time}, click off the dialogue box                       everything else grayed out

   Click on the fader graphic, box pops up, make sure max is 5, min is 0
      Remember Manual Time is the time a channel goes to full when you type
      1 Full Enter

   [Live]     with Man Time fader at 0      [1] [At] [Full] [Enter]                    goes to full in 0 seconds

   Put Man Time Fader at Full position                                                 remember set as 5 seconds

   [2] [At] [Full] [Enter]                                                             goes to full in 5 seconds

   Recall Snapshot 4
                                                                                       applies manual time to non-intensity
   «All Cycs» (G22), «Red» (CP1)                                                       parameters as well, fades in 5 seconds
   Pull Man Time Fader down to about 2.5 seconds

   «Orange» (CP2)                                                                      fades in 2.5 seconds

   Pull Man Time Fader all the way down

   «Yellow» (CP3)                                                                      fades immediately

  Moving the Man Time fader while channel is fading has no effect.

     Eos Family Console Programming Level 4

### EFFECTS ON FADERS

       Channels running effects can be loaded onto a submaster. By default, pressing the
       bump button of the submaster starts or stops the effect.

       [Clear] [Sneak] [Enter]

       «FOH Movers» (G5), «100%» (IP1), «Singer» (FP2), «Yellow» (CP3), «Circle»
                                                                                           set levels
       (FX901)

       [Select Last] [Record] [Load] on 6th fader, [Enter]
                                                                                           record a sub with an effect
                (Ion Xe) ( & ) [Enter]

       [Clear] [Sneak] [Enter]                                                             remove manual data
                                                                                           fader controls both intensity and size and
       Move fader up to see what it does…                                                  rate of the effect

### FADER LIST DISPLAY

       Recall Snapshot 1

       Click on Add-a-Tab (the {+} sign), in Displays, Fader List Display (#35)            opens Fader List display (Tab 36)
                                                                                           fader page (1 to 100) / fader number on that
```text
       {Fader} [3] [/] [6] [Enter]                                                         page (1 to 10)
       Click on the 1X in upper right of fader icon. Change to 3x                          changes from 1 physical fader to 3 faders
```

       Click on 2nd fader in the group and make Effect Size

       Click on 3rd fader and make Effect Rate
       On manual faders, LEDs blinking, not at correct position. Raise to 50%

       Click on bottom button of 2nd fader and select Freeze

       Click on bottom button of 3rd fader and select Solo

       Click on load button of 3rd fader and select Macro, [11] [Enter]

       [Live]

       Raise first fader to full to start effect, play with size and rate faders

       Use Freeze Button (bottom button of Fader 7)                                        pauses/resumes the effect
                                                                                           forces all other channels to zero while it’s
       Use Solo Button (bottom button of Fader 8)                                          held

       Push load button on 8th fader, Macro 11                                             resets all Faders to home position

       Great macro to have with motorized faders! Still must move the manual faders -
       Inhibitive subs should be at Full, Proportional subs should be at 0, FX Size/Rate
       faders should be at 50%

### GLOBAL EFFECT FADER

    A fader can be mapped as a global effects fader in the Fader Configuration display.
    This fader type is used to master all effects or specific effects based off the current
    filtering applied to the fader. You can use multiple global effects faders.

    In Tab 36, use the Page Selection tools to change to Fader Page 3

    On Fader 10, change the fader target type to Global FX                                        by deafult, that is set as Effect Size
                                                                                                  assumes the same page, unless you specify
```text
    {Fader} [3] [/] [10] [Copy To] [9]                                                            otherwise
    Note:         Can press the Load buttons to put the fader on the command line.
```

    On fader 9, change the fader type to Effect Rate
    Note:         Non-motorized faders need to run faders up to about 50%.

    [Go To Cue] [37.3] [Enter]

    Move Global Effects Size fader up and down                                                    changes size of all running effects

    Move Global Effects Rate fader up and down                                                    changes rate of all running effects

    Note:         These are just temporary overrides. They are not intended to allow content to
                  be changed and stored in a cue.

### TEMPORARY PLAYLIST

    Can mix content types on a fader

        Recall Snapshot 4

        [Go To Cue] [18] [Enter]

        [Macro] [11] [Enter]                                                                      ensure all the playbacks (faders) home

        [Clear]

        Press [Load] on the 3rd fader                                                             puts fader 3/3 on the command line

        «Guitar» (FP1), «Orange» (CP2), «Drums» (FP3), «Lt Blue» (CP5) [Enter]                    loads selected targets in a list

        Press bottom bump button of 3rd fader….again….again…again.                                steps through the targets

    Bump button plays each step of the play list. Without a wrap, a bump at the end of
    the list will release the channels to their background state.
    This will affect all channels that are stored in the targets.

        [Group] [21] [Full] [Full]

        Continue to hit the bump button                                                           Color Palettes affects the cyc channels

    Notice when a Focus Palette is played, cyc goes to background state.
Note:      This is currently only a TEMPORARY fader mapping. While it can be moved and
           copied to different faders, if cleared off the fader, the list is gone.

      Eos Family Console Programming Level 4

## Virtual Faders

     Without physical faders?

      Add-a-Tab (the ‘+’ sign), in the controls area, select Tab 28 – Faders              opens a Fader Module display

     Remember that a single page of faders is a bank of 10. So a single page of
     faders is shown by default. On the right of the display are page buttons to
     navigate to other pages. The faders themselves behave just like physical faders.

### FADER MODULE CONFIGURATION MENU

         The Fader module has a configuration menu, which is accessed by double tapping
         on the tab name or using the gear on the left.
         The following options are available in this configuration menu:
         - Rows - sets the number of rows used for the module. Maximum
             number of rows is six.
         - Columns - sets the number of columns used for the module.
             Maximum number of columns is six.
         - Slider Format - shows buttons only or the entire fader. This is useful
             if you want a module of just the configurable fader buttons.
         - Display Master Fader Pair - toggles the Master Fader Pair on and off
         If more faders are needed, simply open another Fader Module.

## Playback Filters

Playback filters can be applied on a fader by fader basis, which will allow only
specified data to be played back. Data can be filtered by channel, parameter,
effect and target. Playback filters do not impact how data is stored.

### BY CHANNEL FILTER

 Recall Snapshot 1

 In Fader Config Tab, go to the third page of faders

 Click on the blue box under Fader #3                                                 opens Channel/Parameter Filter box

 {Chan Filter}, [Group] [5] [Enter] touch out of the box                              watch command line

                                                                                      the temporary playlist only affects the
 In Live, push bump button of 3rd Fader… Bump… Bump…                                  group 5 channels
 Back in Fader Config Tab, looking at Page 3

 {Fader} [3] [/] [5] [Copy To] [3] [/] [4] [Enter]                                    copies contents of fader

 On Fader 3/4, {Param Filter}, {Intensity} at top and touch out of the box            filters only intensity

 On Fader 3/5, {Param Filter}, {Focus}, {Color}, {Form}, {Image}, {Shutter}           filters everything but intensity

 Recall Snapshot 4

 Put the Manual Time fader filtered to Intensity (fader 3/4) at 0

 Put the Manual Time fader filtered to Non-Intensity parameters (Fader 3/5) at Full
 (5 sec)

 [Group] [3] [Thru] [4] [At] [50] [Enter]     «Yellow» (CP3),                         intensity snaps, color fades in 5 secs.

 Push Fader 4 up to Full, Fader 5 down to 0                                           reverse the faders

 [At] [Full] [Enter]   «Dk Blue» (CP6)                                                intensity fades in 5 secs., color snaps

 Pull both Fader 4 & 5 down to 0
                                                                                      now only changes rate on Effect 3 (Color
```text
 [Go To Cue] [37.3] [Enter]                                                           Chase on cyc)
 Run Fader 9 (Global Effects rate) up and down, leave at 100 (mid-way)                all 3 chases run faster, then slower
```

     Eos Family Console Programming Level 4

### USE FILTER BUTTON

       On Eos Ti, Gio, Gio@5, Ion Xe and Element 2, there is a half-moon [Filter] button
       above the rate wheel that can be used instead of the {Filters} button in the CIA.

          Hold [Filter] above the rate wheel, press [Load] on Fader 10 [Enter]
                                                                                           Command line says “Fader 3/10 Filter
```text
          [Effect] [3] [Enter]                                                             Effect 3”
          Push Fader 10 up                                                                 only the color effect is changed
```

          [Clear] [Sneak] [Enter]

          «Reset Faders» (M11)

          [] (Go) into the blackout      [] (Go) again to Cue 101

### TO REMOVE FILTERS

         Hold [Filter], press [Load] again on Fader 10 [Enter]                             removes any filters on fader 10

         Recall Snapshot 1

         Add-a-Tab (the ‘+’ sign), under Controls, open Fader Config (Tab 36)

         Scroll down to page 3
       Faders that are filtered are indicated by gray boxes on the parameter types.

         Click on the blue box under Fader #3, Temporary Playlist

         Click on the red ‘X’ next to the Chan Filter                                      clears the filters on fader #3

         Click on the blue box under Fader #4, Manual Time -Intensity

         Click on the red ‘X’ next to the Param Filter                                     clears the filters on fader #4

         Click on the blue box under Fader #5, Manual Time -Non-Intensity

         Click on the red ‘X’ next to the Param Filter                                     clears the filters on fader #5

       Playback filters are a quick way to change what the faders are outputting without
       having to change the content.

         [Live]       Recall Snapshot 4       Be in cue 101 if not already there

         Hold [Filter], press [Load] on Fader 1 «All Cyc» (G22) [Enter]                    Fader 1 is CP1, now filtered to cyc only

         Run Fader 1 up and it only changes the color of the cyc

         Hold [Filter], press [Load] on Fader 1 «FOH Movers» (G5) [Enter]                  now filtered to FOH Movers

         Run Fader 1 up again and it only changes the color of those fixtures

## Record Filters

```text
Record Filters                                                                           All consoles: Do not use the [Filter]
Record filters allow only specific parameter data to be stored to targets. When          button located above the Rate
no filters are selected, all parameters can be stored.                                   wheel – center of console. It is for
Filters are most effective to execute repetitive record commands that have               Channel and Parameter Filters on
```
                                                                                         Faders.
similar content requirements, such as Palettes. Filters will affect recording ANY
target including palettes, presets, cues, and submasters. Filters are applied
using the CIA.
On consoles with internal touchscreens, there is a [Filter] button on the angled
touchscreen panel. On consoles without internal touchscreens the {Filters}
button is with the parameter tiles in the CIA.

### APPLYING FILTERS

  Recall Snapshot 1, press [Displays] to open CIA                                      in table view

  [Go To Cue] [28] [Enter]

  [101] [Enter], scroll to see beam parameters
                                                                                       select the categories using parameter
  Hold [Filter] and select {Gobo Select} on the CIA, then release [Filter]             tiles – notice the gray ‘N’s
                                                                                       select the categories using parameter
        OR in the CIA, {Filters}, {Gobo Select}, {Filters}                             tiles – notice the gray ‘N’s

    - Filters will remain active until cleared.
    - FILTER ON will appear below category names where parameters are
           active and being recorded.
    - All parameters and categories that will not be recorded are grayed
           out on the Live display, and the Null “N” will appear. Any item that is
           nulled WILL NOT be recorded.

### RECORDING WITH FILTERS ACTIVE

  [] (Go) into cue 29         [] (Go) into Cue 30.                                    Record Filters have no affect on playback.
                                                                                        records filtered Beam Palette – all
  [Group] [5] [Record] [Beam Palette] [11] [Label] OPEN [Enter]                         channels have null value or ‘n’ except
                                                                                        Gobo Select

  [Select Last], put next gobo into the fixture (Foliage 2)
                                                                                        records filtered Beam Palette with just
  [Select Last] [Record] [Beam Palette] [12] [Label] Foliage [Enter]                    the Foliage Gobo

  [Blind], in table view, flexi active

  [Beam Palette] [11] [Enter]        [Next] to see Beam Palette 12                      view filtered Beam palettes

    Even though palettes were stored using the Record command, which typically
    stores all parameters of a selection, because filters were on, only the filtered
    parameters were stored.

      Eos Family Console Programming Level 4

       [Live] [Go To Cue] [18] [Enter]

       [{Filters}]

       Deselect {Gobo Select}, select {Gobo Ind/Speed} & {Gobo Mode}

       [101] [Enter], scroll to the beam

       [Group] [5] [Record] [Beam Palette] [22] [Label] Slow Rot [Enter]     only stores the rotation mode and speed

       Increase the gobo rotation speed using the encoder

       [Record] [Beam Palette] [23] [Label] Fast Rot [Enter]

       [Select Last] {Gobo Ind/Speed} [0] [Enter]                            stop the rotation

       [Select Last] [Record] [Beam Palette] [21] [Label] Stop Rot [Enter]   store a Beam palette to stop rotation

       [Clear] [Sneak] [Enter]

### STORING FILTER STATES

     Filter states can be stored in Snapshots to be easily recalled later.
                                                                             stores state of the filters (and nothing
```text
       [Record] [Snapshot] [11]        Don’t hit Enter!!                     else) into Snapshot 11
       Uncheck all monitors                                                  don’t want monitor status in snapshot
```

       Select the Filters checkbox,

       Uncheck all other, boxes                                              visible work space will be selected…

       [Label] Gobo Rot [Enter]

       [Clear]

### CLEARING FILTERS

       {Filters}, touch {Clear Filters}                                      removes any filters – no more null values

       [Record] [Snapshot] [10], deselect all the monitors

       Select the Filters checkbox

       Uncheck all other, boxes including the tab boxes                      Visible work space will be selected…

       [Label] Clear Filters [Enter]            [Clear]

       [Snapshot] [2]

       [Snapshot] [11]                                                       applies filters, see all the null ‘N’s
                                                                             filters not affected (were not stored in
```text
       [Snapshot] [1]                                                        this snapshot)
       [Snapshot] [10]                                                       clears the filters
```

## Additional Snapshots Tools

Snapshots store layouts so that you can recall them quickly. They are stored in
the show file, can be recalled on any device on the network.

### SNAPSHOT OPTIONS

  [Go To Cue] [Out] [Enter]
  [{Snapshot}] [3] [Enter]
  Add additional tabs to custom direct selects frame                               adds Patch and a Group List

  [Record] [{Snapshot}] [3]       Don’t hit Enter yet!                             opens snapshot selection window

    You can choose to select/deselect various components, monitors, frames, etc.
    from your snapshot.
    - You can choose to include or exclude Monitors or Frames, by
        selecting/deselecting them in the preview area. Use the {Frames/
        Monitors} button to select whether you will see monitor or frame
        numbers in the preview area.
    - Visible Workspaces – includes only the visible workspaces.
    - All Workspaces – include all workspaces, including those not visible
        at the time of recording.
    - Faders – captures the current state of the faders and master fader
        pair including: content mapping, content state, and fader wing
        groups, based on configuration.
    - Encoders – records the current page of the encoders.
    - Filters – records the current setting of the record filters.
    - Direct Selects – when used without visible workspaces selected,
        recalls all direct select tabs and their settings.
    - Favorite – stores the favorite display () selected for the CIA
    - Color – assign colors ({Red}, {Green}, or {White}) or {Dark} to a
        snapshot. {Dark} assigns no color to the snapshot. The colors display
        beside the snapshots name in a direct select, and/or if that snapshot
        has been assigned to one of the customizable hardkeys on Eos Ti,
        Gio, Gio@5, and RPU.
    - Master Fader Pair and Faders – including mapping and state
    - Top Bar Timecode List – can be stored in a snapshot or ignored
    - Reset – sets the menu back to its defaults.
    - You can also use the list to check/ uncheck monitors, frames, and
        tabs
    -
  Uncheck the tabs you just added, leave your Direct Selects Tab checked
  [Enter] [Enter]
  Recall Snapshot 3                                                                Patch and Group List are not included

      Eos Family Console Programming Level 4

### TO CHANGE A SINGLE TAB

            In Direct Selects, change from Groups to Focus Palettes
            [Record] [{Snapshot}] [6], deselect {All}, then select Tab 4.2 [Enter]
            Recall Snapshot 3 then recall Snapshot 6                                    it just changes the Direct Selects

            Recall Snapshot 4 with same Tab 4.2         then recall Snapshot 6          changes DS 4.2 to Focus Palettes

### RECALLING SNAPSHOTS

     Recalling Snapshots does not post to the command line. You will see the
     command above the command line in red text!
       [{Snapshot}] [1] [Enter]                                                         recalls the content of snapshot 1

       [{Snapshot}] [{Snapshot}] or Add-a-Tab (the ‘+’ sign), (Tab 19)                  opens the Snapshot list

       [6] [Label] DS Change [Enter]                                                    adds a label

### SNAPSHOT POPUP

            Touch Snapshot Pop-up                                                       see all 6 snapshot in the pop up

            [{Snapshot}] [{Snapshot}]
            [2] [Thru] [4] [Enter] {Favorite} [Enter]                                   turn Favorite column off

            Touch Snapshot Popup                                                        displays just Snapshots 1 and 6

### SNAPSHOTS BEST PRACTICES

        - Place your snapshots (like a Direct Select or a Magic Sheet object) in
               the same location on your displays so they are easy to find.
        - Snapshots that include Faders do not store fader attribute states,
               such as Timing Disable, Rate, etc.

## Eos Family Color Tools

### COLOR CONFIGURATION

Color configuration information is stored within the fixture profiles in your
show file.
  [Patch]      [31] [Enter]                                                             In Patch, looking at channel 31

  {Fixtures}                                                                            Opens the Fixture Profile Editor
Fixtures with additive color properties will display a color configuration button
in the Fixture Profile Editor.

This button will open the Color Configuration Editor window.

### EDITING COLOR CONFIGURATION

    For accurate color control, each color parameter in an additive fixture profile
    needs an accurate definition of the correct emitter color, wavelength (in
    nanometers), and relative brightness compared to the brightest emitter in the
    fixture.
    The dropdown menus on the left allow you to choose the correct wavelength for
    each individual color parameter. The color band sliders on the right allow you to
    adjust the relative brightness.

### EXCLUDING PARAMETERS

        The checkbox by each color parameter allows you to exclude specific colors
        from color mixing. You will still be able to control excluded parameters
        directly, and none of their stored data will be cleared. UV parameters are
        excluded (unchecked) automatically.

     Eos Family Console Programming Level 4

### COLOR CONFIGURATION DATA

       The data required for color configuration can originate from a variety of sources.

### CALIBRATED

            Calibrated color configuration data has been gathered using lab-quality
            equipment and measuring techniques. This generally provides higher quality
            color picking and gel matching.
            Fixture profiles with calibrated color configuration are indicated in the
            fixture profile editor with a CIE icon.

### MANUFACTURER

            This type of color configuration data is provided by the fixture's
            manufacturer and can be manually entered into the profile via the Color
            Configuration Editor. The quality of this data, and the subsequent color
            performance of the fixtures that use it, will depend on the quality of the
            manufacturer's initial measurement process.

### FIELD SURVEY

            There are a variety of ways to measure a fixture's color information with
            tools in the field. The fixture profile can then be updated with the gathered
            configuration data.

### DEFAULT

            If a fixture profile has none of the above types of color configuration data,
            Eos will create an auto-generated configuration based on the fixture's color
            parameters.

### LEGACY COLOR CALIBRATION

            If a pre-v3.2.0 show file with additive color RGB and RGBA fixtures is
            opened, Eos will automatically simplify the color calculations being used for
            those fixture profiles. This can greatly improve fixture performance and
            speed for use in pixel maps.

            These fixture profiles can be updated via the color configuration editor to
            get the full set of color configuration tools.

       CAUTION: Updating a fixture profile or library will update all legacy calibration.

### COLOR PICKER

 Add-a-Tab (the {+} sign) and select the Color Picker                                      opens the Color Picker tab

### A LITTLE THEORY

  The default is a color space and the Gel Picker. The cross hairs on the color space
  indicate its chromaticity, or the X-Y coordinates of a color in a two-dimensional
  color space. The default color space is the CIE xy space.
  With an additive color system like RGB - Red, Green, Blue, when plotted on a color
  space, the result is a triangular plane. Imagine that each of the corner points has a
  string attached to the cross hairs. Moving the cross hairs changes the lengths of
  the strings. Every point in the color space where the x and y can hit can only be
  described with unique values of all three of the points. There is no way to describe
  the same point with different values of the three points.
  However as soon as a fourth point is added to the color space, for example, RGBA,
  now there is the potential to describe an XY location with different combinations,
  or recipes, of the four different emitters.
  This is a phenomenon called metamers, two color recipes that are at the same
  chromaticity. Looking at the two recipes on a white wall, the colors would look the
  same. As soon as it is reflected of complex spectral surfaces such as fabric, scenic
  paint or even skin tones, then the differences of the content of that spectrum will
  become apparent. With color systems that have five, six, or even seven emitters,
  the probability of describing the same XY coordinate, the chromaticity, with
  multiple recipes from the emitters becomes much higher.

 [301] [Enter]                                                                             selects a fixture with RGBA

  Easily visible are the three points of the triangle, and, though hard to see, a fourth
  point for the amber emitter is available as well.

 [141] [Enter]                                                                             selects an X7 fixture with 7 colors

  With all seven emitters, all colors within the gamut are available with multiple
  recipes using different combination of emitters. This fixture has a cyan emitter
  that stretches the gamut out beyond the line from blue to green.
  Something to note is that white emitters don’t stretch the gamut; they just
  increase the brightness because they live at the center of the spectrum. Fixtures
  that are three colors plus the white emitter do not have the increased ability to
  have metamers.

     Eos Family Console Programming Level 4

### GEL PICKER

       Chromaticity, gamut and metamers all matter when the gel picker is used. To
       better see this, open the Spectrum tool.

         Select {5 Rosco Roscolux} in the center column of tiles                             opens the swatch library

         Select the gear icon () in the left most tab on the display                        opens Display Configuration Tool

         Select {Spectrum}                                                                   to change the color picker options

       The Spectrum view shows the location of all the emitters in the visible spectrum
       and what their current values are.

         Select {R052}                                                                       to change the color picker options

       The spectrum view displays all the emitter composition that it is using to get as
       close to CC052 as it can.
       The board also displays, in the spectrum display, the information about the
       spectral power distribution of the gel with a dotted line. This is the same
       information that is on the print card behind every gel in a swatch book. This shows
       when light passes through this filter, what spectral content is allowed to pass
       through.

### BRIGHTEST

       Sometimes the gel picker is not quite accurate. That is because the software gives
       you the brightest metamer of all the metamers for a specific chromaticity as the
       default.
       In the Spectrum display for CC052, the Lime emitter is brighter than where the gel
       distribution is. That might shift the color for costumes or scenic paint.

### SPECTRAL

         Click or touch {Brightest} at the top of the center column of tiles                 changes to Spectral

       Software picks a metamer that is most spectrally accurate to what the gel
       distribution passes.

         Select {R052} again                                                                 see how the composition changes

       In the Channel Display, when using the Spectral match, a dot is displayed in front
       of the gel in all the parameters.

### HYBRID

       Often the most spectrally accurate metamer gives up a lot of brightness in an
       additive color system.

         Click or touch {Spectral} at the top of the center column of tiles                  changes to Hybrid

       Software picks a metamer that is halfway between the brightest metamer and the
       most spectrally accurate metamer

         Select {R052} again                                                                 see how the compostion changes again

       In the Channel Display, when using the Hybrid match, two dots are displayed in
       front of the gel.

### TINT TOOL

The color picker is great to quickly get close to the color you want. When more
granular adjustments, open the Tint Tool.

 Select the gear icon () in the left most tab on the display                                 opens Display Configuration Tool

 Deselect {Spectrum}                                                                          closes the Spectrum display

 Select {Tint}                                                                                opens the Tint Tool

Regardless of the parameters of the fixture (RGB, CMY, X7), small adjustments
such as making it a little cooler, adjusting the saturation up or down, or simply
pulling some green out can be made quickly and easily.
The tint tool will translate what that means to shift green out of the fixture
even though there isn’t a green parameter.

 [Go To Cue] [116] [Enter]

 [31] [Thru] [50] [At] [Full] [Enter], using the color picker, make them cyan
    The tinting tool is a tool created for relative adjustments to color, or the tools used
    for “designer speak”.

 Tap {Cooler} several times

 Press and hold {Saturation -}
    Watch the crosshairs as you make adjustments using the Tint tool.

 [101] [At] [Full] [Enter], using the color picker, make them blue
                                                                                              moves the color point away form the
 Even though no green parameter, use {Green +} of {Green -}                                   green part of the spectrum

      Eos Family Console Programming Level 4

### COLOR PATH

     When fading LED fixtures from one color to another, sometimes they will fade
     through undesirable colors or with fade times that are not ideal.Color Path is a
     tool for editing color fades and timing between cues.
     By default, color fades happen in the native space of the fixture. If you want a
     fade that resembles a fade in a different color space, you use color paths.
     There are eight preprogrammed color paths, and you can also record your
     own. Up to 1000 color paths are supported. Channels involved in the fade have
     to be selected before you can choose or modify a color path.

       [Clear] [Sneak] [Enter]

       Select the gear icon () in the left most tab on the display

       Deselect {Tint} and select {Color Path}

       [Group] [22] [Enter], using the color picker, make them amber                        set channels at level and in color

       [Update] [Enter]                                                                     updates the cue

       [] (Stop/Back)           [] (Go) to watch the cyc fade                             fades from saturate blue to amber

       [Group] [22] [Enter]                                                                 shows the fade path on the color picker

         With channels selected, in the color space, the path is displayed that the
         colors are going to take. This is the native color fade – without any
         intervention from the color space.
       [] (Stop/Back)           [] (Go) to watch fade run again along the path

### COLOR PATHS

         The color path display has a drop-down list of the available paths, a color path
         preview bar, and time control buttons.

         Run finger or mouse along Preview Bar                                              to see fade at any point along path

         Timing control buttons are:

### COLOR PATH TYPES

         - Q (#) I – replays the color fade using the cue time.                            1     Native          5    RGB
         - GoToQ (#) I – replays the color fade using the Go to Cue time                   2     Gel             6    CMY
         - 5 I – replays the color fade in five seconds.                                   3     Sat Adjust      7    Hue Sat
         - 10 I – replays the color fade in ten seconds.                                   4     CIE xyY         8    Auto Dim
         - II – pauses the color fade.
         -  – plays / resumes the color fade.
         - I – skips to the end of the color fade.

### COLOR PATH MENU

 On top (No Color Path) far right, select the drop down menu ()                        Opens the Color paths drop-down menu

 Select {2) Gel}                                                                        Gel path similar to native color space

You'll see a representation of those changes in both the color path preview bar
and in the color space.

### TOOLS

    There are also individual control tools to adjust the fade. In Color, Out Color
    and Brightness
     Drag {Delay} along the In Color bar and watch Preview ribbon                       more blue and quicker to amber
    This doesn’t change the path that it takes through the color space, but it
    changes the timing characterization of the fade.
     Reset that {Delay}                                                                 more blue and quicker to amber
    If trying to match two incandescent fixtures with saturate gels fading
    between one another, often times there is a dip in brightness halfway
    through the fade. With LED fixtures, the fade goes closer to white and there
    is a pop in brightness.
     Drag {Brightness} to a lower percentage, watch the Preview                         prevents going though too much white

### SAVE COLOR PATH TO CUE

Color Path information is stored in the destination cue as Absolute data. It is not a
direct path through color space; it is math that determines how to get from the
start color to the end color. This is beneficial if the start color or end color is
changed, the path does not need to be redrawn.
In the Channel display, there is a red ‘C’ next to the channel numbers to indicate a
change or modification to the path.
                                                                                        to see which path each parameter is
```text
  Hold [About] and press [Path]                                                         using, currently using a modified Gel Path
  [Update] <116> [Enter]                                                                updates the destination cue
```

  Open the color picker on the right monitor

  [Group] [22] [Enter]                                                                  to select the channels
                                                                                        fades from saturate blue to amber
  [] (Stop/Back)          [] (Go) to watch the cyc fade                               without white as brightness is less
    This tends to fix most cross fades.
  On top far right, select the drop down menu (), select {6) CMY}                      selects a different color space
    Different tools for this color space: Cyan, Magenta, Yellow
  Change the Gel path to {7) Hue/Sat}                                                   again a different color space
    Adjustments here determine how closely the fade hugs the outside of the
    color space.

     Eos Family Console Programming Level 4

### SAVE A NEW COLOR PATH

          [Change the Gel path to {5) RGB}                                                     another color space

          On the color picker, make the end result more yellow, closer to green                using the color picker, make them yellow

       With additive fixtures, Green is both in the start cue and the destination cue, so it
       will likely fade through white.

          Delay Green (drag the delay on the green bar towards the middle)                     watch the color path in the color picker

       When saving a new path, that data will then be referenced, and any changes made
       to that path will be used anytime that path is used.

          [Record] [Path]/{Color Path} [101] [Label] RGB-Avoid Green [Enter]                   saves the color path with a label
            Path will now be in the drop down menu as well.

### COLOR PATH DISPLAY LIST

             [Path] [Path] / {Color Path} {Color Path}                                         opens the Color Path List

### SAVE COLOR PATH FOR A FIXTURE

       If a fixture always has an undesirable color path, a path can be selected to run on
       that fixture every time it fades without having to record it in every cue.

          In Patch, {Attributes}, [301] {Color Path} [101] [Enter]                             uses that path everytime it fades

          [301] {Color Path} [Enter]                                                           removes the color path

### HELPFUL SUPPORT AND TRAINING LINKS

```text
           ETC Support Website                               ETC Technical Support                         Community – ETC Consoles
  All the support and training resources you might   Contact our 24/7 technical support team to help      Hop on the ETC forums to ask the user
              need in one handy place                         troubleshoot your ETC gear                   community your questions about Eos
                                                     https://www.etcconnect.com/Contact/Technical-       https://community.etcconnect.com/control_
```
       https://www.etcconnect.com/support
                                                                      Support.aspx                              consoles/eos-family-consoles/

```text
      Video Tutorials – Eos Family                    Support Knowledge Base Articles                                ETC Training
   Experience hands-on Eos training anywhere,        Get quick answers to your technical questions       Find in-person training opportunities near
  anytime with the series of videos and workbooks    with support articles created by ETC experts         you, as well as other learning resources
```
  https://www.etcconnect.com/Support/Tutorials/E
                                                          https://support.etcconnect.com/ETC               https://www.etcconnect.com/Training/
           os-Family-Videos/Overview.aspx

```text
           ETC Search Manuals                                  ETC LearningStage                               ETC Custom Training
  Search for manuals, datasheets, release notes,     Take part in a variety of online training courses   ETC offer multiple custom training options
          and more on the ETC website                        for technicians and operators                            to fit your needs
```
                                                                                                         https://www.etcconnect.com/Support/Traini
       https://www.etcconnect.com/Search-
                                                       https://learningstage.etcconnect.com/learn             ng-Events/Custom-Training.aspx
       Documentation.aspx?DocType=137

```text
      Eos Family Training Materials                          Educational Resources
     Find all of the Eos family Learning Series        These free materials provide a overview of
   workbooks and training materials in one place               essential lighting concepts
                                                     https://www.etcconnect.com/Support/Training-              https://www.etcconnect.com/
```
      https://www.etcconnect.com/workbooks/
                                                          Events/Educational-Resources.aspx

Corporate Headquarters  Middleton, WI, USA  Tel +608 831 4116  Service (Americas) service@etcconnect.com
London, UK  Tel +44 (0)20 8896 1000  Service (UK) service@etceurope.com
Holzkirchen, DE  Tel +49 (80 24) 47 00-0  Service (DE) techserv-hoki@etcconnect.com
Hong Kong  Tel + 852 2799 1220  Service (Asia) service@etcasia.com
Paris, FR  +33 1 4243 3535
Web etcconnect.com  © 2025 Electronic Theatre Controls, Inc.  Trademark and patent info: etcconnect.com/ip
Product information and specifications subject to change. ETC intends this document to be provided in its entirety.

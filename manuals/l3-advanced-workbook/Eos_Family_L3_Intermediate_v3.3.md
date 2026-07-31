# Eos Family Console Programming — Level 3: Intermediate Workbook (v3.3C)

- Source : PDF officiel ETC, « Eos Family Console Programming — Level 3: Intermediate Workbook (v3.3C) », V3.3C, publié 2026-05
- Fichier source : [`source/Eos_Family_L3_v3.3.pdf`](source/Eos_Family_L3_v3.3.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select


Eos Family Console Programming

          Level 3: Intermediate

                        Workbook
                                     V3.3C

            www.etcconnect.com/education

                             Released: 2026-05

## Table of Contents

ETC permits the reproduction of materials in this manual only for non-commercial purposes. All
     other rights are reserved by ETC.

4    Eos Family Level 3 Intermediate

## Purpose of the Class

    The class is intended for people who are well versed in Eos Family
    terminology, already know the layout of the desk, and are experienced
    conventional and intelligent fixture programmers. This class is intended to
    build on your knowledge, and make you faster.

### LEARNING OBJECTIVES:

        After completing this class, users should be able to:
          - Use advanced patch functions, such as copying and moving show data,
               editing fixture profiles, and creating keywords
          - Use advanced selection and manual control features
          - Define and use Highlight, Lowlight, and custom RemDim
          - Use the fan function on encoders, the command line, and for references
          - Control multiple-intensity fixtures
          - Apply and store filters
          - Use manual playback functions like Make Null, Make Manual, and
               Capture
          - Use advanced palette and preset modifiers
          - Use advanced cues, like Multipart, and multi-list
          - Create and use Macros
          - Utilize intermediate Magic Sheet skills

### SYNTAX ANNOTATION

          - Bold                           Browser menus
          - [Brackets]                     Facepanel buttons
          - {Braces}                       Softkeys and direct selects
          - <Angle brackets>               Optional keys
          - [Next] & [Last]                Press & hold simultaneously
          - «Direct Select»                Direct Select button press
          - MS Object                    Object on a Magic Sheet

          - Play Icon                      Link to video on ETC’s YouTube Channel -
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
        Please note that it is not available on Windows XP devices, but is available as a download
        from the web site.

### MERGE SHOW FILE DATA

### START THIS DAY IN LEVEL 2 COMPLETE !

Merging show files is how we bring data from another show file into our
current show file.

### MERGE COMPLETE TARGET LISTS

     From [Live}, [Go To Cue] [Out] [Enter]                                           start with a blank stage

     [Displays], {Browser}, File > Merge, select a show, and press [Select]           opens main Merge screen

   By default, all items are unselected. Selected items will turn gray. Incoming
   targets will overwrite existing targets if they share the same number.

### ADVANCED MERGE

   {Advanced} allows you to select specific ranges of the targets and place them
   where you want them in the current show file.
     - Start - The first in a range (such as a range of groups).
     - End - The last in a range of components.
     - Target - The desired location of the components in the new show file
        (for ranges, this will be the location in the new show of the first
        component in the range. The others will follow in order).

      {Groups}                                                                        selects what you want to merge
                                                                                      selects the starting number of the range from
      {Start} [6]
                                                                                      the stored show
      [Page►] to the End column, [23]                                                 sets the ending number of the range

      {Target} [206]                                                                  sets starting location in current show

      {Cues}                                                                          selects what you want to merge

      {List} {3}                                                                      from Cue List 3 in the stored show

      [Page►] to {List Target} {103}                                                  going into current show as Cue List 103
                                                                                      selects the starting number of the range from
      [Page►] to {Start} [1]
                                                                                      the stored show
      [Page►]to the End column, [5]                                                   sets the ending number of the range

      {Groups} [91] [Page►] [95]              or {Groups} [91] [Thru] [95]            multiple ranges of the same targets

      Don’t hit {Ok}!!!           {Cancel}                                            to go back to main Merge screen

        {Return} goes back to the full target display of Merge

6    Eos Family Level 3 Intermediate

### PATCH A MULTICELL FIXTURE

    Some fixtures have multiple segments, or cells, that can be individually
    controlled within a single fixture. For example, many linear LED fixtures
    have the ability to control different sections independently within the
    fixture, allowing us to assign a range of colors or intensities across one
    device. There are also some models of moving lights that have multiple
    moving parts within a single fixture. These types of fixtures can create
    dynamic effects and unique stage looks – but first we have to patch them as
    Multicell fixtures.

     In Patch
     [291] [Thru] [295] [Enter] {Type}                                                            selects the channels
                                                                                                  assigns the fixtures to the channels – notice
     Search SGM SP 6             in mode, select 6ch MC [6] [6 Cells]
                                                                                                  the parts (.1, .2…)

     [At] [4] [/] [411] [Enter]                                                                   assigns addresses to cells

        Note addresses are assigned to individual cells, not to the parent cell.
        Sometimes the parent and cells are labeled differently – pixels.

     [Live] and look at [291] [Enter]
     [291] [Thru] [295] [At] [Full] [Enter]
     [Clear] [Sneak] [Enter]

### CHANGING EXISTING TO MULTICELL

         In Patch [Group] [22] {Unpatch} [Enter] DON’T HIT ENTER AGAIN                            notice the message

        Notice it will remove all non-intensity parameter show data – we don’t want to do that!

         [Clear]

         {Type} Color Force II 72 RGBA x4 OFF MC [24] [6 cells]                                   no need to change addresses

         [Live] and look at [Group] [22] [Enter] or [301] [Enter]

## Multicell Channels

### WORKING WITH MULTICELL FIXTURES IN LIVE

   [Go To Cue] [Out] [Enter]
      Notice for these fixtures, the cells are at Full by default.

                                                                                                   selects parent and individual cells of entire
   [301] [Enter]
                                                                                                   channel
                                                                                                   posts channel cells only on command line –
   [301] [.] [Enter] posts Chan 301 Cell on the command line
                                                                                                   individual cells only selected
                                                                                                   posts channel minus cells on command line –
   [301] [Shift] & [.] [Enter] …. posts Chan 301 Minus Cells
                                                                                                   parent cell only selected
      [.] [0] selects just the parent cells - same as [Shift]&[.]

   [301] [Full] [Full]                                                                             full intensity in parent cells, lights on

         [Out]                                                                                     takes lights out

   [301] [Thru] [312] [Full] [Enter]                                                               lights on
                                                                                                   fans intensity across individual cells, parent cell
   [301] [Thru] [312] [.] [Full] [Thru] [10] [Enter]
                                                                                                   still at full
   [Select Last] [Full] [Full]

### USING OFFSET WITH MULTICELL CHANNELS

   [Select Last] {Offset} [4] [Out]                                                                notice channel selection

   [Select Last], [Clear] to remove the 4, {Mirror Out} [Full] [Thru] [10]
   [Enter]

### FLEXICHANNEL MODE

   [301] [Thru] [312] [Enter], then hold [Flexi]                                                   to see {Cells Off} and {Masters Off} options

  - Cells Off – collapses the individual cells, can also use [Flexi]&[.]
  - Masters Off – collapses the parent cell, leaving only the individual cells

   [Format]                                                                                        to go to summary view

   Hold [Flexi], select {Cells off}                                                                collapses all cells

      Channels that have individual cell intensities that are different from the parent cell are
             displayed with a ‘+’

   [Clear] [Sneak] [Enter]                                                                         takes all light out

   [Snapshot] [1] [Enter]                                                                          recalls Snapshot 1

8    Eos Family Level 3 Intermediate

    Patch Exercise - see Appendix 1

       Go to Appendix 1 – Channel Hookup in the back of the book (pg 50) to verify
       the patch and add the additional channels (Ignore Notes/labels).
       When done, do a Channel check and then save your show.

### CHANNEL/ADDRESS CHECK

                                                                                     quickly steps through all patched channels at
         [Live] [111] [Full] {Chan Check} [Enter] then [Next] … [Next] …
                                                                                     100%

### CHANNEL CHECK WITH MULTICELLS

         [301] [Thru] [312] [Full] [Enter]                                           parents and cells all at Full

         [301] [Thru] [312] [.] [Out]                                                takes cells out - no level

         [301] [Thru] [312] [.] [Full] {Chan Check} [Enter]                          now will bring one cell at a time to full

### UPDATE THE HOME PRESET

         [Clear] [161] [Thru] [168] [Full] [Enter] Tip up on stage …
                                                                                     update Home Preset to include these channels on
         [Select Last] {Focus} [Update] [Preset] [999] [Enter]
                                                                                     stage

### SAVE AS

       Please save the show file with a new name using Save As:
         [Displays], {Browser}, File > Save As > and select Show File Archive

         Do you really want to save? [Select] or click {OK}.

         Press [Label] to clear “Show File…”

         Enter a new show name                                                       Please do not overwrite the existing show file.

         [Enter] on either console or keyboard.

### DON’T FORGET! QUICK SAVE

         [Shift]&[Update]                                                            quick save

## Patch Features

### COPY CHANNELS IN PATCH

When you copy a channel in Patch, only the patch information is copied to
the target channel(s) – type, labels, all attributes, interface, and database
information.
  Recall Snapshot 1
                                                                                           copies only the fixture type (no address) to
  In Patch, [101] [Copy To] [106] [Enter]
                                                                                           new channel

To copy show data for a channel, use softkey modifiers. This will copy all
show data for the copied channels including data in cues, submasters,
palettes and presets, effects, and groups.

                                                                                           copies the patch and all show data to new
  [101] [Copy To] [107] {Plus Show} [Enter]
                                                                                           channel
                                                                                           copies only the show data to new channel,
  [101] [Copy To] [108] {Only Show} [Enter]
                                                                                           and doesn’t copy any patch info
  [Blind], [Format] to Spreadsheet, and be in Flexi-Active state in cue 21

  [101] [Thru] [108]                                                                       can see levels are copied

     [Shift]&[Format]                                                                      to hide non-intensity parameters

  Back in Patch, [101] [Copy To] [109] {Only Text} [Enter]                                 copies only the database information

### MOVE CHANNELS IN PATCH

When you move a channel in patch, you are essentially renaming it from
one channel number to another. All show file information and patch
information, including the address, is moved to the target channel, as well
as park information for the channel(s).

                                                                                           moves channel’s show and patch information
  [106] [Copy To] [Copy To] [110] [Enter]
                                                                                           to new channel

NOTE:      Certain show information will not get copied or moved when executed through
           Patch. This includes channel numbers called in macros, and channel objects in
           Magic Sheets and Pixel Maps.
NOTE:      When copying a channel, park information from the original channel does not
           copy to the target channel(s). However, when moving a channel, the move will
           be made in Park as well.

                                                                                           see that 107 is now in Focus Palette 1, you
        [Blind] [Focus Palette] [1] [Enter],    in Table View
                                                                                           will need to go back and fix its focus
        [Group] [Group]

          Notice that Group 5, 23 and 99 have extra channels in them
                                                                                           remove channels from these groups for
        [Group] [5] [+] [23] [+] [99] [Enter]     [-] [107] [Thru] [108] [Enter]
                                                                                           future operations

10    Eos Family Level 3 Intermediate

## Database & Keywords

     Each part of a channel can be assigned one note, up to ten keywords, and a
     gel swatch. These can be used to inform operators locally regarding
     attributes of the fixtures, working notes, or to assist with Query operations.
     Notes can accept paragraph-form text and are not utilized when using the
     [Query] function. Keywords can be defined in notation-style and can be
     searched with [Query].
       In {Patch}, {Database}                                                             navigates to the Database tab of Patch

### ADDING NOTES TO A CHANNEL OR PART

           [1] {Notes} Hung sideways from catwalk [Enter]                                 selects channel 1 and adds the note

           [152] [Thru] [154] [Part] [2] {Notes} rental units [Enter]                     selects part 2 of channels and adds note

               These notes are also visible in the About Channel display.

### ADDING GEL NOTES

           [1] [Thru] [10] {Gel} R033 [Enter]                                             adds text and a color swatch

           [201] [Thru] [209] {Gel} L201 [Enter]                                          adds text and a color swatch

### ADDING KEYWORDS TO CHANNELS OR PARTS

           From a clear command line – [Shift]&[Clear]
           {Text1} [Label] Lamp [Enter]                                                   changes Text1 to Lamp

           {Text2} [Label] Position [Enter]                                               changes Text2 to Position

           {Text3} [Label] System [Enter]                                                 changes Text3 to System

           [1] [Thru] [10] {Lamp}                                                         selects channels and text field
                                                                                          adds the new keyword to the database and
           {New Keyword} 575W [Enter]
                                                                                          automatically fills in text field
           [131] [Thru] [134] [+] [141] [Thru] [144] [+] [151] [Thru] [154] [+] [161]
                                                                                          selects channels and text field
           [Thru] [164] [+] [171] [Thru] [174] {Position}
                                                                                          adds the new keyword to the database and
           {New Keyword} SL Booms [Enter]
                                                                                          automatically fills in text field
           [135] [Thru] [138] [+] [145] [Thru] [148] [+] [155] [Thru] [158] [+] [165]
                                                                                          selects channels and text field
           [Thru] [168] [+] [175] [Thru] [178] {Position}
                                                                                          adds the new keyword to the database and
           {New Keyword} SR Booms [Enter]
                                                                                          automatically fills in text field
           [131] [Thru] [138] {System} {New Keyword} Head High [Enter]

           [171] [Thru] [178] {System} {New Keyword} Shins [Enter]

### KEYWORD BEST PRACTICES

           - Keywords are helpful if they are concise and consistent. Having
                 keywords such as “S4 19deg” is easy to understand, but having another
                 keyword “S4-19” will make it difficult to use [Query] to find channels
                 that you want. Re-use keywords that you have already established for
                 similar fixtures.

## Query

[Query] is used to find and select channels that meet conditional criteria
and keywords. Query will always result in either a channel selection or an
error (if no channels meet the criteria).

  Back in Live,         [Go To Cue] [Out] [Enter]
  [Record] [100] [Time] [2] [Block] [Assert] [Label] Blackout [Enter]
  [Group] [1] [At] [5] [Time] [7] [Enter]                                              set up some channels to use with Query

  [Group] [2] [At] [75] [Enter] [Color Palette] [6] [Enter]
  [Group] [20] {Offset} {Mirror In} [At] [10] [Thru] [Full] [Enter]
  [Color Palette] [6] [Enter]
  [Group] [5] [At] [80] [Enter] [Focus Palette] [1] [Enter]
  [103] [Full] [Full]
  [Record] [101] [Time] [3] [Enter]                                                    Records new look

### BASIC QUERY

  Be in Live Summary View, press [Displays] to open CIA
  [Query] [At] [75] [Enter]                                                            selects all channels currently at 75%

  [At] [50] [Enter]     [At] [Full] [Enter]   [Update] [Enter]                         takes them to 50%, and then to Full

### QUERY WITH KEYWORDS

                                                                                       keywords displayed in CIA - selects all channels
  [Query] {Text} {575W} [Enter]
                                                                                       with a 575w lamp
  [Query] {Text} {SL Booms} [Enter]
                                                                                       selects all channels in the SR Booms that are
  [Query] {Text} {SR Booms} {Fixture Type} {Scroller} [Enter]
                                                                                       scrollers
  [Full] [Full]                                                                        turns them on

  [Sneak] [Enter]                                                                      and sneaks them back out

    Check out all the options for Query in the CIA: the parameter tiles, Default,
    Text, and Fixture Types.

### QUERY SOFTKEYS

    {IS IN} & {ISN’T IN}
    The specified channels or parameters that are or are not currently at a specific
    value:
     [Query] {Is In} [Color Palette] [6] [Enter]                                       selects all channels currently in Color Palette 6
                                                                                       selects one channel (103) in Focus Palette 1
     [Query] {Is In} [Focus Palette] [1] [At] [Full] [Enter]
                                                                                       with an intensity of Full
                                                                                       selects channels in range that do not have a
     [1] [Thru] [50] [Query] {Isn’t In} [Time] [7] [Enter]
                                                                                       time of 7

12    Eos Family Level 3 Intermediate

### QUERY AND FLEXI

         [Live], [Flexi], and change the Flexi state to Active
        Remember a standard command line selection will return different values
        based on your Flexi State. Query ignores that Flexi state and returns any
        channel that meets the criteria of the query.

### OTHER QUERY MODIFIERS

                 {MOVES ONLY}
                 Finds anything in the current cue that has a move instruction
                                                                                               looks for anything that has a move instruction
                  [Query] [Cue] [5] {Moves only} [Enter]
                                                                                               in Cue 5

                 {UNPATCHED}
                 Finds channels that are not patched or do not have an address in Patch
                  [Query] {Unpatched} [Enter]                                                  looks for anything that is unpatched
                                                                                               looks for anything that is stored in the
                  [Query] {Unpatched} {Is In} [Cue] [1] [Thru] [Enter]
                                                                                               selection but is unpatched

                 Query ends in one of two ways: 1) channel selection that meets the
                 query or 2) an error message – no channels meet the query

                  [Query] [At] [40] [Enter]                                                    will return an error

                  [Shift]&[Clear]                                                              to remove error

### OTHER QUERY MODIFIERS

         - Can Be -                                  •   Can’t Be -
         - Or                                        •   Moves Only
         - Less Than (and equal to)                  •   Greater Than (and equal to)
         - Mark (cue where intensity is active)      •   Broken Mark
         - Marking (future cue)                      •   Track
         - Up Moves                                  •   Down Moves
         - Live Moves                                •   Dark Moves
         - Block                                     •   Autoblock
         - Assert                                    •   Part
         - Park                                      •   Delay
         - Capture

### QUERY BEST PRACTICES

             - Query results are not altered by Flexi – it will select channels that are
                   true even if they are not in the current flexi view.
             - Query works great in Blind Spreadsheet.
             - Save frequently used Queries as macros for quick dynamic channel
                   selection.

## Macros

A Macro is an automated series of console actions. Macros are a way to
automate repetitive, complex or hard-to-reach commands in the desk.

### LEARN A MACRO

                                                                                                     button flashes green, “Learning Macro 1”
 [Live]        [Learn] [1] [Enter]          places console in Learn mode
                                                                                                     flashes above CIA command line
 [Stop Effect] [Enter] then hit [Learn]                                                              records ‘Stop Effect’ command as macro
        On Apex consoles, [Shift]&[Effect] is the Stop Effect command. Also
        [Effect] [#] [At] will post Stop Effect on the command line.

 [Group] [99] [Enter]

 Press [Displays]                                                                                    to open the CIA

 [Learn] [2] [Enter] [Select Last] {Saturation} [At] [/] [90] [Enter] [Learn]
                                                                                                     records macro that records last selection of
 [Learn] [3] [Enter] [Select Last] [Record] [Focus Palette] [Next] [Enter] [Learn]
                                                                                                     channels into a new focus palette

### RECALL A MACRO

 Recall Snapshot 2                                                                                   to see the color picker and Direct Selects

 [Group] [2] [Thru] [4] [Full] [Rem Dim] [Enter] [Color Palette] [1] [Enter]                         will make color less saturated

 [Macro] [2] [Enter]                                                                                 macro makes the color less saturated

 [Macro] [2] [Enter]                                                                                 less saturated again

### DESK SETTINGS IN MACROS

 [Displays] {Setup} {System} {Mobile Apps}                                                           to be in right place to record macro

 [Learn] [4] [Enter]      {Allow App Connections} [Learn]                                            remember this is a toggle option

NOTE: In addition to calling a macro on the command line, macros can be called by a direct select,
      magic sheet button, a cue execute, a system command, or a connected show control system.

### MACRO EDITOR DISPLAY

  The Macro editor display allows you to edit macros, and access
  softkeys that aren’t available from all areas of the desk.
   Recall Snapshot 1

   [Macro] [Macro]                                                                                   opens macro editor

   [1] [Label] Stop FX [Enter]                                                                       label the macro

   [Next] [Label] Desaturate [Enter]

   [Next] [Label] Rec Next FP [Enter]

   [Next] [Label] App Enable [Enter]

14     Eos Family Level 3 Intermediate

### EDITING A MACRO

           Select Macro 4, press {Edit} or [Learn]                                                        enters Edit mode for the macro

           Using [Page ] and [Page ] to select “Clear_CmdLine”
                                                                                                          Do not use the hard key delete when editing a
           Use the softkey {Delete}!!
                                                                                                          macro – it adds Delete to the macro.
           [Page ] to , Find “Enable” in the “Common” section in the CIA

           [Learn] or {Done}

           [4] [Copy To] [5] [Enter]

           {Edit}, highlight “Enable”, {Delete}

```text
           Click on the magnifying glass icon                          (below lamp controls)              opens a search window
           Type in “Disable” and when it appears, double click on Disable in the list                     puts Disable in the macro editor

           Don’t forget [Learn] or {Done}!!                                                               exits Edit mode for the macro.
```

           [Label] RFR Disable [Enter]

     NOTE: Cursor can be moved using page left and right keys. In Edit mode, only your page arrow keys,
           Escape, Select, and softkeys will not post to the Macro. All hard keys and CIA softkeys will
           post into the macro and play back each time the macro is called.

          The Macro list should look something like this:

## Custom Direct Selects

Custom Direct Selects (CDS) support thousands of custom target lists, which
can be mapped to any direct select tab.

### ASSIGNING TARGETS

     Recall Snapshot 2

     Press «Groups» and choose «Custom» as the target type                                              CDS Layout window opens

     Choose tile 11 and press {Confirm Create}                                                          Starts a list of targets
                                                                                                        Opens a pop-up that allows the user to
     Click on the first empty tile, DS 1
                                                                                                        populate the DS
                                                                                                        Fills in first CDS with channel 1 – label comes
     Choose {Channels}, Start at {1} {Enter}, {Enter}, and hit {OK}
                                                                                                        from Label field in Patch.
     Click on the next empty tile, DS 2                                                                 Opens the pop-up

     {Channels}, Start at {2} {Enter}, End at {10} {Enter}, Offset 1 {Enter} and hit
                                                                                                        Fills in CDS 2 – 10.
     {OK}
     Type [FP] [1] [Thru] [5], then double tap a tile, DS 11                                            Populates tiles using the command line

     [Shift]&[Clear]                                                                                    To clear the command line

     Note: To assign a range of channels to the direct selects, you can also use the configuration
           window. From the command line, you can only assign one channel at a time.

### CLEARING CUSTOM DIRECT SELECTS

   Use [Escape] to clear custom DS

     Hold down [Escape] and tap the last channel DS (10)                                                It disappears

     Hold [Escape] and then long-press the channel DS (1) until a red X appears.                        To delete a range

     While still holding down [Escape], touch the last channel DS (9)                                   That range will be removed

   Remember that this is only removing the target from your CDS, it is not
   deleting the content from your show file.
     [IP] [1], then double tap DS 10

### CUSTOM DIRECT SELECT EDITOR (BLIND)

   You may want to change to full screen and collapse the CIA.
     Tap target type «Custom», then choose «Custom» again
                                                                                                        Opens Tab 39, can also be opened from the
     In the CDS Layout selector, press {Open Custom DS Editor}
                                                                                                        Add-a-Tab screen

   Notice the list at the bottom – a list of CDS layouts

     With 11 highlighted, [Label] Mixed Targets [Enter]

16   Eos Family Level 3 Intermediate

### LAYOUTS

       The CDS Editor allows us to audition some common row/column layouts using
       the shortcuts at the top, or we can create custom numbers of rows/columns.
       Note that changing these in the Editor does not have any bearing on using the
       DS in a frame – that will be determined by the size of the DS tab in each frame.
        Look at the layout with 25. Look at layout with 10 rows x 1 column                = the layout for the target keys on Apex

           Note that as the arrangement of targets changes – each target stays
           mapped to its same DS number. IP1 is always on DS10 no matter which
           layout.
        Let’s go back to 50

### CUT/COPY/PASTE BUTTONS.

        Use your mouse to click and drag around our 5 focus palletes                      Also known as lassoing…
           If just click on focus palettes and not in order, different results.
                                                                                          Notice the preview of the order below the
        Press {Copy}
                                                                                          cut/copy buttons
        Tap on the first tile in the next row down and press {Paste}

### ADD CUSTOM DIRECT SELECTS IN THE EDITOR

        Tap on Tile 1, {Color Palettes}, Start at 1, End at 7, Offset 1, [Enter]          Just like adding DS in Live

        Press {Apply}
           There is the option to include non-existent whole number targets in case
           space is needed for future targets. It is checked by default.
        Lasso the entire bottom row of tiles (41 – 50)

        Press {Presets} then Start at 1 {Enter], Offset 1 {Enter}

        Uncheck the “Include Non-Existent Whole Number Targets” box                       If left checked, would have 3 to 998

        Press {Apply}                                                                     Only fills in existing stored presets

### ADD CONSOLE BUTTONS

       We can also assign tiles to be console buttons (like we can on magic sheets)
       and navigation buttons.

        Tap on an empty tile, then press {Button}
        Top drop down menu – leave as Console Button
        In the second drop down menu, select {Offset} and tap {Apply}                     Menu includes all hard and soft key options

        Lasso the bottom row of presets and the offset button                             Can also tap to select them 1 at a time

        Press {Delete}

        Tap on Tile #40 in lower right corner, then press {Button}
                                                                                          Function like the Page Up/ Down arrows that
        Use the top drop down to select {Next Page/Prev Page}
                                                                                          can be toggled on/off in DS modules
        Choose {Prev Page} and hit {Apply}
        Tap on Tile #50, choose {Next Page}, {Apply}

### BUILD LAYOUT TO MIMIC EOS TI MACRO BUTTONS

 On the console, [Copy To] [12] [Enter]

 Press [Label] [Label] Macros [Enter]
 Lasso the top 3 rows of tiles and click {Delete}                                                      Removes all tiles except Next/Prev Page

 Select the tiles in the order that they appear on the console
    Targets will populate in the order that the tiles were selected.

 Press {Macros} then Start at 801 {Enter}, {Enter}
 Press {Apply}                                                                                         Fills in macros 801 through 808

 Press {}                                                                                             To move down a page

 Select 10 more tiles
 Press {Macros} then Start at 1 {Enter}, {Enter}
 Press {Apply}                                                                                         Fills in macros 1 through 10

 Press {}                                                                                             To move back or up a page

 Tap the tile above {Prev Page}, then press {Button}
 Use the top drop down to select {Jump To}                                                             Can jump with in a list or to another list

 Below Jump To, click on Same List, then on 11: Mixed Targets
      Can also select where in the list to jump to - leave as 1
 Press {Apply}                                                                                         Tile reads Jump to 11/1 (List 11, Tile 1)

 Lasso the {Jump To} and both page buttons. Press {Copy}

 Press {}, select tile 80, press {Paste}                                                              Adds navigation button to first page

 Select just {Jump To} and press {Copy}

 Press [Last] to switch back to our first layout, Mixed Targets

 Go back to the first page, select tile 30 and press {Paste}

 Click on {Jump To} on right, edit list to Macros list (12), {Apply}                                   Basically, you are selecting a different list

 Delete the top row of Focus Palettes                                                                  leaving an empty row between CP and FP

 Recall Snapshot 2

 Replace Group DS with Custom DS - Mixed Targets

 Replace Color Picker with DS - Groups

 Press «Jump To 12/1» to navigate to Macros. Press «Next Page», then
 «Jump To 11/1» again

 [Group] [20], «100%», pick a color                                                                    Works just like the rest of Direct Selects

 Record Snapshot 3
    Note:   Show files saved in versions prior to v3.1 will bring in their custom DS layouts as long
            as they were stored into a Snapshot.

18    Eos Family Level 3 Intermediate

### MULTICELL CHANNELS IN GROUPS

          [Group] [Group]                                                                 to go into the Group List
                                                                                          to create a group of the whole multicell
          [Group] [31] [Enter], [301] [Thru] [312] [Enter]
                                                                                          fixtures
          [Label] MC Whole [Enter]
                                                                                          to create a group with the cells only of the
          [Group] [32] [Enter], [301] [Thru] [312] [.] [Enter]
                                                                                          selected multicell fixtures
          [Label] MC Cells [Enter]
                                                                                          to create a group with the cells only of the
          [Group] [33] [Enter], [301] [.] [1] [Thru] [306] [.] [3] [Enter]
                                                                                          selected multicell fixtures
          [Label] Cyc Cells SL [Enter]

          [Group] [34] [Enter], [301] [Thru] [312] [Shift]&[.] [Enter]                    to create a group with only parent cells

          [Label] MC Minus Cells [Enter]

          [Group] [35] [Enter], [301] [Thru] [312] [.] {Offset} {Mirror Out} [Enter]      using offset

          [Label] Cyc Top Cells Mirror Out [Enter]

          [Group] [35] [Copy To] [36] [Enter]                                             creates a copy of the group

          [Group] [36] [Enter], {Reverse} [Enter]                                         reverses the content of the group

          [Label] Cyc Top Cells Mirror In [Enter]

          [Group] [41] [Enter]

          [301] [Thru] [312] [+] [351] [Thru] [362] [.] {Offset} {Mirror out} [Enter]

          [Live]      [Group] [22] [Full] [Full]

          [Group] [41] [Color Palette] [2] [+] [7] [Enter]                                that’s not what we want!

            Mirroring out entire selection, want them to mirror out in pairs

          [Group] [Group]

          [Group] [41] [Enter]
          [301] [Thru] [312] [+] [351] [Thru] [362] [.] {Offset} {Mirror out} {Chan per
          Group} [2] {Interleave} [Enter] [Enter]
          [Live], [Group] [41] [Color Palette] [2] [+] [7] [Enter]                        mirrors out in pairs across cyc

          [Group] [Group]

          [Group] [41] [Label] Full Cyc Mirror Out [Enter]

          [Group] [41] [Copy To] [42] [Enter]

          {Reverse} [Enter]

          [Group] [42] [Label] Full Cyc Mirror In [Enter]

Let’s look at some additional channel selection offset tools.

### MULTIPLE OFFSETS ON THE COMMAND LINE

  [Live]

```text
  [301] [Thru] [312] [.] {Offset} {Even} [+] [(] [351] [Thru] [362] [.] {Offset}                     [Shift]&[/] = ( ). Out command closes the
  {Jump} [4] [Out]                                                                                   parenthesis on the command line
```
    Note that with a single channel selection we were able to turn off the even numbered cells
            on the top cyc and every 4th cell on the bottom cyc

  [Full] [Full]                                                                                      To restore all cells back to full

### RANDOM SUBGROUPS

  [301] [thru] [312] [.] {Offset} {Random Subgroups}                                                 This is the same as using “Random”

  {Num Groups} [12]                                                                                  Creates 12 sub-groups in a random order
                                                                                                     To re-distribute the channels throughout the
  {Interleave}
                                                                                                     12 groups
  Press {Reorder}, {Reorder}, {Reorder}                                                              To get a new random selection

  [Shift] & [Clear]                                                                                  To clear the command line

### USING OFFSET INSIDE & OUTSIDE OF SUBGROUPS

  [Group] [32] [Out]            [Shift] & [Clear]
  [(] [301] [thru] [312] [.] {Offset} {Mirror in} [)] {Offset} {Odd} [@] [0] [Thru]
  [Full] [Enter]

20    Eos Family Level 3 Intermediate

## Manual Control

### REMDIM

     RemDim can be used to take all active channels that are not in a selection,
     and force them to a lower level.

### ABSOLUTE REMDIM

           Recall Snapshot 1              [Live]   [Go To Cue] [Out] [Enter]

           [1] [Thru] [5] [Full] [Full]                                            turns on channels
                                                                                   puts channel 1 at 50, and forces all other
           [1] [At] [5] [RemDim] [Enter]
                                                                                   channels to 0
           [5] [Thru] [2] [At] [1] [Thru] [3] [Enter]                              sets channels at different levels
                                                                                   puts channel at 50, and any channels that are
           [10] [At] [5] [RemDim] [20] [Enter]                                     above 20 to 20, any values below 20 stay at
                                                                                   their current value
                                                                                   toggles RemDim off – only works once,
           [RemDim]                                                                immediately after a RemDim command is
                                                                                   completed (mini-Undo)

### PROPORTIONAL REMDIM

           [1] [Thru] [10] [At] [50] [Enter]                                       puts channels at 50
                                                                                   puts selected channels at 75, and puts all other
           [Group] [2] [At] [75] [RemDim] [/] [50] [Enter]
                                                                                   channels at 50% of their current level

### HIGHLIGHT & LOWLIGHT

     Highlight mode allows you to put fixtures into a temporary, pre-defined
     state. You can use the desk’s defaults for Highlight, or define your own
     Highlight, Lowlight, and Highlight RemDim behaviors.

### USING HIGHLIGHT MODE

         Highlight is very useful to isolate and adjust individual fixtures.
          [Clear] [Sneak] [Enter]

          [High]/{Highlight} [Enter]                                               enters Highlight mode – look at command line
                                                                                   selects first channel in a group, turns others off
          [Group] [5] [Enter], then [Next]
                                                                                   and advances thru group
             [Next]…[Next] and focus each light on crate on far stage right        notice yellow HL on each channel

          [Select Last] [Record] [Focus Palette] [7] [Label] Crate [Enter]         records Focus Palette 7

          [High]/{Highlight}                                                       exits Highlight mode – no [Enter] required

### HIGHLIGHT & LOWLIGHT PRESETS

    [Clear] [Sneak] [Enter]
                                                                                                    selects all the moving lights
    [Group] [23] [Full] [Full]
                                                                                                    records intensity, color & beam into preset,
    [Select Last] [-] {Focus} [Record] [Preset] [997] [Label] Highlight [Enter]
                                                                                                    not pan & tilt (focus)

    [Select Last] [Enter], run cyan and magenta to full and yellow out to make
    them all dark blue, [At] [50] [Enter],
                                                                                                    records new preset with color set as blue and
    [Select Last] [-] {Focus} [Record] [Preset] [998] [Label] Lowlight [Enter]
                                                                                                    intensity at 50%

### DEFINE HIGHLIGHT, LOWLIGHT AND HIGHLIGHT REMDIM LEVELS

  There are three levels that can be defined with presets or hard values.
   [Displays] {Setup} {User} {Manual Control}
   {Highlight Preset} [997] [Enter]                                                                 defines Preset 997 as Highlight preset

   {Lowlight Preset} [998] [Enter]                                                                  defines Preset 998 as Lowlight preset

   {Highlight RemDim} [20] [Enter]                                                                  puts in a value for Highlight RemDim

    NOTE:    You can set Highlight RemDim as a hard percentage value (like the example
             above), a [/] value (percentage) or as a preset.

### USING HIGHLIGHT MODE

   [Live] [Go To Cue] [101] [Enter]                                                                 go back to Live and into a cue
                                                                                                    go into Highlight mode, levels drop to
   [High]/{Highlight} [Enter]
                                                                                                    Highlight RemDim value (20)
                                                                                                    puts current channel within selection at
                                                                                                    Highlight level, puts remainder of channels
   [Group] [7] [Enter] … [Next],* [Next], [Next]                                                    within selection at Lowlight level, and puts all
                                                                                                    unselected channels at Highlight Rem Dim
                                                                                                    level
    Note:    101 is in Highlight Preset (HL), rest of Group 99 is using Lowlight Preset (LL), and
             all channels outside of the selection are manual (red) using the Highlight
             RemDim level.
                                                                                                    still in Highlight, focus all 5 fixtures downstage
   [Group] [5] [Enter] [Next], focus downstage center, [Next], [Next]…
                                                                                                    center
                                                                                                    selects the channels and records them into a
   [Select Last] [Record] [Focus Palette] [11] [Label] Down Center [Enter]
                                                                                                    focus palette
   [High]/{Highlight}                                                                               exits Highlight, restores look on stage

   [Record] [102] [Enter]

### HIGHLIGHT & LOWLIGHT BEST PRACTICES

    - Highlight is a great way to quickly build up focus palettes for a group of
        fixtures.
    - Highlight can be helpful to see lights in a rig when there is ambient light
        you cannot control, like work lights, or while programming outdoors.
    - With Highlight RemDim disabled, all channels not in the selected group
        remain at their current values. So you’ll have light on stage.

22    Eos Family Level 3 Intermediate

## Fan

     It is possible to take a selection of channels, and quickly spread across them
     a range of mathmatical values – such as intensity, focus (pan & tilt), color, or
     beam values.

### COMMAND LINE FAN

           [Go To Cue] [Out] [Enter]                                                          takes us to a clean stage
                                                                                              fans the intensities across the channel
           [1] [Thru] [5] [At] [10] [Thru] [Full] [Enter]
                                                                                              selection and defined intensity range
           Be in Table View on the Live display

           [351] [Thru] [362] [Full] [Full]                                                   puts parent cells at Full
                                                                                              channel selection matters, look at cells of
           [Select Last] [.] [At] [10] [Thru] [Full] [Enter]
                                                                                              each fixture, nice gradient
           [Select Last] [Fan] {Mirror Out} [At] [10] [Thru] [Full] [Enter]                   creates dark center
                                                                                              intensity repeats across 4 subgroups,
           [Select Last] [Fan] {Repeat} [4] [At] [10] [Thru] [Full] [Enter]
                                                                                              scalloping on the cyced

### FAN MODIFIERS

             Fan is a mode. When enabled, any parameter that is moved will spread
             evenly across the selection based on the styles below.
             – {Center} – The middle channel in the order is the start and remains
                 unchanged; first and last channels change in different directions.
             – {Reverse} – The selected channel order is reversed
             – {Mirror Out} – The middle channel in the selected order is the starting
                 channel; the first and last channels are the end channels.
             – {Repeat} – The number of times a pattern is repeated within a selection
                 [31] [Thru] [42] [Fan] {Repeat} [3] [At] [50] [Thru] [70] [Enter] – Fans
                 the intensity values of 50 to 70 across channels 31 to 34, 35 to 38, and
                 39 to 42.
             – {Cluster} –The channels are put into collections, which contain channels
                 with all of the same value. [31] [Thru] [42] [Fan] {Cluster} [4] [At] [50]
                 [Thru] [70] [Enter] - sets channels 31 to 34 at 50%, 35 to 38 at 60%,
                 and 39 to 42 at 70%.
             – {Random Channels} – selected channels are put in a random order
             – {Forward} is the default Fan mode, on the second page of softkeys

### FAN PARAMETERS

           Recall Snapshot 3                                                                  recalls the Direct Selects

           «FOH Movers» (G5) [Full] [RemDim] [Enter]           «Singer» (FP2)

           [Fan] [Enter]                                                                      enables Fan mode in Forward as the default
                                                                                              first channel is anchor, and others fan relative
           Move the Pan encoder
                                                                                              to the first channel
                                                                                              look at beams – White to Cyan across the
           Move the Cyan encoder
                                                                                              fixtures, first channel unaffected
           Run the Level Wheel up and down                                                    same with intensity

  Touch «Singer»                                                                           sets fixtures back to Focus Palette 2

  [Fan] {Center} [Enter]
                                                                                           center channel is anchor, and channels fan
  Move the Pan encoder
                                                                                           out from the middle
                                                                                           same, channels fan up and down from the
  Move the Tilt encoder
                                                                                           middle
  Touch «Singer»                                                                           puts all fixtures back on Singer

  «MC Minus Cells» (G34) [Full] [Full]                                                     brings up the cyc fixtures

  «MC Cells» (G32) [Fan] {Mirror Out} [Enter]
  Roll Amber out and then Green out                                                        watch how the fixtures respond now

  [Fan] {Mirror Out} {Repeat} [3] [Enter]                                                  repeats the fan in the selection

  Roll out all of the Red and slowly dial in the Green                                     3 separate subgroups

  Note:     Pressing and holding [Fan] remembers the last fan state used without putting
            Fan on the command line again.

### FAN REFERENCES

It is possible to fan referenced data over a range of channels.
                                                                                           creates a gradient fan between the two color
  [Group] [20] [Full] [Enter]       [Color Palette] [1] [+] [6] [Enter]
                                                                                           palettes
                                                                                           fans the movers between guitars and drums,
  [Group] [5] [Focus Palette] [1] [+] [3] [Enter]
                                                                                           like a line from one to the other
  [Select Last] [Sneak] [Enter]
                                                                                           fans all seven color palettes across the
  [Group] [20] [Color Palette] [1] [Thru] [7] [Enter]
                                                                                           channels, and repeats
  [Select Last] [Fan] {Mirror Out} {Cluster} [2] [Color Palette] [1] [Thru] [7]
                                                                                           assigns a color palette to each subgroup of 2
  [Enter]
  [Record] [102] [.] [5] [Enter]

### FAN DISCRETE TIMING

Ranges can be used to fan discrete time and delays.
  [Group] [2] [Full] [Full]
  [101] [+] [103] [Preset] [1] [Enter]
  [104] [+] [105] [At] [80] [Enter], «Drums» (FP3)                                         on drummer

  [102] [At] [80] [Enter], «Guitar» (FP1)                                                  on guitar

  [Group] [22] «Dk Blue» (CP6)                                                             Cyc in dk blue

  [Clear]
  ( [101] [+] [103] ) [+] [102] [+] ( [104] [+] [105] ) [Time] [2] [Thru] [12] [Enter]     [Shift}&[/] to create the ( )

  Hold [Time] display key          (or [About]&[Time] on other consoles)                   to see channel timing

  [Group] [41] [Delay] [0] [Thru] [6] [Enter]
  Hold [Time] display key again                                                            only applied to cells

  [Record] [103] [Enter]
  [Go To Cue] [102] [Enter]         press [] (Go)       and [] (Go)                      watch cue 102.5 and then cue 103

  Note:     To view discrete timing, hold the Time Display button or [About]&[Time].
            [About] [Time] [Time] latches the timing view.

24   Eos Family Level 3 Intermediate

     Building Palettes

### RECORDING COLOR PALETTES WITH MACROS

        Recall Snapshot 3               [Go To Cue] [Out] [Enter]
                                                                                     builds new Color Palette with macros and
        [Group] [99] [Full] [Full]      Touch «Red» (CP1)
                                                                                     Direct Selects
        [Macro] [2] [Enter]                                                          use the desaturate macro

        [Select Last] [Record] [Color Palette] [11] [Label] Lt Red [Enter]           stores new Color Palette

        Double tap the blank custom direct select under «Red»                        adds it to the Direct Selects

        Touch «Orange» (CP2) [Macro] [2] [Enter]                                     use the desaturate macro

        [Record] [Color Palette] [12] [Label] Lt Orange [Enter]                      stores new Color Palette

        Double tap the blank custom direct select under «Orange»                     adds it to the Direct Selects

        Touch «Yellow» (CP3)         [Macro] [2] [Enter]                             use the desaturate macro

        [Record] [Color Palette] [13] [Label] Lt Yellow [Enter]                      stores new Color Palette

        Double tap the blank custom direct select under «Yellow»                     adds it to the Direct Selects

        Collapse CIA
        Change each frame to have 2 banks: bottom left - Focus Palettes and bottom
        right - Macros
        [Record] [Snapshot] [4] [Enter]

       Snapshot Four should look something like this:

                                                                                     Building Palettes                25

### RECORDING FOCUS PALETTES WITH MACROS

 [Clear] [Sneak] [Enter]

 Touch «OS Movers Wash» «100%», [Form] {Zoom} [19] [Enter] (G7)

 Tilt fixtures up until at the SL & SR edges of stage, in line with the proscenium   builds new Focus Palette

 «Rec Next FP» [Label] X Stage Look [Enter]                                          stores new Focus Palette

 [Select Last] [Enter] and tilt fixtures up until they are in the grid

 «Rec Next FP» [Label] Flyout [Enter]                                                stores new Focus Palette

### RECORDING PALETTES WITH HIGHLIGHT & FAN

 [High]/{Highlight} [Enter]                                                          toggle Highlight mode on
                                                                                     notice that only Pan is fanned – they tilt
 [Select Last] {Offset} {Chan Per Group} [2] {Pan} [Fan] {Center} [Enter]
                                                                                     together
 Tilt all fixtures back down, so they are all on center line

 [Next]

 [Next] Pan/tilt these fixtures downstage on top of the first pair

 [Next] Pan/tilt these fixtures downstage on top of others

 [Next] Pan/tilt these fixtures downstage on top of others

 [Select Last]    [Update] «Down Center» (FP11)                                      updates Focus Palette

 [High]/{Highlight}                                                                  to exit Highlight mode

26   Eos Family Level 3 Intermediate

## Reference Data Explanation

### REFERENCED DATA

       Another feature that moving light desks gave us has to do with the oft-times
       repetitive nature of working with automated lighting. It quickly became appar-
       ent that the act of setting lights manually to the down stage left sofa each time
       you wanted them there or putting them in the closest approximation of R80
       repeatedly was time consuming and, well… boring. Enter referenced data,
       typically called palettes. These smaller record targets are building blocks upon
       which cues can be built. Palettes are constructed from “absolute data” – the
       term that we use for lights that have values provided from encoders and/ or a
       keypad (channel 5 at 50, cyan at 35, magenta at 20 and yellow at 0 are
       examples of absolute data).

       Palettes can contain intensity, focus, color, or beam parameters, depending on
       the palette type. Palettes can only contain their type of parameter data. This
       automatic selective storing by category makes it faster to set them up. Most
       desks support “all palettes”, which allow you to put any data into one of these
       referenced building blocks. Typically, you focus any lights you might want on
       the down stage left sofa on that sofa and store them in focus palette ‘n’. Then,
       when you later need one of your lights on the sofa, you just select it and recall
       focus palette n. When the director later moves the sofa three feet to the left at
       the last dress rehearsal, you are left with one focus palette to update instead of
       300 individual cues. The modification to this focus palette then propagates
       through all the cues in which it was used.

### ABSOLUTE             STORED

### MANUAL              REFERENCED

       A bit of data theory – a piece of data is always in two states, each with two
       options. First, a piece of data is either manual or it is stored. To convert
       something from manual to stored, you simply record it. There are tools to make
       data manual as well.

       Second, data is either absolute or referenced. Absolute data are hard numbers
       that don’t point to any other location in the show file. But palettes and presets
       are referenced data, meaning the data is stored in a “bucket,” not directly in
       the cue. The cue looks into the bucket every time it is called and replays that
       data. This means that if a reference is used in multiple places in a show, it can
       easily be changed globally. Let’s say there is a couch that is in several scenes,
       and you make a focus palette for the couch and store it in several cues. When
       the director decides to move the couch, you can update the focus palette, thus
       changing all the cues in which it is stored, so you don’t have to go into every
       cue and change it one by one.

## Data Manipulation Tools

Data is always either Manual or Stored, and it is always either Absolute or
Referenced. To convert from Manual to Stored, simply Record. Absolute
data is numeric or hard data. Referenced data such as palettes and presets
are combinations of parameter settings that get used over and over. The
desk offers different tools to collect and handle these different data types,
and to convert data between.

### CHANGE ABSOLUTE TO REFERENCE

 [Live]       Recall Snapshot 2
 [Go To Cue] [28] [Enter]
 [Group] [21] [Full] [Full], in Color Picker, Standard Colors, choose Blue              cyc channels have manual (red) data

 [Group] [22] [Record] [Color Palette] [21] [Label] Split Cyc [Enter]                   all channels are manual & referenced

 [Blind], [Format] to be in table view
 [Color Palette] [21] [Enter]                                                           all cyc channels have data stored

### CHANGE REFERENCE TO ABSOLUTE (MAKE ABSOLUTE)

 [Live], be in table view, looking at channel 101                                       current Focus values have references

 [101] [+] [104] {Focus} {Make Absolute} [Enter]                                        breaks the references, leaving manual

 [Select Manual] [-] [101] [Record] [Preset] [11] [Enter]                               selects only channels with manual data (- 101)
                                                                                        stored all the data for 104 as well cyc
 [Blind] [Preset] [11] [Enter]     [104] [Enter]
                                                                                        channels that were manual as well
    Select Manual command includes the entire channel, even if only some
    parameters have manual values.

### CHANGE MANUAL TO STORED

 [Live]   [Update] [Enter]       (still in cue 28)                                      converts all manual values to stored values

 Look at [301] [Enter]                                                                  data is stored and referenced (PR11)

 Look at [101] [Enter]                                                                  Focus data is stored and absolute

### MAKE MANUAL & RECORD ONLY

 [103] [Full] [Full]     {Beam} [Home] [Enter]                                          adds manual values

 [Focus Palette] [3] [Enter]                                                            Intensity and Focus values are manual

 [104] [+] [105] {Focus} {Make Man} [Enter]                                             converts stored values to manual values (red)

 [Clear] command line
 [Record Only] [Preset] [12] [Enter]                                                    stores only manual data to selected target
                                                                                        only things that were manual (red) were
 [Blind] [Preset] [12] [Enter]     [101] [Enter]
                                                                                        stored
    Record Only is not a selection tool; it is a store manual values tool. Therefore,
    only the manual data was stored into this Preset.

28    Eos Family Level 3 Intermediate

## Update

     Update is a ‘save changes’ tool. It only pertains to values that are red or
     modified – values that have been changed. Update saves manual changes
     back to targets such as cues, palettes, presets and submasters.

      [Live]      [Go To Cue] [35] [Enter]
                                                                                                             note that the focus information is stored in a
      [104] [Enter]
                                                                                                             reference (drums)
                                                                                                             data is now manual and absolute – notice the
      Pan/tilt fixture up to the figure SL on staircase (behind the drummer)
                                                                                                             red ‘R’s
```text
      [Update]         look at where it’s updating, default style on right                                   (straight to cue as absolute data)
      [Enter]                                                                                                no longer a reference
```
      [105] [Preset] [1] [Enter]
      [101] [Enter], make a slight adjustment to the focus on the drums
                                                                                                             look at where the values are updating – targets
      [Update] {All} [Enter]
                                                                                                             and cues *
     Note:    Remember that updating a palette or preset will change it everywhere it is used in the show.

### TO CHANGE DEFAULTS OF UPDATE DISPLAY

             Go into Setup > User > Record Defaults
             Change {Update Mode} to All
             Disable {Break Nested}             Disable {Update Last Ref}
                                                                                                             Update style and modifiers changed to new
             [Live],    [Update] to see the changes                  [Clear]
                                                                                                             defaults

### UPDATE MODIFIERS

### UPDATE LAST REF

             [103] [Focus Palette] [4], pan/tilt to make slight adjustments                                  manual and absolute – notice red ‘R’s
                                                                                                             look at where the values are updating – FP2
                                                                                                             (Singer) which is stored in cue 35
                                                                                                             changes to FP4 (Low Platform), the most
             {Last Ref}
                                                                                                             recently used manual reference
             [Enter]                                                                                         new FP4 (Low Platform) stored in cue

### UPDATE BREAK NESTED

             [105] [Enter], iris down to headshot, pan/tilt up to head                                       Iris and Pan/Tilt have red ‘R’s
                                                                                                             Notice 105 is updating into Preset 1 and FP2 –
             [{Snapshot}] [1] [Enter]        [Update]      Do not hit Enter!       [Clear]
                                                                                                             do you want to change FP for rest of show?
                                                                                                             look at focus (stored as referenced data) and iris
             [Blind] [Preset] [1] [Enter]       [105] [Enter]
                                                                                                             (stored as absolute data)
                                                                                                             look at where it’s updating (preset 1 only, not
             [Live]       [Update] {Break Nested}          [Enter]
                                                                                                             the FP)
             [Blind] [Preset] [1] [Enter]       [105] [Enter]                                                notice Absolute data for iris and pan/tile
                Singer FP did not get updated. The Pan/Tilt data from channel 105 was
                stored in Preset 1 as absolute data, not referenced data

### UPDATE REF ONLY

 [Live]
 [102] [Enter] pan/tilt up to the guitar player                                   see absolute data

 [101] [Enter] make slight adjustment to pan/tilt on drums                        see referenced red ‘R’s

 [Update]                                                                         look at where the values are updating
                                                                                  now only 101 is updating into FP3, 102 is not
 {Ref Only}
                                                                                  being stored into the cue
 [Enter]
                                                                                  101 doesn’t move (it is in same FP, which we
 [Go To Cue] [Enter]                                                              updated), 102 moves back to where it was since
                                                                                  we never updated it

### UPDATE INTENSITY CUE ONLY

When Intensity Cue Only is enabled, regardless of the Track/Cue Only setting of
the desk, Intensity modifications will always be Cue only.
Non-intensity modifications will update based on the Track/Cue Only setting of
the desk, or the application of Track/Cue Only key prior to Enter.
Previously would have been 2 commands.

30    Eos Family Level 3 Intermediate

### UPDATE TRACE

     Trace allows changes to be tracked backwards through the track in the cue
     list to where the level was first changed and forward in the cue list until it
     sees a new move instruction. It will update into a block, but not past it.

           [Go To Cue] [36] [Enter]            Recall Snapshot 4

           [Live], [Format] in to Summary View, look at [301]                               cyc fixtures in a tracked value of 50

           [Blind], [Format] to Spreadsheet , look at [301], [Shift]&[Format]               see the move instruction in cue 34

           [Live]

           «All Cyc» (G22) [At] [/] [5] [Enter]                                             takes intensities down by half

           [Update] [Trace] [Enter]                                                         now tracked values at 25

           [Blind] – Spreadsheet, look at [301]                                             move instruction was updated in Cue 34

### TRACE TRACE

         {Trace} {Trace} will force that channel’s new value to go backward if there were
         no levels preceding the change in the cue list.
           Still in [Blind], «Side Mids» (G9), look at [141]                                notice fixtures aren’t on

           [141] [At] [Full] [Trace] [Enter]                                                only tracks forward since it was at 00

           [Undo] [Enter]

           [Live]

           «Side Mids» (G9) [Full] [Full], then «Green» (CP4)
                                                                                            forces fixture level on from previous
           [Update] [Trace] [Trace] [Enter]
                                                                                            instructions and makes change to color
                                                                                            notice it changed back to cue 32, also forward
           [Blind] Look at [141]
                                                                                            into the Block but not beyond it

### TRACE CUE ONLY

         Using [Q Only/Track] as a modifier allows changes to be tracked backwards
         through the track in the cue list to where the level was first changed and then
         creates a move instruction in the next cue to stop the track going forward. This
         is basically a backwards Trace only.

           In Blind, [141] [At] [5] [Trace] [Q Only/Track] [Enter]                          creates two move instructions

## Navigation and Editing in Blind

### NAVIGATION

Navigation in Blind works similarly to other areas of the desk. You have
access to Format, Flexi, and paging tools, as well as Data and Time Display
options. [Blind] is a hard key.
When in Blind, the screen background turns gray, the word “Blind” is in
front of the command line and in the top left corner of each display.

### VIEWING OTHER TARGETS IN BLIND

    When you enter the Blind display, you always enter in Cue Blind. Blind is also
    used to view and edit other target data.
      Recall Snapshot 1

      [Blind], [Format] to Table view                                                                defaults to the cue that is current in Live
                                                                                                     displays the data stored in color palette 2 -
      [Color Palette] [2] [Enter]
                                                                                                     able to edit this data
      Flexi to Active Channels                                                                       shows only active channels in current target

      [Color Palette] [Color Palette]                                                                opens the color palette list
                                                                                                     from a target list, Edit drops you into the blind
      [Color Palette] [5] [Enter]            {Edit}
                                                                                                     view of that target
      [Next], [Last]                                                                                 scroll through targets

      [Cue] [1] [Enter]                 [Next]……..[Last]                                             switches to looking at cue targets

      [Live]                                                                                         notice still in Cue 36

      [Displays], Setup > User > Displays                                                            to change the behavior
                                                                                                     when back to Blind, the last cue selected in
      Enable {Preserve Blind Cue}
                                                                                                     Blind is displayed. Disabled by default.
      [Live],     [Go To Cue] [36] [Enter], [Blind], [Cue] [7] [Enter]

      [Live], still in 36, [Blind] returns to Cue 7

      Go back into Setup and disable {Preserve Blind Cue}
               If this is something that you may use often, this would be a great macro.

### NON-INTENSITY PARAMETERS IN SPREADSHEET

      In [Blind], [Format] to Spreadsheet view                                                       by default, all parameters are shown

      [Shift]&[Format]                                                                               hides all non-intensity parameters

      [101] [Enter]
                                                                                                     shows all color information columns for all
      Press & Hold [Data]/[Params], [Color]
                                                                                                     channels
      Press & Hold [Data]/[Params], deselect {Color}                                                 back to seeing only intensities

      NOTE:      By default, encoders are disabled in Blind. To enable use of the encoders, press
                 any of the Encoder Page navigation buttons.

32    Eos Family Level 3 Intermediate

### EDITING DATA IN BLIND

     Data that is changed in Blind is automatically stored, without the need for a
     Record or Update command. This makes it extremely fast, but be sure to
     use caution. Undo if necessary.

### AT ENTER – PALETTES, PRESETS, AND SUBS

         [At] [Enter] behind a channel or parameter selection will remove the data that
         is stored in a target
           [Format] to Table View, [Flexi] to Active
                                                                                                        displays only the channels with data stored in
           [Clear] [Color Palette] [1] [Enter]
                                                                                                        Color Palette 1
                                                                                                        shows all color parameters are stored in this
           [101] [Thru] [128] [Enter]
                                                                                                        palette
                                                                                                        grabs all parameters except Cyan, Magenta,
           [Select Last] [-] {Cyan} {Magenta} {Yellow} [At] [Enter]                                     and Yellow, and removes the data from those
                                                                                                        parameters
                                                                                                        shows none of other color parameters affected
           Scrolling up and down
                                                                                                        except 101 - 128
                   Keep in mind the difference between no data and a zero value.

### AT ENTER – CUES

         [At] [Enter] in a cue removes the data stored, but unlike other targets, there
         are tracking implications when removing data.
           [Format] to Spreadsheet View
                                                                                                        displays all the cues in spreadsheet, with cue
           [Cue] [12] [Enter]
                                                                                                        12 selected
           [31] [Thru] [33] [At]         Look at the values                                             shows move instruction to go to Full
                                                                                                        removes the move instructions for these
                [Enter]                                                                                 channels, and allows the previous values to
                                                                                                        track forward
           [Undo] [Enter]                                                                               puts the values back
                                                                                                        removes the move instruction and adds a move
           [6] [At] [Cue Only] [Enter]
                                                                                                        instruction in the next cue
           NOTE:     [At] [Enter] in Live will give you that channel or parameter’s value from the
                     previous cue, in a manual state. Updating the cue will result in a tracked value
                     from the previous cue – the same as removing the move instruction in blind.

### RANGE EDITING IN BLIND

 You can edit over a range of cues, including overwriting cues with
 move instructions. Just like any edit, there are tracking implications
 when changing data.
   Still in Blind Spreadsheet, [Cue] [21] [Thru] [25] [Enter]                               selects a range of cues
                                                                                            puts a move instruction in the first cue, tracks
                                                                                            that value through the range, and continues the
   [3] [At] [75] [Enter], may need to scroll to see how far it tracks
                                                                                            track until the next move instruction outside of
                                                                                            the range
   [Undo] [Enter]                                                                           puts the data back
                                                                                            puts a move instruction in the first cue, tracks
                                                                                            that value through the range, but stops the
   [3] [At] [75] [Cue Only] [Enter]
                                                                                            track at the end of the range and adds a move
                                                                                            instruction in the first cue of the range

### REPLACE WITH

  You can find values across ranges of cues and replace them with new values.

     [Cue] [1] [Thru] [15] [Enter]       [1] [Enter]                                        selects the cue range and resets to channel 1
                                                                                            finds all values that are 35, and replaces them
     [1] [Thru] [10] [At] [35] {Replace With} [50] [Enter]
                                                                                            with values of 50
     NOTE:    Replace With works with palettes and presets as well. You can also command
              line filter to specific parameters for more control.

### MOVING CUES

  Just like any edit, there are tracking implications when moving cues.

     Still in Blind Spreadsheet, Flexi - Patched, look at Ch. 51 thru 82
                                                                                            look at channel 51– move instructions tracked
     [Cue] [13] [Copy To] [Copy To] [0] [.] [5] [Enter] [Enter]
                                                                                            into cues 1 and 2
     [Undo] [Enter]                                                                         puts the data back
                                                                                            look at channel 51 – a simple move
     [Cue] [13] [Copy To] [Copy To] [0] [.] [5] [Cue Only] [Enter] [Enter]
                                                                                            instruction in 0.5., another in cue 1
     [Undo] [Enter]

     NOTE:    You can move ranges of cues, with the same tracking or cue only behavior as
              moving a single cue.

### BLIND BEST PRACTICES

     - If a cue on stage is edited in Blind (either through cue changes or
         referenced data changes), the cue must be reloaded on stage. Sub edits
         in Blind are immediately changed in Live.

34    Eos Family Level 3 Intermediate

## Additional Display Functions

### FLEXI VIEW CHANNELS

     It is possible to make a custom Flexi view based on a channel selection.

       [Live],   Recall Snapshot 4

       Hold [Shift], Touch «FOH Movers» (G5) and «OS Movers» (G7)                             puts groups on command line unterminated
                                                                                              completes the command line, makes the
       Press & Hold [Flexi] {View Chans}
                                                                                              channel selection a Flexi State
                                                                                              cycle thru Flexi state and see new View
       [Flexi] [Flexi], [Flexi]…
                                                                                              Channels

     NOTE:   This will remain the View Channels state until you change the selection. To
             replace the channels in View Channels Flexi, simply do the same process again.

### PREVIEW

     {Preview} displays the intensity values for another cue under the current
     values in the Live Summary tab. Preview is not available in Table View.
     - {Previous} - previews the last cue run from the selected cue list.
     - {Pending} - previews the pending cue from the selected cue list.
     - {Preview} [Next] - previews the cue higher than the one currently
         selected (or pending if no cue selected).
     - {Preview} [Last] - previews the cue lower than the one currently
         selected (or previous if no cue selected).
     - {Preview} <Cue> [5] - will preview cue 5.
     - {Preview} [Enter] - takes you out of preview mode

       Format to Summary and Flexi All

       [Go To Cue] [2] [Enter]

       {Preview} {Pending}                                                                    previews whatever cue is pending

       [Next], [Next], [Last],                                                                to look at future cues

       {Preview} [10] [Enter]                                                                 previews cue 10

         An indicator of which Preview mode you are in is displayed in the upper left-
         hand corner of the Live Summary display.

       [10] [At] [75] [Enter]                                                                 can do other work and Preview stays

       [Clear] {Preview} [Enter]                                                              turns Preview off

### TAB DISPLAY BEHAVIOR

Display tools in Eos follow tab focus. There are two types of display tabs:
- Display tabs – various displays available on the console
- Control tabs – virtual control options

### TAB FOCUS

     Recall Snapshot 4
     Left hand screen - 2 Display tabs – Live Summary is in focus, PSD is grayed-
     out, not in focus
     Right hand screen - 2 Control tabs – both Direct Select tabs are purple
    Control tabs don’t take focus when being interacted with.
                                                                                       displays tools such as paging are tied to that
     Touch or click on the PSD tab – notice the gold frame
                                                                                       display.
     Touch or click on a Direct Select tab – notice it doesn’t pull focus
     Double hit or click on the tab name                                               to pull focus to that controls tab

     Touch or Click on the Add-a-Tab (+)                                               Displays tabs on left and Controls tabs on right

### OTHER WAYS TO PULL FOCUS

                                                                                       to change focus from open display to the
     Press [Tab] … [Tab] … [Tab]
                                                                                       next open display
                                                                                       to select/highlight a specific display by
     Hold [Tab] & press [#] of specific display,
                                                                                       number

### SHIFT LIVE

    If you have multiple Live /Blind Tabs open, you can pull focus through all the
    Live/Blind displays using [Shift]&[Live]
     Add another Live Tab
     Hold [Shift] and press [Live], [Live], [Live]…                                    toggles just Live and Blind displays,

### MAGIC SHEET DISPLAY BEHAVIOR

    Magic sheets can be either a Display tab or a Control tab. We allow you to
    make the selection.
     Hide the CIA                                                                      for better visibility

     Open the Magic Sheet display, select the one you have been working on             to open Magic Sheet 1

     Open the Magic Sheet editor

     In Settings (the Gear tab in Objects Library), select Display Behavior            Normal, Channel or Control options

        Default is Normal                                                              follows the rules of a Displays Tab
                                                                                       Magic Sheet tab is now purple, double -hit the
     Change to a Control tab and close the Editor     [Live]
                                                                                       tab name to bring focus to it
     Open the Editor, and select Channel Display and close the Editor
                                                                                       now in the rotation when using [Shift] & [Live]
     Hold [Shift] and press [Live], [Live], [Live]…
                                                                                       with other Live and Blind tabs

36    Eos Family Level 3 Intermediate

## Referenced Marks

     A Mark automates the process of presetting moving lights to their required
     state in a cue, prior to fading intensity up (Also referred to as move while
     dark/move before bright). All move info about a marked cue is stored in the
     reference or source cue.

### CREATE A REFERENCED MARK

         AutoMark always uses the cue before the light turns on to mark the fixture. Not
         a lot of flexibility. So….

          Recall Snapshot 1
                                                                                               notice lots of ‘Rs in the flags column of the
          [Displays], {Setup}, {System}, {Cue Settings}, and disable Automark
                                                                                               PSD
          [Blind] [Cue] [104] [Thru] [Thru] [110] [Enter] [Enter]                              creates cues

          [Time] [1] [Enter]                                                                   changes timing

          [Live] [Go To Cue] [110] [Enter]
          [Group] [7] [Full] [Full] [Home] [Enter]
          [Focus Palette] [11], {Zoom} [19], [Color Palette] [5] [Enter]
                                                                                               updates cue 110 , notice the L in the Moves
          [Update] [Enter]
                                                                                               column of the PSD
                                                                                               notice the red m’s - Focus, color & beam
          [Group] [7] [Mark] [106] [Enter]         [Update] [Enter]                            times moved to Q106, Q110 now has R
                                                                                               (reference), Q106 has an M (Mark)
          [Go To Cue] [105] [Enter]
                                                                                               channels take their marks in cue 106, track
          [] (Go) on 106, play cues through 110                                               through cue 107, come up in position in cue

### SEE WHERE A MARK IS HAPPENING

          Hold [About]&[Mark]                                                                  to see where a mark is happening

### CHANGE A MARK

          [Group] [7] [Mark] [104] [Enter]                                                     marks these channels in cue 104

          [Update] [Enter]                                                                     need to update the red ‘M’s

         ‘M’ indicates cue has current channels that are marking. A small ‘m’ indicates
         the cue still has a Mark flag even though nothing is marked on that cue,
         identifying it as having once been a marked cue. May want to use it again.

         To quickly mark fixtures to a predesignated mark cue, simply select the
         channels and type [Mark] [Enter]. It will find the Mark flag that is the closest up
         the list and then mark in that cue.

### REMOVE A MARK

          [Cue] [106] [Mark] [Enter]                                                           removes the m

### BROKEN MARK

 [Go To Cue] [106] [Enter],

 [Group] [7] [Full] [Full], [Focus Palette] [12] [Color Palette] [1] [Enter]                         breaks the mark
                                                                                                     channels unable to mark now in cue 104 (m)
 [Update] [Q only] [Enter]
                                                                                                     and in cue 109 notice the x
 [] (Go) on 107, [] (Go) on 108, [] (Go) on 109                                                   channels do their best to mark for cue 110

 [] (Go) on 110                                                                                     Lights come up in cue 110
                                                                                                     gets the marks back in cue 107 notice the M in
 [Group] [7] [Mark] [107] [Enter] [Update] [Enter]
                                                                                                     the PSD
 [Go To Cue] [104] [Enter]

 [] (Go) on 105, [] (Go) on 106                                                                    notice the Live moves

 [Group] [7] [Mark] [Enter] [Update] [Enter]                                                         finds the nearest mark flag

 [] (Go) on 107, [] (Go) on 108, [] (Go) on 109,
                                                                                                     watch for live and dark moves
 [] (Go) on 110

### TIMING ON MARKS

By default, Marks use the time of the cue in which they move. To change the
mark time to a different time, use a discrete time on the parameters that mark
in the reference cue (R).
  All attributes of the mark are stored in the Reference cue!

 In Cue 110, [Group 7] [-] {Intensity} [Time] [5] [Enter]                                            notice red ‘t’s, also m’s
                                                                                                     in the PSD, notice in Cue 107 the discrete time
 [Update] [Enter]
                                                                                                     + , and the duration is 6 s
 [Go To Cue] [106] [Enter],         [] (Go) into 107                                                1 sec to fade out, 5 seconds to mark

 Run the cues, watch the fades                                                                       End up in Cue 110

    Note that the intensities fade up in the cue time because we did not put a discrete timing on
            the intensity

### MARK TIME

Mark Time is a setup option which allows you to set the time that mark
instructions will use.
                                                                                                     all marks will use this time instead of their cue
 [Displays], {Setup}, {System}, {Cue Settings}, {Mark Time} [5] [Enter]
                                                                                                     time
When {Mark Time} is disabled, which is the default, mark instructions use cue
timing unless overridden with discrete timing.
When you enter a Mark Time in Setup, all NPs that mark (either through
referenced marking or Auto-Mark) use this time. The only way to override
setup mark time is to use discrete timing.

### REMOVE A MARK

 [Live]

 [121] [+] [122] [Mark] [Enter] [Update] [Enter]                                                     removes a mark on a specific channel

38    Eos Family Level 3 Intermediate

## Effects Editing

### EFFECT STATUS DISPLAY

      Recall Snapshot 4

      [Effect] [1] [Thru] [4] [+] [901], double tap a blank Custom DS

      [Shift] & [Clear]

      [Go To Cue] [Out] [Enter]

      [Group] [30] [Enter]… Touch «DS Chase» (FX1)

      From a clear command line, [Effect]                                                 to open Effect Status Display in CIA (or Tab 6)

     This display shows you any currently running effects, the channels on that
     effect, the source (man, cue or sub) as well as attributes of the effect such
     as Rate and Size, which defaults at 100..
     This display gives you the ability to edit just this instance of the effect, on a
     cue-by-cue basis.

### ENCODERS AND SOFTKEYS

         You can modify an effect by clicking on the properties displayed on the bottom
         of the display – Attributes, Duration, Entry, Exit, Grouping, Trail.
         You can also use the encoders to adjust the effects
           - Axis – Default is 0° and can be modified by +/- 180°.
           - Shape – Vertical or Horizontal as defined by the {Mode} button) –
                Default is 100%, and can be modified from 0%-2000%.
           - Size – modifies scale. Default is 100%, range from 0%-2000%.
           - Rate – modifies cycle time. Default is 100%, range of 0%-2000%.
         The softkeys also give you access to Rate, Size, Axis, and more.

         {Rate} [300], {Rate} [50]                                                        enter a rate numerically

         [Stop Effect] [Enter] or «Stop FX»

### GLOBAL CHANGE TO AN ABSOLUTE EFFECT

 [Group] [30] [Enter]… «Intens Fade» (FX4)

 [Effect] [Effect]                                                                            to see actions in effect
                                                                                              changes second action to an absolute value,
 [Live] [Select Last] [At] [25] [Enter]                                                       background value doesn’t matter Background
                                                                                              state is now 25
 [Effect] [Effect],
                                                                                              intensity values are going between 50 and 100,
 Change Action 2 from background to [50] [Enter]                                              level is an absolute value, background value
                                                                                              doesn’t matter
  Note:    Be careful about globally changing effects as the changes will populate anywhere
           the effects are used.

### EDIT A RELATIVE EFFECT

 [Live],   Touch «FOH Movers» (G5), «100%» (IP1), «Singer» (FP2)

 «Circle» (FX901)

 Pan fixtures to stage right, stage left, then back to center                                 run relative to their location on stage
                                                                                              workspace 2 icon in upper left corner of
 Go to a new Workspace,
                                                                                              monitor
 Add-a-Tab (the {+} sign), open the Effect Status Tab (6)                                     under Controls, bottom line

 [Effect] [901] [Enter] if not already selected

 [Effect] {Size} [50] [Enter]

 Use size encoder to make the effect size larger,

 [Clear]   [Update] [110] [Enter]                                                             larger circle size is stored in cue 110

 [Go To Cue] [110] [Enter]

40    Eos Family Level 3 Intermediate

### EFFECT CHANNELS DISPLAY

     In the Effect Channels Display, you can override certain effect properties per
     channel at the cue level.

        Back to Workspace 1

        «OS movers» (G7) in «Flyout» (FP13)

        [Group] [30] [Color] [Home] [Enter]

        Switch back to Workspace 2

         Changes made here are stored in the cue, won’t affect the base effect

        Add-a-Tab (the {+} sign) and open Effect Channels tab (8)

        [31] [+] [35] {Rate} [500] [Enter]

        [102] [+] [104] {Size} [50] [Enter]                                                    can also use encoders to change size

        [101] [+] [103] [+] [105] {Horiz Form} [0] [Enter]                                     sweep left and right

        [Record] [111] [Time] [2] [Enter]

        [Go To Cue] [37.2] [Enter], Back to Workspace 1

        Touch «OS Movers» (G7), «100%» (IP1),and [Home] [Enter]

        Touch «X Stage Look» (FP12), «Heart» (FX2)

        [Clear]            [Effect]                                                            opens effect Status display

        {Grouping} [4] [Enter]

        Switch back to Workspace 2 with the Effect Chan Display tab                            Workspace 2

        [121] [+] [122] {Rate} [250] [Enter]

        [125] [Thru] [128] {Size} [50] [Enter]

        [Update] [Enter]

         Note:    All the values have been recorded into the cue and will track forward till
                  they receive another move instruction

### BPM – BEATS PER MINUTE

 We can assign Beats per Minute to an effect within the base effect
 or on a cue-by-cue basis. Beats per minute (BPM) can be set up for
 step-based and absolute effects. For step-based effects, BPM
 affects the step times and for absolute effects, this affects the
 time/dwell.

     Go to Workspace 1

     [Go To Cue] [37.3] [Enter]

     Touch «All Cycs» (G22), «Abs Rainbow» (FX3)                                     runs rainbow effect on cyc channels

     [Clear]            [Effect]                                                     opens Effect Status Display

     Change Grouping to 2                                                            makes effect less granular

### DIRECTLY SETTING BPM

  Done in Blind, changes applied immediately to all instances of this effect.

    [Effect] [Effect]      [Effect] [3] should be on command line                    make sure you are in Effect 3

    Softkey {BPM} [200] [Enter]                                                      sets the BPM of the effect to 200

  Notice BPM is posted in the Effect Editor to the far right of the Effect number.
  Also notice changes to Step times and Cycle times.

    {Cycle Time} [7] [Enter]                                                         removes the BPM

### LEARNING BPM

  Done in Live, changes will need to be recorded.
    [Live]                                                                           jump back into Live

    [Effect] [3] [Learn] [Time]                                                      opens the Effect Status Displays

    Notice “Effect 3 Learn Time Sample BPM” on the command line.

                                                                                     averages the timing or tap rate of the last
    [Enter] [Enter] [Enter]
                                                                                     three hits of Enter
    [Learn]                                                                          stops the Learn mode or averaging

    Notice the red BPM to the far right of the Effect number.

                                                                                     updates effect in cue with the modified BPM
    [Update] [Enter]
                                                                                     (3* in effects column on PSD)

42    Eos Family Level 3 Intermediate

## Intermediate Magic Sheets

### OPEN THE MAGIC SHEET TAB

       Recall Snapshot 1

       Use Add-a-Tab (the {+} sign) and select the magic wand (Tab 3)

       Select Magic Sheet 1 that we build previously

     OR
       [Displays] {Magic Sheet} [1] [Enter]                                  opens Magic Sheet 1

     After Level 2, the Magic Sheet should look something like this:

### ADDITIONAL OBJECTS

      Open the Magic Sheet Editor

      Use your mouse wheel                                                    to zoom out a bit

      Drop in a fader on the right.

      Assign it to 1/3 (Frontlight Inhib) page #/fader #

      In Style: look at both Modern or Classic and view options to display

      Select Classic

      Change Fill Color to red                                                to mimic an inhibitive submaster
                                                                              follow main user or any other user, have
      Add CL - command line in top left, stretch across top of screen
                                                                              command line in full screen mode

We can assign objects to show the current state of various cue lists.

 Drop in 2 squares to the left of the command line object.

 Resize them to be a little bigger.

 Assign the left one to Cue – Active, the right one to Cue – Pending

Note:    The target for these objects refers to which cue list it will reference. This is a
         great way to keep an eye on a specific cue list that isn’t loaded to your master
         fader pair.

 Add clock in top right                                                                       helpful in full screen mode

 Move the Group objects to the left a bit                                                     include gobo and arrow images as well

 Select the Quick Layout tool                                                                 notice the + on the cursor

 Select a fixture, Source 4, drop in 4 fixtures and hit Done.                                 prevents you from adding more

 Don’t forget to go back to normal cursor!

 Select the third fixture down, in the properties, check the scroller box                     adds scroller to fixtures, shows color

 Select all fixtures, change target to groups, rotate them horizontally

 Use Alignment tools – align them center and distribute vertically                            remember to look at the gold arrows!

 Grab just the bottom fixture, drag it up a bit, then select all four, and distribute
                                                                                              realigns between two farthest objects
 vertically again
 Select all 4 fixtures, change field 1 to Label, nothing in fields 2 and 3
 Using Quick Number tool, assign to groups 8, 9, 10, 12.
 Click on bottom fixture twice to “skip” 11. Don’t forget to hit Done!

 Add stick of truss, rotate it, stretch a bit, and place on fixtures

 Turn line color to white, fill color to none (transparent)                                   can see things through it

 Ordering Tools: Send truss to bottom                                                         fixtures are visually on top of the truss

 Drop in a stop sign (octagon) object, stretch it, make it red

 Assign it be Macro 1, first field is Label,                                                  the Stop Effect macro

 Drop in a rectangle, stretch it. Color it orange,

 Assign to Effect 901, change field 1 to Label                                                the circle effect

 Right click on the object to see options, select Copy (Ctrl+C)

 Click off the object, right click, select Paste Renumber (Ctrl+Shift+V)

 Change target to 4, color to lavender.

 Add an Intensity Palette (IP1), make field 1 Label, field 2 & 3 nothing

44    Eos Family Level 3 Intermediate

### COMMAND OBJECTS

     The Command Object allows you to type a function and trigger it directly
     from the Magic Sheet.

      Add a triangle object, make it bigger

      Make the target a command

      Click in the Command box, type      clear sneak enter                                  No need to hit Enter

      Oh, and make it green

         A text field can also be added to many objects. This field is tied to the object,
         as opposed to being tied to the content of an object. Perhaps on the triangle,
         add some text that reminds the user what the triangle does.

      Click in the text box and type “CSE”                                                   CSE = Clear Sneak Enter

      Let’s make the font dark green and make the size 30

      Position it at the bottom of the triangle object

      Go ahead and close the Editor and play with the Magic Sheet

### MAGIC SHEET VIEWS

### DISPLAY TOOLS

   Right click or tap on the Magic Sheet tab                                          to see configuration settings

  Another option is to click on the Gear tab for the same options.
      - < Add View > – for each magic sheet, multiple views may be created,
          then < and > allow for scrolling through the views.
    -
   Press or click on Add View                                                        records Magic Sheet 1 View 1

   Zoom in and adjust so just Groups are visible                                      zooms in to show only selected item

   [Record] {Displays} {Magic Sheet} [1] [/] [2] [Enter]                              records Magic Sheet 1 View 2

   Now use the < > to go back and forth between views

### BUILD A SECOND MAGIC SHEET TO “CHANGE PAGES”

    Open config – MS browser, add a new magic sheet
    Already in Editor
    Drop in a few objects                                                             nothing specific

    Use browser to go between
       or, on the command line, {Magic Sheet} [1] [Enter]
    Open the Editor
    Select the arrow object, make its target Magic Sheet 2
    Clear the fields
    Close the editor and hit the arrow – MS 2
    Open Editor, select an object, make it Magic Sheet 1 View 1

  Don’t forget Magic Sheet List to see all magic sheets and views
  If you call a Magic Sheet without a view, it will zoom to all and takes the Magic
  Sheet and fills the space that you have.

46    Eos Family Level 3 Intermediate

### POPUP MAGIC SHEET

     The Popup gives you a temporary magic sheet window. The window that
     pops up is 800 x 450 pixels

      Touch or click on the Magic Sheet Popup (wand) on the top of the screen               see the Magic Sheet browser

      Magic Sheet browser, open a new Magic sheet

      Open the Editor

      Drop in a square – target =none, make the fill be nothing

      At the very bottom of properties, make the size w: 800, h: 450                        gives a border to constrain the MS

      Drop in a square – make it Macro 4, change field 1 to label

      Close the editor                                                                      shows macro is called RFR enable

      Open the Editor again, make it green                                                  as it enables

      Control C, Control V to copy the object, make it Macro 5, make it red                 this one disables

      Also drop in a fader, make it fit in the border, make it the Fader 1/3, make it red   same fader as in the other Magic Sheet

      Touch or click on the Magic Sheet Popup (camera) on the top of the screen

      Touch or click on Magic Sheet 3, the Utilities that we just created

        Anywhere you go, always have access to that Popup Magic Sheet

         The first time you open the Magic Sheet Popup, it gives you the Magic Sheet
         browser, and you can select whichever Magic Sheet you want to be your
         popup.

### TO CHANGE THE POPUP TARGET

          [Displays], {Setup}, {User}, {Displays}, {Popup MS}                               currently set as Magic Sheet 3 from the last

          {Popup Nav Lock}                                                                  locks navigation of your Magic Sheet

          [Live]

### USE A MAGIC SHEET TO WRITE CUES

 Collapse the CIA, and open a new tab, Magic Sheet #1

 [Go To Cue] [Shift]&[Home] [Enter]                                              to go to the last cue in the show file (111)

 Hit Stop Effect object on the magic sheet                                     to stop the current effects running

 Grab Side - Mids boom fixtures, then Full Rem Dim Enter                 turn select channels on and rest off

 Put them in Magenta                                                           change color of selected channels

 Grab Scroller fixtures, 100%, use color encoder to select Frame 6           turn scrollers on and put in color

 [Group] [22] [Full] [Enter] and put them in Orange                            turn cyc on and put in color

 Grab 105 and 104, left two FOH Movers, 100%, Guitar                     focus channels on guitar player

 Grab 102 and 101, right two FOH Movers, 100%, Drums                     focus channels on drum player

 Grab 105 104 102 101, and put them in Lt. Blue                        change all four to a new color

 [Record] [Next] [Time] [3] [Enter]                                              records next cue (112)

 [Group] [22] [Enter] and put them in Dk. Blue                                 change color of cyc lights

 Grab Overstage Movers [Focus Palette] [13] [Enter]                            effect is still running but new position

 Intensity Fade                                                                adds intensity fade effect to same fixtures

 Grab Side Mids boom fixtures, [Out]

 [Record] [113] [Time] [3] [Enter]                                               records next cue (113)

 Grab Overstage Movers (G7) [Out] [Enter] and Stop Effect                    turn channels off and stops effect

 Grab 105 104 102 101, {Beam} [Home] [Enter], Singer                   removes beam attributes, refocuses

 [Record] [Next] [Time] [2] [Enter]                                              records next cue (114)

Depending on the style and experience of the programmer, Magic Sheets
can be a great way to expediate their programming process.

48    Eos Family Level 3 Intermediate

### COMMAND LINE SEARCH

     Having troubles finding the correct target number? Here’s a quick way to
     search target labels.

      Grab 105 104 102 101                                                  select the channels

      [Focus Palette]                                                               type in the target type

      [Shift]&[About]                                                               opens a search bar in the CIA

      Start typing `crate’,                                                         field narrows down by letter
                                                                                    puts target on the command line,
      then [Enter],
                                                                                    unterminated, so can continue to program
      [Enter]                                                                       to terminate command line

      Yellow

      [Record] [115] [Enter]                                                        (115)

                                                                                    shows all groups that contain `side’ in the
      [Group] [Shift]&[About] type `side’
                                                                                    label
      Double click on menu option: `Group 10: Side Scrollers’, [Out]

      [Group] [22] [Color Palette] [Shift]&[About], type `split’, [Enter] [Enter]   changes cyc to split color palette

      [At] [50] [Enter]                                                             Intensity at 50 %

      [Record] [Next] [Enter]                                                       (116)

     [Shift]&[About] will work with any record target, including groups,
     pallettes, presets and cues.

### PSD FLAGS

Flags can be applied to cues to change specific behaviors. Flags can be set for “Mark -
M”, “Block - B”, “Assert - A”, “Preheat - P”, “AllFade - AF” and “Moves - MV.”

  M - Mark (Auto Mark Disabled)

     m        A cue that has been set as a Mark cue but has nothing marking in it.

     M        A cue that has been set as a Mark cue and has channels marking in it.
              A Reference cue, which stores move instructions for channels that are being marked in a
     R
              previous Mark cue.
     +        A cue that is both a Mark cue (with or without marking channels) AND a Reference cue.

              A broken Mark. Always appears in the cue directly before a Reference. A Mark gets
              broken when the channels become Active between their Mark cue and their Reference
     x
              cue. When a Mark is broken, the software will use Auto Mark behavior to try to get the
              parameters marked in the cue immediately preceding the Reference cue.

  M - Mark (Auto Mark Enabled)

              A cue that the software is using for an Auto Mark and has channels marking in it. The 'M'
     M        always appears in the cue directly before the Reference (which is not indicated when
              Auto Mark is enabled).

     D        A cue where Auto Marks have been disabled, allowing live moves.
  B - Block
```text
     B        Cue-Level Block
     b        Discrete channel/parameter Blocks are present
     b        Auto-Blocks are present
     I        Intensity Block
```
  A - Assert
```text
     A        Cue-Level Assert
     a        Discrete channel/parameter Asserts are present
```
  P - Preheat
              A cue that is set for Preheating. The cue before it will use each channel's preheat value
     P
              from patch.
  AF - All Fade
              Plays the cue in an All Fade mode, which sends any intensities that are not owned by the
     *
              cue to zero.
  MV - Moves
         A cue with Dark Moves. There are channels that have an intensity of zero and non-
    D    intensity moves stored in this cue. This is where you might want to delete unnecessary
         moves.
              A cue with Live Moves. There are channels that have an intensity of zero stored in the
     L        previous cue, and an intensity above zero and non-intensity moves stored in this cue.
              This is where you might want to Mark channels to a previous cue.

     +        A cue where both Dark Moves and Live Moves are present.
  R - Release
           Like Make Null, but releases data to a background state or out. Tracks through until
      R
           removed or a move instruction happens.

## Appendix 1 – Channel Hookup

     Grayed out channels should have been patch in Level 1 & 2
```text
      Chan       Univ / Address        Manufacturer              Fixture                Mode                 Label
      1          1       1             Generic                   Dimmer                 Dimmer [1]           Frontlight - A
      2          1       2             Generic                   Dimmer                 Dimmer [1]           Frontlight - B
      3          1       3             Generic                   Dimmer                 Dimmer [1]           Frontlight - C
      4          1       4             Generic                   Dimmer                 Dimmer [1]           Frontlight - D
      5          1       5             Generic                   Dimmer                 Dimmer [1]           Frontlight - E
      6          1       33            Generic                   Dimmer                 Dimmer [1]           Frontlight - A
      7          1       31            Generic                   Dimmer                 Dimmer [1]           Frontlight - B
      8          1       32            Generic                   Dimmer                 Dimmer [1]           Frontlight - C
      9          1       35            Generic                   Dimmer                 Dimmer [1]           Frontlight - D
      10         1       34            Generic                   Dimmer                 Dimmer [1]           Frontlight - E

      31         1       301           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - A
      32         1       310           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - B
      33         1       319           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - C
      34         1       328           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - D
      35         1       337           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - E
      36         1       346           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - F
      37         1       355           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - G
      38         1       364           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - H
      39         1       373           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - I (eye)
      40         1       382           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - J
      41         1       391           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - K
      42         1       400           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - L (ell)
      43         1       409           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - M
      44         1       418           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - N
      45         1       427           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - O (oh)
      46         1       436           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - P
      47         1       445           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - Q
      48         1       454           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight – R
      49         1       463           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight – S
      50         1       472           ETC Fixtures              D60 Lustr+ +3D         Direct Str [9] +3D   Downlight - T

      51         2       1             ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 1  Left
      52         2       7             ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 1  Mid
      53         2       13            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 1  Right
      54         2       19            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 2  Left
      55         2       25            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 2  Mid
      56         2       31            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 2  Right
      57         2       37            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 3  Left
      58         2       43            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 3  Mid
      59         2       49            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 3  Right
      60         2       55            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 4  Left
      61         2       61            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 4  Mid
      62         2       67            ETC Fixtures              ColorSource SPOT +3D   Direct [6] +3D       Hi Side Tx - Ln 4  Right
```
     + End of range +

```text
 Chan       Univ / Address     Manufacturer       Fixture                  Mode                  Label
 71         2      73          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 1  Right
 72         2      79          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 1  Mid
 73         2      85          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 1  Left
 74         2      91          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 2  Right
 75         2      97          ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 2  Mid
 76         2      103         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 2  Left
 77         2      109         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 3  Right
 78         2      115         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 3  Mid
 79         2      121         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 3  Left
 80         2      127         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 4  Right
 81         2      133         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 4  Mid
 82         2      139         ETC Fixtures       ColorSource SPOT +3D     Direct [6] +3D        Hi Side Tx - Ln 4  Left

 101        2      201*        High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D     FOH Mover - Spot
 102        2      251         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D     FOH Mover - Spot
 103        2      301         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D     FOH Mover - Spot
 104        2      351         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D     FOH Mover - Spot
 105        2      401         High End Systems   SolaFrame Theatre +3D    …Pan 540 [47] +3D     FOH Mover - Spot
```
                   * Think Offset!
```text
 111        3      1           High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover - Spot
 112        3      48          High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover – Spot
 113        3      95          High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover – Spot
 114        3      142         High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover – Spot
 115        3      189         High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover – Spot
 116        3      236         High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover – Spot
 117        3      283         High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover – Spot
 118        3      330         High End Systems   SolaFrame 750 +3D        …Pan 630 [47] +3D -   Overstage Mover - Spot

 121        4      1           High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D -   Overstage Mover - Wash
 122        4      37          High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash
 123        4      73          High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash
 124        4      109         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash
 125        4      145         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash
 126        4      181         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash
 127        4      217         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash
 128        4      253         High End Systems   SolaWash 2000 {36] +3D   …Pan 630 [36] +3D     Overstage Mover - Wash

 131        5      1           ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 132        5      10          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 133        5      19          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 134        5      28          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 135        5      37          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 136        5      46          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 137        5      55          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
 138        5      64          ETC Fixtures       S4 LED S2 Lustr +3D      Direct Str [9] +3D    Side - High
```
+ End of range +

```text
      Chan        Univ / Address      Manufacturer       Fixture               Mode                  Label
      141         5     73            ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      142         5     82            ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      143         5     91            ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      144         5     100           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      145         5     109           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      146         5     118           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      147         5     127           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid
      148         5     136           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Mid

      151         1     281           Generic            Dimmer                Dimmer [1]            Side - Scroller
      151 P2      1     291           Generic            Scroller [1]          --                    Side - Scroller
      152         1     282           Generic            Dimmer                Dimmer [1]            Side - Scroller
      152 P2      1     292           Generic            Scroller [1]          --                    Side - Scroller
      153         1     283           Generic            Dimmer                Dimmer [1]            Side - Scroller
      153 P2      1     293           Generic            Scroller [1]          --                    Side - Scroller
      154         1     284           Generic            Dimmer                Dimmer [1]            Side - Scroller
      154 P2      1     294           Generic            Scroller [1]          --                    Side - Scroller
      155         1     285           Generic            Dimmer                Dimmer [1]            Side - Scroller
      155 P2      1     295           Generic            Scroller [1]          --                    Side - Scroller
      156         1     286           Generic            Dimmer                Dimmer [1]            Side - Scroller
      156 P2      1     296           Generic            Scroller [1]          --                    Side - Scroller
      157         1     287           Generic            Dimmer                Dimmer [1]            Side - Scroller
      157 P2      1     297           Generic            Scroller [1]          --                    Side - Scroller
      158         1     288           Generic            Dimmer                Dimmer [1]            Side - Scroller
      158 P2      1     298           Generic            Scroller [1]          --                    Side - Scroller

      161         5     301*          High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      162         5     351           High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      163         5     401           High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      164         5     451           High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      165         6     1*            High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      166         6     51            High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      167         6     101           High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
      168         6     151           High End Systems   SolaFrame 750 +3D     …Pan 630 [47] +3D -   Side Mover - Spot
                        * Think offset!     Note Universe Wrapping
      171         5     163           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      172         5     172           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      173         5     181           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      174         5     190           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      175         5     199           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      176         5     208           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      177         5     217           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
      178         5     226           ETC Fixtures       S4 LED S2 Lustr +3D   Direct Str [9] +3D    Side - Shin
```
     + End of range +

```text
 Chan        Univ / Address   Manufacturer   Fixture               Mode                 Label
 181         3     381        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Front Wash
 182         3     390        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Front Wash
 183         3     399        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Front Wash
 184         3     408        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Front Wash
 185         3     417        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Front Wash

 201         1     191        Generic        Foot Light [1]        --                   Talent Uplight
 202         1     192        Generic        Foot Light [1]        --                   Talent Uplight
 203         1     193        Generic        Foot Light [1]        --                   Talent Uplight
 204         1     194        Generic        Foot Light [1]        --                   Talent Uplight
 205         1     195        Generic        Foot Light [1]        --                   Talent Uplight
 206         1     196        Generic        Foot Light [1]        --                   Talent Uplight
 207         1     197        Generic        Foot Light [1]        --                   Talent Uplight
 208         1     198        Generic        Foot Light [1]        --                   Talent Uplight
 209         1     199        Generic        Foot Light [1]        --                   Talent Uplight

 251         3     431        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Architectural Highlight
 252         3     440        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Architectural Highlight
 253         3     449        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Architectural Highlight
 254         3     458        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Architectural Highlight
 255         3     467        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Architectural Highlight
 256         3     476        ETC Fixtures   S4 LED S2 Lustr +3D   Direct Str [9] +3D   Architectural Highlight

 261         4     351        Generic        LED IRGBA             8B [5]               Scenic Highlight
 262         4     356        Generic        LED IRGBA             8B [5]               Scenic Highlight
 263         4     361        Generic        LED IRGBA             8B [5]               Scenic Highlight
 264         4     366        Generic        LED IRGBA             8B [5]               Scenic Highlight
 265         4     371        Generic        LED IRGBA             8B [5]               Scenic Highlight
 266         4     376        Generic        LED IRGBA             8B [5]               Scenic Highlight
 267         4     381        Generic        LED IRGBA             8B [5]               Scenic Highlight
 268         4     386        Generic        LED IRGBA             8B [5]               Scenic Highlight
 269         4     391        Generic        LED IRGBA             8B [5]               Scenic Highlight
 270         4     396        Generic        LED IRGBA             8B [5]               Scenic Highlight
 271         4     401        Generic        LED IRGBA             8B [5]               Scenic Highlight
 272         4     406        Generic        LED IRGBA             8B [5]               Scenic Highlight
```
+ End of range +

### MULTICELL PATCH

       Done on page 6 of this workbook
```text
     Chan    Univ / Add        Manufacturer   Fixture             Mode                            Label
     291     4     411         SGM            SP 6                6 ch MC [6] [6 cells]
     292     4     417         SGM            SP 6                6 ch MC [6] [6 cells]
     293     4     423         SGM            SP 6                6 ch MC [6] [6 cells]
     294     4     429         SGM            SP 6                6 ch MC [6] [6 cells]
     295     4     435         SGM            SP 6                6 ch MC [6] [6 cells]

     301     8     1           Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     302     8     25          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     303     8     49          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     304     8     73          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     305     8     97          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     306     8     121         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     307     8     145         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     308     8     169         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     309     8     193         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     310     8     217         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     311     8     241         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top
     312     8     265         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Top

     351     9     1           Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     352     9     25          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     353     9     49          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     354     9     73          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     355     9     97          Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     356     9     121         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     357     9     145         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     358     9     169         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     359     9     193         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     360     9     217         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     361     9     241         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
     362     9     265         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 cells]   Cyc Bottom
```

### HELPFUL SUPPORT AND TRAINING LINKS

```text
         ETC Support Website                         ETC Technical Support                     Community – ETC Consoles
All the support and training resources you   Contact our 24/7 technical support team to      Hop on the ETC forums to ask the
      might need in one handy place              help troubleshoot your ETC gear           user community your questions about
```
                                                                                                            Eos
```text
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

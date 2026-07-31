# Busking with the Eos Family of Consoles — Workbook (v3.0.1)

- Source : PDF officiel ETC, « Busking with the Eos Family of Consoles — Workbook (v3.0.1) », V3.0.1, publié 2021-04
- Fichier source : [`source/Eos_Family_Busking_v3.0_Wkbk.pdf`](source/Eos_Family_Busking_v3.0_Wkbk.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select


Busking with the Eos Family of Consoles

                                Workbook
                                            V3.0.1

                    www.etcconnect.com/education

                                    Released: 2021-04

                                                                                                                                                Table of Contents:                3

Table of Contents:

      ETC permits the reproduction of materials in this manual only for non-commercial purposes. All other
           rights are reserved by ETC.

4   Eos Family Busking

## Purpose of the Class

    Of course, you can busk on the Eos platform. Don’t know how? The
    purpose of this class is to learn the basics of what you might need to
    program a live show with little prep time. Learn from a master the tricks
    and tips for approaching non-linear playback by deploying magic sheets,
    fader configuration options like priority and background priority, fader
    control options, effects masters, timing masters and more. This session
    will help you learn how to setup a system and what content you need at
    your fingertips to be ready for anything.
    Target Audience: You should be very familiar with Eos Family consoles.
    You must know how to quickly navigate the system, create snapshots,
    groups, palettes, and cues. You should understand Direct Selects and
    Fader properties. Part of the class is building content very quickly. This is
    not an entry-level training course!

### LEARNING OBJECTIVES:

        After completing the class, one should be able to:
        - Quickly analyze the rig and current show file to know what you have
            to work with
        - Create building blocks including a base look
        - Use Playlists effectively when programming Live
        - Layout the faders for quick access to content
        - Configure the faders with timing and effect attributes
        - What to do when things go wrong.

### WORKBOOK SYNTAX ANNOTATION

        - Bold                     Syntax and Browser menus
        - [Brackets]               Face panel buttons
        - {Braces}                 Softkeys or buttons on touchscreen
        - <Angle brackets>         Optional keys or command line text
        - [Next] & [Last]          Keys to be pressed & held simultaneously
        - «Direct Select»          Direct Select button press
        - MS Object              Object on a Magic Sheet

### ABBREVIATIONS

        Throughout the book, short cuts or abbreviations are used::
        - G                Group
        - CP      Color Palette
        - FP      Focus Palette
        - BP      Beam Palette
        - MS      Magic Sheet
        - DS      Direct Select
        - NPs     Non-Intensity Parameters

## Visiting a Venue

### BUSKING DEFINITION

Creating lighting looks, most of the time, on the fly…lighting improvised

### GETTING FAMILIAR WITH THE RIG AND FILE

Open the file: Eos Family Busking Rev B 2020-06-01.esf2
Take 15 minutes to learn the venue rig, the file, and add any tricks you
may want.
Using the Magic Sheet, review the systems
- Bring the FOH Movers to Full, Pan & Tilt, orientation?
- OH Spots to Full, Pan & Tilt, orientation?
- LED Tab – check groups
- Cyc Tab – check groups – notice the Pixel Map option
- Effects Tab
- Rig Tab – become familiar with the rig
What should they be looking for?
- Macros
- Palettes
- Presets
- Effects
- Magic Sheets
What is worth adding if there is time?
- Single Shot effects
- Groups
- Playlists
- Base Cues
- Timing
- Faders
What are things you don’t want to change?
- Patch
- Invert pan/tilt…
What is destructive and why you don’t want to hurt the person who will
be back tomorrow….
- Moving / Overwriting
- Save-As a new show

6   Eos Family Busking

## Burn In

### READY? GO!

    Song for the morning: “We Shot the Moon” – Love and Fear.
    Let’s jump right in and busk a piece of music.
    The song will be played 3 times back to back.
    The job is to set up and then busk this song after 15 minutes.
    The 15 minutes starts when the song starts.
    Start a timer. Go!

### AFTERMATH

    Let’s play the song one more time.
    Go ahead and busk it again.
    Let’s discuss what happened.
    - What went wrong and what went right?
        _____________________________________________________
        _____________________________________________________
        _____________________________________________________
    - How did that feel?
        _____________________________________________________
        _____________________________________________________
        _____________________________________________________
    - What were you trying to achieve?
        _____________________________________________________
        _____________________________________________________
        _____________________________________________________
    - Why did you go about it that way?
        _____________________________________________________
        _____________________________________________________
        _____________________________________________________
    - What went well? What went horribly wrong?
        _____________________________________________________
        _____________________________________________________
        _____________________________________________________

## Build a Base Cue

### DEFINE LAYOUT AND BASE LOOKS AND PILE-ONS

Layout _______________________________________________________
    _____________________________________________________
Base look ____________________________________________________
    _____________________________________________________
Pile-on _______________________________________________________
    _____________________________________________________
Why build a base cue?
- Always somewhere to go back to.
- Built in transitions.
- Multiple base cues for different colors, different feels or moods

### START BIG. GET LIGHT ON THE STAGE

### USING THE CYC MAGIC SHEET (MS)

      Cyc All (G307) [At] [30] [Enter]

```text
      Cells Mirror Out (G316) , [Shift]&Lavendar (CP 9035), release the      [Shift]& a MS object leaves an open-ended
      shift and tap Red (CP 9021)                                              command line
```

      Cyc Pixels (G321) Azure (CP 9031)

      [Select Last] [At] [30] [Enter]

### USING THE MOVERS MS

      OH Wash (G104) X DS FP (FP111) Azure (CP 9031)

      [Select Last] [At] [05] [Enter] Middle Zoom (BP 9043)

      [Select Manual] [Record] [Cue] [100] [/] [1] [Label] Base Purple [Enter]

      [Cue] [100] [/] [1] [Master]                                               load on the Main Fader Pair/Main Playback

      [] (Go)                                                                   to establish the look on stage

      OH Wash (G104) [Out]

      OH Spot (G103) [At] [At]

### FP USCX (FP112)

      Zoom Medium (BP9043)

      E-100 (BP9026)

      Blocky Gobo (BP9221.4)

8   Eos Family Busking

           Go back to the Cyc Page

           Cyc Top (G301) [At] [10] [Enter]

           Make them Gold (CP9024)

           Cyc Bottom (G304) [At] [10] [Enter]

           Make them Blue (CP9033)

           [Record] [Next] [Label] Base Blue/Gold [Enter]

       Why multiples?
       - Why not?
       - You can use for each song or use them all in one song?!
       Where do you populate it?
       - Main Playback. Why?
       - Easy double timing.
       - Shift Go and Back & Recorded time.

## Cue List Window

### OPEN THE CUE LIST INDEX

 [Cue] [Cue]                                                                      Should be looking at Cue List 100

### GO FROM LAST/ BACK FROM FIRST - WRAP? MAYBE? YES!

  While busking you don’t want to have to worry about which direction you
  are going. You want to make sure a change happens when you want it to
  happen.

   Set {Back From First} and {Go From Last} to {Wrap}

### PRIORITIES

  The software allows control of the same channels with different targets.
  Priority is used to protect values from being affected by other targets that
  have a lower priority level. They will, however, still be impacted by manual
  control, grandmaster, blackout, park instructions, or other playback faders
  and submasters at the same or higher priority.
  There are 10 levels of Priority: 1 is lowest, 10 is highest, default is 4.
  A base cue would be a good example of a higher priority, something that
  you can come back to when you need to. Whereas a strobe effect would be
  an example of a lower priority.

### FOREGROUND VS BACKGROUND.

      − Low Foreground so overrides will work.
      − High background so if overrides are dumped, control is released
        to the Cue

   Set Priority to P3.

   Set Bkgrd Priority to P8.

  As a general rule never do the lowest or highest priority so that you have
  one extra step in case you need to add something later that is higher or
  lower without having to redo all of the priorities. Good practice is to leave
  two places on either end for flexibility.
  Might be a good time to check the back timing in settings and adjust that if
  you feel it is necessary.

10   Eos Family Busking

## Presets

### RECORD A BAND FRONT LIGHT PRESET

     You will probably use it later.
     At this point, the band will feel like they can be seen so now you have
     some leeway to build if they are doing a soundcheck.
     Start by seeing if the Focus Palettes that exist work for you or if they get
     you close. Time saving effort!

           FOH Spots (G102) 25% (IP2)                                                            Nice not to blind the band you just met at
                                                                                                     beginning of the gig. Save that till later :)
           [101] Drums (FP119)

           [103] Singer (FP118)

           [105] Guitar (FP117)                                                                    Adjust as needed but do not update the
                                                                                                     existing FPs that are in the file.
                                                                                                     Breaks the reference in case you didn't
           [101] [+] [103] [+] [105] {Focus} {Make Absolute}                                         change one of the palettes. We don't want
                                                                                                     to store the reference.
             The band will never be where they planned, if they planned anything before walking in
             the venue.

           [102] Backup Singer Lower Platform – New Focus

           [104] Backup Singer Upper Platform – New Focus

           FOH Spots (G102) [Record] [FP] [120] [Label] Band Start

           FOH Spots (G102) Edge E-40 (BP9023)                                                   Soften the edge

           FOH Spots (G102) 6500 (CP9010)                                                        Make it white

           FOH Spots (G102) [-] {Intensity} [Record Only] [Preset] [301] [Label]
           Band Base Front

           [101] [+] [103] [+] [105] [At] [60] [Enter]
                                                                                                     Band has specified that the Backup Singers
```text
           [102] [+] [104] can stay lower                                                            be lit but fall off into the background.
           FOH Spots (G102) [Record Only] [Sub] [301] [Label] Band Fronts                          For now, store this in a sub
```

           [Sub] [301] [Enter] {Properties}

           Set it to an LTP intensity master with a Bkgrd Priority of 5

           Load sub 301 on first fader on the lower bank of the faders

           [Select Last] [Sneak] [Enter]

           Mark the Sub and bring it up.                                                             Leave it up!

## Focus Palette Playlist

Why use playlists?
- Quick.
- Flexible with filters.

    Be Sitting in Cue 100/2

Let’s look at the Focus Palettes that exist for the OH Washes.

        OH Washes (G104) [Full] [Full]

        Tap through the FP’s on the magic sheet

        Let’s build a FP List using «DS Weave (FP113)» to «Flyout (FP114)»

        Press the Load button for the 6th fader in the bottom right bank of
                                                                                      The command line should say Fader 2/6
        faders (or the top and bottom bump buttons).

        Hold Shift and tap the «DS Weave (FP113)» on the magic sheet and
        then tap the «DS Flyout (FP114)». Then [Enter]

        [Fader] [2] [/] [6] [Label] OHWash FOC [Enter]

        [Sneak] [Enter] and press the bottom bump button for that fader

     What Happens? All the fixtures recorded in that palette are fired. That is not
     what is wanted. To control specific channels, apply a channel filter.

        Go to the Fader Config Tab (Tab 36)

        For Fader 2/6, change to LTP, and wrap Go from Last

        Select Chan Filter and type [121] [Thru] [128] [Enter]

     You can also put groups in here. The benefit of groups is that if you add a
     channel to that group you won’t have to adjust the filter, the console will do
     it for you.

        Back to [Live]

        Press the bottom bump for that fader and see how just the OH
                                                                                      But wait! Can’t see them!
        Washes move.

        OH Washes (G104) [Full] [Full]

     There are a few ways to deal with intensity. You can add them to the cue
     and build an Inhibitive Sub or you can put the intensities in a Proportional
     Sub.

        [Select Last] {Intensity} [Record] [Sub] [351] [Label] OH Wash INT
        [Enter]

        Load that in the 6th fader on the top row – right above the FP
        Playlist just built.

12   Eos Family Busking

     Let’s build another using a few different systems

      Grab the Side Spots (G105), bring to Full and tilt them as far up as they
      will go

      [Select Last] [Record] [FP] [151] [Label] Sides Up

      Click Side Spot >(G110) [Fan] and tilt them so that the upstage spot is
      horizontal

      Click Side Spot <(G115) [Fan] and tilt so it matches the other side.

      Side Spots (G105) [Record] [FP] [152] [Label] Sides Pyramid

      Select Side Spots (G105) and tilt them all down so that the most
                                                                                    Centered around the singer…
      downstage pair is flanking the Singer

      [Select Last] [Record] [FP] [153] [Label] Sides Down

     Let’s build another FP List for these channels.

      Clear the command line

      Press the two buttons on the fader next to the last FP List made.             The command line should say Fader 2/7

      [Focus Palette] [151] [Thru] [153] [Enter]

      [Fader] [2] [/] [7] [Label] SS FOC [Enter]

      Go into Fader Config and change it to Wrap

      [Select Last] [Sneak] [Enter]

      Run the Fader up and hit the bottom bump button                               Hey, nothing happens!

         Now time to record the Intensity control sub

          Side Spots (G105) [Full] [Full]

          [Select Last] {Intensity} [Record] [Sub] [352] [Label] Side Spots INT

          Load above the FP List fader next to the other INT Fader

          Both FP Lists should be Priority P6/P3 LTP; make sure FX Off 0 is
          unchecked

## Color Playlists

It is easy to build a playlist for some color transitions. Keep it simple for
each song. There is no need to go farther than three colors.

 Make sure to release the FP playlists – top bump button on each fader

```text
 Press the buttons corresponding to Fader 1/8, tap Azure (CP9031) ,                   Drops color palettes on Fader 1/8 on the
 Open (CP9001) , Gold (CP9024) , then press [Enter]                                 command line

 Fader 1/8 [Label] OHS COL                                                              Spots
```

 Bring the fader up and press the bottom bump button
Is that what is wanted or is a step missing?
A Channel filter IS NEEDED!

 Go to the Fader Config. Tab (Tab 36)
It would be nice to have the same palette list but individually on each
system that is used. Let copy this fader and then filter all three of them.

 Set the priorities of Fader 1/8 to P6/ P3 and Wrap and LTP

 {Fader} [1] [/] [8] [Copy To] [1] [/] [9] [Enter]

 {Fader} [Copy To] [1] [/] [10] [Enter]                                                 Now have 3 similar faders

 Now filter fader 1/8 to the OH Spots (G103)                                            Use the command line

 Filter 1/9 to OH Wash (G104)

 Filter 1/10 to Side Spots (G105)

 Fader 1/9 [Label] OHW COL                                                              Wash

 Fader 1/10 [Label] SS COL                                                              Side Spots

 {Fader} [1] [/] [8] [Thru] [10] [Copy To] [Copy To]* [2] [/] [3] [Enter]               to move the three faders just created to the
                                                                                        bottom row of faders
    Remember [Copy To] [Copy To] posts Move To on the command line.

Let’s create one more Color List for the Backwall Pixels.

 {Fader} [2/5] [Copy To] [2/2]

 {Fader} [2/2] [Label] Pix Color

 Press the two buttons for fader 2/2

 Select Red (CP9021) , Blue (CP9033) , Yellow (CP9025) , Purple
 (CP9036) , Green (CP9027) [Enter]

 Now filter the list in Fader Config to Cyc Pixels (G321)

 Change the timing to Up 0.2 and Down 0.2;               set the priorities to P6/ P3

 Go back to Live and run the list

14   Eos Family Busking

## Gobo List for Spot Fixtures

     In order to add quick access to texture, let’s build a Beam Palette list for
     our gobos.
     First let’s move our Front Light Sub to a different Fader. Because it is on
     and plunging the band into darkness wouldn’t be appropriate, load it on
     Fader 1/10 first.

      [Sub] [301] and press both buttons on Fader 1/10

      Bring it up if it is flashing.

      Hold [Shift] and press [Load] to clear the old fader
     Now let’s continue:

      Press both buttons under fader 2/1

      Tap in order the Beam Palettes for all the gobos for the Sola 750s but
      don’t do the open frame

      Hit [Enter]

      Bring the fader up and press the bottom button

      Go back into Fader Config and change the behavior to wrap and set the
      priority to P6/P3 and LTP and make sure FX Off 0 is unchecked

      Label this fader OHS Gobo
                                                                                    Keep the Side Spots as beams to keep some
      Filter this for only the OH Spots.
                                                                                    clean lines in the air.

## Effects

With a good base, some effects are needed in addition to all this. A
good idea would be to build some presets to house the effects. Then
build a preset FX list. This is more useful than building one submaster for
one instance. These can be built in Blind so that only the effect data and
not the position data is recorded.

 [Blind] [Preset] [310] [Enter] [Label] Side Figure 8

 Side Spots (G105) [Effect] [903] [Enter]

 [Clear]

 [Preset] [311] [Enter] [Label] Side Spiral

 Side Spots (G105) [Effect] [906] [Enter]

 [Clear]

 [Preset] [312] [Enter] [Label] Side Ballyhoo

 Side Spots (G105) [Effect] [909] [Enter]

 [Clear]

 Press the two buttons corresponding with Fader 2/10 and using the
 direct selects, select in order Preset 310, 311, 312 and press [Enter]

 Label this fader SS FX

 Set the priorities of Fader 2/10 to P6/P2 and LTP

Now another focus effect list for the OH Washes:
If making several faders of a similar type, a good practice is to copy a
fader with all the options configured before populating it with presets.

 {Fader} [2/10] [Copy To] [2/9] [Enter]

Now it is possible to overwrite contents without affecting settings.

 [Blind] [Preset] [321] [Enter] [Label] OHS F8 M Out

 OH Spots (G103) {Offset} {Mirror out} [Effect] [903] or Figure 8 [Enter]

 [Clear]

 [Blind] [Preset] [322] [Enter] [Label] OHS Bally M In

 OH Spots (G103) {Offset} {Mirror in} [Effect] [909] or Ballyhoo [Enter]

 [Live]

 Press the buttons corresponding to Fader 2/9

 Preset 321 , Preset 322 [Enter]

 {Fader} [2/9] [Label] [Label] OHS FX [Enter]                                   to relabel the fader

16   Eos Family Busking

## Timing and Global Faders

     Hitting the bump button to step through the playlist, you see that
     everything snaps to place, and when the playlist is released, it also snaps
     home or to its background state. That may be what you want for some
     looks, but for most, maybe easing into the change even if they need to
     go in quickly might be a better option.

      In Fader Config, let’s look at Fader 2/10 as an example.                        Look at the Properties

     Look at the timing column with Up and Down Times. The Up Time is
     how long it takes to go from Step to Step. The Down Time is how long
     it takes to Release the Data to Background
     Let’s change the timing for both the FX faders at the same time.

      {Fader} [2/9] [+] [10] [Time] [1] [Time] [Time] [1] [Enter]                     Up 1 / Down 1 (No dwell)
             Note that the Dwell time is not being adjusted on these Faders

      {Fader} [2/3] [Thru] [5] [Time] [1] [Time] [Time] [1] [Enter]                   to change the up and down timing for all
                                                                                      the color playlists

### GLOBAL FX FADER

         Now with timing on these faders, there is an option to control the overall
         rate and size of the effects that are playing. These are called Global FX
         Faders.

          In Fader Config Tab (Tab36)

          Click where it says unmapped over Fader 1/1

          Click in the Target Box and select Global FX

          Then click on the size, 2x                                                  The first fader says Effect Size

          Click the second fader and change that to Effect Rate

          Change the max value to 400 on both faders                                  Allows for a little more flexibility

          Add a Freeze button on the bottom button of the 2nd fader

         Notice that the corresponding Fader Buttons are flashing.

          Move the faders up to the 50% mark; the faders stop flashing                Can now make the size and rate bigger and
                                                                                      smaller than it is recorded
             Motorized faders will automatically set themselves to half.

          Start Fader 9 (OHS FX) and play with Effect Size, Rate, and Freeze          Make it bigger/smaller, faster/slower

          Click the large open box under where it says Global FX.
                                                                                      Can filter this to a single attribute or a full
```text
          Click in the Param Filter box.                                              category
          Now select the Focus Category at the top.                                   Filters to focus effects
```

Best practice is to have two sets of these built from the start. One for
Focus and One for Color.

 Starting with Fader 1/3, build a Color Global FX Fader                    Do this on your own…

Once that is done have some FXs running on stage and slowly bring the
size fader all the way down. See how the movement gets smaller and
then stops. Now bring it slowly all the way to full. Woohoo!
Bring that size fader back to half and slowly bring the rate fader down.
Watch how the fixtures slow down and then stop wherever they are.
Now bring the Rate Fader all the way up. Woohoo!

18   Eos Family Busking

## Stomp!

     Everyone needs a few fast fire effects that can be triggered at any point.
     Some examples may be a strobe, an open white flash, and a scenic
     wipe.
     To keep our fader layout, it makes sense to move Sub 301 to Fader 1/5
     Populate it first and then remove the old one.
     Use the backwall pixels for maximum oomph.

### STROBE

        Let’s build a quick LED Random Strobe

         [Effect] [Effect]

         [981] [Enter]

         Choose {Linear}

         [Label] LED Random Strobe

         Click {Edit}

         Click {Patterns} and select {Random}, the last option                       Till you get something that you like

         Click {Apply}

         Change the Cycle time to 0.2

         Go to [Live]

         Select Cyc Pixels Random Group (G323) from the Cyc MS and hit
                                                                                     Nice!
         [Effect] [981] [Enter]

         [Select Last] {Intensity} [Record] [Sub] [302] [Label] Pix Strobe [Enter]

         Load to Fader 1/8

         [Sub] [302] [Enter] {Properties}

         Set it to LTP with a Priority of P9/P2, LTP, set the Dwell to Man and
                                                                                     Priority set to override everything
         Exclude from Rec

         [Clear] [Sneak] [Enter]

### OPEN WHITE FLASH

 Select Cyc Pixels Group (G321) [Home] [Enter]
                                                                              These are crazy bright. Going for shock and
 [At] [40] [Enter]
                                                                              awe, not pain.
 [Select Last] [Record] [Sub] [303] [Label] Pix White

 Load on Fader 1/9

 [Sub] [303] [Enter] {Properties}

 Set it to LTP with a Priority of P9/P2, LTP, set the Dwell to Man and
                                                                              Again priority set to override everything
 Exclude from Rec

### SCENIC WIPE

Let’s copy the already built Int Wave effect so it can be editted later.

 [Effect] [Effect]

 [932] [Copy To] [932.1] [Enter]

 [932.1] [Label] Cyc Wave

Adjust the effect to make it a single shot effect and change some timing to
pretty it up.

 Scale to 100

 Cycle time to 1.5

 Duration Number of Cycles 1                                                  Want wave to run just once

 Set Exit to Cascade and Fade By Size

 [932.1] [Copy To] [932.2] [Label] Cyc Wave Part 2

Let’s put these in Presets.

 [Blind] [Preset] [331] [Enter] [Label] Cyc Wave P1

 Select Cyc Pixels Mirror Out (G327) [At] [40] [Enter]

 [Select Last] [Effect] [932.1] [Enter]

 [Blind] [Preset] [332] [Enter] [Label] Cyc Wave P2

 Select Cyc Pixels Mirror Out (G327) [At] [40] [Enter]

 [Select Last] [Effect] [932.2] [Enter]

 Click the two corresponding buttons for Fader 1/10

 Tap Preset 331 and 332. Hit [Enter]

20   Eos Family Busking

        There are now two presets with two effects with the same data in them.
        This will allow us to fire the effect before the last one completes for some
        fun flexibility.

         In Fader Config

         Set this to LTP, P9/P2

         Set Wrap and Stomp Release                                                    Stomp release – if something else comes
                                                                                       along with same channels, what do I do?
         Fader 1/10 [Label] Cyc Wave

         Hit the bump button once and see how it fires, then hit it twice in
         succession.

         Next hold the Open white bump and hit the Cyc Wave bump at the
         same time.

## Play Time!

     The song will be played twice.
     You should play around with all the new toys.
     Have some fun.

## Busking Magic Sheet

Let’s look at an example of a magic sheet for busking. This is just one
example built specifically for manual control - changing lights live on
stage without recording the data. In order to do this, a magic sheet is
needed that enables changes to information very quickly.

Snapshot 103.1 Enter                                                            MS 8004 Effects and MS 8002 “Busking”

Most of this magic sheet should look familiar to you. Parts of other
magic sheets in the file have been taken and copied into this magic
sheet to keep all the necessary tools on one page so that while you are
busking you are not changing magic sheet pages as much.
This is a quick way to create the control surface you need with the tool
sets already built.

### A QUICK REVIEW.

   To do this you would go into the magic sheets that are already created and
   make sure you group the objects you want to copy then CTRL-C. Close the
   chevron and edit the new magic sheet and CTRL-V to paste the objects in a
   new magic sheet. Grouping the objects will preserve the target numbers so
   you won’t have to renumber all the copied objects.
   There is no reason to rebuild all the data if it’s in the file already.
   Looking at this Magic Sheet, keep your workflow in mind.

22   Eos Family Busking

### WORK FLOW

     What is the first thing you do?
     - Select the Channels
     - Offset or fan
     - Intensity
     - NP Modifiers
     This may not be the way your mind works.
     Maybe you want to make all the adjustments to the NP’s, then bring up
     the intensity.
     Maybe you want to make all the changes and then use offsets and fans
     just for FX selections.
     That’s OK! Figure out a layout and workflow that works for you. There
     is no right answer here. The right answer is a page that helps you get
     the information on stage as fast as possible.
     Now let’s look at the magic sheet a little closer.

### CHANNEL AND GROUP SELECTIONS WITH OFFSET AND FAN MACROS

### INTENSITY CONTROL

### NP MODIFIERS: FOCUS, COLOR, BEAM

24   Eos Family Busking

### SYSTEM CONTROL OPTIONS

### SNEAK OPTIONS

        On the left is a column of Sneak buttons that sneak individual categories.
        Do the following without touching the keypad, only using the touch screen.

         FOH Spots (SolaThtr) (G102) Full (IP5)

         Singer (FP118) BP9201.4 - third Gobo on wheel one

         Edge E-40 (BP9023)

         Zoom BP9043 - medium

         Azure (CP9031)

         Hit Focus Sneak (M8023)                                                                  Only the Focus Parameters were snuck.

         Singer (FP118)                                                                           Focuses the group back on the Singer.

         Hit Color Sneak (M8038)                                                                  How long does it take? What is default in
                                                                                                    this show file?
         Hit Sys Sneak 2 (M8039)                                                                  Did you just see the screen flash?
                                                                                                    These macros go into User Settings and
                                                                                                    change the global sneak time
             Caution! These Macros will clear the command line as it goes in and out of settings.

         FOH Spots (SolaThtr) (G102) [At] [0] [Sneak] [Enter]                                     Sneaks out at new default time (3 sec)

### MANUAL TIME SECTION

 In Manual Time area, under the INT Column, tap 2                             Fader Icon under that column moved to 2

These Macro buttons are adjusting Manual Time Faders that are filtered to
each parameter type.
These faders are set with a range of 0-4 Seconds. This can easily be adjusted
by adjusting the ranges in the Fader Configuration and adjusting the
percentages in the Macros.

 [Macro] [Macro]                                                                Let’s see what the Macros say.

 [8103] [Enter]                                                                 The Macro says Fader 10/1 @ 50 Enter
    Another way to read this is Fader Page 10 Fader 1 @ 50 Percent.

The range is set 0-4 on the fader so 50 percent is 2.

 [Live] {Snapshot} [103.1] [Enter]

 Under INT, 3

 Under Focus, 1

 Under Color, 4

 Under Beam 1

 FOH Spots (G102) Full (IP5)                                                They came up in 3 Seconds.

 X DS (FP111)                                                                 They moved in 1 second.

 Orange CP9022)                                                               Slow fade over 4 seconds.

 Zoom BP9045 - Big                                                            Zoomed in 1 Second

As you can see, having quick access to these timing changes can be very
helpful. They are fast enough that it doesn’t have to be something you set
and forget. These should be used often and as part of the flow to get data
on stage. The fixtures snapping to orange has a different affect on the
audience vs the fixtures fading to orange.
Are you making this change because of an emotional change or are you
changing the data on a beat?
Do you want the audience to notice the change or do you want them to
eventually notice the scene change?

 Change the Fader page to page 10.

You see each of the subs is blinking and has control over the timing.

 All Off - lower right corner on the Magic Sheet                              The faders have now stopped flashing and
                                                                                if motorized, moved back to the bottom

These are no longer active and do not have control of the manual timing.
When these faders are off, the console defaults to the manual time setting
set in Settings.

 Change the Fader page back to 1.

26   Eos Family Busking

     Before talking about the last section of the magic sheet, it’s time to play
     around a little.
     - Use the tools created to change the scene as the song is playing.
     - Be QUICK about it.
     - If you have a thought, execute it, don’t over think it.
     - Keep it simple.
     - This is all about being fast.
     - If it’s not pretty, you have the rest of the song to make what’s on stage
         pretty. The first song is always going to be rough. Maybe even the first
         set?!
     - Get your bearings and get some lights on and play around with
         bouncing through colors to the beat.
     - Add some Effects.
     - Don’t forget about the timing buttons!

### CHANGE SONG.

         Let’s try a different song.
         After three times. Stop the music.
         - How did that feel?
         _____________________________________________________
         _____________________________________________________
         - What worked and what didn’t work
         _____________________________________________________
         _____________________________________________________
         - Did you feel like you were missing anything?
         _____________________________________________________
         _____________________________________________________
         - What would you have changed on this magic sheet?
         _____________________________________________________
         _____________________________________________________

## Saving for Dump Cues!

While busking, did you feel like you wanted to record some of the looks
you built to get back to them quickly later in the song? Maybe you
really liked what you did for the chorus or verse? Maybe the base cue
you started with should have morphed throughout the song and you
wanted a different place for all the lights to go back to.
The last part of magic sheet is where there are macros to record and
access dump cues.
This are lovingly refered to as dump cues because it doesn’t necessarily
matter what cues they are; they are just places to dump data into.
Let’s take a look at Magic Sheet 8002 “Busking”.

[Clear] [Sneak] [Enter]    [Go to Cue] [Out] {Enter]                               Start with a blank canvas

### RECORD CONTROLS

    Tap Cue 100/1 Base Purple World

   By Setting one of our magic sheet buttons to a cue target, when you hit the
   button, it acts as if the cue was loaded and runs off of the cue timing.

    Tap Cue 100/2 Blue and Gold World

   Under each cue button there have two Record options. A Full Record button
   and a Manual Record Button. The Full Record buttons will take the entire
   scene, including all data coming from the faders and store it in the specific
   cue. The Manual Record button will only take the manual data and record it
   into the cue, leaving the faders to keep control over the data.

28   Eos Family Busking

### FULL RECORD

        Currently in Cue 100/2

         On the faders, bring up S301 (Band Fronts) to half

         Bring up S351 (OH Wash INT) to full

         Hit  (Go) on the OHW Focus Playlist.

         On the Magic Sheet, tap Side Spots (Sola 750) (G105)

         75% (IP4)

### USC X (FP112)

                                                                                        They are already set to Open, but the
         Open (CP9001)                                                                data needs to be manual.

                                                                                        All the red data in the Summary view is
         Tap Record 3 (8055) under Cue100/3         Full Record option                now gone.
         Select FOH Spots (SolaThtr) (G102)

        Look at the Live Summary. The Data is now blue and is stored in the Cue.
        The Command line now says Cue 100/3.
        After using any of the Full Record buttons, reset the faders that contributed
        to the look on stage.

         Bring S301 (Band Fronts) down and hit the bottom bump button                   To release the fader

         Hit the top bump button on the OHW Focus playlist

         Fade S351 OH Wash Int to the bottom

        Something to keep in mind: If you record any effects into the cues and
        the rates and sizes have been adjusted using the Global FX fader, the cues
        will record with the times from the FX, not from the Global FX faders. Global
        FX fader contributions are not recorded.
        All of these Macros are recording these cues as Cue Only to preserve each
        cue. If you don’t have Auto Mark enabled, you may have to set marks or you
        will see each live change cue to cue. This might be what you want! Just pay
        attention.

### MANUAL RECORD OPTIONS

 HS CSpot > (G220) HS CSpot < (G240) Full (IP5) Red (CP9021)

 OH Wash (Sola 2K) (G104) Out (IP1)

 In the Cyc area, tap Cells >< (G315)

 Hold [Shift] and tap 6500 (CP9010) Red (CP9021) [Enter]

 OH Spot (Sola 750) (G103) Full (IP5)

 House (FP116) Red (CP9021)

 On the faders, hit the SS FX bottom bump button ()                               To start the FX

 Tap Man Record 4 (8058)

 Tap Cue 100/3                                                                   The FX is still running, and you still have
                                                                                   control with the Playlists and Subs.
 Tap Cue 100/4

 Hit the SS FX top bump button()                                                  To release the SS FX fader

A Note: Each Quick Access button has a field for Label already in place, so
if you label those 4 cues, they will show up in the Magic sheet.
Under the 4 cue buttons and records, there are two larger record buttons.
No matter where in the stack you are, you can record the next available cue
to continue the stack if more than 4 cues are needed. Most of the time you
will try and fit more than 4 quick access buttons on the sheet. As few as
three and as many as 12. It’s a balance of fitting all the other selection tools
and other control tools on the page plus the records buttons.

 Top D60 (G200) Full (IP5)

 Blue (CP9033)

 On the faders, hit the SS Foc bottom bump button () twice.

 Cyc All (G307) Out (IP1)

 Cyc Pixels (G321) 25% (IP2)

 Blue (CP9033)

 Record Next Available

 Hit  (Stop/Back) on the Main Playback

 Hit  (Go).

SS Focus Playlist is no longer contributing, and that data is now in the cue.

 Cyc All (G307) Full (IP5)

 On the faders, hit the OHS FX bottom bump button ()

 Man Rec Next Available

 Hit the OHS FX top bump button()                                                 OHS FX was not recorded into a cue.

30   Eos Family Busking

### RECORD NEXT

        The two Rec Next Available macros are able to be recorded from any cue.
        They will record a cue stack in order beyond the 4 dump cues you already
        have if you need more. This is handy to build a new cue off of an existing
        cue. For example, you are in a Chorus look and you want to record a new
        verse, but you are also going to use the other cues you have recorded.
        Lets see it work.

         Hit Cue 100/1 Base Purple World

         Hit Record Next Available                                                 Command line should say Cue 100/7

         Hit  (Stop/Back) on the Main Playback

         Hit  (Go)

## Final Play Time

Let’s play around for about 45 minutes and get a feel for using the
manual controls and the subs.
The music will play on repeat and switch songs every three plays.
At the end of this, one song will be selected as the final busking song.
Consider these 45 minutes as a sound check.
- If you need to build base cues or just practice the order of adding
    manual data do that.
- If you want to wing it just play around. You don’t have to record
    anything.
- Be sure to include both manual data as well as recorded playlists. Don’t
    want the show to be just hitting Go when it’s real.

Run the song a final time and see how it goes.

After the song is over, stop the music.
Let’s discuss what happened.
- What worked?
    _____________________________________________________
    _____________________________________________________
- What didn’t?
    _____________________________________________________
    _____________________________________________________
- How did that feel?
    _____________________________________________________
    _____________________________________________________
- What will you change for your own workflow next time?
    _____________________________________________________
    _____________________________________________________
- What were you missing all day?
    _____________________________________________________
    _____________________________________________________
- Are you planning on using manual data in conjunction with recorded
    data next time you busk?
    _____________________________________________________
    _____________________________________________________

32   Eos Family Busking

                                                                                   Hookup             33

## Mind the Gap Channel Hookup

```text
Chan   Univ / Address   Manufacturer   Fixture            Mode             Label
1      1      1         Generic        Dimmer             --               Frontlight - A
2      1      2         Generic        Dimmer             --               Frontlight - B
3      1      3         Generic        Dimmer             --               Frontlight - C
4      1      4         Generic        Dimmer             --               Frontlight - D
5      1      5         Generic        Dimmer             --               Frontlight - E
6      1      33        Generic        Dimmer             --               Frontlight - A
7      1      31        Generic        Dimmer             --               Frontlight - B
8      1      32        Generic        Dimmer             --               Frontlight - C
9      1      35        Generic        Dimmer             --               Frontlight - D
10     1      34        Generic        Dimmer             --               Frontlight - E

31     1      301       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - A
32     1      310       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - B
33     1      319       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - C
34     1      328       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - D
35     1      337       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - E
36     1      346       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - F
37     1      355       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - G
38     1      364       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - H
39     1      373       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - I (eye)
40     1      382       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - J
41     1      391       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - K
42     1      400       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - L (ell)
43     1      409       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - M
44     1      418       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - N
45     1      427       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - O (oh)
46     1      436       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - P
47     1      445       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - Q
48     1      454       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight – R
49     1      463       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight – S
50     1      472       ETC Fixtures   ETC D60 Lustr+     Direct Str [9]   Downlight - T

51     2      1         ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 1  Left
52     2      7         ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 1  Mid
53     2      13        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 1  Right
54     2      19        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 2  Left
55     2      25        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 2  Mid
56     2      31        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 2  Right
57     2      37        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 3  Left
58     2      43        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 3  Mid
59     2      49        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 3  Right
60     2      55        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 4  Left
61     2      61        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 4  Mid
62     2      67        ETC Fixtures   ColorSource Spot   Direct [6]       Hi Side Tx - Ln 4  Right
```

34 Eos Family Busking

```text
Chan     Univ / Address     Manufacturer       Fixture             Mode                     Label
71       2      73          ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 1  Right
72       2      79          ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 1  Mid
73       2      85          ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 1  Left
74       2      91          ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 2  Right
75       2      97          ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 2  Mid
76       2      103         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 2  Left
77       2      109         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 3  Right
78       2      115         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 3  Mid
79       2      121         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 3  Left
80       2      127         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 4  Right
81       2      133         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 4  Mid
82       2      139         ETC Fixtures       ColorSource Spot    Direct [6]               Hi Side Tx - Ln 4  Left

101      2      201*        High End Systems   SolaFrame Theatre   SolaFrame Theatre [47]   FOH Mover - Spot
102      2      251         High End Systems   SolaFrame Theatre   SolaFrame Theatre [47]   FOH Mover - Spot
103      2      301         High End Systems   SolaFrame Theatre   SolaFrame Theatre [47]   FOH Mover - Spot
104      2      351         High End Systems   SolaFrame Theatre   SolaFrame Theatre [47]   FOH Mover - Spot
105      2      401         High End Systems   SolaFrame Theatre   SolaFrame Theatre [47]   FOH Mover - Spot
```
                * Think Offset!
```text
111      3      1           High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
112      3      48          High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
113      3      95          High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
114      3      142         High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
115      3      189         High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
116      3      236         High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
117      3      283         High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot
118      3      330         High End Systems   SolaFrame 750       SolaFrame 750 [47]       Overstage Mover - Spot

121      4      1           High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
122      4      37          High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
123      4      73          High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
124      4      109         High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
125      4      145         High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
126      4      181         High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
127      4      217         High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash
128      4      253         High End Systems   SolaWash 2000       SolaWash 2000 [36]       Overstage Mover - Wash

132      5      10          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High
133      5      19          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High
134      5      28          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High
135      5      37          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High
136      5      46          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High
137      5      55          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High
138      5      64          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – High

141      5      73          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
142      5      82          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
143      5      91          ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
144      5      100         ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
145      5      109         ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
146      5      118         ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
147      5      127         ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid
148      5      136         ETC Fixtures       S4 LED S2 Lustr     Direct Str [9]           Side – Mid

Chan     Univ / Address    Manufacturer       Fixture           Mode                          Label
151      1     281         Generic            Dimmer            --                            Side – Scroller
151 P2   1     291         Generic            Scroller          --                            Side – Scroller
152      1     282         Generic            Dimmer            --                            Side – Scroller
152 P2   1     292         Generic            Scroller          --                            Side – Scroller
153      1     283         Generic            Dimmer            --                            Side – Scroller
153 P2   1     293         Generic            Scroller          --                            Side – Scroller
154      1     284         Generic            Dimmer            --                            Side – Scroller
154 P2   1     294         Generic            Scroller          --                            Side – Scroller
155      1     285         Generic            Dimmer            --                            Side – Scroller
155 P2   1     295         Generic            Scroller          --                            Side – Scroller
156      1     286         Generic            Dimmer            --                            Side – Scroller
156 P2   1     296         Generic            Scroller          --                            Side – Scroller
157      1     287         Generic            Dimmer            --                            Side – Scroller
157 P2   1     297         Generic            Scroller          --                            Side – Scroller
158      1     288         Generic            Dimmer            --                            Side – Scroller
158 P2   1     298         Generic            Scroller          --                            Side – Scroller

161      5     301 *       High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
162      5     351         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
163      5     401         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
164      5     451         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
165      6     1           High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
166      6     51          High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
167      6     101         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
168      6     151         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Side Mover – Spot
```
               * Think Offset!

```text
171      5     163         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
172      5     172         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
173      5     181         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
174      5     190         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
175      5     199         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
176      5     208         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
177      5     217         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin
178      5     226         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Side – Shin

181      3     381         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Front Wash
182      3     390         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Front Wash
183      3     399         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Front Wash
184      3     408         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Front Wash
185      3     417         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Front Wash

191      4     441         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Box Wash – Downstage
192      4     450         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Box Wash – Downstage
193      4     459         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Box Wash – Downstage
194      4     468         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Box Wash – Downstage
195      4     477         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Box Wash – Downstage
196      4     486         ETC Fixtures       S4 LED S2 Lustr   Direct Str [9]                Box Wash – Downstage

197      6     325         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Box Wash – Spot
198      6     372         High End Systems   SolaFrame 750     SolaFrame 750 [47]            Box Wash – Spot
```

36 Eos Family Busking

```text
Chan     Univ / Address   Manufacturer   Fixture       Mode   Label
201      1      191       Generic        Footlight     --     Talent Uplight
202      1      192       Generic        Footlight     --     Talent Uplight
203      1      193       Generic        Footlight     --     Talent Uplight
204      1      194       Generic        Footlight     --     Talent Uplight
205      1      195       Generic        Footlight     --     Talent Uplight
206      1      196       Generic        Footlight     --     Talent Uplight
207      1      197       Generic        Footlight     --     Talent Uplight
208      1      198       Generic        Footlight     --     Talent Uplight
209      1      199       Generic        Footlight     --     Talent Uplight

211      1      151       Generic        Dimmer        --     Under Platform S4 Mini
212      1      152       Generic        Dimmer        --     Under Platform S4 Mini
213      1      153       Generic        Dimmer        --     Under Platform S4 Mini
214      1      154       Generic        Dimmer        --     Under Platform S4 Mini
215      1      155       Generic        Dimmer        --     Under Platform S4 Mini
216      1      156       Generic        Dimmer        --     Under Platform S4 Mini
217      1      157       Generic        Dimmer        --     Under Platform S4 Mini
218      1      158       Generic        Dimmer        --     Under Platform S4 Mini
219      1      159       Generic        Dimmer        --     Under Platform S4 Mini
220      1      160       Generic        Dimmer        --     Under Platform S4 Mini
221      1      161       Generic        Dimmer        --     Under Platform S4 Mini
222      1      162       Generic        Dimmer        --     Under Platform S4 Mini
223      1      163       Generic        Dimmer        --     Under Platform S4 Mini
224      1      164       Generic        Dimmer        --     Under Platform S4 Mini
225      1      165       Generic        Dimmer        --     Under Platform S4 Mini
226      1      166       Generic        Dimmer        --     Under Platform S4 Mini

231      1      251       Generic        House Light   --     Houselight
232      1      252       Generic        House Light   --     Houselight
233      1      253       Generic        House Light   --     Houselight
234      1      254       Generic        House Light   --     Houselight
235      1      255       Generic        House Light   --     Houselight
236      1      256       Generic        House Light   --     Houselight
237      1      257       Generic        House Light   --     Houselight
238      1      258       Generic        House Light   --     Houselight
239      1      259       Generic        House Light   --     Houselight
240      1      260       Generic        House Light   --     Houselight
241      1      261       Generic        House Light   --     Houselight
242      1      262       Generic        House Light   --     Houselight
243      1      263       Generic        House Light   --     Houselight
244      1      264       Generic        House Light   --     Houselight
245      1      265       Generic        House Light   --     Houselight
246      1      266       Generic        House Light   --     Houselight
247      1      267       Generic        House Light   --     Houselight
248      1      268       Generic        House Light   --     Houselight
249      1      269       Generic        House Light   --     Houselight
250      1      270       Generic        House Light   --     Houselight

Chan   Univ / Address   Manufacturer   Fixture             Mode                            Label
251    3      431       ETC Fixtures   S4 LED S2 Lustr     Direct Str [9]                  Proscenium Highlight
252    3      440       ETC Fixtures   S4 LED S2 Lustr     Direct Str [9]                  Proscenium Highlight
253    3      449       ETC Fixtures   S4 LED S2 Lustr     Direct Str [9]                  Proscenium Highlight
254    3      458       ETC Fixtures   S4 LED S2 Lustr     Direct Str [9]                  Proscenium Highlight
255    3      467       ETC Fixtures   S4 LED S2 Lustr     Direct Str [9]                  Proscenium Highlight
256    3      476       ETC Fixtures   S4 LED S2 Lustr     Direct Str [9]                  Proscenium Highlight

261    4      351       Generic        LED IRGBA           8B [5]                          Scenic Highlight
262    4      356       Generic        LED IRGBA           8B [5]                          Scenic Highlight
263    4      361       Generic        LED IRGBA           8B [5]                          Scenic Highlight
264    4      366       Generic        LED IRGBA           8B [5]                          Scenic Highlight
265    4      371       Generic        LED IRGBA           8B [5]                          Scenic Highlight
266    4      376       Generic        LED IRGBA           8B [5]                          Scenic Highlight
267    4      381       Generic        LED IRGBA           8B [5]                          Scenic Highlight
268    4      386       Generic        LED IRGBA           8B [5]                          Scenic Highlight
269    4      391       Generic        LED IRGBA           8B [5]                          Scenic Highlight
270    4      396       Generic        LED IRGBA           8B [5]                          Scenic Highlight
271    4      401       Generic        LED IRGBA           8B [5]                          Scenic Highlight
272    4      406       Generic        LED IRGBA           8B [5]                          Scenic Highlight

291    4      411       SGM            SP 6                6ch MC [6] [6 cells]            6-Pack Back Highlight
292    4      417       SGM            SP 6                6ch MC [6] [6 cells]            6-Pack Back Highlight
293    4      423       SGM            SP 6                6ch MC [6] [6 cells]            6-Pack Back Highlight
294    4      429       SGM            SP 6                6ch MC [6] [6 cells]            6-Pack Back Highlight
295    4      435       SGM            SP 6                6ch MC [6] [6 cells]            6-Pack Back Highlight

301    8      1         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
302    8      25        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
303    8      49        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
304    8      73        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
305    8      97        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
306    8      121       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
307    8      145       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
308    8      169       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
309    8      193       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
310    8      217       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
311    8      241       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top
312    8      265       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Top

351    9      1         Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
352    9      25        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
353    9      49        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
354    9      73        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
355    9      97        Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
356    9      121       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
357    9      145       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
358    9      169       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
359    9      193       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
360    9      217       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
361    9      241       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
362    9      265       Chroma Q       Color Force II 72   RGBA x4 Off MC [24] [6 Cells]   Cyc Bottom
```

38 Eos Family Busking

```text
Chan     Univ / Address   Manufacturer   Fixture   Mode                       Label
601      --     --        ETC Fixtures   Virtual   Server Ver 1.0 [0]         VMS – Back Wall Grid
602      --     --        ETC Fixtures   Virtual   Layer Ver 1.0 [0]          VMS – Back Wall Grid
603      --     --        ETC Fixtures   Virtual   Layer Ver 1.0 [0]          VMS – Back Wall Grid
604      --     --        ETC Fixtures   Virtual   Effect Layer Ver 1.1 [0]   VMS – Back Wall Grid
605      --     --        ETC Fixtures   Virtual   Effect Layer Ver 1.1 [0]   VMS – Back Wall Grid

611      --     --        ETC Fixtures   Virtual   Server Ver 1.0 [0]         VMS – “MTG”
612      --     --        ETC Fixtures   Virtual   Layer Ver 1.0 [0]          VMS – “MTG”
613      --     --        ETC Fixtures   Virtual   Layer Ver 1.0 [0]          VMS – “MTG”
614      --     --        ETC Fixtures   Virtual   Effect Layer Ver 1.1 [0]   VMS – “MTG”
615      --     --        ETC Fixtures   Virtual   Effect Layer Ver 1.1 [0]   VMS – “MTG”

701      20     1         Generic        LED RGB   8B [3]                     Back Wall Grid
702      20     4         Generic        LED RGB   8B [3]                     Back Wall Grid
703      20     7         Generic        LED RGB   8B [3]                     Back Wall Grid
704      20     10        Generic        LED RGB   8B [3]                     Back Wall Grid
705      20     13        Generic        LED RGB   8B [3]                     Back Wall Grid
706      20     16        Generic        LED RGB   8B [3]                     Back Wall Grid
707      20     19        Generic        LED RGB   8B [3]                     Back Wall Grid
708      20     22        Generic        LED RGB   8B [3]                     Back Wall Grid
709      20     25        Generic        LED RGB   8B [3]                     Back Wall Grid
710      20     28        Generic        LED RGB   8B [3]                     Back Wall Grid
711      20     31        Generic        LED RGB   8B [3]                     Back Wall Grid
712      20     34        Generic        LED RGB   8B [3]                     Back Wall Grid
713      20     37        Generic        LED RGB   8B [3]                     Back Wall Grid
714      20     40        Generic        LED RGB   8B [3]                     Back Wall Grid
715      20     43        Generic        LED RGB   8B [3]                     Back Wall Grid
716      20     46        Generic        LED RGB   8B [3]                     Back Wall Grid
717      20     49        Generic        LED RGB   8B [3]                     Back Wall Grid
718      20     52        Generic        LED RGB   8B [3]                     Back Wall Grid
719      20     55        Generic        LED RGB   8B [3]                     Back Wall Grid
720      20     58        Generic        LED RGB   8B [3]                     Back Wall Grid
721      20     61        Generic        LED RGB   8B [3]                     Back Wall Grid
722      20     64        Generic        LED RGB   8B [3]                     Back Wall Grid
723      20     67        Generic        LED RGB   8B [3]                     Back Wall Grid
724      20     70        Generic        LED RGB   8B [3]                     Back Wall Grid
725      20     73        Generic        LED RGB   8B [3]                     Back Wall Grid
726      20     76        Generic        LED RGB   8B [3]                     Back Wall Grid
727      20     79        Generic        LED RGB   8B [3]                     Back Wall Grid
728      20     82        Generic        LED RGB   8B [3]                     Back Wall Grid
729      20     85        Generic        LED RGB   8B [3]                     Back Wall Grid
730      20     88        Generic        LED RGB   8B [3]                     Back Wall Grid
731      20     91        Generic        LED RGB   8B [3]                     Back Wall Grid
732      20     94        Generic        LED RGB   8B [3]                     Back Wall Grid
733      20     97        Generic        LED RGB   8B [3]                     Back Wall Grid
734      20     100       Generic        LED RGB   8B [3]                     Back Wall Grid
735      20     103       Generic        LED RGB   8B [3]                     Back Wall Grid
736      20     106       Generic        LED RGB   8B [3]                     Back Wall Grid
737      20     109       Generic        LED RGB   8B [3]                     Back Wall Grid
738      20     112       Generic        LED RGB   8B [3]                     Back Wall Grid
739      20     115       Generic        LED RGB   8B [3]                     Back Wall Grid
740      20     118       Generic        LED RGB   8B [3]                     Back Wall Grid

Chan   Univ / Address   Manufacturer   Fixture   Mode              Label
741    20     121       Generic        LED RGB   8B [3]            Back Wall Grid
742    20     124       Generic        LED RGB   8B [3]            Back Wall Grid
743    20     127       Generic        LED RGB   8B [3]            Back Wall Grid
744    20     130       Generic        LED RGB   8B [3]            Back Wall Grid
745    20     133       Generic        LED RGB   8B [3]            Back Wall Grid
746    20     136       Generic        LED RGB   8B [3]            Back Wall Grid
747    20     139       Generic        LED RGB   8B [3]            Back Wall Grid
748    20     142       Generic        LED RGB   8B [3]            Back Wall Grid
749    20     145       Generic        LED RGB   8B [3]            Back Wall Grid
750    20     148       Generic        LED RGB   8B [3]            Back Wall Grid
751    20     151       Generic        LED RGB   8B [3]            Back Wall Grid
752    20     154       Generic        LED RGB   8B [3]            Back Wall Grid
753    20     157       Generic        LED RGB   8B [3]            Back Wall Grid
754    20     160       Generic        LED RGB   8B [3]            Back Wall Grid
755    20     163       Generic        LED RGB   8B [3]            Back Wall Grid
756    20     166       Generic        LED RGB   8B [3]            Back Wall Grid
757    20     169       Generic        LED RGB   8B [3]            Back Wall Grid
758    20     172       Generic        LED RGB   8B [3]            Back Wall Grid
759    20     175       Generic        LED RGB   8B [3]            Back Wall Grid
760    20     178       Generic        LED RGB   8B [3]            Back Wall Grid
761    20     181       Generic        LED RGB   8B [3]            Back Wall Grid
762    20     184       Generic        LED RGB   8B [3]            Back Wall Grid
763    20     187       Generic        LED RGB   8B [3]            Back Wall Grid
764    20     190       Generic        LED RGB   8B [3]            Back Wall Grid
765    20     193       Generic        LED RGB   8B [3]            Back Wall Grid
766    20     196       Generic        LED RGB   8B [3]            Back Wall Grid
767    20     199       Generic        LED RGB   8B [3]            Back Wall Grid
768    20     202       Generic        LED RGB   8B [3]            Back Wall Grid
769    20     205       Generic        LED RGB   8B [3]            Back Wall Grid
770    20     208       Generic        LED RGB   8B [3]            Back Wall Grid
771    20     211       Generic        LED RGB   8B [3]            Back Wall Grid
772    20     214       Generic        LED RGB   8B [3]            Back Wall Grid
773    20     217       Generic        LED RGB   8B [3]            Back Wall Grid
774    20     220       Generic        LED RGB   8B [3]            Back Wall Grid
775    20     223       Generic        LED RGB   8B [3]            Back Wall Grid
776    20     226       Generic        LED RGB   8B [3]            Back Wall Grid
777    20     229       Generic        LED RGB   8B [3]            Back Wall Grid
778    20     232       Generic        LED RGB   8B [3]            Back Wall Grid
779    20     235       Generic        LED RGB   8B [3]            Back Wall Grid
780    20     238       Generic        LED RGB   8B [3]            Back Wall Grid
781    20     241       Generic        LED RGB   8B [3]            Back Wall Grid
782    20     244       Generic        LED RGB   8B [3]            Back Wall Grid
783    20     247       Generic        LED RGB   8B [3]            Back Wall Grid
784    20     250       Generic        LED RGB   8B [3]            Back Wall Grid
785    20     253       Generic        LED RGB   8B [3]            Back Wall Grid
786    20     256       Generic        LED RGB   8B [3]            Back Wall Grid
787    20     259       Generic        LED RGB   8B [3]            Back Wall Grid
788    20     262       Generic        LED RGB   8B [3]            Back Wall Grid
789    20     265       Generic        LED RGB   8B [3]            Back Wall Grid
790    20     268       Generic        LED RGB   8B [3]            Back Wall Grid
791    20     271       Generic        LED RGB   8B [3]            Back Wall Grid
792    20     274       Generic        LED RGB   8B [3]            Back Wall Grid
```

40 Eos Family Busking

```text
Chan     Univ / Address   Manufacturer   Fixture   Mode     Label
793      20     277       Generic        LED RGB   8B [3]   Back Wall Grid
794      20     280       Generic        LED RGB   8B [3]   Back Wall Grid
795      20     283       Generic        LED RGB   8B [3]   Back Wall Grid
796      20     286       Generic        LED RGB   8B [3]   Back Wall Grid
797      20     289       Generic        LED RGB   8B [3]   Back Wall Grid
798      20     292       Generic        LED RGB   8B [3]   Back Wall Grid
799      20     295       Generic        LED RGB   8B [3]   Back Wall Grid
800      20     298       Generic        LED RGB   8B [3]   Back Wall Grid
801      20     301       Generic        LED RGB   8B [3]   Back Wall Grid
802      20     304       Generic        LED RGB   8B [3]   Back Wall Grid
803      20     307       Generic        LED RGB   8B [3]   Back Wall Grid
804      20     310       Generic        LED RGB   8B [3]   Back Wall Grid
805      20     313       Generic        LED RGB   8B [3]   Back Wall Grid
806      20     316       Generic        LED RGB   8B [3]   Back Wall Grid
807      20     319       Generic        LED RGB   8B [3]   Back Wall Grid
808      20     322       Generic        LED RGB   8B [3]   Back Wall Grid
809      20     325       Generic        LED RGB   8B [3]   Back Wall Grid
810      20     328       Generic        LED RGB   8B [3]   Back Wall Grid
811      20     331       Generic        LED RGB   8B [3]   Back Wall Grid
812      20     334       Generic        LED RGB   8B [3]   Back Wall Grid
813      20     337       Generic        LED RGB   8B [3]   Back Wall Grid
814      20     340       Generic        LED RGB   8B [3]   Back Wall Grid
815      20     343       Generic        LED RGB   8B [3]   Back Wall Grid
816      20     346       Generic        LED RGB   8B [3]   Back Wall Grid
817      20     349       Generic        LED RGB   8B [3]   Back Wall Grid
818      20     352       Generic        LED RGB   8B [3]   Back Wall Grid
819      20     355       Generic        LED RGB   8B [3]   Back Wall Grid
820      20     358       Generic        LED RGB   8B [3]   Back Wall Grid
821      20     361       Generic        LED RGB   8B [3]   Back Wall Grid
822      20     364       Generic        LED RGB   8B [3]   Back Wall Grid
823      20     367       Generic        LED RGB   8B [3]   Back Wall Grid
824      20     370       Generic        LED RGB   8B [3]   Back Wall Grid
825      20     373       Generic        LED RGB   8B [3]   Back Wall Grid
826      20     376       Generic        LED RGB   8B [3]   Back Wall Grid
827      20     379       Generic        LED RGB   8B [3]   Back Wall Grid
828      20     382       Generic        LED RGB   8B [3]   Back Wall Grid
829      20     385       Generic        LED RGB   8B [3]   Back Wall Grid
830      20     388       Generic        LED RGB   8B [3]   Back Wall Grid
831      20     391       Generic        LED RGB   8B [3]   Back Wall Grid
832      20     394       Generic        LED RGB   8B [3]   Back Wall Grid
833      20     397       Generic        LED RGB   8B [3]   Back Wall Grid
834      20     400       Generic        LED RGB   8B [3]   Back Wall Grid
835      20     403       Generic        LED RGB   8B [3]   Back Wall Grid
836      20     406       Generic        LED RGB   8B [3]   Back Wall Grid
837      20     409       Generic        LED RGB   8B [3]   Back Wall Grid
838      20     412       Generic        LED RGB   8B [3]   Back Wall Grid
839      20     415       Generic        LED RGB   8B [3]   Back Wall Grid
840      20     418       Generic        LED RGB   8B [3]   Back Wall Grid
841      20     421       Generic        LED RGB   8B [3]   Back Wall Grid
842      20     424       Generic        LED RGB   8B [3]   Back Wall Grid
843      20     427       Generic        LED RGB   8B [3]   Back Wall Grid
844      20     430       Generic        LED RGB   8B [3]   Back Wall Grid

Chan   Univ / Address   Manufacturer   Fixture   Mode              Label
845    20     433       Generic        LED RGB   8B [3]            Back Wall Grid
846    20     436       Generic        LED RGB   8B [3]            Back Wall Grid
847    20     439       Generic        LED RGB   8B [3]            Back Wall Grid
848    20     442       Generic        LED RGB   8B [3]            Back Wall Grid
849    20     445       Generic        LED RGB   8B [3]            Back Wall Grid
850    20     448       Generic        LED RGB   8B [3]            Back Wall Grid
851    20     451       Generic        LED RGB   8B [3]            Back Wall Grid
852    20     454       Generic        LED RGB   8B [3]            Back Wall Grid
853    20     457       Generic        LED RGB   8B [3]            Back Wall Grid
854    20     460       Generic        LED RGB   8B [3]            Back Wall Grid
855    20     463       Generic        LED RGB   8B [3]            Back Wall Grid
856    20     466       Generic        LED RGB   8B [3]            Back Wall Grid
857    20     469       Generic        LED RGB   8B [3]            Back Wall Grid
858    20     472       Generic        LED RGB   8B [3]            Back Wall Grid
859    20     475       Generic        LED RGB   8B [3]            Back Wall Grid
860    20     478       Generic        LED RGB   8B [3]            Back Wall Grid
861    20     481       Generic        LED RGB   8B [3]            Back Wall Grid
862    20     484       Generic        LED RGB   8B [3]            Back Wall Grid
863    20     487       Generic        LED RGB   8B [3]            Back Wall Grid
864    20     490       Generic        LED RGB   8B [3]            Back Wall Grid
865    20     493       Generic        LED RGB   8B [3]            Back Wall Grid
866    20     496       Generic        LED RGB   8B [3]            Back Wall Grid
867    20     499       Generic        LED RGB   8B [3]            Back Wall Grid
868    20     502       Generic        LED RGB   8B [3]            Back Wall Grid
869    20     505       Generic        LED RGB   8B [3]            Back Wall Grid
870    20     508       Generic        LED RGB   8B [3]            Back Wall Grid
871    21     1         Generic        LED RGB   8B [3]            Back Wall Grid
872    21     4         Generic        LED RGB   8B [3]            Back Wall Grid
873    21     7         Generic        LED RGB   8B [3]            Back Wall Grid
874    21     10        Generic        LED RGB   8B [3]            Back Wall Grid
875    21     13        Generic        LED RGB   8B [3]            Back Wall Grid
876    21     16        Generic        LED RGB   8B [3]            Back Wall Grid
877    21     19        Generic        LED RGB   8B [3]            Back Wall Grid
878    21     22        Generic        LED RGB   8B [3]            Back Wall Grid
879    21     25        Generic        LED RGB   8B [3]            Back Wall Grid
880    21     28        Generic        LED RGB   8B [3]            Back Wall Grid
881    21     31        Generic        LED RGB   8B [3]            Back Wall Grid
882    21     34        Generic        LED RGB   8B [3]            Back Wall Grid
883    21     37        Generic        LED RGB   8B [3]            Back Wall Grid
884    21     40        Generic        LED RGB   8B [3]            Back Wall Grid

901    22     1         Generic        LED RGB   8B [3]            MTG – “M”
902    22     4         Generic        LED RGB   8B [3]            MTG – “M”
903    22     7         Generic        LED RGB   8B [3]            MTG – “M”
904    22     10        Generic        LED RGB   8B [3]            MTG – “M”
905    22     13        Generic        LED RGB   8B [3]            MTG – “M”
906    22     16        Generic        LED RGB   8B [3]            MTG – “M”
907    22     19        Generic        LED RGB   8B [3]            MTG – “M”
908    22     22        Generic        LED RGB   8B [3]            MTG – “M”
909    22     25        Generic        LED RGB   8B [3]            MTG – “M”
910    22     28        Generic        LED RGB   8B [3]            MTG – “M”
911    22     31        Generic        LED RGB   8B [3]            MTG – “M”
```

42 Eos Family Busking

```text
Chan     Univ / Address   Manufacturer   Fixture   Mode     Label
912      22     34        Generic        LED RGB   8B [3]   MTG – “T”
913      22     37        Generic        LED RGB   8B [3]   MTG – “T”
914      22     40        Generic        LED RGB   8B [3]   MTG – “T”
915      22     43        Generic        LED RGB   8B [3]   MTG – “T”
916      22     46        Generic        LED RGB   8B [3]   MTG – “T”
917      22     49        Generic        LED RGB   8B [3]   MTG – “T”
918      22     52        Generic        LED RGB   8B [3]   MTG – “G”
919      22     55        Generic        LED RGB   8B [3]   MTG – “G”
920      22     58        Generic        LED RGB   8B [3]   MTG – “G”
921      22     61        Generic        LED RGB   8B [3]   MTG – “G”
922      22     64        Generic        LED RGB   8B [3]   MTG – “G”
923      22     67        Generic        LED RGB   8B [3]   MTG – “G”
924      22     70        Generic        LED RGB   8B [3]   MTG – “G”
925      22     73        Generic        LED RGB   8B [3]   MTG – “G”
926      22     76        Generic        LED RGB   8B [3]   MTG – “G”
927      22     79        Generic        LED RGB   8B [3]   MTG – “G”
```

Corporate Headquarters  Middleton, WI, USA  Tel +608 831 4116  Service (Americas) service@etcconnect.com
London, UK  Tel +44 (0)20 8896 1000  Service (UK) service@etceurope.com
Holzkirchen, DE  Tel +49 (80 24) 47 00-0  Service (DE) techserv-hoki@etcconnect.com
Hong Kong  Tel + 852 2799 1220  Service (Asia) service@etcasia.com
Paris, FR +33 1 4243 3535
Web etcconnect.com  © 2021 Electronic Theatre Controls, Inc.  Trademark and patent info: etcconnect.com/ip
Product information and specifications subject to change. ETC intends this document to be provided in its entirety.

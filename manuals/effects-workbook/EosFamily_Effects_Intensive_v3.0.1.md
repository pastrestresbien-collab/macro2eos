# Eos Family Effects Intensive Workbook (v3.0.1B)

- Source : PDF officiel ETC, « Eos Family Effects Intensive Workbook (v3.0.1B) », V3.0.1B, publié 2021-07
- Fichier source : [`source/EosFamily_ET_Effects_INT_Wrkbk.pdf`](source/EosFamily_ET_Effects_INT_Wrkbk.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select


Eos Family Effects Intensive

                   Workbook

                           V3.0.1B

     www.etcconnect.com/education

                       Released: 2021-07

Table of Contents

           ETC permits the reproduction of materials in this manual only for non-commercial
             purposes. All other rights are reserved by ETC

           Graphics courtesy of David Kane
           .

2    Eos Family Effects Intensive

## Purpose of the Class

    Eos Family Intensive Classes are not entry-level training courses. They
    are fast-paced, feature-focused sessions designed for users with an
    enhanced knowledge of the desk. Instructors will expect attendees to
    be competent in full system navigation, speedy keypad operation,
    move-fade philosophy, referenced data structures, and intermediate
    knowledge of the topics being covered. Unlike other classes, the class
    will move very quickly. Once created, your assignments will be shared
    with the class and assessed, in order to provide constructive feedback
    to grow your skills in the topics being covered.

### LEARNING OBJECTIVES:

       After completing the Effects class, one should be able to:
       - Create any of the five Effect types and be able to modify an Effect’s
              parameters
       - Apply Effects to channels or groups and record to both subs and cues
       - Build an Effects library or show file for future use
       - Configure Faders to control Effects or the parameters of the Effects
       - Override Effects in cues or presets at the Effect level, cue level or
              channel level

### SYNTAX ANNOTATION

       - Bold                           Browser menus
       - [Brackets]                     Face panel buttons
       - {Braces}                       Softkeys and direct selects
       - <Angle brackets>               Optional keys
       - [Next] & [Last]                Press & hold simultaneously
       - «Direct Select»                Direct Select button press
       - MS Object                    Object on a Magic Sheet

### HELP

       Press and hold [Help] and press any key to see:
       - the name of the key
       - a description of what the key enables you to do
       - syntax examples for using the key (if applicable)

              As with hard keys, the “press and hold [Help]” action can be also used with
              softkeys and clickable buttons

### THE MANUAL

       The manual is available on the console, Tab #100.

           Click on Add-a-Tab (the {+} sign), select Manual

               Hold [Tab] & press [100]

       Please note that it is not available on Windows XP devices or on Mac
       computers but is available as a download from the web site.

## Unit 1 – Intro Test

Start with one of the following show files:

### “EOS FAMILY EXPERT TOPICS – EFFECTS – REVA.ESF3D, .ESF2 OR .ESF”

### INTRO TEST - GETTING FAMILIAR WITH THE FILE & RIG

Take 10 minutes to learn the venue rig and the file.
- Familiarize yourself with the magic sheet navigation.
- What building blocks already exist that we can use to build
   effects?
    - Color Palettes
    - Focus Palettes
    - Beam Palettes
- Take note of the effects magic sheet page. These are the types of
    effects we will be covering today.

### INTRO TEST - BUILD AN COLOR EFFECT

You have 20 minutes to build a color effect, effect 400
- Build a color effect that fades between red, violet, and turquoise
   across the Cyc Top (Group 301).
- You may not use any effects that already exist in the file.
- Record the Effect in Cue 401/1.
- Stop the effect in Cue 401/2.

### LET’S TALK

- How did you go about building the effect?
    Did you use an absolute effect? You should.
- Did you struggle?
    Let’s build Effect 400.1 together – absolute color effect and build the three
    cues
- How do you stop an effect running in a cue?
        [Group] [301] [Stop Effect] [Enter] or [Effect] [Enter]

        [Effect] [400] [.] [1] [Stop Effect] [Enter] or {At] [Enter]

        Effect 400.1 : R/V/Tq
```text
          Action        Param             Step Time          Time      Dwell             Level
            1                                (1)               1        0            CP 9021 (Red)
            2                                (1)               1        0           CP 9034 (Violet)
             3                                (1)              1        0       CP 9028 (Turquoise)

4       Eos Family Effects Intensive
```

## Unit 2 – Step-based Effects

        [Effect] [Effect]                                                                  Open the Effect Editor

        [401] [Enter]                                                                      To create Effect 401

    There are just three types of effects. Step-based, Absolute, and Relative.
    Focus, Linear, and Color are Relative effects.
        {StepBased} softkey or touchscreen [Enter]                                         To select Step-based

### WHAT IS A STEP-BASED EFFECT?

    - Step-based effects are a way to build chases across specific
           channels
    - Steps have a defined on-state and off-state which allows you to
           specify exactly what a channel does at every point in the effect. No
           other type of effect has this.
    - Not transferrable to other channels.
    - They are not as flexible as other effects, but their rigidity allows
           you be incredibly detailed
    - You can specify a specific channel order as well as use the same
           channel multiple times
    - Steps cumulatively make cycle time, which will proportionally
           modify the effect when edited.
    - The power of a Step-based effect lives in Step Time
           - Step Time is the time from triggering the current step to triggering the
                next step…how long on the “go”
           - It gives you control of positive or negative space in the relationship
                between step time and total in/dwell/out time. Larger step time =
                more air between steps. Smaller step time = overlap between steps

- Default timing is Step Time 1, In Time 1, Dwell Time 0, Decay Time
    - This creates a rolling wave-like effect
    - When the Step Time matches the In Time, the next step goes as soon
        as the previous step peaks into the dwell. The first step is complete as
        the second step reaches its dwell
    - You can then modify each individual time for specific steps/channels
        from there for a unique, specific effect.

6    Eos Family Effects Intensive

### CREATE A SIMPLE STEP-BASED EFFECT

    We have already created effect 401, and selected Step-based.
    Now we are going to edit it
     [Label] Front Chase [Enter]
                                                                                            Second Enter to confirm the creation of 5
     {Step} [1] [Thru] [5] [Enter] [Enter]
                                                                                            steps
     With all 5 steps selected, [Page►] to the Channels column

     [1] [Thru] [5] [Enter]

                                                                                            Notice how it goes in order through
     [Live] [Recall From] [Effect] [401] [Enter]
                                                                                            channels 1 through 5
                                                                                            to apply the effect on a random channel
     [1] [Thru] [5] [Offset] [Random] [Effect] [401] [Enter]
                                                                                            order

        It still runs in order channels 1 thru 5 because it is following the set order in
        the effect.

     [101] [Thru] [105] [Effect] [401] [Enter]

        Error: No channels were modified. This effect only applies to channels 1
        thru 5.

     [Record] [401] [/] [3] [Label] Front Chase [Enter]

     [Group] [301] (Cyc) [Out]                                                              To see only channels 1 through 5

     [Record] [401] [/] [4] [Label] Cyc Out [Enter]

### EFFECT MODIFIERS

 [Effect] [Effect]                                                                  Open the Effect Editor again

Let’s look at the options on the right in the CIA

### TYPE

    The type of effect. Currently looking at a step-based

### CYCLE TIME

    The time it takes to complete all the steps in the table. If you change this
    time, it will proportionally change all the times in the steps.
                                                                                    Watch how the changes affect the
        Change the Cycle Time to 1. Change it to 3.
                                                                                    effect

### DURATION

    How long the effect runs until stopping.
                                                                                    Watch how the effect runs for 2
        Change the Duration to 2.
                                                                                    seconds before stopping

          Note that the command line says Duration 0:02. Maybe you have a
          flicker and you want it to run for 1.5 seconds. You would use duration.
    Other options under duration include:
    - Num Cycles: Number of completed cycles before stopping.
                                                                                    Restart the effect in Live to see it run for
            Change Num Cycles to 1.
                                                                                    1 cycle before stopping

          Want a one-time ripple across the stage. Do 1 cycle.
    - Infinite: Runs infinitely until you tell it to stop. This is default.
            Change Num Cycles back to Infinite                                      Restart the effect again in Live

### PARAMETERS

    Specifies the fixture parameters that will be involved in this effect such as
    Pan, Tilt, Cyan, Red, Zoom…

### ATTRIBUTES

    - Forward: This is the default. Steps run forward 1-5
    - Reverse: Steps run backwards 5-1. Set to Reverse
            Select Reverse.

    - Bounce: Steps run forwards, then backwards: 1, 2, 3, 4, 5, 4, 3, 2, 1.
            Select Bounce.                                                          Watch the effect for a bit

            Deselect Bounce and select Forward

    - Random Group: Step order is applied continuously randomly.
            Select Random Group.        Watch for a bit.   Deselect Random Group

    - Random Rate: This overrides the rate/cycle time off the effect. It is
          applied in a range.
            Select Random Rate                                                      Watch the effect for a bit

            [50] [Thru] [150] [Enter]

          This randomizes the rate between steps, and is great for flickers
            Select Random Rate and hit [Enter] without entering a value             To reset or remove the random rate

8   Eos Family Effects Intensive

      - Build: Keeps each step’s value at its on state even when the step isn’t
             active. It adds each step until it gets to the last step, and then turns all
             steps off and starts over.
              Select Build.   Watch for a bit.    Deselect Build.                           A perfect example: a marquee effect

      - Positive: This is the default. The effect runs as programmed. The on
             state is the level when the step is active. The off state is the level when
             the step is inactive
      - Negative: The effect runs inverse. The on state is the level when the
             step is inactive. The off state is the level when the step is active.
              Select Negative.    Watch for a bit.    Select Positive.                      A toggle between the two options

      - Continuous Run: The effect will keep running until there is a stop
             effect command
      - Repeat on Go: The effect will restart every time a new cue is fired,
             and the effect is still running
                                                                                            Restart the effect in Live to see it run for
              Change the Duration – Num Cycles to 1.
                                                                                            1 cycle before stopping
              [Go To Cue] [2] [Enter]

              Hit  (Go) into cue 3                                                         Watch the effect start and play once

              Hit  (Go) again                                                              The effect does not restart

              In Attributes, select Repeat on Go

              [Go To Cue] [3] [Enter]

              Hit  (Go) into cue 4                                                         The effect repeats on the Go of cue 4

### ENTRY

      How the effect starts / how the channels enter the effect. We will talk
      about most of the entry & exit types when we get to other types of effects
      - Entry Time – the length of time for the channels to enter the effect.
             Notice how the default is Cue/Sub. This means the effect fades in
             using the time of the cue/sub it is recorded into.
                                                                                            The effect fades up in 2 seconds, the
              [Go To Cue] [2] [Enter]    Hit  (Go) into cue 3
                                                                                            time of Cue 3
              Change the Entry Time to 0
                                                                                            The effect starts immediately following
              [Go To Cue] [2] [Enter]    Hit  (Go) into cue 3
                                                                                            the entry time of 0

### EXIT

      How the effect ends/ how the channels exit the effect.
      - Exit Time – the length of time for the channels to exit the effect.
             - Stop and Hold: when the effect is exited, channels will halt and
                 stay exactly where the effect left them
             - Stop and Fade: when the effect is exited, channels will stop
                 running the effect where they are and fade to their background
                 state using the exit time.

### QUESTION

We have a problem with our effect. We want a smooth exit. With 1 cycle,
the effect is restarting on channel 1 before abruptly stopping. This is
happening because 0.6 seconds after step 5 starts (Step Time) the effect
cycles back to step 1. The effect doesn’t complete until we get to the off
state of step 5, which is 0.6 seconds after step 1 restarts. What is a way we
could fix this?

### POSSIBLE ANSWERS:

- Set the Exit to Stop & Fade. The effect will stop after step 5 and fade
       to background
- Or Change the step time of step 5 to 1.2. This will mean that step 1
       will not start until step 5 completes if the duration is infinite. If it is set
       to number of cycles, step 5 will finish and the effect will stop before
       step 1 restarts.

### QUESTION

The designer has asked to change this effect. They have said “The lights roll
past the actor (who is CS), like a train passing, and when the actor is lit by
the train they should stay at a glow as the train keeps going. How can we
do this?

### POSSIBLE ANSWER:

- Change the off state of channel 3 to 50. Change the exit to stop and
       hold so channel 3 will remain at 50 and not return to the background
- Note: the effect will restart every time a cue is triggered with it
       applied, which means when the effect restarts in cue 4, channel 3 will
       turn off until step 3 of the effect happens. In this scenario, we would
       probably only want one cue.

### CLEANUP

    [1] [Thru] [5] [Stop Effect] [Enter] or [Effect] [401] [Stop Effect] [Enter]

    [Record] [5] [Label] Stop Front Chase [Enter]                                         Notice Channel 3 is recorded at 50!

       It records the state of the channels when the effect is stopped if stop &
       hold is selected.

10    Eos Family Effects Intensive

## Unit 3 – Absolute Effects

### WHAT IS AN ABSOLUTE EFFECT?

     Absolute effects are sequential actions that channels are to take. Unlike
     Step-based effects, they have no on/off state but rather they define
     progressive behavior from one action to the next. You specify exactly
     what actions you’d like the fixtures to take, in a specific order. Each
     action goes to its level in its timing and awaits further instruction.
     Absolute effects can be applied to any channel (or group of channels in
     any order) that has the parameter specified in the effect. This is the
     power of the absolute effect. It is flexible and universal to any fixture in
     your rig that has the capability to do the effect

### CREATE A SIMPLE ABSOLUTE EFFECT

                                                                                       Open the Effect Editor and create effect
 [Effect] [Effect], then [402] [Enter]
 {Absolute} softkey or touchscreen [Enter]                                             To select Absolute

The default absolute effect has two actions. It basically goes from a
level of 0 to a background level. Very usable as is. Let’s go Live and
apply it!

 [Live]   [Group] [301] [Effect] [402] [Enter]

    This will start the effect on the cyc. Notice we don’t see anything even
    though the effect has started! That’s because this effect goes from 0 to
    background. The background is currently 0, so the lights are going from 0
    to 0…not a very exciting effect

 With Group 301 on the command line, run the level wheel slowly up to full

    The lights fade from 0 to whatever level the channels are at as they are
    being rolled up. This is the beauty of an absolute effect with background as
    a level. It gives you the flexibility to apply the affect and have the lights go
    from where they currently are to a determined level

Let’s look at this effect on different channels!
 Using MS 301 “ML”, FOH Spots (Sola Thtr) (G102) Full (IP5)

 [Effect] [402] [Enter]                                                                The effect works!

    This effect has no channels specified in it, so it can work on any fixtures
    that have intensity

 [Effect] [Effect]
                                                                                       Cyc now goes from 0 to 50, no matter
 Change the level of action 2 to 50 – select Bkgrd, then [50] [Enter]
                                                                                       what level they are at in the background
                                                                                       Effect is running across the cyc from
 [Live]
                                                                                       channels 301 – 312
 [312] [Thru] [301] [Effect] [402] [Enter]                                             Now it runs in the opposite direction.

    This is because absolute effects don’t have channels embedded in the
    effect, so they run on the channels selected, in the order selected.

 [Clear] [Sneak] [Enter]                                                               Remove manual values

12    Eos Family Effects Intensive

### OFFSETTING

     Offsetting with absolute or relative effects allows you to apply the same
     effect across the same channels in a different order.
     Channel order matters. The actions will run across the group of
     channels in the order in which the channels were selected.
     Offsetting macros are incredibly useful. Some common ones are:
     - Reverse
     - Random
     - Mirror In / Mirror Out
     - Num Groups / Chan Per Groups
     - Interleave

     Let’s try some offsetting with pre-existing tools in the show file!
      {Snapshot} [102] or use the Popup Snapshot directory                                  Look at Magic Sheet 8001 “Programmer”

         These are macros for commonly used syntaxes. On the bottom left there
         are a lot of offsetting tools
                                                                                            The Offset tool opens in the CIA, with
      [Group] [301] Offset < > (M8049)
                                                                                            Mirror Out selected
                                                                                            Now it runs from the inside of the cyc to
      [Effect] [402] [Enter]
                                                                                            the outside because of the offset.

         It is the exact same effect but creates a much different look with the same
         effect. Very powerful!
                                                                                            Results in a random ordering of the cyc in
      [Group] [301] Offset Random (M8067) [Effect] [402] [Enter]
                                                                                            the effect.

         It’s a good idea to create different groups of the same channel with
         different orders using the offset tool

      {Snapshot} [104] or use the Popup Snapshot directory                                  Take a look at Magic Sheet 304 “Effects”

      Select the Cyc Tab along the left-hand side

         This Magic Sheet has many different groups with different offsets already

      Cyc Top (G301) [Effect] [Enter]                                                    To stop the effect on the cyc top

       Cells (G303) [Effect] [402] [Enter]

         The effect is now running across the individual cells because we used the
         cells and not the parents. This effect has much more granularity than just
         using the parents. Notice this cyc magic sheet has different offset groups
         for both the parents and the cells.

       Parents (G302) and roll it down & up with the level wheel

         These are the parents of the cells. Each parent (fixture) has 6 cells in it. We
         applied the effect to just the cells, so it is running on the cells and ignoring
         the parents. The parents must be on in order to see the effect. As you roll
         them down, they act as a mini grand master for their cells
         When we first applied the effect to the Cyc top group (group 301) we did
         not specify the cells, and it ran across each fixture with their cells acting as
         one.

 Parents (G302) and roll it up to full

[3] [Out]

[Record] [401] [/] [6] [Time] [0] [Label] Cyc Chase [Enter]

[Go To Cue] [3] [Enter]

 (Go) into cue 4 and quickly (Go) into cue 5                                   not giving the effect time to finish

   Because the effect is stop and hold, channels 1,2,4, & 5 have values from
   the effect

 (Go) into cue 6

   These effect values track.
   So, if we want this cue to send all 5 of these lights to 0, no matter where
   they stopped in the effect…

[Cue] [6] [Assert] [Enter]                                                       Puts an assert on cue 6.

[Go To Cue] [3] [Enter] and rerun the series of cues

14    Eos Family Effects Intensive

### EFFECT MODIFIERS

     Let’s look at some more effect modifiers!

### ENTRY / EXIT

         - Immediate – all channels enter the effect immediately – the Default
                                                                                          The effect starts immediately from the
                 [Go To Cue] [5] [Enter]      (Go) into cue 6      (Stop/Back)
                                                                                          middle of the cyc
         - Cascade – channels enter the effect in selection order
                 [Effect] [Effect]    Change the entry to Cascade
                                                                                          The effect starts on 301.1 and cascades in
                 (Go) into cue 6
                                                                                          across the cyc

         These two modifiers work the same for Exit. When the duration is infinite,
         currently the only option is immediate exit. Once you have a duration or
         number of cycles, you can cascade the exit

### RELATIVE VALUES

         Absolute effects can have relative values as levels. This allows channels to
         change relative to their background state.
         - Background – the background state
         - + Relative Value
         - – Relative Value
         - + Relative %
         - – Relative %
             [403] [Enter] {Absolute} [Label] +30 Intensity [Enter]                       create a new absolute effect
                                                                                          when the channels do this action, they
             Select the level of action 1, [+] [30] [Enter]
                                                                                          will go +30 from the background value

                                                                                          The lights fade from their background (0)
             [Live] [101] [Thru] [105] [Effect] [403] [Enter]
                                                                                          to 30 above their background (30)
                                                                                          The lights fade from their background (50)
             [At] [50] [Enter]
                                                                                          to 30 above their background (80)
                                                                                          The lights go from a level of 30 to 30
             [Effect] [Effect]   Select the level of action 2, [30] [Enter]
                                                                                          above their background (80)
                                                                                          Change the level of action 2 back to
             Select action 2, [At] [Enter]
                                                                                          background

         We want to create an effect that sets the lights to half of where we
         currently are. Any guesses on how to do that?
             [404] [Enter] {Absolute} [Label] Half Intensity [Enter]                      create a new absolute effect
                                                                                          when the channels do this action, they
             Select the level of action 1, [/] [50] [Enter]
                                                                                          will go +30 from the background value
                                                                                          Channels fade from their background (50)
             [Live] [101] [Thru] [105] [Effect] [404] [Enter]                             and go up half that value (75).
                                                                                          This wasn’t what we wanted!

         If we look in the editor, we will see that the level for action 1 reads (+) 50
         percent. We need it to be negative!
                                                                                          Display reads (+) -50 %. Channels fade
             [Effect] [Effect]   Select the level of action 1, [-] [/] [50] [Enter]       from their background (50) to half their
                                                                                          background (25)

### REFERENCES IN ABSOLUTE EFFECTS

One of the powerful things about absolute effects is that the levels of
the actions can be references (palettes/presets) you have already
created. We are working an event for the 4th of July! So of course, we
need to make a Red, White, and Blue effect.

### RED, WHITE, AND BLUE EFFECT

     [405] [Enter] {Absolute} [Label] R/W/B [Enter]                             create a new absolute effect

     On the Magic Sheet, Select the Cyc Tab along the left-hand side

     Select the Level of Action 1, Red (CP9021)                               Action 1 is now the red color palette

     [Page ] to the Level of Action 2

     Open (CP)                                                                Action 2 is now the open state

     [Page ] to the Level of Action 3, Blue (CP9033)
                                                                                Both the intensity effect (402) and this
     [Live]    Cells (G303) [Effect] [405] [Enter]
                                                                                color effect are running.
     [Group] [303] {Intensity} [Effect] [Enter]
                                                                                Stops just the intensity effect
     Or [Effect] [402] [Stop Effect] [Enter]

   This effect has a lot of pink in it for something that should just be red,
   white, and blue! Let’s make it snap between our three colors instead
     [Effect] [Effect]   {Action} [1] [Thru] [3] Enter]                         Selects all three actions at the same time

```text
     [Page ] to the Time column, [0] [Enter]                                   change the time of all three actions to 0
     [Page ] to the Dwell column, [1] [Enter]                                  and the dwell to 1
```

   The lights now snap to each color, remain there for 1 second, and then
   snap to the next color.

16   Eos Family Effects Intensive

### ANOTHER MODIFICATION

       What if we want the lights to go to 70 while they do this? We don’t know
       when we are going to use this effect…maybe we are going to record a cue
       or maybe we are doing our show live and will be manually applying it. No
       matter what, we want the background state of the channels to go to full.
        Have Action 1 selected or highlighted
                                                                                         Inserts a new Action 1 and relabels the
        {Action} [1] {InsrtBefore} [Enter]
                                                                                         others 2 through 4
        [Page ] to the Time column, [0] [Enter], then Level [70] [Enter]

        [Live]    Cells (G303) [Effect] [405] [Enter]                                 Reapply the effect

       We previously had an effect that only affected the color parameters of the
       fixtures. We added intensity, but never applied the effect to the intensity of
       the lights. By reapplying, we are telling the effect to run on all applicable
       parameters
       Action 1: The lights jump to 70, then the color is mathematically divided
       amongst the lights via the next actions and timing. Action 1 again: The
       lights stay at 70.
       This may look like what we want but it isn’t! We are giving more time to
       action 4 – blue. After the channels turn blue, they go back to action 1
       which is to stay at 70. The lights stay blue…they haven’t been told to
       change colors. 1 second after that action starts, action 2 goes and the lights
       snap to red. They spend 1 second in Red & Open, but 2 in Blue.

       We want the lights to spend equal time in each color. How do we fix this?
        [Effect] [Effect]   {Action} [1] [Page ] to the Step Time column, [0] [Enter]

       Change the step time of action 1 to 0. Action 2 will start at the same time
       as action 1. Remember step time is the amount of time until the next action
       starts!
       Channels will jump to 70 and Red, then Open, then Blue.

### EXERCISE:

Noticed that blue looks dimmer than the other colors. When the channels
are blue, the designer has asked us to make them full. The channels should
remain at 70 when they are open and red.

Answer:     Maybe add an action before Blue. The level should be 100. The Time
            and Step Time should be 0

### EXERCISE!

Let’s make another absolute effect 406! We are going to be busking
(creating lighting live) some music and have been asked to make an effect
that takes the channels in whatever color they are currently in, and snaps
between red and that color. We would like it to be a little faster – an overall
cycle time of 0.5 seconds. Go ahead and make that effect.

Answer:     Use the magic sheets to find color palette 9021 – Red. That will be the
            level of action 1. Action 2 should remain as background. The time of
            both steps should be changed to 0. The dwell of both steps should be
            changed to 0.25

Excellent! Let’s look at that on the cyc.
 [Live]    Cells (G303) [Effect] [406] [Enter]

We want this to go from red to Green.
  Cells (G303) Green (CP9027)                                                    That doesn’t look great.

 Blue (CP9033)

This effect is great because it can be applied on top of any color, including
gradients! But now the designer wants it to bounce back and forth – like a
red dot
 [Effect] [Effect]   {Attributes} {Bounce}                                            Not quite right!

    That’s because the effect is bouncing the actions. So now it goes action
    1 – red. Action 2 – background. Action 1 – Red. And so on.
We want the effect to go across all the channels and bounce back.
 Deselect {Bounce} and select {Bounce Channels}                                       That’s it!

 [Live]   [Record] [401] [/] [8] [Label] Bouncing Red [Enter]

18   Eos Family Effects Intensive

### EXERCISE!

       We want a white sparkle effect (407), where the lights jump to full and
       white from wherever they are, linger for a second, and then jump back to
       what they were doing. It’s a sparkle so it should have an element of
       random!
       When done, apply it to the cyc cells. Also apply it to the D60s (Group 200)
       – play around with offsetting.
       Set them in a color at a dim level and apply the effect. Record Q401/9
       labeled white sparkle

       Answer:     The key here is that it should have a random rate. I did 100 > 200. You
                   could also make the choice to have a random group. I chose not to so
                   that I can do that with my grouping…I may want to use this sparkle
                   across a sequential selection.

### CREATE A COMPLEX ABSOLUTE EFFECT

A common effect asked for is a flyout. A flyout has four elements
    1. Lights turn on
    2. Lights tilt up
    3. Lights turn off
    4. Lights reset to tilted down

### FLYOUT USING PRESETS

   There are two ways to make this effect. The first is using presets.
    [Live]   Movers Tab      FOH Spots (G102) {Pan} [0] {Tilt} [0] [Enter] [Out]

    [Group] [102] {Focus} {Intensity} [Record] [Preset] [408.1] [Label] Down/Off
    [Enter]

    FOH Spots(G102) [Full] [Enter]. point them at the top of the proscenium

    [Group] [102] {Focus} {Intensity} [Record] [Preset] [408.2] [Label] Up/On
    [Enter]

    [Effect] [Effect]   [408] [Enter] {Absolute} [Label] Preset Flyout [Enter]

    Action 1 should be the Down/Off Preset (408.1)
                                                                                     Both have the default time of 1 and dwell
    Action 2 should be the Up/On Preset (408.2)
                                                                                     of 0
    [Live]   FOH Spots (G102) [Effect] [408] [Enter]                               This isn’t quite what we want

       We can see the lights fade out as the move down to reset. They need
       to go out first
    [Effect] [Effect]   {Action} [3] [Enter]   [Enter]

    Time and Step Time = 0.5, Dwell = 1, Level = 0

   As soon the lights finish turning off, they reset to the down position –
   action 1. The intensity of 0 dwells for 1 second as that reset happens in 1
   second.
   This is a fun effect to see with all the lights doing this together. How do we
   do this?
    {Grouping} {1} [Enter]

    [Live]   FOH Spots (G102) [Stop Effect] [Enter] [Home] [Enter]

20   Eos Family Effects Intensive

### FLYOUT USING PARAMETERS

       We can specify parameters the effect applies to. You can do that on a per
       effect basis in the overall params section, or on a per action basis.
       The second way to make this effect is to use absolute values. The
       advantage is this allows any lights with Tilt & Intensity to use this effect.
        [Effect] [Effect]       [409] [Enter] {Absolute} [Label] Relative Flyout [Enter]

        In Params on the right of the CIA, select Intens & Tilt

### REMEMBER OUR 4 STEPS TO A FLYOUT!

            1.   Lights turn on in their current location

                  Action 1: Param = Intens, Level = 100                                    Lights on in current postion.

                  Step Time = 0,                                                           We want it to have its background tilt at
                                                                                           the same time
                  Time = 0                                                                 We want it to snap

                  Dwell = 4                                                                The overall time tilting will be 4 seconds.
                                                                                           The lights should stay on this whole time
                  Action 2: Level = Bkgrd, Param = Tilt

                  Step Time, Time, and Dwell = 0                                           Ensures Tilt is at its background level

            2.   Lights tilt up

                  Action 3: Level = - 100, Param = Tilt

                  Time = 3.5.                                                              A nice movement up, not too fast

                  Dwell = 0.5.                                                             Let it linger at the top for a bit. Gives the
                                                                                           effect a breath
                  Step Time = 2.5.                                                         A second before it reaches the top, begin
                                                                                           the next action and start fading out
            3.   Lights Turn off

                  Action 4: Level = 0, Param = Intens

                  Time = 0.5                                                               Quick out

                  Dwell = 1.5                                                              Gives the effect a breath and the lights
                                                                                           time to reset
                  Step Time = 0.75                                                         The lights are comfortably off. Start the
                                                                                           next action and reset
            4.   Lights reset

                  Action 5: Level = Bkgrd, Param = Tilt

                  Time = 0                                                                 Move as fast as possible

                  Dwell = 0                                                                This doesn’t need a dwell. Action 2
                                                                                           reinforces the lights tilt at background
                  Step Time = 1.5                                                          Gives the lights time to reset

        [Live]    FOH Spots (G102) [Effect] [409] [Enter]

        Cyc Tab -  Cells (G303) [Stop Effect] [Out]                                     Sparkle effect still running from exercise

        LED Fixtures Tab - Top D60 (G200) [Stop Effect] [Out]                            Sparkle effect still running from exercise

        [Record] [401/10] [Label] Flyout [Enter]

### BREAK MODE

Break Mode is an effects attribute. When the number of channels is
greater than the number of steps in an effect, each channel will cycle
through each step and then wait in the last action until the last channel
enters the last action.
- Each channel does each action, then waits and repeats
- The last action becomes the “background” as the other actions
    chase over.

### TRAILING STAR

   Let’s say the designer wants an effect that looks like a star across a row of
   the back-wall pixels. They want it to snap to pink front and then fade to a
   longer yellow tail, before fading into the background
     [Effect] [Effect]   [410] [Enter] {Absolute} [Label] Trailing Star [Enter]

     Action 1: Level = Pink (CP 9038). Time = 0, Dwell = 1

     Action 2: Level = Yellow (CP 9025). Time = 1, Dwell = 1

     Action 3: Level = Bkgrd. Time = 1, Dwell = 1

     [Live], on the Cyc Tab, click the Pixel Wall Expand Button on the far right

     All (G700) Full (IP5) Collapse    Blue (CP9033)                        Turns all the pixels to full and in blue

     Back on the Pixel Wall MS,  (G732) [Effect] [410] [Enter]

   Yikes! That wasn’t what we wanted! Each channel is cycling through pink,
   yellow, then background evenly. They aren’t waiting for all channels to
   complete the effect.
     [Effect] [Effect]   {Attribute} {Break Mode}                                   That’s a short little tail!

   To increase the yellow, add more yellow steps.
     Action 1: Level = Pink (CP 9038). Time = 0, Dwell = 1

     Action 2 - 6: Level = Yellow (CP 9025). Time = 1, Dwell = 1

     Action 7: Level = Bkgrd. Time = 1, Dwell = 1

     [Live],  (G732) [Effect] [410] [Enter]                                      Great, it has a longer yellow tail now, but
                                                                                    it feels way too slow for a trailing star
     [Effect] [Effect]   {Cycle Time} [0.5] [Enter]

   If you’d like to do this on more than 1 row of pixels, make duplicate effects.
     [Effect] [410] [Copy To] [410.1] [Enter] [Label] Trailing star 2 [Enter]

     [Live]  (G783) [Effect] [410.1] [Enter]

     [Record] [11] [Label] Trailing Star [Enter]

22    Eos Family Effects Intensive

## Unit 4 – Relative Effect

### WHAT IS A RELATIVE EFFECT?

     A relative effect is a mathematical offset from the current state of a
     channel parameter. Like absolute effects, they can be applied to any
     channel that has the parameter specified in the effect, or directly to a
     channel parameter via the command line.
     There are three type of Relative Effects: Focus, Color, and Linear. There
     are 18 “stock” effects preprogrammed in Eos: Effects 901 – 918. All
     are relative.

### LINEAR EFFECTS

        A Linear Effect is a linear diagram or waveform applied to a parameter over
        time. It does not have to be parameter specific. It can just be a linear
        diagram that can be applied to any parameter
          [Effect] [Effect]   [411] [Enter] {Linear} [Label] Intensity Wave [Enter]

          [Live], All (G700) [Stop Effect] [Enter]        FOH Spots (G102) [Stop Effect]
          [Enter]

        The default for a relative effect is intensity over time
        The default waveform is a sine wave. The values fade up to its highest
        value, and immediately after peaking fades down to its lowest value and
        continues in that way.
        The value of the parameter at the X axis (Time axis) is the background. The
        channel will follow the waveform above and below that point based on the
        scale of the effect
        Scale allows you to say how far away the effect moves from the current
        state of the light. The default is 25

          [Live], [31] [Thru] [47] [Effect] [411] [Enter]                                      Applies the effect

          Open (CP)

        Notice how the channels are going from 0 to 25 to 0, and then holding
        there before starting over
        The lights are trying to go 25 above and below the background. They are
        going from 0 to +25 (25) down to 0 – 25 (still 0). So, they are just stopping
        at 0.

 [Full] [Enter]

The same issue is happening but on the positive side of the effect. The
lights are staying at full for half the effect, before fading down to 75 and
back up
 [At] [50] [Enter]                                                              The lights are going from 25 to 75

 [At] [0] [Enter]                                                               It is easier to see the grouping & trail this
                                                                                way

 [Effect] [Effect], in Effect 411   {Scale} [50] [Enter]                        The lights are going from 0 to 50

 {Scale} [10] [Enter]                                                           The lights are going from -10 to 10.

 {Scale} [25] [Enter]                                                           To reset

### GROUPING

    To determine how the channels currently running the effect are
    grouped. This is only for absolute and relative effects

    Defaults to Spread. Every channel the effect is applied to will act as an
    individual element, moving through the effect sequentially based on
    the channel selection order. Note: subgrouping still holds. A subgroup
    in a group will act as an individual channel.
    You can do grouping 0 through 2000. Grouping 0 is spread.

24   Eos Family Effects Intensive

             Set {Grouping} to {2}

            Every other channel (or subgroup) running the effect will move
            together through the effect – 2 cars evenly divided across the effect

             Set {Grouping} to {4}

            Every fourth channel (or subgroup) running the effect will move
            together through the effect – 4 cars evenly divided across the effect

             Set {Grouping} to {20}

            Every twentieth channel (or subgroup) running the effect will move
            together through the effect – 20 cars evenly divided across the effect
            This grouping number is larger than the number of channels in the
            effect. The effect still leaves the space for those extra 3 groups. This
            makes a larger

             Set {Grouping} to {1}

            Every channel running the effect will move together through the effect
            – 1 car
             Set {Grouping} back to {Spread}

### TRAIL

Trail determines how channels are to follow each other through the
effect.
-      It is a percentage of the cycle time
-      It can be any value from 0-200% - what percentage through the
       effect the first channel/group is before the next one starts
-      When the first group is n% through the effect, the second group
       will start, and so on through the remaining groups. The groups
       trail n% behind each other as a percentage of the cycle time
-      Can also be even or solo
Trail is like traffic! How far apart the channels, or “cars” are following
each other on the road.

### EVEN

The groups will be distributed evenly throughout the effect pattern.
Cycle time of the effect divided by number of groups of channels

### SOLO

The first group will do the entire effect on its own. The next group will
start when the previous has finished. One at a time!

50%

When the first group is 50% through the effect, the second group will
start, and so on through the remaining groups. The groups trail 50%
behind each other as a percentage of the cycle time

26   Eos Family Effects Intensive

            25%

            When the first group is 25% through the effect, the second group will
            start, and so on through the remaining groups. The groups trail 25%
            behind each other as a percentage of the cycle time

            10%

            When the first group is 10% through the effect, the second group will
            start, and so on through the remaining groups. The groups trail 10%
            behind each other as a percentage of the cycle time

        Set {Trail} back to {Even}
                                                                                    If the effect is only applied manually,
        [Live], [31] [Thru] [47] [Sneak] [Enter]
                                                                                    sneak will stop it

       Effect 411 can be applied to more than just a channels’ intensity. If no
       parameter is specified, it will default to intensity
        Side Spots (G105) [Full] [Enter]
                                                                                    Apply the effect to their Tilt parameter - is
        Side Spots (G105) {Tilt} [Effect] [411] [Enter]
                                                                                    following the sine waveform!
                                                                                    Apply the effect to zoom - is also
        Side Spots (G105) {Zoom} [Effect] [411] [Enter]
                                                                                    following the sine waveform!
        Side Spots (G105) [Sneak] [Enter]

### CREATE A LINEAR FLICKER EFFECT

 [Effect] [Effect]   [412] [Enter] {Linear} [Label] Intensity Flicker [Enter]

 {Edit}                                                                         To access the form editor

We want to change the pattern to a Flicker! There are several premade.
 {Patterns}

The NTX Flickers are great for this. There are three…NTX Flicker, NTX Fire,
and NTX Lightning.
 Second row, last three options: Toggle between these three.

 Select NTX Flicker (first of the three)

This flicker defaults to being in the top half of the grid, above time. This
means it will only flicker above the background level. We would like it to
flicker above and below the background level
 {Move} and drag the entire effect down so it is centered on the X axis
                                                                                To alter the form of the effect – expand or
 {Form} and drag up and down
                                                                                condense it
    {Undo}     {Redo}                                                           Can undo and redo changes made
                                                                                You will lose the changes if you don’t hit
 Don’t forget to hit {Apply}
                                                                                apply

Flickers like to be random! Let’s change some attributes
 {Attributes} {Random Group}

 {Random Rate} [50] [Thru] [200] [Enter]

 [Live]   OH Spots (G103) [Effect] [412] [Enter]

 USC X (FP112)     Medium Zoom (BP9043)

 Play with intensity on the wheel to see what feels good.                       Maybe around 20

 [Record] [12] [Label] Spots Flicker [Enter]

 OH Spots (G103) [Stop Effect] [Enter]       [Home] [Enter]

28   Eos Family Effects Intensive

### CREATE LINEAR FX 413 – INTENSITY FIRE FLICKER

       We would like to make another flicker effect. This time, we don’t want it
       quite so jumpy. It’s going to function as a less intense candle flicker and
       could also be used as a fire flicker. Let’s look at some of our other options.

        [Effect] [Effect]     [413] [Enter] {Linear} [Label] Intensity Fire Flicker [Enter]

        {Edit}   {Patterns}     {Random (Many Points)} Bottom row, second option

       This is a great start! What if we want to edit it a little more specifically?
        {Select} and choose one point on the drawing                                          White dot turns red

        {Move} and drag up and down                                                           Move the point up to create a higher peak

        {Select} and choose two points on the drawing                                         Two red dots in line

        {Subdivide}                                                                           Adds a point halfway between two points

        {Select} and choose new point and {Remove}                                            To get rid of the new point

        Don’t forget to {Apply}!

        [Live]   OH Spots (G103) [Effect] [Enter]        [Out]

        FOH Spots (G102) [Effect] [413] [Enter]        [At] [50] [Enter]

        Tip them up to the cyc so we can see them

### LINEAR EFFECTS WITH NON-INTENSITY PARAMETERS

Other effective fire flicker effects involve color parameters. In RGB lights,
quickly adjusting the green parameter will allow the fixture to flicker to
different hues of red, orange, and yellow. Magenta will do the same in
CMY Effects.
 [Effect] [Effect]     [414] [Enter] {Linear} [Label] Color Fire Flicker [Enter]

 {Parameters}        {Green}   {Magenta} [Enter]

 {Edit]     {Clear All}   {Draw}   draw a spikey effect      {Smooth}               To draw your own pattern – don’t like it?

 {Patterns}     {Random (Many Points)}        {Random (Many Points)}…               Keep clicking until you find one you like!

 {Apply}!

The scale is currently default 25. That’s large to apply to magenta.
 {Scale} [10] [Enter]                                                               More subtle

As this is another flicker, Let’s do some random!
 {Attributes}     {Random Rate} [50] [Thru] [200] [Enter]

 [Live]     FOH Spots (G102)      Orange (CP9022)      [Effect] [414] [Enter]   Automatically applied to magenta

30   Eos Family Effects Intensive

### EXERCISE

       This is looking good! We often find fire effects are more realistic if there is
       movement on the top as if the fire is growing and shrinking. Let’s play with
       a shutter effect! The top shutter is Shutter A
       Create effect 415 that moves the top shutter in/out and waves the angle,
       so it looks like the top of the beam is waving like the fire
       growing/shrinking.

       Possible Answer: Create linear effect 415 labeled Shutter A Wave – All we must do
                  is change the parameter to Angle A and Thrust A

                                                                                           The top shutter waves in and out, adding
        [Live]    FOH Spots (G102)      [Effect] [415] [Enter]
                                                                                           to the feeling of fire

       What’s one more thing we could add? Hint – it isn’t an effect
       Don’t forget normal non intensity parameters! Sometimes the simplest
       things are the most effective.
        [Live]    FOH Spots (G102)      Fire (BP9021.6)                                Add the gobo to the scene

        1 Rotate (BP9122)       >  (BP9127)                                            Slowly rotate to the rights

        E-40 (BP9023)                                                                    Soften the edge a bit

        [Record] [401] [/] [13] [Label] [Fire] [Enter]

### LET’S MAKE ONE MORE LINEAR EFFECT!

             [Effect] [Effect]   [416] [Enter] {Linear} [Label] Pan Wave [Enter]

             {Parameters} {Pan} [Enter]

             [Live]   FOH Spots (G102) [Home] [Enter]        [Stop Effect] [Enter]       Stops all the effects

             FOH Spots (G102) [Effect] [416] [Enter]                                     Only Pan is affected, moving positive and
                                                                                           negative relative to its current location

            It is a great effect to make the lights look like they are scanning

### FOCUS EFFECTS

A Focus Effect impacts a channel’s pan and tilt parameters. It is Pan/Tilt
instead of a parameter over time. This creates a shape on the graph that
the fixtures follow. The Default is a circle
 [Effect] [Effect]   [417] [Enter] {Focus} [Label] Circle [Enter]

Scale applies to a focus effect just as it does to a linear effect. In the focus
effect, scale is how much positive & negative pan/tilt is applied to the
channels.
 [Live]   FOH Spots (G102) [Stop Effect] [Enter]                                 Stop all the effects on the FOH movers

 [Effect] [417] [Enter]

 [Effect] [Effect]   {Scale} [10] [Enter]                                          The fixtures move less – not as far away
                                                                                   from their background position
                                                                                   Now circle around the singer – their new
 [Live]   FOH Spots (G102) Singer (FP118)
                                                                                   background position.

### GROUPING

    When the grouping is spread, the channels travel as individual “cars”
    around the effect, as shown on the left below.

     Set {Grouping} to {2}

    When the grouping is 2, the channels work in two groups evenly (if the
    trail is even) around the effect, as shown on the right above.

     Set {Grouping} back to {Spread}

32   Eos Family Effects Intensive

### TRAIL

            Remember, trail is like the traffic. It is how close the “cars" are
            following each other
             Change {Trail} to {10% 0.5s}

             Change {Trail} to {Even} [Enter] and {Scale} to [25] [Enter]

             [Live]   FOH Spots (G102) [Stop Effect] [Enter]                              Stop all the effects on the FOH movers

             [Record] [401] [/] [14] [Label] Singer [Enter]

             FOH Spots (G102) [Effect] [417] [Enter]                                      The fixtures move less – not as far away
                                                                                            from their background position
             [Record] [401] [/] [15] [Time] [5] [Label] Singer Circle [Enter]               Now circle around the singer – their new
                                                                                            background position.

### MORE ENTRY/EXIT ATTRIBUTES

            ENTRY: Entry refers to how the channels enter/start the effect.
            -   Cascade or Immediate: channels enter according to the trail and
                cycle time values or all channels enter the effect instantaneously.
            -   Fade By Size: This is the default. The effect will achieve its full
                value as allowed by the effect using the entry time. In relative
                effects, this refers to scale, starting at 0 and growing to its full
                scale using the entry time.
            -   Fade By Size & Rate: achieves its full values as allowed by the
                effect and ramp up from a rate of 0 to full speed using the entry
                time
            -   Fade By Rate: increases the rate of the effect as it enters. The
                rate will be 0 and increase to effect value using the entry time
            -   Entry Time: the length of time for channels to enter the effect
            EXIT: Exit refers to how the channels exit or stop the effect.
            -   Fade By Size & Rate: when the effect is exited, channels will
                stop running the effect and return to their background state using
                the exit time.
            -   Fade by Size: values will return to their background state using
                the exit time. In relative effects, this again refers to scale, the scale
                will be at the effect value and shrink to 0 using exit time
            -   Fade by Rate: decreases the rate of the effect as it exits
            -   Stop and Hold: channels will halt and stay exactly where the
                effect left them (We looked at this in step-based effects!)
            -   Stop and Fade: channels will stop running the effect where they
                are and fade to their background state using the exit time.
                (Again, we looked at this in step-based effects!)
           -    Exit Time: the length of time for channels to exit the effect

### LET’S LOOK AT THE DIFFERENT STYLES OF ENTRY

     [Live]     [Go To Cue] [14] [Enter]       (Go)                                      Lights start the effect at full speed,
                                                                                          gradually moving from a scale of 0 (on the
                                                                                          singer) out to its effect scale over 5 seconds
     Change {Entry} to {Fade by Rate}           [Go To Cue] [14] [Enter]       (Go)      Lights jump out to their effect scale and
                                                                                          ramp up from stopped to the effect rate
                                                                                          over 5 seconds
     Change to {Fade by Size & Rate}            [Go To Cue] [14] [Enter]       (Go)      Lights move from a scale of 0 (on the
                                                                                          singer) to their effect scale, ramping up
                                                                                          from a rate of 0 to the effect rate over 5
                                                                                          seconds

### EFFECT FORM EDITOR WITH FOCUS EFFECTS.

     [Effect] [Effect]

     [418] [Enter] {Focus} [Label] [Label] Focus Pattern [Enter]                          2nd Label to clear default label

     [Live]     FOH Spots (G102) [Effect] [418] [Enter]

     [Effect] [Effect]      {Edit}

     {Patterns}     {Infinity} (Figure 8) Second row, second option
                                                                                          Careful! If you reach the edges of the
     {Scale}     select the object and resize it
                                                                                          graph, the shape flattens out!
     {Rotate}     select the object and adjust the angle of the object

     {Mirror Hor}        {Mirror Vert}                                                    Shape is mirrored horizontally or vertically

     {Apply}!

### ENCODERS

    Your encoders have some attributes on them! Play with them!
    -     Scale
    -     Cycle Time
    -     Horizontal – Horizontal shape. It will flatten or elongate the
          shape horizontally
    -     Vertical – Vertical shape. It will flatten or elongate the shape
          vertically (press and hold shift and horizontal will change to
          vertical)
    -     Axis – Rotate
    Edit the effect again. Clear out the pattern and draw your own shape!
    Don’t forget to hit {Apply}!

### EXERCISE:

We made effect 416, Pan wave, earlier using a linear effect. We could have
also made it using a focus effect with Pan/Tilt instead. Make an effect
416.1 that makes this pan wave as a focus effect. Apply this effect on the
FOH Movers – Group 102. After

Answer:     Straight Line Focus Effect. This effect is applied to pan and tilt, forcing
            it to just do a pan wave. With the linear pan effect, it is only applied to
            pan. A separate effect can be applied to tilt

34   Eos Family Effects Intensive

### COLOR EFFECTS

       A color effect impacts a channel’s color parameters. Hue and saturation
       offsets are represented in the graph. The default is a circle
       Word of warning! You must enable create virtual HSB in the settings for
       these effects to work!
        [Effect] [Effect]   [419] [Enter] {Color} [Label] [Label] Color FX [Enter]       2nd Label to clear default label

        [Live], LED Fixtures, HS CSpot > (G220) HS CSpot < (G240) Full (IP5)
                                                                                         A nice cool effect centered around blue. It
        [Effect] [419] [Enter]      Blue (CP9033)
                                                                                         looks like water, but predictable…
        [Effect] [Effect]   {Grouping} [5] [Enter]                                       Grouping adds a bit more variety

### SAME EFFECT ON MOVERS

                                                                                         Stops effects on the FOH Movers and
             HS CSpot > (G220) HS CSpot < (G240) [Stop Effect] [Enter]       [Out]
                                                                                         turns them off
             Movers OH Spot (Sola 750) (G103) Full (IP5) House (FP116)

             [Effect] [419] [Enter]

            This is a multicolored pastel look. Maybe more vibrant and fun.
             Lavender (CP9035)                                                         A little more like Cotton Candy!

### RAINBOW EFFECTS!

            There are two rainbow effects in the console already: Effect 917 –
            Rainbow RGB and Effect 918 – Rainbow CMY. They are relative effects
            using the named parameters.

### EFFECT 917 – RGB

            This effect takes Red, Green, and Blue and fades them to -100 of
            current value, dwells there, and then fades up to 0. The Eos stock
            effect staggers these parameters to create a rainbow. If we were to
            make this effect, all three would be affected together, essentially
            making an intensity effect doing color

      [Live], Cyc,   Cyc Top (G301)       under Home, Color (M103)
                                                                                        A rainbow effect starts on the cyc. But it
      Cells (G303) [Full] [Enter] [Effect] [917] [Enter]
                                                                                        looks pastel

    Amber remains at full. This is an RGB effect, so it only affects the
    parameters red, green, and blue
      Cyc Top (G301)      {Amber} {Min}                                              A more saturated RGB effect now

    Remember, this is relative! Let’s play around with the color
      Workspace 2 on monitor 1 (CIA Monitor)                                            (has the color picker on it)
                                                                                        The cyc changes relative to its current
      Select colors on the color picker
                                                                                        color

### EXERCISE:

These rainbow effects are relative and only apply to specific parameters. I
would like a Rainbow effect 420 that will work on all the color changing
lights in this rig. I would like this effect running together on the cells of
entire cyc (top & bottom) from the outside to the inside. Record Cue
401/17 – Rainbow. Make sure the OH Spots (Group 103) remain in the
house running their effect.

Possible Answer: Absolute effect using color palettes. All the fixtures in this rig
           have data in the color palettes and this effect will work on everything
           recorded in these palettes. It will always be rainbow – it is not relative
           to the current color of the fixtures

            Turn on the cyc bottom (Group 304) and apply this effect to the cells
            >< group (group 315). This mirrors the effect in on the cells of the top
            & bottom together. Record Q401/17 Rainbow

36       Eos Family Effects Intensive

     Unit 5 – An Effects Library
     Programmers will typically have a file that contains effects they have
     built. This is referred to as a library. They are almost exclusively relative
     & absolute effects so they can apply to any fixture type that is
     encountered.
     There are four basic forms that are standard in effects. They can be
     built in relative and absolute effects.
     At their default, relative & absolute effects with the same form will look
     different from each other unless attributes of the effect are changed.
     - Cycle Time
           The absolute effect will default to 2 seconds – there is 1 second per action,
           and 2 actions. This effect will be faster than the relative effect unless
           changed
           The relative effect defaults to 5 seconds. This effect will be slower than the
           relative effect unless changed
     - Level
           The absolute effect defaults to the levels 0 and background. This effect will
           go between 0 as the first action, and the background as the second unless
           changed
           The relative effect defaults to the waveform having positive & negative
           intensity. It will go 25 (default) above and below the background level
           unless changed.

### STANDARD FORMS

### WAVE/SINE

           In this form, the channels fade between levels

### RELATIVE WAVE/SINE

                                                                                               fades between 25 points above & 25
                   [Effect] [Effect] [421] [.] [1] [Enter] {Linear} [Label] Wave Rel [Enter]
                                                                                               points below the background
                   Change the grouping to 1                                                    The effect is easier to see

### ABSOLUTE WAVE/SINE

                   [Effect] [Effect] [421] [.] [2] [Enter] {Absolute} [Label] Wave Abs
                                                                                               fades between 0 and background.
                   [Enter]

                It is a fading wave effect because the time of each action is 1 and the
                dwell is 0 – the actions fade in 1 second before immediately fading to
                the next action in 1 second.
                   Change the grouping to 1                                                    The effect is easier to see

                                                                                 Unit 5 – An Effects Library   37

### STEP/SQUARE

In this form, the channels snap between levels

### RELATIVE STEP/SQUARE

                                                                                 fades between 25 points above & 25
     [Effect] [Effect] [422] [.] [1] [Enter] {Linear} [Label] Step Rel [Enter]
                                                                                 points below the background
     {Edit] {Clear All} {Draw}, draw a line starting Top left to Top
                                                                                 Draw a single step down
     centerline, then to Bottom centerline and finish Bottom left

     {Apply}!                                                                    The result is a square wave

     Change the grouping to 1                                                    The effect is easier to see

### ABSOLUTE STEP/SQUARE

     [422.2] [Enter] {Absolute} [Label] Step Abs [Enter]

    If the lights should step to each value, what should the timing be?
     Both actions should have a Time of 0 and a Dwell of 1

     Change the grouping to 1

### RAMP

In this form, the channels ramp to the first level and snap to the second

### RELATIVE RAMP

     [423] [.] [1] [Enter] {Linear} [Label] Ramp Rel [Enter]

     {Edit]     {Patterns}   {XY Slope} (first row, second option)               A pattern exists for this

     {Apply}!

     Change the grouping to 1                                                    The effect is easier to see

### ABSOLUTE RAMP

     [423] [.] [2] [Enter] {Absolute} [Label] Ramp Abs [Enter]

    If the lights should first fade on and then immediately snaps off, how
    do we do that?
     Action 1 should have a Time of 1 and a Dwell of 0

     Action 2 should have a Time of 0 and a Dwell of 1                           Fades from 0 to background, then ramps
                                                                                 down to 0 and pops up to the background
     Change the grouping to 1

38    Eos Family Effects Intensive

### PULSE/BURST

         In a Pulse/Burst, the channels snap to their first level and fade to the
         second.

### RELATIVE PULSE/BURST

              [424] [.] [1] [Enter] {Linear} [Label] Pulse Rel [Enter]

              {Edit]     {Patterns}   {XY Slope} (first row, second option)           Needs to start up and ramp down

              {Mirror Hor.}                                                           To reverse the ramp

              {Apply}!

              Change the grouping to 1                                                The effect is easier to see

### ABSOLUTE PULSE/BURST

              [424] [.] [2] [Enter] {Absolute} [Label] Pulse Abs [Enter]

             If the lights should first fade on and then immediately snaps off, how
             do we do that?
              Action 1 should have a Time of 0 and a Dwell of 1

              Action 2 should have a Time of 1 and a Dwell of 0                       Fades from 0 to background, then pops
                                                                                      down to 0 and fades up to the
                                                                                      background
              Change the grouping to 1

              [Live], LED Fixtures,    Top D60 (G200) 50% (IP3)

              Under Home        Color (M103)

             Using the effects direct selects on monitor 1 workspace 1, apply each
             of these effects and see how they look
              [Effect] [421] [.] [1] [Enter                                           Applies the Wave/Sine Absolute effect

              [Record] [401] [/] [18] [Label] Breathing Floor [Enter]

     These four basic forms can be applied to any parameter!
                                                                                          Other relative focus effects that
```text
     In the absolute effects, action 2 is typically left as background. Action 1          you may want in your library:
     can then be any palette or preset or an absolute value. It is very                   • Circle        • Square
     common to create color effects with one palette in each of these                     • Triangle      • Figure 8/ bally
     effects. For example, you could create these 4 absolute effects with the             • Pan wave • Tilt wave
```
     color palette 9021 – Red as action 1.
     The relative effects are often applied to parameters like pan, tilt, zoom,
     and iris either via the command line or using parameters in the effect.

## Unit 6 – Pre-existing File Effects

Let’s look at the effects already in the file. This file was built to have a
good base to start with, with a lot of common “effects library” effects.

### FIRE SNAPSHOT 104 – EFFECTS

    This is an example of a magic sheet laid out for effects. It is divided into
    parameter type, so the user can easily find what kind of effect they are
    looking for. There are relative & absolute effects mixed in. There is only one
    step-based effect just to have an example. Step based effects are most
    often show specific, and therefore are not typically included in a library
    page.

### INTENSITY

    The orange buttons on top are intensity effects. They are orange for
    consistency and organization…the console color for intensity palettes is
    orange. They are divided into 3 sections
    - The first section, outlined in yellow, contains relative effects. We went
        over many of these. There are step, wave, pulse, and ramp effects as

40   Eos Family Effects Intensive

            well as a shimmer. There are two of each – one random, and one
            normal.
       - The second section, outlined in red, contains absolute effects. Again,
            we went over these! We have the absolute version of step, wave,
            pulse, and ramp effects both random and not random. Additionally,
            there are some set values/bk (background) effects.
            - You might want different speeds of strobes
            - Might also want a twinkle or shimmer
       - The last section, outlined in gold, are specifically flicker and strobe
            effects. There are both relative and absolute effects here.

### FOCUS

       The Green buttons in the left middle are Focus effects. Similarly, to the
       orange intensity effects, these are green because focus palettes are green in
       the console
       All of these are relative effects with different shapes. Most are Focus
       Pan/Tilt Effects.
       Pan Wave & Tilt wave are linear sine wave effects with the parameter/time.

### BEAM

- The Blue buttons in the right middle are beam effects. Again, these
    buttons are blue because beam palettes are blue in the console
- These are all absolute effects going between two beam palettes –
    small to large. They could have also been created using a linear
    relative effect, so that they are relative to their background values
    instead of only going from their smallest size to largest size
- Like the Intensity effects, we have used two of our basic forms – wave
    and step. However, instead of using random, we have divided by
    grouping –spread and one

### COLOR

Color has the most effects on this magic sheet. The top section has relative
color effects. They are the stock effects included in the file. The buttons are
gray because that is the color that color palettes are assigned in the console
To the right of the relative effects is one step-based effect. It is a bull’s eye
effect, where the D60s change color from the inside out, and then from the
outside in.
The bottom section has four rows of color effects. All of these are absolute
color palette/background effects. The color palette is the color of the
button. The decimal reflects what form and grouping the effect is.
- The effect number reflects the number of the color palette
- The top two rows are step/square effects where the colors snap.
    - The top row (it says 0 on the left) has grouping of spread
    - The bottom row (it says 1 on the left) has a grouping of 1.
- The bottom two rows are wave/sine effects where the colors fade
    - The top row (it says 0 on the left) has grouping of spread
    - The bottom row (it says 1 on the left) has a grouping of 1
- A more complete version of this library would have all four forms –
    wave, step, pulse/burst, and ramp. They would also have more
    groupings. Often Spread, 1, 2,3 or 4, 8, and then a Random grouping.

42   Eos Family Effects Intensive

### SPECIAL FX

       - This small box in the upper right corner has special effects. These are
            the effects in this file that are for a specific purpose, or contain more
            than one parameter
       - Other types of effects might fall into this category that you might
            want in your library
             - Fire & Candle                - Lightning
             - TV/Film Flickers             - Paparazzi
             - Police Car                   - Fireworks
             - Chasing Rainbow              - White Strobes
             - White Shimmers

### CONTROL

       This last section on the bottom left is a control section to control running
       effects It contains virtual faders that are set to global effects rate & size.
       They are divided by color to show which type off effect they are filtered to.
       There is also an overall global effects override
       There are stop effect buttons under the corresponding faders. They are
       specific to the parameter the fader controls.
       There is also a home faders button, which resets and homes these faders.

## Unit 7 – Effects Fader Configuration

### EFFECTS IN SUBMASTERS

### RECORDING AN EFFECT IN A SUBMASTER

   [Live],   [Go To Cue] [401] [/] [18] [Enter] if not already there

   [Live], Movers,    FOH Spots (G102) Full (IP5) Singer (FP118)

   [Effect] [417] (Circle) [Enter]

   [Select Last] [Record] [Sub] [401] [Label] Singer Circle [Enter]

   [Sneak] [Enter]

   [Sub] [401] [Enter] {Properties}, under Exclude, {Record}

   Press & hold [Fader Page] [41]

   Load Sub 401 onto fader 41/1      Top button or both bottom buttons

   Bring up Sub 401

  The fader proportionally controls the parameters of the lights (IFCB), the
  effect rate, and the rate size. This effect has an entry of fade by size and
  rate. If its entry was fade by size, the fader wouldn’t control rate, only
  intensity and size
  With the fader down, the bump button (bottom button) turns on and off
  the effect.

### EFFECT SUB

  An effect sub contains only effect information, not any other parameters.
  The bump button starts the effect and the fader controls the rate/size of
  the effect according to the entry behavior
   Pull the fader down      [Blind] [Sub] [401] [Enter]

  There are values for all parameters of the channels, as well as FX 417 on
  the focus.
   {Properties}, under Mode, {Effect}

  An effect sub only has the effect information. All other channel values are
  removed
   Bring up Sub 401                                                               Nothing happens.

  The effect has started but the lights have no intensity
   [Live], Movers,    FOH Spots (G102) Full (IP5)                           Now can see the effect

  Undo changing the submaster to an effect sub
   {Properties}, under Mode, {Additive}

  Once you change it to an effect sub, you lose the channel’s parameter
  information. Changing it back to additive does not retrieve that information
   [Undo] [Enter]

   Make sure the fader is down and the sub is off

44   Eos Family Effects Intensive

### INTENSITY MASTER

       The Fader on Intensity Master Submaster only controls the intensity of the
       fixtures. The bump button marks the lights. In a submaster that contains an
       effect, the bump button also starts the effect.
       This means that the fader does not control the effect size/rate.
           [Sub] [401] {Properties}, under Master, {Int} (Intensity master)

           With the fader down, press the bottom bump button

       The lights’ non-intensity parameters mark and the effect starts. You can see
       this in the Live Table.
           Bring up the fader (Sub 401)                                                   The fader just controls intensity

       The lights are already marked and running the effect at its full rate & size.

### EFFECTS RATE & SIZE ON FADERS

       Fader configuration allows us to control much more than just submaster.
       There are several tools to aid in effect manipulation
           Workspace 3 on monitor 1 (CIA Monitor)                                         (has a Fader Configuration tab on it)

       This tab shows every fader, laid out by pages. A Page has 10 faders on it.
       This tab is where you assign the faders and associated buttons property
       Each fader is divided into sections you can edit the functions and properties
       of
       - Mapping – what the fader is mapped to. Click this will pop up a menu
              that allows you to specify a target or list of targets to map
       - Size – a fader can be mapped so its content can take up more than 1
              fader. It can have up to 3
       - Configuration – this pops up a menu that will give you additional
              configuration of the properties of the target you have assigned. You
              will see the properties of the content on the fader in this box
       - Filters – we can filter what a fader controls. This is where you set that
       - Fader – this is where you assign the behavior of the fader/slider itself
       - Buttons- there are 3 buttons you can assign functions to. On a
              motorized fader, the load button is on top of the fader. On a non-
              motorized fader, the load button is both the bottom buttons (square
              & triangle) pressed at the same time
       At the top of the tab is a page number.
           Select the Page box, a window pops up, then type [41] [Enter]                  To jump to page 41

       We will see Submaster 401 mapped to fader 41/1. Right now, the Intensity
       master fader is only controlling intensity and we have no way to control the
       rate and the size. Let’s change that
           Select the Size box, a window pops up, and select 3X                           Expands the sub to 3 faders

           Change the second fader to be Effect Size.

           Change the Maximum to 400

       On a motorized fader, the fader jumps to the halfway point. That’s because
       the default size of the effect is 100 – the actual size in the effect. You can
       then adjust it larger or smaller. On a non-motorized fader, you will have to
       put it halfway up yourself.

 Change the third fader to be Effect Rate.

 Change the Maximum to 400

On a motorized fader, the fader jumps to the halfway point. That’s because
the default rate of the effect is 100 – the actual size in the effect. You can
then adjust it larger or smaller. On a non-motorized fader, you will have to
put it halfway up yourself
 Play with the Size and Rate faders!

 Leave the Size and Rate faders at approximately the middle.

 Change the middle  button of the second fader to Start Stop Effect

 Push the button to see how it works. Push it again to restart the effect

Start/Stop Effect will start and stop the effect each time it is pushed. When
stopping, it will stop the effect and snap the lights to the
submaster/background position. When starting, it will start the effect with a
snap
 Change the bottom  button of the second fader to Freeze

 Push the button to freeze the effect. Push it again to restart the effect

Freeze will pause the effect where it is. The lights do not snap back to their
submaster/background value or stop the effect on the channels. It just halts
the effect until the button is pushed again
 Change the bottom  button of the third fader to Solo

 Push and hold the button.      Then release it.

Solo suppresses any intensity values not provided by the content of the
fader while pressed. When released, intensity values are restored

### GLOBAL EFFECTS FADERS

Global Effects Faders master all effects globally. They can be set to effect
size, effect rate, or effect master.
 Click on the Mapping button of fader 41/4 and change it to Global FX.

 Make the size 2x

 Change the first fader (41/4) to Effect Size, min of 0 and max of 400

 Change the second fader (41/5) to Effect Rate, min of 0 and max of 400

 Change the middle  button on the first fader (41/4) to Freeze.

 Play with the Size / Rate faders and Freeze button

Notice how this affects all running effects, regardless of where they get
their information. We currently have effects running in the cue, and from
submaster 401. If we had effects manually applied, this fader would still
affect them
 Press the bottom  button of the first fader – 41/4

This will turn off the global effect fader and it will no longer affect the
channels. Notice it did not reset the faders. If you press the bump button
again the rate & size will be where you left them. For now, keep this fader
off.

46   Eos Family Effects Intensive

### FILTERS

       Filters are incredibly powerful tools that allow you to specify what a fader
       can control. It allows you to get specific and organized with what you are
       controlling. There are several different types of filters that can be applied
           Click on the Configuration area on the Global Effects 2x fader                  A filter area pops up showing all the
                                                                                           possible filters

       - Channel – applying a channel filter limits the fader’s control to just the
             channels specified
       - Parameter – the fader will only affect the specified parameters
       - Submaster – the fader will only affect content controlled by the
             specified submaster
       - Cue list – the fader will only affect content controlled by the specified
             cue list
       - Effect – the fader will only affect the effect specified
       - Manual filter – if this is on, the fader will only affect manual
             information, not stored information
       - The red X’s next to the filters allows you to clear it out

### INTENSITY FILTER ON GLOBAL FX

               Click on the Mapping button of fader 41/6 and change it to Global FX.

               Change the fader (41/6) to {Effect Rate}, min of 0 and max of 400

               Change the middle  button to {Freeze}

               Click on the Configuration area on the Global Effects 2x fader              A filter area pops up showing all the
                                                                                           possible filters
               Click on Param Filter (Parameters)

             This pops up a screen with all parameters you have patched in your
             show file, divided by category. You can pick an entire category using
             the category filters across the top, or you can be as specific as one
             parameter
               Click on the Category Filter {Intensity} along the top

               Play with this fader.                                                       See how it only controls intensity.

### FOCUS FILTER ON GLOBAL FX

             On Global Effects faders filtered to Focus, it is best to make it a size of
             2x so both size and rate are on faders.
               Click on the Mapping button of fader 41/7 and change it to Global FX.

               Make the size 2X

               Change the first fader to {Effect Size}, min of 0 and max of 400

               Change the second fader to {Effect Rate}, min of 0 and max of 400

               Change the middle  button of the first fader to {Freeze}

               Click on the Configuration area on this Global Effects 2x fader (41/7)      A filter area pops up showing all the
                                                                                           possible filters
               Click on Param Filter (Parameters)

               Click on the Category Filter {Focus} along the top

### COLOR FILTER ON GLOBAL FX

     [Shift]&[Clear], hit the load (top) button of Fader 41/6 – Intensity
                                                                                          Posts Fader 41/6 on the command line
     Global FX

     [Copy To] and hit the load (top) button of Fader 41/9                                This copies fader 41/6 to 41/9.

     In the Fader Configuration Tab

     Click on the Configuration area on Fader (41/9)                                      A filter area pops up showing all the
                                                                                          possible filters
     Click on Param Filter (Parameters)

     Change the filtered parameters from Intensity to {Color}

### BEAM FILTER ON GLOBAL FX

     [Shift]&[Clear], hit the load (top) button of Fader 41/9                             Posts Fader 41/6 on the command line

     [Copy To] and hit the load (top) button of Fader 41/10                               This copies fader 41/6 to 41/9.

     In the Fader Configuration Tab

     Click on the Configuration area on Fader 41/10                                       A filter area pops up showing all the
                                                                                          possible filters
     Click on Param Filter (Parameter)

     Change the filtered parameters to {Form} {Image} & {Shutter}                         All the Beam sub-categories

### PLAY WITH ALL THE GLOBAL FX FADERS!

You can control different aspects of the effects. This is great for busking to
music or altering effects on the fly. Filtering to different parameters gives
you finer control

### CHANNEL FILTER

    While playing with the color global effects fader, notice how it is controlling
    both the effect on the cyc, and the one on the movers in the house. These are
    both color effects. What if we don’t want it control the lights in the house? We
    only want it to control the effect on the cyc.

     Click on the Configuration area on Fader 41/9 – the Global FX Fader                  A filter area pops up showing all the
                                                                                          possible filters
     Click on Chan Filter (Channel)

     Workspace 1 on monitor 1, Cyc, select the Cyc All (G307) [Enter]                 Or just type [Group] [307] [Enter]

    Now this fader only applies to the cyc. The cyc is a big system that really affects
    the overall feel of the stage. Sometimes altering just one system is enough to
    really change the mood. Creating Global FX faders filtered to one group of
    channels allows for that specificity

### RELEASE THE FADERS!

When using many global FX faders, it is easy to get lost and have too much
on at a time. Many programmers have a macro to release their faders so
they are homed and no longer affecting content on stage.
Macro 401 already exists that will do just that.
     Back in Fader Config, (Workspace 3 on monitor 1)

     Change the middle  button of the second fader of Fader 41/4 to
     {Macro}, ID # [401] [Enter]

     Press that Macro button                                                              Watch these fader release.

48    Eos Family Effects Intensive

     Unit 8 – Effect Overrides

### EFFECT OVERRIDES IN CUES & PRESETS

     We can edit the effects we make. There are three places we can edit an
     effect: at the Effect Level, at the Cue Level or at the Channel Level

### EFFECT OVERRIDES

        Editing an effect in the effect editor is a global change to the base effect.
        Every time an effect is applied, either manually or from a recorded target,
        the console looks inside the effect itself and applies what it sees there.
         [Effect] [Effect]      [420] [Enter]                                            (Chasing Rainbow)

         Change the Cycle Time from 7 to 2

        The effect on the cyc is now moving with a cycle time of 2. This effect is
        recorded into the cue. The console sees that the effect cycle time has
        changed and adjusts the effect accordingly. Every time this effect is played
        back, it has this new cycle time
         [Live], [Group] [200] [Effect] [420] [Enter]                                    Applies the effect to the D60s

        This effect is applied manually. The D60s are also running with a cycle time
        of 2 because that is the new cycle time of the effect itself.
         [Effect] [Effect].      Change the Cycle Time back from 2 to 7

         [Go To Cue] [Enter]                                                             Restores the cue

### CUE LEVEL OVERRIDES

        We can edit effects on a cue level. These are changes that are applied on
        top of the base effects, in this cue only. This change will not affect the
        base effect
         [Live], [Group] [105] [Full] [Enter]        [Effect] [416] [Enter]              Applies the Pan Wave effect to the Side
                                                                                         Spots
         [Record] [401] [/] [19] [Label} Scanning Sides [Enter]

         From a clear Command line, hit [Effect]                                         The Effect Status Display pops up in the
                                                                                         CIA

        In the Effect Status Display, we can see all the effects running. This display
        shows us the effect number, the channels they are running on (and the
        order they are running in), the source of the effect, and any modifications
        have been made at the cue level
         [420] [Enter]        {Rate} [500] [Enter]                                       Red for manuals changes

        A rate of 100 is the rate of the base effect. You can change it at a cue level
        in a range of 0% to 2000%. This is the same for Size.
        Word of warning! An override adjusts the attributes of the base effect. If
        the cycle time of an effect is 2 seconds, and you make a cue override of the
        rate at 200%, it will be 1 second in the cue. If you later change the base
        effect to a cycle time of 1 second in the effect editor, the cue will now play
        back with a time of 0.5 seconds.
         {Grouping} [200] [Enter]                                                        Along the bottom to the CIA above the
                                                                                         encoder area

                                                                                   Unit 8 – Effect Overrides       49

This larger grouping makes the effect look like each color is almost fully
coming in across the cyc before the next one starts
We also can set a BPM (beats per minute) live, as we listen to music. Let’s
do this with the intensity effect on the D60s
 [Effect] [421] [Learn] [Time]                                                   The command line reads: Effect 421
                                                                                 Learn Time Sample BPM
 [Enter] [Enter] [Enter]                                                         Averages the timing (tap rate) of the
                                                                                 last three hits of Enter

The side lights are panning far onto the proscenium.
Let’s make the size smaller so the lights don’t move as far. In addition to
using the softkeys, you can use encoders to set effect attributes
 [Clear}                                                                         To stop the BPM function

 [Effect] [416] [Enter] and roll the Size encoder down to 40

Besides using the encoders and softkeys, you can click directly in the ESD
table. This has the benefit of automatically selecting the correct effect

### CHANNEL LEVEL OVERRIDES

We can also override some effect properties on a per channel basis. These
changes will not affect the base effect.
 Workspace 2 on monitor 2                                                        Divided into 2 frames: Effect Status
                                                                                 (Tab 6) and Effect Channels (Tab 8)
 Make sure the tab focus is on Effect Channels.

The Effect Channels tab is where we make changes to effect properties on
a per channel basis
The two downstage-most lights on the scanning sides are still going over
the proscenium. If we edit the scale on all the channels, that would make
for a very small effect. Just make the scale on the two downstage lights
smaller, so they don’t go onto the proscenium front
 [161] [+] [165] roll Size down using the encoder until the lights don’t go
 over the proscenium

You’ll now see that the size of effect 416 has a + in the ESD. This is letting
you know that you have channels that are individually overridden for this
attribute.
 [Record] [401] [/] [20] [Label] Effect Override [Enter]

Notice that effects 416, 420, and 421 all have asterisks in the FX column in
the PSD in this cue. This is letting you know you have made overrides on
either the cue or channel level

50   Eos Family Effects Intensive

### EFFECTS IN PRESETS

       In addition to recording effects in cues and submasters, effects can be
       recorded into a preset. Cue and channel overrides are included when
       effects are stored in presets. This is a really great way to keep “looks”
       together for easy recall. It is especially useful when multiple effects are
       applied to the same fixtures.
        Stop all effects except the Pan Wave (Effect 416) on Side Spots (Group 105)

        Turn off the Cyc (Group 307)

        Make the OH Spots (Group 103), and the D60s (Group 200) Blue (CP 9033)

        From a clear command line, [Effect] [416] {Size} [Enter]                          To remove the effect overrides on the
                                                                                          Side Spots
        Make sure the tab focus is still on the Effect Channels tab

        [161] [+] [165] {Size} [At] [Enter]                                               To remove the overrides on specific
                                                                                          channels
        Go back to Workspace 1 on monitor 1, the Magic Sheet, Movers

        Side spots (G105) [Record] [Preset] [401] [Label] Side Spots [Enter]

        In [Blind], look at [Preset] [401] [Enter]

       There isn’t an effect in the preset! Pan has no effect. This is because we
       didn’t specify that we wanted the effect recorded.
        Back in [Live]

        Side spots (G105) [Record] [Preset] [402] {Plus Fx} [Label] Scanning Sides
        [Enter]

        In [Blind], look at [Preset] [402] [Enter]                                        The effect is included.

       Now when the preset is applied, the effect will be applied as well
        Back in [Live]

        [Record] <Cue> [401] [/] [21] [Label] Iso Sides [Enter]

        In [Blind], look at [Preset] [402] [Enter]                                        The effect is included.

       There is an easy way to change one effect for another that may fit better in
       this moment
        [Effect] [416] [Replace With] [417] [Enter]                                       Replaces the Pan Wave with the Circle

       Everywhere Effect 416 was used, it is now Effect 417. Notice, even though
       Effect 417 is a circle that applies to both Pan & Tilt, it is only on Pan. If we
       had selected the lights and applied Effect 417, it would be on Pan & Tilt.
       Because we did a Replace With, it is only where Effect 416 was
        [Live] [Go To Cue] [Enter]                                                        Notice the effect on Pan remains 416.

       Notice, the Effect on Pan remains 416. Changing an effect in the preset
       does not make the change anywhere the preset is already used! It must be
       reapplied!
        [Group] [105] [Preset] [402] [Enter]                                              Now it is using the preset effect 417

        [Update] [Enter]                                                                  Updates the cue with the new effect

## Unit 9 – Solve the Effect!

In this unit, we have a list of problems that the students must solve
with effects. This is time for the students to play and receive feedback.
They can ask questions but should be making these effects on their
own. Every 10-15 minutes, we should check in and share how people
are solving problems.
Some may have more than one shown solution, and there is always
more than one correct way. If more than 1 effect is used to achieve the
solution, they should be point numbers. (Ex. 450 & 450.1)
 [Go To Cue] [Out] [Enter]                                                  Before starting

All these effects will be recorded into cue list 402!

Effect 451: Problem:
In a TV studio and need to create a flicker effect with a variety of
spiking levels. The lighting designer wants to be able to use a light
meter and specify the levels of the spikes and specific moments on the
effect, so it won’t be too bright or too dim for the camera. We will be
running this on the FOH Spots.
Record into Cue 402/1

Effect 452: Problem:
I am working on a play that has a scene with a lantern in the DSL
corner. Throughout the scene, the candle flickers. We want the D60
downlight in that corner to mimic the lantern that is there.
Stop the flicker on the FOH Spots & turn them off. Record this new
candle effect into cue 402/2

Effect 453: Problem:
The designer has asked for a shimmer on the back-wall pixels (Group
700). They want it to feel like a dancing shimmy.
Stop the candle effect and turn the fixture off. Record this back-wall
shimmer into cue 402/3

52    Eos Family Effects Intensive

     Effect 454: Problem:
     We have been asked to create an effect that looks like fireworks
     shooting up and an exploding using the FOH Movers (Group 102)
     Stop the back-wall shimmer and turn them off. Record the fireworks
     into cue 402/4

     Effect 455: Problem:
     We have been asked to make the stage look like water. We want a full,
     immersive environment. Don’t forget, you can use multiple effects as
     well as non-intensity parameters!
     Record your water look as cue 402/5

     Effect 456: Problem:
     The electrician/gaffer has asked us to create an effect they can use to
     check the color flags in any CMY moving light before the programmer
     has arrived on site. They would like all the lights together to turn on to
     full, and snap between cyan, magenta, and yellow while they walk
     around and check.
     Record cue 402/6 with this CMY check on all moving lights (Group
     101). Everything else should be off.

     Effect 457: Problem:
     There is a sound effect of a beating hospital heart monitor. We want to
     create an effect that encapsulates that feeling on the intensity of the
     high side templates (Group 230 & 240). We want the effect to beat
     from current intensity of the lights.
     Stop the ML check cue and record this heartbeat into cue 402/7

Effect 458: Problem:
We are going to be doing a jail scene later and the convicts have
escaped. We want to create police searchlights using the FOH movers
(group 102). We are making this ahead of time, and we don’t know
how often we will use it. We should be able to recall this easily

54    Eos Family Effects Intensive

     Appendix 1 Unit 9 Solutions

### EFFECT 451: SOLUTION:

                 Effect 451: Absolute High Intensity
```text
                 Action          Param          Step Time         Time    Dwell   Level
                 1                              (1)               0.14    0       75.0
                 2                              (1)               0.14    0       100.0
                 3                              (1)               0.14    0       25.0
                 4                              (1)               0.14    0       65.0
                 5                              (1)               0.14    0       85.0
                 6                              (1)               0.14    0       35.0
                 7                              (1)               0.14    0       100.0
```

### ATTRIBUTES:

             -       Random Group
             -       Random Rate 50 > 200
             -       Cycle Time 1
             -       Grouping Spread
             -       Trail Even
             -       Duration Infinite
             -       Entry Immediate, Fade by Size, Cue/Sub
             -       Exit Immediate, Fade by Size, Cue/Sub

### EFFECT 452: SOLUTION:

        Channel 31 @ 50 in Orange (CP 9022)
        I applied a linear intensity flicker and a linear color flicker

### EFFECT 452 – CANDLE FLICKER

### ATTRIBUTES:

             -       Random Rate 50> 200
             -       Cycle Time 2
             -       Grouping Spread
             -       Trail Even
             -       Duration Infinite
             -       Entry Immediate, Fade by Size, Cue/Sub
             -       Exit Immediate, Fade by Size, Cue/Sub
             -       Scale 10

                                                  Appendix 1 Unit 9 Solutions   55

### EFFECT 452.1 – COLOR CANDLE FLICKER

### ATTRIBUTES:

     -   Random Rate 50> 200
     -   Cycle Time 2
     -   Grouping Spread
     -   Trail Even
     -   Duration Infinite
     -   Entry Immediate, Fade by Size, Cue/Sub
     -   Exit Immediate, Fade by Size, Cue/Sub
     -   Scale 10
     -   Parameters Red, Green, Amber

### EFFECT 453: SOLUTION:

### EFFECT 453 – RELATIVE SHIMMER

### ATTRIBUTES:

     -   Cycle Time 3
     -   Grouping 5
     -   Trail Even
     -   Duration Infinite
     -   Entry Immediate, Fade by Size, Cue/Sub
     -   Exit Immediate, Fade by Size, Cue/Sub
     -   Scale 25

### EFFECT 453.1 – ABSOLUTE SHIMMER

### ATTRIBUTES:

     -   Cycle Time 4
     -   Grouping 5
     -   Trail Even
     -   Duration Infinite
     -   Entry Immediate, Fade by Size, Cue/Sub
     -   Exit Immediate, Fade by Size, Cue/Sub

56    Eos Family Effects Intensive

### EFFECT 454 SOLUTION:

     Absolute effect using presets. I included a small preset at the up
     position so that the firework wouldn’t explode until it reached closer to
     the top

### PRESET 454.1: FIREWORKS DOWN/OFF

### ATTRIBUTES:

             -   Group 402 in their home position
             -   Off
             -   Firework Gobo (BP 9201.5)
             -   Small Zoom (BP 9041)
             -   Sharp (BP 9027)
             -   Red (CP 9021)
             -   Small Iris (I dialed to 42)

### PRESET 454.2: FIREWORKS UP/ON/SMALL

### ATTRIBUTES:

             -   Group 402 Tilted up to the top of the proscenium
             -   Pan fanned center out so they are slightly spread
             -   On
             -   Firework Gobo (BP 9201.5)
             -   Small Zoom (BP 9041)
             -   Sharp (BP 9027)
             -   Red (CP 9021)
             -   Small Iris (I dialed to 42)

### PRESET 454.3: FIREWORKS UP/ON/LARGE

### ATTRIBUTES:

             -   Group 402 Tilted up to the top of the proscenium
             -   Pan fanned center out so they are slightly spread
             -   On
             -   Firework Gobo (BP 9201.5)
             -   Medium Zoom (BP 9043)
             -   Sharp (BP 9027)
             -   Gold (CP 9024)
             -   Large Iris – 100

### EFFECT 454.4 – FIREWORKS

### ATTRIBUTES:

             -   Cycle Time 2.65 (came from changing action times to make the
                 fireworks feel like they are exploding at the top – I didn’t touch
                 this attribute)
             -   Grouping spread
             -   Trail Even
             -   Duration Infinite
             -   Entry Immediate, Fade by Size, Cue/Sub
             -   Exit Immediate, Fade by Size, Cue/Sub

                                                                                    Appendix 1 Unit 9 Solutions   57

### EFFECT 455: SOLUTION

I used the D60s in a slow color effect to feel like the ocean. I did
absolute. Could also be accomplished with a relative effect – either
color or linear applied to color parameters.
- I put the D60s at full in blue (CP 9033)
- Created an absolute color effect slowly fading between several
    blues
- I applied this effect to the D60s offset in a random group

### EFFECT 455 – WATER

### ATTRIBUTES:

       -   Cycle Time 15
       -   Grouping Spread
       -   Trail Even
       -   Duration Infinite
       -   Entry Immediate, Fade by Size, Cue/Sub
       -   Exit Immediate, Fade by Size, Cue/Sub
       I used the cyc in a slow intensity effect to make it feel like waves
       -   Put the full cyc (Group 207) at 30
       -   Cyc Top (Group 301) in Azure (CP 9031)
       -   Cyc Bottom (Group 304) in Blue (CP 9033)
       -   Apply a linear intensity effect across the mirrored in cells (Group
           315) and put the cells at 50. I felt that this made it feel like waves

### EFFECT 455.1 – WAVES

### ATTRIBUTES:

       -   Cycle Time 8
       -   Grouping Spread
       -   Trail Even
       -   Duration Infinite
       -   Entry Cascade, Fade by Size & Rate, Cue/Sub
       -   Exit Immediate, Fade by Size & Rate, Cue/Sub
       -   Scale 25

       I used the non-intensity parameters in FOH Movers to feel like
       reflecting water
       -   I homed the FOH Movers (Group 102) and stopped the effect
       -   Zoom large
       -   Wave gobo (BP 9211.2)
       -   I put in the animation wheel and slowly rotated it
       -   The odds channels I did positive rotation. The evens I did negative
           rotation
       -   I ran the edge until you couldn’t see the gobo or the animation
           wheel sharp. It looked likes movement.

58    Eos Family Effects Intensive

### EFFECT 456: SOLUTION

     I made this effect using the cyan, magenta, and yellow parameters.
     That way this can be used even if no color palettes are made for the
     fixtures, and we know that it is just each parameter at full on its own.

### EFFECT 456 – CMY CHECK

### ATTRIBUTES:

        - Cycle Time 3
        - Grouping 1
        - Trail Even
        - Duration Infinite
        - Entry Fade by Size, Cue/Sub
        - Exit, Fade by Size, Cue/Sub

### EFFECT 457: SOLUTION

     I made this effect as a relative effect. We could have done it as an
     absolute, but we were asked to make it beat from the current intensity
     of the fixtures

### EFFECT 457 – HEARTBEAT

### ATTRIBUTES:

             -   Cycle Time 1
             -   Grouping 1
             -   Trail Even
             -   Duration Infinite
             -   Entry Fade by Size, Cue/Sub
             -   Exit Fade by Size, Cue/Sub
             -   Scale 25

                                                                                     Appendix 1 Unit 9 Solutions   59

### EFFECT 458: SOLUTION:

I made three effects and recorded it into a preset so I could recall it
later.
One is an absolute intensity snap. To me, the lights snapping on and off
as it moves makes it seem more chaotic – we won’t know where the
lights will be when they next turn on.

### EFFECT 458 – COP INTENSITY STEP

### ATTRIBUTES:

       -   Cycle Time 2
       -   Grouping Spread
       -   Trail Even
       -   Duration Infinite
       -   Entry Immediate, Fade by Size, Cue/Sub
       -   Exit Immediate, Fade by Size, Cue/Sub
       One is a color effect. Red and blue signify the police. I created an
       absolute effect between red and blue.

### EFFECT 458.1 – RED/BLUE COP

### ATTRIBUTES:

       -   Random Rate 50> 200
       -   Cycle Time 5
       -   Grouping 2
       -   Trail Even
       -   Duration Infinite
       -   Entry Immediate, Fade by Size, Cue/Sub
       -   Exit Immediate, Fade by Size, Cue/Sub
       The last is a focus effect. It is a circle, but with the form compressed so
       that there is less tilt. This gives the lights a scanning feel as they roam
       the stage.

### EFFECT 452.1 – SEARCHLIGHT CIRCLE

### ATTRIBUTES:

       -   Cycle Time 10
       -   Grouping Spread
       -   Trail Even
       -   Duration Infinite
       -   Entry Immediate, Fade by Size, Cue/Sub
       -   Exit Immediate, Fade by Size, Cue/Sub
       -   Scale 20
       I recorded this into preset 458 plus FX

60   Eos Family Effects Intensive

Corporate Headquarters  Middleton, WI, USA  Tel +608 831 4116  Service (Americas) service@etcconnect.com
London, UK  Tel +44 (0)20 8896 1000  Service (UK) service@etceurope.com
Holzkirchen, DE  Tel +49 (80 24) 47 00-0  Service (DE) techserv-hoki@etcconnect.com
Hong Kong  Tel + 852 2799 1220  Service (Asia) service@etcasia.com
Paris, FR +33 1 4243 3535
Web etcconnect.com  © 2021 Electronic Theatre Controls, Inc.  Trademark and patent info: etcconnect.com/ip
Product information and specifications subject to change. ETC intends this document to be provided in its entirety.

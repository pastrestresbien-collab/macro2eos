# Virtual Media Server and Pixel Map Control — Eos Family Expert Topics Workbook (v3.0.0 Rev A)

- Source : PDF officiel ETC, « Virtual Media Server and Pixel Map Control — Eos Family Expert Topics Workbook (v3.0.0 Rev A) », V3.0.0 Rev A, publié 2020-12
- Fichier source : [`source/EosFamily_ET_VMS_v3.0.0revA.pdf`](source/EosFamily_ET_VMS_v3.0.0revA.pdf)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran du PDF ne sont pas reproduites)
- Conventions du workbook : **gras** = syntaxe/menus browser ; [crochets] = touches de façade ; {accolades} = softkeys/boutons tactiles ; <chevrons> = touches optionnelles ; & = touches pressées simultanément ; «Direct Select» = appui Direct Select

Virtual Media Server and Pixel Map Control

                  Eos Family Expert Topics

                                       Workbook

                                        V3.0.0 Rev.A

                       www.etcconnect.com/education

                                       Released: 2020-12

## Table of Contents

         ETC permits the reproduction of materials in this manual only for non-commercial purposes.
         All other rights are reserved by ETC.

## Purpose of the Class

    The Eos Family Media Server Control class will explore core concepts of
    media servers, pixel mapping software, and their control. This will include
    using external media servers, Eos Family Pixel Mapping feature, and
    utilizing Eos Family control tools to simplify and speed up media server
    implementation in a show file.

### LEARNING OBJECTIVES:

        After completing the Media Server Control class, you should be able to:
            - Understand the concepts of Media Servers
            - Patch and control external Media Servers
            - Create and configure Pixel Maps
            - Patch and control Virtual Media Servers
            - Understand layer control, channel vs. layer output, and crossfades
            - Record Media Server information into Cues
            - Utilize Palettes and Presets with Media Servers
            - Utilize advanced timing with Media Servers
            - Record Media Server content into Subs for live playback
            - Understand content management and multi-console systems
            - Load user generated content into the console

### WORKBOOK SYNTAX ANNOTATION

               - Bold                        Browser menus
               - [Brackets]                  Face panel buttons
               - {Braces}                    Softkeys and direct selects
               - <Angle brackets>            Optional keys
               - [Next] & [Last]             Keys to be pressed & held simultaneously
               - «Direct Select»             Direct Select button press
               - MS Object                 Object on a Magic Sheet

               - Play Icon                   Link to video on ETC’s YouTube Channel –
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
               Please note that it is not available on Windows XP devices or on Macs, but is available as
               a download from the web site.

## Eos Family Virtual Media Server

Start with the following show file:
“Eos Family Level 4 Complete 2019-07-15 12-31-15.esf”

Eos family consoles have a built-in Virtual Media Server (VMS). VMS does
not output to video devices such as projectors or televisions, but rather
allows content to be mapped to DMX-capable devices.
      For more information on media servers in general, see Appendix 6.

VMS allows you to map content to output devices just like an external
media server, but instead of speaking DMX from the console to the media
server, and the media server outputting video signal to the output
devices, the console speaks DMX directly to the output devices (hence the
need for only DMX-capable devices).

Patch Exercise – see Appendix 1
    First let’s patch the LED Fixtures into the show. Although Appendix 1 is 5
    pages long, it will take 2 simple command lines
```text
     In Patch, [701] [Thru] [884] {Type} {Generic} {LED RGB [3]} {8B [3]} [At]      Patches 8B RGB LEDs to all the cyc pixel
     [20] [/] [1] [Enter]                                                           channels

     [901] [Thru] [927] {Type} {Generic} {LED RGB [3]} {8B [3]} [At] [22] [/] [1]   Patches 8B RGB LEDs to all the MTG pixel
     [Enter] …                                                                      channels
```

### TO CHECK YOUR PATCH:

     [Live]    [701] [At] [Full] [More SK] {Chan Check} [Enter]                     puts the console in Chan Check mode

            then [Next] … [Next] …                                                  steps through all patched channels

### OUTPUT DEVICE CONFIGURATION, OR PIXEL MAPS

In Virtual Media Server, the utility to configure the type and physical
layout of your output devices is called a Pixel Map. Just like an external
Media Server, a Pixel Map determines which pixels in the content get
mapped to which output devices.

### CREATING THE PIXEL MAP

      [Displays]                [More SK]           {Pixel Maps}                    opens the Pixel Map Editor

      [1] [Enter]                                                                   selects and creates Pixel Map 1

### SETTING WIDTH / HEIGHT

      {Width} [31] [Enter]                                                          adjusts the width of the pixel map

      {Height} [20] [Enter]                                                         adjusts the height of the pixel map

### LABEL

      [Label] “Cyc Pixels” [Enter]                                                  assigns a label to the pixel map

### OPENING THE EDITOR

      Once you have laid out a basic Pixel Map space, you need to add the specific
      output devices, or fixtures.
        {Edit}                                                                         opens the Pixel Map Editor
      Many of the same mouse navigation tools work in this space:
        Use your mouse wheel                                                           to zoom in and out

        Right click and hold                                                           to pan or drag the display

        CTRL+C and CTRL+V                                                              to copy and paste

        Control and multiple clicks                                                    to select multiple objects

### SELECTING THE OUTPUT PIXELS

      In the edit screen, you will be able to define which pixels in the map will be
      output devices, or Fixtures.
        Click and hold left mouse button and drag                                      to select the pixels that will be fixtures.

      As you hover over a pixel, you see the coordinates for the pixel.
        Drag from (5,7) to (27, 14)                                                    Overall the selection will be 23x8

### ASSIGNING CHANNELS TO FIXTURES

In the Pixel Patch area, there is a channel or address utility that allows you to
quickly assign start channels or addresses to the selected output objects in
the Pixel Map.

  Click {Start Channel}                                                             posts Start Channel to the command line
                                                                                    defines the devices patched in channels
  [701] [Enter]
                                                                                    701 and up
  In Cell Mapping, click {Cells} and change to {Channels}
                                                                                    changes the way the auto-numbering
  Click on Horizontal and Vertical Order
                                                                                    populates through the pixels.
                                                                                    changes the way the auto-numbering
  Click Direction to “Columns”
                                                                                    populates through the pixels.

                                                                                    assigns each fixture channel sequentially
  Click {Apply}
                                                                                    according to the utility settings

    All the pixels/fixtures turn gray to indicate that they have been assigned
    a Channel, and channel numbers appear in each pixel.

  Click {Done} – a softkey!!!                                                       exits editor and saves work

    All pixels/fixtures turn pink.

### A NOTE ABOUT PIXEL MAPS:

       It is important to remember that setting up a Pixel Map is not the same as
       patching a fixture in the console’s patch function. A Pixel Map in VMS is the
       same as the Output Configuration utility in an external Media Server.
       Instead of telling Content Pixel 1 that it will be controlling a pixel on a
       1280x1024 monitor on Video Card 1 (as you would in an external Media
       Server), in a Pixel Map you are telling Content Pixel 1 that it will be
       controlling an RGB LED on Universe 10 address 1-3.
       If it helps, think of the Pixel Map utility as a Media Server box inside of the
       console – hence the name Virtual Media Server.

### ASSIGNING SERVER & LAYER CHANNELS

       Just like in an external Media Server, we must tell the Virtual Media Server
       what it is listening to for control. In an external Media Server, we would give
       the server channel and the layer channels DMX addresses at the server (like a
       moving light). But because the VMS is contained in the console, we only have
       to tell the Pixel Map which channels to listen to.
       No address is required so assigning the channels can be done in the Pixel
       Map Edit area.

                                                                                         Assigns the channel number for the VMS
        {Server Channel} [511] [Enter]
                                                                                         server channel (Master Layer)
                                                                                         Assigns the channel numbers for the
        {Media Layer Channels} [512] [+] [513] [Enter]
                                                                                         Media layers (Content Layers)
                                                                                         Assigns the channel number for the
        {Effect Layer Channels} [514] [+] [515] [Enter]
                                                                                         Effect layers (Content Layers)
                                                                                         Verify that these channels have been
        In Patch, [511] [Thru] [515] [Enter]
                                                                                         populated with the correct fixture types

       Each Virtual Media Layer contains one piece of media content, which can be
       stacked on top of each other or used separately. These layers are controlled
       in a very similar manner as moving lights and just like their automated
       counterparts they contain many parameters that can be modified in order to
       create the desired look.

       The Virtual Effect Layer allows you to use procedurally generated content.
       This is content that is created algorithmically in real time, instead of
       rendering file-based media.

    NOTE:   There can be up to 12 Media Layers and Effect Layers total per Virtual
            Server.

### OTHER USEFUL DISPLAYS

There are two display options that will assist in the usage of VMS:

### PIXEL MAP PREVIEW

    Pixel Map Preview shows what the console is outputting to the pixel map.
      Use Add-a-Tab (the {+} sign)

      {Pixel Map Preview}                                                         opens Pixel Map Preview (PMP) in a tab
                                                                                  to display the grid (other options to be
      Click on the area under {Overlay}
                                                                                  discussed later)

### ML CONTROLS

    ML Controls shows thumbnails of the media content and provides individual
    control of all the parameters of the virtual media server.

      Use Add-a-Tab (the {+} sign)

      {ML Control}                                                                select ML Controls

## VMS Manual Control

### GETTING STARTED WITH MEDIA LAYERS

      [Live] with ML Controls display

      [511] [At] [Full] [Enter]                                                           turns on the server

      [512] [At] [Full] [Enter]                                                           turns on media layer 512

      Scroll right to Image section, Library :: 0

### ADJUSTING CONTENT PLAYBACK OPTIONS

        - {Library} - selects the image folder - allows selection of video
            folder 0 through 255 (0 is default ETC folder)
        - {File} - selects the media file within the selected library - allows
            selection of video clip 0 through 255
        - {Playback Mode 1}:
            - {Display Centered} – shows the file in it’s centered frame
            - {Display In Frame} – shows the start frame of the video file
            - {Display Out Frame} – shows the end frame of the video file
            - {Play Loop Forward} – plays the file from its start frame to its end
                   frame and repeats
            - {Play Loop Reverse} – plays the file from its end frame to the start
                   frame and repeats
            - {Play Once Forward} – plays the file from start frame to end frame
                   and stops
            - {Play Once Reverse} – plays the file from the end frame to the start
                   frame and stops
            - {Stop} – stops the file in its current frame
        - {Playback Speed} - the speed at which the video plays back (fps)
        - {In / Out Point} - determines where in the clip (frame number)
            you want to enter in or to exit (basic video editing feature –
            select a section of the video to play)

### PLAYBACK EXERCISE

                {File} {46}                                                               with mouse, click on file 46

                Scroll back left to {Play Mode}, {Play Loop Forward}                      select the playback mode
                                                                                          mouse over playback speed and click or
                Increase {Playback speed} to 100
                                                                                          roll mouse wheel

### ADJUSTING CONTENT COLOR RENDERING OPTIONS

    Scroll left to Color section                                               with chan 512 still on the command line

- Color (Red, Green, Blue; Hue & Saturation) - Filters the color of
       the content. For example, if all the colors are set to full, the
       content will play all colors normally. If blue is at 0, then only the
       red and green pixels of the content will play. The color and gel
       pickers can be used to select color filtering quickly.
- Contrast - Adjusts the contrast of the content playing, just like a
       television or monitor.
- Negative - With negative on, the output is the negative of the
       content. With it off, the content plays back normally.
- Image Brightness - Adjusts the brightness of the content, just like
       a television or a monitor. Moving toward 100 shifts the content
       toward white, moving toward -100 shifts the content toward
       black. Image brightness should not be confused with Intensity.

### COLOR RENDERING EXERCISE

        {Red} {Min}        {Red} {Home}                                        varies the red filter on the content

        {Negative On}              {Negative Off}                              toggles content output

        {Image Brightness} [50]             {Image Brightness} {Home}          varies the brightness normal to full white

                                                                               varies the contrast from -100 to 100,
        {Contrast} {Max}            {Contrast} {Home}
                                                                               home = 0 or normal

### ADJUSTING CONTENT SHAPE AND LOCATION OPTIONS

           Scroll right to Shutter section                                       with chan 512 still on the command line

       - Scale - Changes the scale of the content to either be larger or
             smaller than the standard content playback.
       - Aspect Ratio - Stretches or shrinks the content only along the X
             axis, making it wide or squished looking. Z Rotate can be used to
             modify the aspect ratio along the Y axis.

              Scroll right to Focus section                                      with chan 512 still on the command line

       - Pan and Tilt - Moves the content up and down, left and right
             within the pixel map frame.

### SHAPE AND LOCATION EXERCISE

                                                                                 changes the content scale to 15% of its
              {Scale} [15] (Don’t forget command line shortcuts!)
                                                                                 original size
              {Pan} [-] [15]                                                     moves the content to the left by 15%

              {Tilt} [15]                                                        moves the content upwards by 15%

### ADJUSTING CONTENT 3D ROTATION OPTIONS

- {X and Y Rotate} - Rotates the content in 3 dimensions. X rotates
    the content along the X axis – or toward and away from you. Y
    rotates the content along the Y axis – or left and right in front of
    you.
- {Z Rotate} - Rotates the content around the Z axis (the axis
    pointed straight at you). There are two options, just like gobo
    rotations:
    - {Gobo Mode Index} – adjusts the content by degrees, and does not
          continually rotate
    - {Rotate} – rotates the content continually, from slow to fast.
- {Field of View (FoView)} - Adds a perspective view to the content.
    This can only be used when X and/or Y rotate are not at 0.

### 3D ROTATION EXERCISE : X, Y &Z ROTATE, FIELD OF VIEW

        [512] [Enter]                                                        re-selects channel 512

            Under Shutter in the ML Controls
        {X Rotate} [50] (roll the wheel slowly to 50 to see changes)         rotates the content along the X-axis.

        {Y Rotate} [50] (roll the wheel slowly to 50 to see changes)         rotates the content along the Y-axis.

            Under Form in the ML Controls
                                                                             shifts the Field of View more drastically
        {FoView} [100] (roll the wheel slowly to 100 to see changes)
                                                                             as you move toward 100.
        {FoView} {Home}                                                      restores Field of View to home.

            Under Shutter in the ML Controls
                                                                             opens Z Rotate encoder next to X,Y
        Click on the Z Rotate Header
                                                                             Rotate
        {Gobo Mode Index}, notice scale -180 to 180 Degrees                  default mode for Z Rotate

          Roll Z Rotate encoder                                              indexes content

          {Z Rotate} {Home}                                                  homes the content index

        {Rotate}, notice scale -100 to 100%                                  default mode for Z Rotate
                                                                             rotates content continually, from slow to
          Roll Z Rotate encoder
                                                                             fast
          {Z Rotate} {Home}                                                  homes the content

### MULTIPLE LAYER CONTROL AND OPTIONS

      [Clear] [Sneak] [Enter]                                                              clears all previous work

### SETTING UP CONTENT LAYERS

        Because each VMS can have multiple layers, there are certain tools that work
        specifically with two or more layers interacting. But first, let’s look at layer
        structure and interaction rules.

                                                                                           turns on the server channel, as well as
         [511] [Thru] [513] [At] [Full] [Enter]
                                                                                           both content (media) layers
         [512] [Enter]                                                                     selects channel 512 – first content layer

             Within ML Controls:
         Scroll to Library :: 0 and then select {File 39}                                  loads the ETC logo content

         {Scale} [10] [Enter]                                                              adjusts the scale to 10%
                                                                                           places the graphic near the upper-left
         {Pan} [-] [25] [Enter]      {Tilt} [25] [Enter]
                                                                                           corner

         [513] [Enter]                                                                     selects channel 513 – a media layer

         Scroll to Library :: 0 and then select {File 65}                                  loads the pink swirl content

         {Scale} [20] [Enter]                                                              adjusts the scale to 20%
                                                                                           places the graphic near the lower-right
         {Pan} [20] [Enter]       {Tilt} [-] [20] [Enter]
                                                                                           corner

### LAYER INTENSITIES (OPACITY)

Notice that the higher numbered Layer Channel is on top. The lowest
numbered layer will always be on the bottom, and the highest on the top in
each VMS.

                                                                                  notice transparency of overlapping
 With [513] still selected, roll down intensity wheel
                                                                                  layers.
 Roll intensity back in

Intensity can be used to dim a layer or to allow other lower layers bleed
through (also known as opacity).

### MASK

A Mask takes a lower layer and a higher layer, finds only the non-transparent
pixels they have in common, and then displays the common pixels of the
higher layer.

 [513] [At] [Full] [Enter], [512] [Enter]                                         brings 513 to full, selects 512
                                                                                  notice the only pixels showing are the
 {Mask} {On}
                                                                                  ones in [513] that overlap with [512]

 {Mask} {Off}

Using some of the shapes in the library (folder 0, files 12-38) are great ways
to trim or shape content on another layer. Just remember, the Mask must
always be applied to the lower of the two layers.

### SETUP FOR MIXER MODE EXERCISE

 [512] [Enter]

 Scroll to Library :: 0, select {File 65}, {Scale} [15] [Enter], {Focus} {Home}   loads and sets the ETC Logo content

 [513] [Enter]

 Scroll to Library :: 0, select {File 20}, {Scale} [12] [Enter], {Focus} {Home}   loads and sets the star content

### MIXER MODE

       The Mixer allows different transparencies, masks, and color rendering tools
       to be utilized in how two layers interact.

```text
                        File :: 39                                                                      File :: 20
         Top Layer (lowest channel)                                                       Bottom Layer (highest channel)

         Mixer Mode                  Description                                          Result

         {Over} (Default)            Top layer blended with bottom layer
```

                                     Top Layer with opacity reduced by opacity of
         {In}
                                     bottom layer

                                     Top layer with opacity reduced by
         {Out}
                                     inverse opacity of bottom layer

                                     Top layer with opacity reduced by
         {Atop}                      opacity of bottom layer and then
                                     blended with bottom layer

                                     Top and bottom layers color and opacity added
         {Add}
                                     together

                                     Top and bottom layers color and opacity
         {Subtract}
                                     subtracted from each other

                                     Top and bottom layers color and opacity multiplied
         {Multiply}
                                     together

                                     Top and bottom layers colors inverted and then
         {Screen}
                                     multiplied together

               Does a multiply or screen effect based on the
{Overlay}
               lightness or darkness of the bottom layer

               Top layer’s color merges with bottom layer’s color,
{Lighten}
               with the lighter color winning

               Top layer’s color merges with the bottom layer’s
{Darken}
               color, with the darker color winning

               Bottom layer’s color brightened to reflect top
{Dodge}
               layer’s color

               Bottom layer’s color darkened to reflect the top
{Burn}         layer’s color

               Does a multiply or screen effect on the lightness or
{Hard Light}
               darkness of the top layer

               Darkens or lightens colors depending on the top
{Soft Light}
               layer

               Top layer with opacity reduced by inverse opacity
               of bottom layer, and then blended with the bottom
{Xor}
               layer with opacity reduced by the inverse opacity
               of the top layer

### VIRTUAL EFFECT LAYERS

        Virtual Effect layers are a special type of layer in that they do not need pre-
        generated content to output to devices. Instead, they use variables defined
        by the programmer to create algorithmically-generated procedural media. To
        put it more simply – you change a few parameters, and the board
        mathematically generates content.
        Virtual Effect Layers share many of the same controls as Media layers. Some
        of these have the same behavior as their Media Layer counterparts, and
        some behave differently. This section will go through examples on things that
        are different in Effect layers. Parameters whose behaviors remain entirely
        the same are:
             - Pan & Tilt
             - Playback Mode
             - Negative and Image Brightness
             - FoView, Scale, Aspect Ratio and X, Y & Z Rotate
             - Mask and Mixer Mode

### ABOUT GENERATED CONTENT

        Because there are simple but powerful algorithms, there is no need for a
        massive library of folders and files for content. Therefore, you will only find a
        File 1 parameter. The parameter includes 4 types of content:

          Perlin Noises, user defined colors (files 1-3)

          Perlin Noise, rainbow colors (file 4)

          Gradients, rainbow colors (files 5-9)

          Gradients, user defined colors (files 10-19)

        Each content type will have different selections for shape and size.

        Certain tools will behave differently based on whether a Perlin or a Gradient
        is selected, or whether it is Rainbow or User Defined color. We will cover all
        instances applicable to each parameter.

### VIRTUAL EFFECT LAYERS: GRADIENT, RAINBOW

  [Clear] [Sneak] [Enter]                                                                          clears all previous work

  [511] [At] [Full] [Enter]                                                                        turns on the server

  [514] [At] [Full] [Enter]                                                                        turns on the effect layer

  Scroll to File :: 0, select {File 5}                                                             selects linear rainbow gradient
                                                                                                   increases the content to fill the entire
  {Width} [13] [Enter]          {Height} [9] [Enter]
                                                                                                   pixel map
  {Playback Speed} [0] [Enter]                                                                     stops the movement of the gradient

  {Playback Speed} [50] [Enter]                                                                    speeds up the movement of the gradient
                                                                                                   compresses gradient, adding more
  {Layer Effect} [50] [Enter]                                                                      repeats – up to 4 as you approach 100
                                                                                                   spreads gradient, eventually becoming a
  {Layer Effect} [-] [50] [Enter] {Min}
                                                                                                   single color as you approach -100

    Gradient Layer Effect: 0                    Gradient Layer Effect: 50                   Gradient Layer Effect: -50

### CONTINUING CONTENT: PERLIN NOISE, RAINBOW

  Scroll to File :: 0, select {File 4}                                                             selects Perlin noise rainbow
                                                                                                   increases noise and pixelation, getting
  {Layer Effect} [50] [Enter]
                                                                                                   sharper as you approach 100
                                                                                                   decreases noise, less pixalation (larger),
  {Layer Effect} [-] [50] [Enter]
                                                                                                   getting softer as you approach -100
                                                                                                   scrolls the effect in one direction as you
  {Layer Effect 2} [50] [Enter]
                                                                                                   approach -100 to 100
                                                                                                   scrolls the effect in opposite direction as
  {Layer Effect 2} [-] [50] [Enter]
                                                                                                   you approach -100 to 100
  {Layer Effect 2} [0] [Enter]                                                                     stops the effect from scrolling

    Perlin Layer Effect: 0                      Perlin Layer Effect: 50                     Perlin Layer Effect: -50

    Parameters with no affect on rainbow effects are Intensity 2, Red, Blue, Green, Red2,
    Blue2, Green2, Hue, Saturation, In Point, and Out Point.

### CONTINUING CONTENT: USER DEFINED COLORS (GRADIENT)

       User-Defined Colors use a Start Color and an End Color to define their range
       and behavior. Each has a few parameters associated with it. The Start Color
       uses Red, Green, and Blue to mix the color, Intensity to change opacity, and
       In Point to select how far from the mixed color the gradient starts. Not
       surprisingly, the End Color uses Red2, Green2, Blue2, Intensity2, and Out
       Point for all the same features.

         [514] [Enter]                                                                      selects the effect layer

         Scroll to File :: 0, select {File 3}                                               selects user-defined gradient

         Use first Color Picker to select green                                             changes the start color to green

         Use second Color Picker to select blue                                             changes the end color to blue
                                                                                            just like rainbow gradients, layer effect
         {Layer Effect} [50] [Enter]
                                                                                            compresses or expands the gradient

### CONTINUING CONTENT: PERLIN NOISE, USER DEFINED COLORS

       Perlin noise with user defined colors combines the tools already learned as
       one would expect. The colors are user-definable through the above-
       mentioned color and opacity selection, but the noise and animation can be
       adjusted just like in rainbow Perlin noise.

         [514] [Enter]                                                                      selects the effect layer

         Scroll to File :: 0, select {File 2}                                               selects user-defined Perlin noise
                                                                                            decreases noise, getting softer as you
         {Layer Effect} [-] [50] [Enter]
                                                                                            approach -100
                                                                                            scrolls the effect faster in opposite
         {Layer Effect 2} [50] [Enter]
                                                                                            directions as you approach -100 to 100

           Gradient Layer Effect: 50              Perlin Layer Effect: 50            Perlin Layer Effect: -50

### EFFECT LAYER EXERCISE: SIMPLE FIRE EFFECT

Let’s build a quick example – you need the look of fire, and instead of finding
video content, sizing it, importing it, and trying to loop it on a Media layer,
you decide to use a VMS Effect Layer.

 [Clear] [Sneak] [Enter]                                                          clears all previous work

 [511] [+] [514] [At] [Full] [Enter]                                              turns on the server and the effect layer

 [514] [Enter]                                                                    selects just the effect layer

 Scroll to File :: 0, select {File 1}                                             selects a user defined Perlin noise effect

 Use first Color Picker to select yellow                                          makes the start color yellow

 Use second Color Picker to select red                                            makes the end color red

 {Playback Speed 1} [50] [Enter]                                                  gives the noise a bit more movement

 {Layer Effect 2} [50] [Enter]                                                    gets the fire moving – but sideways

 {Z Rotate} [90] [Enter]                                                          rotates the fire to flame vertically
                                                                                  makes the red more opaque – gives a
 {Intensity 3} [40] [Enter]
                                                                                  smoldering look

## Server Controls

     Server controls have the same functionality as layer controls, but instead
     of affecting a single layer and its content, the server controls affect every
     layer in the VMS.

### BASIC CONTROLS

                                                                                             works similarly to the video layer except
       Intensity
                                                                                             for all layers
       Pan/Tilt                                                                              moves all layers

       Color – Red, Green, Blue; Hue, Saturation                                             filters color for all layers

       FoView                                                                                adjusts the perspective of all layers

       Scale                                                                                 adjusts scale of all layers

       Aspect Ratio                                                                          adjusts aspect ratio of all layers

       XYZ Rotation Controls                                                                 rotation control for all layers

### CROSSFADE

     Crossfade is a server-only parameter and is used to adjust the priority
     when parameters in a Pixel Map are also patched as desk channels. A
     value of 100 gives the desk channel priority, while -100 gives the VMS
     priority. At 0 (the default home) the output is calculated as Highest Takes
     Precedence (HTP) per parameter between the two sources.

       [Live]          [701] [Thru] [884] [At] [Full]                                        turns on LEDs (desk control)

       Put the LEDs in a Green using Color Picker                                            fire effect running from previous exercise

       [511] [Enter]                                                                         reselects server, currently HTP per color
                                                                                             desk channels have control where data is
       {Crossfade} [100] [Enter]
                                                                                             available
       {Crossfade} [-][100] [Enter]                                                          Virtual Media Server has control
                                                                                             Home or 0 – Highest takes precedence
       {Crossfade} [Home] [Enter]                                                            for each emitter

### MULTIPLE SERVERS USING THE SAME OUTPUT DEVICES

                It is possible to have multiple servers talking to the same output devices
                by patching the same fixtures in multiple pixel maps. Unless there is a
                Server channel with a higher Crossfade parameter, all parameters will
                respond HTP to all Server and Desk channel sources speaking to it. If a
                Server channel’s Crossfade gives it a higher priority over Desk channels,
                it will win over Desk channels with values, but not other Server channels.
                Crossfade does not affect priorities between Server channels.

## Recording

### RECORDING CUES

   [Record] [Cue] [501] [Enter]                                                 records cue 1 with VMS content

 Yes, it is that simple! Since Virtual Media Servers and Layers are handled
 exactly like moving lights, all the same rules apply. Some things to keep in
 mind when recording Virtual Media content are:
      - Mark/AutoMark
      - Tracking rules
      - Update rules
      - Discrete Timing
      - Snap Parameters

### RECORDING SUBS

    [Record] [Sub] [501] [Enter]                                                records Sub 501
                                                                                designates the sub as an Intensity
    [Sub] [501] {Properties}, under Master, {Int}
                                                                                master sub

 Subs will work in the same manner as cues with regards to Virtual Media
 Servers. Due to the amount of information needing to be preset it is highly
 recommended that all subs that utilize Virtual Media Servers be made into
 Intensity Masters. This will help reduce some of the visible parameter
 changes.

### RECORDING PALETTES AND PRESETS

 Due to the massive amount of data available for modification with Virtual
 Media Servers, it is highly recommended that the users take advantage of
 the console’s presets and palettes.
 Some examples of where presets and palettes could be helpful:
      - Quick File/Folder Recall
      - Color Overlay
      - Layer Positioning
      - Overall Look Recall

     Locked Palettes are very useful when working with Virtual Media Servers.

### OTHER PIXEL MAP TOOLS

### COLUMN / ROW GUIDES

        Provides gathering elements in the pixel map display that may be useful for
        large maps

### NAVIGATING WITHIN THE PIXEL MAP EDITOR

          Right Mouse Button                                                          Pan control

          Mouse Wheel                                                                 Zoom

          [Format] + Level Wheel                                                      Zoom

### OPTIONS AVAILABLE FOR CHANGING THE MAPPING

          {Horizontal Order}                                                          toggle state from left to right/right to left
                                                                                      toggle state from top to bottom to
          {Vertical Order}
                                                                                      bottom to top
          {Direction}                                                                 toggle state from rows to columns

          {Rotate 90}, {Flip V}. {Flip H}, {Invert}

### PIXEL MAP PREVIEW ADVANCED OPTIONS

          Zoom                                                                        mouse wheel

          Mask On/Off                                                                 see full video or just pixels

          Overlay:                                                                    default in None

                 Grid                                                                 displays a grid on top of the preview

                 Cells                                                                displays outline of pixels (by cell)

                 Fixtures                                                             displays outline of pixels (by fixture)

          Next & Last                                                                 preview different Pixel Maps

## Appendix 1 – Pixel Mapping Hookup

### CYC PIXELS

```text
Channel   Universe   Address   Manufacturer   Type                     Focus/Notes
701       20         1         Generic        LED RGB – 8B             Cyc Pixels
702       20         4         Generic        LED RGB – 8B             Cyc Pixels
703       20         7         Generic        LED RGB – 8B             Cyc Pixels
704       20         10        Generic        LED RGB – 8B             Cyc Pixels
705       20         13        Generic        LED RGB – 8B             Cyc Pixels
706       20         16        Generic        LED RGB – 8B             Cyc Pixels
707       20         19        Generic        LED RGB – 8B             Cyc Pixels
708       20         22        Generic        LED RGB – 8B             Cyc Pixels
709       20         25        Generic        LED RGB – 8B             Cyc Pixels
710       20         28        Generic        LED RGB – 8B             Cyc Pixels
711       20         31        Generic        LED RGB – 8B             Cyc Pixels
712       20         34        Generic        LED RGB – 8B             Cyc Pixels
713       20         37        Generic        LED RGB – 8B             Cyc Pixels
714       20         40        Generic        LED RGB – 8B             Cyc Pixels
715       20         43        Generic        LED RGB – 8B             Cyc Pixels
716       20         46        Generic        LED RGB – 8B             Cyc Pixels
717       20         49        Generic        LED RGB – 8B             Cyc Pixels
718       20         52        Generic        LED RGB – 8B             Cyc Pixels
719       20         55        Generic        LED RGB – 8B             Cyc Pixels
720       20         58        Generic        LED RGB – 8B             Cyc Pixels
721       20         61        Generic        LED RGB – 8B             Cyc Pixels
722       20         64        Generic        LED RGB – 8B             Cyc Pixels
723       20         67        Generic        LED RGB – 8B             Cyc Pixels
724       20         70        Generic        LED RGB – 8B             Cyc Pixels
725       20         73        Generic        LED RGB – 8B             Cyc Pixels
726       20         76        Generic        LED RGB – 8B             Cyc Pixels
727       20         79        Generic        LED RGB – 8B             Cyc Pixels
728       20         82        Generic        LED RGB – 8B             Cyc Pixels
729       20         85        Generic        LED RGB – 8B             Cyc Pixels
730       20         88        Generic        LED RGB – 8B             Cyc Pixels
731       20         91        Generic        LED RGB – 8B             Cyc Pixels
732       20         94        Generic        LED RGB – 8B             Cyc Pixels
733       20         97        Generic        LED RGB – 8B             Cyc Pixels
734       20         100       Generic        LED RGB – 8B             Cyc Pixels
735       20         103       Generic        LED RGB – 8B             Cyc Pixels
736       20         106       Generic        LED RGB – 8B             Cyc Pixels
737       20         109       Generic        LED RGB – 8B             Cyc Pixels
738       20         112       Generic        LED RGB – 8B             Cyc Pixels
739       20         115       Generic        LED RGB – 8B             Cyc Pixels
740       20         118       Generic        LED RGB – 8B             Cyc Pixels
741       20         121       Generic        LED RGB – 8B             Cyc Pixels
742       20         124       Generic        LED RGB – 8B             Cyc Pixels
743       20         127       Generic        LED RGB – 8B             Cyc Pixels
744       20         130       Generic        LED RGB – 8B             Cyc Pixels
745       20         133       Generic        LED RGB – 8B             Cyc Pixels
746       20         136       Generic        LED RGB – 8B             Cyc Pixels
747       20         139       Generic        LED RGB – 8B             Cyc Pixels
748       20         142       Generic        LED RGB – 8B             Cyc Pixels
749       20         145       Generic        LED RGB – 8B             Cyc Pixels

```

### CYC PIXELS (CONTINUED)

```text
     Channel   Universe   Address   Manufacturer   Type           Focus/Notes
     750       20         148       Generic        LED RGB – 8B   Cyc Pixels
     751       20         151       Generic        LED RGB – 8B   Cyc Pixels
     752       20         154       Generic        LED RGB – 8B   Cyc Pixels
     753       20         157       Generic        LED RGB – 8B   Cyc Pixels
     754       20         160       Generic        LED RGB – 8B   Cyc Pixels
     755       20         163       Generic        LED RGB – 8B   Cyc Pixels
     756       20         166       Generic        LED RGB – 8B   Cyc Pixels
     757       20         169       Generic        LED RGB – 8B   Cyc Pixels
     758       20         172       Generic        LED RGB – 8B   Cyc Pixels
     759       20         175       Generic        LED RGB – 8B   Cyc Pixels
     760       20         178       Generic        LED RGB – 8B   Cyc Pixels
     761       20         181       Generic        LED RGB – 8B   Cyc Pixels
     762       20         184       Generic        LED RGB – 8B   Cyc Pixels
     763       20         187       Generic        LED RGB – 8B   Cyc Pixels
     764       20         190       Generic        LED RGB – 8B   Cyc Pixels
     765       20         193       Generic        LED RGB – 8B   Cyc Pixels
     766       20         196       Generic        LED RGB – 8B   Cyc Pixels
     767       20         199       Generic        LED RGB – 8B   Cyc Pixels
     768       20         202       Generic        LED RGB – 8B   Cyc Pixels
     769       20         205       Generic        LED RGB – 8B   Cyc Pixels
     770       20         208       Generic        LED RGB – 8B   Cyc Pixels
     771       20         220       Generic        LED RGB – 8B   Cyc Pixels
     772       20         214       Generic        LED RGB – 8B   Cyc Pixels
     773       20         217       Generic        LED RGB – 8B   Cyc Pixels
     774       20         220       Generic        LED RGB – 8B   Cyc Pixels
     775       20         223       Generic        LED RGB – 8B   Cyc Pixels
     776       20         226       Generic        LED RGB – 8B   Cyc Pixels
     777       20         229       Generic        LED RGB – 8B   Cyc Pixels
     778       20         232       Generic        LED RGB – 8B   Cyc Pixels
     779       20         235       Generic        LED RGB – 8B   Cyc Pixels
     780       20         238       Generic        LED RGB – 8B   Cyc Pixels
     781       20         241       Generic        LED RGB – 8B   Cyc Pixels
     782       20         244       Generic        LED RGB – 8B   Cyc Pixels
     783       20         247       Generic        LED RGB – 8B   Cyc Pixels
     784       20         250       Generic        LED RGB – 8B   Cyc Pixels
     785       20         253       Generic        LED RGB – 8B   Cyc Pixels
     786       20         256       Generic        LED RGB – 8B   Cyc Pixels
     787       20         259       Generic        LED RGB – 8B   Cyc Pixels
     788       20         262       Generic        LED RGB – 8B   Cyc Pixels
     789       20         265       Generic        LED RGB – 8B   Cyc Pixels
     790       20         268       Generic        LED RGB – 8B   Cyc Pixels
     791       20         271       Generic        LED RGB – 8B   Cyc Pixels
     792       20         274       Generic        LED RGB – 8B   Cyc Pixels
     793       20         277       Generic        LED RGB – 8B   Cyc Pixels
     794       20         280       Generic        LED RGB – 8B   Cyc Pixels
     795       20         283       Generic        LED RGB – 8B   Cyc Pixels
     796       20         286       Generic        LED RGB – 8B   Cyc Pixels
     797       20         289       Generic        LED RGB – 8B   Cyc Pixels
     798       20         292       Generic        LED RGB – 8B   Cyc Pixels
     799       20         295       Generic        LED RGB – 8B   Cyc Pixels
     800       20         298       Generic        LED RGB – 8B   Cyc Pixels
```

### CYC PIXELS (CONTINUED)

```text
Channel   Universe   Address   Manufacturer   Type                     Focus/Notes
801       20         301       Generic        LED RGB – 8B             Cyc Pixels
802       20         304       Generic        LED RGB – 8B             Cyc Pixels
803       20         307       Generic        LED RGB – 8B             Cyc Pixels
804       20         310       Generic        LED RGB – 8B             Cyc Pixels
805       20         313       Generic        LED RGB – 8B             Cyc Pixels
806       20         316       Generic        LED RGB – 8B             Cyc Pixels
807       20         319       Generic        LED RGB – 8B             Cyc Pixels
808       20         322       Generic        LED RGB – 8B             Cyc Pixels
809       20         325       Generic        LED RGB – 8B             Cyc Pixels
810       20         328       Generic        LED RGB – 8B             Cyc Pixels
820       20         331       Generic        LED RGB – 8B             Cyc Pixels
812       20         334       Generic        LED RGB – 8B             Cyc Pixels
813       20         337       Generic        LED RGB – 8B             Cyc Pixels
814       20         340       Generic        LED RGB – 8B             Cyc Pixels
815       20         343       Generic        LED RGB – 8B             Cyc Pixels
816       20         346       Generic        LED RGB – 8B             Cyc Pixels
817       20         349       Generic        LED RGB – 8B             Cyc Pixels
818       20         352       Generic        LED RGB – 8B             Cyc Pixels
819       20         355       Generic        LED RGB – 8B             Cyc Pixels
820       20         358       Generic        LED RGB – 8B             Cyc Pixels
821       20         361       Generic        LED RGB – 8B             Cyc Pixels
822       20         364       Generic        LED RGB – 8B             Cyc Pixels
823       20         367       Generic        LED RGB – 8B             Cyc Pixels
824       20         370       Generic        LED RGB – 8B             Cyc Pixels
825       20         373       Generic        LED RGB – 8B             Cyc Pixels
826       20         376       Generic        LED RGB – 8B             Cyc Pixels
827       20         379       Generic        LED RGB – 8B             Cyc Pixels
828       20         382       Generic        LED RGB – 8B             Cyc Pixels
829       20         385       Generic        LED RGB – 8B             Cyc Pixels
830       20         388       Generic        LED RGB – 8B             Cyc Pixels
831       20         391       Generic        LED RGB – 8B             Cyc Pixels
832       20         394       Generic        LED RGB – 8B             Cyc Pixels
833       20         397       Generic        LED RGB – 8B             Cyc Pixels
834       20         400       Generic        LED RGB – 8B             Cyc Pixels
835       20         403       Generic        LED RGB – 8B             Cyc Pixels
836       20         406       Generic        LED RGB – 8B             Cyc Pixels
837       20         409       Generic        LED RGB – 8B             Cyc Pixels
838       20         412       Generic        LED RGB – 8B             Cyc Pixels
839       20         415       Generic        LED RGB – 8B             Cyc Pixels
840       20         418       Generic        LED RGB – 8B             Cyc Pixels
841       20         421       Generic        LED RGB – 8B             Cyc Pixels
842       20         424       Generic        LED RGB – 8B             Cyc Pixels
843       20         427       Generic        LED RGB – 8B             Cyc Pixels
844       20         430       Generic        LED RGB – 8B             Cyc Pixels
845       20         433       Generic        LED RGB – 8B             Cyc Pixels
846       20         436       Generic        LED RGB – 8B             Cyc Pixels
847       20         439       Generic        LED RGB – 8B             Cyc Pixels
848       20         442       Generic        LED RGB – 8B             Cyc Pixels
849       20         445       Generic        LED RGB – 8B             Cyc Pixels
850       20         448       Generic        LED RGB – 8B             Cyc Pixels

```

### CYC PIXELS (CONTINUED)

```text
     Channel   Universe   Address   Manufacturer   Type           Focus/Notes
     851       20         451       Generic        LED RGB – 8B   Cyc Pixels
     852       20         454       Generic        LED RGB – 8B   Cyc Pixels
     853       20         457       Generic        LED RGB – 8B   Cyc Pixels
     854       20         460       Generic        LED RGB – 8B   Cyc Pixels
     855       20         463       Generic        LED RGB – 8B   Cyc Pixels
     856       20         466       Generic        LED RGB – 8B   Cyc Pixels
     857       20         469       Generic        LED RGB – 8B   Cyc Pixels
     858       20         472       Generic        LED RGB – 8B   Cyc Pixels
     859       20         475       Generic        LED RGB – 8B   Cyc Pixels
     860       20         478       Generic        LED RGB – 8B   Cyc Pixels
     861       20         481       Generic        LED RGB – 8B   Cyc Pixels
     862       20         484       Generic        LED RGB – 8B   Cyc Pixels
     863       20         487       Generic        LED RGB – 8B   Cyc Pixels
     864       20         490       Generic        LED RGB – 8B   Cyc Pixels
     865       20         493       Generic        LED RGB – 8B   Cyc Pixels
     866       20         496       Generic        LED RGB – 8B   Cyc Pixels
     867       20         499       Generic        LED RGB – 8B   Cyc Pixels
     868       20         502       Generic        LED RGB – 8B   Cyc Pixels
     869       20         505       Generic        LED RGB – 8B   Cyc Pixels
     870       20         508       Generic        LED RGB – 8B   Cyc Pixels
     871       21         1         Generic        LED RGB – 8B   Cyc Pixels
     872       21         4         Generic        LED RGB – 8B   Cyc Pixels
     873       21         7         Generic        LED RGB – 8B   Cyc Pixels
     874       21         10        Generic        LED RGB – 8B   Cyc Pixels
     875       21         13        Generic        LED RGB – 8B   Cyc Pixels
     876       21         16        Generic        LED RGB – 8B   Cyc Pixels
     877       21         19        Generic        LED RGB – 8B   Cyc Pixels
     878       21         22        Generic        LED RGB – 8B   Cyc Pixels
     879       21         25        Generic        LED RGB – 8B   Cyc Pixels
     880       21         28        Generic        LED RGB – 8B   Cyc Pixels
     881       21         31        Generic        LED RGB – 8B   Cyc Pixels
     882       21         34        Generic        LED RGB – 8B   Cyc Pixels
     883       21         37        Generic        LED RGB – 8B   Cyc Pixels
     884       21         40        Generic        LED RGB – 8B   Cyc Pixels
```

### MTG PIXELS

```text
Channel   Universe   Address   Manufacturer   Type                     Focus/Notes
901       22         1         Generic        LED RGB – 8B             MTG Pixels
902       22         4         Generic        LED RGB – 8B             MTG Pixels
903       22         7         Generic        LED RGB – 8B             MTG Pixels
904       22         10        Generic        LED RGB – 8B             MTG Pixels
905       22         13        Generic        LED RGB – 8B             MTG Pixels
906       22         16        Generic        LED RGB – 8B             MTG Pixels
907       22         19        Generic        LED RGB – 8B             MTG Pixels
908       22         22        Generic        LED RGB – 8B             MTG Pixels
909       22         25        Generic        LED RGB – 8B             MTG Pixels
910       22         28        Generic        LED RGB – 8B             MTG Pixels
911       22         31        Generic        LED RGB – 8B             MTG Pixels
912       22         34        Generic        LED RGB – 8B             MTG Pixels
913       22         37        Generic        LED RGB – 8B             MTG Pixels
914       22         40        Generic        LED RGB – 8B             MTG Pixels
915       22         43        Generic        LED RGB – 8B             MTG Pixels
916       22         46        Generic        LED RGB – 8B             MTG Pixels
917       22         49        Generic        LED RGB – 8B             MTG Pixels
918       22         52        Generic        LED RGB – 8B             MTG Pixels
919       22         55        Generic        LED RGB – 8B             MTG Pixels
920       22         58        Generic        LED RGB – 8B             MTG Pixels
921       22         61        Generic        LED RGB – 8B             MTG Pixels
922       22         64        Generic        LED RGB – 8B             MTG Pixels
923       22         67        Generic        LED RGB – 8B             MTG Pixels
924       22         70        Generic        LED RGB – 8B             MTG Pixels
925       22         73        Generic        LED RGB – 8B             MTG Pixels
926       22         76        Generic        LED RGB – 8B             MTG Pixels
927       22         79        Generic        LED RGB – 8B             MTG Pixels

```

## Appendix 2 – Hookup Additions

### VIRTUAL MEDIA SERVERS

```text
     Channel   Universe   Address   Manufacturer   Type                             Focus/Notes
     501       NA         NA        ETC            Virtual – Server Ver 1.0         Cyc Pixels Server
     502       NA         NA        ETC            Virtual – Layer Ver 1.0          Cyc Pixels Media Layer
     503       NA         NA        ETC            Virtual – Layer Ver 1.0          Cyc Pixels Media Layer
     504       NA         NA        ETC            Virtual – Effect Layer Ver 1.1   Cyc Pixels FX Layer
     505       NA         NA        ETC            Virtual – Effect Layer Ver 1.1   Cyc Pixels FX Layer

     511       NA         NA        ETC            Virtual – Server Ver 1.0         MTG Pixels Server
     512       NA         NA        ETC            Virtual – Layer Ver 1.0          MTG Pixels Media Layer
     513       NA         NA        ETC            Virtual – Layer Ver 1.0          MTG Pixels Media Layer
     514       NA         NA        ETC            Virtual – Effect Layer Ver 1.1   MTG Pixels FX Layer
     515       NA         NA        ETC            Virtual – Effect Layer Ver 1.1   MTG Pixels FX Layer

     521       NA         NA        ETC            Virtual – Server Ver 1.0         Cyc Server
     522       NA         NA        ETC            Virtual – Layer Ver 1.0          Cyc Media Layer
     523       NA         NA        ETC            Virtual – Layer Ver 1.0          Cyc Media Layer
     524       NA         NA        ETC            Virtual – Effect Layer Ver 1.1   Cyc FX Layer
     525       NA         NA        ETC            Virtual – Effect Layer Ver 1.1   Cyc FX Layer
```

## Appendix 3 – Adding Media

### IMPORTING MEDIA CONTENT

There are three ways to import media. Those methods are:
   - Import All Pixel Map Media - An automatic method for importing
        media.
   - File Manager - A manual method for importing media.
   - Import Show Pixel Map Media - An automatic method of
        importing all media needed for the current show file. Used by
        backup and clients.

File names for media content need to follow the naming convention of file
number underscore filename. For example, 002_Volcano.mov is a file
name that would be recognized. When importing by using the file
manager, you need to number the files prior to importing. However, using
Import All Pixel Map Media allows you to specify the library and file
numbers, and the console will auto-number the file names as needed
during the import process.

### USING IMPORT ALL PIXEL MAP MEDIA

To import go to Browser>Import>Import Pixel Map Media>Import All Pixel
Map Media and select the device with the media on it.

Options in this display include:
   - {Library(1-255)} - selects the library to import media.
   - {File(0-255)} - selects the file number.
   - {Reorder Libraries} - specify whether the library on the source
       device will be renumbered. If the source device’s library is not
       numbered, it will be assigned the specified library number.
   - {Reorder Files} - specify whether the file(s) on the source device
       will be renumbered. If the source device’s file(s) is not numbered,
       it will be assigned the specified file number.
   - {Overwrite} - overwrite the existing media files.
   - {Start Import} - begins the import process. A progress bar will
       appear to indicate the status of the import process. When
       finished, click {Done}.
   - {Cancel} - stops the import and exits the display.

### IMPORTING WITH THE FILE MANAGER

     To import, go to ECU>Settings>Maintenance>File Manager

     Select the device with the media on it in one window and in the other
     window select the MediaArchive folder. Inside the MediaArchive folder,
     you will see numbered folders. Those folders correspond to libraries. You
     can copy or move files.

### EXPORTING MEDIA CONTENT

     There are two ways to export media. Those methods are:
        - Export Pixel Map Media - An automatic method for exporting
             media.
        - File Manager - A manual method for exporting media.

### USING EXPORT PIXEL MAP MEDIA

     This is an automatic method of exporting all the media used in the current
     show file. This includes any pixel map media stored in cues, presets,
     submasters, etc.

     To export, go to Browser>Export>Export Pixel Map Media
     Select the device you want to export the media content to.

     There are only two options available in this display:
        - {Start Export} - begins the export process. A progress bar will
             appear to indicate the status of the import process. When
             finished, click {Done}.
        - {Cancel} - stops the export and exits the display.

### USING FILE MANAGER

     Exporting with the file manager is very similar to importing with it. You
     select the files in the MediaArchive folder that you wish to export, and
     you can either copy or move them to your device.

## Appendix 4 – In a Multi-Console System

When using file-based media in a multi-console environment, the primary
console should be used as the ‘base’ media archive.

Media can be imported to the primary, and the backup console and/or
any other clients can then synchronize their own, local media archives
with the primary. The backup must synchronize media with the primary if
the backup must take control as the master. For clients, synchronizing the
media is optional but useful if you wish to see the media playing back in
the Pixel Map Preview display.

### STEPS FOR CONFIGURING A MULTI-CONSOLE SYSTEM

Once the Eos Family Pixel Mapping Installer has been installed on all
consoles, follow these steps to configure your multi-console system:

### SETTING UP THE PRIMARY

                   On the primary console, exit to the Eos Configuration Utility
      Step 1:
                   (ECU).
      Step 2:      Press the {Settings} button

      Step 3:      Press {General} if needed.
                   Make sure that the {Share Media Archive} box is checked.
                   This will allow for sharing of the primary’s media archive. Copy
      Step 4:
                   the path name, you will need it to setup the backup and/or
                   client.

### SETTING UP THE BACKUP AND CLIENTS

                     On the backup or client, exit to the Eos Configuration Utility
         Step 5:
                     (ECU)
         Step 6:     Press the {Settings} button

         Step 7:     Press {Maintenance}

         Step 8:     Press {Network Drives}

         Step 9:     In the Network Drives display, click the {Add} Button
                     In the Add Network Drive display, choose a drive letter for
         Step 10:
                     {Local Drive}

                     Enter in the {Network Path}. The path name is listed next to
         Step 11:
                     the primary’s {Share Media Archive} checkbox.
                     Select the appropriate console type for the {Network Path
         Step 12:
                     Type}.

                     Click {Ok}. You will now be able to access the primary’s media
         Step 13:    archive from the backup or client. This new drive will appear
                     in the browser like a USB drive.
         Step 14:    Click {Done} and launch the Eos Application.

### SYNCHRONIZING MEDIA ARCHIVES

To view media playback in the Pixel Map Preview display, you will need to
first import the required media into your backup and/or client’s local
media archive. This is done from the browser. There are two options for
importing media:
     - Import Show Pixel Map Media - This import function should be
         used by the backups and clients. It is the easiest way to ensure
         that your console will have all the media required by the current
         show file.
     - Import All Pixel Map Media - This import function should be used
         by the primary to load the base media content and later to load
         media on the fly as required. This import function provides more
         complex options, like targeting which Library and File the media
         data will be imported into.

### STEPS FOR SYNCHRONIZING SHOW PIXEL MAP MEDIA

      Step 1:      On the backup or client, navigate to the browser.
                   Expand File>Import>Import Pixel Map Media>Import Show
      Step 2:
                   Pixel Map Media

      Step 3:      Select the appropriate network drive.
                   The Import Show Media display will open. Press the {Start
      Step 4:
                   Import} button.
                   A progress bar will appear to indicate the status of the import
                   process. When finished, click {Done}. You will now be able to
      Step 5:
                   see the media playing in the Pixel Map Preview display on the
                   backup and/or clients.

     Appendix 5 – General Notes on VMS Usage

### SOFTWARE INSTALLATION

        If your desk was purchased before 1.9.6 release (January 2011), you will need
        to install a separate piece of software in addition to your Installation of the
        most recent console software.
        Go to www.etcconnect.com, navigate to the Eos Family downloads page
        Download and unzip “Pixel Map Installer v1.0.0 for Eos, Ion, PRU, RVI and PC”
        Install the same as you would a standard software update
        You MUST install separately on each device – automatic software updates do
        not work with the Pixel Map installer
        You only need to install this once on each device. Once it is installed, you will
        not need to update it with every other software update.

### DEVICES, OUTPUTS, AND SHOW LIMITATIONS

        VMS is only available on Eos, Gio and Ion, not on Element. The addresses you
        patch in a Pixel Map count toward the output limitation of your console.
        They will only count once if you patch the same address in both desk patch
        and in a Pixel Map.

        VMS has the following limitations in each show file:
           - 12 Layers per Virtual Media Server
           - 40 Pixel Maps
           - 16,384 pixels per Pixel Map

### USER-ADDED CONTENT

        Users may import their own content in to PBM. Supported media file formats
        are:
             - Images - .png, .jpg, .gif, .tiff, and .svg
             - Movies - any format that QuickTime® supports. (.3gp .3gpp .3gpp2
                .3gp2 .3g2 .3p2 .flc .h264 .hdmov .m4a .m4b .m4p .moo .moov .mov
                .movie .mp4 .mpg4 .mpg4 .mqv .mv4 .pic .pict .qif .qt .qti .qtif .tvod
                .vid)
             - Text - .txt
             - HTML - .htm, .html

        Your content storage is limited by your console hard drive. It is a good idea to
        remove content when not being used.

        When creating content for VMS, keep your output device in mind. There is
        no need to waste processing power rendering a 1080p video for a 50 pixel by
        50-pixel output range.

### COPYWRIGHTED CONTENT

        Don’t forget to observe copyright laws on any content that you are importing
        that is not your original creation.

## Appendix 6 – Media Server General Info

### WHAT IS A MEDIA SERVER?

A Media Server is a highly specialized computer with software that can
manipulate and play back images, videos, and audio content to devices
such as projectors, monitors and televisions.

Media Server Hardware consists of large storage devices (hard drives),
lots of memory and processing for managing resources, and many high-
quality video cards to render content output.

Media Server Software consists of output device configuration tools,
content import and management tools, and complex content modification
tools that allow changes to content before or while it is being played back.

### HOW DOES A MEDIA SERVER WORK?

### OUTPUT DEVICE CONFIGURATION:

    First, you need to connect the devices the Media Server is going to output
    content to, tell the Media Server what kind of device they are, and where
    they are in relation to one another:

    The Media Server Software will allow you to tell each output what type of
    device will be connected to it, as well as its resolution (how many pixels it
    contains). Generally, there is also a graphical environment to arrange the
    objects in a way that is like how they are arranged in real life.

    Because the Media Server knows each object’s true-space relation to all the
    other objects, the Media Server can map the right pixels of the content to
    the right object and its pixels:

       The actual output of your Media Server and its associated objects will be
       what content resides on the output devices:

### CONTENT IMPORT AND MANAGEMENT:

       Content is any media file that the Media Server can play back – movies,
       photos, animations – whatever the Media Server’s software and graphics
       cards can render. These differ by manufacturer.
       Because Media Servers are controlled by DMX values (more about this in
       Control), their content file structure is very specific. Most media servers
       allow you to have up to 256x256 – or 65,536 – individual pieces of content.
       So why the odd limit on pieces of content?
       Media Servers use 2 DMX addresses like Coarse and Fine control on a moving
       light for content navigation (think Pan & Tilt). And just like moving lights,
       each coarse step – 256 total – has a full range of Fine steps – 256 total
       (65,536 total possible combinations of Coarse and Fine).
       Thus, a Media Server uses 256 folders in its content library – like the Coarse
       parameter on a moving light – and each folder can contain up to 256 pieces
       of content – like the Fine parameter (65,536 total possible combinations of
       folder and file).

       So, you could load a specific piece of content by going to folder (Coarse) 15,
       and file (Fine) 158.
       All Media Servers have ways to import your content into the server. Most
       servers will help you organize your content by starting the folder and file
       names with a number from 000 to 255. Many servers allow a user-defined
       name to follow the numeric code in the folder or file name. A file path might
       look like:
       D:/MediaArchive/015-Lava/158-Red_Lava_Fast.mov

### MEDIA SERVER CONTROL:

So now you have a remote computer with tons of video and images loaded
on to it, and lots of output devices connected to receive the content. How do
you get your Eos or Ion to make the Media Server work?
A moving light uses multiple DMX addresses, each controlling a different
parameter in the fixture:

Each motor that is associated with a parameter listens to its own DMX
address – move the DMX value, move the motor.
Luckily, Media Servers behave a lot like moving lights when it comes to
control, only there are no motors to move. Each controllable parameter of
the Media Server is listening to its own DMX address – move the DMX value,
change the parameter:

### SERVER AND LAYER CHANNELS:

One final common element to all Media Servers is the server and layer
channel structure. Think of the server channel as a grandmaster and the
layer channels as submasters. The layer (just like a sub) controls individual
pieces of content – you can have multiple layers with different values to
create a single look. However, your server (just like a grandmaster) affects
ALL your layers. So, if you take your server channel to 50% intensity, all layer
channels will be limited to 50% of their current value.
In the Media Server software, there is a utility to assign DMX start addresses
to the server channel and each of the layer channels. You will need this
information to patch the Media Server in the console, just like when you
patch a moving Light.
The number of layers you can use depends on the model of Media Server
you have. Just like subs, the more layers you have, the more individual
control you have. But more layers usually mean using a more expensive
Media Server. For basic Media Server programming, four layers are usually
enough. When we start controlling Media Servers, we’ll discuss some
situations that may require more layers.

### PATCHING AN EXTERNAL MEDIA SERVER

### PATCHING THE MEDIA SERVER CHANNEL:

             In {Patch} - By Channel Format

             [171]                            select channel for server

             {Type}                           select manufacturer

             {Green Hippo}                    select Green Hippo

             {Hippo} {V3.2 Master}            assigns type as a server

             [At] [8] [/] [1] [Enter]         patches the server at address 8/1

### PATCHING THE LAYER CHANNELS:

             [172] [Thru] [175]               selects four channels for media layers

             {Type}                           select manufacturer

             {Green Hippo}                    select Green Hippo

             {Hippo} {V3.2 Media}             assigns type as media layers

             [At] [8] [/] [61] [Enter]        patches layers starting at address 8/61

Corporate Headquarters  Middleton, WI, USA  Tel +608 831 4116  Service (Americas) service@etcconnect.com
London, UK  Tel +44 (0)20 8896 1000  Service (UK) service@etceurope.com
Holzkirchen, DE  Tel +49 (80 24) 47 00-0  Service (DE) techserv-hoki@etcconnect.com
Hong Kong  Tel + 852 2799 1220  Service (Asia) service@etcasia.com
Paris, FR +33 1 4243 3535
Web etcconnect.com  © 2020 Electronic Theatre Controls, Inc.  Trademark and patent info: etcconnect.com/ip
Product information and specifications subject to change. ETC intends this document to be provided in its entirety.

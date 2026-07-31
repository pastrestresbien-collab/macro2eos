# Eos Family User Manual v3.2.0 — Chapitre 27 : Virtual Media Server

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 27
## Virtual Media Server
### Virtual Media Server

The virtual media server feature of Eos is comprised of two areas, the virtual media server and its virtual layers, and pixel maps. These areas are completely dependent on each other.

The virtual media server is a feature used to create layouts of fixtures, known as pixel maps, which then applies media content (images, movies, text, and procedurally generated effects) by way of virtual media layers to the pixel map.

A pixel map is a layout of fixtures onto a grid, which determines order of playback and how the data will be interpreted and outputted to create the desired image or effect. A pixel map creates relationships among the channels in an X-Y grid so that the channels and their parameters can be associated with pixels in an image.

A virtual media layer contains one piece of media content. A pixel map can contain up to 12 virtual media layers, which can be stacked on top of each other or used separately.

### Pixel Map Media

Image, video, HTML, and text files can be applied to a pixel map. A stock library of media can be obtained by installing the Eos Family Pixel Mapping Installer.

#### Importing Media Content

Additional media content can be imported. Files must follow the naming convention filenumber_filename; for example, [002_Volcano.mov]{.underline}.

Size, resolution and length of any imported content should be as minimal as possible. For example, stock video content is under 10MB, under 320x180 resolution, and between 2-20 seconds.

added via the following methods.

##### Import All Pixel Map Media

Automatically import media via File > Import > Pixel Map Media > All Pixel Map Media. Options when importing include:

-   {Library (1-255)} - selects the library to import media.

-   {File (0-255)} - selects the file number.

-   {Reorder Libraries} - specify whether or not the library on the source device will be renumbered. If the source device's library is not numbered, it will be assigned the specified library number.

-   {Reorder Files} - specify whether or not the files on the source device will be renumbered. If the source device's file(s) is not numbered, it will be assigned the specified file number.

-   {Overwrite} - overwrite the existing media files.

-   {Start Import} - begins the import process. A progress bar will appear to indicate the status of the import process. When finished, select {Done}.

-   {Cancel} - stops the import, and exits the display.

##### Import Show Pixel Map Media

Automatically import all media needed for the current show file used by backup and client consoles via File > Import > Pixel Map Media > Show Pixel Map Media.

> For more information on synchronizing media content, see *Synchronizing Media Archives (on page 559)*.

##### Import with the File Manager

> Manually import media via the ECU > *Settings > Maintenance (on page 589)* > {File Manager\...}. Files should be numbered manually prior to import.

#### Supported Media Formats

##### Image

-   .gif

-   .jpg

-   .png

-   .svg

-   .tiff

##### Video

The following video formats are recommended:

-   .gif

-   .mov (.H264 encoding)

-   .mp4

For a full list of supported video formats, please consult [etcconnect.com](https://www.etcconnect.com/).

##### HTML & Text

-   .htm

-   .html

-   .txt

#### Exporting Media Content

##### Export Pixel Map Media

Automatically export all the media used in the current show file via File > Export > Show Pixel Map Media, selecting the device to which you want to export the media content. This includes any pixel map media stored in cues, presets, submasters, etc.

There are only two options available in this display:

-   {Start Export} - begins the export process. A progress bar will appear to indicate the status of the import process. When finished, select {Done}.

-   {Cancel} - stops the export and exits the display.

##### Export with the File Manager

Exporting with the file manager is very similar to importing with it. You select the files in the MediaArchive folder that you wish to export, and you can either copy or move them to your device.

### Setting Up Pixel Maps

A pixel map is a layout of fixtures onto a grid, which determines order of playback and how the media content will be interpreted and output to create the desired image or effect. A pixel map creates relationships among the fixtures in an X-Y grid so that the channels and their parameters can be associated with pixels in an image.

Limitations of pixel maps include:

-   40 pixel maps per show file

-   12 layers per pixel map

-   16,384 pixels per pixel map grid

Open up the pixel map display via [Displays] > {More SK} > {Pixel Maps}. The display can also be opened from the home screen, or by using [Tab] [9].

> **Note:** *Hovering your cursor above the pixel map will display the column and row location for the pixel.*

In the pixel map display, any numeric entry is assumed to be a pixel map. Each pixel map must have a unique number.

To create a pixel map, type in the number you want to assign to it and hit [Enter].

#### Assigning Layers

The virtual media server and layer(s) need to be assigned to the pixel map.

*(figure omise)*{width="5.393685476815398in" height="0.8074989063867016in"}

Using the softkeys, select {Server Chan}, {Media Layer Chan}, and {Effect Layer Chan}, and associate them with the channels you want to patch. If those channels are unassigned, Eos will automatically patch them accordingly. An error will appear if any channels are assigned to a different device type.

If you prefer to assign Pixel Map layers in Patch first, profiles are available under {Type} >

{Manufctr} > {ETC Fixtures} > {Virtual}.

**Note:** *No addresses need to be assigned in Patch for the pixel map layers.*

In this display you can also label the pixel map, assign the interfaces it will use, and adjust the width and height. Column and row guides can be created numerically in either the pixel map or in the Edit displays. The guides can aid in viewing a pixel map.

### Setting Pixel Map Features

After layers have been patched, press the {Edit} softkey to select the fixtures.

In the Edit screen, you will be able to define the array and types of fixtures. To do this, you can select pixels from the map by using a touchscreen or by holding down the left button on a mouse and dragging across the pixels you wish to select.

Once the pixels have been selected, you need to select their fixture type and then assign the starting address or starting channel.

-   When either {Starting Channel} or {Starting Address} is selected, both fields will be cleared.

-   Address-based pixels can not overlap with channel-based pixels. This includes the entire DMX fixture footprint.

-   If using {Starting Channel}, any overlapping channel-based pixels will be removed and any overlapping address-based fixtures will be unpatched.

-   If using {Starting Address}, any overlapping address-based pixels will be removed and any overlapping channel-based fixtures will be unpatched.

-   When the [Data] key is latched, the address for channel-based pixels will display.

-   When [Format] is pressed, the address will toggle between port/offset and address number.

By default, the addresses will be organized in rows starting from the left to the right and top to bottom. The edit screen shows a representation of the current mapping. The pixels are color coded based on if they have been patched or not. A color coding guide is provided on the screen.

> **Note:** *Any pixel can have its size adjusted for better representation of the actual fixtures. This is done by selecting the pixel and then dragging the vertical and / or horizontal borders.*
>
> **Note:** *A pixel map can be moved within the edit display by holding down the right mouse button. The map can be zoomed either by using a mouse wheel or by holding down [Format] and moving the level wheel.*

Options available for changing the mapping:

-   {Horizontal Order} - toggle state from left to right to right to left

-   {Vertical Order} - toggle state from top to bottom to bottom to top

-   {Direction} - toggle state from rows to columns

-   Click the {Apply} button to see the changes made while still in the edit display. In the edit display, the softkeys will repaint to the following mapping options:

> **Note:** *To see the changes made by using the softkey mapping options, you don\'t need to press {Apply}.*

-   {Rotate 90}

-   {Flip V}

-   {Flip H}

-   {Invert}

The {Flash} button can be used to check the address output while still in the edit display.

{Flash} works the same as it does in Live.

When editing is finished, press the {Done} softkey to exit the edit display.

### Working with the Virtual Media Server

Before you begin working with the Virtual Media Server, you will want to open the Pixel Map Preview display from the home screen or by using [Tab] [1][0]. Pixel maps can be manipulated via encoders, ML Controls, by opening [Tab] [5], or via the quick access tools.

> **Note:** *For any output, the Server Channel must be set to a level along with any layers you are using.*
>
> **Note:** *You can use Park and Address Check for Virtual Media Server outputs.*

#### Server Channel Controls

When working with the Server Channel, the following controls will be available:

-   {Intensity}

-   {Pan} and {Tilt} - used to adjust layers within the frame.

-   {Color} - filters color for all layers.

-   {FoView} - field of view, or perspective. This only affects media when {X Rotate} and/or

> {Y Rotate} are not set to 0.

-   {Crossfade} - used to adjust the priority when devices in the pixel map are also used as console channels. -100 gives the pixel map priority, and +100 give the console channel priority. At 0 (the default) the output is calculated using HTP. The Virtual Media Server crossfade parameter level will display in subscript beside the intensity.

-   {Blend} - a smoothing function for crossfades. It is a linear parameter that defaults to zero.

-   {Inactive Media Behavior} - sets the layer behavior when intensity is at 0 to one of the following options:

    -   Stop / Unload Layers - stops the media, and unloads it from memory

    -   Pause Layers - stops the media, but leaves it loaded in memory

    -   Let Layers Play - media continues playing with 0 intensity

-   {Scale} - adjusts scale of all layers.

-   {Aspect Ratio} - adjusts aspect ratio of all layers.

-   {XYZ Rotation Controls} - rotation control for all layers

#### Layer Channel Controls

When working with the Layer Channels, the following controls will be available:

-   {Intensity}

-   {Pan} and {Tilt} - used to adjust the image of the individual layer within the frame.

-   {Color} - filters the color of the content. For example, if all the colors are set to full, the content will play all colors normally. However if blue is at 0, then only the red and green pixels of the content will play. The color and gel pickers can be used to select color filtering quickly.

-   {Negative On/Off} - with negative on, the output is the negative of the content. With it off, the content plays back normally.

-   {Image Brightness} - this varies from intensity. The following images illustrates the differences between image brightness and intensity.

> **Note:** *All Virtual Media Layers operate in 16-bit color mode.*

*(figure omise)*{width="4.954593175853018in" height="1.9534372265966755in"}

-   {Playback Mode 1}:

-   {Display Centered}

-   {Display In Frame}

-   {Display Out Frame}

-   {Play Loop Forward}

-   {Play Loop Reverse}

-   {Play Once Forward}

-   {Play Once Reverse}

-   {Stop}

-   {Playback Speed}

-   {In Point} - determines where in the clip (frame number) you want to enter in.

-   {Out Point} - determines where in the clip (frame number) you want to exit.

-   {Mix Modes} - sets how the layers will interact. The following table shows the various mixer modes available. To illustrate the modes, the following layers were used:

*(figure omise)*{width="1.575in" height="1.130624453193351in"}

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Mode                        Description                                                                                    Result
  --------------------------- ---------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------
  {Over} (Default)            Top layer blended with bottom layer                                                            *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {In}                        Top layer with opacity reduced by opacity of bottom layer                                      *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Out}                       Top layer with opacity reduced by inverse opacity of bottom layer                              *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Atop}                      Top layer with opacity reduced by opacity of bottom layer and then blended with bottom layer   *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Mode                        Description                                                                               Result
  --------------------------- ----------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------
  {Add}                       Top and bottom layers color and opacity added together                                    *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Subtract}                  Top and bottom layers color and opacity subtracted from each other                        *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Multiply}                  Top and bottom layers color and opacity multiplied together                               *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Screen}                    Top and bottom layers colors inverted and then multiplied together                        *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Overlay}                   Does a multiply or screen effect based on the lightness or darkness of the bottom layer   *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Lighten}                   Top layer's color merges with bottom layer's color, with the lighter color winning        *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Darken}                    Top layer's color merges with the bottom layer's color, with the darker color winning     *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Mode                        Description                                                                                                                                                              Result
  --------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------
  {Dodge}                     Bottom layer's color brightened to reflect top layer's color                                                                                                             *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Burn}                      Bottom layer's color darkened to reflect the top layer's color                                                                                                           *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Hard Light}                Does a multiply or screen effect on the lightness or darkness of the top layer                                                                                           *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Soft Light}                Darkens or lightens colors depending on the top layer                                                                                                                    *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}

  {Xor}                       Top layer with opacity reduced by inverse opacity of bottom layer, and then blended with the bottom layer with opacity reduced by the inverse opacity of the top layer   *(figure omise)*{width="1.1066666666666667in" height="1.1066666666666667in"}
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   {Library} - selects the image library.

-   {File} - selects the media file within the selected library.

-   {Mask On/Off} - masks takes a lower layer and a higher layer, finds only the non-transparent pixels they have in common, and then displays the common pixels of the higher layer.

-   {FoView} - perspective. This only affects media when {X Rotate} and/or {Y Rotate} are not set to 0.

-   {Loop In} - sets the starting point of a gradient.

-   {Loop Out} - sets the ending point of a gradient.

-   {Scale} - changes the scale of the content to either be larger or smaller than the standard content playback.

-   {Aspect Ratio} - stretches or shrinks the content only along the X axis, making it wide or

-   squished looking. Z Rotate can be used to modify the aspect ratio along the Y axis.

-   {XYZ Rotation Controls} - rotation control for all layers.

### Effect Layers

The Virtual Media Server allows you to use procedurally generated content. This is content that is created algorithmically in real time, instead of rendering file based media.

In order to use procedurally generated content, you must patch the pixel map layer as a virtual effect layer instead of a virtual media layer. Setting up the pixel map is the same as for using virtual media layers. There are two versions of the effect layer, {Effect Layer Ver 1.0} and

{Effect Layer Ver 1.1}.

#### Types of Effects

*(figure omise)*{width="1.4440409011373578in" height="1.7475in"}

There are three main effect types:

-   Two color gradients - adjustable gradients with start and end colors

-   Rainbow gradients - fixed gradient, full hue spectrum

-   Perlin noise - good for animating random color effects, adjustable gradients

The effects are stored in file 1. File 1:0 is a home position of no effect. 1 through 3 are perlin noise effects, 4 is a perlin noise/ rainbow gradient, 5 through 9 are rainbow gradients, and 10 through 19 are two color gradients.

Effects have various options of additional control.

##### Using Two Color Gradients

For the effects that use two color gradients (two color and perlin noise), there are several options for control of the gradients. The two colors are known as the start and end colors. Those options include:

-   {Intensity} and {Intensity 2} - specifies the opacity of the start and end colors respectively for Virtual Effect Layer 1.0. If you want to fade a two color effect using this layer, you will need to fade both {Intensity} and {Intensity 2}.

-   {Intensity 2} and {Intensity 3}- specifies the opacity of the start and end colors respectively. {Intensity} is a master opacity control for the entire layer. This is for Virtual Effect Layer 1.1. If you want to fade a two color effect using this layer, you can just fade the {Intensity}.

-   {Red}, {Green}, {Blue} or {Hue} and {Saturation} - specifies the start color. You can also use the Start Color picker.

-   {Red 2}, {Blue 2}, and {Green 2} - specifies the end color. You can also use the End Color picker.

-   {In Point 1} and {Out Point 1} - changes the distribution of the two colors in the gradient. In Point 1 moves the start color position closer to the end color. Out Point 1 moves the end color position closer to the start color.

-   {Playback Mode 1} - basic animation, forward or reverse.

-   {Playback Speed 1} - speed of animation.

-   {Layer Effect} - adjusts the number of repeats in the gradient. Layer Effect has a range of

> -100% to 100%. At the home value of 0%, one full gradient is shown. Moving toward 0%, you will see less of the gradient and moving toward 100%, you will see up to four repetitions of the gradient.
>
> **Note:** *The button {Layer Effect 2} is for use with perlin noise effects.*

##### Using Rainbow Gradients

For Rainbow Gradients, the colors cannot be adjusted. But the number of repeats can be adjusted by using {Layer Effect}. {Playback Mode 1} and {Playback Speed 1} work in the same way as for two color gradients.

##### Using Perlin Noise

For perlin noise effects, there are different options for control:

-   {Playback Mode 1} - basic animation of noise, forward or reverse.

-   {Playback Speed 1} - speed of animation.

-   {Layer Effect} - adjusts the amount of noise. -100% equals very little noise, and 100% equals a lot of noise.

-   {Layer Effect 2} - adjusts the horizontal scrolling speed. -100% equals a fast left scroll, 0% equals no scrolling, and 100% equals a fast right scroll.

##### Effects Color Pickers

The effect layers have a two color pickers for selecting the start and end colors.

*(figure omise)*{width="4.1149562554680665in" height="1.9693744531933508in"}

Using the buttons located between the two color pickers, you can also copy the start color to the end color, swap the start color and the end color, or copy the end color to the start color.

### Pixel Mapping in a Multi-Console System

When using file based media in a multi-console environment, the primary console should be used as the 'base' media archive.

Media can be imported to the primary, and the backup console and / or any other clients can then synchronize their own, local media archives with the primary. The backup must synchronize media with the primary in the event that the backup must take control as the master. For clients, synchronizing the media is optional but useful if you wish to see the media playing back in the Pixel Map Preview display.

#### Steps for Configuring a Multi-Console System

Once the Eos Family Pixel Mapping Installer has been installed on all consoles, follow these steps to configure your multi-console system:

Setting up the Primary

1.  On the primary console, exit to the Eos Configuration Utility (ECU).

2.  Press the {Settings} button.

3.  Press {General} if needed.

4.  Make sure that the {Share Media Archive} box is checked. This will allow for sharing of the primary's media archive. Copy the path name, you will need it to setup the backup and / or client.

*(figure omise)*{width="4.024298993875766in" height="1.8140616797900262in"}

5.  Setting up the Backup and Clients

6.  On the backup or client, exit to the Eos Configuration Utility (ECU).

7.  Press the {Settings} button.

8.  Press {Maintenance}.

9.  Press {Network Drives}.

*(figure omise)*{width="1.8027580927384077in" height="1.6672911198600175in"}

10. In the Network Drives display, click the {Add} button.

11. In the Add Network Drive display, choose a drive letter for {Local Drive}.

*(figure omise)*{width="1.7349781277340333in" height="1.24375in"}

12. Enter in the {Network Path}. The path name is listed next to the primary's {Share Media Archive} checkbox.

13. Select the appropriate console type for the {Network Path Type}.

*(figure omise)*{width="2.186926946631671in" height="1.0571872265966755in"}

14. Click {Ok}. You will now be able to access the primary's media archive from the backup or client. This new drive will appear in the browser like a USB drive.

15. Click {Done} and launch the Eos application.

#### Synchronizing Media Archives

To view media playback in the Pixel Map Preview display, you will need to first import the required media into your backup and / or client's local media archive. This is done from the browser. There are two options for importing media:

-   Import Show Pixel Map Media - This import function should be used by the backups and clients. It is the easiest way to ensure that your console will have all of the media required by the current show file.

-   Import All Pixel Map Media - This import function should be used by the primary to load the base media content and later to load media on the fly as required. This import function provides more complex options, like targeting which Library and File the media data will be imported into. See *Pixel Map Media (on page 548)*.

Steps for Synchronizing Show Pixel Map Media

1.  On the backup or client, navigate to the browser.

2.  Expand File>Import>Import Pixel Map Media>Import Show Pixel Map Media.

*(figure omise)*{width="4.4409864391951in" height="1.2643744531933507in"}

3.  Select the appropriate network drive.

4.  The Import Show Media display will open. Press the {Start Import} button.

5.  A progress bar will appear to indicate the status of the import process. When finished, click {Done}. You will now be able to see the media playing in the Pixel Map Preview display on the backup and / or clients.

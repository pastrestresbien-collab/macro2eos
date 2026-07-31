# Eos Family User Manual v3.2.0 — Chapitre 26 : Augment3d

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 26
## Augment3d
### Augment3d

Augment3d is an Eos tool that allows you to configure and focus virtual representations of your fixtures in a 3D environment, as well as program and visualize looks.

### Hardware and Software Requirements

#### Console

Augment3d on Eos Family consoles requires Eos Family Software v3.0.0 or later, and a console with at least one Display Port connector.

#### PC / macOS

For the most up-to-date specifications for Augment3d on PC or Mac, please visit [etcconnect.com/etcnomad/performance/](https://etcconnect.com/etcnomad/performance).

#### iOS / Android

Augment3d includes a feature inside of the iRFR and aRFR mobile apps. iRFR requires iOS 11 or later. aRFR requires Android OS 7.0 (Nougat, sdk 24) or later.

> **Note:** *Focus wand also requires ARKit/ARCore functionality. Check your device\'s specifications to ensure compatibility, or reference the Augment3d Reality Support* *field in the app\'s About menu.*

### Running Augment3d

#### Console / PC / Mac

> Eos Family consoles and computers that meet the hardware and software requirements can run Augment3d natively (see *Hardware and Software Requirements (above)*).

*(figure omise)*{width="2.505084208223972in" height="0.92625in"}

Either open a new tab and select {Augment3d} from the Displays list, or hold down [Tab] and type [38].

> **Note:** *In console implementation, Augment3d render quality is limited to Low or Medium.*

#### PC / Mac (Tether Mode)

You can also run Augment3d on a separate computer, connected to a console using tether mode. Augment3d tether is an extension of the console it is connected to, rather than a standalone client.

The setup for this mode is identical to that of an ETCnomad client computer in a networked system of consoles. An ETCnomad dongle is not required for Augment3d tether.

> **Note:** *Eos Puck is considered a console, and is subject to the console restrictions above.*

1.  Ensure the computer is running the version of ETCnomad that matches the software version installed on the connected console.

2.  On the console, enable Augment3d for your user number. In the CIA, navigate to Setup

    -   System > Users.

*(figure omise)*{width="2.951502624671916in" height="1.1558333333333333in"}

3.  Connect your computer using an Ethernet cable through a network switch. Ensure that the computer\'s network information is in a compatible range with the console.

4.  Launch ETCnomad and select {Augment3d Tether}. Augment3d will launch in its own window, and try to connect to the console.

5.  Choose the correct tether device on the console (see *Augment3d (on page 233)*).

*(figure omise)*{width="2.7106364829396323in" height="0.5462489063867016in"}

To exit tether mode, click the {X} in the corner. To exit when in Edit mode, choose File > Exit.

##### Tether Command Line

*(figure omise)*{width="1.2666655730533682in" height="0.12666666666666668in"}

A command line can be displayed on the tethered device, which will mirror the command line on the connected console.

With the keyboard button toggled on, both Eos and Augment3d commands will be sent from the tether to the console. When toggled off, only Augment3d commands will be sent.

Click the {X} to disable the tether command line entirely, or toggle it from Window > Command Line.

#### Standalone ETCnomad

Augment3d can be run on a PC or Mac in a local tab as part of ETCnomad v3.0.0 and later, and used without a connected Eos Family console. Once ETCnomad v3.0.0 or later is installed, no additional installation is necessary.

### Augment3d Key Terms

The following are specific terms and definitions of various features unique to Augment3d.

-   Click-To-Focus - clicking or touching a point in the Augment3d model to perform XYZ programming on that point.

-   Control Mode - the default display mode of Augment3d. Allows for visualization and navigation of your model, fixtures, and objects.

-   Edit Mode - an alternate Augment3d mode. Allows for editing and configuration of your model, fixtures, and objects.

-   Find Me - using aRFR/iRFR to perform XYZ programming aimed at the mobile device.

-   Focus Wand - using aRFR/iRFR to perform click-to-focus.

-   FPE - Fixture Position Estimation. Estimates the physical locations of fixtures based on fixture profile information and user-provided focus palettes.

-   Origin - a known location in your space, represented as the intersection of the XYZ axes (0,0,0), that acts as a reference point for the measurements of the rest of your Augment3d model.

-   Pan / Tilt Kinematics - an aspect of a fixture profile that turns DMX values into a direction the beam is pointing.

-   Model - the Augment3d virtual 3D space.

-   XYZ Programming - telling the console to aim a fixture\'s beam through a particular point in virtual space.

-   Zones - objects in the Augment3d model that can automatically trigger various fixture behaviors.

### Navigation in Augment3d

#### Keyboard

> In *Augment3d Control Mode (on the next page)*, use the standard arrow keys to move the camera around the Augment3d space. In *Augment3d Edit Mode (on page 501)*, both the standard arrow keys and WASD keys may be used.

-   W / UP - moves the camera up.

-   SHIFT + W / UP - moves the camera forwards in the direction it is current facing.

-   A / LEFT - moves the camera to the left.

-   S / DOWN - moves the camera down.

-   SHIFT + S / DOWN - moves the camera backwards in the direction it is currently facing.

-   D / RIGHT - moves the camera to the right.

Tap any key to increment or decrement the camera position, or hold the key down to move smoothly.

#### Mouse

-   RIGHT MOUSE - drag to rotate the camera to look around the model.

-   CENTER MOUSE - drag to pan the camera in the current perspective.

-   ALT + RIGHT MOUSE - drag for orbital control.

-   CTRL + RIGHT MOUSE - drag to pan the camera in the current perspective.

> **Note:** *Use keyboard and mouse controls simultaneously for optimal navigation control.*

#### Eos Snapshots

Camera view and other Augment3d settings can be saved directly in Eos Snapshots for quick playback.

### Augment3d Control Mode

Control Mode is the default Augment3d view, allowing for visualization and navigation of your space, fixtures, and objects.

*(figure omise)*{width="5.93824365704287in" height="3.4825in"}

Collectively, the Augment3d virtual environment is referred to as the model. All fixtures and objects must be part of the model in order to be configured.

> In Control Mode, a command line can be toggled on or off on a connected Augment3d tether. For more information, see *Tether Command Line (on page 497)*.

#### Toolbar

Limited toolbar options are available in Control Mode:

-   *Camera Tool (on page 515)*

-   *Focus Tool (on page 516)*

-   *Labels Tool (on page 516)*

-   *Sticks Tool (on page 517)*

-   *Light Tool (on page 517)*

-   *Options Tool (on page 517)*

### Augment3d Edit Mode

Edit Mode is the secondary Augment3d view, allowing for editing and configuration of your space, fixtures, and objects.

*(figure omise)*{width="5.94321741032371in" height="3.4854166666666666in"}

Surrounding the central workspace are primary windows to assist in fixture and object manipulation: the Library, Materials, Preferences, Hierarchy, and Inspector. These windows can be freely dragged, rearranged, re-sized, and closed.

#### Using Edit Mode

To enter Edit Mode, press the {Edit} button in the upper-right corner.

> **Note:** *Only one console in a multi-console system can be in Edit Mode at a time.*

*(figure omise)*{width="1.0555872703412073in" height="0.8589577865266842in"}

To exit Edit Mode, select {Done}. Choose whether to apply the changes you have made to the Augment3d model, or revert them and exit without saving changes.

In a multi-console system, only one console can edit the Augment3d model at once. If a connected console is already in Edit Mode, the option to force revert changes appears. This option will revert all changes made by the console currently in Edit Mode and exit all consoles from Edit Mode. It is not possible to undo or recover reverted changes.

> **CAUTION:** *Do not use Eos Undo operations via the command line while editing an Augment3d model, as it can alter your show data unexpectedly. Full Undo options for Augment3d will be implemented in a future Eos software release.*

#### XYZ & Origin

In Edit Mode, Augment3d models are arranged around three axes; horizontal X (red) and Y (green), and vertical Z (blue).

*(figure omise)*{width="4.076937882764654in" height="2.244374453193351in"}

The point at the intersection of these axes (0,0,0) is the origin. This virtual point in Augment3d must correspond to a real point in your space, ideally on the floor. This could be in the center of your stage, in a corner, or any convenient point.

All other measurements in Augment3d reference the origin. To improve the accuracy of your model, choose a physical point that is easily accessible for measurements.

##### Units

By default, Augment3d measures distance in metric (meters). This can be changed in Setup

-   System Settings > System > *Metric / Imperial (on page 213)*.

*(figure omise)*{width="1.4542935258092737in" height="1.0643744531933508in"}

Available options are meters, decimal feet, or feet and inches.

#### Library

The Library contains all of the non-fixture items in an Augment3d project and comes preloaded with a large number of stock objects for your convenience. You can also import your own Augment3d objects (see *Importing Augment3d Objects (on page 541)*).

> *(figure omise)*{width="1.5452723097112862in" height="1.6070833333333334in"}

Drag objects to add them from the Library into your model at the origin. Use the Search function to quickly locate specific items. Create folders from the dropdown to organize Library items.

##### Library Items

###### Objects

Any objects contained in the Stock folder can be added to an Augment3d model (see

> *Augment3d Objects (on page 536)*).
>
> Any custom objects imported into Eos will also appear here (see *Importing Augment3d Objects (on page 541)*).

###### Nodes

> Nodes can be associated with one or more Augment3d objects in the *Hierarchy (on page 511)*. This allows those objects to be controlled together; for example, as patched scenic elements (for more information, see *Scenic Elements (on page 537)*).

Scenic elements can be given intensity values, moved, rotated, etc. This allows you to change the visibility and position of Augment3d objects using cues, submasters, and so on.

###### Groups

A group is an Augment3d object designed to be the parent of other objects which have their own unique coordinates. Fixtures that have a group parent will display their relative coordinates in Patch.

A group cannot be scaled, but can be moved and / or rotated. Moving or rotating the group node will move or rotate all of its child objects.

###### Zones

> Zones are objects in the Augment3d model that can automatically trigger various fixture behaviors. See *Augment3d Zones (on page 537)*.

###### Labels

Labels are floating text that can be positioned anywhere in your Augment3d model.

#### Materials

Materials in Augment3d are collections of assets that can be applied to objects. Materials can affect aspects of an object\'s appearance like color, texture, reflectiveness, and so on.

> **CAUTION:** *Augment3d materials are referenced data, meaning any material edits will be reflected across all objects with those materials applied.*

##### Materials Library

*(figure omise)*{width="5.825768810148731in" height="3.915in"}

Navigating to Window > Materials will open a window with the materials library, containing all stock materials, along with any you have created or imported.

> **Note:** *Stock materials cannot be edited or deleted. To alter a stock material, duplicate it and make changes to the copy.*

Search for materials using the search bar. The dropdown menu allows you to create folders for further organization, or create new materials.

Materials can be dragged from the materials library into the Augment3d scene, and dropped onto objects or object subcomponents to apply the material directly.

*(figure omise)*{width="5.847887139107612in" height="2.3558333333333334in"}

Selecting a material in the library will display the following options:

-   Name - the name of the material.

-   Duplicate - this button creates a copy of the selected material.

-   Base Color - the underlying color used for the material.

-   Base Color Image - the texture for the material. If transparent, the base color will show through.

Color materials only contain a base color. Texture materials have an additional base color image, for which the following properties are available:

-   Metallic - adjusts the reflectiveness between dielectric / absorbing some light (0) to pure metal / reflects all light (1).

-   Smoothness - adjusts the texture between roughest (0) and polished (1).

-   Rotate - rotates the base color image in degrees.

    -   Quick buttons are also available to rotate the material 90° CCW and CW, mirror left/right, and mirror top/bottom.

-   Alignment - changes the texture\'s alignment on the object along the X and Y axes of the object\'s UV map (0-0.9).

-   Repeat - alters the texture\'s size by setting how many times it repeats along the X and Y axes between fewest repeating patterns (1) and most repeating patterns (100).

Accurately editing the properties above may rely on knowing the UV mapping of an object, the 2D representation of how materials are applied to the 3D surface. To aid in this, duplicate the stock UV Map texture (Stock > Textures > Miscellaneous > UV Map) and temporarily apply it to your object to see the stock mapping. Edit the properties above to test how your changes will be applied to the object with a different texture.

##### Materials in the Inspector

*(figure omise)*{width="3.2916666666666665in" height="2.46875in"}

Selecting an object in the *Hierarchy* will display associated information in the *Inspector*. Selecting in the Materials field will show a list of all materials currently applied to that object.

> **Note:** *Complex objects can be expanded to view and edit the materials for the object\'s component parts.*

Select a material to open a dropdown version of the materials library, where new materials can be selected. New colors can quickly be added using the color picker and material name options from the color column. Materials with image assets have additional adjustment options to alter image alignment, rotation, and scale for the selected object.

To save changes and close the materials list, use the checkmark icon. To revert changes, use the counterclockwise icon.

##### Importing Materials

Custom materials can be imported into Augment3d *Using the Browser (on page 83)* via File > Import > Augment3d Scenic Materials, or from Augment3d Edit Mode via File > Import to Library > Import 3D Model. If a tether and a console are connected, objects must be imported via Augment3d Edit Mode on the tether device. A confirmation will appear for successful imports.

> **CAUTION:** *Custom materials must be applied to an object in order to be saved with the show file. Custom materials not applied are shown in darker text and will be deleted upon shutdown of Augment3d.*

Custom materials can be created by adding images of the following formats to a zipped folder:

-   JPG

-   PNG

-   SVG

-   SVGZ

-   WEBP

The images must match the following naming conventions:

-   Base Color image - filename_base_color.jpg/png

-   Normal Map image (optional) - filename_normal_map.jpg/png If a map image is not included, the stock mapping will be used.

Additional materials resources are also available on the ETC website, [etcconnect.com](http://www.etcconnect.com/).

#### Augment3d Preferences

Preferences contains all the settings for your Augment3d model.

> **Note:** *Many of these options can also be changed from the toolbar. For more information, see Augment3d Toolbar (on page 515).*

##### Editor

*(figure omise)*{width="3.1059383202099737in" height="1.2072911198600176in"}

###### Grid

Toggles the grid on or off. Also available in Toolbar > Grid.

###### Snap

Toggles object placement snapping to the grid on or off. Also available in Toolbar > Snap.

###### Snap Distance

Sets the distance increment for the spacing of the grid, along with object placement snapping (in the chosen global unit).

###### Angle

Sets the angle increment for object placement snapping (in degrees).

###### Focus Height

Sets the Focus Height offset. Also available in Toolbar > Focus.

###### Origin

Toggles the origin point marker on or off.

###### Show Refresh Rate

Toggles visible frame rate monitoring on or off.

##### Graphics

*(figure omise)*{width="3.0669160104986877in" height="1.54375in"}

###### Quality

The following graphics quality options are available:

-   Low - no realtime lighting, simple beam indicator, low-texture resolution, no anti-aliasing, no shadows

-   Medium - realtime lighting, low beam quality, medium-texture resolution, no anti-aliasing, no shadows

-   High - realtime lighting, medium beam quality, high-texture resolution, anti-aliasing, medium-resolution hard shadows

-   Ultra - realtime lighting, high beam quality, high-texture resolution, anti-aliasing, high-resolution soft shadows

On Eos Family consoles, Augment3d render quality is limited to Low or Medium. A tethered computer is required for High or Ultra.

> Also available via Toolbar > *Performance Indicator (on page 518)*.

###### Refresh Rate (FPS)

The maximum refresh rate attempted by Augment3d. By default, this is set to 30 frames per second. This can be adjusted higher or lower in a range from 5 - 60 FPS, but will be ultimately limited by the graphics processor on the device running Augment3d. Also available via Toolbar

-   *Performance Indicator (on page 518)*.

###### Resolution Limit

> **Note:** *This option is only available for Eos Apex consoles and ETCnomad on Windows and macOS.*

Sets the Augment3d resolution. The following options are available:

-   2160p - 4K

-   1440p - 2K

-   1080p - Full HD

-   720p - HD

-   480p

-   360p

-   240p

> Defaults to 1080p. Lower resolutions may result in improvements to Augment3d performance. Also available via Toolbar > *Performance Indicator (on page 518)*.

###### Lighting

Sets the lighting mode. The following lighting options are available:

-   Pass-Through - light passes through objects. Least resource-intensive.

-   Approximated (default) - light will pass through an object if all corners of the beam do not hit that object. Moderately resource-intensive.

-   Realistic - accurately-modeled light. Most resource-intensive.

> **Note:** *Console output will stay consistent regardless of Augment3d performance.*
>
> Also available via Toolbar > *Performance Indicator (on page 518)*.

###### Light

Sets the overall intensity of the simulated light. Also available via Toolbar > Light.

> **Note:** *This only affects the intensity of the simulated light beams in Augment3d, not the intensity values of the fixtures themselves.*

###### Haze

> Sets the overall haze level. Also available via Toolbar > *Light Tool (on page 517)*.

###### Smoke

Toggles animated haze smoke particles on or off.

###### Ambient Light

> Sets the color and level of ambient light. Also available via Toolbar > *Light Tool (on page 517)*.

###### Bloom*

Controls the amount that simulated light in the scene reflects on objects to make them glow. Also available via Toolbar > Light.

###### Bloom Diffusion*

> Adjusts the concentration of the bloom effect. Also available via Toolbar > *Light Tool (on page 517)*.

###### Saturation*

Sets the overall saturation of colors in the Augment3d model.

###### Contrast*

Sets the overall contrast of the Augment3d model.

> **Note:** *Settings marked with an asterisk (*) are only applied in High and Ultra quality settings.*

##### View

*(figure omise)*{width="3.11837489063867in" height="1.5952077865266843in"}

###### Camera Follow Mode

Toggles Camera Follow Mode between Off and Fixture POV, which switches the camera view to that of the first selected fixture. Also available in Toolbar > Camera.

###### Camera View

Toggles between Perspective and Orthographic view. Also available in Toolbar > Camera.

###### Animate Camera Presets

Toggles animation while moving between camera presets.

###### Animate Pan/Tilt Movement

Toggles animation of automated fixtures. Also available in Toolbar > Focus.

###### Fixture Labels

Toggles labels over the fixture body for all, automated, selected, and / or active fixtures. Also available in Toolbar > Labels.

###### Beam Center Labels

Toggles labels in the center of the simulated beam for all, automated, selected, and / or active fixtures. Also available in Toolbar > Labels.

###### Focus Handles

Toggles beam-end handles for all, automated, selected, and / or active fixtures, and text labels for each handle. Also available in Toolbar > Labels.

###### Stick Beams

Toggles Stick Beams for all, automated, selected, active, and / or inactive fixtures. Also available in Toolbar > Labels.

###### Light Beams

Toggles beams for all, automated, or selected fixtures. Also available in Toolbar > Light.

###### Cue Preview Mode

Toggles Cue Preview between Default (off) and Pending Cue. Pending Cue mode allows Augment3d to display a virtual preview of the look used in the next upcoming cue. Also available in Toolbar > Options.

##### Reset

*(figure omise)*{width="5.422811679790026in" height="0.7746872265966754in"}

###### Reset Settings to Default

Resets all settings in Preferences back to defaults.

###### Reset UI to Default

Resets the Augment3d window size and layout back to defaults.

#### Hierarchy

The Hierarchy lists the objects and fixtures currently in your Augment3d model. This includes all objects that have been manually added and all fixtures automatically added via Patch.

*(figure omise)*{width="1.6610695538057743in" height="1.5991655730533683in"}

The dropdown menu allows you to add query folders, as well as the option to create new objects and groups without using the Library.

The search bar allows you to search for objects by name or tag. This is useful for editing large, complicated models, which can have hundreds of objects and fixtures.

Right-clicking a hierarchy object allows you to change its color swatch.

> **Note:** *Color swatches are for identification only, and do not alter the color of the associated object.*

##### Groups

To create a new group, use the dropdown menu to add a new group folder. Items added to this folder from elsewhere in the hierarchy will be considered part of the same group, and can be moved, scaled, and rotated in unison. To remove an item from the group, remove it from the folder.

##### Query Folders

Query folders are smart folders that update their contents automatically. Once a query folder is created from the Hierarchy, the *Inspector (on page 513)* will display options for the folder.

*(figure omise)*{width="1.3326060804899387in" height="1.6941666666666666in"}

Available options are:

-   Include Types (Fixture, Group, Model, FPE Calibration Point, Label, Dynamic, Reference Point) - toggling any combination of these options will include all objects of that type in the folder.

    -   Dynamic objects (currently Pipes, Trusses, and Curtains) proportionally adjust to scaling.

-   Include Names - includes all objects of a specific name in the folder.

-   Include Tags - includes all objects with a specific tag in the folder.

###### Refining Query Folders

You can further refine the Names and Tags options using wildcards. An asterisk (*) will replace multiple characters, and a question mark (?) will replace single characters. For example, three Person 1 objects have been added to the model, named \"Alex,\" \"Chris,\" and \"Kim.\" A search for \"*i*\" will return Chris and Kim, (which both contain an \"i\"), while a search for \"?i?\" will only return Kim, the only three-character option containing an \"i.\"

##### Sorting and Reordering

Use the Sort button next to the dropdown button to organize the contents of the Hierarchy between A-Z, Z-A, and unsorted. In unsorted mode, Hierarchy objects can be freely dragged and reordered. This order is temporarily stored, but may not be maintained.

##### Triangle Count

*(figure omise)*{width="1.676438101487314in" height="1.203332239720035in"}

This button provides an overview of the objects using the most triangles, along with information about their impact on Augment3d. Reducing the number of triangles used in a model will improve processing performance.

##### Nesting Objects

Nesting objects within the Hierarchy associates multiple \"child\" objects with a \"parent,\" allowing you to create sets of objects that can be moved, shown, and hidden in unison. Nest objects to a Scenic Element or Scenic Element Movable Channel so that they can be moved, shown, and hidden during cue playback.

To nest objects, select the desired child objects in the Hierarchy by clicking while holding SHIFT (for consecutive objects) or CTRL (for individual objects). Once selected, simply drag them over the parent object in the Hierarchy and release when the parent is highlighted to nest them underneath. Select and drag child objects out from under their parent to separate them again.

> Position data for nested objects is relative to their parent, rather than the world position. For more information, see *Position, Rotation, & Scale (on page 514)*.

###### Expanding and Collapsing Objects

Complex objects added to the Hierarchy may be expanded into a series of nested objects by right-clicking on them and choosing \"Expand.\" Child objects may be selectively recombined by right-clicking a child object at any level and choosing \"Collapse.\"

#### Inspector

The Inspector window contains a variety of controls for modification of any selected objects.

*(figure omise)*{width="1.5798906386701663in" height="2.85in"}

##### Name

Sets the name for the object.

##### Materials

Allows you to edit the *Materials (on page 503)* assigned to the object. A preview of the applied material or a mosaic of multiple applied materials is shown to the right.

##### Lock

Locks objects to prevent them from being altered in the Inspector.

> **Note:** *Locked objects may still be moved, scaled, or rotated by selecting them in the Hierarchy.*

##### Visibility

Controls object visibility in the Augment3d scene.

##### Focus

Sets object focus behavior between the following options:

-   Always Focus - if this object is clicked on, it is used as the point for click-to-focus.

-   Never Focus - this object is ignored when using click-to-focus.

-   Selective Focus - object is used as the point for click-to-focus. If CTRL is held while clicking, the object is ignored.

##### Rotation

These icons rotate the selected object counterclockwise (CCW / left) or clockwise (CW / right) about the X, Y, and Z axes respectively.

##### Move to Ground Plane

Aligns the selected object with the ground plane of the Augment3d model.

##### Pivot

Allows you to determine the point around which the selected object rotates. Select one of the white dots to choose it as the new pivot point. The standalone dot on the left is the object\'s default pivot point, usually defined by the software the object was created in.

##### Position, Rotation, & Scale

Allows you to manually enter the position, rotation, and scale data for the selected object. Values can be adjusted by typing in the corresponding box, or by dragging left or right on the box labels.

Position refers to the physical location where the item is placed in the space in relation to the origin, if the item is not nested to any other object. If the item is nested to another object, the position data represents the physical location where the item is placed in relation to its parent\'s origin.

##### World

Information about the world position and size of the selected object. The world position is always the physical location where the item is placed in the Augment3d scene in relation to the origin of the model. Values can be adjusted by typing in the corresponding box, or by dragging left or right on the box labels.

##### Bounds

Information about the size of the selected object.

##### Tags

You can add tags to objects in this field. In large or complicated models, this makes them easier to search for via the Hierarchy.

### Augment3d Toolbar

The toolbar contains different options for altering Augment3d fixtures and objects.

> **Note:** *Certain tools are only available in Edit Mode. See Edit Mode Tools (on page 518).*

#### Camera Tool

Camera provides several options to change your view and position in Augment3d. Reset all options to default by clicking Restore Camera Mode Defaults.

> **Note:** *In a multi-console system, the Augment3d camera view is synced between devices assigned to the same user ID. All other Augment3d settings are set and adjusted per-device.*

*(figure omise)*{width="1.9030249343832022in" height="1.6149989063867016in"}

##### Home

Returns you to the default camera position. This can be updated to the current position by holding down the Home bookmark, or reset by clicking Restore View Defaults.

##### Bookmarks

You can record up to five custom camera positions as bookmarks. Like Home, these can be updated by holding, or reset by clicking Restore View Defaults. Updated bookmarks can be stored and recalled using Eos Snapshots that include the Augment3d tab or tether (see *About Snapshots (on page 462)*).

##### Look

The Look buttons provide shortcuts to different camera positions, oriented around the current camera position.

##### Zoom

Zooms the camera view to whatever fixtures or objects are currently selected in Augment3d.

##### Fixture POV

Positions the camera from the point of view (POV) of the gate of the first selected fixture. Exiting POV mode returns the camera to its previous position. When enabled, a Fixture POV symbol will overlay the Camera icon. Also available in Preferences.

##### Mode

Toggles between Perspective and Orthographic camera modes. In Perspective mode, objects that are further away are smaller than nearby objects. In Orthographic mode, all objects are the same scale. Also available in Preferences.

##### Move

Toggles between Fly and Orbit camera modes. In Fly mode (indicated by a Fly symbol overlaying the Camera icon), the mouse alters the angle of the camera. In Orbit mode (indicated by an Orbit symbol overlaying the Camera icon), the mouse moves the camera around a center point. Movement is still possible via keyboard controls in either mode. Hold ALT to temporarily reverse the behavior.

#### Focus Tool

*(figure omise)*{width="0.8013615485564305in" height="0.9384372265966754in"}

Provides options to edit the Focus Offset height and toggle automated fixture animation on or off. LEFT MOUSE + CENTER WHEEL will also adjust the height. Also available in Preferences.

#### Labels Tool

Labels provides options to toggle various informational overlays on or off. Reset all options to default by clicking Restore Label Defaults. All label options are also available in Preferences.

*(figure omise)*{width="1.6748436132983378in" height="1.571457786526684in"}

##### Fixture Labels

Toggles labels overlaying fixture bodies for all, automated, selected, and / or active fixtures.

##### Beam Center Labels

Toggles labels overlaying fixture beams for all, automated, selected, and / or active fixtures.

##### Focus Handles

Toggles focus handles for all, automated, selected, and / or active fixtures. Spherical handles may be moved to proportionally refocus automated fixtures. Cubic handles indicate a conventional fixture, but cannot be used to refocus. Labels overlaying focus handles can also be toggled.

#### Sticks Tool

Stick beams can be toggled to see where a fixture is pointed (even if it is not currently outputting), or for differentiating between multiple fixtures focused on the same location.

*(figure omise)*{width="1.584915791776028in" height="0.6175in"}

Toggle stick beams for all, moving, selected, active, or inactive fixtures. Reset all options to default by clicking Restore Stick Defaults. Also available in Preferences.

#### Light Tool

Provides options to configure the simulated light in an Augment3d model. Reset all options to default by clicking Restore Beam Defaults. All light options are also available in *Graphics*.

*(figure omise)*{width="1.601091426071741in" height="1.5081244531933509in"}

##### Beams

Toggles simulated light beams for all, moving, or selected fixtures.

##### Light

Intensity adjusts the overall intensity of the simulated light. This option does not alter the actual intensity values of fixtures themselves.

Glow and Diffusion control the degree to which objects in the scene glow. These options only apply in High and Ultra quality.

##### Beam Intensity

Toggles between low, medium, and high intensity simulated beams. Toggle Haze on to increase the realism of the beams.

##### Ambient Light

Toggles between no, low, medium, and high overall ambient light levels in the Augment3d model.

#### Options Tool

##### Pending Cue Mode

This mode allows Augment3d to display a virtual preview of the look used in the next upcoming cue.

> *(figure omise)*{width="1.0323053368328958in" height="1.1903116797900262in"}

Reset Cue Preview by clicking Cue Preview Mode Defaults. An eye will appear on the Options icon when in Cue Preview mode. Also available in Preferences.

##### Quality

*(figure omise)*{width="1.9949573490813648in" height="1.9435411198600174in"}

Allows you to adjust the quality of the Augment3d render, the Refresh Rate, and the Lighting mode. Eos Apex consoles and ETCnomad on Windows and macOS allow you to set a resolution limit to improve performance. Also available in Preferences. See *Graphics (on page 507)*.

**Note:** *Augment3d render quality on consoles is limited to Low or Medium.*

#### Performance Indicator

This color-coded dot on the toolbar indicates Augment3d\'s current quality and performance level.

-   High - 25 FPS and higher

-   Medium - 20 to 24 FPS

-   Low - 15 to 19 FPS

-   Very Low - 10 to 14 FPS

-   Poor - 10 FPS and lower

Selecting the dot provides quick access to the quality, rendering, and lighting settings from the *Graphics (on page 507)* preferences menu.

#### Edit Mode Tools

The following tools are only available when in Edit Mode.

##### Grid Tool

*(figure omise)*{width="0.16656167979002626in" height="0.16656167979002626in"}

Toggles the grid on or off. Also available in Preferences.

##### Snap Tool

*(figure omise)*{width="0.15615157480314962in" height="0.16656167979002626in"}

Toggles object snapping to the grid on or off. Also available in Preferences.

##### Move Tool

*(figure omise)*{width="0.15615157480314962in" height="0.16656167979002626in"}

Allows you to move objects along the X/Y/Z axes. Handles have conical ends.

##### Scale Tool

*(figure omise)*{width="0.1769717847769029in" height="0.16656167979002626in"}

Allows you to resize objects along the X/Y/Z axes. Handles have cubic ends. Use the center handle to resize all dimensions proportionally.

##### Rotate Tool

*(figure omise)*{width="0.14574146981627298in" height="0.16656167979002626in"}

Allows you to rotate objects around the X/Y/Z axes.

##### Local Tool

*(figure omise)*{width="0.16656167979002626in" height="0.16656167979002626in"}

Toggles Move and Rotate object tools between global XYZ orientation and object

XYZ orientation. Scale is always performed relative to the object\'s Local XYZ orientation.

*(figure omise)*{width="3.413325678040245in" height="1.2431244531933507in"}

On the left barrel, Local is toggled off, so the Move tool orients itself based on the Augment3d model. On the right, Local is toggled on, so the Move tool orients itself relative to the position of the barrel.

### Fixtures in Augment3d

Fixtures must be patched in Eos and then added to an Augment3d model before they can be displayed and controlled. If you already know the position and orientation of your fixtures, you can manually add them to Augment3d through the Eos Patch screen on a channel-by-channel basis.

In Patch, certain fixtures will appear with the Augment3d \"3d\" logo next to them. This symbol indicates profiles with an Augment3d model. Fixtures without the \"3d\" logo will use a default fixture model based on the closest fixture type. To change the model used by the fixture type, see *Physical Data Editor (on page 208)*.

> **Note:** *Fixtures requiring a profile update will display with an asterisk (*). For more information, see Update Profile (on page 193).*
>
> **Note:** *Moving Mirror fixtures are not currently supported.*

#### Position and Orientation Data

##### Position

> Position data is either local or world. For more information, see *Inspector (on page 513)*.

*(figure omise)*{width="4.569055118110236in" height="1.4368744531933508in"}

In the above example, the fixture patched to Channel 184 is -2 meters offset on the X axis, -13 meters offset on the Y axis, and 7.5 meters offset on the Z axis.

##### Orientation

Orientation data reflects how the fixture is rotated. The values for X, Y, and Z represent a rotation in degrees around that axis in relation to the global XYZ axes.

*(figure omise)*{width="3.3219903762029745in" height="2.28in"}

The above left example shows the default orientation of 0/0/0, or pointing straight down. The center shows a rotation of 180° about the X axis, pointing the fixture straight up. The final example shows a rotation of 90° about the Y axis, pointing the fixture to the side.

#### Adding Fixtures Manually

*(figure omise)*{width="4.261209536307962in" height="1.2825in"}

Under the Augment3d section in Patch, fixtures have fields for XYZ Position and Orientation. If the fixture is nested, this data is relative to the parent. World Position and Orientation are absolute, relative to the scene overall. If nested, an arrow indicator will apear next to the position and orientation fields. For more information about nesting, see *Nesting Objects*.

You can also edit the following additional properties:

-   Beam Angle - set the beam angle from 1-179 degrees

    -   0 will reset back to the default (36 degrees) and clear the field

-   Shutters - see *Shutter Graphic (on page 252)*

-   Gobo Rotate - set the gobo rotation

-   Beam Edge - set the beam edge from 0-100 (empty/default is 50)

-   FPE Set - see *FPE Sets (on page 527)*

-   Hide Beam - when enabled, the fixture\'s beam will not appear in Augment3d

##### Entering Fixture Position & Orientation Data

Select the channel of a fixture for which you have position and orientation data, and navigate to the Position & Orientation section of the Augment3d tab in Patch. Selecting one of the position or orientation fields opens a keypad to input specific values.

Alternatively, keyboard syntax can be used. Use [/] to separate X, Y, and Z when typing in multiple values, and [Thru] to enter information for multiple fixtures at once.

-   [Chan] [1] [Select] [5] [/] [5] [/] [5] [Enter] sets the position of Channel 1 to 5,5,5.

-   [Chan] [1] [Select] [/] [2] [/] [Enter] sets the Y coordinate of Channel 1 to 2. No changes are made to the X and Z coordinates.

-   [Chan] [1] [Select] [+] [3] [/] [/] [Enter] adds 3 to the current X coordinate of Channel 1. No changes are made to the Y and Z coordinates.

-   [Chan] [1] [Select] [+] [/] [1] [/] [-] [5] [Enter] adds 1 to the current Y coordinate of Channel 1, and subtracts 5 from the Z coordinate. No change is made to the

> X coordinate.

-   [Chan] [1] [Thru] [5] [Select] [0] [/] [0] [/] [5] [Thru] [10] [/] [10] [/] [5] [Enter] sets the position of Channel 1 to 0,0,5 and the position of Channel 5 to 10,10,5. The positions of Channels 2, 3, and 4 are evenly distributed between the two.

-   [Group] [10] [Select] [5] [/] [/] [Thru] [10] [/] [/] [Enter] distributes the X coordinate of all channels in Group 10 between 5 and 10. No changes are made to the Y and Z coordinates.

All trailing slashes are optional. [Chan] [1] [Thru] [10] Position [5] [Thru] auto-completes to [Chan] [1] [Thru] [10] Position [5] [/] [*] [/] [*] [Thru].

The corresponding fixture is automatically added to the Augment3d model. Repeat the process for any additional channels or fixtures, or edit fixture position and rotation using tools available in the toolbar or the Inspector.

Position [@] [Enter] will remove the pose (position and orientation) of the selection. Orientation [@] [Enter] will reset the orientation of the selection to (0,0,0).

##### Shutters

> If you have a fixture with shutters, they must be configured in the *Fixture Editor (on page 193)*

to display accurately in Augment3d.

1.  First ensure that the fixture is hung base up and that pan and tilt are moving the fixture in the correct directions. If not, correct these before continuing.

2.  Adjust tilt to +90° or until the fixture is pointing at a wall.

3.  Set the frame assembly angle near the mid-range so that the shutters form a square.

*(figure omise)*{width="5.85081583552056in" height="2.2422911198600173in"}

Standard shutter controls are now normalized relative to the square so that A controls the top edge, with controls B, C, and D continuing clockwise in that order.

Pushrod-style shutter parameters are normalized so that frame a1 corresponds to the counterclockwise side of the top edge and b1 to the clockwise side, with frames a2, b2, a3, b3, a4, and b4 continuing clockwise in that order.

##### Moving Mirrors

If your fixture has a moving mirror accessory, it must be patched to a two-part channel, with P1 patched to an address as a dimmer and P2 as a moving mirror accessory.

*(figure omise)*{width="5.867490157480315in" height="1.0040616797900261in"}

Position and orientation data for the fixture can only be added and edited in P1. Attempting to add position and orientation data to the entire channel will return a syntax error. The moving mirror can be controlled via the pan and tilt parameters for P2.

Regardless of the fixture and mirror type, the model will display in Augment3d as a Source Four with a generic mirror.

#### Editing Fixture Position and Rotation

> Fixture position and rotation can also be edited in *Augment3d Edit Mode (on page 501)* using tools available in the toolbar or in the Inspector.

Any changes made to fixture position in Augment3d will automatically update the values in Patch. Similarly, any change made via Patch will automatically update the fixtures in Augment3d.

#### Setting Orientation for Conventional Fixtures in Patch

The Orientation property for conventional (non-automated) fixtures is used to aim static lighting fixture at the correct point.

1.  Navigate to Patch.

2.  Select conventional fixtures via the command line, or by selecting them in Augment3d. The fixtures will light up to indicate their selection.

**Note:** *You do not need to enter Augment3d Edit Mode to select fixtures.*

3.  Aim the fixtures at their intended target using a long selection, or SHIFT + left mouse.

#### Importing Augment3d Fixtures

> Fixtures can also be manually added by importing them into Augment3d object library *Using the Browser (on page 83)* via File > Import > MVR / Capture Model. This option supports both MVR and GITF file formats. See *Supported 3D File Formats (on page 543)*.
>
> **Note:** *MVR files can also include 3D model data. If Augment3d is running, the Merge Augment3d Scenery (#) option described below can optionally merge this data into Augment3d. If Augment3d isn\'t running, or running on a tethered device, a notification will prompt you to open Tab 38 to merge scenery.*

##### Import Options and Mapping

When importing, you will likely need to adjust the data before proceeding.

*(figure omise)*{width="5.080823490813648in" height="1.1439577865266841in"}

###### Options

The following options are available:

-   Merge Augment3d Scenery (#) - when enabled, any 3D scenery in the source file will be merged into Augment3d. Disabled by default. The number in parentheses indicates the total amount of 3D objects in the file.

-   Starting / Ending Channel - defines a specific range of channels to be imported.

-   Overwrite - overwrites the data in the show file when enabled, and merges the data when disabled. Disabled by default.

-   Update fixture types - enables or disables the update of fixture types in the show file. Enabled by default.

-   Only import Augment3d XYZ location - enables import of just Augment3d location data. Disabled by default.

-   Only Import Text/Notes/Labels/Gels - enables import of just the patch database text. Disabled by default.

###### Mapping Fields

You can map Eos patch fields to fields in the source file being imported. Channel and Address are required; any other field can be ignored if desired. Options can be selected again for placement in multiple fields.

####### Address Formats

Eos will accept multiple address formats for importing. Examples of those formats are 2/3, 2.3, 2,3, 2-3. Eos will convert all formats to n/n.

###### {Map Devices}

You can also map Eos fixture library devices to devices in the source file.

*(figure omise)*{width="5.13340113735783in" height="1.3220833333333333in"}

1.  Select {Map Devices} to open the mapping utility.

2.  Select a device from the Source File column and choose its matching Eos fixture profile. Multiple devices can be selected at a time.

*(figure omise)*{width="4.7091447944007in" height="1.1281244531933508in"}

3.  Select {Link Devices}.

*(figure omise)*{width="4.7091447944007in" height="1.1281244531933508in"}

4.  Repeat steps 2 and 3 until all devices have been associated with fixture profiles. To unlink a device, select it in the Mapping column and select {Unlink Device}.

5.  When complete, select {Done}, then {OK}. Your devices and their associated position information will now appear in Patch and Augment3d.

*(figure omise)*{width="3.9828740157480316in" height="1.2349989063867017in"}

Device mapping and import fields are saved with the show file.

##### Vectorworks Import Support

Eos 3.2.0 and newer utilize Vectorworks\' MVR export to move model and fixture data, and require Vectorworks 2023 Service Pack 3 or later. Older versions of Eos use generic 3D exports from Vectorworks for models, and an ETC-made plug-in for fixture data.

> For legacy installation instructions, see Appendix > *Vectorworks Augment3d Plug-in (on page 702)*.

#### Fixture Position Estimation (FPE)

If you don\'t know the position and orientation of your fixtures, Eos can automatically configure the location and orientation of automated fixtures in Augment3d using a process called Fixture Position Estimation (FPE). FPE associates four or more points in your space with corresponding Focus Palettes in order to estimate the location and rotation of your automated fixtures.

If you are setting up your fixtures for the first time, it is generally easier to choose FPE points first and then record Focus Palettes for each one. However, if you have existing Focus Palettes it may be possible to use those focus locations for your FPE points instead.

##### FPE Points

Each point is a known physical location in a space, measured in relation to the *XYZ & Origin (on page 502)*. It is recommended to choose at least four points on the floor encompassing the origin and as much of your space as possible.

For best results, the four points should be on the same plane (have the same Z coordinate). If differing Z coordinates must be used, list the points in a clockwise direction from the point of view of the fixtures. While four points is the minimum requirement, additional points may increase FPE accuracy.

1.  Determine the X and Y coordinates of these points by measuring outwards from the origin point.

*(figure omise)*{width="3.7538779527559054in" height="1.151874453193351in"}

Once you have your points chosen and measured, enter the coordinates for each point.

2.  Navigate to the Eos Patch screen. Click the Augment3d tab and select the FPE section.

3.  Enter the measured coordinates of each point. Augment3d will automatically place an FPE Point at each location.

Updating XYZ coordinates in Patch will alter the FPE Point\'s location in the Augment3d model.

> An error will appear if the points chosen are suboptimal. For help, see *Troubleshooting FPE (on page 528)*.

##### Focus Palettes

Once you have chosen, measured, and entered the coordinates of your points, associate each point with a Focus Palette.

1.  Focus your fixtures at one of your FPE points and record a Focus Palette.

> **Note:** *Fixture beams must be centered on the FPE point. Focusing fixtures one at a time, sharpening the beam edge, and narrowing the iris to create a smaller-sized beam may help you center the beam. Using a gobo with an easily-identifiable center point (such as a crosshair) may also help.*

2.  In Patch, enter the Focus Palette number into the \"FP#\" column that corresponds with the point on which you focused.

3.  Repeat this process until all your FPE points have associated Focus Palettes.

This association between FPE Points and Focus Palettes is crucial to the accurate rendering of fixtures in Augment3d.

##### FPE Sets

If multiple sets of FPE calibration data are needed, FPE Points can be arranged in up to ten sets. Each set has its own FPE Points, allowing you to maintain FPE data for multiple spaces within the same Eos showfile. Each FPE set can then be assigned to a channel or range of channels.

The fixtures patched to those channels will then use the FPE Points in that set for their calibration and focusing.

Multiple FPE sets can be useful for consoles that control more than one space, or for touring shows working in multiple venues. This can also be useful if all the fixtures in your space cannot focus on the same set of FPE points.

##### Calculating FPE

Once you have at least four FPE Points matched to Focus Palettes, you are ready to calculate FPE.

*(figure omise)*{width="1.8203729221347331in" height="1.151874453193351in"}

Press Realculate FPE , then Confirm FPE to commit your changes.

*(figure omise)*{width="4.37346675415573in" height="1.413124453193351in"}

A window will appear summarizing any FPE changes and / or a table of errors.

> **Note:** *Any errors must be resolved before proceeding. It is not possible to undo an FPE calculation.*

Press Accept FPE Changes to proceed.

If calculating FPE for the first time, this will automatically generate fixtures in your Augment3d model. You can also make subsequent FPE edits or recalculations the same way.

###### Selective FPE

With nothing selected in the command line, FPE will recalculate positions for all patched fixtures in a show file. If specific fixtures or ranges of fixtures are selected, the FPE calculation will only affect the selection.

##### Troubleshooting FPE

###### Accuracy

There are several ways to calculate the positions and rotations of the fixtures in your show. There are several factors that can also impact the accuracy of this estimation, including:

-   Fixture profile inaccuracy

-   Poor FPE point selection

-   FPE point measurement error

-   Slack in automated fixture belts

-   Asymmetry about the tilt axis

-   Fixture-to-fixture pan / tilt variations

FPE accuracy is dependent on profile information and user-supplied data. If the data is inaccurate, the computation will either fail or give poor results. Adequate care should be taken to ensure that profiles do not have errors and that the positions of FPE points are accurately measured.

###### Best Practices

*(figure omise)*{width="4.488533464566929in" height="3.9622911198600175in"}

There are many ways to select FPE Point positions. The preferred method is to use at least 4 points close to the bounds of your space, as in the example above. Larger angles between points reduces the possibility of redundant information being used in the calculation. It may help to think of the points as outlining the base of a 3D shape that should cover as much of your space as possible.

> *(figure omise)*{width="3.974932195975503in" height="2.2404155730533684in"}

One example of a poor configuration is shown above, with all FPE points in a line. The two center points are redundant, as they are part of the line from the two end points. Additionally, there is no coverage of the stage space possible with all points arranged in a line.

*(figure omise)*{width="4.481347331583552in" height="3.96625in"}

A better (but still problematic) configuration is pictured above. Since one of the points is in a line between two others, the data from that point is redundant and cannot be used to calculate the fixtures\' positions.

###### Troubleshooting

If fixture response is inaccurate or if fixtures are not generated correctly in Augment3d, check the following:

-   Ensure your fixture profiles are up to date, and update if not (see *Update Profile (on page 193)*).

    -   This is likely to fix the problem if fixtures of one type respond accurately and fixtures of another type do not.

-   Ensure the measured ground points in your space match how they were entered in Eos, and that the X and Y coordinates were not accidentally swapped.

-   Verify you are using the correct units of measurement.

-   Replay your Focus Palettes.

    -   Did they record correctly?

    -   Were they assigned to the correct Reference Point?

    -   Do any of the fixtures pan more than 180 degrees? If so, press {Flip} and re-record (or update) the Focus Palette

*(figure omise)*{width="3.2889916885389328in" height="0.9618744531933509in"}

-   Add an additional FPE Reference Point and Focus Palette. Recalculate FPE. Is fixture response more accurate?

###### Other Common Issues

The following are some of the issues that most often affect the FPE calculation.

####### Beam Centering

The calculations expect the optical center of the beam to be at the measured ground points. If this is hard to see with the naked eye, using a crosshair gobo (or any gobo with an easily identifiable center point) can aid in lining up the beam more accurately over the ground point.

####### Fixture Profiles

Some automated fixtures may have pan and / or tilt settings that are incorrectly calibrated in their profile. These profiles must be corrected in order to accurately work with FPE. For more information, see *Fixture Profile Correction (below)*

####### User-Definable Pan / Tilt

Some fixtures have user-definable pan / tilt ranges that may cause inaccuracies. Check the settings of your fixture and ensure any parameter ranges set on the fixture match the ranges set in the fixture profile.

####### Fixtures

Some automated fixtures may be subject to mechanical defects that cause them to behave inaccurately when compared to their profile or other fixtures of the same model. Unless a custom profile is created that matches the specifications of that fixture, it will not work correctly with FPE.

##### Fixture Profile Correction

If FPE has been checked and run correctly, continuing issues may be due to inaccuracies in a fixture profile or the physical fixture itself.

> Before continuing, please ensure that your fixture profile library is updated to the current version (see *Update Profile (on page 193)*).
>
> **Note:** *If you correct inaccuracies in a fixture profile, please report the necessary updates via the ETC Augment3d forums at community.etcconnect.com. When possible, please include a copy of the fixture manual .*

###### Pan / Tilt Inversion

If a fixture in Augment3d pans and / or tilts in the opposite direction as it does in the real world, either parameter may be inverted.

> **Note:** *Many fixtures have a setting to invert and/or swap pan and/or tilt within the fixture firmware. Ensure that these are not enabled before testing for inversion as described below.*

####### Testing for pan / tilt inversion

1.  Set the fixture's pan to 0° and tilt to +90°. Increment the pan in either direction. Does the virtual fixture rotate in the same direction as the physical fixture?

2.  Set the fixture\'s pan and tilt to 0°. Increment the tilt in either direction. Does the virtual fixture point in the same direction as the physical fixture?

####### Correcting pan / tilt inversion

If you find that the pan or tilt value did not move in the correct direction, use the range editing tools in the *Fixture Editor (on page 193)* to invert the DMX range, or swap the DMX and User Min/Max at the same time.

###### Pan Range

If the pan direction is correct, but the virtual fixture pans further in either direction than the real fixture, the fixture\'s physical pan range or values may not match its profile.

####### Testing pan range

1.  Aim your fixture at a point on your stage. Press the "Flip" button. Does the fixture return to the same point? If so, pan is mapped correctly. If not, set the fixture\'s tilt to +90°,or until the fixture is pointing forwards.

*(figure omise)*{width="3.2889916885389328in" height="0.9618744531933509in"}

2.  Test with pan values of -90°, 0°, and +90°. The fixture should point to the left, straight forwards, and to the right, respectively. If so, pan is mapped correctly. If not, follow the steps below to correct the pan range in the Fixture Profile Editor.

####### Correcting pan range

1.  First, find the correct DMX home value for pan.

    a.  Set pan to 0° and tilt to +90°.

    b.  Increase or decrease pan, using the smallest value possible, until the optics are pointed away from the UI of the fixture.

    c.  *Using About (on page 443)*, find the raw DMX values for pan (including course and fine), and note them.

*(figure omise)*{width="3.114663167104112in" height="1.1241666666666668in"}

d.  Set this new raw DMX level as your pan DMX home value in the *Fixture Editor (on page 193)*.

```{=html}
<!-- -->
```
2.  Then, using the new DMX home value, calculate the maximum.

    a.  Set your pan value to the minimum DMX value (likely 0) and select a tilt value that targets a point in your venue.

    b.  Increase your pan value 360° until the fixture is pointing at the same point again and note this DMX value as your found pan value.

    c.  Note the minimum allowed DMX value for pan (likely 0) and the maximum allowed DMX value for pan (likely 255 or 65535).

    d.  Calculate the User Min and Max Degree values:

        -   min pan value = (360 ÷ (found pan - minimum pan)) * (minimum pan - pan DMX home value)

        -   max pan value = (360 ÷ (found pan - minimum pan)) * (maximum pan - pan DMX home value)

3.  Set the output of this calculation as your new user minimum and maximum.

4.  Recalculate FPE (see *Calculating FPE (on page 527)*) and test for accuracy.

###### Tilt Range

If the tilt direction is correct, but the virtual fixture tilts further in either direction than the real fixture, the fixture\'s physical tilt range or values may not match its profile.

####### Testing tilt range

1.  Aim your fixture at a point on your stage. Press the "Flip" button. Does the fixture return to the same point? If so, tilt is mapped correctly. If not, set the fixture\'s pan and tilt to 0°.

2.  Pan the fixture in a circle. Does the fixture beam remain stationary, pointed straight down? If so, tilt is mapped correctly. If not, follow the steps below to correct the tilt range in the Fixture Profile Editor.

####### Correcting tilt range

First, find the correct DMX home value for tilt.

1.  Set your tilt to 0°. Pan clockwise 360°, then counterclockwise 360°, and repeat.

2.  Slowly increase or decrease your tilt value until the fixture spins with no wobble in the beam during the sweep.

3.  Set the raw DMX value as your tilt DMX home value in the *Fixture Editor (on page 193)*. Then, using the new DMX home value, calculate the maximum.

```{=html}
<!-- -->
```
1.  Set your tilt to your new DMX home value.

2.  Begin increasing tilt until the fixture head is approximately perpendicular to its base and record this DMX value as your found tilt value.

3.  Not ethe minimum allowed DMX value (likely 0) and the maximum allowed DMX value (likely 255 or 65535) for tilt.

4.  Calculate the user min and max degree values:

    a.  min tilt value = (90 ÷ (found tilt - tilt DMX home value)) * (minimum tilt - tilt DMX home value)

    b.  max tilt value = (90 ÷ (found tilt - tilt DMX home value)) * (maximum tilt - tilt DMX home value)

5.  Set the output of this calculation as your new user minimum and maximum.

6.  Recalculate FPE (see *Calculating FPE (on page 527)*) and test for accuracy.

###### Fixture Defects

If none of the troubleshooting or profile correction steps help, there may be an issue with the fixture itself.

Certain mechanical defects may cause an automated fixture to behave inaccurately when compared to their profile or other fixtures of the same model. Unless a custom profile is created that matches the specifications of the fixture, it will not work correctly with FPE.

> For more information, see *Creating a New Fixture (on page 194)*.

#### Working with Fixtures

Once fixtures are added to your model, you can begin using Augment3d to focus and control them. There are a variety of tools available to help with this.

##### Fixture Selection & Focus

###### Selecting Fixtures

To select fixtures in Augment3d, either select them via the Eos command line or use a mouse. Click on a fixture to select it. You can also drag, or hold shift to select multiple fixtures.

There are three colors used for selection:

-   Gold - fixtures selected in Eos

-   Blue - fixtures selected in Augment3d Edit Mode

-   Pink - fixtures selected in both Eos and Augment3d

###### Focusing with Click-To-Focus

Selecting and holding on an object or plane in your Augment3d model will focus the selected fixture on that spot. Pressing SHIFT + LEFT MOUSE will also activate Click-To-Focus. You can also drag around the model to move the fixtures. Fixtures without pan / tilt parameters must be selected while in Patch for Click-to-Focus to work.

##### Other Useful Tools

###### Labels Tool

*(figure omise)*{width="5.825024059492564in" height="1.8793744531933507in"}

Fixture Labels display the channel number of the fixture. This can be useful in identifying which fixture is creating a particular beam of light.

*(figure omise)*{width="5.694514435695538in" height="1.8880205599300088in"}

Focus Handles create a controllable point at the end of the beam of an automated fixture, which can be dragged to focus a single fixture, or multiple fixtures together while maintaining their spatial relationships.

> For more information, see *Labels Tool (on page 516)*.

###### Sticks Tool

*(figure omise)*{width="5.794662073490814in" height="2.0658333333333334in"}

Stick Beams draws a line from the fixture to wherever the beam lands. Stick Beams do not require intensity and can be used to focus a fixture that is not currently outputting.

> For more information, see *Sticks Tool (on page 517)*.

###### Focus Tool

Use the Focus Height feature to set a vertical offset from the location that is being focused on, in order to adjust focus to an actor\'s chest or face, instead of on the floor where they are standing.

> For more information, see *Focus Tool (on page 516)*.

### Augment3d Objects

Objects are any non-fixture element of your Augment3d model.

#### Adding Objects

There are two ways to add an object to the Augment3d model.

##### From the Library

> Objects can be dragged from the *Library (on page 502)* and placed into the model.
>
> **Note:** *Objects are created with a (0,0,0) position on the XYZ axes when added to the model.*

##### From the Hierarchy

To add objects from within the Hierarchy, right-click, select Create, and choose the object you wish to add.

#### Copying Objects

Objects can be copied and pasted by selecting the object in the *Hierarchy (on page 511)* and using CTRL + C to copy. Use CTRL + V to paste the object. You can also duplicate selected objects using CTRL + D. If working in macOS, use CMD instead of CTRL.

#### Modifying Augment3d Objects

The Position, Scale, and Rotation of any object in an Augment3d model can be modified using one of the associated tools in the toolbar. See *Edit Mode Tools (on page 518)*

Selecting one of the modification tools from the toolbar puts the selected object or objects into the corresponding modification mode (Move, Scale, and Rotation, as seen left-to-right below).

*(figure omise)*{width="3.6139359142607175in" height="1.832707786526684in"}

> These parameters can also be modified using the quick buttons in the Inspector. See *Rotation (on page 513)*.

##### Position

Select the Move tool. Drag on any of the X/Y/Z axes to move the object in that direction. Objects that have been moved away from their 0,0,0 default position will display a trail and distance measurement back to the Origin.

##### Scale

Select the Scale tool. Drag on any of the X/Y/Z axes to enlarge the object in that direction. Drag on the white center box to scale all dimensions proportionally.

##### Rotation

Select the Rotate tool. Drag on any of the X/Y/Z axes to rotate the object in that direction. The point around which the rotation occurs can be defined in the Inspector. See *Pivot (on*

> *page 514)*.

#### Scenic Elements

You may wish to change the visibility and position of Augment3d objects using cues, submasters, and so on. Two new profiles are available in Patch in order to accomplish this, under {Type} > {Manufctr} > {ETC Fixtures} > {Scenic Element}.

> **Note:** *Objects patched as scenic elements are exempt from grandmaster and [Select Active] control.*

##### Scenic Element

An object nested under a channel patched as a scenic element can be shown or hidden on a cue-by-cue basis by giving the channel an intensity value. Any intensity value above 0% will show the nested object.

Imagine an object that is onstage in Act I but is removed for Act II. Instead of removing the object from Augment3d, you could simply hide it by giving its scenic element channel a 0 intensity value in the Act II cues.

##### Scenic Element Movable (SEM)

An object nested under a channel patched as a scenic element can be shown or hidden as above, but can also have their position, orientation, and rotation changed from cue-to-cue.

Imagine an object that remains onstage for the duration of the show, but changes position between Acts I and II. Instead of creating a separate object for each act, you can use the same object and simply change the position and orientation of its SEM channel in the Act II cues.

###### Editing SEMs

> Once a channel has been patched as an SEM, its position and orientation can be set either by entering values in *Patch > Augment3d (on page 186)*, or by using any of the applicable tools in *Augment3d Edit Mode*.

This position and orientation data sets the origin point of the SEM. When an SEM is moved in Live, Blind, or Staging Mode, the new position will display in Augment3d linked to the origin. Any changes made to this new position in Augment3d are temporary and will revert back to the Live, Blind, or Staging Mode value on exiting Edit Mode.

#### Augment3d Zones

Zones are volumes (areas of your space) that can be defined in Augment3d which will affect any fixture whose beam interacts with them. The fixture behavior is configurable and will use override data, which will temporarily take control over any recorded or manual data.

> *(figure omise)*{width="5.858543307086614in" height="3.3in"}

Zones appear in the *Library (on page 502)* as a distinct object type that can be added to your Augment3d model.

##### Configuring Zones

> Once added to your model, zones can be configured in the *Inspector (on page 513)*

*(figure omise)*{width="2.84375in" height="3.0833333333333335in"}

Fields are available to set the name, color, and unique ID number of the zone, along with the following options:

-   Fixture Type - specify what type of fixture will be affected by the zone, in conjunction with any group filters.

    -   Movers Only - only moveable fixtures with pan/tilt parameters.

    -   All Fixtures - all fixture types, including single-parameter conventionals.

-   Group Filter - optionally specify a group of fixtures that will be affected by the zone, in conjunction with the selected fixture type.

-   Fixture Status - specifes which fixtures will be affected based on their current active status.

    -   All - all active and inactive fixtures.

    -   Active Only - only fixtures with an intensity greater than zero.

    -   Inactive Only - only fixtures with an intensity of zero.

-   Beam Type - choose which part of the fixture beam will intersect with the zone.

    -   Cone - the outermost edge of the beam.

    -   Stick - the center of the beam.

> **Note:** *When beam type is set to cone, zone intersection is derived from the fixture\'s standard beam angle, including zoom parameters. Beam alterations from shutters, irises, and other parameters are not currently detected.*

-   Behavior - sets the override action that happens when fixture beams enter or exit the zone boundary, using the fade out and fade in time specified.

    -   Keep Dark - overrides fixture intensity to 0.

    -   Make Bright - overrides fixture intensity to 100.

    -   Make Palette - applies a specified intensity, focus, color, or beam palette.

    -   Make Preset - applies a specified preset.

    -   Trigger - plays up to two macros.

Depending on the chosen behavior, additional configuration options may be available:

-   Fade Out (sec) - sets the fade out time of the intensity, palette, or preset change.

-   Fade In (sec) - sets the fade in time of the intensity, palette, or preset change.

-   Target - specifies which palette or preset to apply.

-   Entry Macro - specifies which macro to play when fixture beams enter the zone boundary.

-   Exit Macro - which macro plays when fixture beams exit the zone boundary.

Zone-based fixture instructions override any recorded or manual data. When one or more fixture beams enters the zone boundary, the override is applied, and the fixtures will follow the zone configuration. This is indicated in Live with pink text indicating the zone source (see *Color Indicators (on page 103)*).

*(figure omise)*{width="3.3020833333333335in" height="1.6770833333333333in"}

Once a fixture exits the zone, the override is released and background data is restored.

If an inactive fixture intersecting a zone is then made active, nothing will happen. Configured behavior only occurs when an active cone or stick beam moves into a zone or a zone moves into an active cone or stick beam.

##### Zones with Scenic Elements

Like other Augment3d objects, zones can be nested under *Scenic Elements (on page 537)*. Under a standard scenic element, this would allow you to show or hide zones from your Augment3d model. When hidden, the zone programming will not apply to any fixtures, allowing you to enable or disable fixture behavior on the fly by simply showing or hiding the zone.

Nesting a zone under a Scenic Element Moveable (SEM) allows you to give the zone movement and rotation instructions in addition to showing or hiding it. This opens up a variety of programming choices, as zones can now be moved into or out of beam trajectories to make the fixtures dynamically react. This may be especially useful in systems of conventional, non-moving fixtures.

#### Importing Augment3d Objects

> Custom 3D objects can be imported into Augment3d *Using the Browser (on page 83)* via File

-   Import > Augment3d Scenic Models, or from Augment3d Edit Mode via File > Import to Library > Import 3D Model. If a tether and a console are connected, objects must be imported via Augment3d Edit Mode on the tether device.

Once imported, the file will appear in the Library. Drag it into your workspace to add it to your model.

> **CAUTION:** *Custom objects must be used in the Augment3d model in order to be saved with the show file. Custom materials not added will be deleted upon shutdown of Augment3d.*
>
> For a full list of supported 3D file types, see *Supported 3D File Formats (on page 543)*.

##### Import Options

After a file is selected via the file browser, the Import Options panel will display.

*(figure omise)*{width="2.0892082239720033in" height="2.16125in"}

Use the available options to configure the import to correctly represent your file in Augment3d.

###### Model Size

The original object dimensions are displayed in the original unit. Choose a different measurement from the dropdown to import the object with those units.

> **Note:** *Vectorworks converts objects to metric on export even when drawn in imperial. It is best to select meters on import, but check scaled values for accuracy.*

###### Origin Position

Determines the position of the object relative to the origin when added to the model from the Library. Defaults to Ground.

> *(figure omise)*{width="4.9620909886264215in" height="2.604582239720035in"}

-   As Model - the object will be placed using the origin point defined in the object model.

-   Center - the object will be centered on the origin.

-   Ground - the object\'s base will be aligned with the origin.

-   Top - the object\'s top will be aligned with the origin.

###### Optimization

A color-coded display of the nodes, meshes, and triangles in the object. A large number of any of these properties in an imported object can affect Augment3d performance. If your object contains more than recommended, the number will display in red.

Select Combine Meshes to combine all meshes in the object. This cannot be undone.

###### {Advanced}

Reveals the following additional import options:

####### Model Size

-   Preserve Aspect Ratio - when disabled, allows you to adjust each scaled dimension independently. Defaults to enabled.

####### Model Orientation

Unlike some 3D modeling software, Augment3d uses the Z plane for up / down positioning. Defaults to Automatic.

-   Automatic - uses the coordinate assignments from the source software.

-   Z-Up - assigns Z to up / down.

> **Note:** *If your model imports sideways, reimport using Z-Up.*

####### Optimization

-   Remove Small Meshes - removes meshes from the object below the specified size.

-   Min. Mesh Size - sets the minimum mesh size.

-   Avoid pure black and full metallic - avoids any pure black or full metallic materials by adjusting them just off pure.

-   Max. Material Size - sets the maximum material size.

#### Supported 3D File Formats

##### Optimal Import Formats

Augment3d supports single-file import of model and fixture information from the following programs or later:

-   Vectorworks 2023, Service Pack 3

    -   MVR

-   Capture 2022

    -   MVR

    -   Capture Model GITF

-   WYSIWYG R46

    -   MVR

> **Note:** *Previous versions of Vectorworks require a plug-in for Augment3d import. See Vectorworks Augment3d Plug-in (on page 702).*

These 3D file formats have been found to work optimally for import into Augment3d:

-   DAE

-   ZAE

-   FBX

DAE files, also known as Collada files, are the optimal export format for Augment3d from AutoCAD and Vectorworks.

##### All Compatible 3D Formats

This is a comprehensive list of all 3D file formats compatible with Augment3d:

-   3D

-   3DS

-   3MF

-   AC

-   AC3D

-   ACC

-   AMF

-   ASE

-   ASK

-   ASSBIN

-   B3D

-   BLEND

-   BVH

-   COB

-   CSM

-   DAE

-   DXF

-   ENFF

-   FBX

-   GLB

-   GLTF

-   HMP

-   IFC

-   IFCZIP

-   IRR

-   IRRMESH

-   LWO

-   LWS

-   LXO

-   MD2

-   MD3

-   MD5ANIM

-   MD5CAMERA

-   MD5MESH

    -   MDC

    -   MDL

    -   MESHXML

    -   MESH

    -   MOT

    -   MS3D

    -   NDO

    -   NFF

    -   OBJ

    -   OFF

    -   OGEX

    -   PK3

    -   PLY

    -   PMX

    -   PRJ

    -   Q3O

    -   Q3S

    -   RAW

    -   SCN

    -   SIB

    -   SKP

    -   SMD

    -   STL

    -   TER

    -   UC

    -   VTA

    -   X

    -   X3D

    -   X3DB

    -   XGL

    -   XML

    -   ZAE

    -   ZGL

### Augment3d with Magic Sheets & Pixel Maps

> Right-click on the Augment3d tab to reveal the context menu, which contains options for working in tandem with pixel maps (see *Virtual Media Server (on page 548)*) and magic sheets (see *About Magic Sheets (on page 476)*).
>
> *(figure omise)*{width="0.9291382327209099in" height="1.5279166666666666in"}
>
> The context menu also has options to set the display mode of Augment3d. See Setup > *User > Displays (on page 223)* > {Augment3d Display Mode}.

#### Augment3d with Pixel Maps

##### Set Channel Locations From Pixel Map

This option allows you to pull fixture locations from an existing pixel map in your show file.

Specify the pixel map number and any X/Y/Z constraints. Select {Confirm} to place fixtures in your show at the same locations they exist in the pixel map.

##### Create Pixel Map From Channel Locations

This option allows you to use your existing Augment3d fixture locations to create a pixel map.

Specify the camera direction that the fixture locations will be pulled from and a pixel map number. Select {Confirm} to create a pixel map with fixtures at the same locations they exist in the Augment3d model.

> **Note:** *This option is governed by fixture selection. If no fixtures are selected, all fixtures in the Augment3d model will be added to the pixel map.*

##### Create Pixel Map From Magic Sheet

This option allows you to create a Pixel Map from an existing magic sheet.

Specify the pixel map to create and the magic sheet to pull from. Select {Confirm} to create a pixel map with fixtures at the same locations they exist in the magic sheet.

#### Augment3d with Magic Sheets

##### Create Magic Sheet From Pixel Map.

This option allows you to create a magic sheet from an existing pixel map.

Specify the magic sheet to create and the pixel map to pull from. Select {Confirm} to create a magic sheet with fixtures at the same locations they exist in the pixel map.

##### Set Channel Locations From Magic Sheet

This option allows you to pull fixture locations from an existing magic sheet in your show file.

Specify the magic sheet number and any X/Y/Z constraints. Select {Confirm} to place fixtures in your show at the same locations they exist in the magic sheet.

##### Create Magic Sheet From Channel Locations

> **Note:** *This option is governed by fixture selection. If no fixtures are selected, all fixtures in the Augment3d model will be added to the magic sheet.*

This option allows you to use your existing Augment3d fixture locations to create a magic sheet.

You can specify the camera direction that the fixture locations will be pulled from and a magic sheet number to create. Select {Confirm} to create a magic sheet with fixtures at the same locations they exist in the Augment3d model.

###### Scale

Scale is measured as a ratio of pixels to 1 meter, and defaults to 80, which would create a magic sheet measuring 80 pixels for each meter in the Augment3d model. Any scale from 1 to 200 can be entered.

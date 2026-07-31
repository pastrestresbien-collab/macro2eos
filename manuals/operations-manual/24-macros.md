# Eos Family User Manual v3.2.0 — Chapitre 24 : Macros

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 24
## Macros
### About Macros

Eos provides you with the ability to record macros, which allow you to compose a series of programming actions and be able to execute them later by recalling the macro.

Macros are comprised of any series of button presses (both hard and softkeys), screen commands and events. Eos provides you with the macro feature to simplify complex or repetitive console programming and operating tasks that you perform often.

When you record the series of button presses to a new macro, you can later play it back by simply pressing the macro direct select button, running it from a linked cue, accessing it from a connected show control system, remotely triggering the macro, or running it from another recorded macro.

You may create up to 99,999 macros either from live, using the macro [Learn] mode to record a sequence of keystrokes as you perform the operation, or you can create a macro from within the macro editor display, entering and editing keystrokes into the macro content editor without actually executing the instructions.

The macro editor display contains a listing of all recorded macros including labels and the contents of the macros stored. All macro editing is accomplished from the macro editor display.

### Store a Macro from Live

The most effective way to store a macro is from live mode using the macro [Learn] mode to record a sequence of button presses as you enter them. You can include any button press on the console (hard key or soft key), except [Macro], the arrow keys, [Escape], [Select], and [Learn].

### Using the [Learn] Key

Pressing the [Learn] key while in live mode places the console in macro learn mode. The [Learn] key flashes and the CIA displays "Learning" above the command line. Assign a number identifier (from 1 to 99,999) to the Macro using the control keypad and press [Enter]. The CIA flashes "Learning Macro ####" above the command line. This indicates that the console is ready to record the macro.

> **Note:** *It is helpful if you plan your macro content in advance of the macro record process. While in learn mode, each button press is recorded as content, even the [Clear] button if you have mistaken a keystroke. There is no way to fix a content error in live mode, but you can rerecord the macro as needed, or you can edit the recorded macro in the macro editor, removing any unneeded commands. See Editing Macros (on page 471)*

Begin writing the sequence of button presses and events for the macro record. When you have finished with the series of events and button presses, press the [Learn] key again to exit macro learn mode.

Examples of a macro record function include:

-   [Learn] [1] [Enter] [Go To Cue] [Out] [Time] [0] [Enter] [Learn] - records macro 1 with the go to cue out command.

-   [Learn] [5] [Enter] [1] [Full] {Chan Check} [Enter] [Learn] - records macro 5 with channel 1 at full in channel check mode. To check the next channel in the list, press [Next].

-   [Learn] [4] [Enter] [-] [Sub] [Record] [Learn] - records macro 4 with instructions to record a target excluding all submaster data.

-   [Learn] [2] [Enter] [-] [Group] [6] {Color} [Record] [Learn] - records macro 2 with instructions to record a target excluding the color data from group 6.

You can also create a macro in live that bumps submasters across fader pages but first you must have content assigned to the submasters.

> Write submasters 1 through 5 and 15 through 17, each with its own channel selections at 100%. Then press:
>
> [Learn] [1] [Enter] [Bump1] [Bump2] [Bump3] [Bump4] [Bump5] [Fader Page]
>
> [Bump15] [Bump16] [Bump17] [Learn]

Once you have created the macro from Live in [Learn] mode, you can easily edit the sequence from the macro editor display. See *Macro Editor Display (below)*.

### Macro Editor Display

Macro editing is accomplished from the macro editor display. As an alternative to recording your macro in live, you may create it from this display instead. Open the macro editor display by pressing [Macro] [Marco], from the browser by navigating to Record Target Lists > Macro Editor, or press [Tab] [1] [8].

The display is divided horizontally, the top portion displays the macro contents in detail while the bottom portion lists all macros, including the label and contents.

![](media/media/image302.png){width="5.456986001749781in" height="1.5802077865266841in"}

While in the macro editor display, any numeric entry on the command line is assumed to be a macro number. If the macro number entered already exists and [Enter] is pressed, the macro list will page to the selected macro and the macro content detail section will display all of the contents of the selected macro. If the macro number entered does not exist in the list and [Enter] is pressed, an empty macro will be created with the specified macro number.

While in the macro editor display, the following functions may be performed using the control keypad and softkeys:

-   [Label] - when a macro is selected and [Label] is pressed, the alphanumeric keypad will display on the CIA. Label the macro and press [Enter].

-   [1] [Label] <name> [Enter] - labels macro 1

-   {Icon} - macros can be assigned an icon, which can be configured to appear on the direct select button in Direct Selects (Tab 4) or Custom Direct Selects (Tab 39). See *Icons (on page 120)*.

-   {Color} - assign colors ({Red}, {Green}, or {White}) or {Dark} to a macro. {Dark} assigns no color to the macro. The colors will display beside the macro name in a direct select, and/ or if that macro has been assigned to one of the customizable hardkeys on Eos Ti, Gio, Gio \@5, and RPU.

-   There is also a {Toggle Blink} softkey. By default a customizable hardkey will blink when the macro assigned to it is running. This softkey will turn off the blinking if it is enabled and a BD will display in the color column when blinking is disabled.

-   Not available on Element Classic

-   [Delete] - when a macro is selected and [Delete] [Enter] is pressed, you will be prompted to confirm the deletion of the selected macro. To confirm press [Enter], to abort press [Clear].

-   [1] [Delete] [Enter] [Enter] - deletes macro 1 from the list.

-   [Copy To] - when a macro is selected and [Copy To] is pressed, you will be prompted to enter the macro number that you want to copy the contents of the selected macro to. You will be prompted to confirm the copy process, press [Enter] to confirm or [Clear] to abort the copy to process.

-   [1] [Copy To] [6] [Enter] [Enter] - copies the entire contents of macro 1 to macro 6.

-   {Edit} - when a macro is selected and {Edit} is pressed, you will have entered edit mode for the selected macro. See *Editing Macros (on the facing page)*. Three notable changes to your macro editor display include:

-   a blinking cursor in the macro content detail portion (top) of the display.

-   "Press [Select] to save or [Escape] to cancel changes"displays above the command line.

-   {Move To} - allows you to move and reorganize your macros anywhere in the macro list numerically. You can access {Move To} by pressing [Copy To] twice.

-   For instance, if you have macros 1 through 5 in the list, and you want to move/ change macro 1 to macro 6 so that your most commonly used macros are first in the list, you would press [1] {Move To} [6] [Enter]. This leaves only macros 2 through 6 in the list.

-   {Mode} - allows you to assign different modes for the macro to run in. There are three modes: background, foreground, and default.

-   {Default}

-   When a macro in default mode is run manually, it runs in the foreground(i.e., the command line) on the device that fired it. When a macro in default mode is executed by a cue or via show control, it runs in the background on the master device.

-   Running a macro on a master device only matters when the macro changes the displays of the device it runs on such as snapshot and flexichannel macros.

-   {Background}

-   When a macro in background mode is run manually, it runs on the device that fired it but will not affect its command line.

-   A macro in background mode that is run from a cue or via show control will run on the master device but will not affect the master\'s command line.

-   When a background macro is running and includes a link to another macro, or is currently waiting, pressing the [Macro] button will stop it.

-   {Foreground}

-   When a macro in foreground mode is run manually, it runs on the device that fired it and affects its command line.

-   If a foreground mode macro is fired via show control, it runs on the master device and will affect its command line.

-   If a cue fires the macro, it will run on the device whose user last pressed [Go] on that playback. If a foreground macro is fired from a cue that is executed from another cue list, the macro will run on the device that last pressed [Go] on the cue's playback but not the playback that triggered the executed cue.

-   {Target Device} - A macro can have a Target Device assigned to it. This allows a cue to execute a macro only on a certain console.

-   The Target Device can be a device name or User ID. These are assigned to a macro in the Macro Display by using the {Target} softkey and either selecting {Device} and {User}. Pressing {Target} will also display a list of connected devices and additional target options.

> {SC Learn} - enables or disables excluding specific macros from being learned as show control events. See *Adding Events Using Learn (on page 603)*.

### Editing Macros

Once a macro is created, you can edit the content by removing or adding commands from the macro editor display.

Select an existing macro number and press [Enter]. The selected macro\'s contents will display in detail. Press {Edit} to make changes to the content.

The cursor in the macro content detail section of the display can be moved through the existing content list using the arrow keys. Arrow keys are not stored as macro content. To add content, place the cursor in the section that you want to insert, then add the command. To delete a command, place the cursor ahead of the content to be deleted, then press the

{Delete} softkey.

Press [Select] when you have completed all editing. Press [Escape] to exit the editor.

> **Note:** *Macros for options with a toggle action between enable and disable, such as AutoMark in setup, can use the {Enable} and {Disable} softkeys for creating absolute actions instead of toggles.*

#### Macro Softkeys

![](media/media/image303.png){width="4.834646762904637in" height="1.2112489063867016in"}

In edit mode, the CIA displays all softkeys available for the system that would otherwise be difficult to find when recording a macro. You can also choose from a list of the most common macro commands, or any lamp commands. The paging buttons allow you to scroll through the available softkeys in any of these selections. Paging buttons are not stored as macro content.

The search button allows you to search a scrollable list of all macro commands. Typing will filter the list. Pressing [Enter] on a command will place it into the macro and return to the search field. [Learn] or {Done} will exit edit mode.

##### Macro-Specific Softkeys

A new set of macro editor softkeys are displayed while in edit mode including:

-   {Loop Begin} - inserts a start command for a loop with a limited number of iterations. An infinite loop is assigned when you use "0" for the iterations.

-   {Loop End} - inserts a loop end command.

-   {Wait} - inserts a pause for a period of time. This needs to be followed with a whole number of seconds.

-   {Delete} - removes commands from the macro.

-   {Wait for Entr} - inserts a pause in the macro that waits for the [Enter] key. Pressing [Enter]will resume the macro.

-   {Wait for Input} - inserts a pause in the macro to allow you to enter data. The pause lasts until you press the [Macro] key again. Then the remainder of the macro will be completed.

-   {Done} - exits macro edit mode. You may also use the [Learn] key to enter and exit edit mode.

#### Creating Macros

Macros can also be created in the macro editor display. Enter any unrecorded macro number from 1 to 99,999 and press [Enter]. Your new macro number will display in the macro list in numerical order but without a label or any contents. To store the macro contents, select the macro and press {Edit}.

-   <Macro> [3] [Enter]

-   {Edit}

-   [Select Active] [At] [5] [Enter]

-   [Sneak] [Time] [1] [0] [Enter]

-   [Macro] [5] [Enter]

-   [Select]

> Creates macro 3. Writes the instruction to set all active channels to 50%, then sneak them to their original levels over 10 seconds and last, links to macro 5.

### Play a Macro

You can play a macro from the command line, from the direct selects, run it from a linked cue, or from another macro.

To play macro 5 from the command line press [Macro] [5] [Enter]. "Running Macro 5" displays above the command line in live while the macro is running.

To run macro 5 from the macro direct selects simply press {Macro 5}. "Running Macro 5" displays above the command line in live while the macro is running.

To run macro 5 from cue 1 press:

-   [Cue] [1] {Execute} [Macro] [5] [Enter]

If you would like to run multiple macros from cue 1, press:

-   [Cue] [1] {Execute} [Macro] [6] [Enter]

-   [Cue] [1] {Execute} [Macro] [7] [Enter]

Each macro has to be entered individually. The previous example would result in macros 5 through 7 being executed from cue 1.

### Stop a Macro

If you need to stop a Macro while running (for example, during an infinite loop) you may press [Escape] and the macro will stop.

### Deleting Macros

You can delete a macro from the Macro Editor display by selecting the macro and pressing [Delete] [Enter]. You will be prompted to confirm the deletion. Confirm by pressing [Enter] again, or abort by pressing [Clear].

> Delete macro 5 from the macro list.

-   [5] [Enter]

-   [Delete] [Enter] [Enter] Or from any display:

-   [Delete] [Macro] [5] [Enter]

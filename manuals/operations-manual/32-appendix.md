# Eos Family User Manual v3.2.0 — Chapitre 32 : Appendix

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 32
## Appendix
### Vectorworks Augment3d Plug-in

Eos 3.2.0 and newer utilize Vectorworks\' MVR export to move model and fixture data, and require Vectorworks 2023 Service Pack 3 or later. Older versions of Eos use generic 3D exports from Vectorworks for models, and an ETC-made plug-in for fixture data.

Legacy installation instructions for the plug-in are available below.

#### Vectorworks System Requirements

Please reference [vectorworks.net/sysreq](https://www.vectorworks.net/sysreq).

#### Installing the Vectorworks Augment3d Plug-in

1.  Download the appropriate plug-in for your operating system (Windows or macOS) from [etcconnect.com](http://www.etcconnect.com/), and extract it. The folder will contain a copy of these instructions and the Vectorworks Augment3d Plug-in as a .vwlibrary file.

2.  Open Vectorworks and navigate to Tools > Plug-ins > Plug-in Manager > Third-party Plug-ins.

![](media/media/image460.png){width="2.7880424321959754in" height="0.7125in"}

3.  Select {Install} and choose the .vwlibrary plug-in file you extracted in Step 1.

4.  Restart Vectorworks when prompted. After relaunch, the installed plug-in will appear in the Built-in Plug-ins tab.

![](media/media/image461.jpeg){width="2.790171697287839in" height="1.35375in"}

#### Configuring Vectorworks to use the Augment3d Plug-in

1.  Launch Vectorworks.

2.  Configure your Vectorworks workspace.

    a.  Open the Workspace Editor. Navigate to Tools > Workspaces > Edit Current Workspace.

    b.  Expand the ETC node in the Commands panel:

![](media/media/image462.png){width="2.7694313210848645in" height="1.167707786526684in"}

c.  Drag \"Export to ETC Augment3d\" to the Spotlight node.

d.  Select {OK} to close the Workspace Editor.

```{=html}
<!-- -->
```
3.  In Vectorworks 2019, you must map the information you want to export to Augment3d. (Vectorworks 2020 and later do not have this option; skip to step 4.) If exporting for the first time, or to change export preferences, navigate to File > Document Settings

-   Spotlight Preferences.

    a.  Select Edit Visualizer Data Mapping. Recommended mapping below:

![](media/media/image463.png){width="1.0356725721784776in" height="0.7560411198600175in"}

b.  Select {OK} to close the Data Mapping window.

```{=html}
<!-- -->
```
4.  Navigate to Spotlight > Export to ETC Augment3d and follow the prompt. Vectorworks will export an a3d file containing your information for import into Augment3d.

> **CAUTION:** *Layers containing lights must be visible in the Vectorworks file in order to export to Augment3d. If no lights are visible, a pop-up will notify you that the file is empty, and cannot be exported.*

#### Importing to Augment3d

> Vectorworks Augment3d files can be imported into Augment3d *Using the Browser (on page 83)* via File > Import > Augment3d (From Vectorworks).

When importing, you will likely need to adjust the data before proceeding.

![](media/media/image165.jpeg){width="5.080823490813648in" height="1.1439577865266841in"}

##### Options

The following options are available:

-   Starting / Ending Channel - defines a specific range of channels to be imported.

-   Overwrite - overwrites the data in the show file when enabled, and merges the data when disabled. Disabled by default.

-   Update fixture types - enables or disables the update of fixture types in the show file. Enabled by default.

-   Only import Augment3d XYZ location - enables import of just Augment3d location data. Disabled by default.

-   Only Import Text/Notes/Labels/Gels - enables import of just the patch database text. Disabled by default.

##### Mapping Fields

You can map Eos patch fields to fields in the source file being imported. Channel and Address are required; any other field can be ignored if desired. Options can be selected again for placement in multiple fields.

###### Address Formats

Eos will accept multiple address formats for importing. Examples of those formats are 2/3, 2.3, 2,3, 2-3. Eos will convert all formats to n/n.

##### {Map Devices}

You can also map Eos fixture library devices to devices in the source file.

![](media/media/image166.png){width="5.13340113735783in" height="1.3220833333333333in"}

1.  Select {Map Devices} to open the mapping utility.

2.  Select a device from the Source File column and choose its matching Eos fixture profile. Multiple devices can be selected at a time.

![](media/media/image167.png){width="4.7091447944007in" height="1.1281244531933508in"}

3.  Select {Link Devices}.

![](media/media/image168.png){width="4.7091447944007in" height="1.1281244531933508in"}

4.  Repeat steps 2 and 3 until all devices have been associated with fixture profiles. To unlink a device, select it in the Mapping column and select {Unlink Device}.

5.  When complete, select {Done}, then {OK}. Your devices and their associated position information will now appear in Patch and Augment3d.

![](media/media/image395.png){width="3.9828740157480316in" height="1.235in"}

Device mapping and import fields are saved with the show file.

#### Exporting Scenery

The Vectorworks Augment3d Plug-in only supports the export of fixtures.

Follow the steps below if you have scenery in your Vectorworks file that you would also like to export.

1.  Hide all fixtures in the Vectorworks workspace.

2.  Expose only the scenery you wish to export, then export as a Collada file by navigating to File > Export > Export COLLADA (3D Only).

3.  In Augment3d, import the Collada file. For more information on importing Augment3d objects, refer to the Eos Family Operations Manual chapter on Augment3d.

### Copyright and Regulatory

Art-Net™ Designed by and Copyright Artistic Licence

#### Apex 5, 10, and 20, Apex Remote Processor, Eos Remote Interface, and Windows 10-based Ion Xe, Ion Xe20, Ion Xe RPU, Gio@5, and Element 2

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

NOTE: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

-   Reorient or relocate the receiving antenna.

-   Increase the separation between the equipment and receiver.

-   Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.

-   Consult the dealer or an experienced radio/TV technician for help. Contains Model: 9260NGW

Contains FCC TX ID: PD99260NG Canada IC:1000M-9260NG

##### Japan

RF:003-170125 TEL:D170079003

##### South Korea

MSIP-CRM-INT-9260NGW

######## WARNING: This device contains a lithium battery. Battery may explode if mistreated. Do not recharge, disassemble or dispose of in fire.

> **CAUTION:** *Power cord must be connected using an earth ground connection.*

A fuse is included for additional protection. Fuse ratings can be found on the rear panel of your console.

> **CAUTION:** *For continued protection against risk of fire, replace only with same type and rating of fuse.*
>
> **VORSICHT:** *Um weiterhin gegen Brandrisiko geschützt zu sein, ersetzen Sie die Sicherung nur mit einer Sicherung gleichen Typs und den gleichen Nennwerten.*
>
> **ATTENTION:** *Pour ne pas compromettre la protection contre les risques d'incendie, remplacer par un fusible de même type et de mêmes caractéristiques nominales.*

#### ETCnomad Puck

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

NOTE: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

-   Reorient or relocate the receiving antenna.

-   Increase the separation between the equipment and receiver.

-   Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.

-   Consult the dealer or an experienced radio/TV technician for help. Contains Model: AX200NGW

Contains FCC TX ID: PD9AX200NG Canada IC:1000M- AX200NG

##### Japan

RF:003-190022 TEL:D190021003

##### South Korea

R-C-INT-AX200NGW

![](media/media/image464.png){width="8.443350831146107e-2in" height="8.375984251968505e-2in"}![](media/media/image465.png){width="2.1777121609798774e-2in" height="2.211395450568679e-2in"}![](media/media/image465.png){width="1.6332020997375327e-2in" height="1.682633420822397e-2in"}![](media/media/image3.png){width="2.0609142607174103e-2in" height="2.179899387576553e-2in"}![](media/media/image13.png){width="1.4559273840769904e-2in" height="1.8375984251968503e-2in"}![](media/media/image466.png){width="1.0439632545931759e-2in" height="1.3456911636045494e-2in"}![](media/media/image467.png){width="1.3916229221347332e-2in" height="1.7735126859142608e-2in"}![](media/media/image468.png){width="1.4843613298337707e-2in" height="1.8685476815398075e-2in"}![](media/media/image469.png){width="1.5844269466316712e-2in" height="1.9934383202099736e-2in"}![](media/media/image14.png){width="1.5454943132108486e-2in" height="1.6583552055993e-2in"}![](media/media/image470.png){width="1.3916229221347332e-2in" height="1.7730752405949256e-2in"}![](media/media/image471.png){width="1.456583552055993e-2in" height="1.8381452318460192e-2in"}![](media/media/image472.png){width="1.0439632545931759e-2in" height="1.3445975503062117e-2in"}![](media/media/image473.png){width="1.0e-2in" height="1.3001968503937008e-2in"}![](media/media/image474.png){width="1.3319116360454943e-2in" height="1.7127077865266842e-2in"}![](media/media/image475.png){width="1.3314741907261592e-2in" height="1.7130358705161854e-2in"}![](media/media/image476.png){width="1.0e-2in" height="1.3001968503937008e-2in"}![](media/media/image3.png){width="2.4774715660542432e-2in" height="2.441819772528434e-2in"}![](media/media/image8.png){width="2.963801399825022e-2in" height="3.126093613298338e-2in"}![](media/media/image477.png){width="3.952099737532808e-2in" height="4.0498687664041993e-2in"}![](media/media/image478.png){width="3.952099737532808e-2in" height="4.050415573053368e-2in"}![](media/media/image479.png){width="9.993547681539808e-2in" height="0.16488735783027123in"}![](media/media/image8.png){width="2.8138670166229222e-2in" height="3.08584864391951e-2in"}![](media/media/image480.png){width="3.516622922134733e-2in" height="3.8038057742782155e-2in"}![](media/media/image481.png){width="4.396434820647419e-2in" height="4.62412510936133e-2in"}![](media/media/image24.png){width="4.4638013998250216e-2in" height="4.469597550306212e-2in"}![](media/media/image482.png){width="0.1126509186351706in" height="0.11253608923884514in"}![](media/media/image483.png){width="3.343175853018373e-2in" height="3.7560148731408574e-2in"}![](media/media/image7.png){width="3.026356080489939e-2in" height="3.268372703412074e-2in"}![](media/media/image484.png){width="3.891404199475065e-2in" height="4.2178477690288714e-2in"}![](media/media/image485.png){width="4.456911636045494e-2in" height="4.808617672790901e-2in"}![](media/media/image486.png){width="3.0307305336832895e-2in" height="3.570538057742782e-2in"}![](media/media/image487.png){width="2.963801399825022e-2in" height="3.126531058617673e-2in"}![](media/media/image488.png){width="3.516622922134733e-2in" height="3.8028215223097114e-2in"}![](media/media/image489.png){width="2.8138670166229222e-2in" height="3.08584864391951e-2in"}![](media/media/image490.png){width="3.343175853018373e-2in" height="3.7564523184601926e-2in"}![](media/media/image491.png){width="3.0307305336832895e-2in" height="3.570100612423447e-2in"}![](media/media/image492.png){width="4.456911636045494e-2in" height="0.10377952755905512in"}![](media/media/image493.png){width="3.02580927384077e-2in" height="3.2658573928258966e-2in"}![](media/media/image14.png){width="1.5452755905511812e-2in" height="1.656933508311461e-2in"}![](media/media/image494.png){width="9.98578302712161e-3in" height="1.299540682414698e-2in"}![](media/media/image495.png){width="9.994531933508312e-3in" height="1.299540682414698e-2in"}![](media/media/image496.png){width="0.33559930008748906in" height="0.17613188976377953in"}

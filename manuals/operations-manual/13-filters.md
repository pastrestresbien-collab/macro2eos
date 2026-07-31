# Eos Family User Manual v3.2.0 — Chapitre 13 : Filters

- Source : DOCX officiel ETC « Eos Family User Manual », Version 3.2.0, réf. 4250M1210-3.2.0 Rev A, publié 2023-04
- Fichier source : [`source/EosFamily_v3.2.0_UserManual_RevA.docx`](source/EosFamily_v3.2.0_UserManual_RevA.docx)
- Confiance : A (document officiel ETC — conversion intégrale du texte ; les illustrations/captures d'écran ne sont pas reproduites, seul le texte)

---

# Chapter 13
## Filters
  -----------------------------------------------------------------------------------------------
  ---------------------------------- ------------------------------------------------------------
  -----------------------------------------------------------------------------------------------
### About Filters

Filters are used to determine which parameters can be stored to cues, palettes, and presets. The filter selection tool in the CIA affects record operations as long as the filters are set.

> **Note:** *Channel and parameter filters can be applied to faders and submasters. Those* *type of filters affect playback and not record functions.*

### Record Filters

Record filters are used to select specific parameter data to store to record targets. When no filters are selected, all parameters can be stored, as appropriate to the [Record], [Record Only], and selective record action used.

> **Note:** *When storing show data, applied filters are highlighted and allow the associated parameters to be stored in record targets.*
>
> **Note:** *When filters are deselected (not highlighted), they prohibit storing the associated parameters.*
>
> **Note:** *There is no difference between having all filters selected and having no filters selected (default). In either state, all parameters are available for recording.*

Record filters are applied from the CIA using the following buttons: {Filter}, the parameter buttons in the CIA, and the parameter category buttons.

The parameter category buttons can be used to select filters, as follows:

-   Intensity (enables recording intensity data)

-   Focus (enables recording pan and tilt)

-   Color (enables recording color data)

-   Beam (enables recording all beam data) To apply record filters by category:

1.  Press and hold {Filter}. The parameter buttons change to display filter selection.

2.  Press the parameter category softkey {Intensity/Focus/Color/Beam} for the category you want to include in the record target. All parameters in that category will be highlighted and "Filter On" will appear above the softkey.

3.  Release {Filter}. The buttons return to their normal appearance.

In subsequent record functions, only the filtered categories will be recorded. You may apply multiple category filters at once. Remember that applying all filters and no filters yields the same effect.

### Partial Filters

If you do not want an entire category to be recorded, you may apply parameter specific filters (partial filters) instead.

To apply partial filters:

1.  Press and hold {Filter}. The parameter buttons change to display filter selection.

2.  Press the parameter button (for example {Zoom}) for the parameter you want to include in the record target. That parameter will be highlighted and "Filter On" will appear

> above the softkey.

3.  Release {Filter}. The buttons return to their normal appearance.

In subsequent record functions, only the filtered parameters will be recorded. You may apply as many partial filters at once, as you wish. Any unfiltered parameters will not be included in record actions. In Live, unfiltered parameter data is displayed in gray, with an "N" (indicating null data) in the upper right corner of the parameter's field.

### Clearing Filters

Applying filters is a toggle state. To clear any filter, simply repeat the application process described above. When pressed again, any applied filter will be removed.

To clear all filters at once:

1.  Press and hold {Filter}. The parameter buttons change to display filter selection. {Clear Filters} appears in the upper left corner of the parameter buttons.

2.  Press {Clear Filters}. Any applied filters will be removed and the highlights will turn off.

3.  Release {Filter}. The buttons return to their normal appearance. All parameters are now available to record functions.

### Storing Data with Record Filters

If a record target is stored with filters in place, the filters allow only associated parameter data to be recorded in the target. Non-filtered data is not included when you record.

The various record targets are affected by filters in the following ways:

-   Palettes - Palettes by definition are already filtered. The color and beam filters can be used to further modify what is stored in the color and beam palettes, however.

-   Presets - Active filter settings impact what is stored in presets.

-   Cues - Active filter settings impact what is stored in cues, even when using "record only" commands.

-   [Recall From] - Recall from instructions are not affected by the filters.

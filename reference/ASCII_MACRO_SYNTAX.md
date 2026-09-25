# Syntaxe des macros dans un export ASCII Eos

**Source** : analyse d'un export ASCII réel de production, `Eos_Family_Busking_Rev_B.asc`
(Eos 3.3.9, tournée busking), fourni par l'utilisateur — **pas** une documentation
officielle ETC (aucune spec ASCII des macros trouvée dans le corpus `manuals/`).
Tout ce qui suit est **déduit par observation structurelle** d'un fichier réel, pas
confirmé par un manuel. À vérifier au banc avant de faire confiance à un import.

## Anatomie d'un bloc macro

```
$MacroDef 8032
   Text Upd Color BT
   $$MacroMode Background          ! absent = mode par défaut (à clarifier)

   $$MacroContents Color Convertir_en_Manuel <Enter>
   $$MacroContents Select_Last Update Palette_Couleur Par_Type

   $$MacroCommands 90 313 38 86 30 114 676
```

- `$MacroDef <n>` — ouvre la macro numéro `n` (même plage que les softkeys de bouton
  macro en façade/nomad).
- `Text <libellé>` — nom affiché sur le bouton.
- `$$MacroMode Background` ou `Foreground` — optionnel. Observé sur les macros qui
  attendent une saisie (`Wait_For_Input`) ou qui touchent plusieurs faders/subs d'un
  coup ; absent sur la majorité des macros simples. Rôle exact non confirmé.
- `$$MacroContents` — **texte lisible**, un mot par token, ponctué de `<Enter>` pour
  chaque validation. C'est la représentation humaine (celle qu'affiche l'éditeur de
  macro sur la console).
- `$$MacroCommands` — **la même séquence en codes numériques**. Chaque mot de
  `$$MacroContents` correspond, dans l'ordre, à un nombre de `$$MacroCommands` (vérifié
  par alignement sur 115 macros du fichier réel, cf. table ci-dessous). Hypothèse forte
  mais **non confirmée par une doc officielle** : `$$MacroCommands` est probablement la
  séquence réellement rejouée à l'exécution, `$$MacroContents` n'étant qu'un affichage —
  à vérifier au banc (ex. : modifier `$$MacroContents` sans toucher `$$MacroCommands`
  dans un import, voir si le libellé affiché change sans changer le comportement).

## Dictionnaire code → commande (partiel, déduit par alignement)

Construit en découpant les 115 macros du fichier source en couples
(mot de `$$MacroContents`, nombre de `$$MacroCommands`) à la même position, sur les
macros où les deux listes ont la même longueur (68 macros exploitables). Les valeurs
purement numériques (`-1`, `10091`, `99.61`…) sont des **paramètres** (numéro de sub,
pourcentage de fader), pas des codes de commande — à ne pas confondre.

| Code | Commande | | Code | Commande |
|---|---|---|---|---|
| 23 | Sneak | | 313 | Convertir_en_Manuel |
| 26 | Cue | | 392 | Macro_Wait |
| 27 | Record | | 407 | Inverse |
| 29 | Jusqu'à | | 437 | Circuits_Aléatoires |
| 30 | Update | | 511 | Fader |
| 34 | Query | | 523 | Flexi_Actifs |
| 38 | \<Enter\> | | 552 | Effacer_Ligne_Cmd |
| 39 | . (point) | | 608 | Home |
| 44 | Live | | 676 | **Par_Type** (= By Type) |
| 45 | Blind | | 790 | Tab_Bas |
| 48 | Setup | | 791 | Tab_Haut |
| 57 | / (slash) | | 813 | Flexi_Patché |
| 76 | Suivant | | 839 | ReleaseSub |
| 77 | Précédent | | 841 | StopEffet |
| 80 | Beam | | 873 | Form |
| 84 | Image | | 898 | FaderMvt |
| 85 | Intensity | | 1087 | SubOff |
| 86 | Select_Last | | 1101 | Centré |
| 87 | Select_Manual | | 1103 | Nbre_Groupes |
| 89 | Focus | | 1104 | Miroir_Out |
| 90 | Color | | 1106 | Regrouper |
| 91 | Shutter | | 1119 | Flexi_Manuel |
| 102 | Bouton_Macro | | 1161 | Miroir_In |
| 114 | Palette_Couleur | | 1362 | Chgmts_Live |
| 119 | Preset | | 143 | Fan_ |
| 143 | Fan_ | | 144 | Offset |
| 146 | Pair | | 147 | Impair |
| 162 | Est_Dans | | 197 | Magic_Sheet |
| 228 | CueOnlyTrack | | | |

Chiffres `0`-`9` et `10` (`@`) codés à l'identique de leur valeur/caractère. Table
incomplète : seulement les mots vus dans ce fichier. Toute nouvelle macro analysée peut
l'enrichir (même méthode : aligner `$$MacroContents` et `$$MacroCommands` mot à mot).

## Ce qui marche en macro vs ce qui bloque

Confronté à `manuals/operations-manual/JOURNAL_observations_banc.md` (phase 9, section
« Macro de patch — softkey `{Type}` en macro (ÉCHEC) ») :

- **Échec confirmé au banc** : le softkey `{Type}` du **Patch** ne s'exécute pas depuis
  une macro (`Wait_For_Input Type …` reste bloqué).
- **Fonctionne dans ce show réel** (macros 8031/8032, `Par_Type` = code `676`) : le
  softkey **`{By Type}` d'un Record/Update de palette**, lui, s'exécute bien en macro :
  ```
  $$MacroContents Select_Last Record Palette_Couleur Par_Type   ! nouvelle palette By Type
  $$MacroContents Select_Last Update Palette_Couleur Par_Type   ! mise à jour par type
  ```
- **Conclusion** : les deux `{Type}` ne sont **pas le même softkey** — celui du Patch
  (assigner un modèle à un channel) bloque en macro, celui d'un Record/Update de palette
  (désigner un circuit comme défaut de type / mettre à jour le défaut) ne bloque pas.
  Ça correspond à deux méthodes différentes du tuto (A = Patch, jamais macro-isable en
  l'état ; B/E.4 = Record/Update palette, candidat macro).

## Piste à tester pour la macro de préparation (tuto, étape B)

**[non testé au banc]** — gabarit à essayer pour scripter la désignation des dummies en
défauts de type (tuto §B, étape 6 `{By Type}` sur la sélection de dummies) :

```
$MacroDef 910
   Text Defauts par type

   $$MacroContents Select_Last Palette_Couleur Par_Type <Enter>
   $$MacroCommands 86 114 676 38
```

Le `Select_Last` suppose que les dummies (`2001 2002 3001 3002…`) sont déjà la
sélection courante avant de lancer la macro — donc **taper la sélection à la main
d'abord** (`[2001] [+] [2002] [+] [3001] [+] [3002]`), puis lancer la macro pour
n'automatiser que le `{By Type}`. Reste à valider : le sens exact de `Palette_Couleur`
seul (sans `Record`/`Update` devant) dans ce contexte — dans les deux macros trouvées il
est toujours précédé de `Record` ou `Update`. Essai à faire au banc avec
`Record`/`Update` explicite si `Palette_Couleur` seul échoue.

## Piste à tester pour la retouche en salle (tuto, étape E.4)

**[non testé au banc]** — gabarit calqué sur la macro 8032 réelle (« Upd Color BT »),
pour scripter `[Update] [Color Palette] [n] {By Type} [Enter]` après un réglage manuel
en Live :

```
$MacroDef 911
   Text MAJ palette par type

   $$MacroContents Color Convertir_en_Manuel <Enter>
   $$MacroContents Select_Last Update Palette_Couleur Par_Type

   $$MacroCommands 90 313 38 86 30 114 676
```

Suppose que le projecteur retouché est déjà sélectionné et que la palette visée est
celle actuellement chargée sur ce circuit (comme dans le tuto, retouche encodeur en
Live). `Convertir_en_Manuel` fige la valeur réglée à l'encodeur avant l'Update — à
confirmer que c'est nécessaire dans notre cas (le tuto ne le fait pas à la main
actuellement, étape E.4 va direct à `Update`).

## Import ASCII de macros — ce qu'on ne sait pas encore

- Import partiel (juste des `$MacroDef`, sans le show complet) possible ou non : **non
  testé**.
- Si `$$MacroContents` est purement cosmétique, on pourrait en théorie n'écrire que
  `$$MacroCommands` — **non testé**, risque que la console recalcule/exige les deux à
  l'import.
- Les codes du dictionnaire ci-dessus sont-ils stables entre versions Eos, ou propres à
  la 3.3.9 (build 25) ? **Non vérifié.**

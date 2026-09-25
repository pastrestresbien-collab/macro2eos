# Tuto — Changer le type de toute une famille de projecteurs (tournée)

Méthode « défauts miroirs », validée au banc (Eos 3.3.9, phase 9 de
`manuals/operations-manual/JOURNAL_observations_banc.md`). Les étapes marquées
**[non testé]** restent à confirmer.

---

## Le principe

Chaque palette contient **une valeur par modèle de projecteur**, portée par un **dummy
sans adresse qui ne change jamais de type**. Les vrais projecteurs ne stockent rien dans
les palettes : ils suivent le dummy de leur type du moment.

→ Aucune valeur n'est jamais convertie : **le retour est exact**.

## Plan de numérotation

| Famille | Vrais projecteurs | Maître (modèle du kit) | Équivalents (un par modèle **et par mode**) |
|---|---|---|---|
| Rush Par 2 RGBW Zoom 9ch | 201 → 206 | 2001 | 2002 → 2020 |
| S4 LED S3 Lustr X8 Direct | 301 → 307 | 3001 | 3002 → 3020 |

---

## A. Une seule fois par show : installer les dummies

1. **Patch**, dummies **sans adresse**, label = famille :
   - `[2001] {Type}` → Rush Par 2 RGBW Zoom 9ch
   - `[2002] {Type}` → Robin LEDBeam 350 M1, etc. (un dummy par modèle et par mode)
   - idem 3001, 3002…
   - Astuce : `[201] [+] [2001] {Type}` patche plusieurs channels d'un coup.
2. **Contrôle** : `[About]` → ligne « Paramètres définis » : les dummies consomment de la
   capacité de paramètres.
3. **Préparer les palettes existantes** (voir B, avec toute la plage de palettes).

## B. Préparer des palettes (existantes ou nouvelles)

⚠ **Uniquement sur les palettes pas encore préparées.** Refaire la copie maître →
équivalents sur une palette déjà préparée **écrase les retouches faites en salle**.

En **Blind** :
1. `[Blind] [Color Palette] [n] [Thru] [m] [Enter]` — la plage à préparer
2. `[201] [Copy To] [2001] [Enter]` — valeur Rush → maître Rush
3. `[301] [Copy To] [3001] [Enter]` — valeur Lustr → maître Lustr
4. `[2001] [Copy To] [2002] [Enter]` — et chaque équivalent Rush (2003, 2004…)
5. `[3001] [Copy To] [3002] [Enter]` — et chaque équivalent Lustr
6. `[2001] [+] [2002] [+] … [+] [3001] [+] [3002] [+] … {By Type} [Enter]` — tous les
   dummies deviennent défauts de leur type
7. `[Color Palette] [1] [Thru] [dernière] {Cleanup} [Enter]` — sans risque sur toutes
   les palettes

**Contrôle** : liste des palettes (`[Tab] [2] [4]`) → colonne « Par Type de circuits » =
la liste des dummies, **aucun `+`**.

## C. Ajouter un nouveau modèle équivalent

1. Patch : `[2003] {Type}` → nouveau modèle (sans adresse, label famille).
2. Blind, **toutes** les palettes : `[Blind] [Color Palette] [1] [Thru] [dernière] [Enter]`
3. `[2001] [Copy To] [2003] [Enter]`
4. `[2003] {By Type} [Enter]`
5. Contrôle : liste des palettes, `2003` présent, aucun `+`.

Pas de macro pour ce §C (deux commandes seulement ; relancée par erreur, elle écraserait
les retouches de salle). Les palettes créées **après** l'ajout du dummy le couvrent
d'office (macro 920 : sélection `2001 Thru 3999`).

**[en test] — vigilance particulière** (protocole en cours, journal à suivre) :
- `Copy To` entre types différents copie **tels quels** les paramètres de même nom (V3) :
  Rush → autre RGBW = mêmes chiffres R/G/B/W, **couleur probablement fausse**. À
  vérifier en Live, et retoucher si besoin (§E.4).
- Le maître 2001 ne doit pas bouger ; toutes les palettes doivent recevoir 2003 (y
  compris la palette Home et les palettes déjà retouchées).
- Valider par un aller-retour réel (201-202 → nouveau type → Rush) comparé à des
  valeurs relevées **avant**, en Data verrouillé.

## D. Avant de partir

1. File > Save As (sauvegarde datée).
2. Liste des palettes : **aucun `+`**.

## E. En salle

1. Patch : **Préserver Natif = Désactivé**.
2. **Toute la famille en une commande** :
   `[201] [Thru] [206] {Type}` → modèle de la salle, puis `[At]` adresses de la salle.
3. `[Go To Cue] [cue en cours] [Enter]` (le Live ne se rafraîchit pas seul).
4. **Retoucher une palette** : sélectionner un projecteur, régler, puis
   `[Update] [Color Palette] [n] {By Type} [Enter]` → la valeur part dans le dummy
   équivalent, le maître n'est jamais touché.
   **Macro validée (phase 15-16)** : `Color Update Seulement_les_Ref Par_Type`, **sans
   `[Enter]`** — relire la fenêtre Update (palettes cibles, circuits) puis `[Enter]` à
   la main. Un seul Update met à jour **toutes** les palettes retouchées.
   ⚠ L'Update prend **toutes les valeurs manuelles**, pas seulement la sélection :
   `[Sneak]` d'abord sur ce qu'on ne veut pas pousser.
5. Vérifier une retouche **en Blind** (ou après Go To Cue), jamais dans le Live juste
   après l'Update.

## F. Retour au kit

1. Patch : `[201] [Thru] [206] {Type}` → modèle maître, puis `[At]` adresses du kit.
2. `[Go To Cue] [cue en cours] [Enter]`.
3. Contrôle : liste des palettes sans `+` ; au besoin une palette en Blind, **Data
   verrouillé** (`[Data] [Data]`).

---

## Règles d'or

1. **En cue, la couleur passe toujours par une palette.** Une valeur hors palette est
   convertie à chaque voyage et revient fausse (testé : un vert est revenu ambre).
2. **Dans une palette, aucun projecteur ne porte de valeur propre** (pas de `+`). Besoin
   d'un projecteur différent → une autre palette.
3. **Un dummy par modèle et par mode** Eos. Nommer les modèles comme Eos les affiche.
4. **Un même modèle ne sert pas d'équivalent à deux familles** (un seul défaut par
   modèle et par palette).
5. **Dummies toujours sans adresse** dans le vrai show.
6. **Mesurer en Data verrouillé** : sans lui, Eos arrondit et affiche des noms de plage.

## Limites connues

- Testé : palettes **couleur**. **[non testé]** palettes Focus/Beam, effets, lyres
  (pan/tilt à régler en salle, sujet séparé).
- **[non testé]** `Copy To` vers une plage de dummies (`[2002] [Thru] [2013]`) : copier
  un par un en attendant.
- `{Type}` du **Patch** bloque en macro (phase 9) : le changement de type (§E.2, §F.1)
  reste manuel. `{By Type}` d'un Record/Update de palette fonctionne en macro.
- **Macros validées au banc** :
  - `macros/920_palettes_lee_11-16.asc` — création de palettes By Type sur les dummies
    par gel (`@ <livre>/<gel>`, ex. `@ 3/106` = Lee 106 ; `[Color] 3/24` marche aussi),
    import ASCII partiel accepté (**{Merge Data?}**, Macros seules, pas de `Clear All`).
    Palette « Home » : `Convertir en Manuel` obligatoire, sinon palette **vide** (v2,
    correctif **[non retesté]** en macro).
  - Macro de retouche §E.4 (ci-dessus), en attente du code ASCII de `Seulement_les_Ref`.
- **[en attente]** palettes par valeurs CIE x/y : syntaxe clavier et codes `{CIE X}` /
  `{CIE Y}` à relever au banc.
- Convention de nom des dummies : le tuto utilise le nom de la famille (`Rush2 Zoom`,
  `Lustr3`) ; un show de tournée réel analysé utilise `Reference` pour tous — les deux
  fonctionnent, question de préférence (voir `reference/ASCII_MACRO_SYNTAX.md`,
  phase 10 du journal).

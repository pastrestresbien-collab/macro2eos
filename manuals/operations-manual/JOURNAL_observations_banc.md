# Journal d'observations au banc — manuel d'exploitation (patch, palettes)

Observations testées sur console réelle (confiance S). Ne jamais les insérer dans les
`.md` convertis du manuel (règle de fidélité, voir `CLAUDE.md` Règle n°3).

---

## 2026-09-24 — Palettes By Type et changement de type de fixture (dummy channels)

**Question testée** : un channel dont on change le Type en Patch suit-il automatiquement
le channel par défaut By Type du nouveau type, et retrouve-t-il ses valeurs au retour à
l'ancien type ? Méthode « dummy channels » (forum ETC, confiance B) : un channel sans
adresse par type de fixture, porteur des valeurs par défaut des palettes By Type.

**Cadre** : show vierge, tous les channels sans adresse DMX (aucune sortie vers le kit).

### Phase 1 — Patch (OK)

| Circ | Adresse | Type |
|------|---------|------|
| 1    | —       | Rush Par 2 RGBW Zoom 9ch |
| 2    | —       | Rush Par 2 RGBW Zoom 9ch |
| 9001 | —       | Rush Par 2 RGBW Zoom 9ch |
| 9002 | —       | Robin LEDBeam 350 M1 |

### Phase 2 — Palette By Type avec deux dummies (OK)

- 9001 réglé en rouge (affiché `G L106+`), 9002 en bleu (affiché `G L120+`).
- `[9001] [+] [9002] [Record] [Color Palette] [1] {By Type} [Enter]`
- Liste des palettes couleur : palette 1 avec indicateur `T`, colonne « Par Type de
  circuits » = `9001 9002`, **sans astérisque**.
- **Constat** : un seul Record By Type sur deux channels de types différents fait de
  chacun le channel par défaut de son type (conforme à `10-palettes.md:431`, désormais
  confirmé au banc).

### Phase 3 — Cue référençant la palette (OK)

- `[9001] [+] [9002] [Sneak] [Enter]`, puis `[1] [Thru] [2] [Color Palette] [1] [Enter]` :
  Live affiche `PC 1` (Palette Couleur 1, interface FR) en rouge (= manuel) sur 1 et 2.
- `[Record] [Cue] [1] [Enter]` : ligne de commande « LIVE: Cue 1 : Record Cue 1 ».
- `[Data] [Data]` (« Data Latched ») : 1 et 2 affichent `G L106+` en bleu (= enregistré).
- **Astuce d'observation retenue** : `[Data]` expose la valeur derrière la référence
  (`02-system-basics.md:734-736`) — c'est le moyen de lire la couleur réelle sur des
  channels sans adresse.

### Phase 4 — Channels 1-2 passés en LEDBeam 350 (OK — hypothèse confirmée)

- Patch : softkey « Préserver Natif » = **Désactivé** (vérifié à l'écran).
- `[1] [Thru] [2] {Type}` → `Robin LEDBeam 350 M1` `[Enter]`.
- Live, cue 1 active, Data Latched : 1 et 2 affichent **`G L120+`** en bleu (valeur du
  défaut Beam 9002), au lieu de `L106` (défaut Rush 9001) avant le changement.
- **Constat (S)** : un channel dont on change le Type suit automatiquement le channel par
  défaut By Type du nouveau type, sans aucune retouche de palette ni de cue.
- Note vocabulaire interface FR : softkey Patch « Remplacer » = `{Replace}` (change
  l'adresse DMX seulement, `04-patch.md:156-164`), « Permuter » = `{Swap}`,
  « Dépatcher » = `{Unpatch}`.
- Blind `[Color Palette] [1]` après le changement : 9001 = `G L106+`, 9002 = `G L120+`
  — la palette conserve **les deux** valeurs (une par type) ; 1 et 2 n'y figurent pas
  (aucune donnée propre, ils suivent le défaut de leur type).
- Data déverrouillé : 1 et 2 affichent `PC 1+` en bleu — la référence palette de la cue
  est intacte.

### Phase 5 — Retour Rush Par 2 (OK)

- `[1] [Thru] [2] {Type}` → `Rush Par 2 RGBW Zoom 9ch` `[Enter]`.
- Live, cue 1, Data Latched : 1 et 2 affichent de nouveau **`G L106+`** en bleu.
- **Constat (S)** : aller-retour Rush → Beam → Rush **sans aucune perte**, la cue garde
  sa référence `PC 1` tout du long. Méthode « dummy channel par type comme défaut By
  Type » validée pour les palettes couleur.

### Conclusion opérationnelle (palettes couleur By Type)

1. Un dummy channel **sans adresse** par type de fixture (ici 9001 Rush, 9002 Beam).
2. Chaque dummy est le channel par défaut By Type de son type dans chaque palette.
3. Les vrais channels ne portent **aucune** donnée propre dans les palettes (suivi pur).
4. Changement de salle : `{Type}` en Patch, Préserver Natif désactivé — rien d'autre.

Non couvert par ce test (à tester séparément si besoin) : palettes Focus/Beam, valeurs
**absolues** (hors palette) stockées dans les cues, channels portant des données
**discrètes** dans une palette, gobos.

### Phase 6 — Témoin : bug du défaut qui change de type (forum B)

**Partie A — palette 2 avec un vrai channel comme défaut (OK)**
- Live : `[1] [Thru] [2]` en vert, `[Record] [Color Palette] [2] {By Type} [Enter]`.
- Liste palettes : palette 2 = `T+`, colonne By Type = `1 ( + particulier )`.
  « particulier » = traduction FR de *discrete* dans l'interface.
- Blind tableau : ch 1 en bleu (défaut) R 0.503 / G 100 / B 0 / W 17.128 /
  Color Mix -138.0 Normal ; ch 2 en blanc (discret), valeurs identiques.
- Conforme à `10-palettes.md:431` (canal le plus bas = défaut, les autres discrets).

**Partie B — faire suivre le ch 2 (OK)**
- Softkey `{Cleanup}` (« Nettoyer » en FR) : ligne de commande
  « BLIND: Palette Couleur 2 : Palette Couleur 2 Nettoyer ».
- Résultat : palette 2 = `T` (plus de `+`), By Type = `1`, ch 2 disparaît du tableau
  (suit le défaut).
- **Constat (S)** : `{Cleanup}` convertit en suivi les valeurs discrètes identiques au
  défaut (`10-palettes.md:455`). Plus sûr que `[n] [At] [Enter]` pour préparer un show
  réel : une valeur volontairement différente n'est pas écrasée.

**Partie C — cue 2 référençant la palette 2 (OK)**
- Live : `[1] [Thru] [2] [Color Palette] [2] [Enter]`, `[Record] [Cue] [2] [Enter]`.
- Live tableau, Data Latched : ch 1 et 2 = `G L124` (R/G/B/W) en bleu, Color Mix
  -138.0 Normal. État de référence avant la partie D.

**Partie D — ch 1 (défaut) passé en LEDBeam : bug forum NON reproduit**
- Patch : `[1] {Type}` → `Robin LEDBeam 350 M1` `[Enter]` (Préserver Natif désactivé).
- Live, cue 2, Data Latched :
  - ch 2 (resté Rush) = `G L124` en bleu → **n'a PAS perdu sa couleur**.
  - ch 1 (devenu Beam) = `G L124` en bleu (converti ; Color Priority -4.0 Additive,
    Color Mix 0.0 Normal, Color Temperature 7200 affichés en gris).
- Liste palettes : palette 2 = `T`, colonne By Type = **`2`** (au lieu de `1`).
- **Constat (S)** : sur la version testée, quand le channel par défaut change de type,
  Eos **réassigne automatiquement** le défaut au plus petit channel restant de l'ancien
  type (ici ch 2). Le bug décrit sur le forum (fils anciens, ~2011) ne se reproduit pas
  — le comportement correspond à la demande d'évolution
  « changing a palette's default channel type … should create a new default channel ».
- **Signal D sur la source forum** pour ce point : obsolète sur cette version.
- Live, Data déverrouillé : ch 1 et ch 2 = `PC 2` sur tous les paramètres couleur →
  références de cue intactes.
- Blind palette 2 : ch 2 (Rush) `G L124` en **bleu** (nouveau défaut) ; ch 1 (Beam)
  `G L124` en **blanc** (discret) → Eos a conservé la valeur du ch 1 **en donnée
  discrète, convertie vers le nouveau type**.
- **Piège d'affichage (S)** : la liste des palettes (colonne By Type = `2`, indicateur
  `T` sans `+`) ne signale **pas** cette donnée discrète du ch 1. Seul Blind la révèle.

### Phase 7 — Retour vers l'ancien type SANS dummy (solution 1)

**Partie A — ch 1 : Rush → Beam → Rush, palette 2**
- Patch : `[1] {Type}` → `Rush Par 2 RGBW Zoom 9ch` `[Enter]`.
- Blind palette 2, Data Latched :
  - ch 1 (discret, blanc) : R 0.503 / G 100 / B 0 / W 17.128 / **Color Mix 0**
  - ch 2 (défaut, bleu)   : R 0.503 / G 100 / B 0 / W 17.128 / Color Mix -138.0 Normal
- Référence d'origine du ch 1 (phase 6 A) : Color Mix **-138.0 Normal**.
- **Constat (S)** : RGBW revenu à l'identique ; **Color Mix perdu** (repris de la valeur
  Beam `0.0 Normal` au lieu de la valeur Rush d'origine). Le ch 1 reste discret.
- Liste palettes : palette 2 = `T+`, By Type = `2 ( + particulier )` → ici la donnée
  discrète est bien signalée (même type que le défaut), contrairement à la phase 6 D
  (discret d'un autre type, non signalé).
- Impact réel du Color Mix 0 sur la sortie du Rush : **non vérifié** (pas de sortie DMX
  dans ce test).
- `{Cleanup}` sur la palette 2 ensuite : R/G/B/W du ch 1 passent en **magenta** (suivi),
  **seul Color Mix `0` reste blanc** (discret). Liste inchangée : `T+`, `2 ( + particulier )`.
- **Constat (S)** : `{Cleanup}` opère **paramètre par paramètre**. Après un retour à
  l'ancien type, `{Cleanup}` puis lecture en Blind = **détecteur de dérive** : tout ce
  qui reste en blanc a changé pendant l'aller-retour.

**Partie B1 — palette 3 de référence (ch 1 et 2 en Rush, orange)**
- `[Record] [Color Palette] [3] {By Type} [Enter]` puis `{Cleanup}` en Blind.
- Blind palette 3, Data Latched, après Cleanup :
  - ch 1 (défaut, bleu) : R 100 / G 61.103 / B 0 / W 29.91 / Color Mix **0**
  - ch 2 : R/G/B/W en magenta (suivi) ; Color Mix **-138.0 Normal** en blanc (discret)
- Liste : palette 3 = `T+`, By Type = `1 ( + particulier )`.
- **Constat (S)** : le Color Mix `0` du ch 1 est la dérive de la partie A restée dans le
  Live → **une dérive non corrigée contamine les enregistrements suivants**.

**Partie B2 — aller : ch 1 et 2 en LEDBeam**
- Patch : `[1] [Thru] [2] {Type}` → `Robin LEDBeam 350 M1` `[Enter]`.
- Liste palettes : palettes 2 et 3 = `T`, By Type = **`9001`** (au lieu de `2` et `1`).
- **Constat (S)** : quand plus aucun channel « réel » de l'ancien type ne reste, Eos
  réassigne le défaut au **seul channel restant de ce type, même un dummy sans adresse
  de numéro élevé** (9001, présent depuis la phase 1, n'avait jamais été défaut des
  palettes 2 et 3).
- ⚠ Le test n'est donc plus « sans dummy » : 9001 a servi de réservoir automatique.
- Piste ouverte : un simple dummy sans adresse par type, **sans aucune préparation des
  palettes**, suffirait-il pour qu'Eos y range lui-même les défauts ? (à valider en B3)
- Blind palette 3, Data Latched, après l'aller :
  - 9001 (Rush, défaut, bleu) : R 100 / G 61.103 / B 0 / W 29.91 / Color Mix 0
  - ch 1 (Beam, discret, blanc) : R 100 / G 61.103 / B 0 / W 29.91 / Color Mix 0.0 Normal
  - ch 2 (Beam) : **R/G/B/W VIDES** ; Color Mix 0.0 Normal (blanc)
- **Constat (S) — CRITIQUE** : quand **tous** les channels d'un type changent de type
  sans défaut préparé pour le nouveau type, **seul l'ancien défaut garde ses valeurs**
  (converties en discret). **Les channels qui suivaient le défaut perdent leurs
  données** (ici ch 2 perd son orange). C'est le bug décrit sur le forum, qui se
  manifeste dans ce cas précis (et pas dans celui de la phase 6 D, où un channel de
  l'ancien type restait).
- Valeur discrète du ch 2 Color Mix -138.0 Normal → 0.0 Normal (convertie/perdue).
- **Conséquence** : la « solution 1 » (changer le type sans rien préparer) est
  **à proscrire** pour un show avec palettes By Type. Un défaut préparé pour le
  **nouveau** type (dummy, phases 1-5) est nécessaire.

**Partie B3 — retour : ch 1 et 2 en Rush**
- Patch : `[1] [Thru] [2] {Type}` → `Rush Par 2 RGBW Zoom 9ch` `[Enter]`.
- Blind palette 3 (affichage gel, sans Data Latched) :
  - 9001 (défaut, bleu) : `G L147` ×4, Color Mix 0
  - ch 1 (blanc, discret) : `G L147` ×4, Color Mix 0
  - ch 2 : `G L147` ×4 en **magenta (suivi de 9001)**, Color Mix 0 en blanc
- Liste : palettes 2 et 3 = `T+`, By Type = `9001 ( + particulier )`.
- **Constat (S)** : au retour, les channels qui avaient perdu leurs données pendant
  l'aller **les retrouvent** en suivant le défaut que le dummy de l'ancien type a
  conservé (9001). Le ch 1 (ancien défaut, discret) a des valeurs identiques à 9001.
- Dérive restante : Color Mix du ch 2, -138.0 Normal → 0.

### Synthèse phase 7

| Élément | Rôle | Préparation nécessaire |
|---|---|---|
| Dummy de l'**ancien** type (ex. 9001 Rush) | Eos y range **automatiquement** les défauts quand plus aucun vrai channel de ce type ne reste → retour sans perte des couleurs | **Aucune** : il suffit qu'il existe dans le patch (sans adresse) |
| Dummy du **nouveau** type (ex. 9002 Beam) | Donne des valeurs aux channels convertis pendant le séjour dans la salle | Valeurs à mettre dans chaque palette (phases 1-5) |
| `{Cleanup}` après le retour | Remet en suivi ce qui est identique, laisse en blanc ce qui a dérivé | Aucune |

Non testé : ce que deviennent les défauts si **aucun** channel de l'ancien type ne reste
dans le show (ni réel, ni dummy).

### Phase 8 — Changement de type SANS aucun channel de l'ancien type restant

**Cadre** : show vierge, **aucun dummy**, ch 1-3 en `Rush Par 2 RGBW Zoom 9ch`, sans
adresse, Préserver Natif désactivé (ch 2-3 patchés par `Copy To` depuis ch 1).

**Phases 0-2 — référence (OK)**
- Orange, `[Record] [Color Palette] [1] {By Type} [Enter]`, puis `{Cleanup}` en Blind.
- Liste palettes : palette 1 = `T`, By Type = `1`.
- Blind palette 1 : seul ch 1 affiché, `G L147` (R/G/B/W) + Color Mix `Normal`, en bleu ;
  ch 2-3 absents (suivi pur).
- Cue 1 : ch 1-3 = `PC 1` sur tous les paramètres couleur ; Beam : Zoom 10,
  Shutter Strobe 255, Strobe Mode Open.

**Phase 3 — tout passe en LEDBeam, aucun Rush restant**
- Patch : `[1] [Thru] [3] {Type}` → `Robin LEDBeam 350 M1` `[Enter]`.
- Liste palettes : palette 1 = `T`, By Type = **`1`** (inchangé).
- Blind palette 1 : ch 1 (**Beam**) `G L147` ×4 + Color Mix `Normal`, **en bleu
  (défaut)** ; ch 2-3 absents (suivi).
- Live cue 1 (Data déverrouillé) : ch 1-3 = `PC 1` ; Color Priority « Addition… » et
  Color Temperature 7200 en gris (paramètres propres au Beam, non stockés).
- **Constat (S)** : s'il ne reste **aucun** channel de l'ancien type, le défaut
  **change de type avec son channel** et les autres (même nouveau type) continuent de
  le suivre → **aucune perte**.
- **Paradoxe avec la phase 7 B2** : c'est l'existence du dummy Rush 9001 qui a capté le
  défaut Rush, laissant le ch 1 en discret et le ch 2 (Beam) sans rien à suivre → perte.
  **Un dummy de l'ancien type provoque la perte pendant le séjour** dans le nouveau type.
- Live cue 1, Data Latched : ch 1-3 = `G L147` ×4 en bleu, Color Mix `0.0 Normal`,
  Color Priority `-4.0 Additive` et Color Temperature 7200 en gris → **les trois
  channels ont gardé la couleur**.

**Phase 4 — retour : ch 1-3 en Rush**
- Patch : `[1] [Thru] [3] {Type}` → `Rush Par 2 RGBW Zoom 9ch` `[Enter]`.
- Blind palette 1, Data Latched : ch 1 (défaut, bleu) R 100 / G 61.103 / B 0 /
  W 29.91 / Color Mix **0** ; ch 2-3 absents (suivi). Liste : `T`, By Type = `1`, pas
  de `+`.
- Live cue 1 : ch 1-3 = `PC 1`. **Aucun `{Cleanup}` nécessaire** (aucun discret).
- **Constat (S)** : sans aucun channel de l'ancien type restant, l'aller-retour complet
  se fait **sans perte de couleur ni de référence**.
- **Dérive probable du Color Mix** : référence phase 2 affichée `Normal` (hors Data
  Latched ; en phase 7 cet affichage correspondait à `-138.0 Normal`), retour = `0`.
  **Non détectable par `{Cleanup}`** ici, car c'est le **défaut lui-même** qui a dérivé
  (aucune valeur de comparaison).

### Explication de la dérive Color Mix (export ASCII utilisateur, Eos 3.3.9)

Table de plages du profil `Martin Rush_Par_2_RGBW_Zoom_9ch` (`$Personality 65241`,
paramètre 208 Color_Mix) : `-138.0` = **Normal** (DMX 0-10) ; -137…-102 = Color 1…36 ;
**-100…100 = « Cycle -100 to 100% »** (DMX 193-243). La valeur `0` revenue après
l'aller-retour sans dummy place donc le Rush en **mode cycle couleur** : dérive **réelle
en sortie**, pas seulement d'affichage.
Idem Lustr X8 Direct (`$Personality 25798`, paramètre 17 Cooling_Fan) : `-2.0` = Auto
(DMX 0-9), `0…100` = vitesse (DMX 20-249) → une dérive vers 0 = ventilation à vitesse 0.
→ Justifie la méthode « défauts miroirs » (maître jamais converti).

### Règle déduite des phases 6-8 (S)

La perte ne survient que dans un cas : **un channel qui suivait le défaut change de
type, alors que le défaut reste sur un channel de l'ancien type** (réel ou dummy). Il se
retrouve alors dans un type sans défaut → données vides.

| Situation | Résultat |
|---|---|
| Tous les channels d'un type changent ensemble, aucun autre channel de ce type dans le show | **Aucune perte** (phase 8) |
| Seul le défaut change, d'autres channels de l'ancien type restent | Aucune perte : défaut réassigné, ancien défaut gardé en discret converti (phase 6 D) |
| Défaut + channels suiveurs changent, mais un channel de l'ancien type reste (ex. dummy) | **Perte pour les suiveurs** pendant le séjour (phase 7 B2), récupérée au retour (7 B3) |

**Conséquence pratique** : ne **pas** garder de dummy de l'ancien type ; convertir
**tous** les channels d'un type en une seule commande `{Type}`. Paramètres propres à un
type (ex. Color Mix du Rush) : dérive possible, à vérifier à la main.

### Macro de patch — softkey `{Type}` en macro (ÉCHEC)

- Macro 901 (Foreground, lancée depuis Patch) :
  `Wait_For_Input  Type  Wait_For_Input  Select_Last  Label`
- **Constat (S)** : la macro **bloque à l'étape `Type`** — le softkey `{Type}` du Patch
  n'est pas exécutable depuis une macro (au moins sous cette forme).
- Contournement proposé : retirer `Type` de la macro, l'utilisateur appuie lui-même sur
  `{Type}` pendant la première pause (`Wait_For_Input`). À valider.
- **Abandonné** par l'utilisateur : la version sans `Type` n'apporte rien.

### Patch multi-channels en une commande (OK)

- `[201] [+] [202] [+] [2001] {Type}` → ligne de commande
  « Circ 201 + 202 + 2001 Type Martin Rush Par 2 RGBW Zoom 9ch ♦ ».
- **Constat (S)** : une sélection en liste (`+`) accepte `{Type}` en une seule commande —
  plus simple que `Copy To` pour patcher plusieurs channels (réels + dummy) du même type.
  Nom exact dans la librairie : « Martin Rush Par 2 RGBW Zoom 9ch ».

### Phase 9 — Validation « défauts miroirs » (deux familles)

**V1 — patch (OK)** : show vierge, Préserver Natif désactivé, tout **sans adresse**.

| Circ | Type (nom Eos) | Label |
|------|----------------|-------|
| 201, 202 | Rush Par 2 RGBW Zoom 9ch | — |
| 301, 302 | S4 LED S3 Lustr X8 Direct | — |
| 2001 | Rush Par 2 RGBW Zoom 9ch (maître) | Rush2 Zoom |
| 2002 | Robin LEDBeam 350 M1 (équivalent) | Rush2 Zoom |
| 3001 | S4 LED S3 Lustr X8 Direct (maître) | Lustr3 |
| 3002 | Sully 653SX 4C Full XY (équivalent) | Lustr3 |

Groupe 1 = `201>202 301>302 2001>2002 3001>3002`, affichage filtré « Circuits
Sélectionnés ».

**V2a — palettes « show existant » (OK)** : `[201] [+] [202] [+] [301] [+] [302]`,
Record `{By Type}`, puis `{Cleanup}`. Liste : palettes 1 et 2 = `T`, By Type =
`201 301`, pas de `+`.

Références (Blind, Data Latched) :

| Palette | Ch | Valeurs |
|---------|----|---------|
| 1 orange | 201 | R 100 / G 36.13 / B 0 / W 0.621 / Color Mix -138.0 Normal |
| 1 orange | 301 | Red 100 / Amber 100 / Lime 25.494 / Green 0 / Blue 0 / Indigo 5.053 / Cyan 0 / Deep Red 100 / Cooling Fan -2.0 Auto |
| 2 bleu | 201 | R 11.649 / G 0 / B 100 / W 19.34 / Color Mix -138.0 Normal |
| 2 bleu | 301 | Red 0 / Amber 0 / Lime 0 / Green 0 / Blue 87.407 / Indigo 100 / Cyan 0 / Deep Red 72.92 / Cooling Fan -2.0 Auto |

**Constat (S) — méthode d'observation** : hors Data Latched, le tableau Blind **arrondit**
les valeurs (11 / 19 / 87 / 72 affichés pour 11.649 / 19.34 / 87.407 / 72.92) et montre
le nom de plage au lieu du nombre (`Normal` pour -138.0). Toute mesure de dérive doit se
faire en **Data Latched**.

**V2b — cues** : cue 1 = palette 1 (201, 202, 301, 302), cue 2 = palette 2, cue 3 =
témoin **hors palette** sur 202 et 302.
- Cue 3, 1er enregistrement (Data Latched) : 202 = R/G/B/W 100, Color Mix -138.0 Normal ;
  302 = les 8 émetteurs à 100, pas de Cooling Fan stockée. Valeurs extrêmes (blanc
  plein) → peu sensibles à une dérive ; ré-enregistrement avec une couleur
  intermédiaire conseillé.
- **Cue 3 ré-enregistrée (vert intermédiaire) — référence retenue** (Live, Data Latched) :
  - 202 : R 0 / G 100 / B 0.017 / W 7.622 / Color Mix -138.0 Normal
  - 302 : Red 0 / Amber 0 / Lime 1.619 / Green 100 / Blue 0 / Indigo 0 / Cyan 19.749 /
    Deep Red 0

**V3 (T1) — Copy To vers les dummies** (Blind, palettes 1 Thru 2 sélectionnées) :
`[201] [Copy To] [2001]`, `[301] [Copy To] [3001]`, `[2001] [Copy To] [2002]`,
`[3001] [Copy To] [3002]`. Lecture palette 1 (Data Latched) :
- 2001 (Rush) : 100 / 36.13 / 0 / 0.621 / -138.0 en **magenta** → copie vers un channel
  de **même type** = channel en **suivi** du défaut 201 (pas de donnée propre).
- 3001 (Lustr 3) : valeurs de 301 en **magenta** → idem, suivi de 301.
- 2002 (Beam 350) : R 100 / G 36.13 / B 0 / W 0.621 en **blanc** (discret), Color Mix
  0.0 Normal → paramètres homonymes (R/G/B/W) copiés **tels quels, sans conversion
  colorimétrique** ; Color Mix -138.0 → 0.0 Normal.
- 3002 (Sully Full XY) : CIE X 0.576 / CIE Y 0.388 en blanc → **conversion réelle** vers
  l'espace xy (paramètres différents).
- Liste : By Type toujours `201 301` (normal, étape `{By Type}` pas encore faite).
- **Constat (S)** : `Copy To` entre types différents copie les paramètres de même nom
  à l'identique et ne convertit que lorsque les paramètres diffèrent.
- Palette 2 : 2001 et 3001 en magenta (suivi) ; 2002 blanc 11.649 / 0 / 100 / 19.34,
  Color Mix 0.0 Normal ; 3002 blanc CIE X 0.186 / Y 0.056.
- **Constat (S)** : `Copy To` en Blind avec `[Color Palette] [1] [Thru] [2]` sélectionnées
  agit sur **toutes les palettes sélectionnées** en une commande.

**V4 — dummies désignés défauts (OK)** : palettes 1 Thru 2 sélectionnées,
`[2001] [+] [2002] [+] [3001] [+] [3002] {By Type} [Enter]`, puis
`[Color Palette] [1] [Thru] [2] {Cleanup} [Enter]`.
- Liste : palettes 1 et 2 = `T`, By Type = **`2001 2002 3001 3002`**, pas de `+`.
- Palette 1 : 2001 / 2002 / 3001 / 3002 en bleu (défauts) ; 201 / 202 / 301 / 302 en
  magenta (suivi), valeurs inchangées.
- **Constat (S)** : `{By Type}` sur une liste de channels + `{Cleanup}` sur une plage de
  palettes = conversion d'un show existant en « défauts miroirs » en **deux commandes**.

(Entre V4 et V5 : positions Augment3d attribuées aux 8 channels — rangée haute réels,
rangée basse dummies — pour contrôle visuel.)

**V5 (T2) — aller : 201-202 → LEDBeam 350 M1, 301-302 → Sully 653SX 4C Full XY (OK)**
- Liste palettes : 1 et 2 = `T`, By Type `2001 2002 3001 3002`, **pas de `+`**.
- Live cue 1, Data Latched :
  - 201, 202 : R 100 / G 36.13 / B 0 / W 0.621 / Color Mix 0.0 Normal (bleu) = valeurs
    de 2002 ; Color Priority -4.0 Additive et Color Temperature 7200 en gris (non
    stockés).
  - 301, 302 : CIE X 0.576 / CIE Y 0.388 (bleu) = valeurs de 3002 ; autres paramètres
    Sully en gris (Saturation 100, Color Mix Mode 0.0 Direct, Color Temperature 1700,
    Tint 0, Intens 2 100).
- **Constat (S)** : à l'aller, tous les channels convertis suivent le dummy de leur
  nouveau type, **aucune donnée discrète créée**.
- Cue 3 (témoin hors palette), Live Data Latched après conversion :
  - 202 (Beam 350) : R 56.34 / G 64.0156 / B 0.0074 / W 3.6776 / Color Mix 0.0 Normal
    (réf. Rush : R 0 / G 100 / B 0.017 / W 7.622) → **conversion colorimétrique** (pas une
    copie brute comme `Copy To`), résultat visiblement jaune-vert.
  - 302 (Sully) : CIE X 0.6956 / CIE Y 0.5897 → **x + y = 1.285 > 1**, coordonnées
    chromatiques **impossibles** : conversion douteuse (bug ou échelle propre au profil).
  - **Constat (S)** : les valeurs **hors palette** sont converties à chaque changement de
    type, avec un résultat discutable → confirme la règle « couleur via palette ».

(Intensités de 201-302 montées à 80 % pour la visualisation Augment3d.)

**V6 (T3) — retouche en salle par Update By Type (en cours)**
- Live cue 1 : 201 Green 36.13 → 20 (encodeur).
- Fenêtre Update : Target « Palette Couleur 1 », Circuits « 201 » ; style « Seulement
  les Ref » ; modificateurs « Dernière Ref » et « Casser Liens » surlignés. Ligne de
  commande : « Update Seulement les Ref Par Type ♦ ». Aucun défaut entre crochets affiché.
- Après exécution, Live : 201 reste **en rouge (manuel)** R 100 / G 20 / B 0 / W 0.621 ;
  202 (même type, suit le défaut) reste G **36.13** en bleu → **le défaut 2002 ne semble
  pas avoir été mis à jour**. À confirmer en Blind palette 1.
- **Blind palette 1 (Data Latched) : la mise à jour A FONCTIONNÉ.**
  - 2002 (défaut Beam 350, bleu) : R 100 / **G 20** / B 0 / W 0.621 / Color Mix 0.0 Normal.
  - 201, 202 : **magenta** (suivi), G 20 → aucune donnée discrète créée.
  - 2001 (maître Rush) : **inchangé** R 100 / G 36.13 / B 0 / W 0.621 / -138.0 Normal.
  - 3001, 3002, 301, 302 : inchangés. Liste : `T`, `2001 2002 3001 3002`, pas de `+`.
- **Constat (S)** : `Update … {By Type}` sur un channel suiveur écrit la valeur dans le
  **défaut de son type actuel** (le dummy équivalent), sans toucher au maître, sans créer
  de discret — **même sans afficher de crochets** dans la fenêtre Update.
- **Piège d'affichage (S)** : juste après l'Update, le Live **n'est pas rafraîchi**
  (201 reste en rouge manuel, 202 affiche encore l'ancienne valeur). Ne pas juger le
  résultat d'un Update depuis le Live sans rafraîchir (Go To Cue) ou vérifier en Blind.
- Après `[Go To Cue] [1]` : Live 201 et 202 = R 100 / **G 20** / B 0 / W 0.621 en bleu
  → la retouche est bien effective en sortie une fois le Live rafraîchi.

**V7 (T4/T5) — retour : 201-202 → Rush Par 2, 301-302 → S4 LED S3 Lustr X8 Direct**
- Liste palettes : 1 et 2 = `T`, `2001 2002 3001 3002`, **pas de `+`**.
- Live cue 1 (Data Latched) :
  - 201, 202 : R 100 / G 36.13 / B 0 / W 0.621 / **Color Mix -138.0 Normal** →
    **identique à la référence** (la retouche G 20 faite sur le Beam 350 n'a pas touché le
    maître Rush).
  - 301, 302 : Red 100 / Amber 100 / Lime 25.494 / Green 0 / Blue 0 / Indigo 5.053 /
    Cyan 0 / Deep Red 100 → **identique à la référence**. Cooling Fan non affichée dans
    ce tableau Live ; 301-302 suivent 3001 (jamais converti, -2.0 Auto en Blind).
- Live cue 3 (témoin **hors palette**) :
  - 202 : R 0 / G 100 / B 0.017 / W 7.622 (identiques) mais **Color Mix 0** au lieu de
    -138.0 Normal → **dérive**.
  - 302 : Red 0 / **Amber 100 / Lime 11.162** / Green 0 / Blue 0 / Indigo 0 / Cyan 0 /
    Deep Red 0 au lieu de Lime 1.619 / Green 100 / Cyan 19.749 → **couleur totalement
    différente** (vert devenu ambre).

**Conclusion phase 9 (S)** :
1. Méthode « défauts miroirs » **validée** : aller-retour **exact** pour toutes les
   valeurs de palettes (Color Mix et paramètres Lustr compris), retouche en salle sans
   effet sur le maître, aucun discret créé.
2. Préparation d'un show existant : `Copy To` (réel → maître, maître → équivalents) +
   `{By Type}` sur la liste des dummies + `{Cleanup}` sur la plage de palettes, toutes
   palettes sélectionnées en Blind.
3. Les valeurs **hors palette** ne survivent **pas** à l'aller-retour → règle
   obligatoire : **en cue, la couleur passe toujours par une palette**.

Note : la palette couleur de la Lustr stocke aussi **Cooling Fan** (paramètre non
couleur) — candidat à la dérive, comme le Color Mix du Rush.

**Version testée** : Eos 3.3.9 Build 25, librairie fixtures 3.3.9.2, PC en mode Offline
(nom d'appareil PCFIXE).

**Bilan phase 6** : sur 3.3.9, changer le type du channel par défaut d'une palette By
Type ne fait **rien perdre** : défaut réassigné au plus petit channel restant de
l'ancien type, valeur du channel changé gardée en discret (convertie). Les dummies
restent utiles pour avoir une valeur **réglée par type** (au lieu d'une conversion
automatique) et pour que les vrais channels restent en suivi pur (pas de discrets qui
s'accumulent).

### Phase 10 — Analyse externe : export ASCII réel d'une tournée (busking)

Pas un test au banc : analyse d'un fichier fourni par l'utilisateur,
`Eos_Family_Busking_Rev_B.asc` (Eos 3.3.9, show de tournée réel, hors du banc de
transport). Objectif : confronter la méthode « défauts miroirs » à un usage en
production, et comprendre la syntaxe des macros dans un export ASCII.

**Patch — le motif dummy existe déjà en production**, sous une forme voisine de la
méthode du tuto :
- Channels 9000-9032 patchés **sans adresse** (`$Patch <circ> <persID> 0 1 1`), un par
  modèle (SolaFrame Theatre, SolaFrame 750, SolaWash 2000…), labellisés `Reference`
  (au lieu du nom de famille comme dans le tuto — convention de nommage différente,
  même principe).
- Ces channels de référence sont **inclus** dans le groupe utilitaire `Highlight`
  (9997) aux côtés des vrais circuits — confirme qu'un dummy sans adresse n'a pas
  besoin d'être exclu des groupes généraux, seulement des palettes tant qu'il n'est pas
  désigné défaut.
- Champ ASCII correspondant à la colonne « Par Type » de la liste des palettes :
  `$$TypeChanList` (liste des circuits désignés défauts pour cette palette, distincte
  des lignes `$$Param` qui portent les valeurs de circuits normaux).

**Macros — deux `{Type}` différents, un seul bloque en macro** : ce show réel contient
deux macros (8031 « New Color BT », 8032 « Upd Color BT ») qui exécutent
`Record`/`Update Palette_Couleur Par_Type` — c'est-à-dire le softkey **`{By Type}` d'un
Record/Update de palette**, avec succès (le fichier vient d'un show utilisé en
tournée). Confronté au constat de la phase 9 (« Macro de patch — softkey `{Type}` en
macro — ÉCHEC ») : ce n'est **pas le même softkey**. Celui du **Patch** (assigner un
modèle à un channel) bloque en macro ; celui d'un **Record/Update de palette**
(désigner un circuit comme défaut de type) ne bloque pas. Détail de la syntaxe ASCII
des macros (`$MacroDef`, `$$MacroContents`, `$$MacroCommands`) et dictionnaire de codes
déduit par alignement : `reference/ASCII_MACRO_SYNTAX.md`.

**Conséquence pour le tuto** : la limite « Macro de préparation : `{By Type}` /
`{Cleanup}` en macro non validés » (tuto §B) était trop pessimiste — seul le `{Type}`
du Patch est confirmé bloqué ; le `{By Type}` d'un Record/Update de palette a un
exemple qui fonctionne ailleurs. Deux gabarits de macro à tester au banc (préparation
§B, retouche en salle §E.4) proposés dans `reference/ASCII_MACRO_SYNTAX.md`, marqués
**[non testé]** jusqu'à validation sur notre propre console.

### Phase 11 — Gélatine en ligne de commande : `[circ] @ <livre>/<gel>` (OK)

- Commande tapée : `[301] [At] [3] [/] [1] [0] [6] [Enter]` → ligne de commande
  « LIVE: Cue 1 : Circ 301 @ 3 / 106 ♦ ».
- `3` = numéro du livre de gélatines tel qu'affiché sur le softkey du Gel Picker
  (« 3 Lee » ; autres livres vus : 1 Apollo Gel, 2 GAM GamColor, 4 Rosco Other,
  5 Rosco Roscolux, 6 Rosco SuperGel, 7 Rosco E Color, 8 TokyoBS Poly Color, 9 Lee CL).
- Résultat (Live, Data Latched, 301 = S4 LED S3 Lustr X8 Direct) : Red 100 / Amber
  18.95 / Lime 0 / Green 0 / Blue 0 / Indigo 0 / Cyan 0 / Deep Red 95.795 ; picker CIE
  x 0.6872 / y 0.3092 = Lee 106 (Primary Red).
- **Constat (S)** : un gel se choisit **au clavier**, sans toucher la tuile du picker.
  Syntaxe non trouvée dans le manuel converti (`06-manual-control.md` ne documente que
  `{Scroller}` pour les changeurs mécaniques). Conséquence : une macro de création de
  palettes par gel peut s'écrire entièrement en ASCII (`@` = code 10, `/` = code 57,
  cf. `reference/ASCII_MACRO_SYNTAX.md`), sans passer par `[Learn]`.
- Mode de conversion (Brightest / Spectral / Hybrid) appliqué par cette commande :
  **non vérifié**.
- Complément lecture de la capture (show « test copie tour claude code », Offline) :
  - Le numéro de livre est un **identifiant fixe**, pas la position à l'écran : ordre
    affiché 3 Lee, 5, 6, 7, 4, 2, 1, 8, 9, Standard Colors. Une macro peut donc s'y fier.
  - Mode de correspondance affiché dans le picker : **`+Lumineux`** (= {Brightest}).
    Que la commande `@ 3/106` suive ce réglage reste **à vérifier** (changer le mode puis
    retaper la commande, comparer les valeurs).
  - Valeurs en rouge (« Circuits Manuels ») : la commande crée des valeurs **manuelles**
    en Live, prêtes pour un Record. Intensité non touchée (vide).
  - Seul 301 était sélectionné (filtre « Circuits Sélectionnés ») : test fait sur un
    circuit réel, **pas encore sur un dummy ni sur une sélection multi-types**.
  - Traduction FR du Gel Picker : `{Show}` = « Conduite », `{Sort Hue}` = « Trier Hue »,
    `{Similar}` = « Similaire », `{Brightest}` = « +Lumineux ».

### Phase 12 — Import ASCII d'une macro écrite à la main (OK)

- Fichier `macros/920_palettes_lee_11-16.asc` : en-tête minimal (`Ident`, `Manufacturer`,
  `Console`, `$$Format`, `$$Software Version`), **sans `Clear All`**, un seul `$MacroDef`,
  `EndData`. Latin-1, CRLF. Import dans un show sans titre (« (sanstitre)* »), écran Blind.
- **Constat (S)** : la console accepte un ASCII partiel ne contenant qu'une macro.
  Macro éditeur : 920, Label « Palettes Lee 11-16 », Color « Blanc », Mode vide,
  Appareil ciblé vide, SC Learn vide.
- Contenu affiché : `2 0 0 1 Jusqu'à 3 9 9 9 ♦ Color Home ♦ Record Palette_Couleur 1 1
  Par_Type ♦ @ 3 / 2 0 5 ♦ Record Palette_Couleur 1 2 Par_Type ♦ @ 3 / 2 0 1 ♦ …`
  → chaque `<Enter>` devient `♦`, l'accent de « Jusqu'à » passe correctement (Latin-1).
- `$$MacroMode` absent → colonne Mode **vide** (mode par défaut, nature à préciser).
- Reste à vérifier : exécution réelle (lequel de `$$MacroContents` / `$$MacroCommands`
  pilote), comportement de `@` en début de ligne après un Record.

### Phase 13 — Exécution de la macro 920 (palettes Lee 11-16 By Type) — partiel OK

- Macro lancée en Live dans « test copie tour claude code ». Contrôle fait par
  l'utilisateur : `Groupe 2 Palette Couleur 15 ♦` (groupe 2 = `201>202 301>302`, vrais
  projecteurs, en type kit : Rush Par 2 et Lustr X8 Direct).
- **Constat (S)** : la palette 15 existe et s'applique aux **deux types** : Augment3d
  montre 201/202 (faisceaux) et 301/302 (disques) en **vert foncé** = Lee 124 (Dark
  Green) → la macro a exécuté au moins jusqu'à `@ 3/124` + `Record Palette_Couleur 15
  Par_Type`, et les vrais projecteurs suivent bien leur dummy de type.
  - Donc confirmé : un import ASCII écrit à la main **s'exécute** ; `@` en début de
    ligne après un Record s'applique à la **sélection restée active**.
- Affichage Live (Data Latched, en rouge = manuel) : toutes les cases couleur montrent
  **`G L124`** (et non une référence de palette type `CP 15`) ; Color Mix Rush reste
  `-138.0 Normal` (hors gel). Encodeurs sur la Lustr : Red 0.503 / Amber 0 / Lime 6.812 /
  Green 100. Signification exacte de `G L124` (référence gel stockée dans la palette ?)
  **à éclaircir** (Blind palette 15, Data Latched).
- Intensités 201-302 à 80 (manuel, pour la visualisation).
- **Non encore vérifié** : liste des palettes (11-16 toutes présentes, `T`, By Type =
  `2001 2002 3001 3002`, pas de `+`) ; palettes 11-14 et 16 ; valeurs des dummies
  2002 (LEDBeam) et 3002 (Sully).
- **Liste des palettes (onglet 24)** après la macro :

  | Palette | `T` | Par Type de circuits |
  |---|---|---|
  | 1, 2 (phase 9) | oui | 2001 2002 3001 3002 |
  | **11 (Home)** | **non** | **vide** |
  | 12, 13, 14, 15, 16 | oui | 2001 2002 3001 3002 |

  Label, Icône, Absolu, Verrouillé vides partout, aucun `+`.
- **Constat (S)** : les 5 palettes créées par `@ 3/<gel>` + `Record … Par_Type` sont
  correctes ; la palette 11, créée après `Color Home`, **existe mais n'est pas By Type**.
  Cause **non établie** (palette vide ? données discrètes ?) → Blind palette 11 à lire.
- **Blind palette 15, Data Latched** (filtre Circuits Sélectionnés, dummies non
  affichés) — vrais projecteurs en **magenta** (suivi du défaut, aucun discret) :
  - 201, 202 (Rush) : R 0.503 / G 100 / B 0 / W 17.128 / Color Mix -138.0 Normal
  - 301, 302 (Lustr) : Red 0 / Amber 0 / Lime 6.812 / Green 100 / Blue 0 / Indigo 0 /
    Cyan 43.218 / Deep Red 0 / Cooling Fan -2.0 Auto
  - En Blind Data Latched, valeurs **numériques** : le `G L124` vu en Live est un
    affichage, la palette stocke des nombres.
- Reste : valeurs des dummies 2002 (LEDBeam) et 3002 (Sully) ; contenu de la palette 11.

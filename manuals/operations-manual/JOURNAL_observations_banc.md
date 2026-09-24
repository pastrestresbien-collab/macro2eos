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
| 2 bleu | 201 | R 11 / G 0 / B 100 / W 19 / Color Mix `Normal` (valeur numérique non relevée) |
| 2 bleu | 301 | Red 0 / Amber 0 / Lime 0 / Green 0 / Blue 87 / Indigo 100 / Cyan 0 / Deep Red 72 / Cooling Fan `Auto` (valeur numérique non relevée) |

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

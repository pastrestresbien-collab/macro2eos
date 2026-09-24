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

**Version testée** : Eos 3.3.9 Build 25, librairie fixtures 3.3.9.2, PC en mode Offline
(nom d'appareil PCFIXE).

**Bilan phase 6** : sur 3.3.9, changer le type du channel par défaut d'une palette By
Type ne fait **rien perdre** : défaut réassigné au plus petit channel restant de
l'ancien type, valeur du channel changé gardée en discret (convertie). Les dummies
restent utiles pour avoir une valeur **réglée par type** (au lieu d'une conversion
automatique) et pour que les vrais channels restent en suivi pur (pas de discrets qui
s'accumulent).

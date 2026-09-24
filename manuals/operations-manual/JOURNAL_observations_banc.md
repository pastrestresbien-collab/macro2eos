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
- Reste à voir : affichage de la référence (`PC 1`) avec Data déverrouillé.

### Phase 5 — Retour Rush Par 2

_(en cours)_

### Phase 6 — Témoin : bug du défaut qui change de type (forum B)

_(en cours)_

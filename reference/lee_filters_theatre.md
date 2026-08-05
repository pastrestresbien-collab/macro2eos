# Lee Filters — table de référence théâtre (partielle)

- Accès réseau : seul `WebSearch` fonctionne dans cet environnement (extraits de
  résultats). `WebFetch` est bloqué (403) sur tous les domaines testés — leefilters.com,
  Rosco, thomannmusic.com, lightspares.com, et même Wikipedia (voir `CLAUDE.md` règle n°1,
  reconfirmé le 2026-08-03). **Ce n'est donc pas une conversion intégrale du catalogue
  Lee** (qui en compte plusieurs centaines de teintes) : c'est le sous-ensemble qu'on a pu
  retrouver et vérifier par recherche, entrée par entrée.
- Deux niveaux de confiance, distincts de l'échelle S/A/B/C/D du reste du projet
  (celle-ci mesure la fiabilité d'une commande console, pas l'existence d'une teinte) :
  - **✅ confirmé** — une page produit Lee identifiable et distincte a été vue pour ce
    numéro précis (titre de page ou URL citant le numéro).
  - **〰️ probable** — le nom apparaît dans un texte de synthèse de recherche, cohérent
    d'une recherche à l'autre, mais sans page produit individuelle repérée. À vérifier
    avant un usage critique.
- **Colonne « Description »** : ajoutée pour permettre une interprétation autonome
  (choisir la bonne teinte sans redemander à l'utilisateur à chaque fois). Remplie
  seulement quand une source la donnait vraiment — jamais déduite du nom seul. Une
  case vide reste vide plutôt que d'inventer un effet plausible.

## Syntaxe console (rappel, confirmé A — voir `grammar/modele.yaml`)

- Ligne de commande : `Color <bibliothèque>/<numéro>`. Lee = bibliothèque **3**.
  Exemple : `Chan 4 Color 3/195 Enter` (manuel §10, corpus #082).
- OSC direct : chaîne `L<numéro>` (ex. `"L106"` pour Lee 106). Confirmé A par
  `Eos_Integration_via_OSC.md` et `Supported_OSC_Commands.md`.

## Teintes primaires — non ambiguës

| N° | Nom | Description / usage | Niveau | Source |
|---|---|---|---|---|
| 106 | Primary Red | Rouge franc et fort, va bien pour un cyclorama. | ✅ | [leefilters.com/colour/106-primary-red](https://leefilters.com/colour/106-primary-red/) |
| 139 | Primary Green | Vert pour cyclorama et effets de décor dramatiques. | ✅ | [leefiltersdirect.com/products/139-primary-green](https://leefiltersdirect.com/products/139-primary-green) |
| 120 | Deep Blue | Bleu intense et riche, effet de profondeur, dramatique. | ✅ | [leefilters.com/colour/120-deep-blue](https://leefilters.com/colour/120-deep-blue/) |
| 101 | Yellow | Effet de soleil / fenêtre, agréable en zone de jeu. | ✅ | [leefilters.com/colour/101-yellow](https://leefilters.com/colour/101-yellow/) |

**Note sur Bleu** : Lee ne nomme aucune teinte « Primary Blue » à proprement parler — 120
Deep Blue est la teinte bleue standard la plus proche d'un bleu primaire dans son
catalogue théâtre. Nom officiel retenu tel quel, pas de renommage inventé.

## Chaud / Froid — deux lectures, précisées mais pas encore closes

« Chaud » et « froid » n'ont pas de réponse unique chez Lee : le mot recouvre deux
usages de conception différents, chacun avec ses propres numéros.

### Lecture 1 — correction de température de couleur (réchauffer/refroidir un projecteur)

| N° | Nom | Description / usage | Niveau | Source |
|---|---|---|---|---|
| 201 | Full C.T. Blue | Refroidit fort — convertit tungstène (3200K) vers plus froid. Par symétrie avec 204 ; description exacte non vue. | 〰️ | — |
| 202 | 1/2 C.T. Blue | Refroidissement moyen. | ✅ | [thomannmusic.com/lee_farbfolie_nr202](https://www.thomannmusic.com/lee_farbfolie_nr202_half_ctblue.htm) |
| 203 | 1/4 C.T. Blue | Refroidissement léger, 3200K→3600K. | ✅ | [usa.leefiltersdirect.com/products/203-quarter-c-t-blue](https://usa.leefiltersdirect.com/products/203-quarter-c-t-blue) |
| 204 | Full C.T. Orange | Réchauffe fort — convertit lumière du jour (6500K) vers tungstène (3200K). C'est la correction la plus forte des trois. | ✅ | [leefilters.com/colour/204-full-c-t-orange](https://leefilters.com/colour/204-full-c-t-orange/) |
| 205 | 1/2 C.T. Orange | Réchauffement moyen — 6500K→3800K. | ✅ | [shopwl.com/lee-filters-205-1-2-ct-orange](https://shopwl.com/lee-filters-205-1-2-ct-orange/) |
| 206 | 1/4 C.T. Orange | Réchauffement léger — 6500K→4600K. | ✅ | [leefilters.com/colour/206-quarter-c-t-orange](https://leefilters.com/colour/206-quarter-c-t-orange/) |

**Confirmé par l'utilisateur (2026-08-03, connaissance terrain, confiance S)** :
204-206 = famille CHAUD (Orange, réchauffe), 201-203 = famille FROID (Blue, refroidit).
Chaque famille est graduée par force : Full (la plus forte) > Half (moyenne) >
Quarter (la plus légère).

**Décision autonome retenue en l'absence d'autre précision : 205 / 202** (force
« moitié », la plus courante en usage général — ni la correction la plus forte ni la
plus discrète). Si un projet demande explicitement une correction forte ou légère,
utiliser 204/201 ou 206/203 à la place.

### Lecture 2 — teinte d'ambiance chaude/froide pour une conduite (wash)

| N° | Nom | Description / usage | Niveau | Source |
|---|---|---|---|---|
| 147 | Apricot | Chaleur avant-scène, flatte la plupart des carnations — **attention sur peau très claire, tend vers le rose**. Confirmé ambre/chaud par l'utilisateur (S). | ✅ S | [leefilters.com/colour/147-apricot](https://leefilters.com/colour/147-apricot/) |
| inconnu | — | Trois candidats froids trouvés, aucun confirmé comme complément officiel de 147 : `161` Slate Blue (ciels, clair de lune, crépuscule), `118` Light Blue (effet de nuit marqué, ambiance froide/calme), ou `202` (lecture 1). | — | — |

**Aucune source consultée ne confirme de paire chaud/froid « officielle » pour un wash.**
Ne pas assembler 147 avec l'un des trois candidats froids sans confirmation.

## Catalogue élargi — recherché le 2026-08-03, hors des six teintes du test initial

Rassemblé pour couvrir un usage plus large que la demande d'origine. Classé par famille.
Rappel : ceci reste un sous-ensemble, pas le catalogue complet (plusieurs centaines de
teintes chez Lee au total). Description remplie seulement quand trouvée.

### Ambres, jaunes, oranges

| N° | Nom | Description / usage | Niveau |
|---|---|---|---|
| 007 | Pale Yellow | — | 〰️ |
| 009 | Pale Amber Gold | — | 〰️ |
| 010 | Medium Yellow | — | 〰️ |
| 013 | Straw Tint | — | 〰️ |
| 015 | Deep Straw | — | 〰️ |
| 020 | Medium Amber | — | ✅ |
| 021 | Gold Amber | — | 〰️ |
| 022 | Dark Amber Orange | — | 〰️ |
| 102 | Light Amber | — | 〰️ |
| 103 | Straw | — | 〰️ |
| 104 | Deep Amber | — | 〰️ |
| 105 | Orange | — | 〰️ |
| 151 | Gold Tint | Effet agréable en théâtre (description vague trouvée, pas de détail). | ✅ |
| 152 | Pale Gold | Utilisé en lumière d'intérieur, flatte les carnations. | ✅ |
| 158 | Deep Orange | Bon effet de feu. | 〰️ |
| 159 | No Colour Straw | Effet chaud. | 〰️ |
| 162 | Bastard Amber | — | 〰️ |

### Rouges, roses, saumon

| N° | Nom | Description / usage | Niveau |
|---|---|---|---|
| 002 | Rose Pink | — | 〰️ |
| 008 | Dark Salmon | — | 〰️ |
| 024 | Scarlet | — | 〰️ |
| 025 | Sunset Red | — | 〰️ |
| 026 | Bright Red | — | 〰️ |
| 027 | Medium Red | — | 〰️ |
| 029 | Plasa Red | — | 〰️ |
| 035 | Light Pink | — | 〰️ |
| 036 | Medium Pink | — | 〰️ |
| 039 | Pink Carnation | — | 〰️ |
| 107 | Light Rose | — | 〰️ |
| 108 | English Rose | — | 〰️ |
| 109 | Light Salmon | — | 〰️ |
| 110 | Middle Rose | — | 〰️ |
| 153 | Pale Salmon | Pour contre-jour, en complément d'une lumière blanche. | 〰️ |
| 154 | Pale Rose | Effet agréable en théâtre, bon effet « lueur de lampe ». | ✅ |
| 157 | Pink | Pour la danse — adoucit les costumes blancs sans changer les carnations. | 〰️ |

### Mauves, lavandes, violets

| N° | Nom | Description / usage | Niveau |
|---|---|---|---|
| 003 | Lavender Tint | — | 〰️ |
| 048 | Rose Purple | — | 〰️ |
| 049 | Medium Purple | — | 〰️ |
| 052 | Light Lavender | — | 〰️ |
| 053 | Paler Lavender | — | 〰️ |
| 169 | Lilac Tint | — | 〰️ |
| 701 | Provence | — | ✅ |
| 702 | Special Pale Lavender | — | ✅ |
| 799 | Special KH Lavender | — | ✅ |

### Bleus, verts

| N° | Nom | Description / usage | Niveau |
|---|---|---|---|
| 061 | Mist Blue | — | 〰️ |
| 063 | Pale Blue | — | 〰️ |
| 118 | Light Blue | Effet de nuit marqué, ambiance froide et calme. | ✅ |
| 132 | Medium Blue | — | 〰️ |
| 161 | Slate Blue | Bleu moyen pur — ciels, clair de lune, crépuscule. | ✅ |
| 213 | White Flame Green | — | 〰️ |

### Diffusion / effets

| N° | Nom | Description / usage | Niveau |
|---|---|---|---|
| 156 | Chocolate | Réchauffe la lumière et réduit son intensité. | ✅ |
| 216 | White Diffusion | — | 〰️ |
| 255 | Hollywood Frost | — | 〰️ |

### Écarté volontairement

Une recherche sur la série « spéciales » 700-799 a renvoyé d'un coup une quarantaine de
noms (ex. « 735 Velvet Green », « 777 Rust »...) sans page produit individuelle
retrouvée pour la plupart. Vu le volume d'un coup et l'absence de vérification
entrée par entrée, le risque d'erreur ou d'invention par l'outil de recherche était trop
élevé pour ce projet — **non retenues**. Seules 701, 702 et 799 ci-dessus, confirmées
individuellement, en font partie.

## Ce qui reste ouvert

- Le complément froid du wash 147 Apricot (lecture 2), si jamais préféré à la lecture 1.
- La majorité des entrées « 〰️ » n'ont pas de description : nom seul, effet inconnu.
  Ne pas choisir l'une d'elles pour une décision où l'effet compte, sans vérifier d'abord.
- Catalogue Lee complet et officiel : toujours absent du dépôt (`PLANNING.md` #34,
  inchangé sur ce point — cette table ne le referme pas, elle documente un sous-ensemble
  vérifié, désormais plus large qu'au 2026-08-03 initial).

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
    avant un usage critique (une couleur récréative). Les couleurs "spéciales" de la
    série 700 rapportées en trop grand nombre en une seule fois ont été **écartées** —
    risque trop élevé d'erreur pour ce niveau de vérification.

## Syntaxe console (rappel, confirmé A — voir `grammar/modele.yaml`)

- Ligne de commande : `Color <bibliothèque>/<numéro>`. Lee = bibliothèque **3**.
  Exemple : `Chan 4 Color 3/195 Enter` (manuel §10, corpus #082).
- OSC direct : chaîne `L<numéro>` (ex. `"L106"` pour Lee 106). Confirmé A par
  `Eos_Integration_via_OSC.md` et `Supported_OSC_Commands.md`.

## Teintes primaires — non ambiguës

| Teinte demandée | Numéro Lee | Nom officiel Lee | Niveau | Source |
|---|---|---|---|---|
| Rouge | 106 | Primary Red | ✅ | [leefilters.com/colour/106-primary-red](https://leefilters.com/colour/106-primary-red/) |
| Vert | 139 | Primary Green | ✅ | [leefiltersdirect.com/products/139-primary-green](https://leefiltersdirect.com/products/139-primary-green) |
| Bleu | 120 | Deep Blue | ✅ | [leefilters.com/colour/120-deep-blue](https://leefilters.com/colour/120-deep-blue/) |
| Jaune | 101 | Yellow | ✅ | [leefilters.com/colour/101-yellow](https://leefilters.com/colour/101-yellow/) |

**Note sur Bleu** : Lee ne nomme aucune teinte « Primary Blue » à proprement parler — 120
Deep Blue est la teinte bleue standard la plus proche d'un bleu primaire dans son
catalogue théâtre. Nom officiel retenu tel quel, pas de renommage inventé.

## Chaud / Froid — AMBIGU, deux lectures possibles, non tranché

« Chaud » et « froid » n'ont pas de réponse unique chez Lee : le mot recouvre deux
usages de conception différents, chacun avec ses propres numéros.

### Lecture 1 — correction de température de couleur (réchauffer/refroidir un projecteur)

| Teinte | Numéro | Nom officiel | Niveau | Source |
|---|---|---|---|---|
| Froid (famille) | 201 | Full C.T. Blue (3200K→4300K) | 〰️ | synthèse recherche |
| Froid (famille) | 202 | 1/2 C.T. Blue | ✅ | [thomannmusic.com/lee_farbfolie_nr202](https://www.thomannmusic.com/lee_farbfolie_nr202_half_ctblue.htm) |
| Froid (famille) | 203 | 1/4 C.T. Blue (3200K→3600K) | ✅ | [usa.leefiltersdirect.com/products/203-quarter-c-t-blue](https://usa.leefiltersdirect.com/products/203-quarter-c-t-blue) |
| Chaud (famille) | 204 | Full C.T. Orange (6500K→3200K) | 〰️ | synthèse recherche |
| Chaud (famille) | 205 | 1/2 C.T. Orange | 〰️ | synthèse recherche |
| Chaud (famille) | 206 | 1/4 C.T. Orange (6500K→4600K) | 〰️ | synthèse recherche |

**Confirmé par l'utilisateur (2026-08-03, connaissance terrain)** : « les correcteurs
chauds sont plutôt de 204 à 206 » — 204-206 forment la famille CHAUD (Orange, réchauffe),
201-203 la famille FROID (Blue, refroidit), chacune graduée full/half/quarter selon
l'intensité de correction. Confiance relevée à S sur ce point (source directe), le reste
(noms précis 201/204/206) demeure 〰️ tant que la page produit individuelle n'est pas vue.

Paire chaud/froid « milieu de famille » : 205 (Half CT Orange) / 202 (Half CT Blue) —
cohérente par construction, les deux nommées comme correction CT complémentaire. À
préciser : 204 (Full), 205 (Half) ou 206 (Quarter) exactement pour la macro ?

### Lecture 2 — teinte d'ambiance chaude/froide pour une conduite (wash)

| Teinte | Numéro | Nom officiel | Caractère rapporté | Niveau | Source |
|---|---|---|---|---|---|
| Chaud | 147 | Apricot | « warm highlight… good for warm front light, complimentary to most skin tones » — **confirmé ambre/chaud par l'utilisateur (S)**, 2026-08-03 | ✅ S | [leefilters.com/colour/147-apricot](https://leefilters.com/colour/147-apricot/) |
| Froid | inconnu | — | trois candidats, aucun confirmé comme complément standard de 147 : `161` Slate Blue (moonlight/dusk), `118` Light Blue (cool/night), ou `202` (lecture 1) | — | — |

**Aucune source consultée ne confirme de paire chaud/froid « officielle » pour un wash.**
Ne pas assembler 147 avec l'un des trois candidats froids sans confirmation.

## Catalogue élargi — recherché le 2026-08-03, hors des six teintes du test initial

Rassemblé pour couvrir un usage plus large que la demande d'origine. Classé par famille.
Rappel : ceci reste un sous-ensemble, pas le catalogue complet (plusieurs centaines de
teintes chez Lee au total).

### Ambres, jaunes, oranges

| Numéro | Nom officiel | Niveau |
|---|---|---|
| 007 | Pale Yellow | 〰️ |
| 009 | Pale Amber Gold | 〰️ |
| 010 | Medium Yellow | 〰️ |
| 013 | Straw Tint | 〰️ |
| 015 | Deep Straw | 〰️ |
| 020 | Medium Amber | ✅ [leefilters.com/colour/020-medium-amber](https://leefilters.com/colour/020-medium-amber/) |
| 021 | Gold Amber | 〰️ |
| 022 | Dark Amber Orange | 〰️ |
| 102 | Light Amber | 〰️ |
| 103 | Straw | 〰️ |
| 104 | Deep Amber | 〰️ |
| 105 | Orange | 〰️ |
| 151 | Gold Tint | ✅ [leefiltersdirect.com/products/lee-151-gold-tint-lighting-gel](https://usa.leefiltersdirect.com/products/lee-151-gold-tint-lighting-gel) |
| 152 | Pale Gold | ✅ [leefilters.com/colour/152-pale-gold](https://leefilters.com/colour/152-pale-gold/) |
| 158 | Deep Orange | 〰️ |
| 159 | No Colour Straw | 〰️ |
| 162 | Bastard Amber | 〰️ |

### Rouges, roses, saumon

| Numéro | Nom officiel | Niveau |
|---|---|---|
| 002 | Rose Pink | 〰️ |
| 008 | Dark Salmon | 〰️ |
| 024 | Scarlet | 〰️ |
| 025 | Sunset Red | 〰️ |
| 026 | Bright Red | 〰️ |
| 027 | Medium Red | 〰️ |
| 029 | Plasa Red | 〰️ |
| 035 | Light Pink | 〰️ |
| 036 | Medium Pink | 〰️ |
| 039 | Pink Carnation | 〰️ |
| 107 | Light Rose | 〰️ |
| 108 | English Rose | 〰️ |
| 109 | Light Salmon | 〰️ |
| 110 | Middle Rose | 〰️ |
| 153 | Pale Salmon | 〰️ |
| 154 | Pale Rose | ✅ (Amazon, fiche produit « Lee #154 Pale Rose ») |
| 157 | Pink | 〰️ |

### Mauves, lavandes, violets

| Numéro | Nom officiel | Niveau |
|---|---|---|
| 003 | Lavender Tint | 〰️ |
| 048 | Rose Purple | 〰️ |
| 049 | Medium Purple | 〰️ |
| 052 | Light Lavender | 〰️ |
| 053 | Paler Lavender | 〰️ |
| 169 | Lilac Tint | 〰️ |
| 701 | Provence | ✅ [leefiltersdirect.com/products/lee-701-provence-lighting-gel](https://leefiltersdirect.com/products/lee-701-provence-lighting-gel) |
| 702 | Special Pale Lavender | ✅ [leefilters.com/colour/702-special-pale-lavender](https://leefilters.com/colour/702-special-pale-lavender/) |
| 799 | Special KH Lavender | ✅ [leefilters.com/colour/799-special-kh-lavender](https://leefilters.com/colour/799-special-kh-lavender/) |

### Bleus, verts

| Numéro | Nom officiel | Niveau |
|---|---|---|
| 061 | Mist Blue | 〰️ |
| 063 | Pale Blue | 〰️ |
| 118 | Light Blue | ✅ [leefilters.com/colour/118-light-blue](https://leefilters.com/colour/118-light-blue/) |
| 132 | Medium Blue | 〰️ |
| 161 | Slate Blue | ✅ [leefilters.com/colour/161-slate-blue](https://leefilters.com/colour/161-slate-blue/) |
| 213 | White Flame Green | 〰️ |

### Diffusion / effets

| Numéro | Nom officiel | Niveau |
|---|---|---|
| 156 | Chocolate (réchauffe, réduit l'intensité) | ✅ [leefilters.com/colour/156-chocolate](https://leefilters.com/colour/156-chocolate/) |
| 216 | White Diffusion | 〰️ |
| 255 | Hollywood Frost | 〰️ |

### Écarté volontairement

Une recherche sur la série « spéciales » 700-799 a renvoyé d'un coup une quarantaine de
noms (ex. « 735 Velvet Green », « 777 Rust »...) sans page produit individuelle
retrouvée pour la plupart. Vu le volume d'un coup et l'absence de vérification
entrée par entrée, le risque d'erreur ou d'invention par l'outil de recherche était trop
élevé pour ce projet — **non retenues**. Seules 701, 702 et 799 ci-dessus, confirmées
individuellement, en font partie.

## Ce qui reste ouvert

- Lequel des deux usages (correction CT ou wash d'ambiance) correspondait à la demande
  du 2026-08-03 — à confirmer avec l'utilisateur avant de générer la macro finale.
- Le complément froid du wash 147 Apricot, si la lecture 2 est retenue.
- Toute entrée « 〰️ probable » : à re-vérifier avant un usage où l'erreur coûterait cher.
- Catalogue Lee complet et officiel : toujours absent du dépôt (`PLANNING.md` #34,
  inchangé sur ce point — cette table ne le referme pas, elle documente un sous-ensemble
  vérifié, désormais plus large qu'au 2026-08-03 initial).

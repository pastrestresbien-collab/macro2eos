# Lee Filters — table de référence théâtre (catalogue officiel intégral)

## Source

- **Catalogue officiel Lee Filters « Art of Light »** (édition ~2007, tampon interne
  « 13/8/07 » sur chaque page), 39 pages. Fourni par l'utilisateur en upload direct le
  2026-08-05 (voir `CLAUDE.md` règle n°1 — seule voie fiable dans cet environnement,
  l'accès réseau direct étant bloqué). PDF conservé intégralement dans
  [`reference/source/LEE_Filters_Art_of_Light_brochure.pdf`](source/LEE_Filters_Art_of_Light_brochure.pdf)
  pour re-vérification future. **Les 39 pages ont été lues intégralement** (réponse à
  « est-il complet ? » : oui, c'est le catalogue complet — sommaire, science de la
  couleur, gamme couleur complète classée par teinte, listing numérique de contrôle,
  filtres techniques, gammes commerciales).
- **Remplace l'ancienne version de ce fichier**, qui était sourcée par `WebSearch`
  (extraits de recherche, confiance variable ✅/〰️ selon qu'une page produit individuelle
  avait été retrouvée ou non). Toutes les entrées ci-dessous viennent directement du
  catalogue officiel, page indiquée : **confiance unique ✅ officiel**, plus de
  distinction à deux niveaux nécessaire.
- **Édition ~2007** : Lee peut avoir ajouté ou retiré des teintes depuis. C'est
  cependant la source la plus complète et la plus fiable disponible dans cet
  environnement. Si une teinte précise semble absente ou discontinuée aujourd'hui, à
  revérifier au besoin (voir `CLAUDE.md` règle n°1 pour la procédure).
- **Colonne Transmission Y%** : pourcentage de lumière transmise (mesuré source C
  standard, donnée telle quelle par le catalogue) — indication de force/saturation de la
  teinte (plus la valeur est basse, plus la teinte est saturée/sombre).
- **Hors de ce fichier** (présents dans le PDF source, pp.28-38, mais pas des
  « couleurs » à proprement parler — diffusions/frosts neutres, tissus de grille, tough
  spun, réflecteurs, protection, polariseur, panneaux acryliques, packs commerciaux) :
  non repris en détail ici, hors sujet pour une macro de palette couleur. Seules les
  conversions de température de couleur (CTO/CTB, pertinentes pour « chaud/froid ») sont
  reprises avec leurs valeurs Kelvin officielles.

## Syntaxe console (rappel, confirmé A — voir `grammar/modele.yaml`)

- Ligne de commande : `Color <bibliothèque>/<numéro>`. Lee = bibliothèque **3**.
  Exemple : `Chan 4 Color 3/195 Enter` (manuel §10, corpus #082).
- OSC direct : chaîne `L<numéro>` (ex. `"L106"` pour Lee 106). Confirmé A par
  `Eos_Integration_via_OSC.md` et `Supported_OSC_Commands.md`.

## Teintes primaires — non ambiguës

| N° | Nom | Description / usage | Transmission Y% | Page |
|---|---|---|---|---|
| 106 | Primary Red | Rouge franc, effet fort, va bien pour un cyclorama. | 9.3 | 22 |
| 139 | Primary Green | Éclairage de plateau, cyclorama. | 11.9 | 19 |
| 120 | Deep Blue | Effet agréable pour l'éclairage théâtral. | 2.1 | 17 |
| 101 | Yellow | Effet de soleil / fenêtre, agréable en zone de jeu. | 80.0 | 21 |

**Note sur Bleu** : Lee ne nomme aucune teinte « Primary Blue » à proprement parler — 120
Deep Blue est la teinte bleue standard la plus proche d'un bleu primaire dans son
catalogue théâtre. Nom officiel retenu tel quel, confirmé par le catalogue.

## Chaud / Froid — deux lectures

« Chaud » et « froid » n'ont pas de réponse unique chez Lee : le mot recouvre deux
usages de conception différents.

### Lecture 1 — correction de température de couleur (réchauffer/refroidir une source)

Table officielle de conversion (catalogue p.30, valeurs Kelvin exactes) :

| N° | Nom | Conversion | Description | Transmission Y% |
|---|---|---|---|---|
| 201 | Full CTB | 3200K → 5700K | Convertit tungstène en lumière du jour photographique. | 34.0 |
| 202 | Half CTB | 3200K → 4300K | Convertit tungstène en lumière du jour. | 54.9 |
| 203 | Quarter CTB | 3200K → 3600K | Convertit tungstène en lumière du jour. | 69.2 |
| 204 | Full CTO | 6500K → 3200K | Convertit lumière du jour en tungstène. | 55.4 |
| 205 | Half CTO | 6500K → 3800K | Convertit lumière du jour en tungstène. | 70.8 |
| 206 | Quarter CTO | 6500K → 4600K | Convertit lumière du jour en tungstène. | 79.1 |

**Confirmé par l'utilisateur (2026-08-03, connaissance terrain, confiance S), et cohérent
avec le sens des conversions officielles ci-dessus** : 204-206 (CTO, orange) = famille
CHAUD, réchauffe une source ; 201-203 (CTB, blue) = famille FROID, refroidit une source.
Chaque famille est graduée par force : Full (la plus forte) > Half (moyenne) > Quarter
(la plus légère).

**Décision autonome retenue en l'absence d'autre précision : 205 / 202** (force
« moitié », la plus courante en usage général — ni la correction la plus forte ni la
plus discrète). Si un projet demande explicitement une correction forte ou légère,
utiliser 204/201 ou 206/203 à la place.

### Lecture 2 — teinte d'ambiance chaude/froide pour une conduite (wash)

| N° | Nom | Description / usage | Transmission Y% | Page |
|---|---|---|---|---|
| 147 | Apricot | Lever de soleil, coucher de soleil, lumière de lampe. | 53.0 | 21 |
| 161 | Slate Blue | Bleu moyen pur. Bon pour ciels, clair de lune, crépuscule. | 24.8 | 18 |
| 118 | Light Blue | Effet de nuit marqué. | 22.2 | 18 |

**Le catalogue ne publie aucune paire chaud/froid « officielle » pour un wash** (les
descriptions ci-dessus sont indépendantes, pas présentées comme complémentaires l'une de
l'autre). 147 Apricot reste confirmé chaud/ambre par l'utilisateur (S). Pour un froid de
wash, 161 Slate Blue (ciels/crépuscule) ou 118 Light Blue (nuit marquée) restent les deux
candidats non tranchés — à défaut d'autre précision, la Lecture 1 (202, correction CT)
reste l'option la mieux sourcée pour « froid ».

## Gamme couleur complète (catalogue officiel, pp.16-25)

Classée par famille, dans l'ordre du catalogue (pâle → saturé au sein de chaque famille).

### Lavandes, mauves, violets (p.16)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 702 | Special Pale Lavender | Lavande froide en tungstène plein, se réchauffe si la source baisse. Bon pour fondus de coucher de soleil lents. | 54.1 |
| 003 | Lavender Tint | Wash froid subtil pour scène et studio. | 75.7 |
| 169 | Lilac Tint | Lavande pâle. Bon pour une lumière presque blanche avec une teinte froide. | 59.5 |
| 136 | Pale Lavender | Pantomime, salles de bal, accentue les tons de peau foncés en poursuite. | 43.2 |
| 170 | Deep Lavender | Éclairage de décor - discothèques - théâtres. | 25.7 |
| 345 | Fuchsia Pink | Revue musicale, pantomime, scènes suggestives. | 15.5 |
| 704 | Lily | Lavande froide à faible composante rouge. Bon pour extérieurs romantiques du soir. | 40.0 |
| 052 | Light Lavender | Latéraux de zone générale. Excellente couleur de poursuite de base. Excellent contre-jour. | 33.0 |
| 194 | Surprise Pink | Avec 193 pour les comédies musicales. | 22.3 |
| 798 | Chrysalis Pink | Nouvelle lavande profonde avec une touche de blush rose. | 3.8 |
| 701 | Provence | Couleur des champs de lavande du sud de la France. Version plus rouge de 180, pour caméras balancées tungstène. | 9.4 |
| 058 | Lavender | Excellent contre-jour. Crée une nouvelle dimension. | 8.9 |
| 343 | Special Medium Lavender | Éclairage d'effet théâtre et TV, contre-jour. | 6.0 |
| 707 | Ultimate Violet | Utilisé en spectacle musical pour washs de couleur généraux et éclairage de décor. | 2.0 |
| 180 | Dark Lavender | Effets agréables pour l'éclairage théâtral, contre-jour. | 6.6 |
| 706 | King Fals Lavender | Lavande froide. | 5.5 |
| 344 | Violet | Effet crépuscule, bons tons de peau, effet romantique. | 20.0 |
| 137 | Special Lavender | Clair de lune, scènes musicales/romantiques, accentue les tons de peau. | 26.4 |
| 053 | Paler Lavender | Wash froid subtil. | 62.2 |
| 709 | Electric Lilac | Bon rendu des couleurs, crée des contours nets, ajoute une touche de drame. | 34.0 |
| 142 | Pale Violet | Clair de lune, cycloramas, mise en valeur de plantes en pot. | 20.1 |
| 199 | Regal Blue | Bleu-lavande profond, accentue fortement les tons de peau. | 5.4 |
| 181 | Congo Blue | Ressemble à une lumière noire avec une source fluorescente. Excellente couleur d'effet. Très saturée. | 0.8 |
| 799 | Special K.H. Lavender | Lavande profonde qui fait ressortir l'UV. | 1.4 |
| 071 | Tokyo Blue | Bleu profond, scènes de minuit, cycloramas. | 1.0 |

### Bleus (pp.17-18)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 198 | Palace Blue | Clair de lune sombre - soirée romantique. | 1.7 |
| 713 | J.Winter Blue | Bleu très sombre à forte teneur UV. Bon en forte concentration pour un wash de scène puissant et mélancolique. | 1.1 |
| 120 | Deep Blue | Effet agréable pour l'éclairage théâtral. | 2.1 |
| 085 | Deeper Blue | Bleu profond et chaud. Bon pour contre-jour et latéraux. | 2.5 |
| 716 | Mikkel Blue | Bleu romantique pour un effet de nuit. | 3.9 |
| 363 | Special Medium Blue | Clair de lune froid, effets d'ambiance. | 4.2 |
| 195 | Zenith Blue | Clair de lune pour décors sombres, cycloramas. | 2.7 |
| 119 | Dark Blue | Bon pour effets d'ambiance créés par contre-jour et latéral. Crée un grand contraste. | 3.1 |
| 715 | Cabana Blue | Bleu profond qui garde assez de transmission pour bien fonctionner à la télévision. | 6.8 |
| 723 | Virgin Blue | Bleu pur, ni trop vert ni trop lavande, garde une sensation chaude pour un bleu, effet petit matin. | 7.0 |
| 721 | Berry Blue | Utilisé en spectacle musical pour wash arrière, ou éclairage de décor. | 6.5 |
| 722 | Bray Blue | Bleu plus pur avec très peu de rouge. | 5.2 |
| 714 | Elysian Blue | Nouvelle version plus profonde d'Alice Blue. | 6.8 |
| 079 | Just Blue | Bon bleu de mélange de couleurs. Excellent pour l'éclairage de cyclorama. | 5.6 |
| 710 | Spir Special Blue | Bleu industriel froid. | 12.2 |
| 197 | Alice Blue | Excellent pour l'éclairage de cyclorama. Ciels bleu profond. | 10.4 |
| 075 | Evening Blue | Bon pour scènes de nuit, clair de lune romantique. | 12.5 |
| 712 | Bedford Blue | Bleu chaud et fumé. Bon pour les tons de peau. | 17.9 |
| 719 | Colour Wash Blue | Permet à un tungstène de faible intensité de garder une sensation froide/bleue. | 19.3 |
| 200 | Double CTB | Convertit tungstène en lumière du jour. | 16.2 |
| 711 | Cold Blue | Donne un effet froid/gris HMI depuis une source tungstène. Aide aussi au mélange tungstène/HMI. | 14.4 |
| 366 | Cornflower | Éclairage d'ambiance saisonnier, clair de lune pâle. | 17.7 |
| 201 | Full CTB | Convertit tungstène en lumière du jour photographique. | 34.0 |
| 708 | Cool Lavender | Teinte plus chaude sans virer au jaune, recrée la couleur d'un éclairage fluorescent. | 43.4 |
| 281 | Threequarters CTB | Convertit tungstène en lumière du jour. | 45.5 |
| 202 | Half CTB | Convertit tungstène en lumière du jour. | 54.9 |
| 061 | Mist Blue | Scènes de nuit, wash froid. | 62.4 |
| 203 | Quarter CTB | Convertit tungstène en lumière du jour. | 69.2 |
| 218 | Eighth CTB | Convertit tungstène en lumière du jour. | 81.3 |
| 063 | Pale Blue | Wash frontal froid, bon pour un effet couvert par temps froid. | 54.4 |
| 174 | Dark Steel Blue | Éclairage de décor - crée de bonnes ombres de clair de lune. | 30.0 |
| 161 | Slate Blue | Bleu moyen pur. Bon pour ciels, clair de lune, crépuscule. | 24.8 |
| 068 | Sky Blue | Tons de peau du matin, ciel nocturne. Lumières de cyclorama. | 13.4 |
| 132 | Medium Blue | Clair de lune profond. Excellent pour le mélange de couleurs. | 8.3 |
| 165 | Daylight Blue | Clair de lune. | 20.0 |
| 141 | Bright Blue | Très dramatique utilisé comme clair de lune. | 18.6 |
| 196 | True Blue | Clair de lune. | 26.6 |
| 143 | Pale Navy Blue | Clair de lune, effet de nuit de cyclorama. | 16.2 |
| 352 | Glacier Blue | Bleu froid, bon pour une ambiance atmosphérique fraîche. | 23.4 |
| 724 | Ocean Blue | Utile à faible niveau de lumière, ciels ternes, clair de lune. | 36.2 |
| 140 | Summer Blue | Bon pour un ciel de milieu de journée léger. Wash légèrement teinté bleu. | 41.4 |
| 117 | Steel Blue | Bon pour washs froids. Ajoute une teinte verte pâle. Excellent pour simuler un temps glacial sur scène. | 54.7 |
| 725 | Old Steel Blue | Wash froid, utile pour les rehauts. | 56.2 |
| 353 | Lighter Blue | Effets de lumière du jour. | 41.0 |
| 144 | No Colour Blue | Bleu propre avec des nuances de vert. Bon pour clair de lune et latéral. | 32.4 |
| 118 | Light Blue | Effet de nuit marqué. | 22.2 |
| 183 | Moonlight Blue | Clair de lune, cycloramas. | 18.7 |
| 172 | Lagoon Blue | Wash chaud en flood - scènes sous-marines - ballet. | 25.4 |
| 729 | Scuba Blue | Utilisé en spectacle musical pour un wash arrière, ou éclairage de décor. | 8.7 |
| 116 | Medium Blue-Green | Effet agréable pour l'éclairage théâtral. | 16.5 |

### Verts (pp.18-19)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 354 | Special Steel Blue | Wash bleu-vert rafraîchissant pour scène et décor. | 39.2 |
| 115 | Peacock Blue | Effet agréable sur décors, toiles de cyclorama, contre-jour (patinoires, galas, etc.). | 35.2 |
| 131 | Marine Blue | Clair de lune romantique - ballet - scènes sous-marines. | 41.3 |
| 241 | LEE Fluorescent 5700 Kelvin | Convertit tungstène en fluorescent 5700K (blanc froid/jour). | 27.4 |
| 728 | Steel Green | Tempête approchante. Jours couverts. Lumière froide et métallique. Clair de lune malveillant. | 45.9 |
| 730 | Liberty Green | Bon vert pour créer mystère et suspense. | 67.5 |
| 243 | LEE Fluorescent 3600 Kelvin | Convertit tungstène en fluorescent 3600K (blanc chaud). | 45.7 |
| 242 | LEE Fluorescent 4300 Kelvin | Convertit tungstène en fluorescent 4300K (blanc). | 37.3 |
| 219 | LEE Fluorescent Green | Correction générale tungstène→fluorescent quand la température couleur du fluo est inconnue, correction moyenne. | 31.0 |
| 323 | Jade | À utiliser pour scènes sous-marines, cycloramas, contre-jour. | 32.0 |
| 322 | Soft Green | Vert froid, pour habillage de gobo, pantomime, cycloramas. | 38.3 |
| 325 | Mallard Green | Bon pour créer une ambiance, sous-bois. | 7.7 |
| 735 | Velvet Green | Belle couleur de fond. Mélodrame victorien. Vert de nuit. | 11.5 |
| 124 | Dark Green | Cycloramas - bon pour le contre-jour. | 29.7 |
| 327 | Forest Green | Vert profond, scènes de forêt sinistre, cycloramas, contre-jour. | 4.2 |
| 090 | Dark Yellow Green | Mise en valeur pour effets de forêt. | 10.9 |
| 736 | Twickenham Green | Vert puissant avec de la profondeur, pour musique ou spectacle. | 7.2 |
| 740 | Aurora Borealis Green | Couleur de jungle primaire. Retire du rouge et du bleu. Fonctionne mieux avec des lampes jour. Effet lampe au sodium. | 3.7 |
| 139 | Primary Green | Éclairage de plateau, cyclorama. | 11.9 |
| 089 | Moss Green | Créateur d'ambiance. Utilisé avec des gobos, crée un excellent effet de feuillage. | 29.8 |
| 122 | Fern Green | Cycloramas - bon pour l'effet d'ambiance. | 51.5 |
| 738 | JAS Green | Vert jaunâtre riche : utile comme wash de concert où tons de peau foncés, costume et décor sont à considérer. | 52.3 |
| 121 | LEE Green | Feuillage dense, effet tropical ou forestier. | 64.0 |
| 088 | Lime Green | À utiliser avec des gobos pour clairières feuillues - pantomimes - ambiance légèrement sinistre. | 70.9 |
| 138 | Pale Green | Bon avec des gobos pour scènes boisées. | 79.9 |
| 244 | LEE Plus Green | Approximativement équivalent à CC30 vert. | 74.2 |
| 213 | White Flame Green | Corrige les arcs carbone à flamme blanche en absorbant l'ultraviolet. | 80.0 |
| 245 | Half Plus Green | Approximativement équivalent à CC15 vert. | 81.7 |
| 246 | Quarter Plus Green | Approximativement équivalent à CC075 vert. | 84.6 |
| 278 | Eighth Plus Green | Léger voile vert. | 87.7 |
| 130 | Clear | Utilisé en animation et projection. | 95.0 |
| 226 | LEE UV | Transmission inférieure à 50% à 410nm. | 91.5 |

### Jaunes, ambres pâles, pailles (pp.20-21)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 159 | No Colour Straw | Effet chaud, lumière du soleil. | 89.4 |
| 444 | Eighth CT Straw | Convertit 6500K en 5700K - jour vers tungstène, biais jaune. | 83.1 |
| 212 | LCT Yellow (Y1) | Réduit la température de couleur des arcs carbone bas à 3200K. | 88.7 |
| 007 | Pale Yellow | Lumière du soleil. | 85.4 |
| 443 | Quarter CT Straw | Convertit 6500K en 5100K - jour vers tungstène, biais jaune. | 79.8 |
| 206 | Quarter CTO | Convertit lumière du jour en tungstène. | 79.1 |
| 763 | Wheat | Ajoute de la chaleur, effet soleil. | 84.3 |
| 103 | Straw | Effet de lumière du soleil pâle à travers une fenêtre - effet hiver chaud. | 81.6 |
| 764 | Sun Colour Straw | Ajoute de la chaleur, soleil vif. | 80.5 |
| 442 | Half CT Straw | Convertit 6500K en 4300K - jour vers tungstène, biais jaune. | 71.2 |
| 205 | Half CTO | Convertit lumière du jour en tungstène. | 70.8 |
| 162 | Bastard Amber | Blanc chaud, wash chaud, lumière de lampe. | 77.7 |
| 009 | Pale Amber Gold | Excellente lumière frontale chaude pour tout ton de peau. | 71.1 |
| 765 | LEE Yellow | Utile pour produire un fort effet de lumière du soleil. | 80.2 |
| 013 | Straw Tint | Plus chaud que les autres pailles. Bon effet soleil utilisé en contraste avec ambres et bleus. | 72.1 |
| 285 | Threequarters CTO | Convertit lumière du jour en tungstène. | 61.3 |
| 744 | Dirty White | Corrige une source jour en tungstène blanc cassé. Avec une source tungstène, donne un effet « miteux » façon bar enfumé. | 57.9 |
| 441 | Full CT Straw | Convertit 6500K en 3200K - jour vers tungstène, biais jaune. | 57.3 |
| 100 | Spring Yellow | Wash de lumière du soleil - à utiliser avec gobos, disco, tons de peau foncés. | 84.2 |
| 010 | Medium Yellow | Jaune vif pur. Pas bon pour les zones de jeu mais excellent pour effets spéciaux et accents. | 86.5 |
| 101 | Yellow | Effet de soleil et fenêtre - agréable en zone de jeu. | 80.0 |

### Ambres, oranges (p.21-22)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 236 | HMI (to Tungsten) | Convertit HMI en 3200K, pour film tungstène. | 58.2 |
| 773 | Cardbox Amber | Teinte chaude pour tons de peau. | 60.2 |
| 108 | English Rose | Wash teinté chaud - tons de peau foncés - tons de peau plus doux. | 57.1 |
| 776 | Nectarine | Coucher de soleil romantique. Pièces d'époque. | 52.9 |
| 147 | Apricot | Lever de soleil, coucher de soleil, lumière de lampe. | 53.0 |
| 237 | CID (to Tungsten) | Convertit CID en 3200K, pour film tungstène. | 38.5 |
| 208 | Full CTO +.6ND | Convertit jour en tungstène 6500K→3200K et réduit la lumière de 2 stops. | 15.6 |
| 207 | Full CTO +.3ND | Convertit jour en tungstène 6500K→3200K et réduit la lumière de 1 stop. | 32.5 |
| 232 | Super Correction W.F. Green to Tungsten | Convertit arc à flamme blanche en 3200K, pour film tungstène. | 37.4 |
| 230 | Super Correction LCT Yellow | Convertit un arc carbone jaune (basse température) en tungstène. | 41.9 |
| 204 | Full CTO | Convertit lumière du jour en tungstène. | 55.4 |
| 102 | Light Amber | Jaune chaud. Excellent pour effet bougie ou fort soleil chaud. | 75.1 |
| 767 | Oklahoma Yellow | Riche mélange de soleil éclatant et de tons ocre chauds. | 68.9 |
| 104 | Deep Amber | Bon pour effet de soleil, accents, latéral. Attention aux tons de peau sous la teinte rougeâtre. | 63.9 |
| 015 | Deep Straw | Lumière ambrée chaude. Bon pour effets bougie et feu. | 60.8 |
| 179 | Chrome Orange | Combinaison de 1/2 CTO et 104 en double force, soleil. | 54.0 |
| 020 | Medium Amber | Soleil d'après-midi, bougie, excellent latéral. | 50.7 |
| 770 | Burnt Yellow | Couleur chaude et dense à la caméra, équilibre entre 179 et 105. | 47.7 |
| 105 | Orange | Surtout spectacle/événementiel. Effet feu si utilisé avec 106, 166, 104. | 41.3 |
| 134 | Golden Amber | Excellent pour simuler une fin de journée. Latéral, cyclorama. | 37.8 |
| 158 | Deep Orange | Effet feu. | 29.9 |
| 777 | Rust | Effet rouille vif. | 24.3 |
| 021 | Gold Amber | Excellent pour couchers de soleil, cyclorama, effets de feu. | 31.3 |
| 778 | Millennium Gold | Utile en éclairage architectural : ambre riche sur tungstène, effet plus froid sur HMI. | 27.3 |
| 022 | Dark Amber | Contre-jour. | 23.9 |
| 135 | Deep Golden Amber | Effet feu. | 19.5 |
| 741 | Mustard Yellow | Inquiétant dans la brume. Retire du rouge et du bleu. Fonctionne mieux avec lampes jour. Effet lampe au sodium. | 3.3 |

### Rouges, roses, saumon (pp.22-23)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 779 | Bastard Pink | Coucher de soleil profond. Utile sur tons de peau foncés. | 38.8 |
| 008 | Dark Salmon | Accentue les tons de peau foncés, couchers de soleil, salles de bal. | 35.4 |
| 017 | Surprise Peach | Tons de peau - ambiance. | 19.6 |
| 127 | Smokey Pink | Cycloramas - éclairage de décor, discothèques. | 12.0 |
| 748 | Seedy Pink | Rose fumé. Bon pour tungstène sur tons de peau. | 14.4 |
| 238 | CSI (to Tungsten) | Convertit CSI en 3200K, pour film tungstène. | 29.8 |
| 747 | Easy White | Développé pour fluorescents, lumière chaude confortable et tons de peau flatteurs. | 31.1 |
| 156 | Chocolate | Réchauffe la lumière et réduit son intensité. | 26.4 |
| 746 | Brown | Sensation trouble et sale sur tungstène. Chocolate plus sombre, moins rose. | 1.5 |
| 025 | Sunset Red | Wash de scène chaud, wash TV studio, effet coucher de soleil. | 26.4 |
| 781 | Terry Red | Rouge ambré fort, fonctionne bien contre des rouges et ambres foncés, en combinaisons wash, et sur cycloramas. | 19.1 |
| 019 | Fire | Rouge/ambre fort. Bon pour effets de feu. | 18.9 |
| 164 | Flame Red | Effets spéciaux, excellent pour le feu. | 18.0 |
| 182 | Light Red | Éclairage d'effet théâtre et télévision, cycloramas. | 11.0 |
| 106 | Primary Red | Effet rouge fort, cycloramas. | 9.3 |
| 026 | Bright Red | Rouge vibrant, bon pour cyclorama. | 8.6 |
| 029 | PLASA Red | Effet feu, comédies musicales, cycloramas. | 5.8 |
| 789 | Blood Red | Effet rouge saturé profond. Utilisé quand un effet rouge vif et intense est requis. | 1.2 |
| 027 | Medium Red | Cyclorama, latéral, rampe. Bon pour le mélange de couleurs. | 3.6 |
| 787 | Marius Red | Beau rouge plein et profond. Couleur feuille de rose. | 1.0 |
| 046 | Dark Magenta | Rose très fort, bon pour contre-jour. | 6.0 |
| 113 | Magenta | Très fort - à utiliser avec précaution sur de petites zones de décor. | 10.9 |
| 148 | Bright Rose | Effets de feu, comédies musicales. | 14.4 |
| 024 | Scarlet | Pantomimes, salles de bal, effets de feu. | 18.7 |
| 166 | Pale Red | Cycloramas. | 25.0 |
| 193 | Rosy Amber | Chaud, émotionnel, romantique. | 36.0 |
| 157 | Pink | Séquences de danse (adoucit les costumes blancs sans affecter les tons de peau). | 36.4 |
| 107 | Light Rose | Bon pour washs généraux. Bon pour poursuites. | 48.0 |
| 109 | Light Salmon | Contre-jour intéressant. | 54.9 |
| 153 | Pale Salmon | Contre-jour combiné à une lumière blanche. | 64.9 |
| 176 | Loving Amber | Contre-jour et zone générale, excellent pour lever de soleil, réchauffe les tons de peau. | 50.2 |
| 790 | Moroccan Pink | Rose naturel riche, bon pour produire des effets de soleil de fin d'après-midi. | 58.1 |
| 004 | Medium Bastard Amber | Accentue naturellement les tons de peau. | 64.1 |

### Pêches, roses pâles, magenta, mauve (p.23-24)

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 151 | Gold Tint | Effet agréable pour l'éclairage théâtral. | 69.4 |
| 152 | Pale Gold | Éclairage intérieur pour accentuer les tons de peau. | 70.7 |
| 154 | Pale Rose | Effet agréable pour l'éclairage théâtral, lumière de lampe. | 73.4 |
| 279 | Eighth Minus Green | Très légère correction magenta. | 86.5 |
| 249 | Quarter Minus Green | Approximativement équivalent à CC075 magenta. | 82.4 |
| 248 | Half Minus Green | Approximativement équivalent à CC15 magenta. | 72.0 |
| 035 | Light Pink | Revues musicales. Wash chaud. | 61.3 |
| 247 | LEE Minus Green | Approximativement équivalent à CC30 magenta. | 57.8 |
| 039 | Pink Carnation | Rose pastel doux et froid, bon pour contre-jour et wash de couleur général. | 60.2 |
| 110 | Middle Rose | Effets agréables pour l'éclairage théâtral. | 47.5 |
| 036 | Medium Pink | Bon pour washs généraux. Latéral. | 45.4 |
| 192 | Flesh Pink | Éclairage clé musical et pantomime. | 34.9 |
| 341 | Plum | Éclairage de décor romantique, atmosphérique. | 19.4 |
| 794 | Pretty 'n Pink | Crée des effets chauds et doux. | 46.8 |
| 111 | Dark Pink | Bon pour cycloramas. | 31.9 |
| 002 | Rose Pink | Wash rose fort pour cycloramas. | 32.7 |
| 328 | Follies Pink | Éclairage de scène dramatique. | 21.6 |
| 128 | Bright Pink | Créé pour le contre-jour, latéral. Bon pour les « spéciaux ». Excellent pour comédies musicales. | 13.7 |
| 793 | Vanity Fair | Rose glamour riche, bon pour occasions spéciales. | 12.0 |
| 332 | Special Rose Pink | Pantomimes, spectacle etc. Wash de scène fort. | 10.5 |
| 795 | Magical Magenta | Riche mélange de rouge et de roses. | 13.1 |
| 048 | Rose Purple | Bon pour simuler le soir. Excellent contre-jour. | 13.9 |
| 049 | Medium Purple | Lueur forte et joyeuse, pour cycloramas et pantomimes. | 4.5 |
| 126 | Mauve | Bon pour contre-jour. Magenta/violet foncé ajoute drame et ambiance. | 4.1 |
| 797 | Deep Purple | Utilisé en spectacle musical pour washs de couleur généraux et éclairage de décor. | 2.3 |

### Frosts teintés (p.24-25) — diffusion + teinte de couleur

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 791 | Moroccan Frost | Adoucit les washs PAR ou flood de grandes zones. Utile pour lumières de salle ; bon pour washs de couleur intérieurs. | 57.2 |
| 749 | Hampshire Rose | Combine le ton chaud de peau 154 avec du Hampshire Frost. | 74.0 |
| 774 | Soft Amber Key 1 | Utilisé pour produire une couleur de lumière clé chaude. | 70.6 |
| 775 | Soft Amber Key 2 | Utilisé pour produire une couleur de lumière clé chaude. | 58.4 |
| 705 | Lily Frost | Adoucit les washs PAR ou flood de grandes zones. Utile pour lumières de salle ; bon wash de couleur pour événements du soir. | 38.5 |
| 720 | Durham Daylight Frost | Adoucit les washs PAR ou flood de grandes zones. Utile pour lumières de salle ; bon pour entrées de lumière naturelle. | 32.3 |
| 717 | Shanklin Frost | 201 avec givrage pour adoucir le faisceau des découpes. | 37.6 |
| 718 | Half Shanklin Frost | 202 avec givrage pour adoucir le faisceau des découpes. | 56.3 |
| 221 | Blue Frost | Utilisé pour effets de lumière douce avec l'ajout de 218. | 42.0 |
| 217 | Blue Diffusion | Comme White Diffusion mais avec l'ajout de 218. | 36.0 |
| 224 | Daylight Blue Frost | Utilisé pour effets de lumière douce avec l'ajout de la correction tungstène 201. | 22.6 |
| 225 | Neutral Density Frost | Utilisé pour effets de lumière douce avec l'ajout de 0.6 Neutral Density. | 25.0 |

### Gamme cosmétique (p.25) — teintes pâles complémentaires à une clé

| N° | Nom | Description / usage | Transmission Y% |
|---|---|---|---|
| 186 | Cosmetic Silver Rose | Teintes pâles complémentaires à l'éclairage clé. | 59.7 |
| 185 | Cosmetic Burgundy | Teintes pâles complémentaires à l'éclairage clé. | 57.7 |
| 187 | Cosmetic Rouge | Teintes pâles complémentaires à l'éclairage clé. | 58.8 |
| 188 | Cosmetic Highlight | Teintes pâles complémentaires à l'éclairage clé. | 66.3 |
| 184 | Cosmetic Peach | Teintes pâles complémentaires à l'éclairage clé. | 58.6 |
| 189 | Cosmetic Silver Moss | Teintes pâles complémentaires à l'éclairage clé. | 71.7 |
| 190 | Cosmetic Emerald | Teintes pâles complémentaires à l'éclairage clé. | 67.1 |
| 191 | Cosmetic Aqua Blue | Teintes pâles complémentaires à l'éclairage clé. | 65.8 |

## Filtres techniques non-couleur (catalogue pp.28-38, non repris en détail)

Présents dans le PDF source si besoin un jour, mais hors sujet pour une macro de
palette couleur : densités neutres (ND, 209-211/298-299), corrections fluorescentes
(219/241-243) et arc (212/213/230/232/236-238) déjà en partie citées ci-dessus quand
elles avaient un nom de teinte, diffusions et frosts neutres (216/250-252/400 etc.),
tissus de grille (430-464), tough spun (214/215/229/261-265), réflecteurs et
protections (269-275/280), polariseur (239), panneaux acryliques (A204-A211).

## Ce qui reste ouvert

- Le complément froid « officiel » du wash 147 Apricot (Lecture 2) : le catalogue ne
  publie pas de paire chaud/froid explicite pour un wash — 161 Slate Blue et 118 Light
  Blue restent des candidats non tranchés, la Lecture 1 (202) reste la mieux sourcée.
- Édition ~2007 : à revérifier auprès de Lee si une teinte précise semble avoir changé
  de nom ou de numéro depuis (le catalogue actuel n'a pas pu être consulté en ligne dans
  cet environnement, réseau bloqué — voir `CLAUDE.md` règle n°1).

# Lee Filters — table de référence théâtre (partielle)

- Confiance : B — pages produit officielles Lee (leefilters.com, leefiltersdirect.com)
  accédées via extraits de résultats de recherche, PAS par téléchargement du catalogue
  complet (bloqué, voir `CLAUDE.md` règle n°1 — testé à nouveau le 2026-08-03 : `WebFetch`
  refuse 403 sur leefilters.com, Rosco, et même Wikipedia dans cet environnement). Chaque
  entrée est individuellement sourcée ; ce n'est PAS une conversion intégrale du catalogue
  Lee, seulement les teintes recherchées pour un besoin de traduction réel (voir
  `PLANNING.md` #34).
- Périmètre : les six teintes demandées lors du test de traduction du 2026-08-03
  (« créer les palettes couleur 1 à 6, Lee, chaud/froid/rouge/vert/bleu/jaune »).
  Pas un catalogue complet — table à étendre au besoin, jamais à deviner en dehors.

## Syntaxe console (rappel, confirmé A — voir `grammar/modele.yaml`)

- Ligne de commande : `Color <bibliothèque>/<numéro>`. Lee = bibliothèque **3**.
  Exemple : `Chan 4 Color 3/195 Enter` (manuel §10, corpus #082).
- OSC direct : chaîne `L<numéro>` (ex. `"L106"` pour Lee 106). Confirmé A par
  `Eos_Integration_via_OSC.md` et `Supported_OSC_Commands.md`.

## Teintes primaires — non ambiguës

| Teinte demandée | Numéro Lee | Nom officiel Lee | Source |
|---|---|---|---|
| Rouge | 106 | Primary Red | [leefilters.com/colour/106-primary-red](https://leefilters.com/colour/106-primary-red/) |
| Vert | 139 | Primary Green | [leefiltersdirect.com/products/139-primary-green](https://leefiltersdirect.com/products/139-primary-green) |
| Bleu | 120 | Deep Blue | [leefilters.com/colour/120-deep-blue](https://leefilters.com/colour/120-deep-blue/) |
| Jaune | 101 | Yellow | [leefilters.com/colour/101-yellow](https://leefilters.com/colour/101-yellow/) |

**Note sur Bleu** : Lee ne nomme aucune teinte « Primary Blue » à proprement parler — 120
Deep Blue est la teinte bleue standard la plus proche d'un bleu primaire dans son
catalogue théâtre. Nom officiel retenu tel quel, pas de renommage inventé.

## Chaud / Froid — AMBIGU, deux lectures possibles, non tranché

« Chaud » et « froid » n'ont pas de réponse unique chez Lee : le mot recouvre deux
usages de conception différents, chacun avec ses propres numéros.

### Lecture 1 — correction de température de couleur (réchauffer/refroidir un projecteur)

| Teinte | Numéro | Nom officiel | Source |
|---|---|---|---|
| Chaud | 205 | 1/2 C.T. Orange | (cité via recherche, page produit Lee) |
| Froid | 202 | 1/2 C.T. Blue | [thomannmusic.com/lee_farbfolie_nr202](https://www.thomannmusic.com/lee_farbfolie_nr202_half_ctblue.htm) |

Paire cohérente par construction : les deux sont explicitement nommées comme correction
CT complémentaire (« Half C.T. » de part et d'autre), pas une paire assemblée par
déduction.

### Lecture 2 — teinte d'ambiance chaude/froide pour une conduite (wash)

| Teinte | Numéro | Nom officiel | Caractère rapporté | Source |
|---|---|---|---|---|
| Chaud | 147 | Apricot | « warm highlight… good for warm front light, complimentary to most skin tones » | [leefilters.com/colour/147-apricot](https://leefilters.com/colour/147-apricot/) |
| Froid | inconnu | — | trois candidats trouvés, aucun confirmé comme le complément standard de 147 : `161` Slate Blue (« moonlight and dusk »), `118` Light Blue (« cool, calming… night effect »), ou `202` (lecture 1). | — |

**Aucune source consultée ne confirme de paire chaud/froid « officielle » pour un wash**
(contrairement à la lecture 1, où 202/205 sont explicitement complémentaires par leur
propre nom). Ne pas assembler 147 avec l'un des trois candidats froids sans confirmation.

## Ce qui reste ouvert

- Lequel des deux usages (correction CT ou wash d'ambiance) correspondait à la demande
  du 2026-08-03 — à confirmer avec l'utilisateur avant de générer la macro finale.
- Le complément froid du wash 147 Apricot, si la lecture 2 est retenue.
- Toute teinte hors de ces six : cette table n'est pas un catalogue, elle ne couvre que
  ce qui a été demandé. Ne pas extrapoler.
- Catalogue Lee complet et officiel : toujours absent du dépôt (`PLANNING.md` #34,
  inchangé sur ce point — cette table ne le referme pas, elle documente un sous-ensemble
  vérifié).

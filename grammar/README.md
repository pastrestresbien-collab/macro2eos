# grammar/ — la grammaire Eos en données exploitables

Traduit la grammaire Eos (jusqu'ici en prose dans
[`../reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md`](../reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md))
en données que du code peut consommer. C'est l'axe A de [`../PLANNING.md`](../PLANNING.md).

## Principe

Le modèle encode le fonctionnement réel d'Eos — **Objet → Action → Cible** (confirmé A,
manuel officiel) — plutôt qu'une grammaire formelle. Raison : la ligne de commande Eos
est modale (`At` ne signifie pas la même chose en Patch qu'en Live) et une partie de sa
sémantique dépend de l'état de la console. Une EBNF forcerait à trancher des points
jamais validés au banc, produisant un artefact d'apparence rigoureuse mais faux sur ses
zones d'ombre.

**`inconnu` est donc une valeur de première classe.** Une combinaison non tranchée est
déclarée comme telle et renvoie au backlog ; le générateur avertit au lieu d'injecter en
aveugle. Chaque validation au banc réel remplit une case.

## Fichiers

| Fichier | Rôle |
|---|---|
| `modele.yaml` | Objets, actions, opérateurs, modificateurs, styles de Fan, contrôle de macro, nuanciers, **matrice de légalité**. Écrit à la main, relisible. Source de vérité. |
| `patrons.yaml` | Recettes éprouvées (couche haute). Un patron n'invente jamais de syntaxe, il pré-remplit une intention connue. |
| `build.py` | Compile le YAML en JSON (`dist/`) et vérifie la cohérence interne. |
| `generateur.py` | IR → chaîne de commande Eos, avec avertissements sur les zones non validées. |
| `test_generateur.py` | Non-régression contre les macros déjà passées au banc de transport. |
| `refus_terrain.yaml` | Journal des rejets réels observés sur console/nomad — preuve de niveau S. |

Le YAML est la source (commentaires possibles, diffs Git lisibles) ; `dist/*.json` est
l'artefact consommé par le code. Le vocabulaire (1155 touches OSC) reste dans
[`../reference/eosKeys.ts`](../reference/eosKeys.ts) et n'est pas dupliqué ici.

## Usage

```bash
python3 grammar/build.py           # compile + vérifie la cohérence
python3 grammar/build.py --check   # vérifie seulement
python3 grammar/generateur.py      # démonstration sur deux exemples
cd grammar && python3 test_generateur.py
```

Dépendance unique : `pyyaml`.

## Refus terrain → matrice de légalité

Un refus de la console est une preuve de niveau S — la plus haute confiance du projet
(voir `../APP.md`, « La console fait autorité »). `refus_terrain.yaml` les accumule au
lieu de les jeter, chacun daté et relié à un numéro `PLANNING.md`.

`build.py` recoupe automatiquement ce journal avec `modele.yaml` : si un refus tranche
un point encore marqué `inconnu`, la compilation affiche un avertissement — le modèle a
pris du retard sur le banc réel, à corriger avant de committer.

Alimentation manuelle pour l'instant (retour verbal en session → ajouté ici). Le jour où
l'app existe, elle journalisera ses propres refus dans le même format.

## Garde-fous appliqués par `build.py`

- Tout terme du vocabulaire — objet, action, modificateur, style de Fan, token de
  contrôle de macro — **doit** porter un niveau de confiance (S/A/B/C/D).
- Toute règle `inconnu` **doit** renvoyer à un numéro de `PLANNING.md`, et **ce numéro
  doit exister** : un renvoi vers un point inexistant donne l'illusion qu'une zone
  d'ombre est suivie quelque part.
- Un style de Fan dont le comportement ou l'arité est `inconnu` **doit** renvoyer au
  backlog, comme une case de la matrice.
- Toute condition Query **doit** porter un champ `osc` explicite — `osc: null` si elle
  n'a pas de touche, jamais l'omission. Et une condition sans touche OSC **doit** renvoyer
  au backlog : elle est hors de portée d'une injection par `/eos/key/`.
- Un mot-clé employé à la fois comme cible de Query et comme action (`Color Palette`)
  **doit** s'écrire pareil des deux côtés — sinon le générateur produirait deux syntaxes
  pour la même chose.
- Tout patron sans confiance établie **doit** lister ses avertissements.
- Un refus terrain qui tranche un point encore `inconnu` déclenche un avertissement.

## Portée actuelle (v0.3)

| Tranche | Contenu |
|---|---|
| v0.1 | sélection channels/groupes, couleur de nuancier, enregistrement de palette |
| v0.2 | **Fan** (§4 de la grammaire consolidée), **cues**, **macros**, **submasters** |
| v0.3 | **Query**, **effets**, **couche d'injection OSC** |
| v0.4 | **contexte d'écran** (modalité) et **auto-terminaison** |
| v0.5 | **Patch** — où `At` s'inverse une seconde fois |
| v0.6 | **Groupes** — un ordre, pas seulement un ensemble |
| v0.7 | **Palettes et Presets** — la référence, et ce qui la casse |

Ce que v0.7 ajoute concrètement :

- **Les quatre familles de palettes** plus le générique `Palette`, avec les trois options
  d'enregistrement `{By Type}`, `{Absolute}`, `{Locked}`.
- **`{Locked}` protège de façon asymétrique** : une palette verrouillée ne peut pas être
  mise à jour directement en Live — seulement par `<channels> Update <cible> Enter` — mais
  elle s'édite **librement en Blind**. La protection est partielle, et le sens de « palette
  verrouillée » en langue naturelle ne le laisse pas deviner.
- **Un preset ne peut pas en référencer un autre.** Contrainte structurelle dure : aucune
  factorisation de preset en preset n'est possible. Une intention du type « le preset B,
  plus deux changements » n'a pas de traduction référencée.
- **Ce qui casse le lien** est encodé : un rappel proportionné (`Int Palette 7 At 50`) le
  conserve, enregistrer la donnée rappelée ailleurs le rompt et fige la valeur en absolu.
- **La règle « sélection = fusion »** se confirme comme une constante de la grammaire :
  déjà vue sur les submasters (§20) et les cues (§12), elle vaut aussi ici. Sans sélection
  un `Record` écrase, avec sélection il fusionne.

Ce que v0.6 avait ajouté :

- **L'ordre des groupes est signifiant.** Un groupe range ses channels dans l'ordre de
  *sélection*, pas dans l'ordre numérique — `10 Thru 2` est légal et donne 10, 9, 8… Cet
  ordre gouverne `Next`/`Last` et l'application des effets, et un `Update` ajoute toujours
  en fin de liste. Réorganisation encodée : `{Insert Before/After}`, `{Reverse}`,
  `{Random}`, `{Reorder}`.
- **Sous-groupes** — `( 1 Thru 4 )`. La frappe console est `Shift & /`, mais ce que porte
  la ligne de commande est une parenthèse, et ce sont les parenthèses qui sont des touches
  OSC nommées. Les quatre cas où un sous-groupe compte pour **un seul channel** sont
  documentés — c'est le même mécanisme que dans le Fan.
- **`Thru Thru` a enfin ses règles**, et elles sont piégeuses : `Group 1.001 Thru Thru
  11.001` crée 10 000 groupes décimaux, mais `… Thru Thru 11.002` en crée 10 **entiers**
  — un chiffre de décimale d'écart change la nature du résultat, sans erreur. Au-delà de
  10 000 cibles, la commande est ignorée en silence.
- **Record ≠ Update sur un groupe** : ré-enregistrer *remplace* (avec confirmation),
  mettre à jour *ajoute* (sans). Deux verbes, deux résultats opposés.

Ce que v0.5 avait ajouté :

- **Patch** — patch par channel et par adresse, univers, dépatch, suppression, courbe,
  preheat, proportion. Plus les règles du patch en masse : `Thru` ne patche en plage que
  des channels (sur des adresses, il crée silencieusement des parts), et le pas d'adresse
  est l'empreinte DMX du fixture, pas +1 — le générateur ne peut donc pas annoncer les
  adresses résultantes.
- **Le piège du mode Format** (voir plus bas) — encodé, signalé, et contourné par la
  seule forme documentée qui y échappe.

Ce que v0.4 avait ajouté :

- **Contexte d'écran** — la table officielle des 37 onglets, `Tab <n> Enter` pour forcer
  le focus, et la polysémie encodée mot par mot. `rendre()` prend maintenant un
  `contexte` (défaut `Live`) et refuse de faire semblant : une commande d'intensité
  générée pendant que Patch a le focus repatche, et le générateur le dit.
- **Auto-terminaison** — `Out`, `Level`, `+%`, `-%` ne prennent pas d'`Enter`. Le
  générateur en ajoutait un systématiquement : c'était un défaut, corrigé. Deux doubles
  appuis changent aussi la commande (`Full Full` et `Sneak Sneak` s'auto-terminent, leur
  forme simple non).

Ce que v0.3 avait ajouté :

- **Query** — 25 conditions, la totalité de la liste du manuel §15. C'est le seul endroit
  du langage Eos où existe une négation : ETC a confirmé par réponse directe qu'il n'y a
  pas de `Not` générique ailleurs. Toute intention de la forme « tout sauf… » passe par
  ici, ou n'a pas de traduction.
- **Effets** — application, retrait, arrêt sélectif ou global, BPM, et la sélection des
  channels d'un effet par Query.
- **Injection OSC** — `rendre_osc()` transforme une commande rendue en paquets prêts à
  partir, `rendre_osc_macro()` déclenche une macro enregistrée, `rendre_osc_touche()`
  couvre ce que la ligne de commande ne sait pas exprimer. Les règles de transport
  confirmées au banc y sont appliquées : `Assert` refusé en ligne de commande, terminaison
  vérifiée, User# dédié recommandé.

Ce que v0.2 avait ajouté :

- **Fan** — 12 styles, dont 7 au comportement documenté (A, exemples chiffrés du manuel
  §8) et 5 dont seule la touche est confirmée. La règle du fan de références est encodée :
  3 références ou plus restent référencées, 2 ou moins sont interpolées en **absolu** et
  perdent la référence. Le générateur avertit — c'est un piège, pas une erreur de syntaxe.
- **Cues** — enregistrement sélectif, Record Only, Update, Go To Cue et ses modificateurs,
  liens et boucles, temps et délais. L'ordre documenté est appliqué : sur un Go To Cue,
  `Time` se pose toujours en dernier.
- **Macros** — les deux voies de création (Learn, éditeur), les tokens de contrôle
  (`{Loop Begin}`, `{Wait}`…), les trois modes, et les règles de génération du projet
  (Foreground par défaut, `Send_String` en dernier, jamais de concaténation).
- **Submasters** — enregistrement, timing de bump montée/dwell/descente, libellé, et les
  bumps `SubDown`/`SubUp` avec leur double réserve : ordre des tokens de confiance C,
  survie ASCII non confirmée.

Le générateur distingue trois sorties, qui n'obéissent pas aux mêmes règles :

| Méthode | Produit | Règles propres |
|---|---|---|
| `rendre()` | lignes de ligne de commande | matrice de légalité, Fan, modificateurs |
| `rendre_macro()` | contenu de macro enveloppé | chaînage en fin, mode, touches non enregistrables en Learn |
| `rendre_osc()` | paquets OSC injectables | terminaison, accolades, `Assert`, User# |

## Deux découvertes de v0.3 qui touchent l'architecture, pas la syntaxe

**Sept conditions Query n'ont pas de touche OSC.** `{Broken Mark}`, `{Marking}`,
`{Up Moves}`, `{Down Moves}`, `{Live Moves}`, `{Dark Moves}` et `{Autoblock}` figurent
dans la liste des softkeys du manuel §15 mais pas dans la liste officielle des touches
OSC du §31, ni dans `eosKeys.ts`. Elles sont atteignables au doigt, pas par
`/eos/key/<nom>`. Reste à savoir si leur nom passe dans une chaîne `/eos/cmd` —
PLANNING #15. Si non, ces sept conditions sont hors de portée de l'app.

**Les accolades ne sont jamais apparues dans une chaîne `/eos/cmd`.** Aucun exemple,
nulle part dans le corpus ni le manuel, ne montre un token softkey entre accolades à
l'intérieur d'une chaîne de ligne de commande OSC. Or **toute** commande générée
portant un style de Fan ou un modificateur en contient. `rendre_osc()` le signale
systématiquement — PLANNING #18. Si les accolades ne passent pas, il faudra décomposer
ces commandes en `/eos/key/<nom>` séparés : c'est la stratégie d'injection qui change,
pas seulement la syntaxe.

Les deux sont le genre de point qu'une grammaire d'apparence rigoureuse aurait masqué.

## v0.5 — `At` s'inverse une seconde fois, et cette fois on ne peut pas le voir

v0.4 avait encodé que `At` vaut un niveau en Live et une adresse en Patch. Le chapitre
§4 en révèle une seconde couche, **à l'intérieur même de Patch** :

```
5 At 100     en mode « by channel »  → patche le CHANNEL 5 à l'ADRESSE 100
5 At 100     en mode « by address »  → patche l'ADRESSE 5 au CHANNEL 100
```

Deux patchs opposés pour une chaîne identique. Et contrairement au contexte d'écran, ce
mode-ci est **hors de portée** : `Format` bascule sans régler, et aucune adresse
`/eos/out/…` ne publie le mode courant — le sous-arbre `/eos/out/get/patch/…` renvoie la
base de patch, pas l'état de l'affichage. Le générateur ne peut donc ni lire ni fixer
l'état dont dépend le sens de ce qu'il écrit.

Une seule parade est documentée : le préfixe `Address <n> At <channel>`, non ambigu quel
que soit le mode. Le générateur l'émet dès qu'il patche par adresse, et signale
systématiquement toute commande de patch par channel — PLANNING #20.

Symétriquement, #21 note que le chapitre §4 n'écrit **jamais** `[Chan]` : notre convention
d'écrire `Chan` partout n'y est pas vérifiée. Si elle tient, c'est la parade symétrique et
elle lève #20 pour de bon.

## Ce que v0.4 corrige, et ce qu'elle ouvre

**Un défaut réel du générateur.** Il ajoutait `Enter` à toutes les commandes. Le manuel
liste explicitement des commandes auto-terminantes — `Out`, `+%`, `-%`, `Level`, actions
de direct select. Un `Enter` de trop sur une commande déjà terminée risque de valider la
ligne suivante. Corrigé, avec les cas du manuel en non-régression.

**Mais la liste d'ETC est incomplète de son propre aveu** : « Some (but **not all**) of
these commands are ». Toute action que le modèle ne marque pas `auto_termine` est donc
*présumée* avoir besoin d'`Enter` — présomption, pas fait établi. C'est PLANNING #19,
à établir commande par commande au banc.

**La modalité est enfin dans le modèle, pas seulement dans la note d'avertissement.**
`At` vaut un niveau en Live et une adresse DMX en Patch — c'est la découverte terrain qui
a justifié d'écarter une grammaire formelle dès le départ. Une EBNF ne peut pas exprimer
qu'un token dépend d'un état extérieur à la phrase. Ici, `rendre(ir, contexte="Patch")`
le vérifie, et `forcer_focus=True` préfixe un `Tab <n> Enter` pour ne plus rien supposer —
au prix de déplacer ce que voit l'opérateur, puisque focus visuel et focus logique sont
le même mécanisme.

## Ce que les tests prouvent — et ce qu'ils ne prouvent pas

`test_generateur.py` couvre deux familles :

1. **Transport** — les deux macros déjà passées au banc `reference/tools/`. Une
   évolution du modèle qui les modifie est une régression.
2. **Manuel** — les exemples chiffrés du manuel officiel v3.2.0, recopiés verbatim
   (§8 Fan, §12 Cues, §15 Query, §16 Playback, §18 Effets, §20 Submasters, §24 Macros).
   Ce sont les seuls cas où l'on sait ce que la console fait vraiment.
3. **OSC** — la forme des paquets injectés, et les règles de transport confirmées au
   banc (`reference/JOURNAL_observations_nomad.md`, confiance S).

Le nombre d'avertissements fait partie de l'attendu : un silence sur une zone d'ombre
serait le vrai bug.

**Rappel** : régénérer une macro déjà transportée ne la valide pas syntaxiquement, et
reproduire un exemple du manuel ne prouve pas que la console l'accepte dans le contexte
généré. Seul un Eos/ETCnomad réel tranche (voir `../PLANNING.md`).

## Différence de forme assumée avec le manuel

Le manuel s'appuie sur les modes implicites du clavier : `[1][Thru][5]` désigne des
channels, `[Record][5]` une cue. Le générateur écrit toujours `Chan` et `Cue` en clair.
Une macro se relit, se réimporte et s'exporte en ASCII — l'implicite y coûte plus cher
qu'il ne rapporte.

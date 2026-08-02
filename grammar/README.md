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

Ce que v0.3 ajoute concrètement :

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

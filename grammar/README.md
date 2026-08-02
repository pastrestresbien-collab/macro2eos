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
| `modele.yaml` | Objets, actions, opérateurs, nuanciers, **matrice de légalité**. Écrit à la main, relisible. Source de vérité. |
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

- Toute règle marquée valide **doit** porter un niveau de confiance (S/A/B/C/D).
- Toute règle `inconnu` **doit** renvoyer à un numéro de `PLANNING.md` — sans quoi une
  zone d'ombre pourrait devenir invisible.
- Tout patron sans confiance établie **doit** lister ses avertissements.

## Portée actuelle (v0.1)

Volontairement étroite : sélection de channels/groupes, application de couleur de
nuancier, enregistrement de palette couleur. C'est le périmètre des deux traductions
déjà éprouvées en transport — le but de cette première tranche est de vérifier que le
modèle les régénère à l'identique avant d'y verser le reste de la grammaire.

**Rappel** : régénérer une macro déjà transportée ne la valide pas syntaxiquement.
Seul un Eos/ETCnomad réel tranche (voir `../PLANNING.md`).

# traducteur/ — du français à l'IR

Prend une phrase en français et produit une **IR** (représentation intermédiaire),
que [`../grammar/generateur.py`](../grammar/README.md) transforme ensuite en commande Eos.
C'est l'axe B de [`../PLANNING.md`](../PLANNING.md).

Ce module n'écrit **jamais** de syntaxe Eos. La syntaxe reste la propriété exclusive du
modèle : le traducteur ne fait que désigner des concepts que le modèle connaît déjà.
Conséquence directe : un mot absent du lexique ne produit pas une commande approximative,
il produit un « je n'ai pas compris ».

## Trois issues, pas deux

C'est le choix de conception central.

| Statut | Sens | Ce que fait l'app |
|---|---|---|
| `compris` | une IR, prête à rendre | affiche la macro et son aperçu |
| `a_preciser` | une ou plusieurs questions | pose la question, relance avec la réponse |
| `incompris` | rien, et les mots non reconnus | demande de reformuler |

**`a_preciser` n'est pas un échec dégradé.** C'est le comportement correct face à une
ambiguïté que seul l'utilisateur peut lever. Sans cette issue, un traducteur n'a d'autre
choix que de deviner — et une couleur devinée produit une macro valide, acceptée par la
console, et la mauvaise teinte sur scène. C'est le pire des trois échecs possibles parce
qu'il est **silencieux** : ni erreur de syntaxe, ni refus, rien à voir dans l'aperçu.

Deux questions sont encodées à ce stade :

- **la portée d'un enregistrement** — `Record Color Palette` capture la sélection
  courante, ou tous les channels non-défaut si rien n'est sélectionné, ce qui n'est
  presque jamais l'intention. Exigence déjà posée dans [`../APP.md`](../APP.md).
- **une couleur ambiguë** — « ambre » a quatre candidats sérieux au catalogue Lee,
  « rose » aussi, avec en prime un piège de traduction (le « Rose » de Lee n'est pas le
  rose français, qui se dit « Pink »).

## Pourquoi aucune IA à l'exécution

Décision prise au démarrage de l'axe B (2026-08-06), pour trois raisons.

1. **Le réseau.** Dans le théâtre, le téléphone est sur le Wi-Fi de la console. Rien ne
   garantit un accès Internet. Un traducteur qui dépend d'un serveur distant tombe
   exactement quand on en a besoin.
2. **« N'invente rien »** est la règle n°1 du dépôt. Un modèle de langue invente par
   construction : il peut produire une syntaxe plausible et inexistante. Un lexique ne
   peut sortir que ce qu'on y a mis, et chaque entrée est sourcée.
3. **C'est réversible.** L'IR est le contrat. Le jour où une couche de compréhension plus
   souple serait souhaitable, elle se branche devant et émet la même IR, sans que rien en
   aval ne bouge. Commencer déterministe ne ferme aucune porte.

## Ce que le traducteur n'essaie pas de faire

Il **n'analyse pas la grammaire de la phrase**. Il repère des mots et remplit des
créneaux, insensible à l'ordre. C'est délibéré : le français du métier est télégraphique
(« palettes couleur 1 à 6, lee, chaud froid r v b j »), et la saisie vocale prévue plus
tard produira pire encore — homophones, ponctuation absente, nombres en toutes lettres.
Une analyse syntaxique casserait sur ces entrées ; le remplissage de créneaux les encaisse.

## La tolérance aux fautes est restreinte au créneau

Jamais globale, et le cas réel qui l'impose mérite d'être connu.

L'utilisateur a écrit **« chang »** pour « chaud ». Cherché dans tout le lexique, le plus
proche voisin de « chang » n'est pas « chaud » (distance 2) mais **« chan »** (distance
1) — le mot-clé Eos pour un circuit. Une correction globale aurait donc traduit une
couleur en sélection de circuits, silencieusement.

Restreinte à la liste des couleurs, où « chan » n'est pas candidat, « chaud » gagne seul.
**C'est le créneau en cours de remplissage qui sert de désambiguïsateur.** Et deux
candidats à égalité de distance ne sont jamais départagés au hasard : c'est une question.

## Fichiers

| Fichier | Rôle |
|---|---|
| `lexique.yaml` | Mots français → concepts du modèle. Aucune syntaxe Eos. Chaque entrée porte sa `source` ou son `choix`. |
| `traducteur.py` | Normalisation, détection d'intention, remplissage de créneaux, questions. |
| `test_traducteur.py` | Non-régression, ancrée sur la demande réelle de l'utilisateur. |

```bash
cd traducteur && python3 traducteur.py        # démonstration sur la phrase réelle
cd traducteur && python3 test_traducteur.py   # non-régression
```

Dépendance unique : `pyyaml`.

## Le cas d'ancrage

La demande réelle de l'utilisateur, recopiée **verbatim dans les tests**, fautes de frappe
comprises :

> `créer les palette de couleur 1 a 6 avec les références lee, chang froid r v b j`

« palette » au singulier, « 1 a 6 » sans accent, « chang » pour « chaud », initiales pour
les quatre dernières couleurs. Le test ne nettoie pas cette phrase : c'est précisément ce
bruit-là que le traducteur doit encaisser. Un second cas rejoue la même demande écrite
proprement et **exige un résultat identique** — si les deux divergent, la tolérance au
bruit est illusoire.

Le résultat, après réponse à la question de portée, est exactement la macro qui avait été
écrite à la main en session avant que ce module existe. Elle sert donc doublement de
non-régression.

## Portée actuelle (v0.1)

| Intention | Exemple |
|---|---|
| créer des palettes de couleur | « créer les palettes couleur 1 à 6 en lee, chaud froid r v b j » |
| colorer une sélection | « circuits 10 à 20 en lee 195 », « groupe 5 en bleu » |
| régler une intensité | « circuits 1 à 5 à 50 % », « circuits 1 à 5 de 10 à 50 % » |

Neuf couleurs nommées, deux couleurs ambiguës déclarées comme telles, un nuancier (Lee).

**Ce qui n'est pas couvert** et devra l'être : cues, groupes, submasters, effets, Query,
macros — soit la majeure partie des 79 actions du modèle. Le lexique se remplit par
tranches, comme le modèle l'a été.

## Deux règles de peuplement du lexique

**Une couleur n'entre que si le rattachement est évident** — le nom Lee est le mot
français, sa traduction directe, ou une décision déjà prise et documentée. Le catalogue
compte environ 230 teintes et la plupart des mots français courants ont plusieurs
candidats sérieux. Dans ce cas la bonne réponse n'est pas de choisir, c'est de déclarer
`ambigu` et de laisser la question se poser.

**Jamais de zéro de tête sur un numéro de gel.** YAML 1.1 lit `020` comme de l'octal : la
valeur chargée vaut 16, pas 20. Le piège est silencieux — aucune erreur, un numéro
parfaitement plausible — et produirait `Color 3/016` sur scène. Rencontré à l'écriture de
ce lexique, corrigé, et désormais vérifié par un test qui contrôle les numéros un par un
et pas seulement le fait qu'une question soit posée.

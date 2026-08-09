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

## Portée actuelle (v0.6)

| Intention | Exemple |
|---|---|
| créer des palettes de couleur | « créer les palettes couleur 1 à 6 en lee, chaud froid r v b j » |
| colorer une sélection | « circuits 10 à 20 en lee 195 », « groupe 5 en bleu », « groupe 1 à 5 en gel 205 » |
| régler une intensité | « circuits 1 à 5 à 50 % », « circuits 1 à 5 de 10 à 50 % » |
| enregistrer une cue (sélectif) | « enregistrer les circuits 1 à 5 dans la cue 4 » |
| aller à une cue | « aller à la cue 5 », « va au noir », « va à la suivante » |
| enregistrer un submaster (sélectif) | « enregistrer les circuits 6 à 10 dans le sub 3 » |
| bump d'un submaster (haut/bas) | « bump haut le sub 5 », « bump bas sub 12 » |
| appliquer un effet à une sélection | « lance l'effet 1 sur les circuits 1 à 10 » |
| arrêter un effet | « arrête l'effet 3 », « arrête tous les effets » |
| enregistrer un preset (sélectif) | « enregistrer les circuits 1 à 5 dans le preset 2 » |
| rappeler un preset sur une sélection | « rappelle le preset 2 sur les circuits 1 à 5 » |
| lancer une macro | « lance la macro 5 » |
| sélectionner via Query (Is In / Isn't In) | « sélectionne ce qui est dans la palette couleur 5 », « ... n'est pas dans le preset 3 » |
| poser un drapeau Mark (cue ou channels) | « marque la cue 10 », « marque les circuits 1 à 5 » |
| parquer un circuit ou groupe à un niveau | « parque le circuit 2 à 50 % » |
| assert (cue, circuit ou groupe) | « assert la cue 5 », « assert le groupe 6 » |

Neuf couleurs nommées, deux couleurs ambiguës déclarées comme telles, un nuancier (Lee),
quatre cibles symboliques de cue (Out/Next/Last/Home).

**Hypothèses — un champ supposé n'est ni un blocage ni un silence.** Quand le traducteur
choisit une valeur sans marqueur explicite dans la phrase (aujourd'hui : le nuancier, Lee
étant le seul connu), il ne pose pas de question bloquante ni ne devine en silence — il
répond `compris` mais marque le champ comme hypothèse (`Traduction.hypotheses`), avec une
question de correction toute prête. Décidé avec l'utilisateur le 2026-08-07 ; voir
`Hypothese` dans `traducteur.py`. Corriger vers une valeur non sourcée (un fabricant hors
corpus, par exemple) ne devine jamais une correspondance : ça redevient `incompris` avec
l'explication.

**Sub n'est délibérément pas un objet de sélection générique.** `grammar/modele.yaml`
interdit `Sub + intensite` au niveau de confiance le plus haut du projet (S : « le
pilotage de niveau d'un sub passe par le fader ou les bumps, pas par `At` »). `Sub` vit
dans un index séparé (`objets_cible`, distinct de `objets`) consulté seulement par
`enregistrer_sub` et `bump_sub` — jamais par `regler_intensite` ou `colorer_selection`.
Une phrase comme « sub 3 à 50 % » ne peut donc structurellement pas produire la commande
qu'on sait déjà fausse ; elle reste `incompris`, vérifié par test.

**Bump de submaster : les noms des touches sont sourcés, pas leur effet.** `SubUp`/
`SubDown` existent bel et bien (`eosKeys.ts`, confiance A sur l'existence, B sur l'ordre
des tokens — corpus #026), mais aucune source du dépôt ne documente ce que « haut »/« bas »
font concrètement sur le plateau. Le traducteur ne l'explique donc pas et pose une
question plutôt que de choisir quand la phrase ne précise pas la direction.

**Effets : la portée « poser un arrêt sur une sélection » n'est pas couverte.** Le modèle
documente trois portées pour `Stop Effect` (tout, un effet précis, ou une instruction posée
sur des channels), mais distinguer dans une phrase un numéro d'effet d'un numéro de circuit
demanderait un marqueur qui n'existe pas de façon fiable — laissé de côté plutôt que deviné.

**Mark : seule la forme la plus simple des deux usages référencés est couverte.**
`<channels> Mark Enter` (désigner la cue source des mouvements NP) et `Cue <n> Mark Enter`
(poser le drapeau M) partagent la même touche et le même handler — c'est `self._objet` qui
choisit Chan/Group/Cue selon le mot présent, sans chercher à distinguer les deux usages.
`Mark Cue <n>` (marquer vers une cue antérieure) et `Mark Earliest` restent hors périmètre.
Le générateur, pas le traducteur, porte l'avertissement sur AutoMark vs marques référencées
(PLANNING #24) : un réglage de Setup sans commande de lecture, donc jamais tranchable ici.

**Park : un seul circuit ou groupe, jamais une plage — restriction volontaire, pas un
oubli.** Le manuel documente une forme bascule (`<chan> At Park Enter`, dépend d'un état
console jamais généré ici) et une forme absolue déterministe (`<chan> At <n> Park Enter`),
seule couverte. Se limiter à un seul circuit élimine à la racine une ambiguïté réelle :
« circuit 4 à 50 % » ne contient qu'un seul « à », qui sert autant de séparateur de plage
que de préposition introduisant le niveau — sans un second « à » pour trancher (le cas que
`regler_intensite` sait résoudre), `self._plage` lirait « 4 à 50 » comme une plage de
circuits. L'échelle (`At / <pourcentage> Park`) et le parquage d'adresse restent hors
périmètre.

**Assert : une cue, un circuit ou un groupe — jamais un submaster, jamais une cue list
explicite.** `Sub` n'existe pas dans `self._objets` (même garde-fou que pour
`enregistrer_sub`/`bump_sub`/Park) : une phrase « assert le sub 3 » ne trouve donc aucun
objet et reste `incompris`, cohérent avec le constat de banc (S) que `Sub <n> Assert`
échoue en erreur de syntaxe. La notation `Cue x/y` (assert sur une cue list précise,
manuel §14) reste hors périmètre — les cue lists multiples ne sont pas modélisées dans le
traducteur dans son ensemble.

**Ce qui n'est pas couvert** et devra l'être : cue lists multiples, cues multipart, patch,
filtres, courbes, snapshots, magic sheets, show control, groupes (au-delà d'une sélection
simple), contrôle partitionné — la majeure partie des 79 actions du modèle. Le lexique se
remplit par tranches, comme le modèle l'a été.

**Query : périmètre volontairement restreint, pas une couverture complète.** Seules les
cibles Color Palette, Preset et Cue sont couvertes — les familles déjà modélisées ailleurs
dans le traducteur. `Group` et `Sub` existent comme cibles de Query dans le modèle mais
restent hors périmètre : `Query {Is In} Group 2` et `Group 2 Enter` sont deux mécanismes
distincts, et le risque de confusion entre les deux n'a pas été tranché. Une seule
condition par requête ; les Query composées (`{Can Be} X {Isn't In} Y`, manuel §15)
restent hors périmètre.

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

## La tolérance aux fautes n'a pas le droit de vote sur l'intention

Second piège réel, trouvé à l'ajout des cues (v0.1, même session) : le mot **« groupe »**
est à distance d'édition 2 de **« rouge »** — dans la marge normalement tolérée pour un
mot de cette longueur. Le joker `@couleurs`, qui sert à détecter l'intention « colorer une
sélection » sans recopier tous les noms de couleurs dans les déclencheurs, utilisait cette
même tolérance. Résultat : « enregistrer le groupe 2 dans la cue 5 » se faisait détourner
vers l'intention couleur, avant même d'arriver au remplissage des créneaux.

Ce n'est pas la même classe d'erreur que « chang »/« chan » — ici la tolérance ne se
trompait pas de valeur *dans* un créneau, elle changeait l'intention *elle-même*, donc
tout le reste de l'analyse avec elle. **Correction : la détection d'intention n'utilise
plus jamais la tolérance aux fautes, seulement des correspondances exactes.** La
tolérance reste réservée au remplissage d'un créneau déjà choisi, où le champ restreint
des candidats la rend sûre — c'est tout l'intérêt du principe « restreint au créneau »
énoncé plus haut, ici appliqué un cran plus tôt qu'attendu.

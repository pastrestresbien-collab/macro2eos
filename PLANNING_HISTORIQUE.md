# PLANNING — journal historique

Journal chronologique détaillé, daté, des tranches de travail (axes A et B) et des
points de backlog résolus. Séparé de [`PLANNING.md`](PLANNING.md) le 2026-08-07 pour
que ce dernier reste léger à relire en début de session — **rien n'a été supprimé**,
seulement déplacé, conformément à la règle du projet (« un point résolu n'est jamais
supprimé »).

**Ce fichier n'est pas à relire systématiquement.** Il sert de trace d'audit et de
justification détaillée — à consulter quand on a besoin de comprendre *pourquoi* une
décision a été prise, pas pour suivre l'état courant du projet (voir `PLANNING.md` pour
ça). Même logique que la règle n°2 de `CLAUDE.md` sur les PDF sources : une archive
qu'on rouvre sur besoin précis, pas à chaque session.

---

## Axe A — structurer la grammaire : le journal des tranches (v0.1 → v0.16)

État courant, chiffres à jour et pointeurs : voir `PLANNING.md` et
[`grammar/README.md`](grammar/README.md). Ce qui suit est le récit tranche par tranche
qui a mené au modèle actuel (79 actions, 164 règles de légalité), conservé pour le
raisonnement et les sources qu'il documente.

**Approche retenue** (2026-08-01) : modèle typé Objet → Action → Cible + matrice de
légalité, plutôt qu'une grammaire formelle (EBNF). La ligne de commande Eos est modale
et dépendante de l'état console ; une EBNF forcerait à trancher des points non validés
au banc. Ici, `inconnu` est une valeur de première classe et renvoie au backlog.

**Fait — v0.1**, voir [`grammar/`](grammar/README.md) : modèle, patrons, compilateur
YAML→JSON avec garde-fous de cohérence, générateur IR→commande avec avertissements, et
test de non-régression. Périmètre : sélection channels/groupes + couleur de nuancier +
record de palette. Les deux macros déjà éprouvées en transport sont régénérées à
l'identique, avec signalement automatique des points 4 et 5 du backlog.

**Fait — v0.2 (2026-08-02)** : extension au Fan (§4 de la grammaire consolidée), aux
cues, aux macros et aux submasters. 20 actions, 10 modificateurs, 12 styles de Fan, 6
tokens de contrôle de macro, 49 règles de légalité. Le générateur distingue désormais
une **ligne de commande** d'un **contenu de macro**, qui n'obéissent pas aux mêmes
règles. Les 28 cas de non-régression comprennent les exemples chiffrés du manuel
officiel recopiés verbatim (§8, §12, §16, §20, §24) — la seule référence disponible sur
ce que la console fait réellement, à défaut de banc.

Deux zones d'ombre nouvelles sont sorties de cette tranche et rejoignent le backlog :
le nom réel de la softkey `{Mirror}` (#13) et le non-déterminisme de `Go To Cue` en
macro (#14). `build.py` vérifie maintenant que tout renvoi au backlog désigne un point
qui existe vraiment.

**Fait — v0.3 (2026-08-02)** : Query, effets, et la couche d'injection OSC. 26 actions,
25 conditions Query, 65 règles de légalité, 46 cas de non-régression. Le générateur
produit maintenant trois sorties distinctes — ligne de commande, contenu de macro,
paquets OSC — chacune avec ses règles propres.

Cette tranche a fait remonter deux points qui touchent l'architecture, pas la syntaxe :

- **Sept conditions Query n'ont pas de touche OSC** (#15). Atteignables au doigt, pas
  par `/eos/key/`. Si leur nom ne passe pas non plus dans une chaîne `/eos/cmd`, elles
  sont hors de portée de l'app — et le traducteur doit le dire au lieu de produire une
  commande muette.
- **Les accolades n'ont jamais été vues dans une chaîne `/eos/cmd`** (#18). Or toute
  commande portant un style de Fan ou un modificateur en contient. Si elles ne passent
  pas, il faut décomposer en `/eos/key/<nom>` séparés : c'est la stratégie d'injection
  qui change.

Plus deux points de nommage : la contradiction `select_active` / `select active` entre
deux sources ETC (#16), et `{Select Last}` après une Query composée (#17), qui
conditionne la stratégie de génération en masse n° 2 appliquée à une sélection
conditionnelle.

**Fait — v0.4 (2026-08-02)** : contexte d'écran et terminaison. La modalité entre dans
le modèle au lieu de rester une note d'avertissement : table officielle des 37 onglets,
`Tab <n> Enter` pour forcer le focus, polysémie encodée mot par mot (`At` vaut un niveau
en Live et une adresse DMX en Patch — cinq sens documentés pour `/`). `rendre()` prend un
`contexte` et le vérifie.

Cette tranche a corrigé **un défaut réel du générateur** : il ajoutait `Enter` à toutes
les commandes, alors que `Out`, `Level`, `+%` et `-%` s'auto-terminent, et qu'un `Enter`
de trop risque de valider la ligne suivante. Corrigé — mais la liste d'ETC est incomplète
de son propre aveu, d'où le nouveau point #19.

**Fait — v0.5 (2026-08-02)** : Patch §4. 44 actions, 90 règles de légalité, 60 cas de
non-régression.

La tranche a mis au jour une **seconde inversion de `At`**, à l'intérieur même de Patch :
`5 At 100` patche le channel 5 à l'adresse 100 en mode par channel, et l'adresse 5 au
channel 100 en mode par adresse. Contrairement au contexte d'écran, ce mode est hors de
portée du générateur — `Format` bascule sans régler, et rien ne publie l'état courant
(#20). La seule parade documentée est le préfixe `Address <n> At <channel>`, que le
générateur émet désormais pour tout patch par adresse.

Deux règles de patch en masse valent aussi d'être retenues : `Thru` ne patche en plage
que des channels — sur des adresses il crée silencieusement des **parts** au lieu
d'échouer — et le pas d'adresse est l'empreinte DMX du fixture, pas +1, donc le
générateur ne peut pas annoncer les adresses résultantes sans connaître le patch.

**Fait — v0.6 (2026-08-02)** : Groups §7 et sous-groupes. 52 actions, 104 règles de
légalité, 67 cas de non-régression.

Un groupe n'est pas seulement un ensemble : il porte un **ordre**, celui de la sélection
au moment de l'enregistrement. `10 Thru 2` est légal et range 10, 9, 8… Cet ordre
gouverne `Next`/`Last` et l'application des effets, et un `Update` ajoute toujours en fin
de liste. Les sous-groupes s'écrivent `( 1 Thru 4 )` — la frappe est `Shift & /` mais ce
sont les parenthèses qui sont des touches OSC nommées — et comptent pour un seul channel
dans quatre cas documentés, dont le Fan.

`Thru Thru` a enfin ses règles, et elles sont piégeuses : un chiffre de décimale d'écart
entre début et fin change la nature du résultat (décimales ou entiers) sans erreur, et
au-delà de 10 000 cibles la commande est ignorée en silence.

Nouveau point #22 : le manuel §7 se contredit sur `{Insert Before}` / `{Insert After}` —
sa liste de softkeys dit l'inverse de ses propres exemples. Le modèle retient les
exemples, mais c'est un arbitrage.

**Fait — v0.7 (2026-08-03)** : Palettes §10 et Presets §11. 60 actions, 122 règles de
légalité, 75 cas de non-régression.

Deux contraintes structurelles en sont sorties. **Un preset ne peut pas en référencer un
autre** (A, énoncé tel quel par le manuel) : aucune factorisation de preset en preset
n'est possible, donc une intention du type « le preset B, plus deux changements » n'a
pas de traduction référencée. Et **`{Locked}` protège de façon asymétrique** : une
palette verrouillée ne peut pas être mise à jour en Live, mais s'édite librement en
Blind — ce que « palette verrouillée » ne laisse pas deviner en langue naturelle.

La règle « sélection = fusion » se confirme comme une **constante de la grammaire** :
déjà relevée sur les submasters (§20) et les cues (§12), elle vaut aussi pour les
palettes. Sans sélection un `Record` écrase, avec sélection il fusionne — même mot,
deux résultats.

**Fait — v0.8 (2026-08-03)** : Mark §9. 64 actions, 130 règles de légalité, 79 cas de
non-régression.

AutoMark et marques référencées s'excluent mutuellement, et le choix est un réglage de
Setup global et rétroactif, sans commande de lecture documentée (#24). C'est le
**troisième état invisible** rencontré, après le mode de patch (#20) et le couple
Q Only/Track : à ce stade, « le sens d'une commande dépend d'un état que le générateur ne
peut pas lire » n'est plus un accident, c'est une caractéristique de la plateforme — et
l'argument le plus solide en faveur de la validation utilisateur avant envoi.

Deux points opérationnels : les channels à marquer sont **obligatoires** (« Eos will not
assume all automated fixtures apply to any given mark »), donc une intention « marque les
asservis » n'a pas de traduction ; et `Mark Cue <n>` supprime silencieusement tout
mouvement NP intermédiaire dans des cues que l'utilisateur n'a pas nommées.

Nouveau #23 : `{High Priority}` / `{Low Priority}` sont documentés au §9 mais absents de
la liste OSC officielle — même classe de problème que les sept conditions Query de #15.

**Fait — v0.9 (2026-08-03)** : cues multipart §17. 66 actions, 135 règles de légalité,
84 cas de non-régression.

La trouvaille de cette tranche dépasse le chapitre : **en Blind, les éditions prennent
effet immédiatement**, sans `Record` ni `Update`. Le manuel le répète en §17 (CAUTION),
§20, §18 et §10. Pour l'app, cela invalide un schéma qu'on aurait pu croire acquis : « je
prépare, l'utilisateur relit, puis j'envoie » n'existe pas en Blind — la première commande
envoyée est déjà appliquée. Toute validation doit précéder l'envoi, jamais s'intercaler
dans une séquence. Cela explique aussi pourquoi une palette `{Locked}` reste modifiable en
Blind : la protection ne porte que sur Live.

Deuxième apport, plus technique : **un channel ne peut recevoir qu'une seule instruction
dans une cue multipart**, et c'est vérifiable statiquement. Le générateur détecte
désormais deux affectations du même channel à des parts différentes. C'est la première
contrainte du modèle qui porte sur la *structure de l'IR* et non sur un couple
objet/action — une piste à réutiliser pour d'autres règles.

**Fait — v0.10 (2026-08-03)** : cue lists multiples §14 et Assert. 67 actions, 142 règles
de légalité, 90 cas de non-régression.

Cette tranche a mis au jour **une contradiction entre deux sources du projet**, et elle
est instructive. `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` §9 affirme, sur la foi du
journal terrain (S) : « Assert n'a pas de mot-clé de ligne de commande ». Le manuel §14
(A) documente pourtant quatre niveaux d'assert en ligne de commande. Les deux disent vrai
sur des objets différents : le constat de banc portait sur un assert de **submaster**, qui
échoue bien. C'est la généralisation qui était fautive, pas l'observation — voir #26.

C'est le premier cas où une source S s'est révélée **sur-généralisée** plutôt qu'erronée.
Leçon méthodologique : une observation de banc vaut pour l'objet observé, jamais pour la
famille entière. Les constats S futurs devraient être enregistrés avec leur portée exacte.

Deux autres apports : un **sixième sens du `/`** (`Cue 2/ Assert` asserte la liste entière,
`Cue 2/5 Assert` une seule cue), et un **quatrième état implicite** (#25) — la liste
d'enregistrement dépend de la « cue sélectionnée », que le générateur ne peut pas lire ;
il nomme donc désormais la liste explicitement, même la liste 1.

**Fait — v0.11 (2026-08-03)** : Park §19 et Filtres §13. 71 actions, 149 règles de
légalité, 94 cas de non-régression, 21 zones non tranchées suivies.

Le point majeur est le **cinquième état implicite**, et il diffère des quatre premiers.
Le mode de patch (#20), le mode de marquage (#24), la cue list courante (#25) et le couple
Q Only/Track changent le *sens* d'une commande. L'état des filtres, lui, change ce qu'elle
*produit* : `Record Cue 5 Enter` enregistre un contenu différent selon un état que rien ne
publie, sans que son texte change d'un caractère (#28). Et poser un filtre passe par un
accord maintenu dont la reproduction en OSC est plausible mais jamais observée (#27).

Park apporte deux pièges de plus : la touche `Park` s'inverse dans l'écran Park (elle sert
à déparquer, le parquage y étant implicite), et `<chan> At Park` sans valeur est un
bascule — le générateur exige donc une valeur. Enfin, une valeur parquée est exclue de
tous les record targets : une macro qui règle puis enregistre un channel parqué produit
une cue correcte sur le papier et un plateau inchangé, sans erreur remontée.

**Fait — v0.12 (2026-08-03)** : Courbes §22, Snapshots §23, et la saisie des niveaux.
75 actions, 156 règles de légalité, 100 cas de non-régression.

La trouvaille majeure ne vient pas des chapitres visés mais d'une vérification faite en
passant : **`At 5` vaut 50 %**, pas 5 %. Le manuel §6 l'établit par cinq occurrences de sa
notation `<0>`, et le §22 le reconfirme sur les points de courbe. C'est le seul piège
rencontré dans tout ce travail qui transforme une commande parfaitement valide en résultat
faux d'un **facteur dix**, en silence. Le générateur refuse désormais d'émettre un niveau
à un chiffre. Comment exprimer réellement 5 % reste ouvert (#29) — aucun exemple du manuel
ne descend sous 10 %. *(Résolu le 2026-08-03, voir « Backlog résolu » plus bas.)*

Deux autres apports. L'**idiome `At Enter`** est encodé comme idiome général plutôt que
redécouvert chapitre par chapitre : six occurrences dans cinq chapitres où `At` suivi
d'`Enter` annule l'instruction courante. Et **supprimer une courbe préprogrammée ne la
supprime pas** — elle revient à son état d'origine, donc une confirmation utilisateur
formulée « supprimer la courbe 901 ? » serait trompeuse.

**Fait — v0.13 (2026-08-03)** : Magic Sheets §25 et show control §31. 158 règles de
légalité, 100 cas de non-régression.

Trois apports. Le champ « Command » d'un objet de Magic Sheet porte un **mini-langage de
préfixes** (`event:`, `macro:`, `udp:`, `local:`, `<U2>`, OSC brut, cumulables) qui
n'existe nulle part ailleurs dans la grammaire — confirmé A par le manuel, là où le
corpus ne l'avait qu'en C, et avec une forme différente de celle que le corpus décrivait
(#30).

Show control n'accepte que **trois actions** : exécuter une cue, piloter un submaster,
exécuter une macro. C'est un argument de plus pour que le traducteur produise des macros
plutôt que des lignes isolées — la macro est le seul objet qu'un évènement sait exécuter.
Le manuel garantit au passage une **sérialisation** : une macro déclenchée avant la fin
d'une autre attend son tour. Cela atténue une partie des craintes de #2 et #3, mais
l'énoncé vaut pour un déclenchement par évènement, pas par OSC direct — à ne pas
généraliser.

Enfin, les **numéros d'évènement ne sont pas stables** (#31) : ils se renumérotent pour
rester chronologiques. Contrairement aux cues ou aux macros, ce n'est pas un identifiant
qu'un traducteur peut mémoriser.

**Fait — v0.14 (2026-08-03)** : export ASCII §3. Tranche à **résultat négatif**, et c'est
son intérêt.

Aucune source du dépôt ne décrit la structure du fichier `.asc`. Le manuel §3 ne documente
que le chemin d'import/export, et prévient en CAUTION que « not all data (such as effects
and **macros**) may be imported » — confirmant au niveau A ce que le corpus #027 ne
rapportait qu'en C sur un cas particulier. **Conséquence sur l'objectif du projet** : tant
que la spécification n'est pas au dépôt, « injection OSC ou ASCII » doit se lire
« injection OSC » (#32). C'est le seul point du backlog qui ne se tranche pas au banc mais
par l'acquisition d'un document.

Deux points restent actionnables et sont encodés : l'import **écrase par défaut**
(`{Merge Data?}` fusionne — le défaut est destructeur, à signaler dans toute procédure
proposée), et l'export n'est **pas générable**, c'est une navigation dans le Browser.

**Fait — v0.15 (2026-08-03)** : relecture d'ensemble. Pas d'ajout de couverture, mais
un audit du modèle après treize tranches écrites l'une après l'autre.

Un vrai doublon trouvé et corrigé : `patch_courbe` (v0.5) et `appliquer_courbe` (v0.12)
écrivaient `Curve <n>` à l'identique — le découpage en tranches avait produit deux actions
pour un même geste documenté au §4 et au §22. Fusionnées.

Trois autres constats se sont révélés **corrects et non des défauts**, et ont été
documentés plutôt que « corrigés » : les homonymies de `At` (quatre actions), `Park` et
`Time` sont la polysémie d'Eos elle-même, désormais déclarées dans `homonymies_assumees` ;
et les deux règles où une confiance S dépasse celle de l'action valident un **refus**
observé au banc, dont la confiance est indépendante de la documentation de l'action.

L'audit est devenu permanent : `build.py` refuse maintenant toute homonymie non déclarée,
toute règle plus confiante que son action (hors refus), toute action absente de la matrice
et toute action sans `source`. Les quatre contrôles ont été vérifiés en les faisant échouer
volontairement.

**Fait — v0.16 (2026-08-03)** : Contrôle partitionné §28. 79 actions, 164 règles de
légalité, 107 cas de non-régression.

Choisi pour sa pertinence directe : macro2eos s'ajoute comme un programmeur de plus à côté
d'un opérateur humain, et c'est précisément ce que ce chapitre régit. Deux apports notables.

**Une confirmation croisée entre deux chapitres indépendants.** Le §19 (Park, encodé en
v0.11) affirmait que le parquage échappe au contrôle par partition. Le §28 le confirme de
son côté, indépendamment : « Park instructions are not subject to partition control ». Deux
chapitres, une même règle établie séparément — le niveau de confiance s'en trouve renforcé,
pas simplement additionné.

**Une inversion apparente de la règle « sélection = fusion » établie en v0.7.** Pour les
record targets (Record Cue/Sub/Palette), une sélection MERGE dans une cible existante ; sans
sélection, on écrase. Pour l'assignation de channels à une partition, c'est l'inverse : une
liste de channels nue (`1 Thru 96 Enter`) REMPLACE le contenu de la partition, et il faut un
`+` explicite pour ajouter. Ce n'est pas une contradiction du modèle — ce sont deux verbes
distincts (« enregistrer des données » contre « définir une appartenance ») qui ne partagent
que la surface syntaxique — mais un traducteur NL qui généraliserait naïvement la règle de
v0.7 à toute commande portant une sélection se tromperait précisément ici. Documenté comme
mise en garde explicite dans le modèle plutôt que laissé à la déduction.

Au passage, l'idiome `<attribut nu> Enter` = effacer l'attribut (documenté en v0.12 pour
`At Enter`) se généralise une fois de plus : `Cue n/ Partition Enter` retire l'assignation
de partition d'une cue list, sans `At` cette fois. Ce n'est donc pas spécifique à `At` : la
forme générale est « un attribut suivi d'`Enter` sans valeur efface l'attribut ».

### Bilan de la campagne d'extension (v0.1 → v0.16) — v0.15 clôturée le 3 août, prolongée le même jour à la demande de l'utilisateur

Seize tranches, du 1ᵉʳ au 3 août 2026, plus une résolution le même jour. Le modèle est
passé de 2 objets et 3 actions à **9 objets, 79 actions, 10 modificateurs, 164 règles de
légalité**, avec **110 cas de non-régression** dont la majorité sont des exemples chiffrés
du manuel officiel recopiés verbatim. Le backlog est passé de 12 à **33 points**, dont 21
ouverts par ce travail. **25 restent encodés dans le modèle** et déclenchent un
avertissement du générateur — ils ne dorment pas dans un fichier, ils parlent à l'usage.
**Un point (#29) est résolu** : c'est la première fois qu'une confirmation réelle, en
session, referme une zone d'ombre plutôt que d'en ouvrir une — la preuve que le mécanisme
fonctionne dans les deux sens.

#### Ce que la couverture atteint

Sélection, Fan, cues (simples, multipart, listes multiples), macros, submasters, Query,
effets, palettes, presets, groupes, patch, mark, park, filtres, courbes, snapshots, magic
sheets, show control, contrôle partitionné, contexte d'écran, terminaison, et la couche
d'injection OSC. L'export ASCII a été instruit et s'est révélé non modélisable faute de
spécification (#32). **Reste hors périmètre** : Augment3d, le pixel mapping, le serveur
média virtuel et le multi-console.

#### Le résultat le plus important n'est pas la couverture

C'est la découverte, chapitre après chapitre, que **le sens ou le résultat d'une commande
Eos dépend souvent d'un état que rien ne publie**. Six cas recensés :

| État | Effet | Lisible ? |
|---|---|---|
| Mode de patch By Channel / By Address (#20) | inverse le sens de `At` | non |
| `Q Only` / `Track` | inverse le sens de la touche | non |
| AutoMark ou marques référencées (#24) | change la nature du marquage | non |
| Cue list courante (#25) | change la cible d'enregistrement | partiellement |
| **État des filtres (#28)** | **change ce qui est enregistré** | **non** |
| Écran actif | change le sens de `At`, `Park`, `/` | oui, via `Tab` |

Les cinq premiers changent ce qu'une commande *veut dire* ; celui des filtres change ce
qu'elle *produit*, sans que son texte change d'un caractère. Pris ensemble, ils
constituent l'argument le plus solide en faveur de la validation utilisateur avant envoi —
qui n'était jusqu'ici justifiée que par prudence.

Version condensée de cette même table, à jour : `REGLES_POUR_UI.md`, règle 1.

#### Le piège le plus coûteux — résolu

**`At 5` vaut 50 %, pas 5 %** (ex-#29). Établi par cinq occurrences de la notation `<0>`
au §6 et reconfirmé au §22. C'était le seul cas rencontré où une commande parfaitement
valide produisait un résultat faux d'un **facteur dix**, en silence. Résolu le 2026-08-03
par confirmation directe de l'utilisateur (confiance S) : sous 10 %, écrire deux chiffres
avec un zéro de tête (`05` = 5 %, `07` = 7 %). Le générateur applique désormais la règle
au lieu de simplement la signaler.

#### Contradictions relevées plutôt que lissées

- **Le manuel se contredit** sur `{Insert Before}` / `{Insert After}` (#22) : sa liste de
  softkeys dit l'inverse de ses propres exemples.
- **Le manuel se contredit** sur les noms de touches OSC (#16) : `select_active` dans la
  liste canonique, `select active` dans l'exemple d'usage — à deux lignes d'intervalle
  pour `XYZ_Format`.
- **Le manuel abrège sans le dire** : `{Mirror}` employé dans trois exemples alors que
  seuls `{Mirror Out}` et `{Mirror In}` sont documentés (#13).
- **Une source S du projet s'est révélée sur-généralisée** (#26) : « Assert n'a pas de
  mot-clé de ligne de commande » vaut pour les submasters, pas pour les cues, cue lists,
  channels et paramètres, que le manuel documente. Leçon de méthode : *une observation de
  banc vaut pour l'objet observé, jamais pour la famille entière*. Les futurs constats
  terrain devraient être enregistrés avec leur portée exacte.
- **Le corpus et le manuel décrivent `macro:` différemment** (#30).

#### Softkeys hors de portée de l'injection OSC

Trois familles documentées au manuel mais absentes de la liste officielle des touches
OSC : sept conditions Query (#15), les deux priorités de marquage (#23), et — question
ouverte — les accolades dans une chaîne `/eos/cmd` (#18), qui concernent **toute** commande
portant un style de Fan ou un modificateur. Si les accolades ne passent pas, c'est la
stratégie d'injection qui change, pas seulement la syntaxe.

#### Prochaines étapes recommandées (rédigées le 2026-08-03, en partie dépassées depuis)

1. **Trancher #18 au banc** — les accolades dans `/eos/cmd` conditionnent l'architecture
   d'injection ; c'est maintenant le point le plus critique encore ouvert (#29 est résolu).
2. **Rapatrier la spécification USITT ASCII** (#32) — sans elle, la moitié annoncée de
   l'architecture de sortie n'existe pas.
3. Brancher la couche NL (axe B), qui peut désormais s'appuyer sur un modèle qui refuse
   d'inventer. *(Fait depuis — voir la section Axe B ci-dessous et `PLANNING.md`.)*

**Reste à faire** (à l'époque) :
cue lists multiples §14, Park §19, Filtres §13, Courbes §22, Snapshots §23, Magic Sheets
§25, puis l'export ASCII. Ensuite, brancher la couche NL (axe B).

---

## Axe B — écrire le traducteur : le journal des tranches (v0.1 → v0.4)

État courant, chiffres à jour et portée détaillée : voir `PLANNING.md` et
[`traducteur/README.md`](traducteur/README.md). L'approche retenue (traducteur
déterministe à lexique, sans IA à l'exécution) et le choix des trois issues
(`compris`/`a_preciser`/`incompris`) restent expliqués dans `PLANNING.md` — ce qui suit
est le récit tranche par tranche.

**Fait — v0.1 (2026-08-06)** : 5 intentions (créer des palettes de couleur, colorer une
sélection, régler une intensité, enregistrer sélectivement dans une cue, aller à une cue),
9 couleurs nommées, 2 couleurs déclarées ambiguës, 4 cibles symboliques de cue
(Out/Next/Last/Home), 24 cas de non-régression. Le cas d'ancrage est la demande réelle de
l'utilisateur recopiée verbatim, fautes comprises, doublée d'un cas identique écrit
proprement qui **exige le même résultat** — sinon la tolérance au bruit est illusoire.

Trois constats de cette tranche valent d'être retenus :

- **La tolérance aux fautes doit être restreinte au créneau en cours**, jamais globale.
  L'utilisateur avait écrit « chang » pour « chaud » ; dans tout le lexique, le plus
  proche voisin de « chang » est « chan » (distance 1), le mot-clé Eos pour un circuit.
  Une correction globale aurait traduit une couleur en sélection de circuits, sans rien
  dire. Restreinte aux couleurs, « chaud » gagne seul.
- **Un numéro de gel ne s'écrit jamais avec un zéro de tête en YAML.** `020` est lu comme
  de l'octal et vaut 16. Bug réellement rencontré à l'écriture du lexique, silencieux et
  plausible (`Color 3/016` au lieu de `Color 3/020`). Corrigé, et désormais vérifié par un
  test qui contrôle les numéros un par un.
- **La tolérance aux fautes n'a pas le droit de vote sur l'INTENTION elle-même**, trouvé
  en ajoutant les cues à la même tranche : « groupe » est à distance 2 de « rouge », dans
  la marge normalement tolérée. Le joker qui détecte l'intention « colorer une sélection »
  sans recopier tous les noms de couleur utilisait cette tolérance et détournait
  « enregistrer le groupe 2 dans la cue 5 » vers la mauvaise intention — pas une mauvaise
  couleur, une bascule d'interprétation entière. Corrigé : la détection d'intention
  n'utilise plus que des correspondances exactes ; la tolérance reste réservée au
  remplissage d'un créneau déjà choisi.

**Fait — v0.2 (2026-08-07)** : submasters (enregistrement sélectif, bump haut/bas) et
effets (application, arrêt). 4 nouvelles intentions, 14 nouveaux cas de non-régression
(39 au total). Choisies pour cette tranche parce qu'elles sont les extensions les plus
naturelles à formuler en français et que `grammar/` les couvre déjà avec de bonnes règles
sourcées (manuel §18 et §20, confiance A sur la syntaxe centrale).

Le constat qui vaut d'être retenu ne vient pas d'une nouvelle zone d'ombre de la console,
mais d'un risque de conception trouvé en préparant cette tranche : le modèle interdit
explicitement `Sub + intensite` (confiance S — « le pilotage de niveau d'un sub passe par
le fader ou les bumps, pas par `At` »). Si `Sub` avait été ajouté à l'index générique
d'objets déjà utilisé par `regler_intensite` (comme `Chan`/`Group`/`Cue` le sont), une
phrase telle que « sub 3 à 50 % » aurait pu produire `Sub 3 At 50 Enter` — une commande
techniquement générée, chargée d'un avertissement du générateur, mais qu'on **sait déjà**
fausse avant même de l'émettre. Corrigé en amont plutôt qu'au générateur : `Sub` vit dans
un second index (`objets_cible`), consulté uniquement par les deux intentions dédiées aux
submasters (`enregistrer_sub`, `bump_sub`), jamais par les intentions génériques de
sélection. La phrase « sub 3 à 50 % » ne déclenche donc aucune intention et reste
`incompris` — vérifié par un cas de non-régression dédié.

Deuxième point, plus modeste : les touches `SubUp`/`SubDown` (bump haut/bas) sont sourcées
sur leur existence (`eosKeys.ts`, A) mais aucune source du dépôt ne documente ce qu'elles
font fonctionnellement sur le plateau. Le traducteur ne l'invente pas — si la phrase ne
précise pas la direction, il pose une question (« Bump vers le haut ou vers le bas ? »)
plutôt que de choisir, sur le modèle déjà en place pour les couleurs ambiguës.

**Nouveauté du 2026-08-07** : `app/prototype.html` n'utilise plus un moteur de
traduction de démonstration — il fait tourner le vrai `traducteur/` (et
`grammar/generateur.py`) directement dans le navigateur, via Pyodide (Python
compilé en WebAssembly, vendu dans `app/vendor/pyodide/`, pas chargé depuis un
CDN). Voir `app/engine.js` pour le détail et les deux bugs réels trouvés en le
testant dans un vrai navigateur (import PyYAML qui plantait Pyodide inutilement,
encodage UTF-8 cassé faute de `<meta charset>`). Testé de bout en bout avec
Playwright : le round-trip complet (question posée, réponse, macro finale)
reproduit exactement `traducteur/test_traducteur.py`.

**Correctif du 2026-08-07 (sans bump de version — amélioration de v0.2)** : un numéro de
gel après « gel »/« gélatine » (pas seulement « lee ») déclenchait déjà l'intention
`colorer_selection` mais le numéro qui suivait n'était jamais lu — seule la présence du
mot-clé nuancier « lee » faisait chercher un numéro après lui. Trouvé en testant l'app
avec une vraie phrase de l'utilisateur (« groupe 1 à 5 en 205 »), pas une phrase écrite
pour le traducteur. Corrigé dans `_colorer_selection` : un numéro resté libre après
extraction de la sélection ne peut plus désigner que le gel. Limite assumée, pas
corrigée : un numéro sans AUCUN mot de la famille couleur reste incompris — trop ambigu
pour être deviné sans aucun repère dans la phrase.

**Nouveauté du 2026-08-07 : les hypothèses (code couleur vert/orange/rouge)**, décidée
avec l'utilisateur en session. Quand le traducteur choisit une valeur sans marqueur
explicite dans la phrase (aujourd'hui : le nuancier, Lee étant le seul connu du projet),
il ne bloque plus par une question ni ne devine en silence — nouveau champ `hypotheses`
sur `Traduction` (classe `Hypothese` : champ, valeur, pourquoi, `correction`). La
traduction part quand même (orange côté UI), mais le champ reste visiblement une
supposition, avec une vraie question de correction toute prête plutôt qu'un texte figé.
Corriger vers une valeur non sourcée (un fabricant hors corpus, Rosco par exemple)
renvoie `incompris` avec l'explication — jamais d'invention, étape 3bis de
`PIPELINE_TRADUCTION.md`. Bonus trouvé en testant ce correctif : l'écran « incompris »
du prototype avalait les `notes` explicatives du traducteur derrière un message
générique — corrigé au passage dans `app/prototype.html`.

**Fait — v0.3 (2026-08-07)** : presets et macros. 3 nouvelles intentions
(`enregistrer_preset`, `rappeler_preset`, `appel_macro`), sourcées manuel §11 (Presets)
et §24 (Macros), confiance A sur la syntaxe centrale. Même garde-fou que pour `Sub` en
v0.2 : `Preset` vit dans `objets_cible`, jamais dans `objets` — un preset ne peut pas en
référencer un autre (manuel §11, « Presets can not refer to other presets »), donc aucune
autre intention ne peut s'en servir comme sélection générique.

Corrigé au passage dans `grammar/generateur.py` (pas seulement le traducteur) :
`record_preset`/`record_only_preset` ne rendaient pas les options (`{By Type}`,
`{Absolute}`, `{Locked}`), alors que le manuel §11 confirme que les presets partagent
exactement les mêmes trois softkeys que les palettes — gap documenté depuis PLANNING #38
(résolu le 2026-08-06) mais jamais corrigé côté générateur faute de code qui l'exerçait.

Point mineur relevé, non corrigé : `Group + record_preset` / `Group + rappeler_preset`
n'a pas d'entrée dans la matrice de légalité (seuls `Chan` et `selection_courante` y
figurent) — le générateur le signale honnêtement comme non vérifiable plutôt que
d'injecter en aveugle, exactement le comportement voulu. Aucune source manuel trouvée
pour trancher dans le temps disponible ; à vérifier au banc comme le reste du backlog.

**Fait — v0.4 (2026-08-07)** : Query. Une intention (`selectionner_query`) : « sélectionne
ce qui est/n'est pas dans » une palette couleur, un preset ou une cue — via Query, le seul
endroit du langage Eos où existe une négation (manuel §15, confiance A).

Périmètre volontairement restreint, et documenté comme tel plutôt que présenté comme une
couverture complète de Query (25 conditions au total dans le modèle) :
- Cibles couvertes : Color Palette, Preset, Cue — les seules familles déjà modélisées
  ailleurs dans le traducteur. Int/Focus/Beam Palette, Group et Sub existent comme cibles
  de Query dans `grammar/modele.yaml` mais restent hors périmètre.
- Un « palette » nu, sans le mot « couleur », reste explicitement `incompris` plutôt que
  de deviner la famille — jamais d'invention silencieuse, même dans un cas qui aurait pu
  sembler sans conséquence (une seule famille de palette existe dans le traducteur).
- Group et Sub comme cibles de Query ne sont pas couverts du tout : le risque de
  confusion avec une simple sélection (`Group 2 Enter` ≠ `Query {Is In} Group 2 Enter`,
  deux mécanismes distincts) n'a pas été tranché — mieux vaut ne pas couvrir que mal
  distinguer.
- Une seule condition par requête ; les Query composées à plusieurs conditions (manuel
  §15, `{Can Be} X {Isn't In} Y`) restent hors périmètre de cette tranche.

**Fait — v0.5 (2026-08-09)** : Mark et Park. Deux intentions (`marquer`, `parquer`), chacune
volontairement restreinte à sa forme la moins ambiguë plutôt qu'à sa couverture complète.

`marquer` (manuel §9, confiance A) réutilise `self._objet` pour choisir Chan/Group/Cue selon
le mot présent — « marque la cue 10 » pose le drapeau M, « marque les circuits 1 à 5 »
désigne la cue source où sont stockés les mouvements NP, deux usages distincts de la même
touche `Mark` que le traducteur ne cherche pas à départager. `Mark Cue <n>` et `Mark
Earliest` restent hors périmètre. C'est le générateur, pas le traducteur, qui porte
l'avertissement AutoMark/marques référencées (#24, réglage de Setup sans commande de
lecture).

`parquer` (manuel §19, confiance A) a mis au jour un bug réel dans un mécanisme *existant*
partagé avec `regler_intensite` : `self._plage` cherche partout dans la phrase un motif
« chiffre, mot de plage, chiffre » et le traite comme une plage de circuits, sans savoir
qu'un seul « à » peut aussi introduire un niveau (« circuit 4 à 50 % »). `regler_intensite`
évite le piège seulement parce que ses phrases attendues portent DEUX « à » (un pour la
plage, un pour le niveau — voir le commentaire dans son code). Une phrase à un seul circuit
suivi d'un niveau («  circuit 4 à 50 % ») échoue donc silencieusement en `incompris` même
pour `regler_intensite`, jamais remarqué faute de test sur cette forme précise. Plutôt que
de retoucher `_plage`, utilisée par de nombreux handlers déjà testés, `_parquer` contourne
le problème à la racine : il ne couvre qu'un seul circuit ou groupe, jamais une plage,
supprimant l'ambiguïté au lieu de la deviner. Le bug plus général dans `regler_intensite`
reste ouvert, noté ici plutôt que corrigé sous pression — une correction de `_plage`
mériterait sa propre vérification contre toute la suite de tests existante.

**Fait — v0.6 (2026-08-09)** : Assert. Une intention (`asserter`, manuel §14, confiance A) :
réaffirmer l'autorité d'une cue, d'un circuit ou d'un groupe sur le plateau. Même garde-fou
que pour Sub ailleurs dans le traducteur (`enregistrer_sub`, `bump_sub`, Park) : `Sub`
n'existe pas dans `self._objets`, donc « assert le sub 3 » ne trouve structurellement aucun
objet et reste `incompris` — cohérent avec le constat de banc (S, backlog #26) que
`Sub <n> Assert` échoue en erreur de syntaxe, contrairement aux cues et channels. La
notation de cue list explicite (`Cue x/y Assert`, manuel §14) reste hors périmètre, comme
tout ce qui touche aux cue lists multiples dans ce traducteur.

**Fait — v0.7 (2026-08-09)** : Filtres. Une intention (`effacer_filtres`, manuel §13,
confiance A) : effacer tous les filtres actifs (`Clear Filters`), sans sélection ni cible —
le seul geste de filtre à disposer d'une touche OSC propre et dédiée. Poser un filtre par
accord maintenu (`{Filter}` + touches de paramètre, tenu puis relâché) reste hors périmètre :
rien dans le dépôt ne confirme que cet accord se reproduit fidèlement en OSC (backlog #27).
Sans la pose, l'app ne peut pas non plus dire quel filtre est actif avant l'effacement —
un effacement à l'aveugle, assumé comme tel plutôt que caché.

Les tranches v0.3 à v0.7 ont été développées en autonomie (sessions du 2026-08-07 et
2026-08-09, « travaille sur les tâches dont tu n'as pas besoin de moi ») : chaque intention
testée unitairement (Python) et, pour v0.3/v0.4, de bout en bout dans un vrai navigateur
contre le vrai moteur avant commit, aucune n'attend de validation utilisateur bloquante —
cohérent avec le principe déjà établi que seules les zones réellement ambiguës doivent
l'être.

---

## Backlog résolu — détail complet

Version compacte (numéro, une ligne, date) dans `PLANNING.md` § Backlog technique. Ce qui
suit est le récit complet de chaque résolution — pourquoi le point existait, ce qui l'a
tranché, ce qui a été corrigé.

37. **✅ Confiance sur-cotée dans `GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` §10.6 — corpus #067
    cité « S » alors qu'il est C.** Trouvé le 2026-08-06 en poursuivant la vérification
    de `REGLES_POUR_UI.md` (règle 8, transport). Le corpus lui-même étiquette #067 :
    « BUG CONFIRMÉ : fuite de commandes d'une macro background vers la fenêtre d'édition
    d'une autre macro **(C, décrit avec précision, non résolu)** ». La grammaire
    consolidée affirmait pourtant « confirmé S » — la confiance la plus haute du projet,
    réservée à l'observation terrain protocolée, pour un témoignage de forum non résolu.
    **Propagé sans contrôle dans `REGLES_POUR_UI.md`** lors de sa rédaction initiale, qui
    citait la même source amont sans remonter au corpus. Deuxième citation erronée trouvée
    dans la même passe : le corpus #060 (concaténation de chaînes tronquant les décimales)
    était cité « confiance S » dans `REGLES_POUR_UI.md` alors que le corpus l'étiquette C
    (« hypothèse plausible d'un contributeur, non confirmée par ETC »).
    **Corrigé** dans les deux fichiers : `GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` §10.6 porte
    désormais « confiance C » avec une note d'audit, `REGLES_POUR_UI.md` cite C pour les
    deux points avec renvoi explicite à cette entrée.
    **Leçon générale** : une confiance mal cotée peut se propager de document en document
    sans qu'aucun ne la questionne — le contrôle doit remonter jusqu'à la source primaire
    (ici le corpus), pas s'arrêter au premier document qui cite un niveau de confiance.

38. **✅ Presets — le piège `{By Type}` de la règle 4 (UI) s'applique identiquement,
    non encodé dans le modèle.** Trouvé dans la même passe : le manuel §11 « Storing a By
    Type Preset » reprend au mot près l'avertissement du §10 sur les palettes — un seul
    channel par type devient le défaut, les autres sont figés en données discrètes.
    `grammar/modele.yaml` documentait déjà ce piège pour `palettes.options.{By Type}`
    mais pas pour `presets` (aucune section `options` n'existait). **Corrigé** :
    `presets.options` ajouté, avec renvoi au texte exact du manuel. Sans conséquence
    immédiate sur `traducteur/` — les presets n'y sont pas encore modélisés (v0.1 ne
    couvre que les palettes de couleur) — mais à respecter dès qu'ils le seront.

35. **✅ Une sélection ne survit pas à un `Record` — et le modèle l'ignorait.**
    Trouvé le 2026-08-06 en vérifiant `REGLES_POUR_UI.md` contre le manuel plutôt que
    contre la mémoire de la session. Le manuel §6 « Deselecting Channels » l'énonce
    **deux fois textuellement** : « Channels are deselected when any action is taken on
    the keypad that is unrelated to manual control, such as recording groups and cues, or
    updating a record target. » Le workbook officiel **L2 Enhanced v3.3** le confirme en
    pratique sur exactement le cas d'usage du projet — sa section « COLOR PALETTES »
    enregistre une série de sept palettes et repose la sélection à **chacun** des sept
    enregistrements, tantôt en réécrivant `[Group] [99]`, tantôt par `[Select Last]` ;
    aucun `Record` n'y est écrit nu.
    **Conséquence : la première macro produite par ce dépôt pour une demande réelle était
    fausse.** Les six palettes de couleur générées le 2026-08-06 n'auraient enregistré
    correctement que la première — les cinq suivantes se seraient enregistrées depuis une
    sélection vide, sans refus de la console ni avertissement du générateur. Exemple
    parfait de la classe d'erreur que ce projet existe pour attraper : commande valide,
    console d'accord, résultat faux et silencieux.
    **Corrigé** : règle encodée dans `grammar/modele.yaml` (`duree_de_vie_selection`,
    confiance A), garde-fou structurel dans `generateur.py`
    (`_verifier_survie_selection`, 3 cas de non-régression), et le traducteur repose
    désormais la sélection sur **chaque** étape plutôt que de compter sur sa survie.
    Choix assumé : reposer la sélection en toutes lettres plutôt qu'employer
    `Select Last` — même raison que pour `Chan`/`Cue` explicites, chaque ligne doit être
    vraie isolément.

36. **✅ `{By Type}` ne dispense pas de sélectionner des channels.**
    Trouvé dans la même passe. `APP.md` et le traducteur présentaient `{By Type}` comme
    une réponse possible à « quels circuits ? » — une palette générique « sans dépendre
    de channels précis ». C'était une erreur de lecture : `{By Type}` décrit ce que la
    palette **contiendra**, pas comment elle s'enregistre. Manuel §10 « Storing a By Type
    Palette » : « the lowest number channel of each fixture type will be the default
    channel. Generally, you will want **only one channel of each fixture type in use**.
    Any additional channels in that fixture type will be recorded with **discrete data**. »
    Enregistrer `{By Type}` sur une sélection large est donc activement contre-productif —
    un channel par type devient le défaut, tous les autres sont figés en valeurs
    discrètes (marqueur `T+`), et la console n'en dit rien.
    **Corrigé** dans `grammar/modele.yaml` (§ palettes, `ne_dispense_pas_de_selection`),
    dans le lexique du traducteur (les deux options de la question exigent désormais une
    sélection, `{By Type}` n'étant plus qu'un modificateur), dans `APP.md` et dans
    `REGLES_POUR_UI.md`.

29. **✅ Niveau sous 10 % — zéro de tête.** Le manuel §6 établissait déjà, par cinq
    occurrences de sa notation `<0>`, qu'un chiffre unique après `At` reçoit un zéro
    implicite : `At 5` vaut **50 %**, pas 5 %. Restait ouvert : comment exprimer un
    pourcentage réellement inférieur à 10, puisqu'aucun exemple du manuel n'y descendait.
    **Résolu le 2026-08-03** par confirmation directe de l'utilisateur en session : « 5 vaut
    50 et 2 vaut 20 ainsi de suite. 05 vaut 5 et 07 vaut 7 ainsi de suite. » Confiance S, par
    analogie avec `reference/JOURNAL_observations_nomad.md` — même nature de source (retour
    direct de l'opérateur console), pas un document tiers. Le générateur écrit désormais
    systématiquement deux chiffres pour toute valeur 1-9 (`_formater_niveau()` dans
    `grammar/generateur.py`), et ne signale plus rien : c'est devenu une règle appliquée, pas
    une zone d'ombre.

34. **Table de référence des couleurs Lee — résolue via catalogue officiel reçu.**
    Trouvé le 2026-08-03 en testant une traduction réelle (« créer les palettes couleur
    1 à 6, Lee, chaud/froid/rouge/vert/bleu/jaune »). Le dépôt sait QUE le nuancier Lee
    est la bibliothèque 3 (`Color 3/<numéro>`, manuel §10, corpus #082) mais n'avait aucune
    table reliant un nom de teinte à son numéro de gel — seul `Lee 195` apparaissait dans
    le corpus, comme exemple générique non rattaché à une couleur nommée.
    **Même nature de lacune que #32 (ASCII)** : ce n'est pas une zone d'ombre de la
    console — ni un banc, ni une session console ne la résout, il faut le document
    lui-même. **Risque distinct des autres points du backlog** : une mauvaise référence
    de gel ne produit ni erreur de syntaxe ni refus de la console — la macro s'exécute et
    donne silencieusement la mauvaise couleur sur scène.
    **Élargi le même jour**, en autonomie, via `WebSearch` (le seul canal réseau qui
    fonctionne ici — `WebFetch` refuse 403 sur toutes les pages testées, y compris
    Wikipedia) : voir [`reference/lee_filters_theatre.md`](reference/lee_filters_theatre.md).
    Environ 60 teintes recensées, à deux niveaux de confiance distincts de l'échelle
    S/A/B/C/D du reste du projet — page produit individuelle retrouvée (✅), ou nom
    cohérent entre recherches mais non vérifié entrée par entrée (〰️, à re-vérifier avant
    un usage critique). Une quarantaine de noms « spéciaux » (série 700) obtenus d'un
    coup sans vérification individuelle ont été délibérément écartés — volume trop grand
    pour ce niveau de confiance, risque d'invention par l'outil de recherche lui-même.
    **Chaud/froid, confirmé par l'utilisateur le 2026-08-03** : 204-206 = famille chaud
    (Orange), 201-203 = famille froid (Blue) — cohérent avec les valeurs Kelvin
    officielles du catalogue (204 : 6500K→3200K, etc.). Décision autonome documentée :
    205/202 (force « moitié ») par défaut en l'absence d'autre précision.
    **Résolu le 2026-08-05** : l'utilisateur a uploadé directement le catalogue officiel
    Lee Filters « Art of Light » (~2007, 39 pages, PDF conservé dans
    `reference/source/LEE_Filters_Art_of_Light_brochure.pdf`) après que la voie réseau se
    soit révélée bloquée pour ce besoin (règle n°1 de `CLAUDE.md`). Les 39 pages ont été
    lues intégralement. `reference/lee_filters_theatre.md` a été réécrit à partir de
    cette source unique : gamme couleur complète (~230 teintes, numéro + nom +
    description officielle), remplaçant l'ancienne table à confiance variable
    sourcée par `WebSearch`. Seul point encore non tranché : le catalogue ne publie pas
    de paire chaud/froid explicite pour un wash (lecture 2, complément de 147 Apricot) —
    detail mineur, documenté comme ouvert dans le fichier. Édition ~2007 : à revérifier
    un jour si une teinte semble avoir changé depuis, mais c'est désormais une source
    officielle et complète, plus un sous-ensemble de recherche.

# PLANNING — macro2eos

Backlog **vivant et unique** du projet. Remplace les trois listes de questions ouvertes
qui coexistaient et divergeaient (corpus « PRIORITÉS BANC », corpus « ZONES ENCORE
OUVERTES », grammaire consolidée §15) — celles-ci restent en place comme trace d'audit
mais ne sont plus à mettre à jour.

Dernière mise à jour : 2026-08-06.

---

## Où en est le projet

**Phase 1 — collecte et conversion documentaire : terminée.**

| Acquis | État |
|---|---|
| Corpus communautaire 174 entrées | ✅ complet (sauf titre de l'entrée #154) |
| Manuel officiel v3.2.0, 32 chapitres | ✅ converti intégralement, vérifié |
| 12 workbooks / documents officiels annexes | ✅ convertis intégralement, vérifiés |
| Table canonique des touches OSC (1155) | ✅ `reference/eosKeys.ts`, croisée avec le manuel |
| Journal terrain nomad réel (confiance S) | ✅ intégré verbatim |
| Grammaire consolidée de référence | ✅ `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` |
| Banc de test transport OSC/TCP | ✅ `reference/tools/` (simulateur + 3 clients) |

**Aucun document en attente.** Toute la documentation officielle ETC identifiée comme
utile est dans le dépôt.

**Phase 2 — exploitation : axe A terminé, axes B et C ouverts.**

Le constat qui ouvrait cette section jusqu'au 3 août — « le dépôt est à 100 % de prose
Markdown, rien n'y est consommable par un programme sauf `eosKeys.ts` » — n'est plus vrai.
[`grammar/`](grammar/README.md) porte désormais un modèle typé de **79 actions et 164
règles de légalité**, compilé en JSON, avec un générateur qui produit trois sorties
distinctes (ligne de commande, contenu de macro, paquets OSC) et **113 cas de
non-régression**, dont la majorité sont des exemples chiffrés du manuel officiel recopiés
verbatim.

**L'axe B est commencé** depuis le 2026-08-06 : [`traducteur/`](traducteur/README.md)
traduit une phrase française en IR, que le générateur rend ensuite. La demande réelle de
l'utilisateur — « créer les palettes couleur 1 à 6, Lee, chaud/froid/rouge/vert/bleu/jaune »,
posée en session comme « un objectif de traduction réelle » — est traitée de bout en bout,
recopiée verbatim dans les tests avec ses fautes de frappe.

| Axe | État |
|---|---|
| **A — structurer la grammaire** | ✅ terminé pour le périmètre visé (v0.16) |
| **B — écrire le traducteur NL** | 🚧 v0.1 — 5 intentions, 25 tests. Déterministe, sans IA à l'exécution (voir ci-dessous) |
| **C — valider au banc réel** | ⬜ non commencé — 36 points recensés au backlog (#34, #35 et #36 résolus) |

Ce qui reste hors périmètre du modèle : Augment3d, le pixel mapping, le serveur média
virtuel, le multi-console — et l'export ASCII, non par oubli mais faute de spécification
(#32). Le contrôle partitionné (§28) est couvert depuis v0.16.

---

## Axes de travail — Phase 2

Trois axes, indépendants entre eux. À prioriser par l'utilisateur.

### A. Structurer la grammaire en données exploitables — **terminé (v0.15)**

Transformer `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` en un jeu de données
interrogeable (JSON/YAML) : vocabulaire des touches, règles de syntaxe, patrons de
commande, niveau de confiance par règle, risques associés.

Sans cette étape, tout parser à écrire devra ré-encoder la grammaire à la main et
divergera de la doc dès la première correction.

**Approche retenue** (2026-08-01) : modèle typé Objet → Action → Cible + matrice de
légalité, plutôt qu'une grammaire formelle (EBNF). La ligne de commande Eos est modale
et dépendante de l'état console ; une EBNF forcerait à trancher des points non validés
au banc. Ici, `inconnu` est une valeur de première classe et renvoie au backlog ci-dessous.

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
ne descend sous 10 %. *(Résolu le 2026-08-03, voir « Résolu » en tête du backlog technique.)*

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

---

## Bilan de la campagne d'extension (v0.1 → v0.16) — v0.15 clôturée le 3 août, prolongée le même jour à la demande de l'utilisateur

Seize tranches, du 1ᵉʳ au 3 août 2026, plus une résolution le même jour. Le modèle est
passé de 2 objets et 3 actions à **9 objets, 79 actions, 10 modificateurs, 164 règles de
légalité**, avec **110 cas de non-régression** dont la majorité sont des exemples chiffrés
du manuel officiel recopiés verbatim. Le backlog est passé de 12 à **33 points**, dont 21
ouverts par ce travail. **25 restent encodés dans le modèle** et déclenchent un
avertissement du générateur — ils ne dorment pas dans un fichier, ils parlent à l'usage.
**Un point (#29) est résolu** : c'est la première fois qu'une confirmation réelle, en
session, referme une zone d'ombre plutôt que d'en ouvrir une — la preuve que le mécanisme
fonctionne dans les deux sens.

### Ce que la couverture atteint

Sélection, Fan, cues (simples, multipart, listes multiples), macros, submasters, Query,
effets, palettes, presets, groupes, patch, mark, park, filtres, courbes, snapshots, magic
sheets, show control, contrôle partitionné, contexte d'écran, terminaison, et la couche
d'injection OSC. L'export ASCII a été instruit et s'est révélé non modélisable faute de
spécification (#32). **Reste hors périmètre** : Augment3d, le pixel mapping, le serveur
média virtuel et le multi-console.

### Le résultat le plus important n'est pas la couverture

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

### Le piège le plus coûteux — résolu

**`At 5` vaut 50 %, pas 5 %** (ex-#29). Établi par cinq occurrences de la notation `<0>`
au §6 et reconfirmé au §22. C'était le seul cas rencontré où une commande parfaitement
valide produisait un résultat faux d'un **facteur dix**, en silence. Résolu le 2026-08-03
par confirmation directe de l'utilisateur (confiance S) : sous 10 %, écrire deux chiffres
avec un zéro de tête (`05` = 5 %, `07` = 7 %). Le générateur applique désormais la règle
au lieu de simplement la signaler.

### Contradictions relevées plutôt que lissées

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

### Softkeys hors de portée de l'injection OSC

Trois familles documentées au manuel mais absentes de la liste officielle des touches
OSC : sept conditions Query (#15), les deux priorités de marquage (#23), et — question
ouverte — les accolades dans une chaîne `/eos/cmd` (#18), qui concernent **toute** commande
portant un style de Fan ou un modificateur. Si les accolades ne passent pas, c'est la
stratégie d'injection qui change, pas seulement la syntaxe.

### Prochaines étapes recommandées

1. **Trancher #18 au banc** — les accolades dans `/eos/cmd` conditionnent l'architecture
   d'injection ; c'est maintenant le point le plus critique encore ouvert (#29 est résolu).
2. **Rapatrier la spécification USITT ASCII** (#32) — sans elle, la moitié annoncée de
   l'architecture de sortie n'existe pas.
3. Brancher la couche NL (axe B), qui peut désormais s'appuyer sur un modèle qui refuse
   d'inventer.

**Reste à faire** :
cue lists multiples §14, Park §19, Filtres §13, Courbes §22, Snapshots §23, Magic Sheets
§25, puis l'export ASCII. Ensuite, brancher la couche NL (axe B).

### B. Écrire le traducteur NL → macro — **commencé (v0.1)**

Le cœur du produit. Dépend de A si l'on veut éviter la duplication de la grammaire
dans le code. Prérequis déjà satisfaits : vocabulaire canonique, grammaire consolidée,
référentiel de risques, banc de transport OSC pour tester l'injection.

**Approche retenue (2026-08-06) : traducteur déterministe à lexique, sans IA à
l'exécution.** Voir [`traducteur/README.md`](traducteur/README.md). Trois raisons :

1. **Le réseau.** Dans le théâtre, le téléphone est sur le Wi-Fi de la console ; rien ne
   garantit un accès Internet (`APP.md`, « Même réseau que la console »). Un traducteur
   qui dépend d'un serveur distant tombe exactement quand on en a besoin.
2. **« N'invente rien »** (`CLAUDE.md` règle n°1). Un modèle de langue invente par
   construction — il peut produire une syntaxe plausible et inexistante. Un lexique ne
   peut sortir que ce qu'on y a mis, et chaque entrée est sourcée.
3. **C'est réversible.** L'IR est le contrat : une couche de compréhension plus souple
   pourra se brancher devant et émettre la même IR sans que rien en aval ne bouge.
   Commencer déterministe ne ferme aucune porte.

**Le choix de conception central : trois issues, pas deux.** `compris`, `a_preciser`,
`incompris`. Poser une question n'est pas un échec dégradé, c'est le comportement correct
face à une ambiguïté que seul l'utilisateur peut lever — c'est « n'invente rien » rendu
exécutable. Sans cette issue, un traducteur n'a d'autre choix que de deviner, et une
couleur devinée produit une macro valide, acceptée par la console, et la mauvaise teinte
sur scène : le pire des trois échecs possibles parce qu'il est **silencieux**.

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

**Reste à couvrir** : submasters, effets, Query, macros — la majeure partie des 79 actions
du modèle. Le lexique se remplira par tranches, comme le modèle l'a été.

### C. Valider au banc réel

Une session sur console/nomad réel lèverait d'un coup la majorité des incertitudes
listées plus bas. C'est le seul axe qui ne peut pas être fait depuis ce dépôt.

**Mécanisme d'accumulation (2026-08-02)** : chaque refus de la console en usage réel est
une preuve de niveau S (voir `APP.md`, « La console fait autorité »). Au lieu de se
perdre, ces refus s'enregistrent dans `grammar/refus_terrain.yaml`, reliés à un numéro
de backlog ci-dessous. `grammar/build.py` signale si un refus tranche un point encore
marqué `inconnu` dans `grammar/modele.yaml` mais pas encore reporté. Le banc réel devient
ainsi cumulatif plutôt qu'une session isolée à programmer.

---

## Backlog technique — à valider au banc réel

Rien ci-dessous ne peut être tranché depuis le dépôt : il faut un Eos ou un ETCnomad.
Le simulateur `reference/tools/fakeeos.ts` ne valide que le transport, jamais la syntaxe.

**Les numéros sont des identifiants stables**, attribués dans l'ordre de découverte et
cités tels quels par `grammar/modele.yaml` et `grammar/refus_terrain.yaml`. Ils ne sont
donc jamais renumérotés : un point ajouté tardivement en priorité haute porte un grand
numéro. C'est la priorité de la section qui fait foi, pas l'ordre des numéros.

**Un point résolu n'est jamais supprimé** : il migre ici, avec sa date et sa source, plutôt
que de disparaître — le numéro reste citable dans l'historique de `grammar/modele.yaml`.

### Résolu

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

### Priorité haute — bloquent des décisions d'architecture

32. **La spécification du format ASCII est absente du dépôt — et elle n'est pas au banc.**
    Contrairement à tous les autres points de ce backlog, celui-ci ne se tranche pas sur
    une console : c'est une **lacune documentaire**. Après revue complète des sources
    disponibles — manuel officiel, 174 entrées du corpus, 12 workbooks, journal terrain —
    aucune ne décrit la structure du fichier `.asc` : ni les mots-clés, ni la
    représentation des macros, ni l'extension propriétaire ETC censée les porter. Le
    manuel §3 ne documente que le *chemin* d'import/export et prévient en CAUTION que
    « not all data (such as effects and **macros**) may be imported ».
    **Conséquence directe sur l'objectif du projet** : tant que cette spécification n'est
    pas au dépôt, « injection OSC ou ASCII » doit se lire « injection OSC ». La voie ASCII
    reste un flux manuel que l'app peut assister, pas générer.
    À rapatrier (voir `CLAUDE.md` règle n°1 pour la procédure) : la norme *USITT ASCII
    Text Representation* et la documentation ETC de son extension macro.

1. **`SubDown` / `SubUp` — survie à l'export/import ASCII.** Corpus #027 signale que les
   macros pilotant un submaster par apprentissage ne survivent pas au cycle ASCII. Si
   confirmé, cela contraint le format de sortie du traducteur.
2. **Macro-dans-macro — fiabilité réelle.** Confirmé possible par le manuel (A), mais
   corpus #070 et #095 se contredisent sur la fiabilité d'exécution. Détermine si le
   traducteur peut décomposer une intention en macros chaînées.
3. **`Send_String` multiples depuis un Client — bug EOS-53576.** Corpus #107. Toujours
   présent en v3.2+ ? Conditionne la stratégie d'injection multi-commandes.
14. **`Go To Cue` en macro Background — exécution non déterministe.** Corpus #061,
    témoignage technique avec logs : le Go To Cue n'est pas toujours exécuté, ou l'est
    sur la mauvaise cue list assertée, avec une possible dépendance au timing. Le projet
    force Foreground par défaut, ce qui limite le risque sans le lever. Si le
    non-déterminisme se confirme même en Foreground, le traducteur ne peut pas produire
    de macro de conduite sans validation post-envoi (`/eos/out/cmd`, §11.6 de la
    grammaire consolidée). Distinct de #7, qui ne porte que sur la troncature décimale.

20. **Mode de patch By Channel / By Address — toggle non observable.** `5 At 100` patche
    le channel 5 à l'adresse 100 en mode par channel, et l'**adresse 5 au channel 100**
    en mode par adresse : la même chaîne produit deux patchs opposés. La bascule `Format`
    est un toggle (pas un réglage absolu), et aucune adresse `/eos/out/…` ne publie le
    mode courant — le sous-arbre `/eos/out/get/patch/…` renvoie la base de patch, pas
    l'état de l'affichage. Le générateur ne peut donc ni lire ni régler ce mode. Seule
    parade documentée : le préfixe `Address <n> At <channel>`, non ambigu quel que soit
    le mode. À vérifier au banc : le préfixe tient-il vraiment dans les deux modes ?
    Ce point valide directement la stratégie « validation utilisateur avant envoi ».

26. **`Assert` en ligne de commande — la grammaire consolidée est trop générale.**
    `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` §9 affirme, sur la foi du journal terrain
    (S) : « Assert n'a pas de mot-clé de ligne de commande — fonction hardkey uniquement ».
    Le manuel §14 (A) documente pourtant `Cue x/y Assert Enter`, `Cue x/ Assert Enter` et
    `<channels> Assert Enter`, avec exemples. Les deux sources sont conciliables : le
    constat de banc portait sur `Sub n Assert`, un assert de **submaster**, qui échoue
    bien — c'est la généralisation qui est fautive, pas l'observation. À trancher au banc :
    `Cue 2/5 Assert Enter` passe-t-il en `newcmd` ? Si oui, corriger le §9 de la grammaire
    consolidée, qui induit en erreur depuis sa rédaction.

28. **L'état des filtres est invisible — et il décide de ce qui s'enregistre.** Aucune
    adresse `/eos/out/…` ne publie l'état des filtres (vérifié sur le manuel §31 et sur
    `Supported_OSC_Commands.md`). La **même** commande `Record Cue 5 Enter` enregistre donc
    un contenu différent selon un état que le générateur ne peut pas lire, sans que son
    texte change d'un caractère. C'est le cinquième état implicite du modèle, et le seul
    qui altère le *résultat* d'une commande plutôt que son *sens* — les autres (#20, #24,
    #25, Q Only/Track) changent ce que la commande veut dire, celui-ci change ce qu'elle
    produit. À trancher : existe-t-il un retour, même indirect, sur l'état de filtrage ?

### Priorité moyenne — affectent la génération de macros

4. **`Group 5 + 1 Thru 6`** — combiner un groupe et une plage de channels. Aucun exemple
   exact dans le corpus ni dans le manuel ; transporté sans erreur par le simulateur
   (`reference/tools/test-client3.ts`), ce qui ne prouve rien syntaxiquement.
5. **`Record ... Label <texte multi-mots>`** — comportement réel avec espaces et tirets,
   dépend du clavier virtuel de la console.
6. **`{Enable}` / `{Disable}` sur le marking** — toggle ou absolu ? Corpus #118.
7. **`Go_To_Cue_<décimale>` concaténé** — troncature observée. Corpus #060.
8. **`Isn't In` / `Could Be` / `Group Cells` / `From Absolute`** — confirmés textuellement
   ailleurs mais absents de `eosKeys.ts`. Syntaxe exacte à vérifier. Corpus #148/#149.
15. **Sept conditions Query sans touche OSC.** `Up Moves`, `Down Moves`, `Live Moves`,
    `Dark Moves`, `Broken Mark`, `Marking`, `Autoblock` figurent dans la liste des
    softkeys Query du manuel §15 (A) mais **pas** dans la liste officielle des touches
    OSC du manuel §31, ni dans `eosKeys.ts`. Elles sont donc atteignables au doigt mais
    pas par `/eos/key/<nom>`. Restent-elles atteignables en écrivant leur nom dans une
    chaîne `/eos/cmd` ? Si non, ces sept conditions sont hors de portée de l'app, et le
    traducteur doit le dire au lieu de produire une commande muette.
18. **Les accolades `{...}` passent-elles dans une chaîne `/eos/cmd` ?** Aucun exemple,
    nulle part dans le corpus ni le manuel, ne montre un token softkey entre accolades
    à l'intérieur d'une chaîne de ligne de commande OSC. Le seul exemple officiel de
    softkey en `cmd` l'écrit en mots sans accolades (`/eos/cmd=Chan 1 XYZ_Format Enable#`,
    manuel §31). Enjeu direct : toute commande générée contenant un style de Fan ou un
    modificateur (`{Mirror Out}`, `{Q Only}`, `{Complete}`…) est concernée. Si les
    accolades ne passent pas, ces commandes doivent être décomposées en `/eos/key/<nom>`
    séparés — ce qui change la stratégie d'injection, pas seulement la syntaxe.

24. **AutoMark ou marques référencées — lequel est actif ?** Les deux mécanismes
    s'excluent mutuellement, le choix est un réglage de Setup **global et rétroactif**
    (désactiver AutoMark convertit toutes les AutoMarks du show en marques référencées),
    et aucune commande de lecture n'est documentée. Une même intention utilisateur —
    « prépare le mouvement pendant que le projecteur est noir » — se traduit donc
    différemment selon un état que le générateur ne peut pas consulter. Existe-t-il une
    sortie OSC ou une commande qui révèle ce réglage ? Sinon, la traduction doit être
    annoncée sous condition, comme pour le mode de patch (#20).

### Priorité basse — complètent la couverture

9. **Styles de Fan non testés** : `{Interleave}`, `{Jump}`, `{Num Groups}`,
   `{Channels Per Group}`, `{Curve}`. Noms confirmés (A), comportements jamais observés.
19. **Liste des commandes auto-terminantes — incomplète de l'aveu d'ETC.** Le manuel
    énonce `Out`, `+%`, `-%`, `Level` et les actions de direct select, puis ajoute
    explicitement « Some (but **not all**) of these commands are ». Toute autre commande
    est donc présumée avoir besoin d'`Enter` sans preuve. Deux doubles appuis connus
    changent aussi la donne (`Full Full`, `Sneak Sneak` auto-terminent, pas leur forme
    simple). Un `Enter` de trop sur une commande déjà terminée risque de valider la
    ligne suivante. À établir au banc, commande par commande.
21. **Le mot-clé `Chan` est-il accepté en contexte Patch ?** Le chapitre §4 du manuel
    n'écrit jamais `[Chan]` — uniquement des numéros nus (interprétés selon le mode) et
    le préfixe `[Address]`. Or le générateur écrit `Chan` partout, par convention
    d'explicitation adoptée dès v0.1. Que `Chan 5 At 100` soit accepté en Patch — et
    surtout qu'il force l'interprétation channel quel que soit le mode Format — est une
    extrapolation, jamais vérifiée. Si elle tient, c'est la parade symétrique de
    `Address` et elle lève #20 pour de bon.
22. **`{Insert Before}` / `{Insert After}` — le manuel se contredit.** Sa liste de
    softkeys (§7, « Ordered Channels ») décrit `{Insert Before}` comme insérant « after
    the specified channel » et `{Insert After}` comme insérant « before » — l'inverse de
    leurs noms. Ses propres exemples chiffrés, quelques pages plus loin, font l'inverse
    de la liste et respectent les noms. Le modèle retient les exemples, cohérents entre
    eux, mais c'est un arbitrage : une frappe sur console tranche en dix secondes.
23. **`{High Priority}` / `{Low Priority}` sur une marque — pas de touche OSC.**
    Documentés au manuel §9 (l'ordre de tentative est high → normale → low) mais absents
    de la liste officielle des touches OSC du §31 comme de `eosKeys.ts`. Même classe de
    problème que les sept conditions Query de #15 : atteignables au doigt, hors de portée
    de `/eos/key/`. Attention à ne pas les confondre avec `priority`→`SOURCE_PRIORITY`,
    qui existe bien mais désigne la priorité de submaster (§20), un autre mécanisme.
25. **Cue list courante — quatrième état implicite.** La liste vers laquelle on enregistre
    est déterminée par la « cue sélectionnée », qui change à chaque `Record`, `Update`,
    `Go`, `Back`, `Go To Cue` ou simple modification d'attribut. Le manuel juge utile de
    prévenir : « It is very useful to keep an eye on the selected cue ». Le générateur
    nomme désormais la liste explicitement, même la liste 1, plutôt que d'hériter d'un
    état qu'il ne peut pas lire — reste à vérifier qu'un préfixe explicite l'emporte bien
    dans tous les cas de figure.
27. **Poser un filtre est un accord maintenu — reproductible en OSC ?** Le manuel §13
    décrit la pose en trois temps : tenir `{Filter}`, presser les touches de paramètre,
    relâcher. `filter`→`FILTER` et `clear_filters`→`CLEAR_FILTER_COMMAND` existent bien
    comme touches OSC, et `/eos/key/<nom>` accepte un front (1.0 appui, 0.0 relâchement) —
    la reproduction de l'accord est donc *plausible*, mais nulle part documentée ni
    observée. Si elle ne marche pas, l'app ne peut pas choisir son état de filtrage : elle
    hérite de celui de la console, avec les conséquences décrites en #28. Tester d'abord
    `{Clear Filters}` seul, qui a sa propre touche et devrait être le cas le plus simple.
30. **`macro:` dans un bouton de Magic Sheet — quelle forme exactement ?** Le corpus #063
    (C, d'après l'infobulle native) le décrit comme le moyen d'appeler une macro depuis un
    bouton, ce qui suggère `macro:<numéro>`. Le seul exemple du manuel §25,
    `macro:Tab_Down 2 7 Tab_Up`, montre autre chose : une suite de commandes de macro en
    noms internes, sans numéro. Les deux formes peuvent coexister — rien ne les oppose —
    mais seule la seconde est attestée, et c'est celle que le modèle retient.
31. **Les numéros d'évènement de show control ne sont pas stables.** Le manuel est
    explicite : « The event number is not fixed », et les évènements se renumérotent pour
    rester chronologiques (l'exemple RTC montre un « Event 3 » devenu « Event 1 » après
    tri). Contrairement aux cues, palettes et macros, ce n'est donc pas un identifiant
    qu'un traducteur peut mémoriser d'une session à l'autre. À vérifier : existe-t-il un
    identifiant stable pour désigner un évènement, ou seul le couple heure/action fait foi ?
33. **Flexichannel « Partitioned » — mode non couvert.** Devient disponible quand le
    contrôle partitionné est actif (manuel §28) ; limite l'affichage flexi aux channels de
    la partition courante. Le mécanisme Flexichannel lui-même (`§6`, « Using Flexichannel »)
    n'est pas encore dans le modèle — hors périmètre pour l'instant, pas une zone d'ombre
    de la console.
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
10. **Ambiguïté `duration` (OSC)** et dérive de nommage `console_settings` /
    `desk_settings` — écarts relevés dans `reference/eosKeys_vs_manual_comparison.md`.
11. **Familles entières jamais explorées fonctionnellement**, découvertes via `eosKeys.ts` :
    RTC/Astro (déclenchement horaire), Pixel Mapping complet, édition de courbes,
    `startup_macro` / `shutdown_macro`. Corpus #152.
12. **Lamp Control** — incohérence de softkeys en édition directe. Corpus #091.
13. **`{Mirror}` — nom réel de la softkey de Fan.** Le manuel §8 emploie `{Mirror}` dans
    trois exemples alors que sa propre liste de softkeys ne documente que `{Mirror Out}`
    et `{Mirror In}`, et `eosKeys.ts` ne connaît que `mirror_in` / `mirror_out`.
    L'exemple `{Mirror}` donne le même résultat chiffré que l'exemple `{Mirror Out}` :
    abréviation rédactionnelle probable, jamais confirmée. En attendant, le générateur
    écrit `{Mirror Out}` en clair et n'émet jamais `{Mirror}`.
16. **`/eos/key/<nom>` — espace ou underscore ?** Deux sources ETC se contredisent :
    la liste canonique du manuel §31 écrit `select_active`, tandis que l'exemple d'usage
    du même chapitre — et le PDF *Supported OSC Commands* de 2017 — écrivent
    `/eos/key/select active` avec un espace. Le manuel se contredit même à deux lignes
    d'intervalle sur `XYZ_Format` / `XYZ Format`. Un alias est probable, jamais confirmé.
    En attendant, n'émettre que la forme underscore de `reference/eosKeys.ts`.
17. **`{Select Last}` après une Query composée.** Corpus #083 (C) : au lieu de renvoyer
    la sélection résultante, la touche relance la syntaxe de la requête. Si confirmé,
    cela interdit la combinaison Query + boucle `SelectLast`/`Next` — c'est-à-dire la
    stratégie de génération en masse n° 2 appliquée à une sélection conditionnelle.

### Contradiction connue, non résolue

- Le simulateur `fakeeos.ts` émet un écho différé sur `/eos/sub/<n>`, alors que le journal
  terrain (`reference/JOURNAL_observations_nomad.md`, confiance S) affirme qu'un Eos réel
  ne republie **jamais** spontanément sur cette adresse. Simplification du simulateur
  probable — à ne pas prendre pour argent comptant.

---

## Dettes documentaires mineures

- **Entrée #154 du corpus** : le titre et les premières lignes manquent (contenu présent
  à partir de « Confiance : C/B »). Lacune marquée dans le fichier. Nécessiterait que
  l'utilisateur retrouve le texte d'origine.
- **`Etude_Pont_MIDI-OSC_EOS.md`** : mentionné en début de projet comme source possible,
  jamais reçu. À rapatrier si toujours pertinent (voir `CLAUDE.md` règle n°1 pour la
  procédure de transfert).
- **Piste produit en attente** : « validation post-NL par édition à menus déroulants »,
  décrite dans la section « Notes produit » du corpus. À traiter en phase conception.

---

## Rappels de méthode (ne pas relâcher)

- Conversion **intégrale** des sources, jamais de résumé (`CLAUDE.md`).
- Sources PDF/DOCX = **archive**, pas de consultation routinière (`CLAUDE.md` règle n°2).
- Grammaire normative = sources A/B uniquement. Les usages communautaires (C/D) sont
  admis mais toujours marqués non-autoritaires et « non testé » par défaut.
- Toute macro validée uniquement contre le simulateur reste **non confirmée
  syntaxiquement**.

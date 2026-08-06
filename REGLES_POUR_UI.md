# Les règles structurantes de la grammaire Eos — et ce qu'elles imposent à l'interface

Document de cadrage pour la session qui développe l'UI de l'app.

Il ne remplace ni [`APP.md`](APP.md) (la spécification produit : écrans, flux, décisions
déjà prises) ni [`reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md`](reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md)
(la référence de syntaxe). Il répond à une seule question, transversale aux deux :

> **Qu'est-ce que la grammaire Eos force l'interface à faire ?**

Neuf règles, chacune avec sa conséquence directe sur l'UI. Elles ne sont pas des
préférences de conception : ce sont des propriétés de la plateforme. Une interface qui les
ignore produira des macros valides et fausses.

Une section préliminaire décrit **comment la syntaxe est structurée** — c'est ce que
l'interface affiche, et sa régularité conditionne ce qu'on peut en montrer.

---

## ⚠️ Avant de lire : ce document a déjà véhiculé des erreurs

**Première version le 2026-08-06. Relue le même jour contre le manuel officiel et les
workbooks — deux erreurs trouvées, dont une avait déjà produit une macro fausse livrée
comme correcte** (voir `PLANNING.md` #35 et #36). Les deux venaient de la même cause :
des affirmations écrites de mémoire ou reprises d'une synthèse, présentées avec la même
assurance qu'un fait vérifié.

D'où la règle de lecture de ce document :

> **En cas de contradiction entre ce document et le manuel officiel, le manuel a raison.**
> Signaler l'écart plutôt que de le contourner — c'est ainsi que #35 et #36 ont été
> trouvées.

### Marqueur de confiance sur chaque affirmation

Le reste du dépôt étiquette chaque affirmation par sa source (échelle S/A/B/C/D). Ce
document ne le faisait pas, et c'est ce qui a laissé passer l'erreur. Il le fait
désormais, avec trois marqueurs lisibles sans connaître la console :

| Marqueur | Sens | Comment s'en servir |
|---|---|---|
| ✅ | **Vérifié mot à mot** dans le manuel ou un workbook officiel pendant la relecture du 2026-08-06, chapitre cité | Construire dessus sans réserve |
| 📄 | **Documenté** par une source établie du dépôt (manuel, réponse ETC, observation terrain) mais **non re-vérifié à la source** dans cette passe | Fiable en principe ; re-vérifier avant d'en faire un point d'architecture |
| ⚠️ | **Déduction du projet** — raisonnement cohérent, pas un fait documenté | Ne jamais présenter à l'utilisateur comme une certitude |

Les conséquences UI (« → Pour l'UI ») sont **toujours** des déductions : elles portent le
raisonnement du projet, pas une prescription d'ETC. Elles ne sont pas marquées une par une
pour ne pas alourdir — le marqueur porte sur le **fait console**, qui est ce qui peut être
faux.

**Origine** : synthèse des 16 tranches de [`grammar/`](grammar/README.md), du manuel
officiel v3.2.0 (32 chapitres), des workbooks officiels, du corpus de 174 entrées et du
journal terrain. Les renvois `#n` pointent le backlog de [`PLANNING.md`](PLANNING.md).

---

# Préliminaire — l'anatomie d'une commande Eos

Avant les règles : la forme. Elle est plus régulière qu'il n'y paraît, ce qui rend un
aperçu structuré possible plutôt qu'un simple bloc de texte.

## ✅ La structure fondamentale : Objet → Action → Cible

Manuel §00 « Important Concepts », vérifié mot à mot. La plupart des instructions
répondent à trois questions, dans cet ordre :

| | Question | Exemple |
|---|---|---|
| 1 | **Qu'est-ce que j'affecte ?** | `Chan 1 Thru 5` |
| 2 | **Que doit-il faire ?** | `At` |
| 3 | **Quelle valeur ?** | `50` |

Le manuel ajoute lui-même la nuance, dans les mêmes lignes : « **most** other functions
are modifiers of these three basic steps ». Ce n'est pas une grammaire complète, c'est le
squelette le plus fréquent. C'est ce principe, et non une grammaire formelle, qui est
encodé dans [`grammar/modele.yaml`](grammar/README.md) : la ligne de commande Eos est
modale, une EBNF forcerait à trancher des points jamais validés.

✅ **Toutes les actions ne passent pas par la ligne de commande.** Manuel §00, textuel :
« Not all actions must be entered from the command line [...] **Other actions bypass the
command line entirely.** » Softkeys, direct selects et encodeurs la contournent — l'app ne
peut donc pas tout exprimer sous forme de texte injectable.

## ⚠️ L'ordre des créneaux dans une ligne

```
[sélection]  [action]  [valeur]  [modificateurs]  [Time …]  [Label …]  [Enter]
```

**Ce schéma est une généralisation du projet, pas une règle publiée par ETC.** Il décrit
fidèlement tous les exemples rencontrés, mais aucun chapitre du manuel ne l'énonce comme
tel. Ne pas s'en servir pour valider une commande, seulement pour la présenter.

En revanche, deux règles d'ordre sont, elles, explicitement établies :

- 📄 **Sur un `Go To Cue`, `Time` se pose toujours en dernier**, après les autres
  modificateurs (manuel §16). `{Manual}` en est exempté.
- 📄 **`Send_String` doit être en dernière position** d'une macro multi-lignes, sinon un
  `/r` parasite s'insère dans l'adresse OSC générée [EOS-55864] — ticket ETC rapporté par
  le corpus, pas une phrase du manuel.

Exemples réels — sorties **exactes** du générateur, vérifiées, telles que l'app les
affichera :

```
Chan 1 Thru 5 Record Cue 4 Enter                    sélection + action + cible
Group 2 Record Only Cue 5 Enter                     objet ≠ Chan
Go To Cue 5 MinusLinks Time Enter                   modificateur puis Time, dans cet ordre
Chan 1 Thru 12 At 50 Thru 70 Fan {Repeat} 3 Enter   valeur en plage + style de Fan
Record Color Palette 4 {By Type} Label FOH Blue Enter    ⚠ 1 avertissement
```

Le dernier porte un avertissement : le libellé fait deux mots, et le comportement du
clavier virtuel de la console avec les espaces n'a jamais été observé (#5). C'est un
exemple concret de la règle 4 plus bas — la commande a l'air parfaitement normale.

**Différence de forme assumée avec le manuel** : le générateur écrit toujours `Chan` et
`Cue` explicitement, là où le manuel s'appuie sur les modes implicites du clavier
(`[1][Thru][5]` désigne des channels, `[Record][5]` une cue). Une macro se relit, se
réimporte et s'exporte : l'implicite y coûte plus cher qu'il ne rapporte. Une session UI
qui compare l'aperçu au manuel doit s'attendre à cet écart — il est voulu.

## Les briques

| Brique | Forme | Note | |
|---|---|---|---|
| Sélection | `1`, `1 Thru 10`, `1 Thru 10 + 15`, `1 Thru 10 - 5`, `Group 3` | `+`/`-` ajoutent et retirent | ✅ |
| Sous-groupe | `( 1 Thru 4 )` | compte pour **un seul** channel dans un Fan, un effet, un parcours | 📄 |
| Sélection conditionnelle | `Query {Isn't In} Beam Palette 25` | seul endroit du langage où existe une négation | 📄 |
| Softkey | `{By Type}`, `{Mirror Out}`, `{Q Only}` | toujours entre accolades | ✅ |
| Libellé | `Label <texte>` | comportement du clavier virtuel avec espaces **non observé** (#5) | ⚠️ |
| Terminaison | `Enter` | sauf commandes auto-terminées, voir plus bas | ✅ |

✅ Numérotation des palettes : de `0.001` à `9999.999` (manuel §10, textuel).

## Quatre propriétés qui ne se devinent pas en lisant une ligne

### ✅ La sélection survit à l'`Enter` — mais pas à un `Record` C'est une règle en deux
temps, et le second temps est un piège de première catégorie.

`Enter` termine la *ligne de commande*, pas la sélection : celle-ci reste active pour la
commande suivante **tant que celle-ci relève du contrôle manuel** (niveau, couleur,
paramètre). Le manuel est explicite : « You may continue to modify channels 1 through 5
since they are still selected. »

Mais — manuel §6, énoncé **deux fois textuellement** :

> « Channels are deselected when any action is taken on the keypad that is **unrelated to
> manual control**, such as **recording groups and cues, or updating a record target**. »

Autrement dit : **un `Record` ou un `Update` désélectionne.** L'étape suivante est
syntaxiquement valide, la console ne refuse rien, et la commande s'applique à une
sélection **vide**. Une séquence « colorer / enregistrer / colorer / enregistrer »
n'enregistre correctement que sa **première** cible.

Ce n'est pas une hypothèse : le workbook officiel L2 Enhanced, qui enseigne exactement
l'enregistrement d'une série de sept palettes de couleur, repose la sélection à **chacun**
des sept enregistrements — tantôt en réécrivant `[Group] [99]`, tantôt par `[Select Last]`.
Aucun `Record` n'y est écrit nu.

Le générateur repose donc la sélection en toutes lettres sur chaque ligne, et **avertit**
si une IR ne le fait pas.

> **→ Pour l'UI.** Deux conséquences, dans cet ordre d'importance.
>
> **1.** Les macros produites par ce projet répètent la sélection à chaque ligne. C'est
> volontairement verbeux : chaque ligne est vraie isolément, et l'aperçu se relit sans
> avoir à reconstituer un état. Ne pas « nettoyer » cette répétition à l'affichage — elle
> est la correction, pas du bruit.
>
> **2.** Si l'interface laisse un jour réordonner, dupliquer ou supprimer des lignes, elle
> doit repasser par le générateur, jamais manipuler le texte. Une ligne déplacée peut
> perdre le sens que lui donnait la précédente.

### ✅ Certaines commandes s'auto-terminent

Elles ne prennent pas d'`Enter` : `Out`, `+%`, `-%`, `Level`, et les actions depuis les
direct selects (manuel §00, liste vérifiée). S'y ajoutent des doubles appuis — `Full Full`
et `Sneak Sneak` s'auto-terminent, leur forme simple non (manuel §02).

Et la liste d'ETC est **incomplète de son propre aveu** : « Some (**but not all**) of these
commands are » — d'où #19. Toute commande non marquée comme auto-terminée est *présumée*
avoir besoin d'`Enter` ; c'est une présomption du projet, pas un fait établi.

⚠️ Qu'un `Enter` de trop **valide la ligne suivante** est une déduction du projet, pas une
phrase du manuel — mais elle motive la prudence du générateur.

> **→ Pour l'UI.** Ne jamais « compléter serviablement » une commande avec un `Enter`.
> La terminaison est calculée par le générateur, commande par commande.

### 📄 Le même symbole a plusieurs sens — et les deux polysémies ne sont pas de même nature

| Symbole | Sens | Distingué par |
|---|---|---|
| `At` / `@` | niveau en Live, **adresse DMX en Patch** | l'**écran actif** — état extérieur à la phrase |
| `/` | 7 sens recensés : préfixe de cue list (`Cue 2/5`), montée/descente (`Time 4/3`), pourcentage de temps (`Time /50`), valeur DMX brute (`At / / 239`), univers/adresse (`At 2 / 146`), liste entière (`Cue 2/ Assert`), échelle de park (`At / 125 Park`) | la **position** dans la ligne |

La distinction compte : la polysémie de `/` est lisible dans le texte de la commande,
celle de `At` **ne l'est pas** — elle dépend d'un état que l'app ne contrôle pas. C'est
la règle n°1 ci-dessous, et le générateur peut au moins forcer l'écran (`Tab <n> Enter`).

Le décompte « sept sens » est un recensement du projet à travers plusieurs chapitres, pas
une liste publiée par ETC — chaque sens est sourcé individuellement dans
`grammar/modele.yaml`, le total ne l'est pas.

### 📄 Fan n'est pas une commande

C'est le comportement **implicite** de toute commande de niveau ou de temps utilisant
`Thru` ou une liste de références. La touche `Fan` ne sert qu'à changer de *style* de
répartition. `1 Thru 10 At 10 Thru 30 Enter` fane déjà, sans qu'aucun mot ne le dise.

> **→ Pour l'UI.** Un utilisateur qui écrit « circuits 1 à 5 de 10 à 50 % » obtient un
> dégradé. C'est l'intention normale, mais rien dans la commande produite ne porte le mot
> « dégradé » : l'aperçu doit le dire en clair si l'app veut être relue utilement.

## 📄 On assemble des tokens, jamais du texte

Observation terrain (corpus #060, confiance S — pas une phrase du manuel) : une commande
construite par concaténation de chaînes — `"Go_To_Cue_" + str(n)` — **tronque les
décimales** sur console réelle. `Go To Cue 5.5` devient `Go To Cue 5`.

> **→ Pour l'UI.** Si l'interface propose un jour de retoucher une macro générée, elle doit
> éditer l'**IR** (la représentation structurée) et la faire re-rendre, **jamais** éditer la
> chaîne affichée. La chaîne est un rendu, pas la source. Un champ de texte libre modifiable
> sur une macro générée serait une régression fonctionnelle, pas une commodité.

## Une même intention a trois formes de sortie

Le générateur produit trois choses distinctes, qui n'obéissent pas aux mêmes règles :

| Sortie | Contenu | Règles propres |
|---|---|---|
| `rendre()` | lignes de ligne de commande | matrice de légalité, Fan, modificateurs, terminaison |
| `rendre_macro()` | contenu de macro enveloppé | chaînage en fin, mode, touches non enregistrables en Learn |
| `rendre_osc()` | paquets OSC injectables | terminaison, accolades (#18), `Assert`, User# |

Ce ne sont pas trois présentations de la même chose. Une macro n'est pas une liste de
lignes de commande : certaines touches ne sont **pas enregistrables** en mode Learn — dont
`[Macro]` elle-même, ce qui oblige à passer par l'éditeur pour tout chaînage.

> **→ Pour l'UI.** L'utilisateur doit savoir laquelle des trois il est en train de
> regarder. « Envoyer cette commande maintenant » et « graver cette macro dans la console »
> ne sont pas la même action et n'ont pas les mêmes risques — la seconde est persistante.

---

# Les neuf règles

## 1. Cinq états de la console sont invisibles — et ils changent le sens des commandes

**La règle.** La ligne de commande Eos est *modale*. Le sens d'une commande ne dépend pas
que de son texte, mais de l'état de la console au moment où elle arrive. Cinq de ces états
sont établis, et **aucun n'est publié par une adresse `/eos/out/…` documentée** — vérifié
sur le manuel §31 et sur `Supported_OSC_Commands.md` :

| | État | Effet | Renvoi |
|---|---|---|---|
| 📄 | Mode de patch By Channel / By Address | `5 At 100` patche deux choses opposées | #20 |
| ✅ | Mode Q Only / Track | **le bouton `Q Only/Track` inverse son sens** selon le réglage | — |
| ✅ | AutoMark | évalué **au playback**, pas à l'enregistrement | #24 |
| ✅ | Cue list « courante » | déterminée par la « cue sélectionnée », qui change à chaque `Record`, `Update`, `Go`, `Back`, `Go To Cue` ou modification d'attribut | #25 |
| 📄 | État des filtres | change **ce qui est enregistré**, à texte de commande identique | #28 |

Trois d'entre eux ont été vérifiés mot à mot le 2026-08-06, et **deux se sont révélés
pires que ce que ce document décrivait d'abord** :

✅ **`Q Only/Track` ne fait pas une chose, il fait son contraire selon le réglage.** Manuel
§00 : « if the console is set to Tracking, the button acts as Cue Only. If console is set
to Cue Only, it behaves as a **Track** button. » Et §12 : « **The system setting determines
the actual context of the button.** » Ce n'est donc pas seulement l'*effet* d'une commande
qui dépend d'un état invisible : c'est le sens d'un **token écrit dans la macro** qui
s'inverse.

✅ **AutoMark est évalué au moment de la lecture, pas de l'écriture.** Manuel §9, textuel :
« AutoMark is based on the current setting of the default **during playback. It does not
matter what the setting is at the point of record.** » Une macro enregistrée aujourd'hui
peut donc produire un résultat différent demain sans avoir changé d'un caractère.

✅ **La cue list de destination est celle de la « cue sélectionnée ».** Manuel §14 : « The
cue list that you are storing to is always determined by the selected cue, **unless you
specify a different cue list**. The selected cue is the last cue that you affected in Live.
This includes a record, an update, a playback action such as [Go], [Back], a [Go To Cue]
instruction, or simply changing a cue attribute. » La parade est dans la phrase même —
nommer la liste explicitement — et c'est ce que fait le générateur.

Les quatre premiers changent ce que la commande *veut dire*. Le cinquième change ce
qu'elle *produit* — c'est le plus dangereux.

À cela s'ajoute la modalité d'écran : `At` vaut un niveau en Live et une adresse DMX en
Patch. Celle-là, au moins, le générateur sait la forcer (`Tab <n> Enter`).

**→ Pour l'UI.** L'aperçu avant envoi n'est pas une politesse, c'est une conséquence
technique — et `APP.md` a raison de le déclarer non négociable. Mais il faut aller plus
loin : **l'app ne doit jamais formuler une promesse de résultat.** Elle montre la commande
qu'elle va envoyer, pas ce qui va se passer sur scène. « Voici ce que je vais envoyer »
est vrai ; « ceci mettra les circuits 1 à 5 en rouge » ne l'est pas toujours, et l'écart
n'est pas détectable depuis l'app.

Corollaire : le User# dédié protège des interférences avec l'opérateur, **pas** de ces
états — ils sont globaux à la console.

---

## 2. Un refus prouve tout, une acceptation prouve peu

⚠️ **La règle est une doctrine du projet, pas une phrase d'ETC.** Elle est posée dans
`APP.md` et rappelée ici parce que l'asymétrie se perd facilement dans une interface. Elle
n'est pas moins solide pour autant — elle découle de faits vérifiés — mais elle relève du
raisonnement, pas de la citation.

- **Un refus est une preuve définitive** — la syntaxe est invalide, sans appel. C'est la
  source de confiance la plus haute du projet (niveau S).
- **Une acceptation établit seulement que la commande est syntaxiquement valide.** Pas
  qu'elle fait ce que l'utilisateur voulait. Une commande valide peut agir sur les mauvais
  circuits, dans le mauvais mode, avec le mauvais filtre actif — la règle 1 en donne cinq
  raisons.

📄 Le retour est exploitable : `/eos/out/cmd` diffuse la ligne en clair avec un flag
d'erreur (1 = erreur de syntaxe, 0 = ok, Eos 2.6.0+ — corpus #140, confiance S, non
re-vérifié dans le manuel §31 lors de cette passe).

**→ Pour l'UI.** Deux traitements visuels distincts, jamais confondus. Un refus est un
état terminal qui n'offre **aucune option de renvoyer tel quel** (déjà décidé dans
`APP.md`). Une acceptation ne doit pas s'afficher comme une réussite pleine : elle
autorise l'étape suivante, qui est la **validation visuelle en salle par l'utilisateur**.
C'est exactement pourquoi une macro n'entre dans les favoris qu'après acceptation *et*
vérification humaine.

Réserve à connaître : la correction proposée après un refus suppose que le message
d'erreur de la console soit assez précis. Non vérifié — le simulateur ne renvoie pas
d'erreur réaliste. Prévoir le cas où l'app ne peut que **signaler** le refus sans proposer
de correction.

---

## 3. En Blind, il n'y a pas d'étape de validation

✅ **C'est la règle la mieux établie de tout ce document.** Le manuel l'énonce **cinq fois,
dans cinq chapitres différents, toujours en CAUTION** — vérifié un par un le 2026-08-06 :

| Chapitre | Texte |
|---|---|
| §10 Palettes | « changes to palettes are automatic, therefore no update or record command is required » |
| §11 Presets | « changes to presets are automatically stored. Therefore no update or record command is required » |
| §12 Cues | « Edits in blind **take effect immediately**. [Record] or [Update] commands are **not required** in blind » |
| §16 Cue Playback | « changes to cues are automatically stored, therefore no update or record command is required » |
| §17 Multipart | « Edits in Blind take effect immediately, they do not require a [Record] or [Update] command » |

Quand ETC répète un avertissement cinq fois, c'est qu'il coûte cher à ignorer.

**→ Pour l'UI.** Le flux « je prépare, l'utilisateur relit, puis j'envoie » **n'existe pas
en Blind**. La première commande envoyée est déjà appliquée. Conséquences :

- Toute validation doit précéder l'envoi de la **première** commande d'une séquence, jamais
  s'intercaler entre deux.
- Une séquence multi-commandes en Blind ne peut pas être interrompue proprement à
  mi-parcours : l'app doit soit tout envoyer, soit ne rien envoyer.
- Si l'UI expose un jour un mode Blind, elle ne peut pas réutiliser le même écran de
  confirmation qu'en Live sans mentir sur ce qui est déjà fait.

---

## 4. Les erreurs les plus graves ne lèvent aucune erreur

**La règle.** C'est la classe de danger propre à ce projet : une commande **valide**,
**acceptée** par la console, qui produit silencieusement le mauvais résultat. Rien ne la
signale — ni erreur de syntaxe, ni refus, ni trace dans l'aperçu.

Cas établis :

- ✅ **Un chiffre seul vaut des dizaines — et pas seulement après `At`.** C'est plus large
  que ce que ce document affirmait d'abord. Manuel §6, exemples textuels : `[1] {Iris} [5]
  [Enter]` « places the iris parameter of channel 1 **at 50%** », et `[5] {Iris} [5] {Zoom}
  [6][5] {Edge} [5] [Enter]` donne iris 50 %, zoom 65 %, edge 50 %. La règle vaut donc pour
  **toute saisie de valeur de paramètre**, pas seulement pour l'intensité après `At`.
  Facteur dix, sans erreur ni refus. *Résolu* : `05` = 5 % (confirmation utilisateur, S) —
  le générateur écrit systématiquement deux chiffres.
- ✅ **Une valeur parquée est exclue de tous les record targets.** Et le manuel §19 précise
  le cas encore plus vicieux : on *peut* régler manuellement puis enregistrer une valeur
  sur un channel parqué — « the values set and stored in live **do not actually output to
  the system** if the parameter is parked ». Une macro qui règle puis enregistre un channel
  parqué produit donc une cue correcte sur le papier et un plateau inchangé, sans qu'aucune
  erreur ne remonte.
- ✅ **Sélection = fusion, absence de sélection = remplacement.** Manuel §12, textuel :
  « Using a selective store for an already existing cue will **modify the selected data
  only, leaving the rest of the cue untouched. This does not overwrite the whole cue.** »
  📄 La constante vaut aussi pour submasters §20 et palettes §10 (non re-vérifiés dans
  cette passe), et l'assignation de channels à une **partition inverse la règle** : une
  liste nue *remplace*, il faut `+` pour ajouter.
- ✅ **Un enregistrement sélectif ne produit pas une cue isolée.** Trouvé pendant la
  vérification, absent de la première version. Manuel §12 : « any channels not included in
  the selective store, but that do have values in the previous cue **will track into the
  recorded cue. This is true even when the console is in Cue Only mode.** » Une demande
  « enregistre seulement les circuits 1 à 5 dans la cue 4 » produit donc une cue qui
  contient **aussi** tout ce qui trackait depuis la cue précédente. La macro est
  sélective, le résultat ne l'est pas.
- ✅ **`Mark Cue <n>` a un effet de bord silencieux.** Manuel §9, textuel : « As long as
  intensity is at zero within the cue range, if there are any non-intensity move
  instructions for these channels between these two cues, **they will be removed.** » Des
  mouvements sont supprimés dans des cues que l'utilisateur n'a pas nommées.
- ✅ **`Mark` est un interrupteur, pas un réglage.** Manuel §9 : « **Mark is a toggle
  state.** Therefore, the first mark command sets a mark. The second removes it. » Une
  macro qui pose une marque *retire* la marque si elle existait déjà — le résultat dépend
  d'un état antérieur invisible. Même famille que le mode `Format` en Patch et que
  `At Park` sans valeur.
- ✅ **Marquer vers une cue inexistante la crée.** Manuel §9 : « it is also possible to
  mark to a cue that doesn't exist, and when the mark is stored, **Eos will automatically
  create the cue** ». Une confirmation « Create Mark Cue? » apparaît sur la console — mais
  une macro qui répond `Enter` à l'aveugle crée une cue que personne n'a demandée.
- 📄 **Supprimer une courbe préprogrammée ne la supprime pas** : elle revient à son état
  d'origine. Une confirmation formulée « supprimer la courbe 901 ? » serait trompeuse.
- 📄 **`Thru Thru`** : un chiffre de décimale d'écart change la nature du résultat
  (décimales ou entiers) ; au-delà de 10 000 cibles, la commande est **ignorée en silence**.
- ⚠️ **Une mauvaise référence de gélatine** ne produit ni erreur ni refus : la macro
  s'exécute et donne la mauvaise couleur sur scène. Déduction évidente, mais c'est une
  déduction — aucune source ne l'énonce.
- ✅ **Une sélection perdue après un `Record`** (voir le préliminaire) : la suite de la
  séquence s'applique à rien. **Ce cas n'est pas théorique — il a été produit par ce
  projet.** La première macro générée pour une demande réelle (six palettes de couleur en
  série) était fausse à partir de sa deuxième palette, et elle a été relue, testée et
  livrée sans que rien ne la signale. Trouvé le 2026-08-06 en vérifiant le présent
  document contre le manuel. C'est l'illustration la plus nette de toute cette section :
  le texte de la macro était impeccable.
- ✅ **`{By Type}` sur une sélection large** fige silencieusement les channels surnuméraires.
  Le manuel §10 : « the lowest number channel of each fixture type will be the default
  channel [...] **any additional channels in that fixture type will be recorded with
  discrete data** ». La palette se crée, la console accepte, et elle contient l'inverse de
  ce qu'on voulait. À ne jamais présenter comme « une palette générique, donc pas besoin
  de choisir les circuits » : la sélection reste obligatoire, et doit idéalement tenir en
  un circuit par type d'appareil.

**→ Pour l'UI.** C'est ici que l'interface gagne ou perd sa valeur. Ces cas ne peuvent pas
être laissés au texte de la commande — il a l'air juste. Ils doivent être **traduits en
clair dans l'aperçu**, dans la langue de l'utilisateur, pas en jargon :

> ⚠ Cette macro enregistre les circuits 1 à 5. Le circuit 3 est parqué : il ne sera pas
> enregistré.

Le générateur produit déjà ces avertissements de façon structurée. **L'UI doit les
afficher, jamais les avaler** — c'est la règle non négociable du module `grammar/`.

Et le pendant côté confirmation : le libellé d'une confirmation destructrice doit décrire
l'effet réel, pas le verbe employé par l'utilisateur.

---

## 5. Trois issues, pas deux — la question est un état de première classe

**La règle.** Le traducteur ([`traducteur/`](traducteur/README.md)) ne renvoie pas
« compris / erreur ». Il renvoie trois états :

| État | Sens |
|---|---|
| `compris` | une macro, prête à relire |
| `a_preciser` | une ou plusieurs **questions**, avec leurs options |
| `incompris` | rien, et la liste des mots non reconnus |

⚠️ Le découpage en trois états est une **décision de conception du projet**, pas une
contrainte d'ETC. Mais elle repose sur un fait, lui vérifié :

✅ **la portée d'un enregistrement** — manuel §10, textuel : « [Record] will store the
relevant current parameter data for **all channels with non-default data** for the
appropriate palette type, **as modified by the filter settings**. » Et : « Otherwise all
channels with appropriate non-default data will be stored in the new palette. » Sans
sélection, un `Record` ratisse donc tout le plateau non-défaut — presque jamais
l'intention — et son résultat dépend en plus de l'état des filtres (règle 1). Motif
générique : vaut pour tout `Record` sans sélection explicite (presets, palettes de toute
famille, submasters).

📄 **une couleur ambiguë** — « ambre » a quatre candidats sérieux au catalogue officiel
Lee, « rose » aussi (`reference/lee_filters_theatre.md`).

`a_preciser` n'est pas un échec dégradé. C'est le comportement correct face à une
ambiguïté que **seul l'utilisateur peut lever**.

**→ Pour l'UI.** Il faut un **troisième écran d'état**, ni succès ni erreur : une question
avec ses options, présentée comme une étape normale du flux et non comme un échec. Une
interface qui n'a que « ça marche » et « ça ne marche pas » forcera tôt ou tard le
traducteur à deviner — et une couleur devinée passe tous les contrôles.

Contrainte de conception : les questions arrivent **structurées** (identifiant stable,
texte, pourquoi, options, et parfois une valeur à saisir). L'UI doit les rendre
génériquement, pas les coder en dur une par une — le lexique en ajoutera d'autres.

Le champ `pourquoi` mérite d'être affichable, en repli : il explique la question sans que
l'utilisateur ait à connaître la console.

---

## 6. Certaines intentions n'ont pas de traduction — l'app doit savoir dire non

**La règle.** Absences structurelles de la plateforme, reprises de §12 de la grammaire
consolidée. ⚠️ **Aucune n'a été re-vérifiée dans cette passe**, et trois d'entre elles ne
viennent pas du manuel mais de réponses ETC en forum ou support — une absence est par
nature difficile à sourcer dans une documentation :

- 📄 **Pas de variables ni de formules natives** (réponse ETC, demande sans suite depuis
  2010). L'indirection macro-dans-macro est le seul palliatif de la plateforme.
- 📄 **Pas d'auto-palette native** (réponse ETC, choix de conception assumé).
- 📄 **Pas de négation hors du sous-système Query** (réponse directe du support ETC).
  Toute intention « tout sauf… » passe par Query, ou n'a pas de traduction.
- 📄 **Un preset ne peut pas en référencer un autre.** « Le preset B, plus deux
  changements » n'a pas de traduction référencée.
- 📄 **Les channels à marquer sont obligatoires** : « Eos will not assume all automated
  fixtures apply to any given mark ». « Marque les asservis » n'a pas de traduction.

⚠️ **Avant de bâtir un écran « ceci est impossible » sur l'une de ces cinq lignes, la
re-vérifier.** Se tromper sur une absence est plus grave que se tromper sur une syntaxe :
l'app refuserait une demande parfaitement légitime, et l'utilisateur n'aurait aucun moyen
de savoir que l'app a tort.

S'y ajoutent des limites de l'outil, pas de la console :

- 📄 **La voie ASCII n'est pas générable** (#32) : sa spécification est absente du dépôt.
  « Injection OSC ou ASCII » doit se lire « injection OSC ». L'export ASCII est de toute
  façon une navigation dans le Browser, sans commande ni touche OSC.
- 📄 **Sept conditions Query n'ont pas de touche OSC** (#15) — atteignables au doigt
  seulement, potentiellement hors de portée de l'app.
- 📄 **`{Emergency Mark}` n'est pas générable** : c'est un réglage de Setup.

**→ Pour l'UI.** Un chemin « ceci n'est pas possible » de plein droit, distinct du refus
de la console et distinct du « je n'ai pas compris ». Avec, quand elle existe, la raison
en clair — « Eos n'a pas de variables » est une information utile ; un échec muet ne l'est
pas. Ce chemin ne doit **jamais** proposer de contournement approximatif.

---

## 7. Les numéros appartiennent à une conduite, pas à une macro

⚠️ **La règle** est une évidence de conception, pas un fait documenté. Une macro générée
référence des numéros propres à un spectacle : palette 5, groupe 12, cue 47. Importée sur
une autre conduite, elle reste **syntaxiquement valide** et pointe vers autre chose.

**→ Pour l'UI.** Déjà décidé dans `APP.md` — l'import **signale sans bloquer**. Ce qui
reste à concevoir : le signalement doit survivre à l'usage, pas seulement apparaître au
moment de l'import. Une tuile de favori importée d'un autre spectacle mérite de rester
identifiable comme telle jusqu'à ce que l'utilisateur l'ait validée une fois.

📄 Rappel utile : un `Group` sélectionne des channels et **ne contient jamais de niveaux**,
contrairement à une palette. La distinction compte dans les libellés affichés. (Corpus
#058/#082, confirmation ETC — **cherché sans succès dans le manuel §7 lors de cette
passe**, donc à re-vérifier avant d'en faire un texte affiché à l'utilisateur.)

---

## 8. Le transport impose ses propres règles

📄 **La règle.** Contraintes établies, non négociables (détail : `APP.md` § Contraintes
techniques, et §11 de la grammaire consolidée). ⚠️ **Aucune n'a été re-vérifiée dans cette
passe** — elles proviennent du journal terrain (S) et de tickets ETC rapportés par le
corpus (B), sources solides mais de seconde main ici :

- OSC sur TCP, port 3032. Ligne de commande via `/eos/cmd` ou `/eos/newcmd`.
- **User# dédié et fixe**, assigné dès la connexion, pour ne pas interférer avec
  l'opérateur travaillant sur la console.
- **Burst d'état initial** émis à la connexion : à absorber avant tout envoi.
- **Une commande envoyée mais non acquittée n'est jamais rejouée automatiquement** — le
  double déclenchement en pleine représentation est pire que l'absence d'effet.
- `Send_String` toujours en **dernière position** d'une macro multi-lignes [EOS-55864] ;
  `Macro_Wait` entre plusieurs `Send_String` déclenchés depuis un Client [EOS-53576].
- **Risque de corruption silencieuse (S)** : déclencher une macro pendant qu'une édition
  de macro est en cours sur la console insère les commandes dans l'édition au lieu de les
  exécuter. L'app ne peut pas détecter cet état.

Deux incertitudes qui peuvent changer la stratégie d'injection, pas seulement la syntaxe :

- **Les accolades `{…}` n'ont jamais été observées dans une chaîne `/eos/cmd`** (#18). Or
  toute commande portant un modificateur ou un style de Fan en contient. Si elles ne
  passent pas, il faudra décomposer en `/eos/key/<nom>` séparés.
- **`Go To Cue` en macro est non déterministe** (#14) selon Foreground/Background et le
  timing.

**→ Pour l'UI.** L'état de connexion s'affiche en permanence (déjà décidé). Ce qui en
découle pour la conception : une commande **en attente d'acquittement** est un état visuel
à part entière, ni envoyée ni échouée, et c'est l'utilisateur qui tranche. Prévoir aussi
que l'envoi d'une séquence puisse s'arrêter en cours de route sans que l'app sache où elle
en est — voir §3 pour le cas Blind, où c'est irrattrapable.

---

## 9. Le modèle n'est pas figé — les avertissements sont des données, pas du texte

**La règle.** Le backlog compte 36 points numérotés (numéros stables, jamais réattribués),
dont **25 sont encodés dans le modèle** comme zones `inconnu` reliées à leur numéro. Le
générateur avertit au lieu d'injecter en aveugle.

Et le modèle se corrige encore. Ce document lui-même a fait remonter deux erreurs le
2026-08-06 (#35 et #36, tous deux résolus) — dont une qui avait produit une macro fausse
livrée comme correcte. Une session UI qui trouve une contradiction entre ce document et le
manuel doit **suspecter le document**, pas le manuel.
Chaque validation au banc réel en remplit une, et **la formulation des avertissements
changera**. Certains disparaîtront, d'autres apparaîtront.

`inconnu` est une valeur de première classe du modèle, pas un trou à combler avant de
livrer.

**→ Pour l'UI.** Ne jamais coder un avertissement en dur dans l'interface. Ils arrivent
structurés depuis `grammar/` et doivent être rendus génériquement : un composant
d'avertissement qui affiche ce qu'on lui donne, en nombre variable, y compris zéro. Si un
avertissement disparaît du modèle demain, aucun écran ne doit être retouché.

Deux conséquences visuelles déjà actées dans `APP.md`, à respecter :

- une macro portant un ⚠ passe en **confirmation plein écran** — impossible à envoyer
  distraitement ;
- **aucun ⚠ ne peut apparaître dans les favoris**, propres par construction puisqu'une
  macro n'y entre qu'après acceptation *et* validation visuelle.

---

## État de vérification — à lire avant de bâtir dessus

Passe du 2026-08-06, contre le manuel officiel v3.2.0 et les workbooks.

| Partie | État |
|---|---|
| Préliminaire (anatomie de la syntaxe) | ✅ vérifié, sauf l'ordre des créneaux (⚠️ généralisation du projet) |
| Règle 1 — états invisibles | ✅ 3 des 5 vérifiés mot à mot ; 📄 patch et filtres non re-vérifiés |
| Règle 2 — refus / acceptation | ⚠️ doctrine du projet, appuyée sur des faits vérifiés |
| Règle 3 — Blind | ✅ vérifié cinq fois, cinq chapitres |
| Règle 4 — erreurs silencieuses | ✅ 7 items vérifiés (dont 3 ajoutés par cette passe) ; 📄 3 non re-vérifiés |
| Règle 5 — trois issues | ✅ le fait qui la fonde est vérifié ; ⚠️ le découpage est un choix de conception |
| Règle 6 — absences | ⚠️ **aucune re-vérifiée** — la partie la plus fragile du document |
| Règle 7 — numéros propres à une conduite | ⚠️ évidence de conception ; 📄 la note sur `Group` reste à confirmer |
| Règle 8 — transport | 📄 aucune re-vérifiée dans cette passe |
| Règle 9 — avertissements = données | ✅ vérifiable directement dans `grammar/` |

**Ce que cette passe a changé.** Trois items nouveaux en règle 4 (enregistrement sélectif
qui n'isole pas, `Mark` en interrupteur, marque créant une cue), deux affirmations
**élargies** parce qu'elles étaient trop étroites (le zéro implicite vaut pour tout
paramètre, pas seulement après `At` ; `Q Only/Track` n'a pas un sens variable mais un sens
**inversé**), et une affirmation **restreinte** parce qu'elle était trop large (l'ordre des
créneaux n'est pas une règle publiée).

**Ce qui reste à faire.** Les règles 6 et 8 n'ont pas été re-vérifiées à la source. La
règle 6 est la plus risquée des deux : une absence mal établie fait refuser à l'app une
demande légitime, et rien dans l'interface ne permettrait de s'en apercevoir.

---

## Ce qu'il faut retenir en une phrase

L'app n'est pas une télécommande : c'est un **atelier de préparation qui montre son
travail et déclare ce qu'il ignore**. Toutes les règles ci-dessus convergent vers la même
exigence — l'aperçu, l'avertissement et la question sont les trois éléments structurants
de l'interface, pas des ornements ajoutés autour d'un champ de saisie.

Et la syntaxe est assez régulière (Objet → Action → Cible) pour que cet aperçu soit
**structuré** plutôt qu'un bloc de texte : c'est une opportunité de conception, pas
seulement une contrainte.

## Où creuser

| Besoin | Fichier |
|---|---|
| Écrans, flux, décisions produit déjà prises | [`APP.md`](APP.md) |
| Syntaxe Eos de référence | [`reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md`](reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md) |
| Modèle exécutable, générateur, avertissements | [`grammar/README.md`](grammar/README.md) |
| Traducteur, questions, lexique | [`traducteur/README.md`](traducteur/README.md) |
| Les 34 points ouverts, numérotés et stables | [`PLANNING.md`](PLANNING.md) |
| Ce qui est vraiment prouvé, et par quoi | [`VERIFICATION.md`](VERIFICATION.md) |

# Les règles structurantes de la grammaire Eos — et ce qu'elles imposent à l'interface

Document de cadrage pour la session qui développe l'UI de l'app.

Il ne remplace ni [`APP.md`](APP.md) (la spécification produit : écrans, flux, décisions
déjà prises) ni [`reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md`](reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md)
(la référence de syntaxe). Il répond à une seule question, transversale aux deux :

> **Qu'est-ce que la grammaire Eos force l'interface à faire ?**

Neuf règles, chacune établie par le corpus, chacune avec sa conséquence directe sur l'UI.
Elles ne sont pas des préférences de conception : ce sont des propriétés de la plateforme.
Une interface qui les ignore produira des macros valides et fausses.

**Origine** : synthèse des 16 tranches de [`grammar/`](grammar/README.md), du manuel
officiel v3.2.0, du corpus de 174 entrées et du journal terrain. Les renvois `#n`
pointent le backlog de [`PLANNING.md`](PLANNING.md).

Une section préliminaire décrit **comment la syntaxe est structurée** — c'est ce que
l'interface affiche, et sa régularité conditionne ce qu'on peut en montrer.

---

# Préliminaire — l'anatomie d'une commande Eos

Avant les règles : la forme. Elle est plus régulière qu'il n'y paraît, ce qui rend un
aperçu structuré possible plutôt qu'un simple bloc de texte.

## La structure fondamentale : Objet → Action → Cible

**Confirmé A** (manuel v3.2.0, « Important Concepts » ; recoupé deux fois par le corpus).
La plupart des instructions répondent à trois questions, dans cet ordre :

| | Question | Exemple |
|---|---|---|
| 1 | **Qu'est-ce que j'affecte ?** | `Chan 1 Thru 5` |
| 2 | **Que doit-il faire ?** | `At` |
| 3 | **Quelle valeur ?** | `50` |

Tout le reste — modificateurs, temps, libellés — vient s'accrocher à ces trois étapes.
C'est ce principe, et non une grammaire formelle, qui est encodé dans
[`grammar/modele.yaml`](grammar/README.md) : la ligne de commande Eos est modale, une
EBNF forcerait à trancher des points jamais validés.

**Toutes les actions ne passent pas par la ligne de commande.** Softkeys, direct selects
et encodeurs la contournent entièrement — l'app ne peut donc pas tout exprimer sous forme
de texte injectable.

## L'ordre des créneaux dans une ligne

```
[sélection]  [action]  [valeur]  [modificateurs]  [Time …]  [Label …]  [Enter]
```

Deux règles d'ordre sont établies et doivent être respectées telles quelles :

- **Sur un `Go To Cue`, `Time` se pose toujours en dernier**, après les autres
  modificateurs (manuel §16). `{Manual}` en est exempté.
- **`Send_String` doit être en dernière position** d'une macro multi-lignes, sinon un
  `/r` parasite s'insère dans l'adresse OSC générée [EOS-55864].

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

| Brique | Forme | Note |
|---|---|---|
| Sélection | `1`, `1 Thru 10`, `1 Thru 10 + 15`, `1 Thru 10 - 5`, `Group 3` | `+`/`-` ajoutent et retirent |
| Sous-groupe | `( 1 Thru 4 )` | compte pour **un seul** channel dans un Fan, un effet, un parcours |
| Sélection conditionnelle | `Query {Isn't In} Beam Palette 25` | seul endroit du langage où existe une négation |
| Softkey | `{By Type}`, `{Mirror Out}`, `{Q Only}` | toujours entre accolades |
| Libellé | `Label <texte>` | comportement du clavier virtuel avec espaces **non observé** (#5) |
| Terminaison | `Enter` | sauf commandes auto-terminées, voir plus bas |

Numérotation : palettes de `0.001` à `9999.999`, presets 1000 maximum, trois décimales.

## Quatre propriétés qui ne se devinent pas en lisant une ligne

**La sélection survit à l'`Enter` — mais pas à un `Record`.** C'est une règle en deux
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

**Certaines commandes s'auto-terminent** et ne prennent pas d'`Enter` : `Out`, `+%`,
`-%`, `Level`, et les actions depuis les direct selects. Un `Enter` de trop ne provoque
pas d'erreur — il **valide la ligne suivante**. Et la liste d'ETC est incomplète de son
propre aveu (« Some, but not all, of these commands are »), d'où #19 : toute commande non
marquée comme auto-terminée est *présumée* avoir besoin d'`Enter`, ce n'est pas un fait
établi.

> **→ Pour l'UI.** Ne jamais « compléter serviablement » une commande avec un `Enter`.
> La terminaison est calculée par le générateur, commande par commande.

**Le même symbole a plusieurs sens — et les deux polysémies ne sont pas de même nature.**

| Symbole | Sens | Distingué par |
|---|---|---|
| `At` / `@` | niveau en Live, **adresse DMX en Patch** | l'**écran actif** — état extérieur à la phrase |
| `/` | 7 sens documentés : préfixe de cue list (`Cue 2/5`), montée/descente (`Time 4/3`), pourcentage de temps (`Time /50`), valeur DMX brute (`At / / 239`), univers/adresse (`At 2 / 146`), liste entière (`Cue 2/ Assert`), échelle de park (`At / 125 Park`) | la **position** dans la ligne |

La distinction compte : la polysémie de `/` est lisible dans le texte de la commande,
celle de `At` **ne l'est pas** — elle dépend d'un état que l'app ne contrôle pas. C'est
la règle n°1 ci-dessous, et le générateur peut au moins forcer l'écran (`Tab <n> Enter`).

**Fan n'est pas une commande.** C'est le comportement **implicite** de toute commande de
niveau ou de temps utilisant `Thru` ou une liste de références. La touche `Fan` ne sert
qu'à changer de *style* de répartition. `1 Thru 10 At 10 Thru 30 Enter` fane déjà, sans
qu'aucun mot ne le dise.

> **→ Pour l'UI.** Un utilisateur qui écrit « circuits 1 à 5 de 10 à 50 % » obtient un
> dégradé. C'est l'intention normale, mais rien dans la commande produite ne porte le mot
> « dégradé » : l'aperçu doit le dire en clair si l'app veut être relue utilement.

## On assemble des tokens, jamais du texte

Règle structurelle, issue d'une observation terrain (corpus #060) : une commande construite
par concaténation de chaînes — `"Go_To_Cue_" + str(n)` — **tronque les décimales** sur
console réelle. `Go To Cue 5.5` devient `Go To Cue 5`.

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

| État | Effet | Renvoi |
|---|---|---|
| Mode de patch By Channel / By Address | `5 At 100` patche deux choses opposées | #20 |
| Mode Q Only / Track | change ce qu'une modification propage aux cues suivantes | — |
| AutoMark vs marques référencées | réglage global *et rétroactif* de Setup | #24 |
| Cue list « courante » | change à chaque `Record`, `Go`, `Back` | #25 |
| État des filtres | change **ce qui est enregistré**, à texte de commande identique | #28 |

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

**La règle** (déjà posée dans `APP.md`, rappelée ici parce qu'elle est asymétrique et que
l'asymétrie se perd facilement dans une interface) :

- **Un refus est une preuve définitive** — la syntaxe est invalide, sans appel. C'est même
  la source de confiance la plus haute du projet (niveau S).
- **Une acceptation établit seulement que la commande est syntaxiquement valide.** Pas
  qu'elle fait ce que l'utilisateur voulait. Une commande valide peut agir sur les mauvais
  circuits, dans le mauvais mode, avec le mauvais filtre actif.

Le retour est exploitable : `/eos/out/cmd` diffuse la ligne en clair avec un flag d'erreur
(1 = erreur de syntaxe, 0 = ok, Eos 2.6.0+ — confirmé S, corpus #140).

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

**La règle** (confirmée A, répétée chapitre après chapitre du manuel — §17 en CAUTION,
§20, §18, §10) : en Blind, les éditions prennent effet **immédiatement**, sans `Record` ni
`Update`.

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

- **`At 5` vaut 50 %, pas 5 %.** Un chiffre unique après `At` reçoit un zéro implicite
  (manuel §6, cinq occurrences ; §22 le reconfirme). Facteur dix. *Résolu* : `05` = 5 %
  (confirmation utilisateur, S) — le générateur écrit systématiquement deux chiffres.
- **Une valeur parquée est exclue de tous les record targets.** Et le manuel §19 précise
  le cas encore plus vicieux : on *peut* régler manuellement puis enregistrer une valeur
  sur un channel parqué — « the values set and stored in live **do not actually output to
  the system** if the parameter is parked ». Une macro qui règle puis enregistre un channel
  parqué produit donc une cue correcte sur le papier et un plateau inchangé, sans qu'aucune
  erreur ne remonte.
- **Sélection = fusion, absence de sélection = remplacement.** Constante de la grammaire
  (cues §12, submasters §20, palettes §10). Mais l'assignation de channels à une
  **partition inverse la règle** : une liste nue *remplace*, il faut `+` pour ajouter.
- **`Mark Cue <n>` a un effet de bord silencieux** : il supprime les mouvements NP
  intermédiaires de ces channels, dans des cues que l'utilisateur n'a pas nommées.
- **Supprimer une courbe préprogrammée ne la supprime pas** : elle revient à son état
  d'origine. Une confirmation formulée « supprimer la courbe 901 ? » serait trompeuse.
- **`Thru Thru`** : un chiffre de décimale d'écart change la nature du résultat (décimales
  ou entiers) ; au-delà de 10 000 cibles, la commande est **ignorée en silence**.
- **Une mauvaise référence de gélatine** ne produit ni erreur ni refus : la macro s'exécute
  et donne la mauvaise couleur sur scène.
- **Une sélection perdue après un `Record`** (voir le préliminaire) : la suite de la
  séquence s'applique à rien. **Ce cas n'est pas théorique — il a été produit par ce
  projet.** La première macro générée pour une demande réelle (six palettes de couleur en
  série) était fausse à partir de sa deuxième palette, et elle a été relue, testée et
  livrée sans que rien ne la signale. Trouvé le 2026-08-06 en vérifiant le présent
  document contre le manuel. C'est l'illustration la plus nette de toute cette section :
  le texte de la macro était impeccable.
- **`{By Type}` sur une sélection large** fige silencieusement les channels surnuméraires.
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

`a_preciser` n'est pas un échec dégradé. C'est le comportement correct face à une
ambiguïté que **seul l'utilisateur peut lever**. Deux sont déjà encodées :

- **la portée d'un enregistrement** — `Record Color Palette` capture la sélection
  courante, ou *tous les channels non-défaut* si rien n'est sélectionné, ce qui n'est
  presque jamais l'intention. Motif générique : vaut pour tout `Record` sans sélection
  explicite (presets, palettes, submasters).
- **une couleur ambiguë** — « ambre » a quatre candidats sérieux au catalogue Lee.

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

**La règle.** Absences structurelles confirmées de la plateforme (§12 de la grammaire
consolidée) :

- **Pas de variables ni de formules natives** (A/B, ETC — demande sans suite depuis 2010).
- **Pas d'auto-palette native** (A/B, choix de conception assumé par ETC).
- **Pas de négation hors du sous-système Query** (B, réponse directe du support ETC).
  Toute intention « tout sauf… » passe par Query, ou n'a pas de traduction.
- **Un preset ne peut pas en référencer un autre** (A). « Le preset B, plus deux
  changements » n'a pas de traduction référencée.
- **Les channels à marquer sont obligatoires** : « Eos will not assume all automated
  fixtures apply to any given mark ». « Marque les asservis » n'a pas de traduction.

S'y ajoutent des limites de l'outil, pas de la console :

- **La voie ASCII n'est pas générable** (#32) : sa spécification est absente du dépôt.
  « Injection OSC ou ASCII » doit se lire « injection OSC ». L'export ASCII est de toute
  façon une navigation dans le Browser, sans commande ni touche OSC.
- **Sept conditions Query n'ont pas de touche OSC** (#15) — atteignables au doigt
  seulement, potentiellement hors de portée de l'app.
- **`{Emergency Mark}` n'est pas générable** : c'est un réglage de Setup.

**→ Pour l'UI.** Un chemin « ceci n'est pas possible » de plein droit, distinct du refus
de la console et distinct du « je n'ai pas compris ». Avec, quand elle existe, la raison
en clair — « Eos n'a pas de variables » est une information utile ; un échec muet ne l'est
pas. Ce chemin ne doit **jamais** proposer de contournement approximatif.

---

## 7. Les numéros appartiennent à une conduite, pas à une macro

**La règle.** Une macro générée référence des numéros propres à un spectacle : palette 5,
groupe 12, cue 47. Importée sur une autre conduite, elle reste **syntaxiquement valide**
et pointe vers autre chose.

**→ Pour l'UI.** Déjà décidé dans `APP.md` — l'import **signale sans bloquer**. Ce qui
reste à concevoir : le signalement doit survivre à l'usage, pas seulement apparaître au
moment de l'import. Une tuile de favori importée d'un autre spectacle mérite de rester
identifiable comme telle jusqu'à ce que l'utilisateur l'ait validée une fois.

Rappel utile : un `Group` sélectionne des channels et **ne contient jamais de niveaux**,
contrairement à une palette. La distinction compte dans les libellés affichés.

---

## 8. Le transport impose ses propres règles

**La règle.** Contraintes établies, non négociables (détail : `APP.md` § Contraintes
techniques, et §11 de la grammaire consolidée) :

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

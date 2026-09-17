# Passation — le traducteur et sa doctrine

À lire avant toute session portant sur `traducteur/`. Écrit le 2026-09-09 pour
la session suivante, à partir d'une session qui a resserré le projet sur le
traducteur seul et remis à plat plusieurs règles.

À lire dans cet ordre : ce fichier, puis `traducteur/README.md` (le détail
technique), puis `reference/journal_questions.yaml` (les questions ouvertes).
`CLAUDE.md` reste prioritaire sur tout — notamment sa règle n°2, qui interdit
de balayer `manuals/`, `corpus/` et `reference/` sans périmètre explicite.

---

## 1. Le périmètre a changé

Le projet ne construit plus une application. **L'interface est une conversation
Claude Code.** L'app web (`app/`) et l'envoi OSC sont mis de côté — pas
supprimés, pas maintenus. L'objectif unique est de rendre le traducteur
français → syntaxe Eos aussi efficace que possible.

Priorité affichée par l'utilisateur, dans cet ordre :

1. **Couverture** — avant la robustesse, avant la correction des cas limites.
2. **Le quotidien** — Sneak, Full, Select Last/Active, Label, Update, temps.

`app/data/` reste une copie gelée des sources servie à Pyodide. Si tu touches
`traducteur/traducteur.py`, `grammar/generateur.py`, `grammar/modele.yaml` ou
`traducteur/lexique.yaml`, lance `./app/build_data.sh` — et `--verifier` avant
de committer. Ce n'est pas décoratif : un moteur périmé a déjà failli partir
en production.

---

## 2. La doctrine, telle qu'elle est aujourd'hui

### La syntaxe Eos est la seule limite dure

Instruction explicite de l'utilisateur, le 2026-09-09 :

> « assouplis les règles pourvu qu'elles permettent de grossir le corpus du
> traducteur en respectant la syntaxe de Eos »

Tout le reste est négociable. Une règle du dépôt qui bloque une phrase
traduisible sans faire gagner en justesse syntaxique doit être remise en
question, pas défendue. Plusieurs l'ont été dans cette session, et à chaque
fois l'assouplissement n'a **rien** coûté en syntaxe : le modèle autorisait
déjà ce que le traducteur refusait.

### N'invente rien — mais ne refuse pas non plus par réflexe

La règle historique tient : le traducteur n'écrit jamais de syntaxe Eos. Il
produit une IR ; `grammar/modele.yaml` possède la syntaxe et
`grammar/generateur.py` l'écrit. Un mot absent du lexique produit un « je n'ai
pas compris », jamais une commande approximative.

Le corollaire, lui, a été appris à la dure : **refuser une phrase claire est
une faute au même titre qu'inventer.** Ça enseigne à l'utilisateur une limite
qui n'existe pas et le pousse à retirer des mots qui marchent. Deux cas réels
de cette session : « créer les palettes de couleur 1 à 6 » était refusé faute
de teinte à mettre dedans, alors qu'il demande limpidement des palettes vides ;
et un refus annonçait « aucun numéro trouvé » quand le vrai obstacle était un
mot inconnu.

### L'autorisation se LIT dans le modèle, elle ne se code pas

`_selection_courante_permise()` interroge la table `legalite` de
`modele.yaml`. Si le banc réel infirme une case un jour, on corrige le modèle
et le traducteur suit sans être retouché. Ne jamais réintroduire une liste
d'actions autorisées en dur dans `traducteur.py`.

### Trois résultats, pas deux

`compris` / `a_preciser` / `incompris`. Une question est un résultat de plein
droit, pas un échec dégradé. Quand plusieurs lectures d'une phrase mènent à
des commandes différentes et qu'aucune n'est plus probable, on **demande**.
Exemple vivant : les quatre familles de palettes ont des mot-clés différents,
donc « copie les libellés des palettes 1 à 5 » pose une question au lieu de
choisir.

### Rien ne tombe en silence

Toute information de la phrase ressort quelque part : dans la commande, dans
une question, dans un refus, ou dans les comptes rendus `non_reconnus` /
`ignores`. Une durée qu'aucune forme attestée ne sait porter fait **refuser**
la phrase en nommant le chemin qui marche — jamais produire la commande en
avalant les vingt secondes.

C'est la règle 4 de `REGLES_POUR_UI.md` : la panne la plus grave du projet est
celle qui ne lève aucune erreur.

### Une absence ne se prouve pas par une citation

Règle 6 de `REGLES_POUR_UI.md`. **Je l'ai enfreinte deux fois dans cette
session**, et les deux fois en toute bonne foi :

- j'ai déclaré le symbole `♦` « convention externe, zéro occurrence dans les
  13 manuels » — une capture de console montre que c'est ainsi qu'**Eos**
  affiche `Enter`. Un glyphe se perd à la conversion PDF → Markdown ;
- j'ai déclaré que `Time` était obligatoire après `Sneak` — le manuel écrit
  `[Sneak] <Time> [3]`, et sa page de conventions (§00 l. 339) dit que les
  crochets angulaires marquent les touches « which don't have to be pressed ».

Leçon opérationnelle : avant de conclure à une absence, vérifier la page des
conventions de notation du manuel, et se rappeler que le corpus converti n'est
pas la console.

### Une confiance ne se copie pas

L'échelle du projet : **S** = observé au banc réel, **A** = manuel, **B** =
ticket ETC rapporté, **C** = report de forum, **D** = rapporté peu fiable.

`grammar/refus_terrain.yaml` est le SEUL dépôt des constats de banc. Une
entrée marquée « confiance S » qui n'y a pas de trace est une confiance
usurpée. Une a été trouvée dans cette session (`Sub` + `intensite`, refusé en
S sans aucune observation derrière) et requalifiée `inconnu`/C.

Requalifier en `inconnu` et non en `oui` : constater qu'une syntaxe est écrite
et documentée ne prouve pas qu'elle fasse ce qu'on croit. Le générateur
avertit alors, au lieu de refuser **et** au lieu de se taire.

### Le mode Background n'est pas le contexte de l'opérateur

Manuel §24 l. 105-109 : « A macro in background mode that is run from a cue or
via show control will run on the **master device** ». Le nom interne du mode
Foreground le confirme — `foreground_mode` vaut `MACRO_USER`.

Conséquence : toute commande qui repose sur « la sélection en cours » peut ne
rien faire du tout, sans erreur. Le remède est de poser la sélection dans la
macro (`Select Manual`, `Select Active`, `Select Last`). La note émise par le
traducteur le dit ; ne pas l'adoucir.

---

## 3. L'assouplissement du 2026-09-09 et ses trois verrous

Le traducteur produit désormais des commandes **sans cible nommée** :
« monte à fond en 20 secondes » → `Full Sneak 20 Enter`. C'est ce qu'écrivent
les praticiens sur leurs boutons de magic sheet.

Ce qui protège n'est plus l'exigence du mot d'objet — c'était un filet **par
accident** — mais trois verrous explicites, dans
`_vise_la_selection_courante()`. Chacun vient d'un cas réel :

| verrou | cas qui l'a imposé |
|---|---|
| un objet nommé **sans numéro** reste une phrase incomplète | un numéro perdu à la frappe deviendrait un ordre sur une sélection inconnue |
| un mot de **cible** (`Sub`, `Preset`) interdit le repli | « sub 3 à 50 % » rendait `At 50 Enter`, un ordre sur des circuits quelconques |
| un seul **mot inconnu** interdit le repli | « passe le fondu de couleur à fond » rendait `Full Enter` — tout le plateau à pleine intensité |

Le troisième est le plus important et le moins évident. Agir sans cible nommée
suppose d'avoir compris la phrase **entière** ; un mot inconnu veut dire
qu'elle parle d'autre chose.

**Ne pas affaiblir ces verrous pour faire monter un score.**

---

## 4. Les six bancs, et pourquoi les deux derniers comptent

```
grammar/test_generateur.py          125 cas
traducteur/test_traducteur.py       155 cas de traduction + 9 de correction
traducteur/test_interpreter_flou.py   8 cas
traducteur/test_catalogue.py         44 phrases, 34 intentions
traducteur/test_corpus_terrain.py    43 entrées — RÉTRO-TRADUCTION
traducteur/test_silences.py         213 vérifications — INVARIANTS
```
(chiffres au 2026-09-14 ; les quatre premiers doivent être verts avant tout commit,
ainsi que `./app/build_data.sh --verifier`.)

Les quatre premiers comparent le traducteur à des attentes écrites par
l'agent. Ils protègent des régressions mais ne peuvent **structurellement
pas** révéler qu'une attente était fausse dès le départ — même boucle fermée
que les corpus de macros fabriqués audités dans cette session. Les deux
derniers sortent de cette boucle, chacun à sa façon.

`test_silences.py` (2026-09-17) ne compare à AUCUNE attente : il vérifie des
invariants que toute traduction correcte respecte, quelle que soit la phrase.
Un nombre écrit doit se retrouver dans la commande ou être signalé ; le
changer doit changer la commande ; la même demande dans plusieurs ordres de
mots doit donner la même commande. C'est le seul banc capable de trouver ce à
quoi personne n'a pensé — il a livré quatre pannes silencieuses le jour de sa
création : trois sur des plages de circuits, et une SYSTÉMIQUE — 32 des 38
intentions laissaient tomber une durée sans un mot, parce qu'un mot de durée
n'est pas rattrapé par `_ignores`. Corrigée par un garde-fou central dans
`_traduire_simple`, qui vaut d'office pour toute intention future. **Attention à son angle mort
propre** : une famille dont plus aucune tournure ne se traduit ne prouve plus
rien, donc il le signale explicitement (« FAMILLE MUETTE ») au lieu de passer
au vert.

`test_corpus_terrain.py` confronte le traducteur à `corpus/handy_macros_etc.yaml`,
la feuille collaborative ETC « Handy Macros » : 43 macros écrites par des
praticiens qui ne connaissent ni ce lexique ni ce modèle.

**Discipline sans laquelle ce banc ne mesure rien :** les phrases françaises du
YAML sont écrites depuis les colonnes *Label* et *Note* de la feuille, **avant**
toute exécution du traducteur. Les formuler d'après ce que le lexique accepte
déjà ne mesurerait que sa propre complaisance. Si tu ajoutes des entrées,
respecte cet ordre.

Un désaccord n'est **pas** un échec du traducteur : c'est une question, et elle
se tranche dans les deux sens. Le manuel §16 a déjà donné tort à la feuille sur
sa macro « Quickstep ». Seule la **régression** fait échouer le banc.

Score actuel : **3/26** sur les entrées comparables (2026-09-14). Le chiffre est bas
et c'est son intérêt — la couverture mesurée contre le modèle du dépôt (34 intentions
pour 85 actions) est un tout autre nombre que celle mesurée contre ce que les
praticiens écrivent. **Ne pas chercher à faire monter ce score directement** : il
monte quand un mécanisme réel arrive, jamais en pliant une entrée du corpus au
lexique. Les causes du reste sont **déclarées entrée par entrée** dans le corpus (champ
`cause:`) et affichées par le banc. Elles ne sont plus déduites du message de refus :
ce classement-là était faux, et il avait produit six jours de fausse priorité (voir
§7). Répartition au 2026-09-14 : 6 `action_absente`, 5 `mecanisme_absent`,
4 `navigation_relative`, 3 `forme_absente`, 2 `hors_ligne_de_commande`,
2 `macro_non_terminee`, 1 `source_douteuse` — et **zéro** `selection_implicite`.
Une entrée hors périmètre sans cause déclarée fait échouer le banc.

---

## 5. Ce qui reste à faire, par taille de bloc

**Mis à jour le 2026-09-14.** Deux lignes de ce tableau ont bougé — lire l'état, pas
le souvenir.

| famille | n | état |
|---|---|---|
| **macros multi-commandes** | 9 | **Le mécanisme est fait** (`_traduire_composee`, séparateurs « puis » et « ; »). Les 9 entrées du corpus ne passent toujours pas, mais plus pour cette raison : elles demandent des mécanismes entiers encore absents (`AllNPs`, `Macro_Loop`, capture `Wait_For_Input` en cours de macro). À re-qualifier une par une avant d'y retoucher. |
| **paramètres de projecteur** | 7 faits | **Résolu par la généricité, pas par l'accumulation.** Pan, Tilt, Zoom, Iris, Edge, Hue, Saturation passent tous par un seul chemin (`regler_parametre`), catalogués dans `grammar/modele.yaml` → `parametres:`. Ajouter Frost, Gobo ou autre = une entrée de données + une source, pas du code. |
| **actions absentes du modèle** | ~6 | Ce qui reste après les paramètres : `Color_Crossfade`, `Fan`/`Center`, `Query Live Moves`/`Dark Moves`, `Flexi`, `Form`, `Make Manual`. Chacune demande une recherche dans les manuels. |
| **vocabulaire seul** | ~7 | verbes et noms, aucun changement de règle. Le moins cher. |

Motif récurrent, à vérifier **avant** d'écrire du code : **`grammar/` est
régulièrement en avance sur `traducteur/`**. La tranche « quotidien » n'a
demandé aucune ligne au générateur ; l'assouplissement non plus ; `Thru Thru`
était déjà dans le modèle. Toujours commencer par tester le générateur
directement sur l'IR visée.

---

## 6. Questions ouvertes, à ne pas trancher au clavier

Toutes sont dans `reference/journal_questions.yaml` avec leurs sources.

- **La console peut être localisée**, et partiellement : sur une console
  francophone, `Jusqu'à` remplace `Thru` et `Palette_Couleur` remplace
  `Color Palette`, mais `Record`, `Label`, `Sneak`, `Time`, `Sub` restent
  anglais. OSC est indifférent à la langue. **Partiellement tranché le 2026-09-13**
  (`corpus/macros_show_reel.yaml`, show réel francophone, confiance B) : la saisie
  change aussi, pas seulement l'affichage — les deux familles de mots coexistent dans
  la même ligne de macro. Reste ouvert : la liste exacte des mots traduits, qui n'est
  documentée nulle part. Tant que ce n'est pas su, **ne rien promettre sur la fidélité
  visuelle du rendu.**
- ~~**`Sub` + `intensite`**~~ — **TRANCHÉ au banc le 2026-09-13, confiance S.** Les
  deux formes passent ; le fader du Sub a été observé montant physiquement à 50 % en
  2 s. `valide: oui` dans le modèle, et « sub 3 à 50 % » se traduit. Laissé ici barré
  et non supprimé : ce document a affirmé le contraire pendant cinq semaines, avec une
  confiance S imméritée. **C'est le rappel le plus utile de la section** — une absence
  d'observation n'est pas une observation d'absence.
- **Le second `Enter` de confirmation** sur `Copy To` et sur les créations en
  série : dépend d'un réglage de Setup invisible dans le texte de la macro.
  Le générateur avertit et ne choisit pas.
- **La tension « sélection implicite »** est atténuée, pas résolue. Trois
  issues possibles listées au journal ; c'est une décision produit.
- **Les nombres chiffre par chiffre** : les macros réelles stockent
  `Sub 9 0 5`, `Sneak 1 0`, `Color_Palette 1 0 1 0`. Le générateur écrit
  `Sneak 10`. Si c'est la forme stockée et pas seulement l'affichage d'un
  enregistrement par `Learn`, le rendu **d'une macro** doit changer — celui
  d'une ligne de commande, non.
- **`Clear_CmdLine` en tête, `Clear_Cmd` en queue** : idiome défensif observé
  dans des macros de production, non modélisé. Deux touches distinctes
  (`RESET_COMMAND_LINE` et `CLEAR`).

---

## 7. Pièges déjà payés — ne pas les repayer

- **Correspondance floue et routage.** Le flou est réservé aux créneaux,
  jamais à la détection d'intention (« groupe » est à distance 2 de
  « rouge »). Dans un créneau, **exact d'abord, flou ensuite** : sinon
  « palettes » gagne sur « couleur » et « lance » gagne sur « groupe ».
- **Clé YAML dupliquée.** `yaml.safe_load` garde la dernière en silence et
  perd la première. Le lexique se charge par `charger_lexique()`, qui refuse
  les doublons avec fichier et ligne. Ne pas revenir à `safe_load`.
- **Ordre de déclaration des intentions = priorité.** La plus spécifique
  d'abord. `verifier` doit précéder `regler_intensite` ; `creer_plage` doit
  suivre `creer_palettes_couleur`, lequel exige désormais un nom de teinte.
- **`declencheurs_optionnels`** ne participe pas au routage mais compte comme
  vocabulaire connu — c'est ce qui débloque le verrou du mot inconnu.
- **`_formater_niveau` complète à deux chiffres** (`05` = 5 %). Juste pour une
  intensité, faux pour une durée : `Sneak 08` n'est pas `Sneak 8`.
- **`Out` s'auto-termine** : pas d'`Enter`. `Full Full` et `Sneak Sneak` aussi,
  mais pas leur forme simple.
- **Un indicateur dérivé peut mentir pendant des jours** (payé le 2026-09-14). Ce banc
  devinait la cause d'un échec en cherchant « aucun numéro » dans le texte du refus, et
  en concluait « sélection implicite ». Sur 11 entrées ainsi classées, **aucune** ne
  l'était : `Chan 1 At 75 Check` nomme sa cible et se plaint d'un niveau ;
  `Color_Crossfade 50` est un réglage global sans sélection. Le chiffre avait fait
  inscrire au planning, en priorité n°1, un arbitrage produit qui ne débloquait rien.
  **Un message de refus dit ce que le traducteur a remarqué en premier, pas ce qui
  bloque.** Quand un chiffre sert à prioriser, lire d'abord comment il est calculé.
- **`_selection_de` / `_plage` mangent les nombres voisins** (payé le 2026-09-14, le
  pire bug de la session). Sans marqueur d'unité fiable, « hue à 180 sur le circuit 1 »
  rendait `Chan 180 Hue 1` — valeur et numéro **échangés**, statut `compris`, aucun
  avertissement. Un faux résultat silencieux, exactement ce que la règle 4 interdit.
  `_regler_parametre` n'appelle donc plus ces helpers du tout : il ne prend que le
  nombre **collé** au mot d'objet. Leçon générale : un helper générique qui lit « N à M »
  comme une plage est un piège dès qu'un autre nombre de la phrase n'est pas un circuit.
  **Tester au moins trois ordres de mots** avant de committer une extraction de nombre.

---

## 8. Ce que l'utilisateur apporte, et comment le traiter

Il transmet régulièrement des corpus de macros et des échanges de forums
(groupe Facebook « Eos francophone », communauté ETC), parfois avec des photos
de console. Trois audits ont déjà été faits, consignés au journal.

Méthode qui a fait ses preuves : vérifier chaque token contre
`reference/eosKeys.ts` (1155 clés), puis contre les manuels, puis contre
`corpus/CORPUS_EOS_COMPLET.md`.

Ce que ça a donné :

- deux corpus de « 100 macros » se présentant comme sourcés et notés 4/5-5/5
  se sont révélés **inutilisables comme source de syntaxe** — une douzaine de
  noms de commande sans aucune trace nulle part, et une échelle de confiance
  incompatible avec celle du dépôt ;
- la feuille communautaire ETC, elle, **tient** : son vocabulaire résout
  presque intégralement, et quatre de ses entrées recoupent mot pour mot des
  passages du dépôt qu'elle ne pouvait pas connaître. C'est la signature d'une
  provenance réelle.

Deux réflexes à garder. Un document qui s'auto-certifie est plus dangereux
qu'un document brouillon : les macros de la feuille ETC ont des cellules
perdues et des coquilles, et c'est précisément ce qui la rend crédible. Et une
réponse de forum juste sur le mécanisme peut omettre le piège qui compte —
celle sur `{Labels Only}` était correcte mais taisait le second `Enter` de
confirmation, qui décide si la macro fonctionne ou reste en attente.

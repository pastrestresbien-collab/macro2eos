# PLANNING — macro2eos

Backlog **vivant et unique** du projet. Remplace les trois listes de questions ouvertes
qui coexistaient et divergeaient (corpus « PRIORITÉS BANC », corpus « ZONES ENCORE
OUVERTES », grammaire consolidée §15) — celles-ci restent en place comme trace d'audit
mais ne sont plus à mettre à jour.

**Ce fichier reste volontairement court : l'état courant et le backlog ouvert, rien
d'autre.** Le récit détaillé, daté, tranche par tranche (« Fait — vX ») et les points de
backlog résolus avec leur justification complète vivent dans
[`PLANNING_HISTORIQUE.md`](PLANNING_HISTORIQUE.md) — à consulter sur besoin précis
(comprendre une décision passée), pas à relire à chaque session. Séparé le 2026-08-07
pour cette raison précise : ce fichier était relu en entier à chaque session et grossissait
sans fin. Rien n'a été supprimé, seulement déplacé.

Dernière mise à jour : 2026-09-14.

**Une seule branche de travail désormais : `claude/macro2eos-app-design-d9c3ou`.**
Elle succède à `claude/macro2eos-app-design-autk7k`, qui portait le prototype
d'interface développé séparément le temps que le traducteur existe ; les deux avaient
divergé, puis ont été fusionnés le 2026-08-07. Toute nouvelle session repart d'ici.

**Dernières nouveautés (2026-09-12 → 2026-09-14)** — détail dans l'historique Git :
- **Le traducteur compose les macros multi-commandes** (« puis », « ; »). C'était le plus
  gros bloc de la passation ; il est fait. Chaque segment est traduit séparément et doit
  être `compris` pour que l'ensemble le soit.
- **Mécanisme générique `regler_parametre`** : un seul chemin de code couvre Pan, Tilt,
  Zoom, Iris, Edge, Hue et Saturation, avec cinq formes possibles (absolue, relatif +/-,
  échelle `/`, DMX `//`). **Chaque paramètre ne déclare que les formes qu'une source
  atteste pour LUI** — rien n'est emprunté à un paramètre voisin. Ajouter un huitième
  paramètre est désormais une entrée de données, pas du code.
- **`Sub` + `intensite` est valide** — confirmé au banc réel le 2026-09-13, confiance S.
  Ceci **annule** l'avertissement inverse que ce fichier portait depuis le 2026-08-07 :
  « sub 3 à 50 % » produit aujourd'hui `Sub 3 At 50 Enter`. Ceci close la question datée
  du 2026-08-07 dans `reference/journal_questions.yaml` (elle n'a jamais eu de numéro de
  backlog propre ici — voir la note de correction dans ce fichier).
- **`CIE X` / `CIE Y`** documentés au banc : la forme qui marche est `CIE X <v> CIE Y <v>`
  avec **un seul** `Enter` final. `CIE XYY` est proposé par l'autocomplétion mais **invalide**
  en ligne de commande — piège encodé dans le modèle.
- **Corpus d'un show réel francophone** archivé (`corpus/macros_show_reel.yaml`, confiance B),
  qui tranche en partie la question de localisation de la console.

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

[`grammar/`](grammar/README.md) porte un modèle typé de **87 actions et 188 règles de
légalité**, plus un catalogue de **7 paramètres de projecteur** (Pan, Tilt, Zoom, Iris,
Edge, Hue, Saturation) rendus par un mécanisme générique unique. Le tout compilé en JSON,
avec un générateur qui produit trois sorties distinctes (ligne de commande, contenu de
macro, paquets OSC) et **140 cas de non-régression**, dont la majorité sont des exemples
chiffrés du manuel officiel recopiés verbatim.

[`traducteur/`](traducteur/README.md) traduit une phrase française en IR, que le
générateur rend ensuite — 38 intentions, 201 cas de traduction + 12 cas de correction,
et la composition multi-commandes (« puis », « ; »). Portée détaillée dans son propre
README.

| Axe | État |
|---|---|
| **A — structurer la grammaire** | ✅ terminé pour le périmètre visé (v0.16) |
| **B — écrire le traducteur NL** | 🚧 v0.20 — 38 intentions, 201 + 12 tests, 215 invariants, multi-commandes et paramètres génériques. Déterministe, sans IA à l'exécution (voir ci-dessous) |
| **C — valider au banc réel** | ⬜ non commencé — 38 points recensés au backlog (#29, #34, #35, #36, #37, #38 résolus) |

Ce qui reste hors périmètre du modèle : Augment3d, le pixel mapping, le serveur média
virtuel, le multi-console — et l'export ASCII, non par oubli mais faute de spécification
(#32). Le contrôle partitionné (§28) est couvert depuis v0.16.

---

## Axes de travail — Phase 2

Trois axes, indépendants entre eux. À prioriser par l'utilisateur. Le récit tranche par
tranche qui a mené à l'état courant de chaque axe est dans `PLANNING_HISTORIQUE.md`.

### A. Structurer la grammaire en données exploitables — **terminé (v0.16)**

Transforme `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` en un jeu de données interrogeable
(JSON/YAML) : vocabulaire des touches, règles de syntaxe, patrons de commande, niveau de
confiance par règle, risques associés. Sans cette étape, tout parser à écrire devrait
ré-encoder la grammaire à la main et divergerait de la doc dès la première correction.

**Approche retenue** (2026-08-01) : modèle typé Objet → Action → Cible + matrice de
légalité, plutôt qu'une grammaire formelle (EBNF) — la ligne de commande Eos est modale et
dépendante de l'état console, une EBNF forcerait à trancher des points non validés au
banc. `inconnu` est une valeur de première classe et renvoie au backlog ci-dessous.

Le résultat le plus important de seize tranches (2026-08-01 → 2026-08-03) n'est pas la
couverture mais la découverte que **le sens ou le résultat d'une commande Eos dépend
souvent d'un état que rien ne publie** — six cas recensés, table à jour dans
`REGLES_POUR_UI.md` règle 1. C'est l'argument le plus solide en faveur de la validation
utilisateur avant envoi.

Détail complet des 16 tranches (v0.1 → v0.16), du bilan de campagne et des contradictions
relevées : `PLANNING_HISTORIQUE.md`, section « Axe A ».

### B. Écrire le traducteur NL → macro — **commencé (v0.2)**

Le cœur du produit. Dépend de A pour éviter la duplication de la grammaire dans le code.
Prérequis déjà satisfaits : vocabulaire canonique, grammaire consolidée, référentiel de
risques, banc de transport OSC pour tester l'injection.

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

**Portée actuelle et détail des tranches v0.1 → v0.10** : `traducteur/README.md` (portée
à jour) et `PLANNING_HISTORIQUE.md` section « Axe B » (récit et constats de chaque
tranche).

**Reste à couvrir** : cue lists multiples, cues multipart, patch, magic sheets, show
control — la majeure partie des 85 actions du modèle. Mark, Park, Assert, Filtres,
Snapshots et Courbes (v0.5 → v0.9) ne couvrent chacun qu'une forme restreinte — voir
`traducteur/README.md` pour le détail exact des limites assumées. Contrôle partitionné
(v0.10) : seulement sélectionner/supprimer une partition, l'idiome `+`/`-` (ajouter/
retirer des channels à la partition courante) et l'assignation à une cue list précise
restent hors périmètre. Query n'est couvert que pour trois cibles (Color Palette, Preset,
Cue) et une seule condition à la fois. Le lexique se remplira par tranches, comme le
modèle l'a été.

**Bug corrigé (2026-08-11, trouvé le 2026-08-09 en construisant `parquer`)** :
`_regler_intensite` échouait silencieusement (`incompris`) sur une phrase à un seul
circuit suivie d'un niveau avec un seul « à » — « circuit 4 à 50 % » — parce que `_plage`
la lisait comme la plage de circuits 4 à 50 avant que le niveau ne soit examiné.
Fonctionnait déjà quand la phrase contenait deux « à » (« circuits 1 à 5 à 50 % ») ou un
marqueur sans « à » (« circuits 1 à 5 intensité 50 »). Corrigé directement dans `_plage`,
avec la suite de tests complète en main comme prévu : un nombre immédiatement suivi d'un
marqueur *postfixe* de niveau (`MARQUEURS_NIVEAU_POSTFIXES` — seulement `%`/`pourcent`,
« intensité »/« niveau » en sont délibérément exclus car eux s'emploient aussi en préfixe
d'un niveau qui suit) n'est plus jamais lu comme la borne haute d'une plage. Trois cas de
non-régression ajoutés à `test_traducteur.py` (le cas cassé, sa variante sous 10 % pour le
zéro de tête, et la forme « intensité » déjà correcte, pour vérifier qu'elle ne casse pas).
`_parquer` continue de bypasser `_plage` entièrement pour sa propre raison (voir
ci-dessus, et `PLANNING_HISTORIQUE.md` § Axe B v0.5) — inchangé, toujours limité à un seul
circuit/groupe.

**Moteur flou (2026-08-11) : un LLM en renfort, jamais en remplacement — phases 1 à 4
terminées.** Le traducteur ci-dessus reste seul à décider ce qui est ambigu ; un LLM
(Claude, clé API personnelle) ne fait que choisir parmi les options *déjà* proposées par
une question `a_preciser`, jamais deviner une intention depuis rien. Voir
`traducteur/build_vocabulaire_llm.py` (vocabulaire fermé exporté du même `lexique.yaml`),
`Traducteur.interpreter_flou` (`traducteur/traducteur.py`, ne touche jamais le réseau,
testé dans `traducteur/test_interpreter_flou.py`), `app/llm_bridge.js` (appel réseau réel,
revalidation stricte contre les options de la question avant tout passage à Python, testé
sans réseau dans `app/test_llm_bridge.js`) et `askEngineFlou` (`app/prototype.html`).
Raison du périmètre restreint : au pupitre, le téléphone est sur le Wi-Fi de la console —
donc **sans Internet**, le Wi-Fi coupant la 4G/5G même sans accès réseau — le LLM n'est
donc utilisable qu'en préparation ; tout échec (hors réseau, timeout, clé absente/invalide,
réponse hors vocabulaire) retombe silencieusement sur le moteur déterministe seul, sans
indicateur de mode.

**Phase 3 — journal de renforcement, patron `refus_terrain.yaml`.**
`traducteur/observations_llm.yaml` accumule trois types de constats (`vocabulaire_manquant`,
`candidat_rejete`, `intention_manquee`), alimentés depuis une file `localStorage` séparée
côté app (rien n'est journalisé tant que le moteur flou n'est pas explicitement activé),
exportée en YAML collable depuis Réglages. Promotion **toujours humaine** — un humain édite
`lexique.yaml` à la main et ajoute la balise `source_llm:` (distincte de `source:`/`choix:`,
elle-même distincte de l'échelle S/A/B/C/D). `traducteur/build.py` avertit (sans jamais
bloquer) quand un même mot revient au moins deux fois sans avoir été promu ni rejeté —
`verifier_observations_llm_recurrentes`, même esprit que
`grammar.build.verifier_refus_non_reportes`.

**Phase 4 — badge honnête.** Une traduction `compris` où le LLM a tranché une question
déjà posée porte désormais un petit indicateur (« Précisé avec l'aide du moteur flou »,
`app/prototype.html`, visible seulement avant envoi comme les hypothèses) — jamais laissé
ambigu sur l'origine de la macro : le corpus reste seul à l'avoir écrite, le LLM n'a fait
que lever l'ambiguïté. Le réemploi `Question`/`Option` pour le cas multi-candidats
(plusieurs propositions de confiance comparable) était déjà couvert par les tests de la
phase 1 (`traducteur/test_interpreter_flou.py`) ; la phase 4 confirme qu'il se comporte
identiquement une fois branché à un vrai (faux, pour le test) appel réseau, sans code
supplémentaire côté rendu.

**Phase 5 (2026-08-14) — discussion libre à plusieurs tours, pas un routage `_intention()`
modifié.** L'idée initiale de « rescaper un `incompris` » en touchant `_intention()`
elle-même (voir plus haut, phases 1-4) n'a pas été retenue — trop invasif pour un
mécanisme qui n'a jamais besoin de voir l'IR. À la place : quand l'utilisateur le demande
explicitement (bouton 💬, jamais automatique), un mini-fil de discussion s'ouvre où l'IA
peut poser des questions et proposer plusieurs formulations françaises sur plusieurs
tours — mais elle ne produit **jamais** de syntaxe Eos ni ne touche au vocabulaire fermé.
Chaque `phrase_a_essayer` qu'elle propose repasse par `window.traduireReel`, exactement
comme si l'utilisateur l'avait tapée lui-même : c'est le vrai traducteur, pas l'IA, qui
reste seul juge. Voir `app/llm_bridge.js` (`window.discuterLlm`) et
`app/prototype.html` (`avancerDiscussion`/`demarrerDiscussion`). Contrairement au premier
passage silencieux d'`askEngineFlou`, un échec ici est **affiché dans le fil**, jamais un
repli silencieux — l'utilisateur attend activement une réponse à ce qu'il vient de taper.
Garde-fous ajoutés en revue de code avant commit : les tours d'erreur ne sont jamais
envoyés à l'API (rôles strictement user/assistant, fusionnés si consécutifs — l'API
Anthropic attend une alternance stricte), et un double envoi pendant qu'une requête est
en cours est bloqué (`e.discussionEnCours`), pas juste visuellement désactivé.

### C. Valider au banc réel

Une session sur console/nomad réel lèverait d'un coup la majorité des incertitudes
listées plus bas. C'est le seul axe qui ne peut pas être fait depuis ce dépôt.

**Mécanisme d'accumulation (2026-08-02, élargi le 2026-08-07)** : chaque refus de la
console en usage réel — ou chaque cas accepté mais dont le résultat diffère de ce qui
était attendu, le plus dangereux des deux car rien ne le signale sur le moment (voir
`REGLES_POUR_UI.md`, règle 4) — est une preuve de niveau S (voir `APP.md`, « La console
fait autorité »). Au lieu de se perdre, ces constats s'enregistrent dans
`grammar/refus_terrain.yaml`, reliés à un numéro de backlog ci-dessous. `grammar/build.py`
signale si un constat tranche un point encore marqué `inconnu` dans `grammar/modele.yaml`
mais pas encore reporté. Le banc réel devient ainsi cumulatif plutôt qu'une session isolée
à programmer.

---

## Prochaine session — plan de travail (révisé le 2026-09-14, après mesure)

**Ce plan a été écrit une première fois le matin même, puis jeté.** Sa priorité n°0
— « trancher la sélection implicite, 11 entrées sur 23 » — était fausse. Elle venait du
banc terrain, qui *devinait* la cause d'un échec en cherchant « aucun numéro » dans le
texte du message de refus. Une qualification à la main des 23 entrées a montré que
**zéro** d'entre elles est bloquée par cet arbitrage :

- `channel_check` = `Chan 1 At 75 Check Enter` → cible **explicite**, il manque `Check` ;
- `address_check` = `Address 1 At 75 Check` → cible **explicite** ;
- `color_xfd_50` = `Color_Crossfade 50 Enter` → réglage **global**, sans sélection ;
- `out_next_level` = `Out Next Level` → navigation `Next`/`Last` ;
- `record_preset`, `startup` → macros **volontairement non terminées**, concept déjà modélisé.

Un message de refus dit ce que le traducteur a remarqué **en premier**, pas ce qui bloque.
Les deux coïncident rarement. La cause est désormais un champ `cause:` écrit à la main
dans `corpus/handy_macros_etc.yaml`, et une entrée hors périmètre sans cause **fait
échouer le banc** — pour qu'aucune ne s'ajoute plus en silence.

**La sélection implicite reste une vraie question de conception** (les boutons de magic
sheet visent bien « ce qui est sélectionné »), mais elle ne bloque aucune entrée mesurée :
elle sort donc du chemin critique. À trancher quand un usage réel la réclamera, pas pour
faire monter un score.

### Classement réel, par cause déclarée

| n | cause | ce que ça veut dire |
|---|---|---|
| 6 | `action_absente` | le mot-clé Eos n'est pas dans le modèle |
| 5 | `mecanisme_absent` | chaîne entière à construire |
| 4 | `navigation_relative` | désigne par position (`Next`/`Last`), pas par numéro |
| 3 | `forme_absente` | l'action existe, pas sous cette forme |
| 2 | `hors_ligne_de_commande` | pilote l'affichage — hors périmètre **par nature** |
| 2 | `macro_non_terminee` | finit exprès sans valeur, l'opérateur complète |
| 1 | `source_douteuse` | cellule de la feuille inexploitable |

Les 3 dernières lignes (5 entrées) ne sont **pas** du travail à faire : deux sont hors
périmètre par nature, deux relèvent d'un concept déjà modélisé
(`regles_generation.fin_volontairement_non_terminee`) qu'il suffira de câbler, une est
une source perdue. Le gisement réel est donc de 18 entrées, pas 23.

### 1. ~~Navigation `Next` / `Last`~~ — **fait le 2026-09-16**

`Out Next Level` et `Out Last Level` se traduisent (banc terrain 3/26 → 5/26). Les deux
variantes `Group` ont été **refusées volontairement** : le manuel §7 l. 175 dit que
`Next` après une sélection de groupe accède au premier circuit DU groupe, pas au groupe
suivant — le label de la feuille suggère un sens qu'aucune source ne confirme, et le
traducteur l'explique au lieu de rendre un `Next` trompeur (cause `sens_non_atteste`).

Deux trouvailles à ne pas perdre, détaillées au journal :
- « va au circuit suivant » rendait `Go To Cue Next Enter` — un saut de cue au lieu d'un
  déplacement de sélection, statut `compris`. Réglé par l'ORDRE de déclaration.
- **Le verrou 3 s'use tout seul.** Il ne tient que tant que le mot reste inconnu du
  lexique : ajouter « passe » a suffi à rouvrir le bug de `Full Enter` sur « passe le
  fondu de couleur à fond ». Contourné, pas corrigé — la vraie parade est le point 2.

### 2. ~~`Color_Crossfade`~~ — **fait le 2026-09-17**

Les trois entrées se traduisent (banc terrain 5/26 → **8/26**). Ce n'est PAS un réglage
global de console comme je l'avais écrit le 2026-09-14 — c'est un **paramètre de
projecteur**, donc le mécanisme générique `regler_parametre` l'a absorbé sans code
nouveau, avec une forme `plein` en plus (`Color_Crossfade Full`). Syntaxe en confiance B
(feuille), classement en paramètre en confiance **C** (inférence) : à trancher au banc,
avec la question de savoir si `Color Scrub` est la même chose.

**La mine du verrou 3 est désamorcée** : `regler_fondu_couleur` est déclarée avant
`plein_feu`, donc « passe le fondu de couleur à fond » ne peut plus rendre `Full Enter`.
« passe » est revenu dans les déclencheurs de navigation. Mais la leçon générale tient :
le verrou 3 s'use à mesure que le vocabulaire grandit, et cette parade est à refaire
pour chaque famille de phrases exposée.

### 3. ~~`Check`~~ — **fait le 2026-09-17**

Les deux entrées se traduisent (banc terrain 8/26 → **10/26**). `Check` était déjà
entièrement implémenté ; ce qui manquait était `Address` comme objet de sélection
(ajouté, manuel §6 « Address Check », confiance A) et les adresses dans les
déclencheurs de `verifier`.

Un vrai défaut corrigé au passage, de la famille déjà connue : `_selection_de` prenait
un nombre suivi de `%` pour un numéro de circuit. `_plage` appliquait déjà l'exclusion
à ses bornes, le repli « nombre isolé » non — l'asymétrie faisait refuser « vérifie les
circuits à 75 % » en annonçant « niveau manquant », soit **la mauvaise cause**.

### 4. Macro volontairement non terminée — **bloqué au banc, pas au clavier**

Examiné le 2026-09-17, puis **laissé en l'état délibérément**. La règle est bien dans
`grammar/modele.yaml`, mais en confiance B et avec la réserve du modèle lui-même : « à
vérifier au banc avant de l'utiliser dans une macro générée automatiquement par ce
projet ». Passer outre au clavier reviendrait à ignorer cette réserve — et une macro
qui s'arrête au mauvais endroit laisse une commande à moitié saisie sur une console en
exploitation.

Les deux entrées demandent de toute façon autre chose en plus : `record_preset` emploie
`Focus` et `Form`, qui ne sont pas des commandes mais des **boutons de page
d'encodeurs** (famille absente du modèle, et qui relève de la conduite au doigt) ;
`startup` emploie `Live Live`, une commande de contexte d'affichage, et son numéro de
snapshot manque sans qu'on puisse distinguer une macro ouverte d'une cellule tronquée.

**Question précise à poser au banc** : une macro dont la dernière ligne n'a pas d'`Enter`
laisse-t-elle vraiment la ligne de commande ouverte à l'opérateur ?

### Ordre imposé, quelle que soit la tâche choisie

Le motif récurrent de la passation : **`grammar/` est régulièrement en avance sur
`traducteur/`**. Chercher dans les manuels → tester le générateur sur l'IR visée →
seulement ensuite toucher au traducteur. Ne rien écrire sans exemple chiffré ; sans
exemple, la confiance est B et doit être écrite comme telle.

### Ce qu'il ne faut PAS faire

- Faire monter le score du banc en reformulant les phrases du corpus au goût du lexique :
  le banc ne mesurerait plus que sa propre complaisance (passation §4).
- Ajouter un 8ᵉ paramètre au catalogue « parce que c'est facile maintenant » sans source
  propre à celui-là. `Zoom + 10` n'est attesté nulle part, malgré `Pan + 10`.
- Rouvrir les verrous de sélection : plus rien ne le réclame.

### Nouveau garde-fou — le banc des silences

`traducteur/test_silences.py` (2026-09-17) est le sixième banc, et le seul qui ne
compare à aucune attente écrite : il vérifie des **invariants** (un nombre écrit se
retrouve dans la commande ou est signalé ; le changer change la commande ; plusieurs
ordres de mots donnent la même commande). C'est le seul capable de trouver ce à quoi
personne n'a pensé — il a livré **quatre** pannes silencieuses le jour même, dont une systémique : 32 des 38
intentions laissaient tomber une durée sans un mot (« parque le circuit 3 à 45 % **en 2
secondes** » → `Chan 3 At 45 Park Enter`). Corrigé par un garde-fou CENTRAL, pas par 32
correctifs — il vaut d'office pour toute intention future.

**À lancer avant tout commit**, au même titre que les cinq autres. Et à ÉLARGIR quand
on touche à une famille de phrases qu'il ne couvre pas : il n'aurait pas trouvé le bug
de plage si les familles de plage n'y avaient pas été ajoutées à la main.

### Dette de méthode

- **Vérifier qu'une confiance S porte sur une OBSERVATION, pas sur une pratique.**
  Précédent `Sub + intensite` : cinq semaines de refus injustifié. Un audit des
  légalités `valide: non` en confiance S est faisable sans console.
- **Se méfier d'un indicateur dérivé.** Celui-ci a orienté un planning entier pendant
  six jours. Quand un chiffre sert à prioriser, vérifier d'abord **comment il est
  calculé** — ici, un `if` sur trois chaînes de caractères.
- **Trois ordres de mots minimum** avant de committer toute extraction de nombre.

---

## Backlog technique — à valider au banc réel

Rien ci-dessous ne peut être tranché depuis le dépôt : il faut un Eos ou un ETCnomad.
Le simulateur `reference/tools/fakeeos.ts` ne valide que le transport, jamais la syntaxe.

**Les numéros sont des identifiants stables**, attribués dans l'ordre de découverte et
cités tels quels par `grammar/modele.yaml` et `grammar/refus_terrain.yaml`. Ils ne sont
donc jamais renumérotés : un point ajouté tardivement en priorité haute porte un grand
numéro. C'est la priorité de la section qui fait foi, pas l'ordre des numéros.

**Un point résolu n'est jamais supprimé** : il migre ici (en une ligne), avec sa date et
sa source — le récit complet de la résolution est dans `PLANNING_HISTORIQUE.md` § Backlog
résolu. Le numéro reste citable dans l'historique de `grammar/modele.yaml`.

### Résolu

- **#37 (2026-08-06)** — confiance sur-cotée (S au lieu de C) sur deux citations du corpus
  (#067, #060), propagée sans contrôle entre documents. Corrigée aux deux endroits.
- **#38 (2026-08-06)** — le piège `{By Type}` des palettes (règle 4 UI) s'applique
  identiquement aux presets, non encodé dans le modèle. `presets.options` ajouté.
- **#35 (2026-08-06)** — une sélection ne survit pas à un `Record` ; le modèle l'ignorait,
  ce qui avait produit une macro livrée fausse. Règle encodée, garde-fou structurel ajouté
  au générateur.
- **#36 (2026-08-06)** — `{By Type}` ne dispense pas de sélectionner des channels ; il
  décrit ce que la palette contiendra, pas comment elle s'enregistre. Corrigé dans le
  modèle, le lexique, `APP.md` et `REGLES_POUR_UI.md`.
- **#29 (2026-08-03)** — niveau sous 10 % : zéro de tête obligatoire (`05` = 5 %),
  confirmé par l'utilisateur (S). Appliqué systématiquement par le générateur.
- **#34 (2026-08-05)** — table de référence des couleurs Lee, résolue via le catalogue
  officiel « Art of Light » uploadé par l'utilisateur (~230 teintes, `reference/lee_filters_theatre.md`).

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

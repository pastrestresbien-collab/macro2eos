# PLANNING — macro2eos

Backlog **vivant et unique** du projet. Remplace les trois listes de questions ouvertes
qui coexistaient et divergeaient (corpus « PRIORITÉS BANC », corpus « ZONES ENCORE
OUVERTES », grammaire consolidée §15) — celles-ci restent en place comme trace d'audit
mais ne sont plus à mettre à jour.

Dernière mise à jour : 2026-08-02.

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

**Phase 2 — exploitation : pas commencée.** C'est là que se situe la bascule à décider.
Le dépôt est aujourd'hui à 100 % de la prose Markdown : excellent pour un humain ou un
LLM qui lit, inutilisable tel quel par du code. Rien dans le dépôt n'est encore
consommable par un programme, sauf `eosKeys.ts`.

---

## Axes de travail — Phase 2

Trois axes, indépendants entre eux. À prioriser par l'utilisateur.

### A. Structurer la grammaire en données exploitables — **démarré**

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

**Reste à faire** : Mark §9, cues multipart §17,
cue lists multiples §14, Park §19, Filtres §13, Courbes §22, Snapshots §23, Magic Sheets
§25, puis l'export ASCII. Ensuite, brancher la couche NL (axe B).

### B. Écrire le traducteur NL → macro

Le cœur du produit. Dépend de A si l'on veut éviter la duplication de la grammaire
dans le code. Prérequis déjà satisfaits : vocabulaire canonique, grammaire consolidée,
référentiel de risques, banc de transport OSC pour tester l'injection.

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

### Priorité haute — bloquent des décisions d'architecture

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

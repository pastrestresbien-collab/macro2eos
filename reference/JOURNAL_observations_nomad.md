# Journal d'observations terrain — nomad réel

Accumule ce qui est **constaté en conditions réelles** (par opposition au
documenté/supposé). Chaque entrée date, décrit le dispositif, et liste les
faits. Sert à figer la bibliothèque d'actions (R1/R7) et les défauts du pont.

---

## 2026-07-19 — Verrou de session : vol silencieux par le navigateur de Claude + reprise en un clic

Dispositif : configurateur web (`npm run webconfig`), deux onglets dans le
navigateur intégré de Claude Code + l'onglet navigateur habituel de Cy.

- **Cause d'une panne récurrente identifiée** : la détection « fenêtre
  dédiée » du verrou de session (server.ts) reposait sur la présence de
  `Electron` dans le User-Agent. Or le navigateur intégré de Claude s'annonce
  `… Claude/1.22209.0 … Electron/42.5.1 …` → il passait pour la fenêtre
  dédiée et **volait la session silencieusement** à chaque ouverture de la
  page. Corrigé : la vraie fenêtre dédiée ajoute un jeton explicite
  `PontEOS-FenetreDediee` à son UA (desktop/main.ts), seul ce jeton évince.
- **Reprise en un clic** : l'onglet refusé/évincé affiche désormais une
  bannière plein écran (même habillage que « Pont libéré ») avec un bouton
  « Reprendre la main ici » — reconnexion `?takeover=1`, même privilège
  d'éviction que la fenêtre dédiée mais sur geste explicite. L'ancien
  message « recharge pour reprendre » ne suffisait pas (la recharge se
  faisait rejeter aussi tant que l'autre onglet vivait).
- Éviction distinguée du refus : `busy` porte `evicted:true` quand on AVAIT
  la main (messages de bannière différents).
- Validé : 12 assertions session-lock-selftest + cycle complet au banc dans
  deux onglets (refus → bannière → reprise → éviction de l'autre).

## 2026-07-19 (suite) — Subs par encodeur muets : hypothèse baseline INFIRMÉE au nomad réel

Dispositif : nomad réel (127.0.0.1:3032, show « (sanstitre) », subs S 1-S 10
en page 1), script de diagnostic jetable (scratchpad), protocole sans
risque : lecture du niveau de Sub 1 via une banque OSC de lecture dédiée
(bank 9), puis envoi de `/eos/sub/1 <ce même niveau>` (aucun changement
d'état), écoute totale 6 s.

- **INFIRMÉ** (l'hypothèse ⚠ du 2026-07-17, cf. fix enc14) : Eos ne
  republie JAMAIS le niveau d'un sub — ni sur `/eos/sub/<n>` (même
  adresse), ni sur `/eos/out/sub/<n>`. Silence total après l'envoi.
  `/eos/sub/999` (inexistant) : silence aussi, pas même une erreur.
- Conséquence : la baseline des mappings `accumulate` (enc13/enc14) ne
  pouvait JAMAIS se remplir → encodeur sub muet pour toujours (sécurité
  anti-saut) — c'est la panne constatée au dernier banc. S'y ajoutait un
  bug de code : la baseline écoutait `osc.address` telle quelle, alors que
  toute sortie Eos non-banque est préfixée `/eos/out/`.
- **Seul canal publiant les niveaux de subs** : la banque de faders OSC
  (`/eos/fader/<bank>/<n>`, aller-retour même adresse, écho ~520 ms —
  reconfirmé aujourd'hui : `/eos/fader/9/1` 0.22 + noms S 1-S 10).
- **Correctif** : `osc.baselineFrom` (config.ts) — adresse DISTINCTE de
  lecture de la baseline ; enc13 (Sub 1) → `/eos/fader/1/1`. L'UI
  « Contrôler un Sub » expose le champ avec explication. enc14 (sub 999,
  mapping de test) reste muet par nature : sub inexistant, porté par aucun
  fader. ⚠ Limite assumée : la correspondance sub ↔ fader de banque dépend
  du show (ici page 1 = S 1-S 10).
- À valider au banc : tourner enc13 → gradation renvoyée sur le fader 1 du
  X-Touch (moteur suit via l'écho de banque).

**Échelle Pan/Tilt sur l'anneau LED** : retour utilisateur après le correctif
de dé-duplication — l'anneau suit bien Intens (0-100 %) mais donne un rendu
faux pour Pan/Tilt (Chauvet Colorado, plage ±270°). Cause : `wheelPercent`
divisait bêtement `value/100`, valable pour la plupart des paramètres mais
pas pour Pan/Tilt qui sont en degrés sur une plage bien plus large. Or Eos
diffuse justement cette plage : `/eos/out/pantilt` envoie
`panMin panMax tiltMin tiltMax panActuel tiltActuel` (ex. `-270 270 -115 115
-56.1 -12`, capturé dès le 2026-07-03 mais pas exploité jusqu'ici). Le pont
l'écoute maintenant (`parsePanTiltRange`) et calcule le vrai pourcentage
`(value - min) / (max - min)` pour les molettes nommées exactement « Pan »
et « Tilt » ; les autres paramètres restent en repli `value/100` (limite
documentée, pas de plage universelle disponible côté Eos).

**Accélération par poussée des encodeurs** (demande utilisateur) : maintenir
un encodeur enfoncé multiplie son delta de rotation avant l'envoi OSC
(`pushAccelerateFactor`, défaut ×5). Implémenté génériquement (positions
indépendantes, Set de positions poussées) pour s'appliquer à un nombre
quelconque d'encodeurs sans coût : la poussée ne fait que multiplier un
nombre en mémoire avant l'envoi OSC déjà coalescé/throttlé — **aucun trafic
MIDI/OSC supplémentaire**, donc pas de risque de saturation même sur 16
encodeurs. Notes de poussée = carto d'usine (poussées encodeurs 1-4 = notes
0-3, couche A). Activé au preset (`encoderPushNotes: [0,1,2,3]`).

---

## 2026-07-06 (suite, même jour) — Hypothèse CC+16 INFIRMÉE au banc réel

L'entrée ci-dessous (« le bon CC était CC+16 ») reposait uniquement sur la
lecture du tableau RX MIDI CONTROL de l'éditeur, **jamais testée au
matériel**. Testée ensuite avec le X-Touch réel (anneau réglé en mode Fan,
`tools/validation/midi-send.ts`, observation à valeur fixe sans minuteur) :

- `CC10 canal 1 = 0` → anneau éteint ✔
- `CC10 canal 1 = 64` → anneau à moitié ✔
- `CC10 canal 1 = 127` → anneau plein ✔

**Le CC de valeur est bien le MÊME que le CC de rotation, pas +16.**
`ringCCs` remis à `[10, 11, 12, 13]` (= `encoderCCs`) dans le preset. Le
tableau RX MIDI CONTROL de l'éditeur reste vrai en tant que documentation du
firmware, mais son interprétation ("CC26-41 = valeur d'anneau en mode
standard") était incorrecte pour notre usage — peut-être une fonction
annexe (2e banc d'encodeurs 9-16, mode MC...) non identifiée.

**Leçon retenue** : ne jamais figer un comportement matériel à partir de la
seule lecture d'un tableau/menu d'éditeur — toujours revérifier avec un
envoi MIDI réel et une observation confirmée avant de coder en dur.

---

## 2026-07-06 — Anneaux LED : hypothèse initiale (CC+16) — voir correction ci-dessus

> ⚠ Cette entrée décrit une hypothèse qui s'est révélée FAUSSE au test
> matériel (voir l'entrée du dessus, même date). Conservée pour la trace
> historique du raisonnement, pas comme référence technique.

**Constaté dans l'éditeur X-Touch (onglet GLOBAL > RX MIDI CONTROL)** : les
CC REÇUS par le X-Touch pour CC10–25 pilotent le **MODE** de l'anneau LED
(Single/Pan/Fan/Spread/Trim), pas sa valeur — alors que ce sont exactement
les mêmes numéros que les CC ÉMIS par la rotation des encodeurs (TX). Le CC
de **valeur** réelle de l'anneau est CC26–41, soit **+16** par rapport au CC
de rotation du même encodeur.

Le preset envoyait la valeur sur `ringCCs = encoderCCs` (CC10-13) : ça
changeait le mode de l'anneau à chaque tick au lieu de sa position — c'est
très probablement l'explication du « pointeur qui tourne de façon erratique »
observé à la sonde plus tôt. Corrigé : `ringCCs: [26, 27, 28, 29]` explicite
dans le preset ; `WheelBank` n'a plus de repli implicite sur `encoderCCs`
(si `ringCCs` est absent, aucun CC d'anneau n'est envoyé, plutôt que de
deviner un mauvais numéro).

Réglage matériel nécessaire en complément (éditeur X-Touch, onglet
ENCODERS) : passer **LED RING** de **Trim** (par défaut, mode pointeur) à
**Fan** (remplissage en barre) pour les encodeurs 1–4. Procédure complète :
`docs/SETUP_XTOUCH.md`.

---

## 2026-07-04 (session autonome) — Améliorations inspirées de Luminosus

Comparaison du pont avec `_reference/LuminosusEosEdition` et implémentation :

1. **Anneaux LED des encodeurs** (demande utilisateur) — Eos publie la valeur
   d'affichage entre crochets (`/eos/out/active/wheel/<n>` → `"Intens  [61]"`).
   Le pont l'extrait et l'envoie en CC sur l'encodeur (valeur/100 → position
   d'anneau), exactement comme `EosEncoderBlock::onIncomingEosMessage` de
   Luminosus. Sur le X-Touch Compact, l'anneau se pilote par le CC de
   l'encodeur. Dé-duplication par position. ⚠ à VÉRIFIER visuellement au banc
   (le mode d'affichage de l'anneau — point/barre — se règle dans l'éditeur
   Behringer). Bipolaires (Pan/Tilt) : seule la part positive remplit
   l'anneau (comme Luminosus) — amélioration possible via /eos/out/pantilt.
2. **Keepalive + détection de connexion morte** (repris de
   `EosOSCManager::updateLatency`/`onLatencyTimeout`) : ping identifié toutes
   les 10 s, délai de garde 1,5 s annulé par tout message entrant ; à
   expiration → reconnexion forcée (TCP ne détecte pas seul une connexion à
   moitié morte). Latence exposée dans l'UI et le runner.
3. **Ré-init des banques de faders au chargement d'un show**
   (`/eos/out/event/show/loaded`) — Luminosus renvoie /eos/subscribe + reconfig
   sur cet événement ; on reconfigure les banques (sinon faders morts après un
   changement de show).

Piste NON tranchée (à valider avec l'utilisateur) : pagination rapide via
`page_encoders_up`/`_down` (touches dédiées) au lieu de la répétition de
`encoder_category_*` (limitée à ~1/s par Eos) — outil `key-burst.ts --loop`
prêt pour l'essai `page_encoders_up`.

---

## 2026-07-03 — Observation passive, nomad piloté par un autre logiciel

**Dispositif** : ETCnomad **3.3.5.69** (console en **français**) sur la machine
de régie, piloté par un logiciel tiers via le X-Touch (ports MIDI monopolisés
par ce logiciel). Observation **passive** : client TCP supplémentaire sur
`127.0.0.1:3032` (`tools/phase1/observe-eos.ts`), 9 minutes, 444 messages,
52 adresses distinctes. Journal brut : `tools/phase1/logs/observe-session1.jsonl`
(non versionné).

### Faits établis

1. **Framing : ce nomad est en TCP OSC 1.1 (SLIP)**, pas 1.0 packet-length
   (le défaut du HANDOFF). Premier octet reçu `0xC0` = délimiteur SLIP.
   → Conséquence codée : auto-détection de framing dans `EosOscClient`
   (discriminant fiable : un flux 1.0 ne commence jamais par `0xC0`, un flux
   SLIP jamais par `0x00`), testée dans `tools/phase0/selftest.ts`.

2. **Eos accepte plusieurs clients TCP simultanés** et diffuse ses sorties à
   tous — l'observation passive pendant qu'un autre logiciel pilote fonctionne.

3. **À chaque connexion TCP, Eos rejoue tout son état** (~40 messages en
   ~130 ms) : `show/name`, `user`, cues active/previous/pending (+`/text`),
   12 softkeys (**libellés localisés FR** : « Exécuter », « Propriétés »…),
   `wheel`, `switch`, `active/chan`, `color/hs`, `pantilt`, `xyz`,
   `event/state`, `event/locked`. → Le pont peut initialiser LEDs et faders
   dès la connexion, sans requête.

4. **Version** : `/eos/get/version` → `/eos/out/get/version "3.3.5.69"
   "3.3.5.19" 0` (requête sans effet, utilisable au diagnostic).

5. **Candidats LED observés** :
   - bump de sub : `/eos/out/event/sub/<n>` (int **1** à l'appui, **0** au
     relâchement) ;
   - Go : `/eos/out/event/cue/<liste>/<cue>/fire` ; Stop :
     `/eos/out/event/cue/<liste>/<cue>/stop` (arg string vide).

6. **Aucun `/eos/out/sub/<n>` (niveau float) ni aucun `/eos/fader/...` en
   9 minutes**, alors que des subs étaient bumpés et des cues déclenchées.
   Le feedback de **niveau** n'est donc pas spontané — soit il n'apparaît que
   sur vrai changement de niveau (non testé ici), soit il faut passer par les
   **banques OSC** (`/eos/fader/<bank>/config/...` puis niveaux sur
   `/eos/fader/<bank>/<n>`). ⚠ À trancher au banc actif — impacte le feedback
   moteur du preset (actuellement `from: /eos/out/sub/<n>`).

7. **Molette d'intensité (R1, côté lecture)** : `/eos/out/active/wheel/1`
   `("Intens  [92]", 1, 92.1)` — cadence observée ~75 ms (≈13 Hz) pendant la
   manipulation. Le retour existe et est riche (libellé + valeur float).
   Le pilotage du **master fader** reste non testé.

8. **Ligne de commande diffusée en clair** : `/eos/out/cmd` et
   `/eos/out/user/<u>/cmd` `(texte, flag_erreur_int)` — ex.
   `"LIVE: Cue 2 : Sub 2 Bouton Go Go Bump #"`, erreurs signalées par le flag
   à 1 (« erreur de syntaxe »). Idéal pour le moniteur de l'UI (phase 3).

### Toujours ouverts (nécessitent un test actif)

- **R7** — noms `/eos/key/<nom>` : aucun `/eos/out/key/...` n'a circulé.
- **Écho fader +3 s** — invisible en passif (il faut corréler avec ses envois).
- **R1** — master fader pilotable ? Niveaux de subs sur `/eos/out/sub/<n>` ?
- Numéros MIDI du preset d'usine (touch-sense, boutons) — port MIDI occupé.

---

## 2026-07-03 — Levées documentaires (sans matériel)

**R7 (documenté)** : liste officielle ETC « Eos OSC Keys » récupérée et
convertie en module : `src/shared/eosKeys.ts` — **1155 touches** (nom OSC →
commande interne). Constats notables :
- `stop_0` **n'existe pas** (utilisé à tort dans la maquette) : le stop du
  master playback est **`stop`** (STOP) ; `go_0` = GO, `go` = PLAYBACK_GO,
  `stopback` = PLAYBACK_STOP_BACK. Preset corrigé.
- Insensible à la casse ; l'espace remplace `_`.

**Carto MIDI d'usine du X-Touch Compact (documenté)** : extraite du manuel
Behringer → `REFERENCE_xtouch_carto_usine.md`. Correction majeure : le
**touch-sense est un CC (couche A : CC101–109)**, pas une note. Moteur, config
et preset adaptés (les deux types restent gérés).

## 2026-07-03 (après-midi) — Banc ACTIF sur le nomad réel (matériel libéré)

`npm run validate` (section OSC) + captures MIDI + pont réel. **Constaté** :

1. **Pas de feedback de niveau sur `/eos/out/sub/<n>`** : `/eos/sub/1` mis à
   0.75 → aucun retour en 8 s. Le feedback moteur DOIT passer par les
   banques OSC. → Preset refondu : faders via `/eos/fader/1/<n>` (aller ET
   retour sur la même adresse).
2. **Banques OSC opérationnelles** : config acceptée, labels reçus
   (« S 1 »…« S 10 » — la page 1 du show porte les subs), **écho de niveau
   à +522 ms** (bien plus court que les « +3 s » documentés ; la fenêtre
   anti-écho de 4 s couvre les deux cas).
3. **Aucun écho `/eos/out/key`** pour les touches envoyées en OSC → pas de
   feedback LED possible par ce canal ; utiliser les événements
   (`/eos/out/event/sub/<n>` 1/0 constaté, `/eos/out/event/cue/...`).
4. **Auto-détection de framing validée en réel** : connexion 1.0 →
   détection sur le premier octet → reconnexion en 1.1 → dump d'état complet.
5. **Carto MIDI (partielle)** : fader 1 = **CC1 ch1** et master = **CC9 ch1**
   (0–127) confirmés au réel — conformes au manuel. ⚠ **Aucun événement de
   touch-sense observé** pendant les mouvements de fader (CC101 attendu,
   rien reçu) : touch désactivé dans la config actuelle du X-Touch ?
   À revérifier (l'anti-« lutte » reposerait alors sur la seule suppression
   d'écho). Encodeurs/boutons non capturés (session interrompue, X-Touch
   débranché ensuite).
6. **Pont réel contre nomad réel** : à la connexion, init de banque
   automatique → Eos renvoie les niveaux initiaux `/eos/fader/1/1..10` →
   le moteur émet les ordres CC1–9 de positionnement des moteurs (fader 10
   non mappé correctement ignoré). **Chaîne feedback phase 2 validée côté
   protocole** ; reste le physique (moteurs, mains) quand le X-Touch revient.

Reste ouvert : R1 (manual master à confirmer à l'écran), touch-sense,
encodeurs (mode absolu/relatif réel), notes exactes des boutons, écho moteur
(`tools/validation/motor-echo-test.ts` prêt, X-Touch absent).

## 2026-07-03 (suite) — Carto MIDI complète + moteurs, X-Touch rebranché

1. **Écho moteur : AUCUN.** Fader 1 et master pilotés par CC sortant (le
   fader a physiquement bougé, confirmé visuellement) → zéro événement MIDI
   entrant. L'anti-boucle est correcte sans filtrage supplémentaire.
2. **Encodeur 1 (CC10) : RELATIF complément à deux** — droite = 1,
   gauche = 127, un tick par cran, aucune accélération matérielle
   (distribution mesurée : {1×35, 127×28}). Le manuel ne le précisait pas ;
   le décodage Luminosus (`relative1`) est le bon. Preset corrigé.
3. **Boutons/poussées conformes au manuel** : poussée encodeur 1 = note 0,
   rangées 1/2/3 = notes 16/24/32, colonne droite = note 54 (plage 49–54).
4. **Touch-sense : CONFIRMÉ ABSENT** — doigt posé 2 s sur le fader 1, aucun
   CC101. La config actuelle du X-Touch n'émet pas le touch (réactivable via
   l'éditeur Behringer ?). Anti-« lutte » = suppression d'écho seule.

---

## 2026-07-04 — Synchro GUI des catégories d'encodeurs : 4 pièges constatés

En développant la banque de molettes dynamique (validée en réel avec le
Chauvet Rogue), quatre comportements d'Eos constatés au banc :

1. **`/eos/out/active/chan` est rebroadcasté quand SEUL le niveau change**
   (ex. `"14  [61]"` → `"14  [55]"`), et Eos ne republie alors que les
   molettes modifiées → ne vider la liste des molettes que si la partie
   « circuits » change.
2. **Les clés nues `intensity`/`focus`/`color`… sont les FILTRES
   d'enregistrement** (`*_CAT`) — les touches qui basculent l'affichage
   encodeurs de la GUI sont **`encoder_category_intensity`/`_focus`/
   `_color`/`_image`/`_shutter`/`_form`/`_custom`**.
3. **La GUI avale les paires down/up explicites en cadence rapide** ; la
   frappe **sans argument** (appui+relâchement implicites, forme Luminosus)
   est la forme fiable.
4. **Eos supprime les répétitions consécutives de la MÊME touche OSC
   espacées de moins de ~1 s** (mesuré à la rafale calibrée
   `tools/validation/key-burst.ts` : à 700 ms une frappe sur deux passe, à
   1000 ms tout passe ; les touches *différentes* passent sans limite ; le
   clavier n'est pas concerné ; l'alternance de casse ne contourne pas —
   la touche est normalisée avant l'anti-répétition). → Le pont applique
   la même règle (`sameKeyMinIntervalMs`, défaut 1000 ms) : un ré-appui
   trop rapide est ignoré des deux côtés, X-Touch et GUI restent synchrones.

Divers : le X-Touch éteint localement la LED d'un bouton au relâchement →
le pont ré-affirme l'état des LEDs après chaque noteOff de bouton de
catégorie.

---

**Protocole Eos selon Luminosus (code source, `_reference/`)** :
- messages préfixables par utilisateur : `/eos/user/<u>/key|fader|wheel/...` ;
- banque de faders : `/load`, `/unload`, `/stop`, `/fire` par fader,
  config renvoyée à chaque connexion (`onEosConnectionEstablished`) ;
- molette : `/eos/active/wheel/coarse|fine/<param>` ou
  `/eos/user/1/wheel/...`, valeur relative, accélération ×2 si |delta|>1 ;
- **décodage encodeur relatif en complément à deux** (127 = −1) — convention
  différente du sign-magnitude Mackie (65 = −1) → le moteur supporte
  désormais les 3 encodages relatifs Behringer (`relative1/2/3`).

---

**Pagination native des encodeurs (banc 2026-07-06, nomad 3.3.5.69,
Rogue R2 Wash + Clay Paky HY B-EYE K15)** :
- La page d'encodeurs affichée par Eos n'est PAS publiée en OSC (cliquer
  les onglets de catégorie sur la GUI n'émet rien ; demande communautaire
  « subscribe to the active encoder page » jamais implémentée par ETC).
- Règle constatée à l'écran, identique sur les deux projecteurs :
  Pan/Tilt épinglés SEULS en première page de Focus (comme les deux gros
  encodeurs d'une Ion/Gio), le reste dans l'ordre des index Eos par
  tranches de 4. Ex. Rogue Focus : [Pan, Tilt] · [X/Y/Z Focus, MSpeed] ·
  [Blink] ; K15 Color (16 params, sans Pan/Tilt) : 4 pages de 4 dans
  l'ordre exact de /eos/out/active/wheel/<n>.
- → WheelBank réplique cette règle (méthode pages()) pour que les
  encodeurs du X-Touch restent corrélés à l'écran d'Eos, quel que soit
  le projecteur (la liste OSC EST l'ordre du profil du patch).

---

**Fenêtre morte à la pagination — enquête EN COURS (banc 2026-07-07, K15 +
Robe à couteaux)**. Symptôme : en tapotant vite le bouton de catégorie
(Focus) du X-Touch, certaines pressions n'avancent pas la page à l'écran
Eos ; il existe un « intervalle mort » après chaque appui. La vraie touche
clavier « Encoder Page Focus » (Control Alt ,), elle, n'a AUCUN intervalle
mort.

Observations mesurées (log du pont + écran) :
1. Codes de catégorie CONFIRMÉS : 1=Intens, 2=Focus, 3=Color, 4=Image
   (gobos), 5=Form (Iris/Edge/Zoom), 6=Shutter (couteaux/frames), 7=Custom.
   Le preset était FAUX avant (Beam→shutter, Image=4 mal mappé) — corrigé.
2. Boutons Custom (note 22) et Encoder Display (note 23) : au début aucun
   notet émis par le X-Touch (rangée en CC0/Toggle dans l'éditeur). Après
   reconfig de l'éditeur (Note 22/23, Momentary) + chargement du preset
   « Pont EOS OSC.bin » → notes reçues. Custom reste vide tant qu'aucun
   paramètre n'y est épinglé côté Eos (normal). Encoder Display : la bonne
   touche est `gio_encoder_display` (pas `encoder_display`).
3. Appui clavier « Encoder Page Focus » → Eos n'émet RIEN en OSC (confirme
   que la page d'encodeurs n'est pas publiée). Les anneaux du X-Touch ne
   bougent donc pas quand on pagine au clavier (le pont n'est pas informé).
4. Appui bouton X-Touch (envoi `encoder_category_focus`) → la pagination
   INTERNE du pont bascule bien p1/p2 (anneaux CC10-13 suivent), mais l'écran
   Eos affiche « page encoder » en ROUGE. À noter : Focus est dans le groupe
   de catégories « rouge » d'Eos (cf. add-on officiel encoders-for-etc-eos)
   — le rouge est peut-être juste la couleur de catégorie, pas une erreur.
5. Envoi DIRECT (hors X-Touch) de `/eos/key/page_encoders_up` en tap →
   « Page Encodeurs Haut · Erreur : erreur de syntaxe », précédé de « 2 : »
   dans la ligne de commande → il restait un « 2 » en attente : la ligne de
   commande n'était pas vide. Après clear_cmdline, résultat non confirmé
   (utilisateur absent).

Piste soulevée par Cy : le X-Touch bride peut-être le NOMBRE d'appuis émis
(débit MIDI) en cadence rapide. Test à FINIR : presser le bouton 8-10 fois
très vite, compter les noteOn réellement reçus dans le log du pont (marqueur
posé). Si < nombre d'appuis → c'est le X-Touch. Sinon → côté Eos.

Décisions prises côté code (non validées au banc, réversibles) :
- forme d'envoi de la touche de catégorie rendue configurable
  (`categoryKeyForm`, défaut « tap »), car ni tap ni down/up n'ont été
  confirmés comme supprimant la fenêtre morte ;
- l'anti-répétition « ~1 s » soupçonnée le 2026-07-04 est à re-mesurer : le
  test automatique key-repeat-measure.ts (touche chiffre « 1 ») n'a montré
  AUCUN bridage à 100 ms, mais la touche testée n'était PAS une touche de
  catégorie — non concluant pour encoder_category_*.

Outils ajoutés : tools/validation/key-repeat-measure.ts (mesure auto de
l'anti-répétition via l'écho ligne de commande) et
tools/validation/encoder-page-probe.ts (essai de plusieurs touches
candidates de pagination).

---

**Fenêtre morte de pagination — DÉCISION (2026-07-07) : acceptée, enquête close.**
Test décisif « répétition Go » : 13 appuis rapides (~150 ms) sur le bouton Go
(note 54) → 13 noteOn reçus par le pont ET Eos a passé les 13 cues. Donc :
- le X-Touch NE bride PAS son débit de notes (13/13 à 150 ms) ;
- Eos NE coalesce PAS une touche ordinaire (`go_0`) répétée vite ;
- ⇒ la fenêtre morte est SPÉCIFIQUE aux touches `encoder_category_*` (Eos
  coalesce le fait de re-sélectionner une catégorie déjà active).

Piste « touche de pagination dédiée » (`page_encoders_up`, ou `pageKey`) :
ESSAYÉE plusieurs fois au banc → **empire les choses** (rejetée par Cy).
Décision : garder le fonctionnement actuel — re-frappe de `encoder_category_*`
en forme **tap** (`categoryKeyForm: "tap"`, défaut). Satisfaisant quoique non
optimal : il subsiste un petit intervalle mort si on tapote la MÊME catégorie
très vite, sans conséquence fonctionnelle (les encodeurs ciblent l'index de
molette absolu, indépendant de la page affichée). Ne pas rouvrir sans élément
nouveau côté firmware Eos.

---

**Pagination Color divergente sur projecteur à Lime (2026-07-07)** — bug de
correspondance encodeurs/écran. Symptôme : Color affiché en page 1 sur Eos,
mais les anneaux du X-Touch montrent des valeurs d'une autre page.

Fausse piste corrigée : j'avais ajouté une « mémoire de page par catégorie »
(le pont restaurait la dernière page vue) — REVERTÉE (commit 8a96eac). En
réalité Eos remet la catégorie en PAGE 1 à chaque entrée (comportement
standard console) ; le pont fait de même (reset page=0 au changement de
catégorie). L'observation qui a tranché : Eos sur Color p1, anneaux montrant
[moitié,0,0,0] = la p2 du pont (White ~50 %, Hue/Sat/ColorMix 0).

VRAIE cause restante : le pont découpe Color par tranches de 4 dans l'ordre
OSC → p1 = « Red | Lime | Green | Blue ». Eos regroupe probablement les
émetteurs autrement (ex. Red/Green/Blue/White ensemble, Lime à part), donc
dès la p1 le contenu diffère sur un projecteur qui a un émetteur Lime (ou
autre hors RGBW). Sur le K15 (ordre OSC = Red/Green/Blue/White) ça collait.
À FAIRE : obtenir les captures des pages Color d'Eos pour ce projecteur et
affiner la règle de découpage Color (regroupement par famille d'émetteurs ?).

---

**Bouton Resync (réalignement pont ↔ écran Eos) — 2026-07-07.**
Mécanisme de la dérive enfin compris : Eos coalesce les répétitions rapides des
touches `encoder_category_*` (la « fenêtre morte »). En frappe rapide, le pont
avance SA page à chaque appui alors qu'Eos n'avance pas toujours → les deux se
désynchronisent, et comme chacun mémorise la page par catégorie (Eos ET pont,
depuis le fix bf13440), la divergence persiste. Les encodeurs pilotent alors un
paramètre décalé par rapport à l'écran.

Choix (Cy) : accepter la dérive, pas répliquer le découpage exact d'Eos. Ajout
d'un bouton **Resync** (`WheelBankConfig.resyncNote`, méthode
`WheelBank.realignToEos`) : un appui envoie `/eos/key/select_active` (Eos
re-sélectionne les circuits actifs → toutes catégories en page 1) ET remet le
pont en page 1 (mémoire de page vidée) → réalignés. Automatise le contournement
manuel « recharger la sélection » que Cy avait trouvé. Note du bouton PROVISOIRE
(52) à confirmer au banc. À valider aussi : que `select_active` n'élargit pas la
sélection ; sinon replier sur une reconstruction de commande via `/eos/newcmd`.

**MàJ Resync (2026-07-07 après-midi)** : bouton Resync placé sur l'ex-« Custom »
(note 22, catégorie Custom inutilisée → 6 catégories restantes). Touche envoyée
changée de `select_active` à **`select_last`** (rappel de la dernière sélection),
choix de Cy pour l'ergonomie.

---

**Boutons associés aux faders — refonte « suit le fader » (2026-07-07, d'après
la proposition de l'autre agent, adaptée au projet fable 5).**
Décision de Cy : les boutons pilotent la POSITION du fader (banque 1, index =
voie), pas un numéro de sub abstrait → le bouton suit le fader qu'il surplombe.
Empilement vertical calqué sur le panneau détail d'un sub Eos (Load/Assert/Bump).

Implémenté dans `presets.ts` (`faderBump`, `faderLoad`) :
- **Bump** : boutons SOUS le fader, notes **40–47** → `/eos/user/1/fader/1/{i}/fire`.
  CONFIRMÉ au banc pour les voies 1–2 (adresse Luminosus/ETCLabs). Remplace les
  anciens bumps de sub (`/eos/sub/{n}/fire`, notes 24–31, avec LED). ⚠ Le feedback
  LED du bouton de fader n'est pas déterminé → `feedback: null` (perte du témoin
  LED des anciens bumps ; à investiguer : adresse d'écho d'un fader ?).
- **Load** : notes **24–31** (rangée matrice « milieu » présumée) →
  `/eos/user/1/fader/1/{i}/load`. ⚠ NON confirmé (adresse Luminosus non testée ;
  notes à valider au banc).

NON implémenté (bloqué) :
- **Assert** : `/eos/newcmd "Sub n Assert#"` → **erreur de syntaxe** confirmée,
  laissé non assigné (mécanisme à revoir — peut-être `Chan`/`Sub` + Assert par
  touche plutôt que newcmd).
- **Macro** (rangée matrice « haut ») : **CONFLIT** — cette rangée (notes 16–22)
  est déjà occupée par les 6 boutons de catégorie + Resync. Impossible sans
  arbitrage de Cy (déplacer les catégories, ou mettre les macros ailleurs).

À VALIDER AU BANC : forme d'envoi (trigger 1.0/0.0 vs tap) de fire/load ; notes
exactes de la rangée Load ; feedback LED éventuel ; résolution du conflit Macro.

---

**Phase 3 — 1re tranche du configurateur web (2026-07-09/10).**
Spec de Cy : interface web (Web MIDI API navigateur) + petit relais Node vers
OSC, schéma cliquable fidèle au X-Touch Compact, inspecteur par contrôle avec
Learn, cohérent avec le mapping par défaut existant.

Décision d'architecture clé : au lieu de dupliquer la traduction MIDI↔OSC
dans le relais, extraction d'une interface `MidiSource` (dans
`src/main/midi/MidiEngine.ts`) — nécessaire car `Bridge` acceptait la classe
concrète `MidiEngine` dans `deps.midi`, et TypeScript exige une
correspondance NOMINALE dès qu'une classe a des champs privés (une classe de
remplacement, même avec des membres publics identiques, n'aurait pas été
assignable). Avec l'interface, `WebMidiRelayEngine` (nouveau,
`tools/webconfig/`) s'injecte tel quel dans `new Bridge(config, { midi })` —
`MappingEngine`/`WheelBank`/`EosOscClient` tournent SANS modification.

Bug trouvé et corrigé pendant le développement (vérification au navigateur,
pas juste `tsc`/tests) : `bridge.on("error", ...)` n'était pas câblé dans
`server.ts` → un EventEmitter Node sans écouteur "error" fait planter tout
le process à la première erreur (ici : Eos injoignable en dev). Même piège
que documenté dans `run-bridge.ts`, oublié une première fois côté webconfig.

Bug fonctionnel trouvé en testant dans le navigateur (pas visible en lisant
le code) : le schéma marquait comme "assignables" les boutons de catégorie
et Resync de la banque de molettes (notes 16-22) — alors que `Bridge` route
`wheelBank.handleMidi()` AVANT `MappingEngine.handleMidi()` (avec `return`
si consommé) : un mapping créé dessus via le configurateur ne se
déclencherait JAMAIS. Corrigé en calculant la réservation DYNAMIQUEMENT
depuis le `wheelBank` de la config chargée (pas une liste figée dans
`xtouchLayout.ts`) — reste correct si la config WheelBank change.

Vérifié en conditions quasi réelles (serveur lancé, page chargée dans le
navigateur du bac à sable, config réelle à 28 mappings chargée) : rendu du
schéma (82 contrôles), sélection d'un fader assigné → bon mapping affiché,
sélection d'un encodeur réservé → panneau lecture seule correct, sélection
d'un bouton de catégorie → réservation dynamique correcte, création d'un
mapping sur un encodeur libre (5-16) → sauvegardé dans `config/pont.json`
puis SUPPRIMÉ proprement (le test n'a pas laissé de résidu). La capture
d'écran et le clic simulé par l'outil de test échouaient de façon répétée
sans erreur console — cohérent avec une invite de permission Web MIDI native
bloquée par le navigateur automatisé du bac à sable (hors de la page, donc
hors de portée) ; contourné en pilotant le DOM directement
(`dispatchEvent`/appels de fonction), qui a confirmé le bon fonctionnement.
**Pas testé avec un vrai X-Touch/navigateur humain — à valider au banc.**

Hors périmètre assumé (cf. plan) : retour Web MIDI OUTPUT vers le X-Touch
physique (LED/moteur — le relais pousse déjà les octets au navigateur,
`kind:"midiOut"`, mais le JS ne les émet pas encore en sortie) ; édition
individuelle des encodeurs 1-4 ; sémantique fine toggle vs latch (traités
identiquement) ; fidélité pixel exacte à la photo de référence (disposition
structurelle reproduite, pas mesurée).

⚠ Note découverte en marge : `npm test` chaîne les suites avec `&&` — le test
`page_encoders_up` déjà cassé (cf. entrée précédente) empêche `bridge-test`
et le nouveau `webmidi-relay-selftest` de s'exécuter sous `npm test` (ils
passent bien isolément, vérifié). Pas corrigé ici (hors périmètre demandé),
mais à garder en tête : un futur échec dans ces deux suites resterait
invisible tant que le premier bug n'est pas réglé.

---

**Reflet dynamique des valeurs X-Touch + incident de session (2026-07-10).**
Demande de Cy : le schéma web doit refléter en direct l'état physique du
X-Touch. Implémenté côté `public/index.html` (`reflectLive`) : faders =
position du curseur (CC "in" ou "out"), boutons/clics = `.pressed` (appui
physique, momentané) et `.lit` (LED renvoyée par le pont, persistant),
encodeurs = anneau rempli **uniquement** depuis le feedback CC "out"
(valeur absolue) — la rotation "in" est un DELTA relatif (encodage
relative1/2/3), l'utiliser comme position aurait été un bug (anneau
erratique). La rotation "in" déclenche juste un flash `.turning`.

**Incident** : en testant, j'ai ouvert mon propre onglet de navigateur
(outil de test automatisé) contre le serveur `npm run webconfig` que Cy
avait déjà lancé et utilisait avec son vrai X-Touch — le serveur ne suit
qu'UNE connexion WebSocket active (`activeSocket`) et l'a silencieusement
remplacée par la mienne, coupant le retour live de Cy sans aucun message.
Cy l'a signalé (« la fenêtre n'est pas connectée en MIDI »).

**Corrigé** : `server.ts` rejette maintenant explicitement toute 2e
connexion tant que la 1re est active (message `{kind:"busy"}` + fermeture
WS code 4001), au lieu de la voler silencieusement. Testé par
`tools/webconfig/session-lock-selftest.ts` — lance une instance JETABLE du
serveur (port 8799, config JSON temporaire, JAMAIS `config/pont.json` ni le
port 8787 par défaut) et vérifie : 1re connexion acceptée, 2e rejetée
proprement, 1re toujours active après le rejet, une 3e connexion acceptée
après fermeture de la 1re.

**Leçon retenue** : ne plus jamais ouvrir un navigateur de test contre le
serveur webconfig en direct (port 8787) — utiliser un port/une config
jetables pour toute vérification automatisée. Le process déjà lancé par Cy
ne reçoit le correctif qu'à son PROCHAIN redémarrage (tsx ne recharge pas
un module déjà chargé) — à relancer quand Cy est prêt (coupure de connexion
WS le temps de recharger la page, pas plus).

---

**Assert des faders — RÉSOLU au banc (2026-07-16, nomad 3.3.5.69).**
Fonction Assert assignée aux boutons rangée 3 (notes **32-39** → faders 1-8).

Pistes ÉLIMINÉES, preuves à l'appui :
- `/eos/newcmd "Sub n Assert#"` : erreur de syntaxe (constat 2026-07-07 —
  « Assert » est une touche console, pas un mot-clé de ligne de commande).
- `/eos/key/subassert` (avec ou sans préfixe user) : aucun effet visible.
- `/eos/user/1/fader/1/<n>/assert` : rejeté par Eos — diagnostics Tab 99 :
  `RECV error, OSCFaderBankMethod invalid fader index [assert]` → la
  méthode `assert` n'existe PAS sur les fader banks OSC de cette version
  (ni dans Luminosus, vérifié dans EosFaderBankBlock.cpp : seulement
  level/load/unload/stop/fire/config).

**La bonne adresse, trouvée par Cy : `/eos/user/1/fader/1/<n>/stop`**
(trigger 1.0/0.0) — sur cette config, le bouton stop d'un fader OSC
réalise la fonction Assert attendue. Mappings `faderassert<i>_bank1_<i>`
écrits dans config/pont.json.

---

**Pagination des faders (2026-07-16) — implémentée, à valider au banc.**
Décisions Cy : ◄◄ (note 49) = page précédente, ►► (50) = suivante, 4 pages
cycliques ; le MAIN (emplacement 9 de la banque) SUIT la page (pas de 2e
banque dédiée) ; indicateur binaire sur les LED ⟲ (51) et ● (52) : page 1 =
tout éteint, 2 = ⟲, 3 = ●, 4 = les deux.

Mécanisme : `FaderPager` (nouveau, `src/main/bridge/FaderPager.ts`, logique
pure comme WheelBank) envoie `/eos/fader/1/config/<page>/10` — changer la
page de la banque OSC déplace ses 10 emplacements SANS réécrire les
mappings : `/eos/fader/1/<n>` pointe vers la nouvelle page, et faders,
bumps, loads, asserts suivent automatiquement. Eos répond
`/eos/out/fader/1` (label de banque) puis rediffuse niveaux + noms → les
moteurs se resynchronisent par le feedback existant de MappingEngine.

Symbiose : le pont ADOPTE la page publiée dans le label de banque (dernier
entier, borné à pageCount, sans renvoyer de config — pas de boucle). Sur le
fake-eos (phase 0) le label est la page nue ("2") ; **forme du label du
VRAI nomad à confirmer au banc** — si elle contient un autre entier final,
ajuster le parsing dans `FaderPager.handleOsc`.

`Bridge.initFaderBanks()` délègue la banque paginée au pageur : une
reconnexion ou un show rechargé ré-établit la page COURANTE (pas de retour
forcé en page 1). Config dans `config/pont.json` (`faderPager`) + preset
d'usine. Configurateur : pilule « Faders page N/4 » (message WS `faderPage`)
et ◄◄/►►/⟲/● marqués réservés (même mécanisme dynamique que la banque de
molettes). Selftest `tools/phase1/faderpager-selftest.ts` (32 vérifications,
dans `npm test`).

Vérifié de bout en bout sur banc isolé (fake-eos port 33099 + serveur
webconfig jetable port 8788, JAMAIS le vrai nomad ni le port 8787) : appui
►► injecté par le relais MIDI → `config/2/10` → label "2" adopté sans
double config → pilule « page 2/4 » ; ◄◄ → retour page 1. Le retour LED
physique (⟲/●) n'était pas observable sans X-Touch (pas de `hello` Web
MIDI) — couvert par le selftest, **à voir au banc**.

En marge : réparé le test `page_encoders_up` du selftest WheelBank, cassé
depuis l'introduction du chord « catégorie & 1 » (le switch émet la touche
de catégorie DEUX fois, down/up — l'assertion attendait encore 1). C'était
le test qui bloquait toute la chaîne `npm test` (cf. note du 2026-07-10) :
la suite complète passe à nouveau, `bridge-test` et les suites webconfig
s'exécutent de nouveau sous `npm test`.

---

**Pagination des faders — 1er retour de banc réel (2026-07-17, à
poursuivre).** Cy signale deux points après un premier essai réel :

1. **Indicateur de page déplacé sur ◄◄/►► eux-mêmes (notes 49/50)**, au lieu
   des notes dédiées ⟲/● (51/52). Simple changement de config
   (`indicatorNotes: [49, 50]` au lieu de `[51, 52]`) — le mécanisme binaire
   ne change pas, `FaderPager` fonctionne déjà avec `indicatorNotes`
   quelconques (y compris identiques à `prevNote`/`nextNote`, cf. doc
   `config.ts` mise à jour). Vérifié par le selftest existant (inchangé,
   teste le mécanisme générique) + `npm test` complet repassé au vert.

2. **Aucun changement visible côté Eos** après appui ◄◄/►► (l'écran nomad
   reste sur Sub 1-10, page 1) — capture d'écran à l'appui montrant la
   rangée F1-F10 (Direct Selects / OSC fader bank, bas de l'écran Live),
   toujours page 1. Cause la PLUS PROBABLE : le process déjà lancé par Cy
   au moment du test n'avait pas encore rechargé le code/la config de cette
   session (`tsx`/Electron ne recharge pas un module déjà en mémoire — même
   piège que documenté le 2026-07-16 pour le verrou de session) : sans
   redémarrage complet de `lancer-pont.bat` (fermer la fenêtre ET vérifier
   qu'aucun process node/electron résiduel ne tourne), `FaderPager` n'existe
   simplement pas dans le process en cours, et les notes 49/50 ne
   déclenchent alors RIEN (aucun mapping n'était assigné dessus avant cette
   fonctionnalité) — symptôme identique à ce qui a été observé.
   Aucune preuve de bug dans le mécanisme lui-même : le selftest et la
   vérification bout en bout sur fake-eos (entrée précédente) confirment que
   `config/<page>/10` part bien et que l'adoption fonctionne.
   **Ajout pour le prochain essai** : `server.ts` logge maintenant en
   console `[webconfig] pagination faders : page N/4` à CHAQUE changement de
   page (interne, avant même l'envoi OSC) — visible dans la fenêtre de
   commande ouverte par `lancer-pont.bat`. Si ce log n'apparaît PAS à
   l'appui d'◄◄/►►, c'est que l'événement MIDI n'atteint pas `FaderPager`
   (process pas à jour, ou note/canal physique différent de 49/50 canal 1 —
   à vérifier avec l'outil MIDI de diagnostic si le log reste muet après un
   redémarrage complet). Si le log apparaît mais qu'Eos ne bouge pas à
   l'écran : vérifier les diagnostics Tab 99 d'Eos pour une erreur sur
   `/eos/fader/1/config/<page>/10` (même méthode que pour Assert).
   **NON RÉSOLU — à reprendre au prochain banc.**

3. **Correction : pagination BORNÉE, PAS cyclique.** Cy a précisé qu'il ne
   doit y avoir AUCUNE boucle possible et AUCUN lien direct entre la page 1
   et la dernière page (4) — la version initiale (`changePage` avec modulo)
   faisait boucler ◄◄ depuis la page 1 vers la page 4, et ►► depuis la
   page 4 vers la page 1. Corrigé : `FaderPager.changePage` borne
   maintenant sur `[1, pageCount]` (`Math.min`/`Math.max`, plus de modulo) ;
   ◄◄ sur la page 1 et ►► sur la dernière page ne font RIEN — le bouton
   reste consommé, mais sans config OSC renvoyée ni évènement `changed`.
   Tests du selftest réécrits en conséquence (butées testées
   explicitement, plus d'assertions de « retour cyclique »).

---

**Encodeurs 9-16 : syntaxe wheel-par-nom CONFIRMÉE au banc (Cy, 2026-07-17).**
Cy a capturé le trafic OSC réel envoyé depuis un outil de test directement
contre Eos, révélant la VRAIE syntaxe des molettes à paramètre nommé —
jusque-là un simple pari non testé côté pont (`/eos/wheel/<param>`, jamais
validé). La syntaxe réelle, confirmée par capture :

- `/eos/user/1/wheel/coarse/<param>` — rotation normale
- `/eos/user/1/wheel/fine/<param>` — rotation, encodeur poussé (précision)

Casse EXACTE vue dans la capture : `zoom`, `intens`, `red` (minuscules,
params à un mot) ; `Shutter Strobe`, `X Focus` (Title Case, params à
plusieurs mots). Cy a aussi demandé une variante **Home** pour le bouton de
l'encodeur (remise à zéro du paramètre) — **AUCUNE capture pour celle-ci** :
`/eos/user/1/wheel/home/<param>` est une EXTRAPOLATION par analogie avec
coarse/fine, **JAMAIS confirmée au banc**. À tester en priorité au prochain
essai (Tab 99 si erreur, comme pour Assert).

**Implémenté :**
- `config.ts` : `OscAction.fineAddress`/`homeAddress` (adresses jumelles
  d'un mapping `wheel`) + `Mapping.wheelPush` (note de poussée + action
  "fine"/"home").
- `MappingEngine.ts` : nouveau bloc de traitement de la poussée (avant le
  touch-sense fader, structure similaire) — "fine" bascule un `Set` de
  wheels poussées (ticks accumulés puis routés vers `fineAddress` SANS
  `scale` au flush, au lieu de `address` coarse avec `scale`) ; "home"
  déclenche une frappe SANS argument vers `homeAddress` à l'appui
  (relâchement ignoré). Généralise le mécanisme fine déjà éprouvé dans
  WheelBank (encoderPushNotes), mais pour un encodeur à paramètre FIXE
  (pas de banque dynamique par catégorie/page).
- Configurateur (`index.html`, panneau « Personnaliser » encodeurs 9-16) :
  remplace le champ texte libre par un menu déroulant (Intens, Pan, Tilt,
  Zoom, Iris, Edge, X/Y/Z Focus, Red, Green, Blue, White, Hue, Saturation,
  Color Mix, Shutter Strobe — les 5 marquées "✓ banc" sont celles de la
  capture de Cy, le reste extrapole les libellés déjà vus côté WheelBank
  mais jamais testés sur CETTE adresse précise) + option « Personnalisé… »
  (texte libre, comme avant) + sélecteur de poussée (Aucune/Fine/Home).
  Bug trouvé et corrigé PENDANT la vérification navigateur (pas visible en
  lisant le code) : un paramètre personnalisé non reconnu (ex. "gobo
  speed") utilisait quand même le préfixe `coarse/` dans l'adresse
  enregistrée, donc `encParamState()` le détectait comme "connu" au lieu de
  "personnalisé" à la réouverture du panneau → le champ texte restait vide
  au lieu de réafficher la valeur sauvegardée. Corrigé en distinguant
  clairement « le paramètre est dans la liste déroulante » de « l'adresse
  utilise le préfixe coarse/ » (deux choses différentes).
- Selftest `engine-selftest.ts` : 2 nouveaux mappings (poussée fine / poussée
  home) + 6 vérifications (coarse↔fine selon l'état poussé, ticks bruts vs
  scale, frappe home sans argument, relâchement home sans effet, rotation
  normale après un home). `npm test` complet repassé au vert.

Vérifié au navigateur (bac à sable, fake-eos + config jetable, JAMAIS le
port 8787 ni `config/pont.json`) : sélection Zoom + poussée Fine sur
Enc 9 → sauvegardé avec `fineAddress` et `wheelPush.action: "fine"` corrects ;
saisie personnalisée "gobo speed" sur Enc 10 → sauvegardée puis
correctement réaffichée à la réouverture (après le correctif du bug
ci-dessus) ; changement vers Pan + poussée Home → `homeAddress` et
`wheelPush.action: "home"` corrects ; champ vidé → mapping supprimé.
**Non testé avec un vrai X-Touch/Eos — à valider au banc, en particulier
Home.**

---

**Encodeurs 9-16 : simplification demandée par Cy (2026-07-17) — panneau
« Personnaliser » supprimé.** Cy a jugé la fenêtre dédiée superflue : le
menu déroulant doit vivre directement dans l'inspecteur STANDARD (celui de
tous les autres contrôles), ses valeurs doivent être des adresses OSC
COMPLÈTES et fonctionnelles (pas de préfixe reconstitué en coulisses), et
la poussée de l'encodeur fait TOUJOURS Fine par défaut — plus de choix
Aucune/Fine/Home dans l'UI.

**Fait :**
- Supprimé : la fenêtre modale (`openEncoderPanel`), le bouton « Personnaliser
  → », `ENC_RIGHT_IDS`/`ENC_PARAM_PRESETS`/`encParamState` et tout le CSS
  dédié (`.modal-*`, `.enc-row`, `.enc-custom-row`).
- L'inspecteur générique (`renderInspector`) affiche maintenant, pour un
  encodeur NON réservé (5-16), un `<select>` d'adresses COMPLÈTES
  (`/eos/user/1/wheel/coarse/<param>`) à la place du champ texte libre —
  même liste de paramètres qu'avant (les 5 marqués « ✓ banc » viennent de
  la capture de Cy), + option « Personnalisé… » pour taper une adresse
  complète arbitraire. C'est la MÊME logique pour n'importe quel encodeur
  libre (5-8 en profitent aussi désormais, pas seulement 9-16).
- La poussée de l'encodeur (fine) est appliquée AUTOMATIQUEMENT à
  l'enregistrement (`applyEncoderPushDefaults`) : `fineAddress` dérivée de
  l'adresse choisie (remplace `/coarse/` par `/fine/`), `wheelPush` branché
  sur la note de poussée correspondante (ex. enc9 → encClick9) avec
  `action: "fine"` — sans aucun réglage à faire. Le support de "home" reste
  dans le moteur (config.ts/MappingEngine.ts, testé) mais n'est plus exposé
  dans cette UI simplifiée.
- Bug trouvé en corrigeant l'ancien panneau réapparaît ici sous une forme
  différente et a été anticipé : `defaultMapping()` pour un encodeur NEUF
  ne forçait plus `mode: "relative1"` (c'était fait par l'ancien panneau,
  disparu) — un nouvel encodeur aurait été mal interprété (absolu au lieu
  de relatif, encodage d'usine du X-Touch). Corrigé : `defaultMapping`
  force `relative1` pour tout NOUVEL encodeur, comme avant.
- Champ adresse vidé → suppression du mapping (si existant), cohérent avec
  l'ancien comportement du panneau.

Vérifié au navigateur (bac à sable, fake-eos + config jetable) : adresse
préréglée (Pan) affichée correctement pour un mapping existant ; passage
en « Personnalisé… » avec une adresse tapée à la main → sauvegardée avec
`fineAddress` dérivée et `wheelPush.action: "fine"` (l'ancien `home`
disparaît bien) ; nouvel encodeur vierge → `mode: "relative1"` bien
présent après sauvegarde ; champ vidé sur Save → aucun mapping créé ;
suppression via le bouton dédié → mapping retiré ; encodeurs réservés
(1-4) toujours affichés en lecture seule, inchangés. `npm test` complet
repassé au vert (aucune régression). **Non testé avec un vrai X-Touch —
à valider au banc.**

---

**Boîte « Paramètres actifs » (2026-07-17) — nouvelle demande de Cy, en
parallèle du protocole de test.** Liste dans le configurateur web TOUS les
paramètres (canaux DMX) de la sélection Eos courante, en direct — pas
seulement la tranche affichée par la page/catégorie active des encodeurs
1-4. Réutilise la MÊME donnée que `WheelBank` (déjà abonnée à
`/eos/out/active/wheel/<n>` pour piloter les encodeurs 1-4), sans dupliquer
le parsing OSC.

**Fait :**
- `WheelBank.ts` : nouvel accesseur `allWheels` (tous les paramètres
  connus, triés par index — pas juste `state.labels`, qui ne couvre que la
  tranche affichée). Deux nouveaux événements ADDITIFS (l'existant
  `changed` n'est PAS touché, aucune régression possible sur la pagination/
  LED déjà testées) :
  - `wheelUpdated` : émis à CHAQUE réception de `/eos/out/active/wheel/<n>`,
    structurel OU simple tick de valeur (contrairement à `changed`, qui ne
    bouge QUE sur un changement de label/catégorie, pour ne pas spammer la
    pagination). Nécessaire pour que la boîte affiche les valeurs EN DIRECT
    pendant qu'on manipule un paramètre sur Eos.
  - `wheelsReset` : émis quand la sélection change (circuits différents) —
    la boîte se vide.
- `server.ts` : relaie ces événements en WS (`activeParams` = snapshot
  complet à la connexion et sur `changed` ; `activeParamUpdate` = une
  seule valeur ; `activeParamsReset` = vidage). Catégories affichées en
  clair via les codes déjà confirmés au banc (1=Intens…7=Custom).
- `index.html` : nouvelle boîte fixe en haut de la colonne inspecteur
  (TOUJOURS visible, indépendante du contrôle sélectionné dans le schéma).
  Mise à jour ciblée d'une seule ligne sur `activeParamUpdate` (pas de
  re-rendu de toute la liste à 30 msg/s pendant qu'on tourne une molette
  réelle — même précaution de perf que `reflectLive`).
- Selftest `wheelbank-selftest.ts` : 7 nouvelles vérifications (`allWheels`
  toutes catégories confondues, `wheelUpdated` sur structurel ET simple
  tick de valeur, `wheelsReset` au changement de sélection).

Vérifié au navigateur (bac à sable, injection directe des fonctions
`setActiveParams`/`upsertActiveParam`, sans remonter tout le pipeline OSC
— fake-eos ne simule pas de sélection de fixture) : rendu initial vide,
liste peuplée avec catégories traduites et triée par index, mise à jour
ciblée d'une ligne SANS re-rendu complet, nouvel index → re-rendu complet,
reset → liste vidée. `npm test` complet au vert. **Non testé avec un vrai
Eos + sélection réelle de projecteur — à valider au banc.**

Note d'architecture : `WheelBank.handleOsc()` traite `/eos/out/active/
wheel/<n>` INCONDITIONNELLEMENT (remplit `this.wheels` quelle que soit
`this.category`) — Eos publie ces messages dès qu'un projecteur/circuit est
sélectionné sur la console (par n'importe quel moyen : GUI, clavier
physique, OSC `/eos/chan`…), SANS dépendre d'un appui sur les boutons de
catégorie du X-Touch. La boîte devrait donc se peupler dès qu'une sélection
existe sur Eos, même sans toucher aux encodeurs 1-4 — à confirmer au banc.

---

**Clics d'encodeur (5-16) oubliés dans la simplification UI — corrigé
(2026-07-17).** Cy a signalé que « CLIC 9 » s'affichait encore comme un
bouton libre générique (Adresse OSC texte + Comportement momentary/toggle/
latch) après la refonte de l'inspecteur des encodeurs — la logique
Fine/Home posée automatiquement à la sauvegarde de l'ENCODEUR n'avait
aucune vitrine côté CLIC. Demande : Fine par défaut, Home en second choix.

**Corrigé** : `renderInspector` route désormais tout `encoderClick` NON
réservé (5-16 ; 1-4 restent gérés par la réservation WheelBank existante,
inchangée) vers `renderEncoderPushInspector(c)`, qui **ne retombe JAMAIS**
sur l'éditeur générique de bouton :
- Si l'encodeur associé (ex. CLIC 9 → ENC 9) a un mapping `wheel` : affiche
  son adresse en aperçu + un menu Fine (défaut)/Home, qui MODIFIE le
  mapping de l'ENCODEUR (`wheelPush.action`, et `osc.homeAddress` dérivée
  à la volée si Home est choisi) — pas un mapping séparé pour le clic.
- Sinon (encodeur pas encore configuré) : message informatif « assigne
  d'abord un paramètre sur ENC N », pas d'édition libre possible.

Nouveau helper partagé `deriveWheelAddress(adresseCoarse, variante)`
(remplace `/coarse/` par `/fine/` ou `/home/`) — réutilisé par
`applyEncoderPushDefaults` (encodeur) ET `renderEncoderPushInspector`
(clic), pour ne pas dupliquer la logique de dérivation d'adresse.

Vérifié au navigateur (bac à sable) : CLIC d'un encodeur configuré → menu
Fine/Home affiché, bascule vers Home → `wheelPush.action`/`homeAddress`
corrects sur le mapping de l'ENCODEUR, réouverture → Home bien
pré-sélectionné ; CLIC d'un encodeur NON configuré → message informatif,
pas d'édition ; CLIC 1-4 (réservés) → toujours en lecture seule, inchangés.
`npm test` complet au vert. **Non testé avec un vrai X-Touch — Home reste
à valider au banc (syntaxe jamais confirmée, cf. entrée du 2026-07-17
sur les encodeurs).**

---

**Home — syntaxe CONFIRMÉE par Cy (2026-07-17) : `/eos/param/<param>/home`**
(ex. `/eos/param/pan/home`). Corrige l'extrapolation précédente
(`/eos/user/1/wheel/home/<param>`, jamais testée) — Home vit dans une
famille d'adresse DIFFÉRENTE de coarse/fine (`/eos/user/1/wheel/…`), à ne
pas confondre.

Corrigé : `deriveWheelAddress()` (index.html) construit maintenant
`/eos/param/<param>/home` pour la variante "home" (coarse/fine inchangés,
toujours dérivés par simple substitution dans `/eos/user/1/wheel/coarse/…`).
Doc `config.ts` (`OscAction.homeAddress`) mise à jour. Avertissement
« ⚠ non confirmé au banc » retiré du menu Fine/Home et de la note de
l'inspecteur du clic d'encodeur (`index.html`) — Home est maintenant
présenté comme confirmé, au même titre que Fine.

Vérifié au navigateur (bac à sable) : bascule Home sur un encodeur
configuré → `osc.homeAddress` = `/eos/param/gobo speed/home` (dérivée de
l'adresse coarse `.../coarse/gobo speed`), plus d'avertissement affiché.
`npm test` complet au vert (aucune régression — homeAddress reste un champ
opaque pour MappingEngine, seule sa valeur générée change).

---

**Session autonome (2026-07-17, machine à distance, aucun accès physique) —
bug enc14/sub999 corrigé, deux nouvelles fonctionnalités UI, tentative de
build portable.** Session menée sans validation humaine en temps réel ;
détail complet dans le compte-rendu livré à Cy (journal d'accès, correction
d'une fausse affirmation UDP 8000/8001 — le projet est bien en TCP:3032,
confirmé partout ailleurs dans ce même journal).

**Bug corrigé : enc14 → /eos/sub/999 en tout-ou-rien.** Cause : le mapping
était `osc.type: "wheel"` (ticks relatifs bruts), envoyés tels quels vers
une adresse qui attend un niveau ABSOLU 0.0-1.0 (comme toute adresse
`/eos/sub/<n>`/`/eos/fader/<bank>/<n>` du projet) — un encodeur physique
étant SANS FIN (pas de position), quelques ticks (± quelques unités)
partaient directement en argument, d'où le comportement binaire constaté.

Corrigé par un nouveau mécanisme générique `osc.accumulate` (config.ts +
MappingEngine.ts) : les ticks sont accumulés dans une valeur ABSOLUE
interne, clampée sur `range` (0-1), envoyée à chaque flush — au lieu des
ticks bruts. **Sécurité ajoutée (jamais demandée explicitement, mais jugée
indispensable sans validation humaine possible)** : la valeur interne
reste INDÉFINIE tant qu'aucun feedback Eos n'est reçu sur l'adresse — le
pont ignore les ticks plutôt que de supposer un niveau à 0/mi-course, ce
qui aurait pu écraser un niveau réel en cours de spectacle si le fix avait
été relancé pendant un show. ⚠ HYPOTHÈSE À VÉRIFIER (jamais confirmée
spécifiquement pour les subs dans ce projet) : que `/eos/sub/<n>` republie
bien son niveau sur cette MÊME adresse quand il change (comme les faders),
permettant cette synchronisation. Si ce n'est pas le cas, l'encodeur restera
silencieux indéfiniment (aucun tick envoyé) — symptôme à surveiller au
prochain banc, cf. checklist.

`config/pont.json` : enc14 mis à jour (`accumulate: true`, `accumulateStep:
0.01`, `range: [0,1]`). Tests : 8 nouvelles vérifications dans
`engine-selftest.ts` (gradation intermédiaire, clamp haut/bas, mode fine
÷10, re-synchronisation, isolation entre adresses).

**Nouveau : option "Contrôler un Sub" dans le menu déroulant d'adresse de
l'encodeur** (index.html) — numéro de sub validé (entier positif, jamais
0/négatif), génère automatiquement un mapping `accumulate`. Le clic de
l'encodeur associé n'offre alors QUE "Fine" (pas de "Home" : ça n'a pas de
sens pour un niveau absolu comme un sub).

**Nouveau : boutons libres (dont notes 51/52 ⟲/●, actuellement libres —
l'indicateur de pagination faders a été déplacé sur 49/50 le 2026-07-17)
— menu déroulant Macro / Commande directe / Personnalisé** à la place du
simple champ texte. Macro → `/eos/macro/<n>/fire` (adresse documentée dans
HANDOFF_Claude-Code_Pont-MIDI-OSC.md depuis la recherche initiale du
projet, PAS une invention de cette session). Commande directe → liste
FERMÉE de 15 commandes puisées dans `src/shared/eosKeys.ts` (1155 touches
officielles ETC, "Eos OSC Keys.pdf") : Go, Stop/Back, Blackout, Record,
Update, Clear, Enter, Escape, Full, Home, Out, Live, Blind, Next, Last —
chacune vérifiée présente dans ce fichier avant d'être ajoutée, aucune
inventée. Rétrocompatible : les mappings existants (`btn_go` → `go_0`,
`btn_encoder_display` → adresse hors liste) se rechargent correctement en
mode "Commande directe" / "Personnalisé" respectivement, sans y toucher.

**Build portable Windows** : `electron-builder` ajouté, packageant
`tools/webconfig/desktop` (l'app RÉELLEMENT utilisée par Cy au quotidien —
PAS `src/main/index.ts`, un shell Electron plus ancien/minimal, jamais
mentionné dans ce projet depuis le début de cette session, probablement
superseded). `asar: false` (les fichiers restent lisibles tels quels —
`bootstrap.js` spawn `tsx` pour exécuter `server.ts`, un mécanisme qui
n'a jamais été validé à l'intérieur d'une archive asar) ; `npmRebuild:
false` — la recompilation native de `@julusian/midi` contre l'ABI
d'Electron a échoué faute de Visual Studio Build Tools sur cette machine
(installer cette chaîne d'outils aurait été un changement système lourd,
hors périmètre sans accord explicite) ; désactivée sur la base d'un fait
déjà établi par l'usage réel du projet : le binaire natif EXISTANT
fonctionne déjà quand `webconfig-app` tourne via `ELECTRON_RUN_AS_NODE`
(c'est exactement le mécanisme réutilisé pour le packaging). ⚠ HYPOTHÈSE
À VÉRIFIER sur le second poste : `@julusian/midi` pourrait échouer à se
charger si ce poste manque le Visual C++ Redistributable x64 (dépendance
native courante) — cf. checklist.

Script `tools/webconfig/verify-connection.ts` ajouté (liste les ports
MIDI + test TCP/OSC ping-pong vers Eos, avec un timeout et un résumé
clair) — testé avec succès contre `fake-eos` (succès ET échec simulé,
les deux chemins de code vérifiés).

**Smoke test du build RÉUSSI sur cette machine** (`Pont X-Touch EOS
0.1.0.exe`, portable, 97,6 Mo, + `Pont X-Touch EOS Setup 0.1.0.exe`, NSIS,
97,9 Mo — les deux générés dans `release/`) : lancé, processus stables,
requête HTTP sur `127.0.0.1:8787` → 200 OK, preuve que le sous-processus
Node embarqué (bootstrap.js → tsx → server.ts) démarre correctement ET que
`@julusian/midi` (natif, chargé transitivement par `WebMidiRelayEngine` →
`MidiEngine`) se charge sans erreur d'ABI dans ce contexte packagé —
répond donc PARTIELLEMENT à l'hypothèse ci-dessus (prouvé sur CETTE
machine ; l'absence du Visual C++ Redistributable sur le SECOND poste
reste, elle, non vérifiable à distance). **Ceci reste un smoke test sur
la machine de développement, PAS un test sur le second PC Windows 11
réel — à confirmer là-bas (cf. checklist).**

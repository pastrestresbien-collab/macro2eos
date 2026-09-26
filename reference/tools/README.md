# Outils de test — banc transport OSC/TCP

- `fakeeos.ts` — simulateur ETCnomad minimal (projet xtouch2Eos, fourni tel quel,
  puis corrigé/enrichi le 2026-09-26, voir « Fidélité » ci-dessous). Reproduit le
  comportement réseau observé sur un vrai nomad : burst d'état initial à la
  connexion, `/eos/ping` → `/eos/out/ping`, config de banque de faders, écho
  fader différé (500 ms par défaut, configurable), écho de touche, écho de ligne
  de commande sur `/eos/out/cmd` **et** `/eos/out/user/<u>/cmd` avec le flag
  d'erreur (`texte, flag_erreur_int`), réception journalisée (sans écho inventé)
  de `/eos/macro/<n>/fire` et de `/eos/sub/<n>`.
- `test-client.ts` — client de test minimal utilisé pour valider le pipeline
  (session de consolidation, 2026-07-31) : connexion TCP, envoi d'une commande
  OSC framée (1.0, longueur 4 octets), lecture de la réponse.
- `test-client2.ts` — teste `/eos/macro/<n>/fire` (déclenchement de macro OSC,
  1.0=appui/0.0=relâchement) et `/eos/key/go_0`.
- `test-client3.ts` — teste une macro à deux lignes chaînées (sélection
  `Group + Chan Thru`, application de gel, `Record ... Label <texte>` avec
  espaces et tiret dans le libellé).

## Ce que ça valide

Le **transport** OSC/TCP (framing, encodage, connexion, écho) — pas la **grammaire**
Eos. `fakeeos.ts` accepte n'importe quelle chaîne de commande sans jamais la
valider syntaxiquement : `flag_erreur_int` (voir « Fidélité ») vaut toujours 0,
sauf si on force artificiellement un refus avec `--erreur-pattern` (commodité de
test, pas une vraie validation — voir plus bas).

**Toute macro validée uniquement contre ce simulateur reste non confirmée
syntaxiquement** — seul un vrai nomad/console peut trancher ce point.

## Fidélité au vrai Eos (mise à jour 2026-09-26)

Le simulateur ne reproduit que ce qui est **confirmé** (niveau S banc réel ou A
manuel officiel) — jamais de syntaxe devinée, conformément à la règle du dépôt
(`CLAUDE.md`, `grammar/README.md`).

**Corrigé / ajouté** :

- `/eos/macro/<n>/fire` et `/eos/macro/fire` : reçus et journalisés (avant :
  ignorés en silence, même dans le log serveur). Toujours sans écho — aucune
  adresse de retour n'est documentée ou observée pour ce déclenchement.
- `/eos/sub/<n>` : reçu et journalisé, écho inventé supprimé (un vrai Eos ne
  republie jamais spontanément sur cette adresse, corpus #139).
- `/eos/out/cmd` porte maintenant ses **deux** arguments confirmés
  `(texte, flag_erreur_int)` au lieu d'un seul — format du corpus #140. Diffusé
  aussi sur `/eos/out/user/<u>/cmd`, comme observé au banc actif.
- Écho fader par défaut passé de 3 s (chiffre communautaire jamais confirmé) à
  **500 ms**, mesuré empiriquement à +522 ms au banc actif (corpus #139).
- Burst initial étendu de 2 à 8 messages à la connexion : `show/name`, `user`,
  `active/cue`, `active/cue/text`, `active/chan`, `wheel`, `switch`,
  `event/state` — toutes des adresses ET formats d'argument confirmés par le
  manuel officiel (chap. 31, Show Control).
- `--erreur-pattern <regex>` : **commodité de test, pas un comportement Eos**.
  Force `flag_erreur_int=1` sur les commandes dont le texte matche la regex,
  pour exercer le chemin « refus » côté app (`APP.md`) sans vrai validateur de
  syntaxe. Aucun refus par défaut.
- `/eos/out/pending/cue/text` ajouté au burst initial (confirmé manuel chap.31,
  et vu dans le layout `reference/touchosc/` — voir plus bas).
- Fader `load`/`unload`/`stop`/`fire`/`out` (`/eos/fader/<b>/<f>/<action>`) :
  reçus et journalisés, sans écho — le manuel (table Fader) confirme ces cinq
  actions sans argument, et ne documente aucun accusé de réception distinct du
  niveau/nom déjà simulés.
- Direct Select — pagination (`/eos/ds/<n>/page/<delta>`) et appui bouton
  (`/eos/ds/<n>/<bouton>`) : reçus et journalisés, sans écho (aucun accusé
  documenté pour l'appui lui-même dans le manuel).

**Analysé mais volontairement pas simulé** : la **création** de banque Direct
Select (`/eos/ds/<n>/<target type>/<count>`, manuel chap.31). Le layout
`reference/touchosc/ANALYSE_LAYOUT_TOUCHOSC.md` (voir plus bas) utilise aussi
des sous-formes non documentées dans notre corpus (`/eos/ds/2/fx/20`, `/ip/`,
`/fp/`, `/cp/`, `/bp/`, `/preset/`) qu'on ne sait pas distinguer avec certitude
d'une vraie création sans connaître le vocabulaire complet des `<target
type>` — les traiter comme des créations serait deviner leur format d'écho.

**Volontairement absent**, faute de syntaxe exacte confirmée dans le corpus —
adresse observée en catégorie seulement (journal terrain, l.188-192), ou format
d'argument non capturé :

- les 12 softkeys (libellés localisés observés, adresses jamais capturées) ;
- l'état de cue précédente (l'état *en attente* est désormais couvert, voir
  ci-dessus) ;
- `/eos/out/color/hs` ;
- le format exact des arguments de `/eos/out/pantilt` et `/eos/out/xyz` ;
- `/eos/out/event/locked` ;
- les événements LED (`/eos/out/event/sub/<n>`, `/eos/out/event/cue/<liste>/<cue>/fire|stop`) ;
- la création de banque Direct Select (voir ci-dessus).

Les inventer romprait la règle de fidélité du dépôt. Chacun reste une piste
« banc réel » ouverte — pas un oubli.

## Source des adresses Direct Select et Fader étendu

Confirmées par recoupement entre le manuel officiel (chap.31 Show Control,
tables Fader et Direct Select) et le layout TouchOSC officiel Eos analysé dans
[`reference/touchosc/ANALYSE_LAYOUT_TOUCHOSC.md`](../touchosc/ANALYSE_LAYOUT_TOUCHOSC.md)
— ce dernier a servi de point de départ (patterns d'adresses observés dans un
vrai fichier `.touchosc`), vérifié ensuite contre le manuel avant toute
implémentation ici. Rien de ce layout n'a été simulé sans cette double
confirmation.

## Tests réalisés (2026-07-31)

**Test 1** (`test-client.ts`) : envoi de `Chan 10 Thru 20 Color 3/195 Enter` (macro
générée pour la traduction NL « circuit 10 à 20 en L195 ») via `/eos/newcmd` → écho
reçu `/eos/out/cmd "LIVE: Chan 10 Thru 20 Color 3/195 Enter"` — pipeline transport OK.

**Test 2** (`test-client2.ts`) : envoi de `/eos/macro/1/fire` (1.0 puis 0.0) et
`/eos/key/go_0`. **Constat d'origine** : `fakeeos.ts` ne gérait pas
`/eos/macro/.../fire` (aucune réponse, silencieusement ignoré, sans même une
trace dans le log serveur) — lacune du simulateur, pas du paquet envoyé
(correctement formé/transporté). `/eos/key/go_0` en revanche échoué correctement
sur `/eos/out/key/go_0`. **Corrigé le 2026-09-26** : `/eos/macro/<n>/fire` et
`/eos/macro/fire` sont maintenant reconnus et journalisés à la réception ;
toujours sans écho, faute d'adresse de retour documentée ou observée pour ce
déclenchement — inventer une adresse serait aller au-delà de ce que le corpus
confirme.

**Test 3** (`test-client3.ts`) : macro à deux lignes générée pour la traduction NL
« groupe 5 + circuits 1 à 6 en Lee 195, enregistrer dans palette couleur 5,
libellé "195-Par LED" » :
```
Group 5 + 1 Thru 6 Color 3/195 Enter
Record Color Palette 5 Label 195-Par LED Enter
```
Les deux lignes sont transportées et échoées sans problème d'échappement, y
compris le libellé contenant espaces et tiret. **Non validé pour autant** : la
syntaxe `Group 5 + 1 Thru 6` (combiner groupe et plage de channels) n'a pas
d'exemple exact dans le corpus, et le comportement réel de `Record ... Label`
avec un libellé multi-mots dépend du clavier virtuel de la console — à vérifier
au banc réel.

**Constat d'origine, corrigé le 2026-09-26** : l'écho simulé sur `/eos/sub/<n>`
(avec délai) dans `fakeeos.ts` contredisait le journal terrain
(`JOURNAL_observations_nomad.md`), qui affirme qu'un vrai Eos ne republie
**jamais** spontanément sur cette adresse (feedback uniquement via les banques de
faders). Le simulateur reçoit et journalise désormais `/eos/sub/<n>` sans écho.

## Usage

```bash
npm install osc
npx tsx fakeeos.ts --port 3032 --framing 1.0 --echo-delay 500
# pour tester le chemin "refus" côté app (voir APP.md) :
npx tsx fakeeos.ts --port 3032 --erreur-pattern "Bogus"
# dans un autre terminal :
npx tsx test-client.ts
```

Nécessite le paquet npm `osc` (non inclus, à installer localement — pas de
`package.json` dans ce dossier, ce sont des scripts autonomes).

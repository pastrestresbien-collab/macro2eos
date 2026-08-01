# Outils de test — banc transport OSC/TCP

- `fakeeos.ts` — simulateur ETCnomad minimal (projet xtouch2Eos, fourni tel quel).
  Reproduit le comportement réseau observé sur un vrai nomad : état initial diffusé
  à la connexion, `/eos/ping` → `/eos/out/ping`, config de banque de faders, écho
  fader différé (~3 s par défaut, configurable), écho de touche, écho de ligne de
  commande sur `/eos/cmd`/`/eos/newcmd` (préfixé `"LIVE: "`).
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
Eos. `fakeeos.ts` accepte n'importe quelle chaîne de commande sans validation
syntaxique, contrairement à un vrai Eos qui renvoie un flag d'erreur
(`flag_erreur_int` sur `/eos/out/cmd`, cf. `JOURNAL_observations_nomad.md` et
`corpus/CORPUS_EOS_COMPLET.md` #140) en cas de syntaxe invalide.

**Toute macro validée uniquement contre ce simulateur reste non confirmée
syntaxiquement** — seul un vrai nomad/console peut trancher ce point.

## Tests réalisés (2026-07-31)

**Test 1** (`test-client.ts`) : envoi de `Chan 10 Thru 20 Color 3/195 Enter` (macro
générée pour la traduction NL « circuit 10 à 20 en L195 ») via `/eos/newcmd` → écho
reçu `/eos/out/cmd "LIVE: Chan 10 Thru 20 Color 3/195 Enter"` — pipeline transport OK.

**Test 2** (`test-client2.ts`) : envoi de `/eos/macro/1/fire` (1.0 puis 0.0) et
`/eos/key/go_0`. **Constat** : `fakeeos.ts` ne gère pas `/eos/macro/.../fire`
(aucune réponse, silencieusement ignoré) — lacune du simulateur, pas du paquet
envoyé (correctement formé/transporté). `/eos/key/go_0` en revanche échoué
correctement sur `/eos/out/key/go_0`.

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

**Constat récurrent, à garder en tête** : l'écho simulé sur `/eos/sub/<n>` (avec
délai) dans `fakeeos.ts` contredit le journal terrain (`JOURNAL_observations_nomad.md`),
qui affirme qu'un vrai Eos ne republie **jamais** spontanément sur cette adresse
(feedback uniquement via les banques de faders). Simplification du simulateur à
ne pas prendre pour argent comptant sur ce point précis.

## Usage

```bash
npm install osc
npx tsx fakeeos.ts --port 3032 --framing 1.0 --echo-delay 500
# dans un autre terminal :
npx tsx test-client.ts
```

Nécessite le paquet npm `osc` (non inclus, à installer localement — pas de
`package.json` dans ce dossier, ce sont des scripts autonomes).

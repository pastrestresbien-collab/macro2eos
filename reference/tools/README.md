# Outils de test — banc transport OSC/TCP

- `fakeeos.ts` — simulateur ETCnomad minimal (projet xtouch2Eos, fourni tel quel).
  Reproduit le comportement réseau observé sur un vrai nomad : état initial diffusé
  à la connexion, `/eos/ping` → `/eos/out/ping`, config de banque de faders, écho
  fader différé (~3 s par défaut, configurable), écho de touche, écho de ligne de
  commande sur `/eos/cmd`/`/eos/newcmd` (préfixé `"LIVE: "`).
- `test-client.ts` — client de test minimal utilisé pour valider le pipeline
  (session de consolidation, 2026-07-31) : connexion TCP, envoi d'une commande
  OSC framée (1.0, longueur 4 octets), lecture de la réponse.

## Ce que ça valide

Le **transport** OSC/TCP (framing, encodage, connexion, écho) — pas la **grammaire**
Eos. `fakeeos.ts` accepte n'importe quelle chaîne de commande sans validation
syntaxique, contrairement à un vrai Eos qui renvoie un flag d'erreur
(`flag_erreur_int` sur `/eos/out/cmd`, cf. `JOURNAL_observations_nomad.md` et
`corpus/CORPUS_EOS_COMPLET.md` #140) en cas de syntaxe invalide.

**Toute macro validée uniquement contre ce simulateur reste non confirmée
syntaxiquement** — seul un vrai nomad/console peut trancher ce point.

## Test réalisé (2026-07-31)

Envoi de `Chan 10 Thru 20 Color 3/195 Enter` (macro générée pour la traduction NL
« circuit 10 à 20 en L195 ») via `/eos/newcmd` → écho reçu
`/eos/out/cmd "LIVE: Chan 10 Thru 20 Color 3/195 Enter"` — confirme que le pipeline
transport (encodage, connexion, framing) fonctionne de bout en bout.

## Usage

```bash
npm install osc
npx tsx fakeeos.ts --port 3032 --framing 1.0 --echo-delay 500
# dans un autre terminal :
npx tsx test-client.ts
```

Nécessite le paquet npm `osc` (non inclus, à installer localement — pas de
`package.json` dans ce dossier, ce sont des scripts autonomes).

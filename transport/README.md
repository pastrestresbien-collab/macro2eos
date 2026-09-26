# transport/ — API Python : parler à Eos depuis Claude Code

Relie `grammar/generateur.py` (IR → commande) au transport OSC/TCP décrit dans
`reference/tools/`. Cible le **simulateur** par défaut (`127.0.0.1:3032`,
`reference/tools/fakeeos.ts`) — jamais une console réelle sans confirmation
explicite (voir `CLAUDE.md`, règle banc/matériel réel).

## Fichiers

| Fichier | Rôle |
|---|---|
| `eos_osc.py` | Client OSC/TCP, stdlib pur (pas de dépendance npm/pip). Encode/décode OSC 1.0, framing longueur 4 octets big-endian, absorption du burst initial, attente d'écho `/eos/out/cmd`. |
| `eos_send.py` | CLI : commande brute ou `--ir-json` (passée à `Generateur`), aperçu par défaut, `--send` pour transmettre réellement. |

## Usage

```bash
# terminal 1 — simulateur
cd reference/tools && npm install osc && npx tsx fakeeos.ts --port 3032

# terminal 2 — aperçu (aucune connexion)
python3 transport/eos_send.py "Chan 10 Thru 20 Color 3/195 Enter"

# envoi réel au simulateur
python3 transport/eos_send.py --send "Chan 10 Thru 20 Color 3/195 Enter"

# depuis une IR JSON (format attendu par grammar/generateur.py)
python3 transport/eos_send.py --send --ir-json exemple_ir.json
```

## Ce que ça valide, ce que ça ne valide pas

Même limite que `reference/tools/` : ceci prouve le **transport**, jamais la
**syntaxe**. Le simulateur accepte n'importe quelle chaîne sans la refuser (sauf
si on lance `fakeeos.ts --erreur-pattern <regex>`, commodité de test — voir
`reference/tools/README.md`) ; seul un Eos/ETCnomad réel peut confirmer qu'une
commande est valide (voir `APP.md`, « La console fait autorité »).

`eos_send.py` lit désormais les deux arguments confirmés de l'écho
(`texte, flag_erreur_int`, corpus #140) et affiche « acceptée » / « REFUSÉE » en
conséquence — utile pour développer le chemin de refus de l'écran 1 (`APP.md`)
avant d'avoir accès à une vraie console.

## Portée actuelle

- Types OSC supportés : chaîne, entier, flottant (suffisant pour `/eos/newcmd`,
  `/eos/cmd`, `/eos/macro/<n>/fire`, `/eos/key/...`).
- Pas de gestion des banques de faders ni des touches — hors périmètre pour
  l'instant, le besoin est l'injection de ligne de commande.
- `--send` vers autre chose que `127.0.0.1:3032` demande une confirmation
  interactive (`o`/`N`) : garde-fou minimal avant de sortir du simulateur.

#!/usr/bin/env python3
"""CLI d'envoi de commande(s) Eos — cible le simulateur par défaut.

Usage :

    # aperçu seul, aucune connexion (défaut)
    python3 transport/eos_send.py "Chan 10 Thru 20 Color 3/195 Enter"

    # envoi réel, vers le simulateur local (reference/tools/fakeeos.ts)
    python3 transport/eos_send.py --send "Chan 10 Thru 20 Color 3/195 Enter"

    # depuis une IR (JSON), passée par grammar/generateur.py
    python3 transport/eos_send.py --send --ir-json exemple_ir.json

Ne cible jamais une console réelle par défaut : `--host`/`--port` doivent être
fournis explicitement pour sortir de `127.0.0.1:3032` (voir CLAUDE.md,
règle sur le banc/matériel réel — confirmation attendue avant tout envoi hors
simulateur).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RACINE = Path(__file__).parent.parent
sys.path.insert(0, str(RACINE / "grammar"))
sys.path.insert(0, str(RACINE))

from generateur import Generateur  # noqa: E402
from transport.eos_osc import EosClient  # noqa: E402

HOTE_DEFAUT = "127.0.0.1"
PORT_DEFAUT = 3032


def obtenir_lignes(args: argparse.Namespace) -> tuple[list[str], list[str]]:
    """Renvoie (lignes de commande, avertissements) selon la source choisie."""
    if args.ir_json:
        ir = json.loads(Path(args.ir_json).read_text(encoding="utf-8"))
        resultat = Generateur().rendre(ir)
        return resultat.commande.splitlines(), resultat.avertissements
    return args.commande.splitlines(), []


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("commande", nargs="?", default="", help="ligne(s) de commande Eos brutes")
    p.add_argument("--ir-json", help="fichier JSON contenant une IR à passer au générateur")
    p.add_argument("--host", default=HOTE_DEFAUT)
    p.add_argument("--port", type=int, default=PORT_DEFAUT)
    p.add_argument("--send", action="store_true", help="envoie réellement (sinon, aperçu seul)")
    p.add_argument("--timeout", type=float, default=2.0, help="délai d'attente de l'écho (s)")
    args = p.parse_args()

    if not args.commande and not args.ir_json:
        p.error("fournir une commande ou --ir-json")

    lignes, avertissements = obtenir_lignes(args)

    cible_hors_defaut = (args.host, args.port) != (HOTE_DEFAUT, PORT_DEFAUT)

    print(f"cible : {args.host}:{args.port}" + (" (⚠ hors simulateur par défaut)" if cible_hors_defaut else ""))
    for ligne in lignes:
        print(f"  EOS> {ligne}")
    for a in avertissements:
        print(f"  ⚠ {a}")

    if not args.send:
        print("(aperçu seul — relancer avec --send pour envoyer)")
        return 0

    if cible_hors_defaut:
        reponse = input(
            f"Cible hors simulateur ({args.host}:{args.port}) — confirmer l'envoi ? [o/N] "
        )
        if reponse.strip().lower() not in ("o", "oui", "y", "yes"):
            print("annulé")
            return 1

    client = EosClient(args.host, args.port, timeout=args.timeout)
    client.connect()
    burst = client.absorber_burst_initial()
    if burst:
        print(f"(burst initial absorbé : {len(burst)} messages)")

    echecs = 0
    for ligne in lignes:
        client.envoyer_commande(ligne)
        echo = client.attendre_echo_cmd(timeout=args.timeout)
        if echo is None:
            print(f"  {ligne!r} → (aucun écho reçu avant {args.timeout}s)")
            echecs += 1
        else:
            # Format confirmé au banc actif (corpus #140) : (texte, flag_erreur_int).
            texte, *reste = echo.args
            flag = reste[0] if reste else None
            statut = {0: "acceptée", 1: "REFUSÉE (erreur de syntaxe)"}.get(flag, "statut inconnu")
            print(f"  {ligne!r} → {echo.adresse} {texte!r} — {statut}")
            if flag == 1:
                echecs += 1

    client.close()
    return 1 if echecs else 0


if __name__ == "__main__":
    raise SystemExit(main())

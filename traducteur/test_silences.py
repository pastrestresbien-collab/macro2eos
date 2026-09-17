#!/usr/bin/env python3
"""Banc n°6 — la chasse au SILENCE, par invariants plutôt que par cas écrits.

Pourquoi un sixième banc. Les cinq autres comparent le traducteur à des
attentes écrites à la main : ils protègent des régressions sur ce qu'on a
PENSÉ à tester. Or toutes les pannes graves de ce projet appartiennent à une
seule famille — la commande a l'air juste, le statut est `compris`, rien
n'est signalé, et le résultat ne répond pas à la demande. Par construction,
un cas écrit à la main ne trouve pas ça : on ne teste pas ce à quoi on n'a
pas pensé.

Ce banc ne compare donc à aucune attente. Il vérifie des INVARIANTS que toute
traduction correcte doit respecter, quelle que soit la phrase :

  A. CONSERVATION — un nombre écrit dans la phrase se retrouve dans la
     commande, ou est signalé (`ignores` / `non_reconnus`). Un nombre qui
     disparaît sans un mot est la signature exacte de la panne ci-dessus.
     Attention : un nombre nu n'est PAS du vocabulaire, donc `_ignores` ne le
     rattrape jamais tout seul — c'est précisément pour ça qu'il faut le
     vérifier ici.

  B. MUTATION — si on change un nombre de la phrase, la commande DOIT changer.
     Sinon le traducteur ne s'en servait pas : il a rendu une commande
     plausible en ignorant une donnée de la demande.

  D. DURÉE — ajouter « en 7 secondes » à n'importe quelle phrase donne deux
     issues acceptables, et deux seulement : la commande emploie la durée, ou
     la traduction est REFUSÉE. Rendre la même commande qu'avant veut dire
     que la durée est tombée en silence. Un mot de durée n'est pas rattrapé
     par `_ignores` (ce n'est pas du vocabulaire de créneau), donc rien
     d'autre ne le voit.

  C. INVARIANCE À L'ORDRE DES MOTS — la même demande, formulée dans plusieurs
     ordres naturels, doit produire la MÊME commande. Une divergence veut dire
     qu'un nombre est lu au mauvais endroit selon la tournure.

Trouvé par ce banc le 2026-09-17, trois pannes silencieuses d'un coup, toutes
sur le mécanisme générique des paramètres :
    « le pan des circuits 1 à 5 à 50 degrés »  ->  `Chan 1 Pan 50`
        la plage TRONQUÉE à un seul circuit, sans aucun signal ;
    « le zoom des circuits 1 à 5 à 50 % »      ->  `Chan 1 Zoom 05`
        plage tronquée ET valeur fausse (5 % au lieu de 50) ;
    « le hue des circuits 1 à 5 à 180 »        ->  `Chan 1 Hue 5`
        valeur remplacée par une borne de plage.

Les familles du test C se construisent depuis `grammar/modele.yaml` : ajouter
un paramètre au catalogue l'ajoute ici sans toucher à ce fichier.
"""
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "traducteur"))
sys.path.insert(0, str(RACINE / "grammar"))

import yaml                                                  # noqa: E402
from traducteur import Traducteur                            # noqa: E402
from generateur import Generateur                            # noqa: E402

TRAD = Traducteur(generateur=Generateur())
CATALOGUE = json.loads((RACINE / "app" / "data" / "catalogue.json").read_text("utf-8"))
MODELE = yaml.safe_load((RACINE / "grammar" / "modele.yaml").read_text("utf-8"))

# Un décalage franc, pour qu'aucune valeur mutée ne retombe par hasard sur une
# autre valeur de la phrase.
DECALAGE = 37


def rendu(phrase: str):
    trad = TRAD.traduire(phrase)
    if not trad.compris:
        return None, trad
    return TRAD.rendre(trad).commande, trad


def chiffres(texte: str) -> list[re.Match]:
    return list(re.finditer(r"\d+", texte))


def present(valeur: str, commande: str) -> bool:
    """`05` et `5` sont le même nombre — le zéro de tête est une mise en forme
    du générateur (règle du zéro implicite), pas une valeur différente."""
    return any(int(t) == int(valeur) for t in re.findall(r"\d+", commande))


def familles_ordre() -> list[tuple[str, list[str]]]:
    """Même demande, plusieurs tournures — construites depuis le modèle."""
    unites = {"Pan": "degres", "Tilt": "degres",
              "Zoom": "%", "Iris": "%", "Edge": "%"}
    familles = []
    for nom, spec in MODELE.get("parametres", {}).items():
        if "absolue" not in spec.get("formes", {}):
            continue
        mot = nom.split("_")[0].lower() if nom != "Color_Crossfade" else None
        if mot is None:              # nommé par une paire de mots, pas un alias
            continue
        suffixe = f" {unites[nom]}" if nom in unites else ""
        for objet in ("circuit", "groupe"):
            familles.append((f"{nom}/{objet}", [
                f"mets le {mot} du {objet} 1 à 50{suffixe}",
                f"{objet} 1 {mot} à 50{suffixe}",
                f"{mot} à 50{suffixe} sur le {objet} 1",
                f"règle le {mot} à 50{suffixe} pour le {objet} 1",
            ]))
        # PLAGES — la famille qui a livré les trois pannes du 2026-09-17. Sans
        # elle, ce banc ne couvrirait pas le cas qu'il documente en tête de
        # fichier : le « à » y sépare une plage ET introduit une valeur, et
        # seule la présence d'un marqueur d'unité permet de trancher. Les
        # paramètres SANS unité déclarée (Hue, Saturation) en sont exclus à
        # dessein — la phrase y est réellement ambiguë et le traducteur doit
        # poser une question, ce que le test C ne sait pas exprimer.
        if suffixe:
            familles.append((f"{nom}/plage", [
                f"mets le {mot} des circuits 2 à 8 à 50{suffixe}",
                f"circuits 2 à 8 {mot} à 50{suffixe}",
            ]))
    for objet in ("circuit", "adresse"):
        familles.append((f"verifier/{objet}", [
            f"vérifie le {objet} 3 à 75 %",
            f"vérifie à 75 % le {objet} 3",
        ]))
    familles += [
        ("intensite", ["mets le circuit 3 à 50 %", "circuit 3 à 50 %",
                       "à 50 % le circuit 3"]),
        ("plein_feu", ["mets le circuit 3 à fond", "circuit 3 à fond",
                       "plein feu sur le circuit 3"]),
        ("fondu_couleur", ["passe le fondu de couleur à 50",
                           "mets le fondu de couleur à 50",
                           "fondu de couleur à 50"]),
    ]
    return familles


def main() -> int:
    echecs: list[str] = []
    testees = 0

    # -- A et B, sur les phrases du catalogue (garanties traduisibles) -------
    questions = 0
    for entree in CATALOGUE:
        phrase = entree["phrase"]
        commande, trad = rendu(phrase)
        if commande is None:
            # `a_preciser` est une ISSUE LÉGITIME, pas un échec : le
            # traducteur pose une question au lieu de deviner (modèle à trois
            # résultats). On ne peut pas vérifier d'invariant sur une
            # question — il n'y a pas encore de commande — mais on le compte
            # et on le dit, plutôt que de passer en silence.
            if trad.statut == "a_preciser":
                questions += 1
                continue
            echecs.append(f"[{entree['intention']}] phrase de catalogue "
                          f"intraduisible : « {phrase} »")
            continue
        signales = set(trad.ignores) | set(trad.non_reconnus)
        for m in chiffres(phrase):
            testees += 1
            if not present(m.group(), commande) and m.group() not in signales:
                echecs.append(
                    f"A. NOMBRE DISPARU — [{entree['intention']}] « {phrase} »\n"
                    f"     le nombre {m.group()} n'est ni dans « {commande} » "
                    f"ni signalé")
            mute = phrase[:m.start()] + str(int(m.group()) + DECALAGE) + phrase[m.end():]
            commande_mutee, _ = rendu(mute)
            if commande_mutee == commande:
                echecs.append(
                    f"B. NOMBRE SANS EFFET — [{entree['intention']}] « {phrase} »\n"
                    f"     changer {m.group()} ne change pas « {commande} »")

    # -- D, la durée ne tombe jamais en silence ------------------------------
    for entree in CATALOGUE:
        phrase = entree["phrase"]
        commande, trad = rendu(phrase)
        if commande is None:
            continue
        # Une phrase qui porte DÉJÀ une durée est exclue : lui en ajouter une
        # seconde crée un doublon, et c'est la première qui gagne — un test
        # qui échouerait sur une phrase absurde plutôt que sur un défaut.
        # Ces phrases-là sont couvertes par l'invariant B, qui change leur
        # durée existante au lieu d'en empiler une autre.
        if trad.ir and Traducteur._ir_porte_une_duree(trad.ir):
            continue
        avec, _ = rendu(f"{phrase} en 7 secondes")
        testees += 1
        if avec == commande:
            echecs.append(
                f"D. DURÉE PERDUE — [{entree['intention']}] « {phrase} »\n"
                f"     « en 7 secondes » ne change rien : « {commande} »")

    # -- C, invariance à l'ordre des mots ------------------------------------
    for nom, phrases in familles_ordre():
        rendus: dict[str, list[str]] = {}
        for phrase in phrases:
            commande, _ = rendu(phrase)
            testees += 1
            rendus.setdefault(commande or "<incompris>", []).append(phrase)
        comprises = {c: p for c, p in rendus.items() if c != "<incompris>"}
        if not comprises:
            echecs.append(f"C. FAMILLE MUETTE — [{nom}] aucune tournure ne se "
                          f"traduit : ce test ne protège plus rien")
        elif len(comprises) > 1:
            detail = "\n".join(f"       {c!r} <- « {p[0]} »"
                               for c, p in comprises.items())
            echecs.append(f"C. ORDRE DES MOTS — [{nom}] tournures divergentes :\n{detail}")

    if echecs:
        print("SILENCES DÉTECTÉS :\n")
        for e in echecs:
            print(f"  {e}")
        print(f"\n{len(echecs)} invariant(s) violé(s) sur {testees} vérifications.")
        return 1
    print(f"{testees} vérifications d'invariants — aucun silence détecté.")
    if questions:
        print(f"  ({questions} phrase(s) de catalogue en `a_preciser` : une "
              f"question, pas une commande — invariants non applicables.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

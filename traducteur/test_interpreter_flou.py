#!/usr/bin/env python3
"""Non-régression de `Traducteur.interpreter_flou` (moteur flou, phase 1).

`sortie_llm` est toujours un dict écrit à la main ici — cette méthode ne
touche jamais le réseau, c'est ce qui la rend testable de façon aussi
déterministe que le reste du traducteur. Un vrai appel LLM (phase 2 du plan)
n'entre jamais dans ce fichier : c'est `app/llm_bridge.js` qui produira
`sortie_llm`, déjà validé contre `traducteur/dist/vocabulaire_llm.json`.

    cd traducteur && python3 test_interpreter_flou.py
"""
from __future__ import annotations

import sys

from traducteur import Traducteur

CAS = [
    {
        # Une sortie LLM est une donnée EXTERNE : sa forme n'est jamais
        # garantie, même quand le prompt la décrit. `{"reponses": "haut"}` —
        # une chaîne au lieu d'un dict — faisait lever un AttributeError,
        # donc PLANTER l'app dans le navigateur, au lieu d'ignorer une
        # réponse mal formée. Trouvé le 2026-09-17 en sondant ce chemin avec
        # des sorties hostiles.
        #
        # Tout le reste tenait déjà et c'est le résultat rassurant de ce
        # sondage : option inventée, clé inconnue, valeur nulle, tentative
        # d'injection dans une réponse — toutes retombent proprement sur
        # `a_preciser`. Le LLM ne peut RIEN forcer : il ne fait que répondre
        # à des questions déjà posées, il ne propose jamais de commande.
        "nom": "sortie LLM mal formée — ignorée, jamais fatale",
        "phrase": "bump le sub 5",
        "sortie_llm": {"reponses": "haut"},
        "statut": "a_preciser",
        "questions": ["bump_direction"],
        "options": ["haut", "bas"],
    },
    {
        "nom": "sortie LLM qui n'est même pas un dict",
        "phrase": "bump le sub 5",
        "sortie_llm": "haut",
        "statut": "a_preciser",
        "questions": ["bump_direction"],
        "options": ["haut", "bas"],
    },
    {
        "nom": "option inventée par le LLM — jamais retenue",
        "phrase": "bump le sub 5",
        "sortie_llm": {"reponses": {"bump_direction": "lateral"}},
        "statut": "a_preciser",
        "questions": ["bump_direction"],
        "options": ["haut", "bas"],
    },
    {
        "nom": "déjà compris — l'avis du LLM n'est jamais consulté",
        "phrase": "groupe 5 en lee 195",
        "sortie_llm": {"reponses": {"nuancier": "autre"}},
        "statut": "compris",
        "rendu": "Group 5 Color 3/195 Enter",
    },
    {
        "nom": "aucune sortie LLM — identique à traduire() seul",
        "phrase": "bump le sub 5",
        "sortie_llm": None,
        "statut": "a_preciser",
        "questions": ["bump_direction"],
        "options": ["haut", "bas"],
    },
    {
        "nom": "candidat unique valide — complète et retraduit",
        "phrase": "bump le sub 5",
        "sortie_llm": {"reponses": {"bump_direction": "haut"}},
        "statut": "compris",
        "rendu": "SubUp 5 Enter",
    },
    {
        "nom": "couleur ambiguë — candidat unique valide",
        "phrase": "groupe 5 en lee ambre",
        "sortie_llm": {"reponses": {"couleur:ambre": "102"}},
        "statut": "compris",
        "rendu": "Group 5 Color 3/102 Enter",
    },
    {
        # Le garde-fou central : une valeur hors du vocabulaire déjà connu
        # de cette question précise (ici, pas une des options réellement
        # proposées) est ignorée — jamais acceptée à l'aveugle.
        "nom": "candidat hors vocabulaire — ignoré, question reposée telle quelle",
        "phrase": "bump le sub 5",
        "sortie_llm": {"reponses": {"bump_direction": "gauche"}},
        "statut": "a_preciser",
        "questions": ["bump_direction"],
        "options": ["haut", "bas"],
    },
    {
        # « propose plusieurs choses » : réduit la question à ces candidats,
        # ne choisit jamais à la place de l'utilisateur.
        "nom": "plusieurs candidats valides — question réduite, pas devinée",
        "phrase": "groupe 5 en lee ambre",
        "sortie_llm": {"reponses": {"couleur:ambre": ["102", "20"]}},
        "statut": "a_preciser",
        "questions": ["couleur:ambre"],
        "options": ["102", "20"],
    },
    {
        # Un mélange de candidats valides et invalides ne garde que les valides.
        "nom": "candidats mixtes — seuls les valides survivent au filtrage",
        "phrase": "groupe 5 en lee ambre",
        "sortie_llm": {"reponses": {"couleur:ambre": ["102", "999", "20"]}},
        "statut": "a_preciser",
        "questions": ["couleur:ambre"],
        "options": ["102", "20"],
    },
    {
        # Aucune intention reconnue du tout : le moteur flou ne rescape pas
        # un `incompris` complet dans cette tranche (voir docstring de la
        # méthode et PLANNING.md).
        "nom": "incompris complet — jamais rescapé par le LLM",
        "phrase": "xyz totalement hors sujet blibli",
        "sortie_llm": {"reponses": {"nimporte_quoi": "valeur"}},
        "statut": "incompris",
    },
]


def controler(nom: str, obtenu, attendu) -> bool:
    if obtenu == attendu:
        return True
    print(f"  ÉCHEC — {nom}")
    print(f"    attendu : {attendu!r}")
    print(f"    obtenu  : {obtenu!r}")
    return False


def main() -> int:
    t = Traducteur()
    echecs = 0

    for cas in CAS:
        trad = t.interpreter_flou(cas["phrase"], cas["sortie_llm"])
        ok = controler(f"{cas['nom']} (statut)", trad.statut, cas["statut"])

        if "questions" in cas:
            ok &= controler(f"{cas['nom']} (questions)",
                            [q.id for q in trad.questions], cas["questions"])

        if "options" in cas:
            ok &= controler(f"{cas['nom']} (options)",
                            [o.cle for q in trad.questions for o in q.options],
                            cas["options"])

        if "rendu" in cas:
            ok &= controler(f"{cas['nom']} (rendu)",
                            t.rendre(trad).commande, cas["rendu"])

        echecs += not ok

    total = len(CAS)
    if echecs:
        print(f"\n{echecs} cas en échec sur {total}.")
        return 1
    print(f"{total} cas de moteur flou (interpreter_flou) — tous conformes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

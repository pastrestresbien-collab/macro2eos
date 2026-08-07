#!/usr/bin/env python3
"""Non-régression du traducteur NL → IR.

Chaque cas déclare une phrase et ce qu'elle doit produire : soit une commande
rendue (via `grammar/generateur.py`, jamais réécrite ici), soit une question,
soit un refus. **Les trois issues sont testées** : un traducteur qui ne sait pas
dire « je n'ai pas compris » finit par deviner.

CAS D'ANCRAGE : la demande réelle de l'utilisateur, recopiée verbatim, fautes de
frappe comprises. C'est elle qui a motivé l'axe B, elle ne doit jamais casser.

    cd traducteur && python3 test_traducteur.py
"""
from __future__ import annotations

import sys

from traducteur import Traducteur

# La phrase réelle, telle qu'elle a été tapée en session le 2026-08-03.
# « palette » au singulier, « 1 a 6 » sans accent, « chang » pour « chaud »,
# initiales pour les quatre dernières couleurs. Ne pas la « nettoyer » : c'est
# précisément ce bruit-là que le traducteur doit encaisser.
PHRASE_REELLE = ("créer les palette de couleur 1 a 6 avec les références lee, "
                 "chang froid r v b j")

CAS = [
    # ------------------------------------------------- cas d'ancrage réel
    {
        "nom": "phrase réelle — la portée n'est jamais devinée",
        "phrase": PHRASE_REELLE,
        "statut": "a_preciser",
        "questions": ["portee_enregistrement"],
    },
    {
        # La portée n'est plus une alternative « avec ou sans circuits » : les
        # deux options en exigent. `{By Type}` décrit ce que la palette
        # contiendra, pas comment elle s'enregistre (manuel §10).
        "nom": "phrase réelle + palette générique sur un groupe de travail",
        "phrase": PHRASE_REELLE,
        "reponses": {"portee_enregistrement": {"cle": "par_type",
                                               "valeur": "groupe 99"}},
        "statut": "compris",
        "rendu": (
            "Group 99 Color 3/205 Enter\n"
            "Group 99 Record Color Palette 1 {By Type} Label Chaud Enter\n"
            "Group 99 Color 3/202 Enter\n"
            "Group 99 Record Color Palette 2 {By Type} Label Froid Enter\n"
            "Group 99 Color 3/106 Enter\n"
            "Group 99 Record Color Palette 3 {By Type} Label Rouge Enter\n"
            "Group 99 Color 3/139 Enter\n"
            "Group 99 Record Color Palette 4 {By Type} Label Vert Enter\n"
            "Group 99 Color 3/120 Enter\n"
            "Group 99 Record Color Palette 5 {By Type} Label Bleu Enter\n"
            "Group 99 Color 3/101 Enter\n"
            "Group 99 Record Color Palette 6 {By Type} Label Jaune Enter"),
    },
    {
        # LA correction du 2026-08-06. La sélection est reposée sur CHAQUE
        # ligne, y compris les Record : elle ne survit pas à un enregistrement
        # (manuel §6, énoncé deux fois). La version précédente de ce test
        # n'écrivait la sélection que sur les lignes `Color` — elle décrivait
        # une macro dont seule la première palette aurait été correcte.
        "nom": "phrase réelle + circuits précis — sélection reposée à chaque ligne",
        "phrase": PHRASE_REELLE,
        "reponses": {"portee_enregistrement": {"cle": "selection", "valeur": "1 a 10"}},
        "statut": "compris",
        "rendu": (
            "Chan 1 Thru 10 Color 3/205 Enter\n"
            "Chan 1 Thru 10 Record Color Palette 1 Label Chaud Enter\n"
            "Chan 1 Thru 10 Color 3/202 Enter\n"
            "Chan 1 Thru 10 Record Color Palette 2 Label Froid Enter\n"
            "Chan 1 Thru 10 Color 3/106 Enter\n"
            "Chan 1 Thru 10 Record Color Palette 3 Label Rouge Enter\n"
            "Chan 1 Thru 10 Color 3/139 Enter\n"
            "Chan 1 Thru 10 Record Color Palette 4 Label Vert Enter\n"
            "Chan 1 Thru 10 Color 3/120 Enter\n"
            "Chan 1 Thru 10 Record Color Palette 5 Label Bleu Enter\n"
            "Chan 1 Thru 10 Color 3/101 Enter\n"
            "Chan 1 Thru 10 Record Color Palette 6 Label Jaune Enter"),
    },
    {
        # Sans valeur de sélection, la question doit être reposée — même quand
        # l'option choisie est « par type ». C'est le bug de conception corrigé.
        "nom": "portée « par type » sans circuits — la question est reposée",
        "phrase": PHRASE_REELLE,
        "reponses": {"portee_enregistrement": "par_type"},
        "statut": "a_preciser",
        "questions": ["portee_enregistrement"],
    },
    {
        # Même phrase écrite proprement : doit donner exactement le même
        # résultat. Si les deux divergent, la tolérance au bruit est illusoire.
        "nom": "phrase réelle écrite proprement — résultat identique",
        "phrase": ("créer les palettes de couleur 1 à 6 avec les références Lee : "
                   "chaud, froid, rouge, vert, bleu, jaune"),
        "reponses": {"portee_enregistrement": {"cle": "par_type",
                                               "valeur": "groupe 99"}},
        "statut": "compris",
        "rendu": (
            "Group 99 Color 3/205 Enter\n"
            "Group 99 Record Color Palette 1 {By Type} Label Chaud Enter\n"
            "Group 99 Color 3/202 Enter\n"
            "Group 99 Record Color Palette 2 {By Type} Label Froid Enter\n"
            "Group 99 Color 3/106 Enter\n"
            "Group 99 Record Color Palette 3 {By Type} Label Rouge Enter\n"
            "Group 99 Color 3/139 Enter\n"
            "Group 99 Record Color Palette 4 {By Type} Label Vert Enter\n"
            "Group 99 Color 3/120 Enter\n"
            "Group 99 Record Color Palette 5 {By Type} Label Bleu Enter\n"
            "Group 99 Color 3/101 Enter\n"
            "Group 99 Record Color Palette 6 {By Type} Label Jaune Enter"),
    },

    # ------------------------------------------------- colorer une sélection
    {
        # Reprend `selection_plage_couleur` (grammar/patrons.yaml, confiance A)
        # et le premier cas de test_generateur.py — la boucle est bouclée.
        "nom": "plage de circuits + numéro de gel explicite",
        "phrase": "circuits 10 a 20 en lee 195",
        "statut": "compris",
        "rendu": "Chan 10 Thru 20 Color 3/195 Enter",
    },
    {
        "nom": "plage de circuits + couleur nommée",
        "phrase": "circuits 1 à 5 en rouge",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/106 Enter",
    },
    {
        "nom": "un seul circuit",
        "phrase": "circuit 4 en lee 195",
        "statut": "compris",
        "rendu": "Chan 4 Color 3/195 Enter",
    },
    {
        "nom": "groupe plutôt que circuits",
        "phrase": "groupe 5 en bleu",
        "statut": "compris",
        "rendu": "Group 5 Color 3/120 Enter",
    },

    # ------------------------------------------------------------------ cues
    {
        # Reprend `record_cue_selectif` (grammar/patrons.yaml, confiance A) et
        # l'exemple chiffré du manuel §12 recopié dans test_generateur.py —
        # même macro par deux voies indépendantes.
        "nom": "enregistrement sélectif dans une cue",
        "phrase": "enregistrer les circuits 1 à 5 dans la cue 4",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Record Cue 4 Enter",
    },
    {
        # Piège réellement rencontré : « groupe » est à distance 2 de
        # « rouge », dans la marge de tolérance normale. Le joker `@couleurs`
        # de `colorer_selection` matchait donc « groupe » en « rouge » et
        # détournait toute la phrase vers la mauvaise intention — pas une
        # mauvaise couleur, une mauvaise INTENTION. Corrigé en interdisant la
        # tolérance aux fautes dans la détection d'intention elle-même (elle
        # reste réservée au remplissage d'un créneau déjà choisi).
        "nom": "enregistrement sélectif — groupe plutôt que circuits",
        "phrase": "enregistrer le groupe 2 dans la cue 5",
        "statut": "compris",
        "rendu": "Group 2 Record Cue 5 Enter",
    },
    {
        "nom": "go to cue — numéro",
        "phrase": "aller à la cue 5",
        "statut": "compris",
        "rendu": "Go To Cue 5 Enter",
    },
    {
        # Cible symbolique : aucun numéro dans la phrase, aucun mot « cue » non
        # plus. « noir » seul doit suffire à déclencher l'intention.
        "nom": "go to cue — cible symbolique « noir » = Out",
        "phrase": "va au noir",
        "statut": "compris",
        "rendu": "Go To Cue Out Enter",
    },
    {
        "nom": "go to cue — cible symbolique « suivante » = Next",
        "phrase": "va a la suivante",
        "statut": "compris",
        "rendu": "Go To Cue Next Enter",
    },
    {
        "nom": "enregistrer cue sans sélection — refus assumé",
        "phrase": "enregistrer dans la cue 4",
        "statut": "incompris",
    },
    {
        "nom": "aller à cue sans cible — refus assumé",
        "phrase": "aller a la cue",
        "statut": "incompris",
    },

    # ------------------------------------------------------------ intensité
    {
        # Deux « à » dans la phrase : le premier borne les circuits, le second
        # introduit le niveau. Lire le niveau en premier donnerait un dégradé.
        "nom": "intensité simple — deux « à » à ne pas confondre",
        "phrase": "circuits 1 à 5 à 50 %",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 50 Enter",
    },
    {
        "nom": "dégradé d'intensité",
        "phrase": "circuits 1 à 5 de 10 à 50 %",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 10 Thru 50 Enter",
    },
    {
        # Le piège le plus coûteux du projet : `At 5` vaut 50 %. Le générateur
        # écrit deux chiffres, et le traducteur ne doit pas le contourner.
        "nom": "niveau sous 10 % — zéro de tête conservé",
        "phrase": "circuits 1 à 5 à 5 %",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 05 Enter",
    },
    {
        "nom": "niveau sans marqueur — refus assumé",
        "phrase": "circuits 1 à 5 à 50",
        "statut": "incompris",
    },

    # ------------------------------------------ questions plutôt que devinettes
    {
        # Les numéros de gel sont vérifiés un par un, et pas seulement le fait
        # qu'une question soit posée. Motif : `020` écrit tel quel dans un YAML
        # est lu comme de l'OCTAL et vaut 16 — bug réellement rencontré à
        # l'écriture de ce lexique, silencieux et plausible. Ce cas le rattrape.
        "nom": "couleur ambiguë — quatre ambres au catalogue, numéros compris",
        "phrase": "créer la palette de couleur 1 avec la référence lee ambre",
        "statut": "a_preciser",
        "questions": ["couleur:ambre"],
        "options": ["162", "102", "20", "104"],
    },
    {
        "nom": "couleur ambiguë — « rose » ne se traduit pas par « Rose »",
        "phrase": "créer la palette de couleur 1 avec la référence lee rose",
        "statut": "a_preciser",
        "questions": ["couleur:rose"],
        "options": ["157", "2", "107", "128"],
    },

    # -------------------------------------------------------------- refus
    {
        "nom": "autant de palettes que de couleurs — sinon refus",
        "phrase": "créer les palettes de couleur 1 à 6 en lee rouge vert",
        "statut": "incompris",
    },
    {
        "nom": "hors sujet — aucune intention reconnue",
        "phrase": "fais moi un café",
        "statut": "incompris",
    },
    {
        "nom": "palettes sans aucune couleur",
        "phrase": "créer les palettes de couleur 1 à 6",
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
        trad = t.traduire(cas["phrase"], reponses=cas.get("reponses"))
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

        # Un mot non reconnu qui passe inaperçu est une traduction partielle
        # présentée comme complète — pire qu'un refus.
        if trad.statut == "compris" and trad.non_reconnus:
            print(f"  ÉCHEC — {cas['nom']} (mots non reconnus alors que compris)")
            print(f"    {trad.non_reconnus}")
            ok = False

        echecs += not ok

    total = len(CAS)
    if echecs:
        print(f"\n{echecs} cas en échec sur {total}.")
        return 1
    print(f"{total} cas de traduction — tous conformes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Non-régression du générateur.

Deux familles de cas, qui ne prouvent pas la même chose :

1. **Transport** — les macros déjà passées au banc de transport
   (`reference/tools/`). Si une évolution du modèle les modifie, c'est une
   régression : le travail déjà validé doit rester reproductible.
2. **Manuel** — les exemples chiffrés du manuel officiel v3.2.0, recopiés
   verbatim. Ce sont les seuls cas où l'on sait ce que la console fait vraiment.
   Ils ancrent le modèle à sa source A.

Différence de forme assumée avec le manuel : le générateur écrit toujours `Chan`
et `Cue` explicitement, là où le manuel s'appuie sur les modes implicites du
clavier (`[1][Thru][5]` = channels, `[Record][5]` = cue). Une macro se relit et
se réimporte — l'implicite y coûte plus cher qu'il ne rapporte.

Le nombre d'avertissements fait partie de l'attendu : un silence sur une zone
d'ombre serait le vrai bug.

    python3 grammar/test_generateur.py
"""
from __future__ import annotations

import sys

from generateur import Generateur

CAS = [
    # ---------------------------------------------------------------- v0.1
    {
        "nom": "test-client.ts — plage de channels + gel",
        "ir": [
            {"selection": {"objet": "Chan", "de": 10, "a": 20},
             "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
        ],
        "attendu": "Chan 10 Thru 20 Color 3/195 Enter",
        "avertissements": 0,
    },
    {
        "nom": "test-client3.ts — sélection mixte + record palette",
        "ir": [
            {"selection": {"objet": "Group", "numero": 5, "plus_plage": [1, 6]},
             "action": {"type": "couleur_gel", "nuancier": 3, "teinte": 195}},
            {"action": {"type": "record_palette_couleur", "cible": 5,
                        "label": "195-Par LED"}},
        ],
        "attendu": ("Group 5 + 1 Thru 6 Color 3/195 Enter\n"
                    "Record Color Palette 5 Label 195-Par LED Enter"),
        # doit signaler les deux zones d'ombre — un silence ici serait le vrai bug
        "avertissements": 2,
    },

    # ------------------------------------------------------------ Fan (§8)
    {
        "nom": "manuel §8 — fan implicite, sans touche Fan",
        # [1][Thru][5][At][1]<0>[Thru][5]<0>[Enter] → 10, 20, 30, 40, 50 %
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "intensite", "de": 10, "a": 50}},
        ],
        "attendu": "Chan 1 Thru 5 At 10 Thru 50 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan {Mirror Out}",
        # [1][Thru][1][0][At][1][0][Thru][3][0][Fan]{Mirror Out}[Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 10},
             "action": {"type": "intensite", "de": 10, "a": 30,
                        "fan": {"style": "Mirror Out"}}},
        ],
        "attendu": "Chan 1 Thru 10 At 10 Thru 30 Fan {Mirror Out} Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan {Repeat} 3",
        # [1][Thru][1][2][At][5][0][Thru][7][0][Fan]{Repeat}[3][Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 12},
             "action": {"type": "intensite", "de": 50, "a": 70,
                        "fan": {"style": "Repeat", "argument": 3}}},
        ],
        "attendu": "Chan 1 Thru 12 At 50 Thru 70 Fan {Repeat} 3 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan {Cluster} 4",
        # [1][Thru][1][2][At][5][0][Thru][8][0][Fan]{Cluster}[4][Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 12},
             "action": {"type": "intensite", "de": 50, "a": 80,
                        "fan": {"style": "Cluster", "argument": 4}}},
        ],
        "attendu": "Chan 1 Thru 12 At 50 Thru 80 Fan {Cluster} 4 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan de temps discrets",
        # [1][Thru][5][Time][6][Thru][1][0][Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "temps", "de": 6, "a": 10}},
        ],
        "attendu": "Chan 1 Thru 5 Time 6 Thru 10 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan de temps sur une plage de cues",
        # [Cue][1][Thru][5][Time][6][Thru][1][0][Enter]
        "ir": [
            {"selection": {"objet": "Cue", "de": 1, "a": 5},
             "action": {"type": "temps", "de": 6, "a": 10}},
        ],
        "attendu": "Cue 1 Thru 5 Time 6 Thru 10 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan de temps sur les parts d'une cue",
        # [Cue][1][Part][1][Thru][3][Time][6][Thru][8][Enter]
        "ir": [
            {"selection": {"objet": "Cue", "numero": 1, "part": [1, 3]},
             "action": {"type": "temps", "de": 6, "a": 8}},
        ],
        "attendu": "Cue 1 Part 1 Thru 3 Time 6 Thru 8 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan de références, 3 palettes (reste référencé)",
        # [1][Thru][5][Int Palette][1][Thru][3][Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "palette_intensite", "de": 1, "a": 3}},
        ],
        "attendu": "Chan 1 Thru 5 Int Palette 1 Thru 3 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §8 — fan de références, 2 palettes (casse la référence)",
        # [1][Thru][5][Int Palette][1][Thru][2][Enter] → interpolation ABSOLUE
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "palette_intensite", "de": 1, "a": 2}},
        ],
        "attendu": "Chan 1 Thru 5 Int Palette 1 Thru 2 Enter",
        # syntaxe correcte, intention trahie : le générateur doit le dire
        "avertissements": 1,
    },
    {
        "nom": "{Mirror} du manuel remplacé par {Mirror Out} explicite",
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "intensite", "de": 10, "a": 30,
                        "fan": {"style": "Mirror"}}},
        ],
        "attendu": "Chan 1 Thru 5 At 10 Thru 30 Fan {Mirror Out} Enter",
        "avertissements": 1,      # PLANNING #13
    },
    {
        "nom": "style de Fan jamais observé — {Interleave}",
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "intensite", "de": 10, "a": 30,
                        "fan": {"style": "Interleave"}}},
        ],
        "attendu": "Chan 1 Thru 5 At 10 Thru 30 Fan {Interleave} Enter",
        "avertissements": 1,      # PLANNING #9
    },

    # ---------------------------------------------------------- Cues (§12)
    {
        "nom": "manuel §12 — enregistrement sélectif dans une cue",
        # [1][Thru][5][Record]<Cue>[4][Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 1, "a": 5},
             "action": {"type": "record_cue", "cible": 4}},
        ],
        "attendu": "Chan 1 Thru 5 Record Cue 4 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §12 — Record Only depuis un groupe",
        # [Group][2][Record Only][Cue][5][Enter]
        "ir": [
            {"selection": {"objet": "Group", "numero": 2},
             "action": {"type": "record_only_cue", "cible": 5}},
        ],
        "attendu": "Group 2 Record Only Cue 5 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §12 — Q Only, dont le sens dépend du mode console",
        # [Record]<Cue>[5][Q Only][Enter]
        "ir": [
            {"action": {"type": "record_cue", "cible": 5},
             "modificateurs": ["Q Only"]},
        ],
        "attendu": "Record Cue 5 Q Only Enter",
        "avertissements": 1,
    },
    {
        "nom": "manuel §12 — lien et boucle sur une cue",
        # [Cue][2]{Link/Loop}<Cue>[1]{Link/Loop}[3]
        "ir": [
            {"selection": {"objet": "Cue", "numero": 2},
             "action": {"type": "cue_link", "cible": 1, "iterations": 3}},
        ],
        "attendu": "Cue 2 Link/Loop 1 Link/Loop 3 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §16 — Go To Cue avec modificateur, Time en dernier",
        # [Go to Cue][5]{Minus Links}[Time][Enter]
        "ir": [
            {"action": {"type": "go_to_cue", "cible": 5, "temps": {}},
             "modificateurs": ["MinusLinks"]},
        ],
        "attendu": "Go To Cue 5 MinusLinks Time Enter",
        "avertissements": 0,
    },

    # --------------------------------------------------- Submasters (§20)
    {
        "nom": "manuel §20 — enregistrement sélectif dans un submaster",
        # [6][Thru][1][0][Record][Sub][3][Enter]
        "ir": [
            {"selection": {"objet": "Chan", "de": 6, "a": 10},
             "action": {"type": "record_sub", "cible": 3}},
        ],
        "attendu": "Chan 6 Thru 10 Record Sub 3 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §20 — timing de bump : montée / dwell / descente",
        # [Sub][8][Time][3][Time][4][Time][3][Enter]
        "ir": [
            {"selection": {"objet": "Sub", "numero": 8},
             "action": {"type": "temps_bump_sub", "montee": 3, "dwell": 4,
                        "descente": 3}},
        ],
        "attendu": "Sub 8 Time 3 Time 4 Time 3 Enter",
        "avertissements": 0,
    },
    {
        "nom": "manuel §20 — libellé de submaster",
        # [Sub][6][Label][xxxx][Enter]
        "ir": [
            {"selection": {"objet": "Sub", "numero": 6},
             "action": {"type": "label", "texte": "Cyclo"}},
        ],
        "attendu": "Sub 6 Label Cyclo Enter",
        "avertissements": 0,
    },
    {
        "nom": "`At` sur un Sub — refusé par le modèle (Assert n'a pas de mot-clé)",
        "ir": [
            {"selection": {"objet": "Sub", "numero": 4},
             "action": {"type": "intensite", "valeur": 50}},
        ],
        "attendu": "Sub 4 At 50 Enter",
        "avertissements": 1,
    },
]

CAS_MACRO = [
    {
        "nom": "manuel §24 — macro 1 : Go To Cue Out en 0 s",
        # [Learn][1][Enter][Go To Cue][Out][Time][0][Enter][Learn]
        "appel": dict(numero=1, contenu=[
            {"action": {"type": "go_to_cue", "mot": "Out",
                        "temps": {"valeur": 0}}},
        ]),
        "attendu": ("Learn 1 Enter\n"
                    "Go To Cue Out Time 0 Enter\n"
                    "Learn"),
        "avertissements": 1,      # PLANNING #14
    },
    {
        "nom": "corpus #026 — bump de submaster en macro",
        "appel": dict(numero=4, contenu=[
            {"action": {"type": "sub_bump_bas", "numero": 5}},
            {"action": {"type": "sub_bump_haut", "numero": 5}},
        ]),
        "attendu": ("Learn 4 Enter\n"
                    "SubDown 5 Enter\n"
                    "SubUp 5 Enter\n"
                    "Learn"),
        # deux fois la confiance B de la syntaxe, une fois la survie ASCII
        "avertissements": 3,
    },
    {
        "nom": "chaînage macro-dans-macro mal placé (doit être en fin)",
        "appel": dict(numero=3, voie="editeur", contenu=[
            {"action": {"type": "appel_macro", "numero": 5}},
            {"selection": {"objet": "Chan", "numero": 1},
             "action": {"type": "intensite", "valeur": 50}},
        ]),
        "attendu": ("Macro 3 Enter\n"
                    "{Edit}\n"
                    "Macro 5 Enter\n"
                    "Chan 1 At 50 Enter\n"
                    "Select"),
        "avertissements": 2,      # PLANNING #2 + position en fin de contenu
    },
    {
        "nom": "chaînage tenté en mode Learn — [Macro] n'y est pas enregistrable",
        "appel": dict(numero=3, contenu=[
            {"selection": {"objet": "Chan", "numero": 1},
             "action": {"type": "intensite", "valeur": 50}},
            {"action": {"type": "appel_macro", "numero": 5}},
        ]),
        "attendu": ("Learn 3 Enter\n"
                    "Chan 1 At 50 Enter\n"
                    "Macro 5 Enter\n"
                    "Learn"),
        # PLANNING #2 + la voie Learn ne peut pas produire ce contenu
        "avertissements": 2,
    },
    {
        "nom": "boucle infinie + attente entière",
        "appel": dict(numero=9, contenu=[
            {"controle": "Loop Begin", "argument": 0},
            {"selection": {"objet": "Chan", "numero": 1},
             "action": {"type": "intensite", "valeur": 100}},
            {"controle": "Wait", "argument": 2},
            {"controle": "Loop End"},
        ]),
        "attendu": ("Learn 9 Enter\n"
                    "{Loop Begin} 0\n"
                    "Chan 1 At 100 Enter\n"
                    "{Wait} 2\n"
                    "{Loop End}\n"
                    "Learn"),
        "avertissements": 1,      # boucle infinie
    },
    {
        "nom": "{Wait} avec une durée décimale — la console exige un entier",
        "appel": dict(numero=10, contenu=[
            {"controle": "Wait", "argument": 1.5},
        ]),
        "attendu": ("Learn 10 Enter\n"
                    "{Wait}\n"
                    "Learn"),
        "avertissements": 1,
    },
    {
        "nom": "mode Background — le projet impose Foreground par défaut",
        "appel": dict(numero=11, mode="Background", contenu=[
            {"selection": {"objet": "Chan", "numero": 1},
             "action": {"type": "intensite", "valeur": 100}},
        ]),
        "attendu": ("Learn 11 Enter\n"
                    "Chan 1 At 100 Enter\n"
                    "Learn"),
        "avertissements": 1,
    },
]


def controler(nom: str, resultat, attendu: str, nb_avert: int) -> bool:
    if resultat.commande != attendu:
        print(f"ÉCHEC — {nom}")
        print(f"  attendu : {attendu!r}")
        print(f"  obtenu  : {resultat.commande!r}")
        return False
    if len(resultat.avertissements) != nb_avert:
        print(f"ÉCHEC — {nom} : {nb_avert} avertissement(s) attendu(s), "
              f"{len(resultat.avertissements)} obtenu(s)")
        for a in resultat.avertissements:
            print(f"    - {a}")
        return False
    print(f"OK — {nom}")
    return True


def main() -> int:
    g = Generateur()
    total = len(CAS) + len(CAS_MACRO)
    reussis = 0

    for cas in CAS:
        if controler(cas["nom"], g.rendre(cas["ir"]),
                     cas["attendu"], cas["avertissements"]):
            reussis += 1

    for cas in CAS_MACRO:
        if controler(cas["nom"], g.rendre_macro(**cas["appel"]),
                     cas["attendu"], cas["avertissements"]):
            reussis += 1

    print(f"\n{reussis}/{total} cas conformes.")
    return 1 if reussis != total else 0


if __name__ == "__main__":
    sys.exit(main())

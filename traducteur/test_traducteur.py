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
    {
        # Trouvé le 2026-08-07 en testant l'app avec une phrase réelle, pas
        # écrite pour le traducteur : « gel »/« gélatine » déclenchaient déjà
        # l'intention (mots du lexique), mais le numéro qui suivait n'était
        # jamais lu — seul le mot-clé nuancier « lee » l'était. La sélection
        # ayant déjà consommé ses propres nombres, un numéro resté libre à ce
        # stade ne peut plus désigner que le gel.
        "nom": "numéro de gel après « gel » plutôt que « lee »",
        "phrase": "groupe 1 a 5 en gel 205",
        "statut": "compris",
        "rendu": "Group 1 Thru 5 Color 3/205 Enter",
    },
    {
        "nom": "numéro de gel après « gélatine »",
        "phrase": "circuits 10 a 20 en gelatine 195",
        "statut": "compris",
        "rendu": "Chan 10 Thru 20 Color 3/195 Enter",
    },
    {
        # La limite délibérée du correctif ci-dessus : un numéro SANS aucun
        # mot de la famille couleur (lee/gel/gelatine/couleur/color) ne
        # déclenche même pas l'intention — trop ambigu pour être deviné sans
        # aucun repère dans la phrase. Refus assumé, pas un oubli.
        "nom": "numéro de gel sans aucun mot-clé — refus assumé",
        "phrase": "groupe 1 a 5 en 205",
        "statut": "incompris",
    },

    # ---------------------------------------- hypothèses (nuancier supposé)
    # Décidé avec l'utilisateur le 2026-08-07 : plutôt que de choisir Lee en
    # silence (une note perdue dans le texte) ou de bloquer par une question
    # (Lee est la seule vraie réponse possible aujourd'hui), le traducteur
    # part quand même, mais marque le champ comme une HYPOTHÈSE — code
    # couleur orange côté UI, corrigeable sans tout retaper.
    {
        "nom": "couleur nommée sans nuancier — hypothèse posée, pas de question",
        "phrase": "groupe 5 en bleu",
        "statut": "compris",
        "rendu": "Group 5 Color 3/120 Enter",
        "hypotheses": ["nuancier"],
    },
    {
        "nom": "numéro de gel via « gel » — hypothèse posée sur le nuancier",
        "phrase": "groupe 1 a 5 en gel 205",
        "statut": "compris",
        "rendu": "Group 1 Thru 5 Color 3/205 Enter",
        "hypotheses": ["nuancier"],
    },
    {
        "nom": "nuancier explicite « lee » — aucune hypothèse, confirmé par la phrase",
        "phrase": "circuits 1 à 5 en lee 195",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/195 Enter",
        "hypotheses": [],
    },
    {
        "nom": "hypothèse confirmée via reponses — plus d'hypothèse au deuxième appel",
        "phrase": "groupe 5 en bleu",
        "reponses": {"nuancier": "lee"},
        "statut": "compris",
        "rendu": "Group 5 Color 3/120 Enter",
        "hypotheses": [],
    },
    {
        # Étape 3bis de PIPELINE_TRADUCTION.md : jamais improviser un
        # fabricant hors corpus. Rosco n'est sourcé nulle part dans le
        # dépôt — le dire plutôt que de deviner une correspondance.
        "nom": "correction vers un nuancier non sourcé — refus explicite, pas d'invention",
        "phrase": "groupe 5 en bleu",
        "reponses": {"nuancier": {"cle": "autre", "valeur": "rosco"}},
        "statut": "incompris",
    },
    {
        "nom": "palette couleur sans nuancier — hypothèse posée (pas de blocage)",
        "phrase": "créer la palette de couleur 1 en rouge",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/106 Enter\nChan 1 Thru 5 Record Color Palette 1 Label Rouge Enter",
        "reponses": {"portee_enregistrement": {"cle": "selection", "valeur": "1 a 5"}},
        "hypotheses": ["nuancier"],
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
    {
        # Bug documenté dans PLANNING.md (trouvé le 2026-08-09 en construisant
        # `_parquer`) : avec un seul objet et un seul « à », `_plage` lisait
        # « 4 à 50 » comme la plage de circuits 4 à 50, laissant `_niveau` sans
        # rien à trouver — `incompris` silencieux. Corrigé dans `_plage` :
        # un nombre suivi immédiatement d'un marqueur de niveau (`%` ici)
        # n'est plus jamais lu comme la borne haute d'une plage.
        "nom": "intensité sur un seul circuit — un seul « à », plus d'ambiguïté (bug _plage corrigé)",
        "phrase": "circuit 4 à 50 %",
        "statut": "compris",
        "rendu": "Chan 4 At 50 Enter",
    },
    {
        # Même correctif, avec le zéro de tête (résolu ex-#29) en plus —
        # les deux pièges ne doivent pas interagir mal l'un avec l'autre.
        "nom": "intensité sur un seul circuit, sous 10 % — zéro de tête conservé",
        "phrase": "circuit 4 à 5 %",
        "statut": "compris",
        "rendu": "Chan 4 At 05 Enter",
    },
    {
        # Forme déjà valide avant le correctif (« intensité » remplace le
        # second « à ») — non-régression : doit continuer à marcher à
        # l'identique une fois `_plage` modifiée.
        "nom": "intensité sur une plage — marqueur « intensité » au lieu d'un second « à »",
        "phrase": "circuits 1 à 5 intensité 50",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 50 Enter",
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
    {
        # Bug trouvé en construisant `interpreter_flou` (moteur flou) :
        # `_couleurs_de` ne consultait jamais `reponses`, donc répondre à la
        # question `couleur:ambre` la reposait indéfiniment au lieu de
        # reprendre où le traducteur s'était arrêté — contrat pourtant
        # documenté par `traduire()`. Corrigé.
        "nom": "couleur ambiguë — la réponse est bien consommée, pas reposée",
        "phrase": "groupe 5 en lee ambre",
        "reponses": {"couleur:ambre": "102"},
        "statut": "compris",
        "rendu": "Group 5 Color 3/102 Enter",
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
        # PRÉMISSE CORRIGÉE le 2026-09-09. Ce cas exigeait `incompris` : sans
        # teinte nommée, `creer_palettes_couleur` n'avait rien à mettre dans
        # les palettes. Mais la phrase est parfaitement claire — elle demande
        # de CRÉER des palettes vides, ce qui est la première étape du flux
        # que les praticiens emploient (créer la plage, puis la remplir en
        # Blind). Refuser une demande limpide enseignait une limite fausse,
        # exactement le défaut que ce dépôt combat ailleurs.
        "nom": "créer des palettes vides — une demande complète, pas une lacune",
        "phrase": "créer les palettes de couleur 1 à 6",
        "statut": "compris",
        "rendu": "Color Palette 1 Thru Thru 6 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # `Thru Thru` CRÉE, `Thru` ne fait que désigner ce qui existe : le
        # manuel §17 l. 149 montre qu'un simple `Thru` ne créerait que les
        # deux bornes. Un verbe de création dans la phrase est donc la seule
        # chose qui autorise le double `Thru`.
        "nom": "création d'une plage de groupes",
        "phrase": "cree les groupes 1 a 20",
        "statut": "compris",
        "rendu": "Group 1 Thru Thru 20 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "création sans famille nommée — question, pas supposition",
        "phrase": "cree les palettes 100 a 150",
        "statut": "a_preciser",
    },

    # -------------------------------------------------------- submasters
    {
        # Reprend l'exemple chiffré du manuel §20 recopié dans
        # test_generateur.py — même macro par deux voies indépendantes.
        "nom": "enregistrement sélectif dans un submaster",
        "phrase": "enregistrer les circuits 6 à 10 dans le sub 3",
        "statut": "compris",
        "rendu": "Chan 6 Thru 10 Record Sub 3 Enter",
    },
    {
        "nom": "enregistrement dans un submaster — groupe plutôt que circuits",
        "phrase": "enregistrer le groupe 2 dans le sub 7",
        "statut": "compris",
        "rendu": "Group 2 Record Sub 7 Enter",
    },
    {
        "nom": "enregistrer sub sans sélection — refus assumé",
        "phrase": "enregistrer dans le sub 4",
        "statut": "incompris",
    },
    {
        # Le cas qui a motivé `objets_cible` plutôt que d'ajouter Sub à
        # `objets` : le modèle interdit `Sub + intensite` (confiance S,
        # « le pilotage de niveau d'un sub passe par le fader ou les bumps,
        # pas par At »). Si « sub » était un objet générique, cette phrase
        # aurait pu passer par `regler_intensite` et produire une commande
        # qu'on sait déjà fausse. Elle ne doit reconnaître AUCUNE intention.
        "nom": "sub + pourcentage — jamais routé vers l'intensité (Sub+At invalide, confiance S)",
        "phrase": "sub 3 à 50 %",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- effets
    {
        # Reprend l'exemple chiffré du manuel §18 recopié dans
        # test_generateur.py.
        "nom": "appliquer un effet à une plage de circuits",
        "phrase": "lance l'effet 1 sur les circuits 1 à 10",
        "statut": "compris",
        "rendu": "Chan 1 Thru 10 Effect 1 Enter",
    },
    {
        "nom": "appliquer un effet à un groupe",
        "phrase": "applique l'effet 7 au groupe 2",
        "statut": "compris",
        "rendu": "Group 2 Effect 7 Enter",
    },
    {
        "nom": "appliquer un effet sans sélection — refus assumé",
        "phrase": "lance l'effet 3",
        "statut": "incompris",
    },
    {
        "nom": "arrêter un effet précis",
        "phrase": "arrête l'effet 3",
        "statut": "compris",
        "rendu": "Stop Effect 3 Enter",
    },
    {
        # Reprend le double appui du manuel §18 recopié dans
        # test_generateur.py — ici la forme simple, sans double appui : `Stop
        # Effect Enter` sans argument arrête tout ce qui tourne.
        "nom": "arrêter tous les effets",
        "phrase": "arrête tous les effets",
        "statut": "compris",
        "rendu": "Stop Effect Enter",
    },
    {
        "nom": "arrêter un effet sans numéro ni « tous » — refus assumé",
        "phrase": "arrête l'effet",
        "statut": "incompris",
    },

    # ------------------------------------------------ bump de submaster
    {
        # Reprend le corpus #026 recopié dans test_generateur.py (bump de
        # submaster en macro) — ici en ligne de commande directe.
        "nom": "bump haut d'un submaster",
        "phrase": "bump haut le sub 5",
        "statut": "compris",
        "rendu": "SubUp 5 Enter",
    },
    {
        "nom": "bump bas d'un submaster",
        "phrase": "bump bas sub 12",
        "statut": "compris",
        "rendu": "SubDown 12 Enter",
    },
    {
        # Aucune source du dépôt ne dit ce que « haut »/« bas » font
        # fonctionnellement — sans direction dans la phrase, c'est une
        # question, jamais un choix par défaut.
        "nom": "bump sans direction — la question est posée",
        "phrase": "bump le sub 5",
        "statut": "a_preciser",
        "questions": ["bump_direction"],
        "options": ["haut", "bas"],
    },
    {
        "nom": "bump sans direction, puis réponse « bas »",
        "phrase": "bump le sub 5",
        "reponses": {"bump_direction": "bas"},
        "statut": "compris",
        "rendu": "SubDown 5 Enter",
    },

    # ------------------------------------------------------------ presets
    {
        # Reprend l'exemple chiffré du manuel §11 recopié dans
        # test_generateur.py.
        "nom": "enregistrement d'un preset",
        "phrase": "enregistrer les circuits 1 à 5 dans le preset 2",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Record Preset 2 Enter",
    },
    {
        "nom": "enregistrer preset sans sélection — refus assumé",
        "phrase": "enregistrer dans le preset 4",
        "statut": "incompris",
    },
    {
        # Même raison que pour Sub : Preset vit dans objets_cible, jamais
        # dans objets — un preset ne peut structurellement pas devenir la
        # cible de colorer_selection.
        "nom": "preset + couleur — jamais routé vers colorer_selection",
        "phrase": "preset 3 en rouge",
        "statut": "incompris",
    },
    {
        "nom": "rappel d'un preset sur une plage de circuits",
        "phrase": "rappelle le preset 2 sur les circuits 1 à 5",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Preset 2 Enter",
    },
    {
        "nom": "rappel d'un preset — verbe « appliquer »",
        "phrase": "applique le preset 9 aux circuits 10 à 20",
        "statut": "compris",
        "rendu": "Chan 10 Thru 20 Preset 9 Enter",
    },
    {
        "nom": "rappeler preset sans sélection — refus assumé",
        "phrase": "rappelle le preset 2",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- macros
    {
        "nom": "lancer une macro par numéro",
        "phrase": "lance la macro 5",
        "statut": "compris",
        "rendu": "Macro 5 Enter",
    },
    {
        "nom": "lancer une macro — verbe « exécuter »",
        "phrase": "execute la macro 12",
        "statut": "compris",
        "rendu": "Macro 12 Enter",
    },
    {
        "nom": "lancer une macro sans numéro — refus assumé",
        "phrase": "lance la macro",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- Query
    {
        # Reprend l'exemple chiffré du manuel §15 recopié dans
        # test_generateur.py (sans l'action `At 50` associée).
        "nom": "Query — sélection positive sur une palette couleur",
        "phrase": "sélectionne ce qui est dans la palette couleur 5",
        "statut": "compris",
        "rendu": "Query {Is In} Color Palette 5 Enter",
    },
    {
        # La seule négation du langage Eos (manuel §15) — vérifie que le
        # français négatif (« n'est pas ») est bien détecté.
        "nom": "Query — négation sur une palette couleur",
        "phrase": "sélectionne ce qui n'est pas dans la palette couleur 5",
        "statut": "compris",
        "rendu": "Query {Isn't In} Color Palette 5 Enter",
    },
    {
        "nom": "Query — cible preset",
        "phrase": "sélectionne ce qui est dans le preset 3",
        "statut": "compris",
        "rendu": "Query {Is In} Preset 3 Enter",
    },
    {
        "nom": "Query — négation sur un preset",
        "phrase": "sélectionne ce qui n'est jamais dans le preset 3",
        "statut": "compris",
        "rendu": "Query {Isn't In} Preset 3 Enter",
    },
    {
        "nom": "Query — cible cue",
        "phrase": "sélectionne ce qui est dans la cue 4",
        "statut": "compris",
        "rendu": "Query {Is In} Cue 4 Enter",
    },
    {
        # Périmètre assumé : seule la palette couleur est modélisée ailleurs
        # dans ce traducteur. Un « palette » nu, sans le mot « couleur »,
        # reste incompris plutôt que de deviner la famille (Int/Focus/Beam).
        "nom": "Query — palette sans « couleur » — refus assumé",
        "phrase": "sélectionne ce qui est dans la palette 5",
        "statut": "incompris",
    },
    {
        # Group et Sub comme cibles de Query sont hors périmètre — voir la
        # note de `selectionner_query` dans lexique.yaml. La phrase ne
        # déclenche même pas l'intention (mot-clé absent des déclencheurs).
        "nom": "Query — groupe hors périmètre — refus assumé",
        "phrase": "sélectionne ce qui est dans le groupe 2",
        "statut": "incompris",
    },
    {
        "nom": "Query — sans cible reconnue — refus assumé",
        "phrase": "sélectionne ce qui est dans le truc",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- Mark
    {
        # Reprend l'exemple chiffré du manuel §9 recopié dans
        # test_generateur.py — le drapeau M sur la cue elle-même.
        "nom": "marquer une cue — pose le drapeau M",
        "phrase": "marque la cue 10",
        "statut": "compris",
        "rendu": "Cue 10 Mark Enter",
    },
    {
        # Deuxième usage de la même touche : la cue SOURCE où sont stockés
        # les mouvements NP, désignée par ses channels.
        "nom": "marquer des channels — cue source des mouvements NP",
        "phrase": "marque les circuits 1 à 10",
        "statut": "compris",
        "rendu": "Chan 1 Thru 10 Mark Enter",
    },
    {
        "nom": "marquer un groupe",
        "phrase": "marque le groupe 2",
        "statut": "compris",
        "rendu": "Group 2 Mark Enter",
    },
    {
        "nom": "marquer sans cible — refus assumé",
        "phrase": "marque",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- Park
    {
        # Reprend l'exemple chiffré du manuel §19 recopié dans
        # test_generateur.py, forme absolue et déterministe.
        "nom": "parquer un circuit à un niveau explicite",
        "phrase": "parque le circuit 2 à 50 %",
        "statut": "compris",
        "rendu": "Chan 2 At 50 Park Enter",
    },
    {
        # Le zéro de tête (résolu ex-#29) s'applique aussi au parquage.
        "nom": "parquer — zéro de tête sous 10 %",
        "phrase": "parque le circuit 2 à 5 %",
        "statut": "compris",
        "rendu": "Chan 2 At 05 Park Enter",
    },
    {
        "nom": "parquer un groupe",
        "phrase": "parque le groupe 7 à 100 %",
        "statut": "compris",
        "rendu": "Group 7 At 100 Park Enter",
    },
    {
        # Sans marqueur de niveau, « circuit 3 à 45 » ne doit jamais être lu
        # comme la plage 3 à 45 : refus assumé plutôt qu'une mésinterprétation.
        "nom": "parquer sans marqueur de niveau — refus assumé",
        "phrase": "parque le circuit 3 à 45",
        "statut": "incompris",
    },
    {
        "nom": "parquer sans niveau du tout — refus assumé (bascule non générée)",
        "phrase": "parque le circuit 3",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- Assert
    {
        # Reprend l'exemple chiffré du manuel §14 recopié dans
        # test_generateur.py (sans la notation de cue list `x/y`).
        "nom": "assert sur une cue",
        "phrase": "assert la cue 5",
        "statut": "compris",
        "rendu": "Cue 5 Assert Enter",
    },
    {
        "nom": "assert sur un groupe",
        "phrase": "assert le groupe 6",
        "statut": "compris",
        "rendu": "Group 6 Assert Enter",
    },
    {
        "nom": "assert sur des circuits — verbe « asserter »",
        "phrase": "asserter les circuits 1 à 5",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Assert Enter",
    },
    {
        # Sub vit dans objets_cible, jamais dans objets — même garde-fou
        # structurel que « sub 3 à 50 % » pour l'intensité.
        "nom": "assert sur un submaster — jamais déclenché (Sub hors objets)",
        "phrase": "assert le sub 3",
        "statut": "incompris",
    },
    {
        "nom": "assert sans cible — refus assumé",
        "phrase": "assert",
        "statut": "incompris",
    },

    # -------------------------------------------------------------- Filtres
    {
        # Reprend l'exemple chiffré du manuel §13 recopié dans
        # test_generateur.py — seul le geste d'effacement est couvert.
        "nom": "effacer les filtres",
        "phrase": "efface les filtres",
        "statut": "compris",
        "rendu": "Clear Filters Enter",
    },
    {
        "nom": "effacer les filtres — verbe « vider »",
        "phrase": "vide les filtres",
        "statut": "compris",
        "rendu": "Clear Filters Enter",
    },

    # ------------------------------------------------------------ Snapshots
    {
        # Reprend l'exemple chiffré du manuel §23 recopié dans
        # test_generateur.py.
        "nom": "enregistrer un snapshot",
        "phrase": "enregistre le snapshot 1",
        "statut": "compris",
        "rendu": "Record Snapshot 1 Enter",
    },
    {
        "nom": "enregistrer un snapshot sans numéro — refus assumé",
        "phrase": "enregistre le snapshot",
        "statut": "incompris",
    },
    {
        "nom": "rappeler un snapshot",
        "phrase": "rappelle le snapshot 5",
        "statut": "compris",
        "rendu": "Snapshot 5 Enter",
    },

    # -------------------------------------------------------------- Courbes
    {
        # Reprend l'exemple chiffré du manuel §22 recopié dans
        # test_generateur.py — la courbe précède la cue dans la phrase,
        # l'inverse de l'ordre attendu par un extracteur positionnel.
        "nom": "appliquer une courbe à une cue",
        "phrase": "applique la courbe 4 à la cue 5",
        "statut": "compris",
        "rendu": "Cue 5 Curve 4 Enter",
    },
    {
        "nom": "appliquer une courbe — ordre inversé dans la phrase",
        "phrase": "applique à la cue 5 la courbe 4",
        "statut": "compris",
        "rendu": "Cue 5 Curve 4 Enter",
    },
    {
        "nom": "appliquer une courbe sans numéro de cue — refus assumé",
        "phrase": "applique la courbe 4",
        "statut": "incompris",
    },
    {
        "nom": "retirer la courbe d'une cue",
        "phrase": "retire la courbe de la cue 5",
        "statut": "compris",
        "rendu": "Cue 5 Curve At Enter",
    },

    # ------------------------------------------------- Contrôle partitionné
    {
        "nom": "sélectionner une partition préprogrammée",
        "phrase": "sélectionne la partition 902",
        "statut": "compris",
        "rendu": "Partition 902 Enter",
    },
    {
        "nom": "sélectionner une partition — autre verbe sourcé (utiliser)",
        "phrase": "utilise la partition 5",
        "statut": "compris",
        "rendu": "Partition 5 Enter",
    },
    {
        "nom": "sélectionner une partition sans numéro — refus assumé",
        "phrase": "sélectionne la partition",
        "statut": "incompris",
    },
    {
        "nom": "supprimer une partition",
        "phrase": "supprime la partition 5",
        "statut": "compris",
        "rendu": "Delete Partition 5 Enter",
    },
    {
        # Le générateur porte l'avertissement (refuse sur les 4 partitions
        # préprogrammées) — le traducteur ne le répète pas, mais la
        # traduction doit rester `compris` (la console fait autorité sur le
        # refus, pas le traducteur, voir APP.md).
        "nom": "supprimer une partition préprogrammée — traduit quand même, le générateur avertit",
        "phrase": "supprime la partition 902",
        "statut": "compris",
        "rendu": "Delete Partition 902 Enter",
    },

    # ------------------------------------------------------------------
    # Trois pertes silencieuses trouvées en test réel le 2026-08-28, toutes
    # de la même famille : la macro avait l'air complète et ne l'était pas.
    # Voir REGLES_POUR_UI.md règle 4 — « les erreurs les plus graves ne
    # lèvent aucune erreur ».
    # ------------------------------------------------------------------
    {
        # L'app annonçait ne pas reconnaître « jaune » — une couleur de son
        # propre lexique, traduite sans peine dans la phrase d'avant. Elle
        # enseignait des limites fausses. « jaune » est un mot de créneau
        # connu (donc `ignores`) ; « clignotants » et « blanc » sont
        # réellement absents du lexique, et restent donc signalés. « effet »
        # est un déclencheur d'intention, ni l'un ni l'autre.
        "nom": "mots connus jamais annoncés comme inconnus, même quand l'intention échoue",
        "phrase": "Bien aintenant je veux un effet jaune clignotants en blanc",
        "statut": "incompris",
        "non_reconnus": ["bien", "aintenant", "je", "veux", "clignotants", "blanc"],
        "ignores": ["jaune"],
    },
    {
        # Le mot tombé était bien calculé, mais l'UI ne l'affichait que sur
        # un `incompris` : sur un `compris`, il disparaissait. La garde
        # globale de `main()` couvre ce cas, l'assertion explicite le nomme.
        "nom": "un mot inconnu sur une phrase par ailleurs comprise reste signalé",
        "phrase": "circuits 1 a 5 en jaune clignotant",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/101 Enter",
        "non_reconnus": ["clignotant"],
        "ignores": [],
    },
    {
        # Le pire des trois : les deux couleurs étaient consommées, donc
        # invisibles pour `non_reconnus` COMME pour `ignores`. Seule la
        # première était appliquée, sans une note.
        "nom": "deux couleurs pour une seule commande — une question, jamais la première d'office",
        "phrase": "circuits 1 a 5 en jaune bleu",
        "statut": "a_preciser",
        "questions": ["couleur_unique"],
        "options": ["101", "120"],
    },
    {
        "nom": "deux couleurs — la réponse tranche, et c'est bien celle-là qui sort",
        "phrase": "circuits 1 a 5 en jaune bleu",
        "reponses": {"couleur_unique": "120"},
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/120 Enter",
    },
    {
        "nom": "une seule couleur — aucune question ajoutée par la garde multi-couleurs",
        "phrase": "circuits 1 a 5 en jaune",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/101 Enter",
        "non_reconnus": [],
        "ignores": [],
    },
    # ------------------------------------------------------------------
    # Tranche « quotidien » (2026-09-03) — les commandes tapées des dizaines
    # de fois par jour. Le modèle les documentait toutes en confiance A et le
    # générateur les rendait déjà : le trou était entièrement dans le lexique.
    # ------------------------------------------------------------------
    {
        "nom": "plein feu — forme « à fond »",
        "phrase": "circuits 1 a 5 a fond",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Full Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "plein feu — la locution « plein feu » ne perd pas « feu »",
        "phrase": "plein feu sur le groupe 3",
        "statut": "compris",
        "rendu": "Group 3 Full Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # `Out` s'auto-termine (manuel §00) : pas d'`Enter`, et c'est le
        # générateur qui le sait — le traducteur n'en décide rien.
        "nom": "hors scène — Out s'auto-termine, donc sans Enter",
        "phrase": "eteins les circuits 1 a 5",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Out",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "sneak sur une sélection",
        "phrase": "sneak les circuits 1 a 5",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Sneak Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # `Sneak Time 3` : SANS destination, le mot-clé `Time` est obligatoire.
        "nom": "sneak temporisé — la forme sans destination garde `Time`",
        "phrase": "sneak les circuits 1 a 5 en 3 secondes",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Sneak Time 3 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # `At 50 Sneak 8` : AVEC destination, `Time` disparaît et le nombre se
        # colle à `Sneak` (manuel §6, « sneaks channel 5 to 50% in 8 seconds »).
        # Les deux formes ne se déduisent pas l'une de l'autre.
        "nom": "niveau temporisé — la forme avec destination perd `Time`",
        "phrase": "circuits 1 a 5 a 50 % en 8 secondes",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 50 Sneak 8 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "durée en postfixe — « 20 s » comme « 50 % »",
        "phrase": "circuits 1 a 5 a 100 % en 20 s",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 100 Sneak 20 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Sans marqueur de durée, un nombre reste un numéro : le 8 de
        # « circuits 1 à 8 » ne doit jamais devenir un temps.
        "nom": "aucune durée sans marqueur — le nombre reste une sélection",
        "phrase": "circuits 1 a 8 a 50 %",
        "statut": "compris",
        "rendu": "Chan 1 Thru 8 At 50 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "go to cue temporisé",
        "phrase": "va a la cue suivante en 3 secondes",
        "statut": "compris",
        "rendu": "Go To Cue Next Time 3 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Le piège du manuel §16 : `Go To Cue 8 Time Enter` emploie les temps
        # STOCKÉS dans la cue. Ce qui les ignore, c'est `Time 0`. La feuille
        # communautaire « Handy Macros » écrit `[time] [enter]` en annonçant
        # « ignores timing » — sa macro fait l'inverse de sa description.
        "nom": "« sans les temps » donne `Time 0`, jamais un `Time` nu",
        "phrase": "va a la cue suivante sans les temps",
        "statut": "compris",
        "rendu": "Go To Cue Next Time 0 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "revue circuit par circuit — une seule ligne, un seul Enter",
        "phrase": "verifie les circuits 1 a 20 a 75 %",
        "statut": "compris",
        "rendu": "Chan 1 Thru 20 At 75 Check Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Sans niveau, `Check` n'a rien à amener nulle part : refus plutôt
        # qu'un niveau par défaut inventé.
        "nom": "revue sans niveau — refus assumé",
        "phrase": "verifie les circuits 1 a 20",
        "statut": "incompris",
    },
    {
        # ASSOUPLISSEMENT DU 2026-09-09. Le modèle déclarait déjà
        # `selection_courante` valide pour cette action (confiance A, manuel
        # §15) et le générateur la rendait sans un avertissement : seul le
        # traducteur refusait de la produire.
        "nom": "sélection courante — aucune cible nommée, commande implicite",
        "phrase": "monte a fond",
        "statut": "compris",
        "rendu": "Full Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "sélection courante avec durée",
        "phrase": "monte a fond en 20 secondes",
        "statut": "compris",
        "rendu": "Full Sneak 20 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "sélection courante — niveau sans objet nommé",
        "phrase": "descends a 0 % en 20 secondes",
        "statut": "compris",
        "rendu": "At 0 Sneak 20 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # VERROU 1 — un objet nommé sans numéro reste une phrase INCOMPLÈTE,
        # jamais un ordre implicite. Sans ça, une phrase dont le numéro a été
        # perdu (frappe, dictée) deviendrait un ordre sur une sélection
        # inconnue, sans le moindre signal.
        "nom": "verrou — objet nommé sans numéro : refus, pas de repli",
        "phrase": "les circuits a fond",
        "statut": "incompris",
    },
    {
        # VERROU 2 — une CIBLE (Sub, Preset) bloque aussi le repli, même si
        # elle n'est pas dans `objets`. Régression réelle du 2026-09-09 :
        # « sub 3 à 50 % » rendait `At 50 Enter`, c'est-à-dire un ordre sur
        # des circuits quelconques, alors que le banc a tranché Sub + At
        # invalide en confiance S.
        "nom": "verrou — un mot de cible interdit le repli",
        "phrase": "sub 3 a 50 %",
        "statut": "incompris",
    },
    {
        # VERROU 3 — le plus important. Agir sans cible nommée suppose d'avoir
        # compris TOUTE la phrase. Trouvé au banc de rétro-traduction le jour
        # même : « passe le fondu de couleur à fond » rendait `Full Enter`,
        # envoyant tout le plateau à pleine intensité pour une demande qui ne
        # parlait que de fondu de couleur.
        "nom": "verrou — un mot inconnu interdit le repli",
        "phrase": "passe le fondu de couleur a fond",
        "statut": "incompris",
    },
    {
        # Une durée doit toujours ressortir : produite, ou refusée. `Out` n'a
        # aucune forme temporisée attestée — le refus nomme le chemin qui
        # marche plutôt que de rendre `Out` en avalant les 20 secondes.
        "nom": "durée sur une commande qui n'en accepte pas — refus, jamais silence",
        "phrase": "eteins en 20 secondes",
        "statut": "incompris",
    },
    {
        # Exemple apporté par la communauté le 2026-09-09 : renommer à la
        # volée des cues d'après les palettes dont elles viennent.
        "nom": "copie de libellés palette -> cue",
        "phrase": "copie les libelles des palettes de couleur 1 a 5 vers les cues 3 1",
        "statut": "compris",
        "rendu": "Color Palette 1 Thru 5 Copy To Cue 3/1 {Labels Only} Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "copie de libellés — autre famille, autre mot-clé",
        "phrase": "renomme les cues 3 1 avec les noms des palettes de focus 1 a 8",
        "statut": "compris",
        "rendu": "Focus Palette 1 Thru 8 Copy To Cue 3/1 {Labels Only} Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Aucune famille par défaut : les quatre ont des mot-clés différents
        # et aucune n'est plus probable. Deviner produirait une commande
        # valide visant la mauvaise famille — erreur silencieuse.
        "nom": "famille de palette non nommée — question, pas supposition",
        "phrase": "copie les libelles des palettes 1 a 5 vers les cues 3 1",
        "statut": "a_preciser",
    },
    {
        # Le remède nommé par la communauté au problème du mode Background :
        # poser la sélection DANS la macro plutôt que d'espérer celle de
        # l'opérateur, qui n'est pas celle de l'appareil maître.
        "nom": "Select Manual — poser la sélection au lieu de l'espérer",
        "phrase": "selectionne le manuel",
        "statut": "compris",
        "rendu": "Select Manual Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "Select Manual ≠ Select Active",
        "phrase": "selectionne les circuits actifs",
        "statut": "compris",
        "rendu": "Select Active Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        "nom": "update d'une cue — la cible est toujours explicite",
        "phrase": "mets a jour la cue 4",
        "statut": "compris",
        "rendu": "Update Cue 4 Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Jamais d'`Update` nu : le modèle avertit qu'une cible implicite
        # dépend de préférences persistantes entre sessions.
        "nom": "update sans numéro — refus assumé plutôt qu'une cible devinée",
        "phrase": "mets a jour la cue",
        "statut": "incompris",
    },
    {
        "nom": "Select Last — « dernière » est aussi un alias de cible de cue, sans conflit",
        "phrase": "selectionne la derniere selection",
        "statut": "compris",
        "rendu": "Select Last Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # « circuits » est du remplissage grammatical ici : Select Active ne
        # prend pas de sélection. Le signaler enseignerait une limite fausse.
        "nom": "Select Active — le mot d'objet n'est pas signalé comme perdu",
        "phrase": "selectionne les circuits actifs",
        "statut": "compris",
        "rendu": "Select Active Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # PRÉMISSE CORRIGÉE le 2026-09-17. Ce cas exigeait `incompris` sous
        # prétexte qu'un numéro perdrait toujours de l'information sur
        # `Select Active`. C'était vrai avant l'ajout des trois formes du
        # manuel §6 : une plage devant `Select Active` la FILTRE sur l'actif
        # (l. 1192, `[1] [Thru] [100] [Select Active] [Enter]`) — le numéro
        # n'était pas une perte, c'était une commande légitime que le
        # traducteur ne savait pas encore produire.
        "nom": "Select Active filtré par une plage — une commande, pas une perte",
        "phrase": "selectionne les circuits 1 a 5 actifs",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Select Active Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Le refus tient toujours, mais ailleurs : un numéro SANS plage
        # reconnue (pas de « à ») n'a rien à filtrer.
        "nom": "Select Active — un numéro isolé reste un refus",
        "phrase": "selectionne les circuits actifs 5",
        "statut": "incompris",
    },
    {
        "nom": "Select Active — exclusion, le manuel §6 « [-] Select Active »",
        "phrase": "selectionne les circuits 1 a 20 sauf les actifs",
        "statut": "compris",
        "rendu": "Chan 1 Thru 20 - Select Active Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Sans plage devant, rien à exclure — le manuel dit « all of the
        # channels IN THE LIST » : il n'existe pas de « Select Inactive »
        # qui prendrait tout le plateau d'office.
        "nom": "Select Active — exclusion sans plage, refus assumé",
        "phrase": "selectionne les actifs sauf les circuits",
        "statut": "incompris",
    },
    {
        "nom": "Select Active — double appui, Select NonSub Active",
        "phrase": "selectionne les actifs sauf les subs",
        "statut": "compris",
        "rendu": "Select NonSub Active Enter",
        "non_reconnus": [], "ignores": [],
    },
    {
        # Les six nouvelles intentions sont déclarées en dernier : elles ne
        # doivent voler aucune phrase aux intentions plus spécifiques.
        "nom": "« sélectionne la partition » reste une partition, pas une sélection d'actifs",
        "phrase": "selectionne la partition 902",
        "statut": "compris",
        "rendu": "Partition 902 Enter",
    },
    {
        "nom": "« sélectionne ce qui est dans… » reste une Query",
        "phrase": "selectionne ce qui est dans la palette couleur 5",
        "statut": "compris",
        "rendu": "Query {Is In} Color Palette 5 Enter",
    },
    {
        "nom": "« à 50 % » reste un niveau, pas un plein feu",
        "phrase": "circuits 1 a 5 a 50 %",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 At 50 Enter",
    },

    {
        # Cinquième de la famille, trouvé le 2026-09-03 en reprenant la piste
        # B. « effet » nomme une capacité entière du lexique ; la phrase part
        # pourtant sur `colorer_selection` et rend un jaune fixe. Le mot
        # n'était ni « non reconnu » (l'app le connaît) ni « ignoré » (tous
        # les déclencheurs en étaient exclus) : il disparaissait sans trace.
        "nom": "un déclencheur d'une AUTRE intention que celle retenue est signalé",
        "phrase": "je veux un effet jaune clignotant sur les circuits 1 a 5",
        "statut": "compris",
        "rendu": "Chan 1 Thru 5 Color 3/101 Enter",
        "non_reconnus": ["je", "veux", "clignotant"],
        "ignores": ["effet"],
    },
    {
        # Le pendant : le déclencheur de l'intention RETENUE a fait son
        # travail et ne doit jamais être signalé. C'est ce qui distingue ce
        # raffinement d'un retour aux 51 faux positifs de la première version.
        "nom": "le déclencheur de l'intention retenue n'est jamais signalé",
        "phrase": "lance l'effet 2 sur le groupe 3",
        "statut": "compris",
        "rendu": "Group 3 Effect 2 Enter",
        "non_reconnus": [],
        "ignores": [],
    },
    {
        # Le plus grave des quatre : le bon numéro sur le MAUVAIS objet.
        # « lance » tombe à distance 2 de « lampe » (alias de Chan) et
        # gagnait la place d'objet avant que « groupe » soit seulement
        # examiné — d'où `Chan 3` au lieu de `Group 3`, sans un mot. Voir
        # `Traducteur._objet` : exact d'abord, tolérance en second seulement.
        "nom": "un verbe ne peut plus voler la place d'objet à un vrai nom d'objet",
        "phrase": "lance l'effet 2 sur le groupe 3",
        "statut": "compris",
        "rendu": "Group 3 Effect 2 Enter",
        "ignores": [],
    },
]


# ----------------------------------------------------------------------------
# Correction en langage naturel (`Traducteur.corriger`) — « à la manière d'un
# LLM » : une instruction courte retouche l'IR déjà produite, plutôt que de
# retraduire depuis zéro. Chaque cas part d'une phrase traduite normalement,
# puis applique une instruction de correction.
# ----------------------------------------------------------------------------
CAS_CORRECTION = [
    {
        "nom": "remplacer l'objet de sélection — groupe par circuit",
        "phrase": "groupe 5 en lee 195",
        "instruction": "remplace groupe par circuit",
        "statut": "compris",
        "rendu": "Chan 5 Color 3/195 Enter",
    },
    {
        "nom": "remplacer l'objet de sélection — verbe « change »/« en »",
        "phrase": "circuit 5 en lee 195",
        "instruction": "change circuit en groupe",
        "statut": "compris",
        "rendu": "Group 5 Color 3/195 Enter",
    },
    {
        "nom": "remplacer un numéro déjà présent, sans ambiguïté",
        "phrase": "groupe 5 en lee 195",
        "instruction": "remplace 5 par 12",
        "statut": "compris",
        "rendu": "Group 12 Color 3/195 Enter",
    },
    {
        "nom": "cible de remplacement non prise en charge — sub jamais proposé",
        "phrase": "groupe 5 en lee 195",
        "instruction": "remplace groupe par sub",
        "statut": "incompris",
    },
    {
        "nom": "objet absent de la macro actuelle — refus assumé",
        "phrase": "groupe 5 en lee 195",
        "instruction": "remplace circuit par groupe",
        "statut": "incompris",
    },
    {
        "nom": "numéro absent de la macro — refus assumé",
        "phrase": "groupe 5 en lee 195",
        "instruction": "remplace 99 par 1",
        "statut": "incompris",
    },
    {
        "nom": "numéro ambigu — présent à plusieurs endroits, refus assumé",
        "phrase": "circuit 1 intensite 1",
        "instruction": "remplace 1 par 7",
        "statut": "incompris",
    },
    {
        "nom": "instruction sans « par » ni « en » — refus assumé",
        "phrase": "groupe 5 en lee 195",
        "instruction": "groupe vers circuit",
        "statut": "incompris",
    },
    {
        "nom": "aucune macro à corriger — IR vide",
        "phrase": None,
        "instruction": "remplace groupe par circuit",
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

        if "hypotheses" in cas:
            ok &= controler(f"{cas['nom']} (hypotheses)",
                            [h.champ for h in trad.hypotheses], cas["hypotheses"])

        if "non_reconnus" in cas:
            ok &= controler(f"{cas['nom']} (mots inconnus)",
                            trad.non_reconnus, cas["non_reconnus"])

        if "ignores" in cas:
            ok &= controler(f"{cas['nom']} (mots ignorés)",
                            trad.ignores, cas["ignores"])

        # Un mot non reconnu qui passe inaperçu est une traduction partielle
        # présentée comme complète — pire qu'un refus. Un mot CONNU resté
        # inutilisé l'est tout autant, et se voit encore moins : rien dans la
        # macro ne trahit son absence. Les deux sont donc des échecs de test,
        # à moins que le cas ne les déclare explicitement (auquel dernier cas
        # l'UI a la charge de les afficher — voir `app/prototype.html`).
        for cle, libelle, mots in (("non_reconnus", "non reconnus", trad.non_reconnus),
                                   ("ignores", "ignorés", trad.ignores)):
            if trad.statut == "compris" and mots and cle not in cas:
                print(f"  ÉCHEC — {cas['nom']} (mots {libelle} alors que compris)")
                print(f"    {mots}")
                ok = False

        echecs += not ok

    total = len(CAS)

    echecs_correction = 0
    for cas in CAS_CORRECTION:
        ir_depart = [] if cas["phrase"] is None else t.traduire(cas["phrase"]).ir
        corr = t.corriger(ir_depart, cas["instruction"])
        ok = controler(f"{cas['nom']} (statut correction)", corr.statut, cas["statut"])
        if "rendu" in cas:
            ok &= controler(f"{cas['nom']} (rendu après correction)",
                            t.rendre(corr).commande, cas["rendu"])
        echecs_correction += not ok

    total_correction = len(CAS_CORRECTION)
    if echecs or echecs_correction:
        print(f"\n{echecs} cas de traduction en échec sur {total}, "
              f"{echecs_correction} cas de correction en échec sur {total_correction}.")
        return 1
    print(f"{total} cas de traduction, {total_correction} cas de correction — tous conformes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

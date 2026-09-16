#!/usr/bin/env python3
"""Rétro-traduction contre la feuille communautaire ETC « Handy Macros ».

CE BANC NE VALIDE RIEN. Il cherche à faire échouer le traducteur contre une
source qu'il n'a pas écrite. C'est sa seule utilité, et c'est ce qui le
distingue des trois autres bancs du dépôt : `test_traducteur.py` compare le
traducteur à des attentes que j'ai posées moi-même, donc il ne peut jamais
révéler qu'une attente était fausse. Ici l'attente vient de praticiens qui ne
connaissent ni le lexique ni le modèle.

Un désaccord n'est PAS un échec du traducteur. C'est une question — et elle
peut se trancher dans les deux sens : le manuel §16 a déjà donné tort à la
feuille sur « Quickstep ». Les cinq verdicts se lisent donc ainsi :

    identique       les deux sources écrivent la même commande — signal fort
    equivalent      formes différentes, toutes deux attestées au manuel
    divergent       désaccord réel — part au journal, ne se tranche pas ici
    hors_perimetre  le traducteur ne couvre pas encore cette intention
    source_fautive  la feuille est démontrablement fausse (manuel à l'appui)
    illisible       cellule perdue à l'export du tableur, rien à comparer
    multi_commande  l'entrée est une MACRO (plusieurs commandes, ou une pause
                    interactive) : le traducteur produit des lignes de
                    commande, pas des macros. Comparer les deux donnerait un
                    faux désaccord alors que c'est une fonctionnalité absente,
                    pas une syntaxe fausse — et ça gonflerait artificiellement
                    le dénominateur d'un test dont tout l'intérêt est d'être
                    honnête sur ce qu'il mesure.

CE QUI FAIT ÉCHOUER CE BANC — un seul cas : la RÉGRESSION, c'est-à-dire un
verdict qui recule par rapport à la référence enregistrée dans le YAML
(`identique` qui devient `divergent`, `divergent` qui devient
`hors_perimetre`). Une progression, elle, ne fait pas échouer : elle demande
juste que la référence soit remise à jour, et le banc dit laquelle.

Ce banc ne prouve JAMAIS qu'une macro fonctionne. La feuille est de confiance
B ; seul le banc réel (grammar/refus_terrain.yaml) produit du S.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).parent
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(RACINE.parent / "grammar"))

import yaml                                                    # noqa: E402
from traducteur import Traducteur                              # noqa: E402
from generateur import Generateur                              # noqa: E402

CORPUS = RACINE.parent / "corpus" / "handy_macros_etc.yaml"

# Ordre de qualité : un verdict ne doit jamais reculer dans cette liste.
# `illisible` est hors échelle — rien à comparer, donc rien à faire reculer.
ECHELLE = ["hors_perimetre", "divergent", "equivalent", "identique"]

# Verdicts posés à la main dans le YAML, que le code ne peut pas déduire :
# ils portent sur la FEUILLE, pas sur le traducteur. Le calcul dirait
# « divergent » sans savoir de quel côté est l'erreur.
FIGES = ("source_fautive", "illisible")

# Marqueurs d'une macro plutôt que d'une ligne de commande.
MARQUEURS_MACRO = ("wait_for_enter", "wait_for_input", "macro_wait",
                   "macro_loop_begin", "macro_loop_end")


def est_multi_commande(syntaxe: str) -> bool:
    """Une macro, ou une ligne de commande ?

    Deux signes suffisent et ils sont sûrs : une pause d'éditeur de macro
    (`Wait_For_Enter`, `Macro_Wait`, `Macro_Loop_*`) n'existe que dans une
    macro ; et deux `Enter` sur une même entrée veulent dire deux commandes,
    puisqu'`Enter` est précisément ce qui termine une commande.
    """
    bas = syntaxe.lower().replace(" ", "_")
    if any(m in bas for m in MARQUEURS_MACRO):
        return True
    return syntaxe.lower().split().count("enter") > 1


def normaliser(commande: str) -> str:
    """Compare des commandes, pas des mises en forme.

    Les deux sources ne ponctuent pas pareil et n'ont pas à le faire : la
    feuille écrit `Copy_To`, le dépôt écrit `Copy To`, Eos traite l'espace et
    le souligné comme équivalents et ignore la casse (documenté en tête de
    reference/eosKeys.ts). Comparer les graphies produirait des désaccords qui
    n'en sont pas, et masquerait les vrais dans le bruit.
    """
    return " ".join(commande.replace("_", " ").lower().split())


# Pourquoi une entrée est hors périmètre se LIT dans le corpus, ça ne se
# devine pas depuis le message de refus.
#
# Ce banc a deviné la cause pendant six jours, en cherchant « aucun numéro »
# dans le texte du refus pour conclure « sélection implicite ». Le 2026-09-14
# une qualification à la main des 23 entrées a montré que ce classement était
# FAUX sur les 11 entrées qu'il rangeait ainsi — et faux dans le sens le plus
# coûteux : il avait fait inscrire au planning, comme priorité numéro un, un
# arbitrage produit sur la sélection implicite qui ne débloquait en réalité
# AUCUNE entrée. Deux exemples suffisent à voir le vice :
#
#   channel_check  `Chan 1 At 75 Check Enter`   — cible explicite. Il manque `Check`.
#   color_xfd_50   `Color_Crossfade 50 Enter`   — réglage GLOBAL, sans sélection.
#
# Un message de refus dit ce que le traducteur a remarqué en premier, pas ce
# qui bloque. Les deux coïncident rarement. La cause est donc désormais un
# champ `cause:` écrit à la main dans `handy_macros_etc.yaml`, en regard de la
# syntaxe de la feuille — et une entrée hors périmètre SANS cause fait échouer
# ce banc, pour qu'aucune ne s'ajoute en silence.
CAUSES_CONNUES = {
    "action_absente": "le mot-clé Eos n'est pas dans le modèle",
    "forme_absente": "l'action existe, pas sous cette forme",
    "navigation_relative": "désigne par position (Next/Last), pas par numéro",
    "mecanisme_absent": "chaîne entière à construire",
    "macro_non_terminee": "finit exprès sans valeur, l'opérateur complète",
    "hors_ligne_de_commande": "pilote l'affichage, pas la conduite",
    "source_douteuse": "cellule de la feuille inexploitable",
    "selection_implicite": "vise « ce qui est sélectionné » — règle 5",
    "sens_non_atteste": "la feuille suggère un sens qu'aucune source ne confirme",
}


# Deux tokens qu'Eos accepte sans les exiger. La liste est COURTE et chaque
# entrée est prouvée par le manuel : élargir cette liste au jugé ferait passer
# des désaccords réels pour des équivalences, et ce banc n'aurait plus qu'à
# être supprimé. Toute addition demande une citation.
#
#   Time  après `Sneak` : le manuel écrit `[Sneak] <Time> [3] [Enter]`, et sa
#         convention de notation (§00 « Welcome », l. 339) dit que les crochets
#         angulaires marquent les touches « which don't have to be pressed ».
#   At    devant un niveau : `[1] [Full]` (§6 l. 314) et `[At] [Full]`
#         (§6 l. 852, 988, 1008, 1268) sont tous deux attestés.
OPTIONNELS = ("time", "at")


def sans_optionnels(commande: str) -> str:
    return " ".join(m for m in normaliser(commande).split()
                    if m not in OPTIONNELS)


def verdict_de(entree: dict, traducteur: Traducteur) -> tuple[str, str, str]:
    """Renvoie (verdict, commande produite, explication)."""
    attendu = entree["syntaxe_feuille"]
    if attendu is None:
        return "illisible", "", entree.get("pourquoi") or "cellule perdue"
    if est_multi_commande(attendu):
        return "multi_commande", "", attendu

    trad = traducteur.traduire(entree["demande_nl"])
    if not trad.compris:
        motif = trad.notes[0] if trad.notes else "aucune intention reconnue"
        return "hors_perimetre", "", motif


    produit = traducteur.rendre(trad).commande
    if normaliser(produit) == normaliser(attendu):
        return "identique", produit, ""
    if normaliser(sans_optionnels(produit)) == normaliser(sans_optionnels(attendu)):
        return "equivalent", produit, f"feuille : {attendu}"
    return "divergent", produit, f"feuille : {attendu}"


def main() -> int:
    corpus = yaml.safe_load(CORPUS.read_text(encoding="utf-8"))
    traducteur = Traducteur(generateur=Generateur())

    regressions: list[str] = []
    progressions: list[str] = []
    compte: dict[str, int] = {}
    causes: dict[str, int] = {}
    non_qualifiees: list[str] = []
    causes_inconnues: list[str] = []
    lignes: list[str] = []

    for entree in corpus["entrees"]:
        calcule, produit, explication = verdict_de(entree, traducteur)
        reference = entree.get("verdict")

        affiche = reference if reference in FIGES else calcule
        compte[affiche] = compte.get(affiche, 0) + 1
        if affiche == "hors_perimetre":
            c = entree.get("cause")
            if c is None:
                non_qualifiees.append(entree["id"])
            elif c not in CAUSES_CONNUES:
                causes_inconnues.append(f"{entree['id']} : cause « {c} »")
            else:
                causes[c] = causes.get(c, 0) + 1

        if reference in ECHELLE and calcule in ECHELLE:
            if ECHELLE.index(calcule) < ECHELLE.index(reference):
                regressions.append(
                    f"{entree['id']} : {reference} -> {calcule}"
                    + (f"  (produit : {produit})" if produit else ""))
            elif ECHELLE.index(calcule) > ECHELLE.index(reference):
                progressions.append(f"{entree['id']} : {reference} -> {calcule}")
        elif reference is None and calcule != "illisible":
            progressions.append(f"{entree['id']} : (non enregistré) -> {calcule}")

        marque = {"identique": "=", "equivalent": "~", "divergent": "!",
                  "hors_perimetre": ".", "source_fautive": "x",
                  "illisible": "-", "multi_commande": "M"}[affiche]
        detail = produit or explication
        lignes.append(f"  {marque} {entree['id']:24} {affiche:15} {detail[:70]}")

    print("Rétro-traduction — feuille communautaire ETC « Handy Macros »")
    print("  =  identique     ~  equivalent      !  divergent")
    print("  .  hors périmètre x  source fautive  -  illisible\n")
    print("\n".join(lignes))

    # Le dénominateur qui compte n'est pas 43, ni même 37 : c'est le nombre
    # d'entrées que le traducteur pouvait honnêtement viser — une seule ligne
    # de commande, lisible, et dont la feuille n'est pas fautive.
    hors_jeu = (compte.get("illisible", 0) + compte.get("multi_commande", 0)
                + compte.get("source_fautive", 0))
    comparables = len(corpus["entrees"]) - hors_jeu
    accord = compte.get("identique", 0) + compte.get("equivalent", 0)

    print(f"\n{accord}/{comparables} en accord sur les entrées comparables "
          f"({compte.get('divergent', 0)} divergences, "
          f"{compte.get('hors_perimetre', 0)} hors périmètre).")
    if causes:
        print("  causes du hors-périmètre (déclarées dans le corpus, "
              "pas déduites du refus) :")
        for nom, n in sorted(causes.items(), key=lambda kv: -kv[1]):
            print(f"       {n:2}  {nom:22} — {CAUSES_CONNUES[nom]}")
    print(f"Hors comparaison : {compte.get('multi_commande', 0)} macros "
          f"multi-commandes, {compte.get('source_fautive', 0)} entrées fautives, "
          f"{compte.get('illisible', 0)} cellules perdues "
          f"— sur {len(corpus['entrees'])} entrées au total.")

    if progressions:
        print("\nRéférences à mettre à jour dans le YAML (progression) :")
        for p in progressions:
            print(f"  {p}")
    # Une entrée hors périmètre sans cause déclarée fait ÉCHOUER ce banc.
    # Sans ça, la qualification se périmerait en silence dès la prochaine
    # entrée ajoutée — et c'est exactement ce silence qui a produit six jours
    # de fausse priorité (voir le commentaire de CAUSES_CONNUES).
    if non_qualifiees:
        print("\nENTRÉES HORS PÉRIMÈTRE SANS `cause:` DÉCLARÉE :")
        for i in non_qualifiees:
            print(f"  {i}")
        print("  -> ajouter `cause:` et `cause_detail:` dans "
              "corpus/handy_macros_etc.yaml, en regard de la syntaxe de la "
              "feuille — PAS d'après le message de refus.")
    if causes_inconnues:
        print("\nCAUSES HORS TAXONOMIE :")
        for c in causes_inconnues:
            print(f"  {c}")
        print(f"  -> valeurs admises : {', '.join(sorted(CAUSES_CONNUES))}")
    if regressions:
        print("\nRÉGRESSIONS :")
        for r in regressions:
            print(f"  {r}")
    return 1 if (regressions or non_qualifiees or causes_inconnues) else 0


if __name__ == "__main__":
    sys.exit(main())

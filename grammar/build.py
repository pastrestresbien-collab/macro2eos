#!/usr/bin/env python3
"""Compile le modèle YAML en JSON et vérifie sa cohérence.

Usage:
    python3 grammar/build.py            # compile + vérifie
    python3 grammar/build.py --check    # vérifie seulement (CI)

Produit `grammar/dist/modele.json` et `grammar/dist/patrons.json`.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).parent
DIST = RACINE / "dist"
PLANNING = RACINE.parent / "PLANNING.md"
CONFIANCES = {"S", "A", "B", "C", "D", None}
ARGUMENTS_FAN = {"aucun", "entier", "inconnu"}
# du plus fiable au moins fiable — sert à repérer une règle plus confiante que
# l'action qu'elle valide
ORDRE_CONFIANCE = {"S": 4, "A": 3, "B": 2, "C": 1, "D": 0}


def charger(nom: str) -> dict:
    return yaml.safe_load((RACINE / f"{nom}.yaml").read_text(encoding="utf-8"))


def numeros_backlog() -> set[int]:
    """Numéros effectivement listés dans le backlog de PLANNING.md.

    Un renvoi vers un numéro qui n'existe pas est pire qu'un renvoi absent :
    il donne l'illusion qu'une zone d'ombre est suivie quelque part."""
    if not PLANNING.exists():
        return set()
    texte = PLANNING.read_text(encoding="utf-8")
    return {int(n) for n in re.findall(r"^(\d{1,3})\. ", texte, re.MULTILINE)}


def verifier_refus_non_reportes(modele: dict, refus_terrain: dict) -> list[str]:
    """Un constat terrain (refus OU comportement inattendu accepté à tort) qui
    tranche un point encore `inconnu` dans le modèle signale que `modele.yaml`
    a pris du retard sur le banc réel — à corriger avant de compiler, pas
    après. Les deux types de constat partagent les mêmes champs `tranche`,
    `backlog`, `date`, `diagnostic` — voir refus_terrain.yaml pour le détail."""
    avertissements: list[str] = []
    backlogs_inconnus = {
        r["backlog"] for r in modele["legalite"]
        if r["valide"] == "inconnu" and "backlog" in r
    }
    for constat in refus_terrain.get("refus", []):
        if constat.get("tranche") not in ("oui", "non"):
            continue
        for b in constat.get("backlog", []):
            if b in backlogs_inconnus:
                avertissements.append(
                    f"constat du {constat['date']} tranche PLANNING #{b} "
                    f"(« {constat['diagnostic'].strip().splitlines()[0]} » ...) "
                    f"mais modele.yaml le porte toujours `inconnu` — à mettre à jour"
                )
    return avertissements


def verifier_vocabulaire(modele: dict, backlog: set[int]) -> list[str]:
    """Objets, actions, styles de Fan, contrôle de macro : tout terme du modèle
    porte une confiance, et tout terme dont le comportement est inconnu renvoie
    au backlog. Même exigence que pour la matrice de légalité — sans quoi une
    zone d'ombre resterait invisible dans le vocabulaire."""
    erreurs: list[str] = []
    actions = set(modele["actions"])

    for section in ("objets", "actions"):
        for nom, spec in modele[section].items():
            if spec.get("confiance") not in CONFIANCES or spec.get("confiance") is None:
                erreurs.append(f"{section}.{nom} : confiance manquante ou invalide")

    for nom, style in modele["fan"]["styles"].items():
        if style.get("confiance") not in CONFIANCES or style.get("confiance") is None:
            erreurs.append(f"fan.styles.{nom} : confiance manquante ou invalide")
        if style.get("argument") not in ARGUMENTS_FAN:
            erreurs.append(
                f"fan.styles.{nom} : `argument` doit valoir "
                f"{'/'.join(sorted(ARGUMENTS_FAN))}, pas `{style.get('argument')}`"
            )
        # un style dont l'effet n'est pas connu ne doit jamais être générable en
        # silence : il porte un renvoi backlog, comme une case `inconnu`
        if "inconnu" in (style.get("comportement"), style.get("argument")):
            if "backlog" not in style:
                erreurs.append(
                    f"fan.styles.{nom} : comportement/argument inconnu mais sans "
                    f"renvoi PLANNING.md"
                )

    for nom, tok in modele["macro"]["controle"].items():
        if tok.get("confiance") not in CONFIANCES or tok.get("confiance") is None:
            erreurs.append(f"macro.controle.{nom} : confiance manquante ou invalide")

    for nom, cond in modele["query"]["conditions"].items():
        if cond.get("confiance") not in CONFIANCES or cond.get("confiance") is None:
            erreurs.append(f"query.conditions.{nom} : confiance manquante ou invalide")
        # une condition sans touche OSC est hors de portée d'une injection par
        # `/eos/key/` : la zone d'ombre doit renvoyer au backlog, pas dormir
        if "osc" not in cond:
            erreurs.append(
                f"query.conditions.{nom} : champ `osc` absent — écrire `osc: null` "
                f"si la condition n'a pas de touche OSC, jamais l'omettre"
            )
        elif cond["osc"] is None and "backlog" not in cond:
            erreurs.append(
                f"query.conditions.{nom} : sans touche OSC et sans renvoi PLANNING.md"
            )

    # le raccourci historique `record_palette_couleur` (v0.1, sous
    # non-régression) doit rester équivalent à la forme générique v0.7 —
    # sinon le modèle porterait deux syntaxes pour le même geste
    raccourci = modele["actions"]["record_palette_couleur"]["mot_cle"]
    generique = " ".join([
        modele["actions"]["record_palette"]["mot_cle"],
        modele["palettes"]["familles"]["Color Palette"]["mot_cle"],
    ])
    if raccourci != generique:
        erreurs.append(
            f"actions.record_palette_couleur (`{raccourci}`) diverge de la forme "
            f"générique (`{generique}`) — deux syntaxes pour le même geste"
        )

    # un mot-clé employé à la fois comme cible et comme action doit s'écrire
    # pareil des deux côtés — sinon le générateur produirait deux syntaxes
    for nom, cible in modele["cibles"].items():
        if cible.get("confiance") not in CONFIANCES or cible.get("confiance") is None:
            erreurs.append(f"cibles.{nom} : confiance manquante ou invalide")
        assoc = cible.get("action_associee")
        if assoc is None:
            continue
        if assoc not in modele["actions"]:
            erreurs.append(f"cibles.{nom} : action associée inconnue `{assoc}`")
        elif modele["actions"][assoc]["mot_cle"] != cible["mot_cle"]:
            erreurs.append(
                f"cibles.{nom} : mot-clé `{cible['mot_cle']}` incohérent avec "
                f"actions.{assoc} (`{modele['actions'][assoc]['mot_cle']}`)"
            )

    for nom, mod in modele["modificateurs"].items():
        if mod.get("confiance") not in CONFIANCES or mod.get("confiance") is None:
            erreurs.append(f"modificateurs.{nom} : confiance manquante ou invalide")
        for cible in mod.get("porte_sur", []):
            if cible not in actions:
                erreurs.append(f"modificateurs.{nom} : porte sur une action inconnue `{cible}`")

    # tout renvoi backlog, d'où qu'il vienne, doit exister dans PLANNING.md
    if backlog:
        for ref, numero in renvois_backlog(modele):
            if numero not in backlog:
                erreurs.append(f"{ref} : renvoi PLANNING #{numero} absent du backlog")

    return erreurs


def verifier_derive(modele: dict) -> list[str]:
    """Contrôles de dérive, ajoutés après la relecture d'ensemble de v0.15.

    Treize tranches écrites l'une après l'autre finissent par produire des
    doublons et des incohérences que rien ne signalait. Ces trois contrôles
    les rendent visibles à la compilation plutôt qu'à la relecture suivante."""
    erreurs: list[str] = []
    actions = modele["actions"]

    # (a) deux actions qui écrivent le même mot-clé sont un doublon, sauf si
    #     l'homonymie est explicitement assumée — la polysémie d'Eos se déclare
    par_mot: dict[str, list[str]] = {}
    for nom, spec in actions.items():
        par_mot.setdefault(spec["mot_cle"], []).append(nom)
    assumees = modele.get("homonymies_assumees", {})
    for mot, noms in par_mot.items():
        if len(noms) < 2 or not mot:
            continue
        declaree = assumees.get(mot, {}).get("actions")
        if declaree is None:
            erreurs.append(
                f"mot-clé `{mot}` porté par {len(noms)} actions "
                f"({', '.join(sorted(noms))}) sans homonymie assumée — "
                f"doublon, ou à déclarer dans `homonymies_assumees`"
            )
        elif set(declaree) != set(noms):
            erreurs.append(
                f"homonymies_assumees.{mot} liste {sorted(declaree)} mais le "
                f"modèle porte {sorted(noms)}"
            )

    # (b) une règle ne peut pas être plus confiante que l'action qu'elle valide.
    #     Exception : un refus (`valide: non`) tient sa confiance de
    #     l'observation du refus, pas de la documentation de l'action.
    for i, regle in enumerate(modele["legalite"]):
        nom = regle.get("action")
        if not nom or regle.get("confiance") is None or regle["valide"] == "non":
            continue
        ca = actions[nom].get("confiance")
        if ca and ORDRE_CONFIANCE.get(regle["confiance"], -1) > ORDRE_CONFIANCE.get(ca, -1):
            erreurs.append(
                f"legalite[{i}] ({regle.get('objet')}/{nom}) : règle en "
                f"{regle['confiance']} alors que l'action n'est qu'en {ca}"
            )

    # (c) une action que la matrice ne cite jamais est invisible au générateur,
    #     qui la signalera « absente du modèle » à la première utilisation
    citees = {r.get("action") for r in modele["legalite"] if r.get("action")}
    for nom in sorted(set(actions) - citees):
        erreurs.append(
            f"action `{nom}` absente de la matrice de légalité — le générateur "
            f"la déclarera non vérifiable"
        )

    # (d) toute action doit citer sa source : c'est ce qui rend le modèle
    #     re-vérifiable contre le manuel
    for nom, spec in sorted(actions.items()):
        if "source" not in spec:
            erreurs.append(f"actions.{nom} : pas de `source` — non re-vérifiable")

    return erreurs


def renvois_backlog(modele: dict) -> list[tuple[str, int]]:
    """Tous les renvois `backlog` du modèle, avec leur emplacement."""
    renvois: list[tuple[str, int]] = []
    for i, regle in enumerate(modele["legalite"]):
        if "backlog" in regle:
            renvois.append((f"legalite[{i}]", regle["backlog"]))
    for nom, style in modele["fan"]["styles"].items():
        if "backlog" in style:
            renvois.append((f"fan.styles.{nom}", style["backlog"]))
    for nom, cond in modele["query"]["conditions"].items():
        if "backlog" in cond:
            renvois.append((f"query.conditions.{nom}", cond["backlog"]))
    for regle in modele["macro"]["regles_generation"]:
        if "backlog" in regle:
            renvois.append((f"macro.regles_generation.{regle['id']}", regle["backlog"]))
    for regle in modele["osc"]["regles"]:
        if "backlog" in regle:
            renvois.append((f"osc.regles.{regle['id']}", regle["backlog"]))
    if "backlog" in modele["osc"]["touche"]["nommage"]:
        renvois.append(("osc.touche.nommage", modele["osc"]["touche"]["nommage"]["backlog"]))
    return renvois


def verifier(modele: dict, patrons: dict, backlog: set[int] | None = None) -> list[str]:
    """Contrôles de cohérence interne. Retourne la liste des erreurs."""
    erreurs: list[str] = []
    objets = set(modele["objets"])
    actions = set(modele["actions"])

    for i, regle in enumerate(modele["legalite"]):
        ref = regle.get("combinaison") or f"{regle.get('objet')}/{regle.get('action')}"

        if regle["valide"] not in ("oui", "non", "inconnu"):
            erreurs.append(f"legalite[{i}] ({ref}) : `valide` doit être oui/non/inconnu")

        if regle.get("confiance") not in CONFIANCES:
            erreurs.append(f"legalite[{i}] ({ref}) : confiance `{regle.get('confiance')}` invalide")

        # une combinaison validée doit porter une confiance, une inconnue doit
        # renvoyer au backlog — sinon la zone d'ombre devient invisible
        if regle["valide"] == "oui" and regle.get("confiance") is None:
            erreurs.append(f"legalite[{i}] ({ref}) : validée mais sans niveau de confiance")
        if regle["valide"] == "inconnu" and "backlog" not in regle:
            erreurs.append(f"legalite[{i}] ({ref}) : inconnue mais sans renvoi PLANNING.md")

        # les références objet/action doivent exister
        obj = regle.get("objet")
        if obj and obj not in objets and obj != "selection_courante":
            erreurs.append(f"legalite[{i}] : objet inconnu `{obj}`")
        act = regle.get("action")
        if act and act not in actions:
            erreurs.append(f"legalite[{i}] : action inconnue `{act}`")

    for p in patrons["patrons"]:
        if p.get("confiance") not in CONFIANCES:
            erreurs.append(f"patron `{p['id']}` : confiance invalide")
        if p.get("confiance") is None and not p.get("avertissements"):
            erreurs.append(
                f"patron `{p['id']}` : sans confiance établie, il doit lister "
                f"ses avertissements (renvois PLANNING.md)"
            )
        for numero in p.get("avertissements", []):
            if backlog and numero not in backlog:
                erreurs.append(
                    f"patron `{p['id']}` : renvoi PLANNING #{numero} absent du backlog"
                )

    return erreurs


def main() -> int:
    modele = charger("modele")
    patrons = charger("patrons")
    refus_terrain = charger("refus_terrain")

    backlog = numeros_backlog()

    erreurs = (verifier(modele, patrons, backlog)
               + verifier_vocabulaire(modele, backlog)
               + verifier_derive(modele))
    if erreurs:
        print("Incohérences détectées :", file=sys.stderr)
        for e in erreurs:
            print(f"  - {e}", file=sys.stderr)
        return 1

    inconnues = [r for r in modele["legalite"] if r["valide"] == "inconnu"]
    styles_ouverts = [n for n, s in modele["fan"]["styles"].items() if "backlog" in s]
    print(f"Modèle v{modele['meta']['version']} — cohérent.")
    print(f"  {len(modele['objets'])} objets, {len(modele['actions'])} actions, "
          f"{len(modele['modificateurs'])} modificateurs, "
          f"{len(modele['legalite'])} règles de légalité")
    conditions = modele["query"]["conditions"]
    sans_osc = [n for n, c in conditions.items() if c["osc"] is None]
    print(f"  {len(modele['fan']['styles'])} styles de Fan "
          f"(dont {len(styles_ouverts)} au comportement non observé), "
          f"{len(modele['macro']['controle'])} tokens de contrôle de macro")
    print(f"  {len(conditions)} conditions Query "
          f"(dont {len(sans_osc)} sans touche OSC : {', '.join(sans_osc)})")
    print(f"  {len(inconnues)} zone(s) non tranchée(s) → banc réel : "
          f"{', '.join('PLANNING#%s' % r['backlog'] for r in inconnues)}")
    print(f"  {len(patrons['patrons'])} patron(s)")
    print(f"  {len(refus_terrain.get('refus', []))} refus terrain enregistré(s)")

    retard = verifier_refus_non_reportes(modele, refus_terrain)
    if retard:
        print("\nRefus terrain non encore reportés dans modele.yaml :")
        for a in retard:
            print(f"  ⚠ {a}")

    if "--check" in sys.argv:
        return 0

    DIST.mkdir(exist_ok=True)
    for nom, data in (("modele", modele), ("patrons", patrons), ("refus_terrain", refus_terrain)):
        cible = DIST / f"{nom}.json"
        cible.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"  → {cible.relative_to(RACINE.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

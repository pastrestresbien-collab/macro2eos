#!/usr/bin/env python3
"""Compile l'index thématique des tutoriels — « où apprend-on X ? ».

Le problème
-----------
`INDEX.md` liste les 13 documents convertis, avec leur version et leur statut
de conversion. C'est un inventaire, pas un sommaire : il dit qu'un workbook
Effets existe, jamais qu'on apprend les submasters au L1 §Submasters, les
propriétés de submaster au L2, et le fader d'effet au workbook Effets §Unit 7.
Pour trouver un tutoriel, il fallait donc chercher — dans ~37 Mo.

Ce script extrait les titres de niveau 2 de tous les documents et en fait deux
vues : par document (le sommaire de chacun) et **par sujet, ordre
alphabétique, tous documents confondus** — c'est cette seconde vue qui répond
à « où apprend-on X ? », parce qu'un même sujet est presque toujours traité à
plusieurs niveaux.

Généré, jamais tenu à la main
-----------------------------
Même doctrine que `traducteur/build_catalogue.py` et
`build_vocabulaire_llm.py` : un index recopié à la main dériverait au premier
document ajouté ou reconverti, et un sommaire qui pointe à côté est pire que
pas de sommaire. Tout vient des titres réellement présents dans les `.md`.

La seule partie écrite à la main est la table `DOCUMENTS` ci-dessous : le
libellé lisible, le niveau et l'ordre de lecture d'un document ne sont pas
déductibles de son contenu. Elle est volontairement minimale.

Usage:
    python3 manuals/build_index_tutos.py

Produit `manuals/INDEX_TUTOS.md`.
"""
from __future__ import annotations

import re
from pathlib import Path

RACINE = Path(__file__).parent

# Seule partie non déduite du contenu : comment présenter chaque document.
#   libelle  - nom court, lisible
#   niveau   - progression pédagogique, pour trier et pour situer un sujet
#   ordre    - ordre de lecture conseillé
DOCUMENTS = {
    "l1-essentials-workbook":       ("L1 — Essentials",          "débutant",     1),
    "l2-enhanced-workbook":         ("L2 — Enhanced",            "intermédiaire", 2),
    "l3-advanced-workbook":         ("L3 — Intermediate",        "avancé",       3),
    "l4-proficient-workbook":       ("L4 — Proficient",          "expert",       4),
    "effects-workbook":             ("Effets (intensif)",        "thématique",   5),
    "magic-sheets-workbook":        ("Magic Sheets (intensif)",  "thématique",   6),
    "busking-workbook":             ("Busking",                  "thématique",   7),
    "augment3d-workbook":           ("Augment3d",                "thématique",   8),
    "virtual-media-server-workbook": ("Serveur média virtuel",   "thématique",   9),
    "operations-manual":            ("Manuel d'exploitation",    "référence",   10),
    "osc-integration":              ("Intégration OSC",          "référence",   11),
    "hotkeys":                      ("Raccourcis clavier",       "référence",   12),
    "control-philosophy-whitepaper": ("Philosophie du contrôle", "référence",   13),
}

# Titres de pure structure, présents dans presque chaque workbook : ils
# n'apprennent rien et noieraient l'index par sujet.
BOILERPLATE = {"table of contents", "purpose of the class"}


def titres_du_document(dossier: Path) -> list[tuple[str, Path, int]]:
    """(titre, fichier, ligne) pour chaque `## ` du document.

    `source/` est ignoré : ce sont les PDF/DOCX d'origine, conservés pour
    re-vérification et jamais consultés en routine (CLAUDE.md, règle n°2).
    """
    trouves: list[tuple[str, Path, int]] = []
    for fichier in sorted(dossier.glob("*.md")):
        for n, ligne in enumerate(fichier.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"^##\s+(.+?)\s*$", ligne)
            if not m:
                continue
            titre = m.group(1).strip()
            if titre.lower() in BOILERPLATE:
                continue
            trouves.append((titre, fichier, n))
    return trouves


def construire() -> str:
    par_document: dict[str, list] = {}
    par_sujet: dict[str, list] = {}

    for nom, (libelle, niveau, ordre) in sorted(DOCUMENTS.items(), key=lambda kv: kv[1][2]):
        dossier = RACINE / nom
        if not dossier.is_dir():
            continue
        titres = titres_du_document(dossier)
        par_document[nom] = (libelle, niveau, ordre, titres)
        for titre, fichier, ligne in titres:
            par_sujet.setdefault(titre.lower(), []).append((titre, libelle, niveau, fichier, ligne))

    out: list[str] = []
    out.append("# Où apprend-on quoi — index des tutoriels\n")
    out.append(
        "**Fichier généré par `manuals/build_index_tutos.py` — ne pas éditer à la main.**\n"
        "Il extrait les titres réellement présents dans les `.md` convertis ; le modifier\n"
        "ici le ferait diverger des documents au premier ajout.\n"
    )
    out.append(
        "[`INDEX.md`](../INDEX.md) dit quels documents existent et dans quel état ils sont.\n"
        "Celui-ci dit **où trouver un sujet** — l'inventaire ne répondait pas à ça.\n"
    )

    out.append("\n## Par sujet\n")
    out.append("Un même sujet revient presque toujours à plusieurs niveaux : c'est\n"
               "exactement ce qu'on veut voir pour choisir par où commencer.\n")
    out.append("\n| Sujet | Où |\n|---|---|")
    for cle in sorted(par_sujet):
        entrees = par_sujet[cle]
        libelle_sujet = entrees[0][0]
        liens = " · ".join(
            f"[{lib}]({fichier.relative_to(RACINE).as_posix()}#L{ligne})"
            for _, lib, _, fichier, ligne in entrees
        )
        out.append(f"| {libelle_sujet} | {liens} |")

    out.append("\n## Par document\n")
    for nom, (libelle, niveau, _ordre, titres) in par_document.items():
        out.append(f"\n### {libelle} — *{niveau}*\n")
        out.append(f"`manuals/{nom}/` — {len(titres)} sections\n")
        for titre, fichier, ligne in titres:
            out.append(f"- [{titre}]({fichier.relative_to(RACINE).as_posix()}#L{ligne})")

    return "\n".join(out) + "\n"


def main() -> int:
    cible = RACINE / "INDEX_TUTOS.md"
    contenu = construire()
    cible.write_text(contenu, encoding="utf-8")
    sujets = contenu.count("\n| ") - 1
    print(f"  → {cible.relative_to(RACINE.parent)} ({sujets} sujets indexés)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

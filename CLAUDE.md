# Instructions pour toute session Claude travaillant sur ce dépôt

## Règle n°1 — PRIORITÉ ABSOLUE : accès réseau bloqué, ne jamais tenter de télécharger soi-même

**L'environnement d'exécution de cette session (et de toute session future sur ce dépôt)
ne peut PAS atteindre `etcconnect.com`, `github.com` en téléchargement direct, ni la
plupart des hôtes externes.** Testé et confirmé bloqué à plusieurs reprises : `curl`,
`WebFetch` (fichiers binaires **et pages HTML** — reconfirmé le 2026-08-03 sur
leefilters.com, Rosco, thomannmusic.com, lightspares.com et même Wikipedia, 403 partout),
`git clone` de dépôts tiers, navigateur headless (Playwright) même avec proxy explicite —
tout échoue systématiquement (403, connexion réinitialisée, ou timeout).

**Correction du 2026-08-03 : `WebFetch` ne marche PAS de façon fiable, contrairement à ce
qu'affirmait cette règle jusqu'ici.** Seul `WebSearch` fonctionne — il renvoie des extraits
de pages (titre, snippet, URL source), jamais le contenu intégral d'une page. Utile pour
vérifier un fait ponctuel et sourcé (voir `reference/lee_filters_theatre.md` pour un
exemple), inutilisable pour une conversion intégrale de document — ça reste le rôle de la
procédure d'upload ci-dessous.

**Ne jamais reperdre de temps à re-tenter ces méthodes.** La seule voie qui fonctionne à
tous les coups dans cette session pour un document complet :

1. Identifier la source exacte (recherche web via `WebSearch` — ça, ça marche ; `WebFetch`
   échoue quasi systématiquement, ne pas compter dessus) et donner à l'utilisateur le
   **lien direct exact** vers le fichier (PDF, DOCX, etc.).
2. L'utilisateur télécharge le fichier lui-même sur son appareil.
3. L'utilisateur l'envoie **directement dans la conversation** (upload dans le chat,
   pas via Git/GitHub — l'upload web GitHub échoue aussi au-delà de 25 Mo et n'est pas
   fiable sur mobile).
4. La session lit le fichier uploadé (`Read` gère PDF/DOCX nativement), le convertit en
   Markdown intégral, et le committe dans le dépôt.

**Ne jamais dire à l'utilisateur d'uploader via l'interface web GitHub** — source
d'échecs répétés (limite de taille, upload qui n'aboutit pas visible côté serveur).
Le chat est le seul canal de transfert de fichier fiable observé jusqu'ici.

## Règle n°2 — PDF/DOCX sources = archive, pas de consultation systématique

Les fichiers PDF/DOCX dans `manuals/<document>/source/` et `reference/source/` sont
conservés **uniquement** pour re-vérification future (règle de fidélité ci-dessous),
pas pour être relus à chaque tâche. Ils sont volumineux (jusqu'à 15 Mo) et ralentissent
le travail sans raison si on les rouvre systématiquement.

**Travailler à partir des `.md` déjà convertis.** Ne lire/consulter un PDF/DOCX source
que si un besoin précis et avéré l'exige (ex. : doute sur une fidélité de conversion à
vérifier, contenu manquant suspecté dans le `.md`). Dans ce cas, ne lire que la portion
nécessaire, pas le fichier entier.

**Cette règle vaut aussi pour les recherches, pas seulement les lectures complètes**
(ajouté le 2026-08-07, après un audit de consommation de tokens). `manuals/`,
`reference/` et `corpus/` — la « bibliographie » du projet — pèsent à eux trois plus de
40 Mo de texte. Un `Grep`/`Glob` sans périmètre explicite balaie tout le dépôt, y compris
ces dossiers : même sans ouvrir un fichier entier, une recherche large y coûte des tokens
en sortie pour un résultat presque toujours hors sujet quand le travail porte sur
`grammar/`, `traducteur/` ou `app/`. **Restreindre `path` (Grep) ou le dossier de départ
(Glob) au périmètre concerné par défaut** ; n'élargir la recherche à la bibliographie que
pour une vérification de fidélité précise contre une source primaire (ce que la règle
n°2 ci-dessus autorise déjà pour la lecture), jamais par réflexe ou par recherche
exploratoire large. Le principe est le même que pour les PDF : ce n'est pas qu'on n'a
pas le droit d'y toucher, c'est que la routine doit l'éviter par défaut.

## Contexte du projet

Voir `INDEX.md` (racine) pour l'état complet du corpus et des manuels convertis, et
`VERIFICATION.md` pour la méthode de vérification d'intégrité appliquée à chaque import.

Objectif du dépôt : corpus de référence complet (grammaire, macros, documentation
officielle ETC) pour un outil de traduction langage naturel → macros ETC Eos, avec
injection OSC ou ASCII vers la console.

## Règles de fidélité déjà en vigueur (voir INDEX.md pour le détail)

- Conversion **intégrale** de tout document source, jamais de résumé.
- PDF/DOCX source toujours conservé dans `manuals/<document>/source/` ou `reference/`
  pour re-vérification future.
- Toute conversion est vérifiée par échantillonnage contre le texte source avant d'être
  considérée complète (méthode documentée dans `VERIFICATION.md`).

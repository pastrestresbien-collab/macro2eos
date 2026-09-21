# PLANNING — macro2eos

Backlog **vivant et unique** du projet. Remplace les trois listes de questions ouvertes
qui coexistaient et divergeaient (corpus « PRIORITÉS BANC », corpus « ZONES ENCORE
OUVERTES », grammaire consolidée §15) — celles-ci restent en place comme trace d'audit
mais ne sont plus à mettre à jour.

Dernière mise à jour : 2026-09-21.

---

## Où en est le projet

**Phase 1 — collecte et conversion documentaire : terminée.**

| Acquis | État |
|---|---|
| Corpus communautaire 174 entrées | ✅ complet (sauf titre de l'entrée #154) |
| Manuel officiel v3.2.0, 32 chapitres | ✅ converti intégralement, vérifié (550/550 figures comptées, voir audit ci-dessous) |
| 12 workbooks / documents officiels annexes | ✅ convertis intégralement, **audités et corrigés le 2026-09-21** (voir section dédiée) |
| Table canonique des touches OSC (1155) | ✅ `reference/eosKeys.ts`, croisée avec le manuel |
| Journal terrain nomad réel (confiance S) | ✅ intégré verbatim |
| Grammaire consolidée de référence | ✅ `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` |
| Banc de test transport OSC/TCP | ✅ `reference/tools/` (simulateur + 3 clients) |

**Aucun document en attente.** Toute la documentation officielle ETC identifiée comme
utile est dans le dépôt.

**Phase 2 — exploitation : pas commencée.** C'est là que se situe la bascule à décider.
Le dépôt est aujourd'hui à 100 % de la prose Markdown : excellent pour un humain ou un
LLM qui lit, inutilisable tel quel par du code. Rien dans le dépôt n'est encore
consommable par un programme, sauf `eosKeys.ts`.

---

## Axes de travail — Phase 2

Trois axes, indépendants entre eux. À prioriser par l'utilisateur.

### A. Structurer la grammaire en données exploitables — **démarré**

Transformer `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` en un jeu de données
interrogeable (JSON/YAML) : vocabulaire des touches, règles de syntaxe, patrons de
commande, niveau de confiance par règle, risques associés.

Sans cette étape, tout parser à écrire devra ré-encoder la grammaire à la main et
divergera de la doc dès la première correction.

**Approche retenue** (2026-08-01) : modèle typé Objet → Action → Cible + matrice de
légalité, plutôt qu'une grammaire formelle (EBNF). La ligne de commande Eos est modale
et dépendante de l'état console ; une EBNF forcerait à trancher des points non validés
au banc. Ici, `inconnu` est une valeur de première classe et renvoie au backlog ci-dessous.

**Fait — v0.1**, voir [`grammar/`](grammar/README.md) : modèle, patrons, compilateur
YAML→JSON avec garde-fous de cohérence, générateur IR→commande avec avertissements, et
test de non-régression. Périmètre : sélection channels/groupes + couleur de nuancier +
record de palette. Les deux macros déjà éprouvées en transport sont régénérées à
l'identique, avec signalement automatique des points 4 et 5 du backlog.

**Reste à faire** : étendre le modèle au reste de la grammaire (Query, Fan, effets,
cues, submasters, macros, OSC), puis brancher la couche NL (axe B).

### B. Écrire le traducteur NL → macro

Le cœur du produit. Dépend de A si l'on veut éviter la duplication de la grammaire
dans le code. Prérequis déjà satisfaits : vocabulaire canonique, grammaire consolidée,
référentiel de risques, banc de transport OSC pour tester l'injection.

### C. Valider au banc réel

Une session sur console/nomad réel lèverait d'un coup la majorité des incertitudes
listées plus bas. C'est le seul axe qui ne peut pas être fait depuis ce dépôt.

**Mécanisme d'accumulation (2026-08-02)** : chaque refus de la console en usage réel est
une preuve de niveau S (voir `APP.md`, « La console fait autorité »). Au lieu de se
perdre, ces refus s'enregistrent dans `grammar/refus_terrain.yaml`, reliés à un numéro
de backlog ci-dessous. `grammar/build.py` signale si un refus tranche un point encore
marqué `inconnu` dans `grammar/modele.yaml` mais pas encore reporté. Le banc réel devient
ainsi cumulatif plutôt qu'une session isolée à programmer.

---

## Backlog technique — à valider au banc réel

Rien ci-dessous ne peut être tranché depuis le dépôt : il faut un Eos ou un ETCnomad.
Le simulateur `reference/tools/fakeeos.ts` ne valide que le transport, jamais la syntaxe.

### Priorité haute — bloquent des décisions d'architecture

1. **`SubDown` / `SubUp` — survie à l'export/import ASCII.** Corpus #027 signale que les
   macros pilotant un submaster par apprentissage ne survivent pas au cycle ASCII. Si
   confirmé, cela contraint le format de sortie du traducteur.
2. **Macro-dans-macro — fiabilité réelle.** Confirmé possible par le manuel (A), mais
   corpus #070 et #095 se contredisent sur la fiabilité d'exécution. Détermine si le
   traducteur peut décomposer une intention en macros chaînées.
3. **`Send_String` multiples depuis un Client — bug EOS-53576.** Corpus #107. Toujours
   présent en v3.2+ ? Conditionne la stratégie d'injection multi-commandes.

### Priorité moyenne — affectent la génération de macros

4. **`Group 5 + 1 Thru 6`** — combiner un groupe et une plage de channels. Aucun exemple
   exact dans le corpus ni dans le manuel ; transporté sans erreur par le simulateur
   (`reference/tools/test-client3.ts`), ce qui ne prouve rien syntaxiquement.
5. **`Record ... Label <texte multi-mots>`** — comportement réel avec espaces et tirets,
   dépend du clavier virtuel de la console.
6. **`{Enable}` / `{Disable}` sur le marking** — toggle ou absolu ? Corpus #118.
7. **`Go_To_Cue_<décimale>` concaténé** — troncature observée. Corpus #060.
8. **`Isn't In` / `Could Be` / `Group Cells` / `From Absolute`** — confirmés textuellement
   ailleurs mais absents de `eosKeys.ts`. Syntaxe exacte à vérifier. Corpus #148/#149.

### Priorité basse — complètent la couverture

9. **Styles de Fan non testés** : `{Interleave}`, `{Jump}`, `{Num Groups}`,
   `{Channels Per Group}`, `{Curve}`. Noms confirmés (A), comportements jamais observés.
10. **Ambiguïté `duration` (OSC)** et dérive de nommage `console_settings` /
    `desk_settings` — écarts relevés dans `reference/eosKeys_vs_manual_comparison.md`.
11. **Familles entières jamais explorées fonctionnellement**, découvertes via `eosKeys.ts` :
    RTC/Astro (déclenchement horaire), Pixel Mapping complet, édition de courbes,
    `startup_macro` / `shutdown_macro`. Corpus #152.
12. **Lamp Control** — incohérence de softkeys en édition directe. Corpus #091.

### Contradiction connue, non résolue

- Le simulateur `fakeeos.ts` émet un écho différé sur `/eos/sub/<n>`, alors que le journal
  terrain (`reference/JOURNAL_observations_nomad.md`, confiance S) affirme qu'un Eos réel
  ne republie **jamais** spontanément sur cette adresse. Simplification du simulateur
  probable — à ne pas prendre pour argent comptant.

---

## Audit de fidélité PDF→MD (2026-09-21)

**Déclencheur** : en travaillant sur `effects-workbook`, un tableau d'actions montré à
l'écran par l'utilisateur (effet 458) s'est révélé absent de la conversion `.md` —
aucune trace, aucun marqueur `(figure omise)`. Vérification étendue à tout le corpus.

**Cause identifiée** : la conversion DOCX→MD (`operations-manual`) marque
systématiquement chaque figure omise — vérifié par comptage exact : **550 références
d'image (`<a:blip>`) dans le `.docx` source = 550 marqueurs `(figure omise)`** dans les
`.md` du manuel. Aucune perte. En revanche, les conversions **PDF→MD** (tous les
workbooks) n'avaient **aucun mécanisme de signalement** : une capture d'écran pleine
page ou un tableau rendu comme image dans le PDF source pouvait disparaître
silencieusement à la conversion, sans laisser de trace. Les tableaux texte natifs et
les captures purement illustratives (redondantes avec un texte déjà complet) n'étaient
pas affectés.

**Méthode de vérification** : `poppler-utils` (absent de l'environnement de base) a été
installé pour rendre les PDF source page par page et les comparer visuellement aux
`.md`. Pour `operations-manual` (`.docx`), LibreOffice s'est révélé cassé dans cet
environnement (échoue même sur un `.txt` trivial) — vérification faite à la place par
comptage XML (`word/document.xml`) des références d'image, comparé aux marqueurs
`(figure omise)`.

**Résultat, par document** (tous corrigés directement dans les `.md`, commits sur
`claude/eos-console-learning-m6zn91`) :

| Document | Trous trouvés | Nature |
|---|---|---|
| `effects-workbook` | 7 | Tableaux d'actions d'effets (458, 458.1, 453.1, 454.4, 455, 456) + figures de formes d'onde |
| `magic-sheets-workbook` | 9 | Le plus touché — sujet visuel par nature. Captures pleine page d'éditeur, de magic sheets finies, d'exemples système/target/plot |
| `busking-workbook` | 7 | Diagramme Cue List Index (grille de propriétés) + 6 captures de la Busking Magic Sheet réutilisée par section |
| `l3-advanced-workbook` | 3 | 2 schémas (Update Ref Only/Make Absolute, magic sheet MS 301) + table Macro Editor (transcrite, lisible) |
| `l1-essentials-workbook` | 1 | Table de tracking Blind/Spreadsheet (valeurs exactes illisibles à la résolution dispo — documentée comme figure omise plutôt qu'inventée) |
| `l2-enhanced-workbook` | 1 | Magic sheet Appendix 2 entièrement absente |
| `virtual-media-server-workbook` | 1 | Schéma comparatif External/Virtual Media Server Control |
| `l4-proficient-workbook` | 2 | Petites captures de contenu de macro affiché à l'écran |
| `augment3d-workbook` | 0 | Propre — **80/80 pages vérifiées intégralement** (2026-09-21, suite à demande), captures uniquement illustratives, jamais seules porteuses de données |
| `control-philosophy-whitepaper` | 0 | Propre — **12/12 pages vérifiées intégralement**, icônes/photos décoratives, légendes déjà en texte |
| `osc-integration` | 0 | Propre — **14/14 pages vérifiées intégralement**, aucune image dans le PDF source, contenu 100% texte vérifié |
| `hotkeys` | 0 | Propre — **5/5 pages vérifiées intégralement**, table à raccourcis secondaires (cellule gauche vide) correctement fusionnée |
| `reference/Supported_OSC_Commands` | 0 | Propre — **17/17 pages vérifiées intégralement**, table dense entièrement vérifiée |
| `operations-manual` (.docx) | 0 | Propre — 550/550 figures comptées, conversion DOCX fiable dès le départ |

**Note méthode (2026-09-21)** : ces 5 documents marqués « propres » ont été vérifiés
**page par page en intégralité**, pas par échantillonnage — `augment3d-workbook`
notamment, plus gros volume du corpus (80 pages, 393 images intégrées), initialement
sondé sur ~44 pages puis complété aux 80 sur demande explicite. Aucun trou
supplémentaire trouvé. Les autres workbooks du tableau ci-dessus (`effects`,
`magic-sheets`, etc.) restent, eux, sondés par échantillonnage large mais pas
exhaustif page par page — un passage exhaustif y reste possible si jugé utile.

**Où sont les fixes** : chaque trou corrigé directement inline dans le `.md` concerné,
soit par transcription complète (quand lisible avec confiance : tables de commandes,
valeurs numériques nettes), soit par un bloc `(figure omise : description...)` avec
renvoi à la page exacte du PDF source (quand illisible ou trop complexe pour être
transcrit sans risque d'inventer une valeur).

**Mise à jour** : la table de tracking `l1-essentials` (p.27 du PDF) a finalement été
transcrite à la demande de l'utilisateur — lecture visuelle de bonne foi, explicitement
marquée non-OCR dans le `.md`, alignement colonne par colonne non garanti pixel-exact.
À revérifier contre le PDF source avant toute utilisation qui dépendrait des valeurs
exactes.

**Leçon méthodologique retenue** : toute future conversion PDF→MD doit désormais
marquer systématiquement chaque figure omise (même principe que la conversion DOCX),
pour ne pas rouvrir ce risque sur un futur document.

## Dettes documentaires mineures

- **Entrée #154 du corpus** : le titre et les premières lignes manquent (contenu présent
  à partir de « Confiance : C/B »). Lacune marquée dans le fichier. Nécessiterait que
  l'utilisateur retrouve le texte d'origine.
- **`Etude_Pont_MIDI-OSC_EOS.md`** : mentionné en début de projet comme source possible,
  jamais reçu. À rapatrier si toujours pertinent (voir `CLAUDE.md` règle n°1 pour la
  procédure de transfert).
- **Piste produit en attente** : « validation post-NL par édition à menus déroulants »,
  décrite dans la section « Notes produit » du corpus. À traiter en phase conception.

---

## Rappels de méthode (ne pas relâcher)

- Conversion **intégrale** des sources, jamais de résumé (`CLAUDE.md`).
- Sources PDF/DOCX = **archive**, pas de consultation routinière (`CLAUDE.md` règle n°2).
- Grammaire normative = sources A/B uniquement. Les usages communautaires (C/D) sont
  admis mais toujours marqués non-autoritaires et « non testé » par défaut.
- Toute macro validée uniquement contre le simulateur reste **non confirmée
  syntaxiquement**.

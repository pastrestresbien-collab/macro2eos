# Pipeline de traduction — NL → macro Eos

Décrit les 9 étapes que suit toute requête utilisateur en langage naturel, de la saisie
à l'ajout au corpus. Discuté et corrigé avec l'utilisateur le 2026-08-07 — voir
l'historique de session pour le raisonnement derrière chaque correction ; ce document
n'en garde que la version retenue.

Complète [`REGLES_POUR_UI.md`](REGLES_POUR_UI.md) (les règles de la grammaire Eos qui
contraignent l'interface) et [`APP.md`](APP.md) (la spécification produit) : celui-ci
décrit le **déroulé**, pas les règles individuelles ni les écrans.

---

## Les 9 étapes

**Étape 1 — Entrée NL**
Capturer la commande brute telle quelle, sans reformulation ni correction silencieuse.

**Étape 2 — Analyse : intention + paramètres**
Identifier l'intention de la demande (ex. : créer une palette, colorer une sélection,
aller à une cue) et en extraire les paramètres (cible, valeur, référence couleur...).
C'est ce découpage qui alimente l'étape 3 — **pas** la structure interne d'une commande
Eos elle-même. Objet → Action → Cible (voir `REGLES_POUR_UI.md`) décrit ce que la
console reçoit *en sortie*, pas comment une phrase française se lit *en entrée* : les
deux structures ne se correspondent pas terme à terme, ne pas les confondre dans le code
ni dans la doc.

**Étape 3 — Proposition de traduction**
Générer la commande Eos à partir du corpus structuré du projet (`grammar/` +
`traducteur/`), lui-même sourcé sur le corpus communautaire et le manuel officiel
(confiance A/B/C/D/S par entrée, voir l'échelle en étape 9). Si aucune entrée ne couvre
le cas : le dire explicitement (issue `incompris` du traducteur), ne jamais extrapoler.

**Étape 3bis — Demande hors corpus (fabricant, référence non couverte)**
Si la demande cite un fabricant ou une référence absente du corpus (Rosco, Apollo...) :
ne jamais improviser une valeur plausible. Deux issues seulement :
- demander à l'utilisateur de préciser autrement (une référence équivalente déjà
  couverte, un numéro exact) ;
- signaler que la donnée doit d'abord être ajoutée au corpus — comme cela a été fait
  pour Lee, à partir d'un catalogue officiel (voir `reference/lee_filters_theatre.md`).

Ne jamais résoudre ce cas en silence, quelle que soit la ressemblance avec une entrée
connue.

**Étape 4 — Affichage par paramètre, code couleur**
Chaque paramètre de la commande proposée s'affiche avec un code couleur selon sa
validité (ex. : vert = confiance haute, orange = ambigu ou confiance faible, rouge =
invalide/non reconnu). **Aucune validation individuelle obligatoire** — l'utilisateur
voit tout d'un coup d'œil, sans avoir à confirmer un par un les paramètres qui n'ont
rien d'ambigu.

Chaque paramètre reste **éditable au clic**, via un menu déroulant listant les
alternatives connues (jamais de saisie inventée par l'app). Deux cas où ce menu s'ouvre :
- l'utilisateur veut changer un paramètre qui n'a rien d'ambigu (édition volontaire) ;
- le paramètre est ambigu ou invalide (rouge/orange), et l'app propose les candidats
  plausibles.

Règles de tri des alternatives dans ce menu — **choix d'ergonomie du projet, pas des
faits sourcés** ; à distinguer clairement dans l'interface de ce qui vient du manuel
(même logique que les marqueurs ✅/📄/⚠️ de `REGLES_POUR_UI.md`) :
- *Famille syntaxique Eos* (cible, opérateur, verbe d'édition...) : ordre par risque
  d'ambiguïté croissant — d'abord la dépendance à un état préalable (sélection active,
  mode Live/Blind...), puis la portée/réversibilité de l'action.
- *Famille sémantique* (ex. couleur) : uniquement les fabricants réellement sourcés dans
  le dépôt (Lee aujourd'hui). Jamais Rosco, Apollo, ou toute référence non vérifiée —
  voir étape 3bis. Toujours une option de saisie libre en fin de liste, marquée « hors
  corpus, à vérifier ».

**Étape 5 — Validation utilisateur**
Afficher tous les paramètres en une seule fois, valeurs par défaut déjà appliquées (pas
d'action requise pour les accepter). **Blocage de l'envoi uniquement si un paramètre
reste rouge (invalide)** — pas de confirmation individuelle exigée sur les paramètres
valides.
Si une modification à cette étape rend la commande syntaxiquement invalide (étape 6) :
retour ici, pas d'étape 6 tant que ce n'est pas corrigé.
Sortie : une commande Eos unique et figée.

**Étape 6 — Contrôle d'intégrité + contexte requis**
Deux contrôles distincts, affichés séparément :
1. Intégrité syntaxique (fermeture, ordre des tokens). Échec → retour étape 5, aucun
   envoi.
2. Contexte console requis (mode Live/Blind, etc.) : **listé comme rappel à vérifier
   soi-même**, jamais comme un contrôle que l'app effectue — la console ne publie pas cet
   état, l'app ne peut pas le lire (voir `REGLES_POUR_UI.md`, règle 1).

Avant tout envoi vers une console réelle : préciser où regarder, attendre une
confirmation explicite. Une réponse à une autre question ne vaut pas accord.

**Étape 7 — Envoi et observation**
Préciser l'écran exact à observer. Attendre confirmation explicite de préparation avant
tout envoi. Point de synchronisation obligatoire — jamais une liste d'envois enchaînés
sans validation entre chacun.

**Étape 8 — Constat**
Un seul mécanisme d'enregistrement (`grammar/refus_terrain.yaml`), pas deux. Trois issues
possibles, toutes consignées au même endroit (`type: "refus"` ou
`type: "comportement_inattendu"`) :
- **conforme** → rien de plus, la commande est confirmée.
- **refusée par la console** → message d'erreur consigné verbatim (`erreur_console`).
- **acceptée mais résultat différent de l'attendu** → à consigner aussi, même sans
  message d'erreur (`attendu` / `observe`) : c'est la panne la plus dangereuse du projet
  (voir `REGLES_POUR_UI.md`, règle 4 — commande valide, console d'accord, résultat faux).

Dans les deux derniers cas → retour à l'étape 4 pour reformuler, le cycle recommence.

**Étape 9 — Ajout au corpus**
Nouvelle entrée : paramètre(s) source, commande finale, niveau de confiance selon
l'échelle du projet (déjà en usage dans tout le dépôt, ne jamais en improviser une
autre) :

**S** (testé sur console réelle) **>** **A** (manuel officiel, workbooks, docs OSC
officiels) **>** **B** (réponse officielle ETC en forum/blog) **>** **C** (communauté,
cohérent mais non testé) **>** **D** (signal négatif ou non fiable).

Une entrée ne peut porter **S** que si elle vient réellement de l'étape 8 avec un test
sur console — jamais par défaut. **État au 2026-08-07 : aucune entrée S** — le fichier
`grammar/refus_terrain.yaml` est vide et l'axe C de `PLANNING.md` (« valider au banc
réel ») n'a pas commencé. Ne pas s'étonner de ce vide, ne pas le combler artificiellement
en attendant.

---

## Points encore ouverts

- **Le rythme étapes 7-8 mélange peut-être deux choses distinctes** : valider le modèle
  une fois pour toutes sur une vraie console (rare, fait par quelqu'un avec la main sur
  le matériel — c'est l'axe C de `PLANNING.md`), et ce qui se passe à chaque commande
  envoyée par un utilisateur normal en usage courant. Décision reportée volontairement
  (2026-08-07) — à trancher plus tard, pas une erreur à corriger maintenant.
- **Étape 5 : les défauts s'appliquent-ils vraiment sans aucune action ?** Ou reste-t-il
  une forme d'accusé de réception implicite (le simple fait d'ouvrir l'aperçu) ? Pas
  encore précisé.

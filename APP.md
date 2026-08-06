# APP — spécification produit

Application Android de traduction langage naturel → macro ETC Eos, avec injection OSC
vers la console.

État : **conception en cours**. Ce fichier ne contient que ce qui est décidé ou imposé
par des faits techniques établis. Le reste est marqué ouvert.

**Avant de développer l'interface**, lire [`REGLES_POUR_UI.md`](REGLES_POUR_UI.md) : les
neuf règles de la grammaire Eos qui contraignent l'UI, et ce que chacune impose. Ce
fichier-ci dit *quoi construire* ; celui-là dit *pourquoi ça ne peut pas être construit
autrement*.

Dernière mise à jour : 2026-08-06.

---

## Décisions

| Date | Décision | Portée |
|---|---|---|
| 2026-08-01 | **Saisie texte d'abord.** La saisie vocale reste au programme, mais après. | Entrée utilisateur |
| 2026-08-01 | **Trois écrans parallèles** : saisie/traduction/envoi, favoris, paramètres. | Structure |
| 2026-08-01 | **La programmation complexe ne se fait pas en jeu.** Envois confirmés et sauvegardés. | Usage |
| 2026-08-01 | Perte de connexion : **l'app tente de se reconnecter** automatiquement. | Réseau |
| 2026-08-01 | Console qui refuse : **proposer une correction bien visible** avant renvoi. | Écran 1 |
| 2026-08-01 | Favoris : **option en paramètres** — envoi immédiat ou après confirmation. | Écrans 2 et 3 |
| 2026-08-01 | Favoris **organisables par onglets** (thématique ou par spectacle). | Écran 2 |
| 2026-08-01 | **Sauvegarde partageable** + export des favoris par mail ou message. | Données |
| 2026-08-01 | Commande envoyée non acquittée : **jamais rejouée automatiquement**. | Réseau |
| 2026-08-01 | Favori importé d'un autre spectacle : **signalé, jamais bloqué**. | Données |
| 2026-08-01 | Export : **les deux formats** — texte lisible et fichier ré-importable. | Données |
| 2026-08-01 | **La console fait autorité sur sa propre syntaxe.** Un refus n'est jamais contesté. | Principe |

**Conséquence de conception à ne pas perdre** : la voix arrivera plus tard sur la même
chaîne. La couche de compréhension ne doit donc jamais supposer une entrée propre — la
dictée apportera des approximations (homophones, ponctuation absente, nombres écrits en
toutes lettres). Concevoir dès maintenant pour une entrée bruitée évite de tout reprendre.

---

## Flux de référence

```
saisie texte  →  compréhension  →  génération macro  →  APERÇU + avertissements
                                                              ↓ confirmation
                                                        envoi OSC  →  retour console
```

L'**aperçu avant envoi n'est pas négociable** : une partie de la grammaire Eos reste non
validée au banc réel (voir `PLANNING.md`), et le générateur sait déjà signaler ce sur quoi
il n'est pas sûr (`grammar/`). L'app doit transmettre cet avertissement à l'utilisateur,
jamais l'avaler.

---

## Les trois écrans

Thème sombre obligatoire sur les trois (salle noire, aucun aplat clair).

### 1. Saisie — atelier de préparation

Pas un écran de jeu : la programmation complexe se fait hors représentation. Peut donc
se permettre d'être bavard et prudent.

- Champ de saisie en langage naturel.
- La macro générée s'affiche en grand, **toujours au même endroit**, avec ses
  avertissements s'il y en a.
- Envoi **toujours confirmé**. Si la macro porte un ⚠ (syntaxe non validée au banc),
  la confirmation passe en plein écran — impossible de l'envoyer distraitement.
- Retour console affiché : acceptée, ou refusée. **En cas de refus, la correction
  proposée est mise bien en évidence** — l'utilisateur la valide avant renvoi, jamais
  de renvoi automatique.
- **Aucune option de renvoyer la commande refusée telle quelle.** La console fait
  autorité sur sa propre syntaxe : la renvoyer à l'identique la ferait refuser à
  l'identique. Les deux issues possibles sont *corriger et renvoyer*, ou *reformuler
  la demande* — si la correction proposée ne convient pas, c'est que l'intention a été
  mal comprise en amont.
- Bouton **Sauvegarder en favori**, actif seulement après un envoi accepté.

### 2. Favoris — le seul écran de jeu

Le seul écran utilisé en représentation. Donc : grandes cibles tactiles, une main,
lisible dans le noir, aucun texte superflu.

- **Onglets** en haut : regroupement thématique ou par spectacle, au choix de
  l'utilisateur.
- Grille de tuiles, une par macro favorite, avec son libellé en clair.
- Un appui = envoi. Comportement réglé en paramètres : **envoi immédiat** ou **après
  confirmation**.
- **Aucun ⚠ ne peut apparaître ici** : une macro n'entre dans les favoris qu'après
  avoir été acceptée par la console depuis l'écran 1. Les favoris sont propres par
  construction.
- Réorganisation des tuiles et des onglets hors jeu uniquement.

### 3. Paramètres

- Connexion : adresse IP de la console, port (3032 par défaut), état de la connexion.
- **User# dédié** de l'app (voir contraintes ci-dessous).
- **Comportement des favoris** : envoi immédiat, ou après confirmation.
- Gestion des favoris et des onglets : renommer, supprimer, réordonner.
- **Sauvegarde / partage** : export et import (voir ci-dessous).
- Plus tard : activation de la saisie vocale.

---

## Reconnexion

L'app tente de se reconnecter automatiquement en cas de perte de connexion, et affiche
son état en permanence.

**Une commande envoyée mais non acquittée n'est jamais rejouée automatiquement.** Si la
connexion tombe entre l'envoi et l'accusé de réception, l'app ne peut pas savoir si la
console a exécuté la commande — la rejouer risquerait un double déclenchement en pleine
représentation. Elle est représentée à l'utilisateur, qui décide.

---

## Sauvegarde et partage

- **Sauvegarde partageable** de la configuration favoris (tuiles + onglets).
- **Export par mail ou message, sous deux formes simultanées** :
  - *texte lisible* dans le corps du message — pour discuter avec un collègue, relire,
    copier une ligne à la main ;
  - *fichier ré-importable* en pièce jointe — pour installer tel quel.

Deux garde-fous :

- L'export **ne contient pas les paramètres de connexion** (IP console, User#) — ils
  sont propres à chaque installation et n'ont aucun sens ailleurs.
- Les macros favorites référencent des **numéros propres à une conduite** (palette 5,
  groupe 12, cue 47). Importées sur un autre spectacle, elles restent syntaxiquement
  valides mais pointent vers autre chose. L'import le **signale sans bloquer** : c'est
  l'utilisateur qui sait si la numérotation correspond.

---

## La console fait autorité

Sur sa propre syntaxe, la console a toujours raison — c'est le même principe que la
hiérarchie de confiance du corpus, où l'observation au banc réel (S) prime sur le manuel
et sur toute déduction.

Conséquence exploitable, et l'asymétrie compte :

- **Un refus est une preuve définitive.** La syntaxe est invalide, sans appel. L'app ne
  doit jamais offrir de passer outre.
- **Une acceptation prouve moins.** Elle établit que la commande est *syntaxiquement*
  valide — pas qu'elle fait ce que l'utilisateur voulait. Une commande valide peut agir
  sur les mauvais circuits.

C'est exactement pourquoi une macro n'entre dans les favoris qu'après acceptation *et*
validation visuelle par l'utilisateur en salle.

---

## Contraintes techniques établies

Issues du corpus et du journal terrain — non négociables, déjà vérifiées.

- **Transport** : OSC sur TCP, port 3032. Reproduit par `reference/tools/fakeeos.ts`.
- **Envoi** : ligne de commande texte via `/eos/cmd` ou `/eos/newcmd`.
- **User# dédié et fixe** à assigner dès la connexion, pour ne pas interférer avec
  l'opérateur travaillant sur la console (corpus, §11.4 de la grammaire consolidée).
- **Burst d'état initial** émis par la console à la connexion : à absorber avant tout
  envoi.
- **Retour d'erreur** exploitable sur `/eos/out/cmd` : l'app peut savoir si la console a
  refusé la syntaxe, et le dire à l'utilisateur.
- **Même réseau** que la console (Wi-Fi du théâtre).

---

## Ouvert

- Apparence concrète des trois écrans (maquette à produire).
- **Dépendance banc réel** : la correction proposée en cas de refus suppose que le
  message d'erreur de la console soit assez précis pour être exploité. À vérifier —
  le simulateur ne renvoie pas d'erreur réaliste. Si le message s'avère trop pauvre,
  l'app signalera le refus sans pouvoir proposer de correction.
- **Enregistrement d'un record target sans scope de channels explicite — l'app doit
  demander.** Trouvé le 2026-08-03 en testant une traduction réelle (« créer les palettes
  couleur 1 à 6, Lee, chaud/froid/rouge/vert/bleu/jaune ») : la demande ne précisait aucun
  channel. `Record Color Palette` capture l'état de la sélection courante, ou de tous les
  channels non-défaut si rien n'est sélectionné (rarement l'intention réelle) — voir
  `grammar/modele.yaml` § palettes. Le traducteur ne doit jamais choisir cette portée à la
  place de l'utilisateur : c'est une **question à poser en écran 1**, pas une valeur par
  défaut à deviner. Deux réponses possibles à proposer : une sélection précise (« quels
  circuits ? »), ou `{By Type}` (palette générique réutilisable sur tout fixture du même
  type, sans dépendre de channels précis — manuel §10). Motif générique, pas propre aux
  palettes couleur : vaut pour tout Record sans sélection explicite dans la phrase
  d'origine (presets, palettes de toute famille, submasters).

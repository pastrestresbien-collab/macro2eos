# APP — spécification produit

Application Android de traduction langage naturel → macro ETC Eos, avec injection OSC
vers la console.

État : **conception en cours**. Ce fichier ne contient que ce qui est décidé ou imposé
par des faits techniques établis. Le reste est marqué ouvert.

Dernière mise à jour : 2026-08-01.

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
- **Export par mail ou message.**

Deux garde-fous à concevoir :

- L'export **ne contient pas les paramètres de connexion** (IP console, User#) — ils
  sont propres à chaque installation et n'ont aucun sens ailleurs.
- Les macros favorites référencent des **numéros propres à une conduite** (palette 5,
  groupe 12, cue 47). Importées sur un autre spectacle, elles restent syntaxiquement
  valides mais pointent vers autre chose. L'import doit le signaler.

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

## Ouvert — à trancher avec l'usage réel

- Format de l'export : texte lisible dans le corps du message, fichier ré-importable,
  ou les deux ?
- Un favori importé d'un autre spectacle doit-il être bloqué, ou seulement signalé ?
- **Dépendance banc réel** : la correction proposée en cas de refus suppose que le
  message d'erreur de la console soit assez précis pour être exploité. À vérifier —
  le simulateur ne renvoie pas d'erreur réaliste.

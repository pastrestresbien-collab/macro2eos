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
- Retour console affiché : acceptée, ou refusée avec le message d'erreur.
- Bouton **Sauvegarder en favori**, actif seulement après un envoi accepté.

### 2. Favoris — le seul écran de jeu

Le seul écran utilisé en représentation. Donc : grandes cibles tactiles, une main,
lisible dans le noir, aucun texte superflu.

- Grille de tuiles, une par macro favorite, avec son libellé en clair.
- Un appui = envoi. Confirmation légère (l'appui long, ou une confirmation immédiate
  annulable), pas de dialogue bloquant.
- **Aucun ⚠ ne peut apparaître ici** : une macro n'entre dans les favoris qu'après
  avoir été acceptée par la console depuis l'écran 1. Les favoris sont propres par
  construction.
- Réorganisation des tuiles hors jeu uniquement.

### 3. Paramètres

- Connexion : adresse IP de la console, port (3032 par défaut), état de la connexion.
- **User# dédié** de l'app (voir contraintes ci-dessous).
- Gestion des favoris : renommer, supprimer, réordonner.
- Plus tard : activation de la saisie vocale.

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

- Gestion de la connexion perdue en pleine représentation.
- Que faire quand la console refuse la syntaxe : proposer une correction, ou rendre la
  main ?
- Confirmation sur l'écran Favoris : appui long, ou envoi immédiat annulable ?
- Les favoris doivent-ils être organisables par spectacle / conduite ?

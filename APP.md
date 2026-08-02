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

- Apparence et ergonomie de l'écran principal.
- Comportement en situation de conduite (urgence, obscurité, une seule main).
- Gestion de la connexion perdue en pleine représentation.
- Historique des commandes envoyées, rejeu, favoris.
- Que faire quand la console refuse la syntaxe : proposer une correction, ou rendre la
  main ?

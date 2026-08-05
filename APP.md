# APP — spécification produit

Application Android de traduction langage naturel → macro ETC Eos, avec injection OSC
vers la console.

État : **conception en cours**. Ce fichier ne contient que ce qui est décidé ou imposé
par des faits techniques établis. Le reste est marqué ouvert.

Dernière mise à jour : 2026-08-05.

---

## Décisions

| Date | Décision | Portée |
|---|---|---|
| 2026-08-01 | **Saisie texte d'abord.** La saisie vocale reste au programme, mais après. | Entrée utilisateur |
| 2026-08-01 | **Trois écrans parallèles** : saisie/traduction/envoi, favoris, paramètres. *(Les trois écrans demeurent ; leur accès est hiérarchisé depuis le 2026-08-05 — voir « Navigation ».)* | Structure |
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
| 2026-08-03 | Macro mal comprise (pas refusée, juste fausse) : **correction ciblée par champ** en tapant l'élément en cause, en complément — jamais en remplacement — de la reformulation complète. | Écran 1 |
| 2026-08-03 | Commande partie sans accusé pendant une coupure : **représentée à l'utilisateur avec un rejeu manuel explicite**, jamais automatique. | Écran 1 / Réseau |
| 2026-08-03 | Import d'un favori d'un autre spectacle : **signalement tuile par tuile** au moment de l'import, jamais un blocage global. | Écran 3 |
| 2026-08-03 | Favoris : **modifiables (libellé), duplicables, supprimables, déplaçables vers un autre onglet**, via un mode édition explicite hors jeu. | Écran 2 |
| 2026-08-03 | **Bibliothèque de macros** issue du corpus, accessible depuis l'écran 1 : remplit le champ de saisie, ne court-circuite jamais l'aperçu. | Écran 1 |
| 2026-08-03 | **Historique des envois** journalisé en paramètres, avec une qualité par entrée (acceptée / a levé un doute / refusée / en suspens). | Écran 3 |
| 2026-08-05 | **Navigation hiérarchisée, pas trois pairs.** Barre du bas réduite à deux destinations (Favoris, Saisie) ; Historique et Réglages montent dans l'en-tête. | Navigation |
| 2026-08-05 | **Mode jeu** : sur Favoris, réduit l'app à la grille de tuiles — barre du bas masquée, édition impossible. | Écran 2 |

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
- **Correction ciblée par champ**, avant envoi. La macro générée n'est pas un bloc de
  texte inerte : chaque élément que le parseur a reconnu (type de cible, numéro) reste
  identifiable et corrigible individuellement — appui sur le "5" pour changer un chiffre,
  appui sur "Group" pour choisir une autre fonction proche (circuit / groupe / palette /
  preset...) dans un petit menu. Objectif : rattraper une mauvaise interprétation du
  langage naturel par une retouche ciblée, sans tout retaper. Ça reste un complément au
  bouton **Modifier la demande**, jamais un remplacement — si rien n'a été reconnu du
  tout, ou si l'erreur est plus profonde qu'un champ, on reformule. Idée reprise du
  corpus (`notes_produit_futures.md`) ; **dépend de l'axe A de la grammaire** pour la
  liste des alternatives plausibles par champ — voir `Ouvert`.
- **Bibliothèque de macros**, accessible depuis l'écran 1 (pas un quatrième écran).
  Une sélection de motifs tirés du corpus communautaire et des manuels officiels — ceux
  qui reviennent le plus souvent et qui rendent service au-delà d'un spectacle
  particulier (nettoyage de show, bump de sub, effet symétrique, highlight/lowlight...).
  Point important : appuyer sur une entrée **remplit le champ de saisie en langage
  naturel**, pas la macro générée directement. La bibliothèque propose une formulation
  et sa source (corpus communautaire ou manuel, avec le niveau de confiance déjà en
  usage dans le dépôt), mais **repasse par le même chemin que toute demande** —
  compréhension, génération, aperçu, avertissements. Elle ne court-circuite jamais
  l'aperçu avant envoi : une raccourci de formulation, pas d'envoi. Les numéros qu'elle
  cite (groupe 1, sub 3, preset 9997...) sont des exemples à adapter, comme pour un
  favori importé d'un autre spectacle.

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
- Réorganisation des tuiles et des onglets hors jeu uniquement, via un **mode édition
  explicite** — jamais accessible par un appui simple sur une tuile, pour ne rien risquer
  pendant le jeu.
- En mode édition, chaque tuile favorite est **modifiable, duplicable, supprimable, et
  déplaçable vers un autre onglet** :
  - *Modifier* ne touche que le libellé affiché — la macro elle-même, déjà acceptée par
    la console, ne se réédite pas ici (retour à l'écran 1 pour changer le fond).
  - *Dupliquer* sert à décliner une variante (ex. « Contre chaud » → « Contre froid »)
    sans repartir de zéro à l'écran 1.
  - *Déplacer vers un onglet* recatégorise une tuile sans la recréer.
  - *Supprimer* retire la tuile ; la macro n'existe alors plus que dans l'historique
    des envois (voir écran 3), pas comme favori.
  - Signal visuel cohérent avec l'écran 1 : en mode édition, les tuiles portent une
    bordure en tirets — le même langage visuel que les champs corrigibles par tap.

### 3. Paramètres

- Connexion : adresse IP de la console, port (3032 par défaut), état de la connexion.
- **User# dédié** de l'app (voir contraintes ci-dessous).
- **Comportement des favoris** : envoi immédiat, ou après confirmation.
- Gestion des favoris et des onglets : renommer, supprimer, réordonner.
- **Historique des envois** : chaque macro générée depuis l'écran 1 est journalisée avec
  l'horodatage, la ligne envoyée, et une **qualité** qui reprend le vocabulaire déjà en
  usage ailleurs dans l'app plutôt que d'en inventer un nouveau :
  - *Acceptée · déjà connue* — syntaxe qui ne portait pas de ⚠ au moment de l'envoi.
  - *Acceptée · a levé un doute* — partait avec un ⚠ (syntaxe non validée au banc), et
    l'acceptation par la console vient d'en apporter la preuve pour ce cas précis.
  - *Refusée* — avec la correction proposée si la console en a fourni une exploitable,
    et si la commande a fini par passer après correction.
  - *En suspens* — envoyée sans accusé de réception (coupure réseau), avec l'issue une
    fois que l'utilisateur a tranché (rejouée / laissée telle quelle).
  - Consultation seule : l'historique ne renvoie rien, il documente ce qui a déjà été
    fait. Une entrée acceptée peut être sauvegardée en favori a posteriori si elle ne
    l'a pas été sur le moment.
- **Sauvegarde / partage** : export et import (voir ci-dessous).
- Plus tard : activation de la saisie vocale.

---

## Navigation

Les trois écrans restent les trois écrans. Ce qui change, c'est qu'ils ne sont pas
**atteints** de la même façon : leur fréquence d'usage et leur niveau de risque vont de
« constante, en pleine représentation » à « une fois par installation ». Les traiter en
pairs dans une barre d'onglets revenait à nier la seule chose que ce produit sait de son
usage.

Le raisonnement tient en une observation : **le pouce se pose en bas de l'écran.** Sur
l'écran de jeu, en salle noire, une main, tout ce qui se trouve à cet endroit et
n'envoie pas de macro est un risque — sortir de la grille de tuiles en plein spectacle
coûte bien plus cher que d'atteindre les réglages une seconde plus tard.

Trois rôles, donc :

- **Destinations** — barre du bas, grandes cibles : **Favoris** et **Saisie**, les deux
  seules choses qu'on *fait*. Favoris en premier, du côté où le pouce se pose.
- **Utilitaires** — en-tête, en haut, hors de la zone du pouce : **Historique** et
  **Réglages**. Consultables depuis n'importe où sans détour, et le retour ramène là
  d'où l'on vient. C'est aussi ce qui corrige un défaut réel : l'historique enregistre
  les envois de Favoris autant que ceux de Saisie, il n'avait aucune raison d'être
  enfermé derrière l'atelier.
- **Satellites** — rattachés à un écran précis et atteints depuis lui seul : la
  bibliothèque appartient à Saisie (elle remplit son champ), la gestion des onglets et
  l'import appartiennent aux Réglages.

### Mode jeu

Le prolongement logique de « réorganisation hors jeu uniquement » : ce qui valait pour
l'édition vaut pour la navigation. Activé depuis Favoris avant que la salle s'éteigne,
il réduit l'app à ce qui sert en représentation :

- barre du bas **masquée** — plus rien sous le pouce que des tuiles ;
- édition, ajout d'onglet et ajout de favori **indisponibles** ;
- onglets **toujours commutables** — changer d'onglet fait partie du jeu ;
- mode d'envoi rappelé **en lecture seule** : on ne découvre jamais en plein spectacle
  qu'il n'était pas celui qu'on croyait, et on ne peut pas le changer d'un doigt qui
  traîne ;
- état de la console toujours visible, et une sortie explicite en haut de l'écran.

Ce mode est un garde-fou, pas un verrou : la sortie est immédiate, en un appui, loin
du pouce. Rien ne doit jamais empêcher quelqu'un de reprendre la main sur sa conduite.

---

## Reconnexion

L'app tente de se reconnecter automatiquement en cas de perte de connexion, et affiche
son état en permanence.

**Une commande envoyée mais non acquittée n'est jamais rejouée automatiquement.** Si la
connexion tombe entre l'envoi et l'accusé de réception, l'app ne peut pas savoir si la
console a exécuté la commande — la rejouer risquerait un double déclenchement en pleine
représentation. Elle est représentée à l'utilisateur, qui décide.

Concrètement : tant que la reconnexion n'a pas abouti, un bandeau ambre reste affiché
en permanence (pas une alerte ponctuelle qu'on referme). La commande en suspens reste
visible avec ses deux issues explicites — **rejouer maintenant** (une fois la console
reconnectée, action volontaire) ou **laisser telle quelle** (l'utilisateur a vérifié à
l'œil sur scène que c'est fait, ou pas). Aucune des deux n'est un état par défaut : tant
qu'aucun choix n'est fait, la commande reste affichée comme en attente.

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

Concrètement, le signalement se fait **tuile par tuile** dans l'écran d'import, pas
comme un avertissement générique en tête de liste : chaque favori importé qui référence
un numéro affiche son badge « autre spectacle », les autres n'en portent pas. L'import
reste **groupé** (tout ou rien pour le lot importé) — seul le signalement est individuel.

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

- **Maquette** : `app/maquette.html` couvre maintenant les trois écrans et leurs
  principales variantes (refus, reconnexion/commande en attente, confirmation plein
  écran, correction ciblée par champ, import inter-spectacle, mode édition des favoris,
  bibliothèque de macros, historique des envois). Reste en apparence d'intention, pas
  des pixels définitifs — à affiner encore à l'usage.
- **Prototype** : `app/prototype.html` — un seul appareil, navigation réelle entre les
  trois écrans, état qui change vraiment (favoris, historique, onglets...). Le moteur de
  traduction NL → macro y est un module de démonstration à vocabulaire volontairement
  limité (quelques motifs reconnus), pas une préfiguration du futur moteur — seuls la
  navigation et les enchaînements d'écrans font foi.
- **Bibliothèque de macros — sélection à revoir avec l'axe A.** Les cinq entrées de la
  maquette sont choisies à la main dans le corpus (motifs qui reviennent, pas un vote de
  popularité qui n'existe pas dans les sources). Une fois l'axe A avancé, la sélection
  et le tri pourraient s'appuyer sur des critères plus systématiques (fréquence
  d'occurrence dans le corpus, niveau de confiance, statut « motif directement
  réutilisable » déjà relevé par endroits) plutôt que sur un choix éditorial ponctuel.
- **Correction ciblée par champ — dépendance axe A** : le motif d'interaction (taper un
  élément reconnu, choisir parmi des alternatives proches) est fixé côté app. Mais la
  liste des alternatives plausibles par champ doit venir de la grammaire structurée
  (`grammar/`, axe A de `PLANNING.md`) — le modèle actuel ne l'expose pas encore. Tant
  que ce n'est pas branché, la maquette montre le motif avec des alternatives d'exemple,
  pas une liste réellement dérivée du modèle.
- **Dépendance banc réel** : la correction proposée en cas de refus suppose que le
  message d'erreur de la console soit assez précis pour être exploité. À vérifier —
  le simulateur ne renvoie pas d'erreur réaliste. Si le message s'avère trop pauvre,
  l'app signalera le refus sans pouvoir proposer de correction.

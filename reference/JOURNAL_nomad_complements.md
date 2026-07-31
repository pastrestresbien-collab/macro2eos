# Compléments au journal d'observations terrain (au-delà de la vague 28 du corpus)

Date : 2026-07-31
Source : [`JOURNAL_observations_nomad.md`](JOURNAL_observations_nomad.md) — journal complet (1017 lignes)
du projet connexe **xtouch2Eos** (pont MIDI/OSC entre un contrôleur Behringer X-Touch Compact
et une console Eos). La vague 28 du corpus (`corpus/CORPUS_EOS_COMPLET.md`, entrées #136-145)
avait déjà extrait les dix observations les plus pertinentes de ce journal. Ce document complète
avec ce qui n'y figurait pas et qui est **directement utile au moteur d'injection OSC/ASCII**
du projet macro2eos (pas au reste du journal, largement dédié à la cartographie MIDI du
contrôleur physique, hors périmètre du traducteur NL→macro).

Niveau de confiance : **S** (observation directe et datée sur nomad réel, comme pour la vague 28)
sauf mention contraire.

---

## Déclenchement de macro par OSC — confirmé et précisé (recoupe et complète le manuel v3.2.0)

- **Adresse confirmée par capture de trafic OSC réelle (Cy, 2026-07-17)** : `/eos/macro/<n>/fire`
  — "documentée dans HANDOFF_Claude-Code_Pont-MIDI-OSC.md depuis la recherche initiale du
  projet, PAS une invention de cette session".
- **Confirmation croisée indépendante** : la table officielle « OSC Macro » du chapitre 31
  (Show Control) de l'Eos Family User Manual v3.2.0 (`manuals/operations-manual/31-show-control.md`)
  documente exactement la même famille d'adresses, avec un niveau de détail supérieur :

  | OSC Method | Arguments | Exemple |
  |---|---|---|
  | `/eos/macro` | numéro de macro à **sélectionner** | `/eos/macro=1` |
  | `/eos/macro/fire` | numéro de macro à **exécuter** | `/eos/macro/fire=1` |
  | `/eos/macro/<number>/fire` | argument optionnel front de bouton : `1.0`=appui, `0.0`=relâchement | `/eos/macro/1/fire=1.0` |

- **Impact direct pour macro2eos** : c'est la commande OSC normative pour déclencher une macro
  déjà enregistrée sur la console. Niveau de confiance **A** (source officielle du manuel,
  confirmée indépendamment par observation terrain).

## Assert : confirmation qu'il n'existe PAS de mot-clé de ligne de commande dédié

- **Piste éliminée avec preuve** : `/eos/newcmd "Sub n Assert#"` → **erreur de syntaxe**
  confirmée au banc (constat du 2026-07-07, re-testé le 2026-07-16). « Assert » est une
  fonction de touche/contexte console, **pas un mot-clé de ligne de commande** injectable via
  `newcmd`/`cmd`.
- **Contournement trouvé** (spécifique au contexte fader OSC, pas à la ligne de commande
  générale) : `/eos/user/1/fader/1/<n>/stop` (trigger 1.0/0.0) réalise la fonction Assert
  attendue pour un sub piloté via banque de faders OSC.
- **Impact pour le référentiel de risques du corpus** : renforce et précise l'entrée déjà connue
  sur `Assert` (cf. section 5 "Submasters & faders" de `GRAMMAIRE_CONSOLIDEE.md`) — à traiter
  comme **commande hors du langage de ligne de commande générable en `newcmd`**, contrairement
  à la plupart des autres fonctions du corpus. Si le traducteur doit un jour générer une action
  "Assert" via macro, il faudra passer par la séquence de touches console normale
  (`[Cue]`/`[Sub]` + `[Assert]`), pas par une construction de chaîne de commande.

## Syntaxe des molettes nommées (`wheel coarse/fine/home`) — confirmée au banc

- `/eos/user/1/wheel/coarse/<param>` — rotation normale (relative)
- `/eos/user/1/wheel/fine/<param>` — rotation en précision (encodeur poussé)
- `/eos/param/<param>/home` — remise à zéro/valeur par défaut du paramètre (**famille d'adresse
  différente** de `wheel`, ne pas confondre — erreur initialement commise dans le journal,
  corrigée par capture réelle le 2026-07-17)
- Casse exacte confirmée par capture : minuscules pour paramètres à un mot (`zoom`, `intens`,
  `red`), Title Case pour paramètres à plusieurs mots (`Shutter Strobe`, `X Focus`)
- **Pertinence pour macro2eos** : périphérique au cœur du projet (génération de macros), mais
  utile si le traducteur doit un jour piloter des paramètres en continu plutôt que par valeur
  absolue (`Chan X At Y`) — confirme une troisième famille de syntaxe OSC (`/eos/param/.../home`,
  `/eos/user/.../wheel/...`) distincte de `/eos/chan`, `/eos/cmd`, `/eos/key/...` déjà bien
  couvertes par ailleurs.

## Liste de commandes validées contre eosKeys.ts (aucune inventée)

Le pont expose une liste fermée de 15 commandes directes puisées dans `reference/eosKeys.ts`,
chacune vérifiée présente avant intégration : **Go, Stop/Back, Blackout, Record, Update, Clear,
Enter, Escape, Full, Home, Out, Live, Blind, Next, Last**. Confirme la méthode de validation
déjà retenue pour macro2eos (toujours vérifier contre `eosKeys.ts`/la table officielle avant de
qualifier une commande de valide) — aucune découverte nouvelle de syntaxe ici, mais une
confirmation de discipline méthodologique partagée entre les deux projets.

## Ce qui n'a PAS été repris (hors périmètre macro2eos)

Le reste du journal (~90 % du contenu) couvre la cartographie MIDI du contrôleur physique
X-Touch Compact (CC des encodeurs, notes des boutons, gestion des anneaux LED, pagination
d'encodeurs, verrous de session du configurateur web, packaging Electron) — sujets propres au
pont matériel xtouch2Eos, sans rapport direct avec la génération de macros Eos en langage
naturel. Conservé uniquement dans le fichier source complet pour traçabilité.

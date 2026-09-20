# Journal d'observations testées au banc — effects-workbook

Recettes construites et vérifiées sur console réelle, en complément du
workbook officiel (`EosFamily_Effects_Intensive_v3.0.1.md`). Ce fichier
n'est PAS une conversion de document source ETC — ne pas le confondre avec
le workbook, qui doit rester une conversion fidèle et intacte.

---

## 2026-09-20 — Effet absolu « un seul projecteur allumé à la fois »

Objectif : dans une sélection de projecteurs, un seul allumé à un instant
donné, les autres éteints, en boucle.

Construction (testée et confirmée au banc, Effet 101 « un seul projo a la
fois ») :

- Type : **Absolu**
- Action 1 : Niveau = **ArrPlan** (Background), Time = 0, Maintien (Dwell) = 1
- Action 2 : Niveau = **0.0**, Time = 0, Maintien (Dwell) = 0
- Temps Cycle : 1 (ajusté selon le nombre de projecteurs et la vitesse voulue)
- Durée : Infini
- **Grouper : Spread** (chaque channel agit individuellement — voir manuel
  §GROUPING, `EosFamily_Effects_Intensive_v3.0.1.md:917-950`. Grouping 1 fait
  l'inverse : tous les channels bougent ensemble)
- **Trail : Solo** (chaque groupe/channel joue l'effet en entier avant que
  le suivant ne commence — manuel §TRAIL/SOLO, l.971-974 : « The first group
  will do the entire effect on its own. The next group will start when the
  previous has finished. One at a time! »)

### Point NON documenté dans le manuel, déduit puis confirmé au banc

L'ordre des deux actions est déterminant. Le manuel décrit, pour un
mécanisme voisin (Break Mode, l.814-815) : « The last action becomes the
"background" as the other actions chase over » — un channel qui n'est pas
en train de jouer son tour se repose au niveau de la **dernière action**.

- Premier essai : Action 1 = 0, Action 2 = ArrPlan → repos = ArrPlan
  (allumé). Résultat observé : tous allumés, un seul s'éteint puis se
  rallume à tour de rôle. **Pas** l'effet voulu.
- Correction : inverser l'ordre → Action 1 = ArrPlan, Action 2 = 0 → repos
  = 0 (éteint). Résultat confirmé au banc : tous éteints, un seul s'allume
  puis se réteint à tour de rôle. **C'est l'effet voulu.**

Cette dépendance à l'ordre des actions pour le mode Trail Solo n'est
énoncée nulle part explicitement dans le workbook pour Solo — seule
l'analogie avec Break Mode le laissait prévoir. À traiter comme confirmé
par le test (confiance S), mais sans citation manuel directe pour Solo.

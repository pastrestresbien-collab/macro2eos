# Comparaison eosKeys.ts vs table officielle « Eos OSC Keys » (manuel v3.2.0)

Date : 2026-07-31
Confiance : A (les deux sources sont officielles — `eosKeys.ts` extrait du PDF ETC « Eos OSC Keys.pdf »,
la table du manuel provient du chapitre 31 « Show Control » de l'Eos Family User Manual v3.2.0)

## Méthode

Comparaison automatique des 1155 entrées de [`eosKeys.ts`](eosKeys.ts) contre les 1160 lignes de la
table « Eos OSC Keys » extraite de [`manuals/operations-manual/31-show-control.md`](../manuals/operations-manual/31-show-control.md#eos-osc-keys).

## Résultat global

- **1152 entrées communes, strictement identiques** (nom OSC + commande interne).
- 3 entrées communes avec une différence de libellé mineure (voir ci-dessous).
- 8 entrées présentes uniquement dans le manuel, 3 uniquement dans `eosKeys.ts`.

C'est un très haut niveau de cohérence entre les deux sources — le fichier `eosKeys.ts` reste
globalement fiable comme référence rapide, mais **la table du chapitre 31 du manuel doit être
traitée comme la source la plus à jour** en cas de divergence (v3.2.0, 2023-04, plus récente
que la source du PDF `eosKeys.ts`).

## Résolution d'une question ouverte du corpus (#148)

Le corpus (`corpus/CORPUS_EOS_COMPLET.md`, vague 29, entrée #148) notait que `Isn't In` et
`Could Be` (vus dans l'image de liste native, vague 12) étaient absents de `eosKeys.ts`, et
laissait ouvert s'il s'agissait de softkeys contextuels non exposés en OSC ou d'une erreur de
transcription.

**Résolution partielle, confirmée par le manuel officiel v3.2.0** :

| Terme du corpus | Statut confirmé |
|---|---|
| `isn't_in` → `ISNT_IN` | **Existe réellement comme touche OSC nommée**, présente dans le manuel officiel mais absente de `eosKeys.ts` (probablement omise à l'extraction, l'apostrophe ayant pu perturber le parsing du PDF source) |
| `can't_be` → `CANT_BE` | **Existe réellement comme touche OSC nommée**, même situation : présente dans le manuel, absente de `eosKeys.ts` |
| `could_be` | **Absent des deux sources officielles** (ni le manuel ni `eosKeys.ts`) — confirme l'hypothèse déjà posée dans le corpus : ce n'est probablement pas une touche OSC nommée indépendamment, mais un softkey contextuel de l'écran Query sans exposition OSC directe |

**Action recommandée** : traiter `isn't_in` et `can't_be` comme confirmés niveau A pour toute
validation syntaxique — `eosKeys.ts` doit être complété avec ces deux entrées, ou la table du
manuel utilisée en complément pour la validation.

## Autres écarts observés

### Dérive de terminologie « console » vs « desk » (deux paires)

| Manuel v3.2.0 (2023) | eosKeys.ts (PDF source antérieur) | Commande interne commune |
|---|---|---|
| `console_settings` | `desk_settings` | `DESK_SETTINGS` |
| `reset_console_settings` | `reset_desk_settings` | `RESET_DESK_SETTINGS` |

Les deux noms OSC partagent la même commande interne. Hypothèse la plus probable : ETC a
renommé la terminologie publique de « desk » vers « console » entre la version source du PDF
`eosKeys.ts` et le manuel v3.2.0, sans changer le comportement interne. **Non vérifié au banc** :
on ne sait pas si l'ancien nom (`desk_settings`) reste accepté par les versions récentes du
logiciel ou s'il a été remplacé. À tester si le moteur de génération doit choisir entre les deux.

### Trois entrées présentes uniquement dans le manuel (nouvelles ou omises à l'extraction)

- `encoder_custom` → `ENCODER_CUSTOM`
- `paramcategory` → `PARAM_CAT_PRE_v1_9_8` (le suffixe suggère une touche de compatibilité
  ascendante pour versions antérieures à 1.9.8 — probablement peu pertinente pour un usage moderne)

### Ambiguïté non résolue : `duration` apparaît deux fois avec deux commandes internes différentes

Dans la table officielle du manuel, `duration` apparaît deux fois consécutivement :

```
duration    EFFECT_DURATION
duration    DURATION_NUM_CYCLES
```

**Ceci pourrait être une nouvelle instance du phénomène de polysémie contextuelle déjà identifié
dans le corpus** (vague 32 #161, vague 33 #162 — `At`/`@` changeant de sens selon l'écran actif,
Patch vs Live). Si `duration` désigne bien deux commandes différentes selon le contexte
(probablement écran Effects vs un autre contexte), c'est cohérent avec ce pattern déjà établi.
**Alternative plus prosaïque** : simple doublon de mise en page dans le document source (déjà
observé pour d'autres listes de softkeys, cf. corpus vague 11 #075 sur les doublons de pages).
**Non tranché — à vérifier au banc ou en recoupant avec le contexte exact du manuel autour de
chaque occurrence.**

### Différences d'annotation mineures (pas de vrai conflit)

- `go_0` : manuel = « GO (Master Fader) », eosKeys.ts = « GO » — précision contextuelle ajoutée
  par le manuel, cohérente avec la résolution déjà actée du conflit corpus #145/#146 (`go_0` = GO,
  pas Stop/Back).
- `go` : manuel = « PLAYBACK_GO (Master Fader) », eosKeys.ts = « PLAYBACK_GO » — même cas.

## Fichiers concernés

- [`eosKeys.ts`](eosKeys.ts) — fichier fourni tel quel par le projet xtouch2Eos, non modifié
- [`manuals/operations-manual/31-show-control.md`](../manuals/operations-manual/31-show-control.md) — table source de comparaison (section « Eos OSC Keys »)
- `corpus/CORPUS_EOS_COMPLET.md` — entrée #148 (vague 29) à mettre à jour avec cette résolution

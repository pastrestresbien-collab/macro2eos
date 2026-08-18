// llm_bridge.js — moteur flou, phase 2 : appel réseau réel vers l'API Claude
// (BYOK, clé personnelle de l'utilisateur — voir Réglages). AUCUNE dépendance
// Pyodide ici : ce module tourne en JS pur, avant même que la question
// « le moteur réel est-il prêt ? » se pose.
//
// Rôle strict de ce module, et rien de plus (voir le plan moteur flou) :
//
//   1. Prendre les Question déjà posées par le traducteur déterministe
//      (`window.traduireReel` a déjà tourné, en local, sans réseau — c'est LUI
//      qui décide ce qui reste ambigu, jamais le LLM).
//   2. Demander au LLM de choisir, pour chacune de ces questions, PARMI LES
//      OPTIONS DÉJÀ CONNUES (Option.cle) — jamais une valeur inventée. Le
//      schéma JSON envoyé à l'API restreint chaque champ à un `enum` construit
//      à partir des options réelles de la question correspondante.
//   3. Revalider la réponse ici, en JS, avant de la laisser approcher Python —
//      toute valeur hors du vocabulaire de sa question rejette la réponse
//      ENTIÈRE (voir `Traducteur.interpreter_flou` et le plan : rejet simple
//      et sûr pour cette phase, quitte à être trop strict).
//
// Ce module ne lit JAMAIS localStorage lui-même (clé API, modèle...) — ça
// reste la responsabilité de app/prototype.html, pour que l'appel réseau
// reste une fonction pure et injectable (voir `opts.appelReseau`, utilisé par
// les tests pour fixer une réponse sans jamais toucher le réseau).
//
// Repli : toute erreur d'ici (réseau, timeout, JSON invalide, hors vocabulaire)
// est une exception JS normale. `askEngineFlou()` (app/prototype.html) l'attrape
// et retombe sur `askEngine()` inchangé — jamais de gestion d'erreur ici.

(function () {
  "use strict";

  var BASE = (function () {
    var scripts = document.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; i++) {
      if (/llm_bridge\.js(\?|$)/.test(scripts[i].src)) {
        return scripts[i].src.replace(/llm_bridge\.js(\?.*)?$/, "");
      }
    }
    return "./";
  })();

  var API_URL = "https://api.anthropic.com/v1/messages";
  var API_VERSION = "2023-06-01";
  var MODELE_DEFAUT = "claude-sonnet-5";
  var TIMEOUT_DEFAUT_MS = 7000;
  var OUTIL_NOM = "resoudre_ambiguites";

  var _vocabPromise = null;

  // Le vocabulaire est mis en cache une fois obtenu (stable tant que
  // lexique.yaml ne change pas), mais un ÉCHEC n'est jamais mis en cache :
  // une coupure réseau passagère (le cas normal quand le téléphone rejoint
  // le Wi-Fi de la console, voir plus haut) ne doit pas condamner le moteur
  // flou pour le reste de la session — la tentative suivante doit pouvoir
  // réessayer une fois la connexion revenue.
  function chargerVocabulaire() {
    if (_vocabPromise) return _vocabPromise;
    _vocabPromise = fetch(BASE + "data/vocabulaire_llm.json").then(function (res) {
      if (!res.ok) throw new Error("échec de chargement du vocabulaire (HTTP " + res.status + ")");
      return res.json();
    }).catch(function (err) {
      _vocabPromise = null;
      throw err;
    });
    return _vocabPromise;
  }

  function instructions() {
    return [
      "Tu aides à traduire des phrases en français vers des macros de console",
      "lumière ETC Eos. Tu ne dois JAMAIS inventer de mot, de synonyme ou de",
      "valeur : tu choisis uniquement parmi les options déjà proposées pour",
      "chaque question, listées ci-dessous avec leurs libellés. Le vocabulaire",
      "général joint sert seulement de contexte pour comprendre le domaine —",
      "il ne redéfinit pas les options valides de chaque question.",
      "",
      "Pour chaque question, réponds avec la ou les clés d'options (`cle`) qui",
      "correspondent le mieux à la phrase de l'utilisateur. Si tu n'es pas sûr,",
      "propose plusieurs clés plutôt que d'en choisir une seule au hasard — un",
      "humain tranchera. Si aucune option ne correspond, n'inclus simplement pas",
      "cette question dans ta réponse : ne force jamais une clé qui ne convient",
      "pas. Si un mot précis de la phrase semblait pertinent pour répondre à une",
      "question mais qu'aucune option ne le couvre (ex. une couleur ou un style",
      "que tu ne reconnais pas parmi les clés proposées), liste-le dans",
      "`mots_hors_lexique` — ça aide à repérer les trous du vocabulaire, ce",
      "n'est jamais une clé inventée.",
    ].join(" ");
  }

  function messageUtilisateur(phrase, questions) {
    var bloc = questions.map(function (q) {
      var options = q.options.map(function (o) {
        return "  - " + o.cle + (o.libelle ? " : " + o.libelle : "") + (o.detail ? " (" + o.detail + ")" : "");
      }).join("\n");
      return "Question « " + q.id + " » — " + q.texte + "\nOptions possibles :\n" + options;
    }).join("\n\n");

    return (
      "Phrase de l'utilisateur : « " + phrase + " »\n\n" +
      "Questions laissées en suspens par le moteur déterministe :\n\n" + bloc
    );
  }

  function construireSchema(questions) {
    var proprietes = {};
    questions.forEach(function (q) {
      var cles = q.options.map(function (o) { return o.cle; });
      proprietes[q.id] = {
        description: q.texte,
        anyOf: [
          { type: "string", enum: cles },
          { type: "array", items: { type: "string", enum: cles }, minItems: 1 },
        ],
      };
    });
    return {
      type: "object",
      properties: {
        reponses: {
          type: "object",
          properties: proprietes,
          additionalProperties: false,
        },
        mots_hors_lexique: {
          type: "array",
          items: { type: "string" },
          description: "Mots de la phrase pertinents pour une question mais absents des options fournies — jamais une clé inventée, un simple signal de trou de vocabulaire.",
        },
      },
      required: ["reponses"],
    };
  }

  // Revalide strictement la sortie du LLM contre les options RÉELLES de
  // chaque question (jamais contre le vocabulaire général) — c'est la seule
  // source de vérité sur ce qui est acceptable, exactement celle que
  // `Traducteur.interpreter_flou` réutilisera côté Python.
  //
  // Retourne soit `{ ok: true, reponses }`, soit `{ ok: false, questionId,
  // candidat }` — le détail du rejet sert à construire une observation pour
  // le journal de renforcement (voir `traducteur/observations_llm.yaml`),
  // jamais à assouplir la validation elle-même.
  function validerReponses(reponsesLlm, questions) {
    var parId = {};
    questions.forEach(function (q) {
      parId[q.id] = q.options.map(function (o) { return o.cle; });
    });

    var out = {};
    for (var id in reponsesLlm) {
      if (!Object.prototype.hasOwnProperty.call(reponsesLlm, id)) continue;
      var clesValides = parId[id];
      if (!clesValides) return { ok: false, questionId: id, candidat: reponsesLlm[id] }; // question inconnue — jamais vue, réponse suspecte

      var propose = reponsesLlm[id];
      var candidats = Array.isArray(propose) ? propose : [propose];
      for (var i = 0; i < candidats.length; i++) {
        if (clesValides.indexOf(candidats[i]) === -1) {
          return { ok: false, questionId: id, candidat: candidats[i] }; // hors vocabulaire de CETTE question
        }
      }
      out[id] = propose;
    }
    return { ok: true, reponses: out };
  }

  async function appelReseauParDefaut(requete, apiKey, timeoutMs) {
    var controller = new AbortController();
    var timer = setTimeout(function () { controller.abort(); }, timeoutMs);
    try {
      var res = await fetch(API_URL, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-api-key": apiKey,
          "anthropic-version": API_VERSION,
          "anthropic-dangerous-direct-browser-access": "true",
        },
        body: JSON.stringify(requete),
        signal: controller.signal,
      });
      if (!res.ok) {
        throw new Error("réponse HTTP " + res.status + " de l'API Claude");
      }
      return await res.json();
    } finally {
      clearTimeout(timer);
    }
  }

  // API publique. `questions` = `base.questions` déjà obtenu localement via
  // `window.traduireReel(phrase, reponses)` — jamais reconstruit ici.
  // `opts` : { apiKey (requis), model, timeoutMs, appelReseau (injectable,
  // pour les tests — voir test_llm_bridge.js) }.
  // Résout vers `{ reponses: {...} }`, au même format que `sortie_llm` attendu
  // par `Traducteur.interpreter_flou`. Rejette (throw) sur tout problème —
  // charge à l'appelant de retomber sur `askEngine()`.
  window.interpreterLlm = async function (phrase, questions, opts) {
    opts = opts || {};
    if (!opts.apiKey) throw new Error("clé API absente");
    if (!questions || !questions.length) throw new Error("aucune question à résoudre");

    var vocabulaire = await chargerVocabulaire();
    var schema = construireSchema(questions);

    var requete = {
      model: opts.model || MODELE_DEFAUT,
      max_tokens: 512,
      system: [
        { type: "text", text: instructions() },
        {
          type: "text",
          text: "Vocabulaire général du domaine (contexte, pas la liste des réponses valides) :\n" + JSON.stringify(vocabulaire),
          cache_control: { type: "ephemeral" },
        },
      ],
      messages: [{ role: "user", content: messageUtilisateur(phrase, questions) }],
      tools: [{
        name: OUTIL_NOM,
        description: "Restitue les réponses choisies pour les questions laissées en suspens, une clé d'option par question au maximum sauf indécision.",
        input_schema: schema,
      }],
      tool_choice: { type: "tool", name: OUTIL_NOM },
    };

    var appelReseau = opts.appelReseau || appelReseauParDefaut;
    var reponseApi = await appelReseau(requete, opts.apiKey, opts.timeoutMs || TIMEOUT_DEFAUT_MS);

    var contenu = reponseApi && reponseApi.content;
    var blocOutil = Array.isArray(contenu) && contenu.find(function (b) {
      return b.type === "tool_use" && b.name === OUTIL_NOM;
    });
    if (!blocOutil || !blocOutil.input || typeof blocOutil.input.reponses !== "object") {
      throw new Error("réponse LLM sans sortie structurée exploitable");
    }

    var validation = validerReponses(blocOutil.input.reponses, questions);
    if (!validation.ok) {
      var erreur = new Error("valeur hors vocabulaire dans la réponse LLM : " + JSON.stringify(validation.candidat));
      // Détail structuré pour le journal de renforcement (§ Réglages →
      // « Exporter les observations ») — l'appelant peut l'ignorer et se
      // contenter du repli silencieux habituel, `catch (e) {}` reste valide.
      erreur.observation = {
        type: "candidat_rejete",
        sortieLlmBrute: blocOutil.input,
        motOuExpression: String(validation.candidat),
      };
      throw erreur;
    }

    var motsHorsLexique = Array.isArray(blocOutil.input.mots_hors_lexique)
      ? blocOutil.input.mots_hors_lexique.filter(function (m) { return typeof m === "string" && m; })
      : [];

    return { reponses: validation.reponses, mots_hors_lexique: motsHorsLexique };
  };

  // ---------------------------------------------------------------------
  // Discussion libre (phase 5 du plan moteur flou) — va-et-vient à plusieurs
  // tours pour affiner une demande vague, PAS un remplacement du mécanisme
  // Question/Option strict ci-dessus. Différence de nature, pas de degré :
  //
  //   - Ici, le LLM ne touche JAMAIS à l'IR ni à une clé du vocabulaire —
  //     il ne produit que du FRANÇAIS LIBRE (son message affiché) et,
  //     optionnellement, une phrase française candidate. Cette phrase
  //     candidate est traitée EXACTEMENT comme si l'utilisateur l'avait
  //     tapée lui-même : elle repasse par `window.traduireReel`, qui reste
  //     seul juge de ce qu'elle veut dire. Rien de nouveau à valider ici —
  //     c'est ça qui rend cette fonctionnalité sûre malgré sa liberté : la
  //     confiance accordée au LLM est nulle, la confiance accordée à une
  //     phrase française ordinaire est celle, déjà éprouvée, du traducteur.
  //   - Pas de schéma JSON restreint par un vocabulaire fermé : rien ne
  //     serait sensé à y restreindre, puisque la sortie n'est jamais une clé
  //     du lexique, juste une conversation.
  function instructionsDiscussion() {
    return [
      "Tu aides un régisseur lumière à préciser une demande en français pour",
      "une console ETC Eos, par une conversation à plusieurs tours. Tu ne dois",
      "JAMAIS produire de syntaxe Eos toi-même (jamais de nom de touche, jamais",
      "une commande) — ton seul rôle est d'aider à formuler une PHRASE FRANÇAISE",
      "précise que le traducteur déterministe pourra comprendre. Utilise le",
      "vocabulaire général joint pour savoir ce que le corpus connaît déjà,",
      "mais ne le récite jamais tel quel : pose des questions naturelles, ou",
      "propose plusieurs formulations si plusieurs interprétations sont",
      "plausibles (« tu veux dire A, ou plutôt B ? »).",
      "",
      "Dès que tu penses avoir une formulation prête à essayer, mets-la dans",
      "`phrase_a_essayer` — elle sera immédiatement testée contre le vrai",
      "traducteur et son résultat (compris, à préciser, ou pas compris) te",
      "sera donné au tour suivant pour continuer la discussion si besoin.",
      "N'hésite pas à en proposer plusieurs, à des tours différents, si la",
      "première ne donne pas ce que l'utilisateur attend.",
    ].join(" ");
  }

  // `historique` : [{ role: "user"|"assistant"|"erreur", texte: string }, ...]
  // — le premier élément est toujours la demande d'origine de l'utilisateur.
  // Les tours "erreur" (panne réseau affichée dans le fil, voir
  // `avancerDiscussion` dans app/prototype.html) sont exclus : ce sont des
  // notices purement côté client, jamais envoyées à l'API. Et l'API Anthropic
  // attend des rôles strictement alternés (user/assistant) — deux tours
  // "user" consécutifs (ex. après une panne : la question restée sans
  // réponse, puis le message suivant de l'utilisateur) sont donc FUSIONNÉS
  // en un seul message plutôt que rejetés ou coupés en deux appels.
  function messagesDiscussion(historique) {
    var out = [];
    historique.forEach(function (tour) {
      if (tour.role !== "user" && tour.role !== "assistant") return;
      var texte = String(tour.texte || "");
      var dernier = out[out.length - 1];
      if (dernier && dernier.role === tour.role) {
        dernier.content += "\n\n" + texte;
      } else {
        out.push({ role: tour.role, content: texte });
      }
    });
    return out;
  }

  var OUTIL_DISCUSSION = "repondre_discussion";

  // `type: ["string", "null"]` (union de types) a longtemps semblé la façon
  // naturelle de coder « optionnel » ici — mais l'API Claude rejette un
  // `input_schema` de tool avec un `type` en tableau (HTTP 400
  // invalid_request_error). Jamais détecté avant : toute la suite de tests
  // (voir test_llm_bridge.js) stubbe `appelReseau`, donc ce schéma n'avait
  // jamais atteint l'API réelle avant un test en conditions réelles le
  // 2026-08-18. Corrigé en `string` simple — absence de formulation prête =
  // chaîne vide, jamais `null` (voir `discuterLlm` plus bas, qui traite déjà
  // une chaîne vide comme absence de phrase).
  function construireSchemaDiscussion() {
    return {
      type: "object",
      properties: {
        message: {
          type: "string",
          description: "Réponse en français naturel, affichée telle quelle à l'utilisateur — jamais de syntaxe Eos.",
        },
        phrase_a_essayer: {
          type: "string",
          description: "Une phrase française à tester immédiatement contre le vrai traducteur, ou une chaîne vide si tu préfères d'abord poser ta question.",
        },
      },
      required: ["message"],
    };
  }

  // API publique. `historique` construit et maintenu par l'appelant (voir
  // ci-dessus). `opts` : { apiKey (requis), model, timeoutMs, appelReseau
  // (injectable, pour les tests) }. Résout vers { message, phraseAEssayer }.
  // Rejette (throw) sur tout problème réseau — repli visible côté appelant
  // (pas silencieux ici : contrairement à `interpreterLlm`, l'utilisateur a
  // explicitement demandé cette réponse, il doit savoir si elle a échoué).
  window.discuterLlm = async function (historique, opts) {
    opts = opts || {};
    if (!opts.apiKey) throw new Error("clé API absente");
    if (!historique || !historique.length) throw new Error("historique de discussion vide");

    var vocabulaire = await chargerVocabulaire();

    var requete = {
      model: opts.model || MODELE_DEFAUT,
      max_tokens: 700,
      system: [
        { type: "text", text: instructionsDiscussion() },
        {
          type: "text",
          text: "Vocabulaire général du domaine (contexte, pour comprendre ce que le corpus connaît déjà) :\n" + JSON.stringify(vocabulaire),
          cache_control: { type: "ephemeral" },
        },
      ],
      messages: messagesDiscussion(historique),
      tools: [{
        name: OUTIL_DISCUSSION,
        description: "Restitue la réponse à afficher et, en option, une phrase française à tester tout de suite contre le vrai traducteur.",
        input_schema: construireSchemaDiscussion(),
      }],
      tool_choice: { type: "tool", name: OUTIL_DISCUSSION },
    };

    var appelReseau = opts.appelReseau || appelReseauParDefaut;
    var reponseApi = await appelReseau(requete, opts.apiKey, opts.timeoutMs || TIMEOUT_DEFAUT_MS);

    var contenu = reponseApi && reponseApi.content;
    var blocOutil = Array.isArray(contenu) && contenu.find(function (b) {
      return b.type === "tool_use" && b.name === OUTIL_DISCUSSION;
    });
    if (!blocOutil || !blocOutil.input || typeof blocOutil.input.message !== "string" || !blocOutil.input.message) {
      throw new Error("réponse LLM sans message exploitable");
    }

    var phrase = blocOutil.input.phrase_a_essayer;
    return {
      message: blocOutil.input.message,
      phraseAEssayer: typeof phrase === "string" && phrase.trim() ? phrase.trim() : null,
    };
  };

  // Exposé pour les tests uniquement (construction de requête isolée du réseau).
  window._llmBridgeInterne = {
    construireSchema: construireSchema,
    validerReponses: validerReponses,
    messageUtilisateur: messageUtilisateur,
    messagesDiscussion: messagesDiscussion,
  };
})();

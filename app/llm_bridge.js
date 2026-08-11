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

  function chargerVocabulaire() {
    if (_vocabPromise) return _vocabPromise;
    _vocabPromise = fetch(BASE + "data/vocabulaire_llm.json").then(function (res) {
      if (!res.ok) throw new Error("échec de chargement du vocabulaire (HTTP " + res.status + ")");
      return res.json();
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
      "pas.",
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
      },
      required: ["reponses"],
    };
  }

  // Revalide strictement la sortie du LLM contre les options RÉELLES de
  // chaque question (jamais contre le vocabulaire général) — c'est la seule
  // source de vérité sur ce qui est acceptable, exactement celle que
  // `Traducteur.interpreter_flou` réutilisera côté Python.
  function validerReponses(reponsesLlm, questions) {
    var parId = {};
    questions.forEach(function (q) {
      parId[q.id] = q.options.map(function (o) { return o.cle; });
    });

    var out = {};
    for (var id in reponsesLlm) {
      if (!Object.prototype.hasOwnProperty.call(reponsesLlm, id)) continue;
      var clesValides = parId[id];
      if (!clesValides) return null; // question inconnue — jamais vue, réponse suspecte

      var propose = reponsesLlm[id];
      var candidats = Array.isArray(propose) ? propose : [propose];
      for (var i = 0; i < candidats.length; i++) {
        if (clesValides.indexOf(candidats[i]) === -1) return null; // hors vocabulaire de CETTE question
      }
      out[id] = propose;
    }
    return out;
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

    var reponsesValidees = validerReponses(blocOutil.input.reponses, questions);
    if (!reponsesValidees) {
      throw new Error("valeur hors vocabulaire dans la réponse LLM");
    }
    return { reponses: reponsesValidees };
  };

  // Exposé pour les tests uniquement (construction de requête isolée du réseau).
  window._llmBridgeInterne = {
    construireSchema: construireSchema,
    validerReponses: validerReponses,
    messageUtilisateur: messageUtilisateur,
  };
})();

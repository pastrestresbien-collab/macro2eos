#!/usr/bin/env node
// Non-régression de app/llm_bridge.js (moteur flou, phase 2).
//
// Aucun appel réseau réel : `appelReseau` est injecté avec des réponses
// fixées (voir le plan moteur flou, § Stratégie de test — « llm_bridge.js
// structuré pour que l'appel réseau soit une fonction injectable »). Seul
// `fetch` du vocabulaire (app/data/vocabulaire_llm.json) est stubé, avec le
// vrai fichier compilé — jamais une copie à la main qui pourrait diverger.
//
//     node app/test_llm_bridge.js
"use strict";

const fs = require("fs");
const path = require("path");

const VOCAB = JSON.parse(
  fs.readFileSync(path.join(__dirname, "data", "vocabulaire_llm.json"), "utf8")
);

// llm_bridge.js est un script de navigateur classique (pas un module
// CommonJS) : il référence `window`/`document`/`fetch` comme variables
// globales. `global.window = global` fait que `window.interpreterLlm = ...`
// et `global.interpreterLlm` sont la même propriété, exactement comme dans
// un vrai navigateur où `window` EST l'objet global.
global.window = global;
global.document = { getElementsByTagName: function () { return []; } };
global.fetch = function (url) {
  if (String(url).indexOf("vocabulaire_llm.json") !== -1) {
    return Promise.resolve({ ok: true, json: function () { return Promise.resolve(VOCAB); } });
  }
  return Promise.reject(new Error("fetch non stubé pour " + url));
};
global.AbortController = function () { this.signal = {}; };
global.AbortController.prototype.abort = function () {};

eval(fs.readFileSync(path.join(__dirname, "llm_bridge.js"), "utf8"));

let echecs = 0;
function controler(nom, obtenu, attendu) {
  const a = JSON.stringify(obtenu), b = JSON.stringify(attendu);
  if (a === b) return true;
  console.log("  ÉCHEC — " + nom);
  console.log("    attendu : " + b);
  console.log("    obtenu  : " + a);
  echecs++;
  return false;
}

const questions = [
  {
    id: "bump_direction", texte: "Dans quel sens ?", pourquoi: "",
    options: [{ cle: "haut", libelle: "Bump Up" }, { cle: "bas", libelle: "Bump Down" }],
  },
];

async function main() {
  const schema = window._llmBridgeInterne.construireSchema(questions);
  controler("schéma — options de la question reprises telles quelles (jamais inventées)",
    schema.properties.reponses.properties.bump_direction.anyOf[0].enum, ["haut", "bas"]);

  controler("validation — candidat unique valide",
    window._llmBridgeInterne.validerReponses({ bump_direction: "haut" }, questions),
    { ok: true, reponses: { bump_direction: "haut" } });

  controler("validation — hors vocabulaire de la question -> rejet détaillé",
    window._llmBridgeInterne.validerReponses({ bump_direction: "gauche" }, questions),
    { ok: false, questionId: "bump_direction", candidat: "gauche" });

  controler("validation — question jamais posée par le lexique -> rejet détaillé",
    window._llmBridgeInterne.validerReponses({ inconnue: "x" }, questions),
    { ok: false, questionId: "inconnue", candidat: "x" });

  controler("validation — plusieurs candidats valides, tous conservés",
    window._llmBridgeInterne.validerReponses({ bump_direction: ["haut", "bas"] }, questions),
    { ok: true, reponses: { bump_direction: ["haut", "bas"] } });

  const sortie = await window.interpreterLlm("bump le sub 5 vers le haut", questions, {
    apiKey: "sk-test",
    appelReseau: function () {
      return Promise.resolve({
        content: [{ type: "tool_use", name: "resoudre_ambiguites", input: { reponses: { bump_direction: "haut" } } }],
      });
    },
  });
  controler("interpreterLlm — bout en bout, réponse valide", sortie,
    { reponses: { bump_direction: "haut" }, mots_hors_lexique: [] });

  const sortieAvecTrou = await window.interpreterLlm("bump le sub 5 en douceur cuivrée", questions, {
    apiKey: "sk-test",
    appelReseau: function () {
      return Promise.resolve({
        content: [{ type: "tool_use", name: "resoudre_ambiguites",
          input: { reponses: { bump_direction: "haut" }, mots_hors_lexique: ["cuivrée"] } }],
      });
    },
  });
  controler("interpreterLlm — signale un mot hors vocabulaire sans jamais l'inventer comme réponse",
    sortieAvecTrou, { reponses: { bump_direction: "haut" }, mots_hors_lexique: ["cuivrée"] });

  let rejeteeHorsVocab = false, observationRejet = null;
  try {
    await window.interpreterLlm("bump le sub 5", questions, {
      apiKey: "sk-test",
      appelReseau: function () {
        return Promise.resolve({
          content: [{ type: "tool_use", name: "resoudre_ambiguites", input: { reponses: { bump_direction: "gauche" } } }],
        });
      },
    });
  } catch (e) { rejeteeHorsVocab = true; observationRejet = e.observation; }
  controler("interpreterLlm — valeur hors vocabulaire -> rejeté (repli attendu côté appelant)", rejeteeHorsVocab, true);
  controler("interpreterLlm — rejet hors vocabulaire porte une observation exploitable (journal de renforcement)",
    observationRejet && observationRejet.type, "candidat_rejete");

  let appele = false, rejeteeSansCle = false;
  try {
    await window.interpreterLlm("bump le sub 5", questions, {
      appelReseau: function () { appele = true; return Promise.resolve({ content: [] }); },
    });
  } catch (e) { rejeteeSansCle = true; }
  controler("interpreterLlm — sans clé API -> jamais d'appel réseau",
    { rejetee: rejeteeSansCle, appele: appele }, { rejetee: true, appele: false });

  let reseauEnPanne = false;
  try {
    await window.interpreterLlm("bump le sub 5", questions, {
      apiKey: "sk-test",
      appelReseau: function () { return Promise.reject(new Error("hors ligne")); },
    });
  } catch (e) { reseauEnPanne = true; }
  controler("interpreterLlm — panne réseau -> rejet propagé (repli côté appelant, cas normal en régie)",
    reseauEnPanne, true);

  // ---- discuterLlm (discussion libre, plusieurs tours) ----

  controler("messagesDiscussion — rôles user/assistant conservés tels quels",
    window._llmBridgeInterne.messagesDiscussion([
      { role: "user", texte: "bump un sub" },
      { role: "assistant", texte: "lequel, et dans quel sens ?" },
      { role: "user", texte: "le 5, vers le haut" },
    ]),
    [
      { role: "user", content: "bump un sub" },
      { role: "assistant", content: "lequel, et dans quel sens ?" },
      { role: "user", content: "le 5, vers le haut" },
    ]);

  controler("messagesDiscussion — un rôle inconnu (ex. futur type de tour) est exclu, jamais envoyé à l'API",
    window._llmBridgeInterne.messagesDiscussion([
      { role: "user", texte: "bump un sub" },
      { role: "inconnu", texte: "ceci ne doit jamais atteindre l'API" },
      { role: "assistant", texte: "lequel ?" },
    ]),
    [
      { role: "user", content: "bump un sub" },
      { role: "assistant", content: "lequel ?" },
    ]);

  controler("messagesDiscussion — tour 'erreur' exclu, et deux tours user consécutifs fusionnés",
    window._llmBridgeInterne.messagesDiscussion([
      { role: "user", texte: "je veux quelque chose pour l'entracte" },
      { role: "erreur", texte: "panne réseau — jamais envoyée à l'API" },
      { role: "user", texte: "un noir sur le sub 9" },
    ]),
    [
      { role: "user", content: "je veux quelque chose pour l'entracte\n\nun noir sur le sub 9" },
    ]);

  const discussionOk = await window.discuterLlm(
    [{ role: "user", texte: "je veux quelque chose pour l'entracte" }],
    {
      apiKey: "sk-test",
      appelReseau: function () {
        return Promise.resolve({
          content: [{
            type: "tool_use", name: "repondre_discussion",
            input: { message: "Tu penses à un noir, ou à un état particulier ?", phrase_a_essayer: null },
          }],
        });
      },
    }
  );
  controler("discuterLlm — question sans phrase à essayer", discussionOk,
    { message: "Tu penses à un noir, ou à un état particulier ?", phraseAEssayer: null });

  const discussionAvecPhrase = await window.discuterLlm(
    [
      { role: "user", texte: "je veux quelque chose pour l'entracte" },
      { role: "assistant", texte: "Tu penses à un noir, ou à un état particulier ?" },
      { role: "user", texte: "un noir sur le sub 9" },
    ],
    {
      apiKey: "sk-test",
      appelReseau: function () {
        return Promise.resolve({
          content: [{
            type: "tool_use", name: "repondre_discussion",
            input: { message: "Je te propose : « sub 9 à 0 » — c'est bien ça ?", phrase_a_essayer: " sub 9 à 0 " },
          }],
        });
      },
    }
  );
  controler("discuterLlm — phrase à essayer proposée, espaces superflus retirés",
    discussionAvecPhrase, { message: "Je te propose : « sub 9 à 0 » — c'est bien ça ?", phraseAEssayer: "sub 9 à 0" });

  let discussionSansMessage = false;
  try {
    await window.discuterLlm([{ role: "user", texte: "test" }], {
      apiKey: "sk-test",
      appelReseau: function () {
        return Promise.resolve({ content: [{ type: "tool_use", name: "repondre_discussion", input: {} }] });
      },
    });
  } catch (e) { discussionSansMessage = true; }
  controler("discuterLlm — réponse sans message exploitable -> rejeté", discussionSansMessage, true);

  let discussionAppele = false, discussionRejeteeSansCle = false;
  try {
    await window.discuterLlm([{ role: "user", texte: "test" }], {
      appelReseau: function () { discussionAppele = true; return Promise.resolve({ content: [] }); },
    });
  } catch (e) { discussionRejeteeSansCle = true; }
  controler("discuterLlm — sans clé API -> jamais d'appel réseau",
    { rejetee: discussionRejeteeSansCle, appele: discussionAppele }, { rejetee: true, appele: false });

  let discussionSansHistorique = false;
  try {
    await window.discuterLlm([], { apiKey: "sk-test", appelReseau: function () { return Promise.resolve({ content: [] }); } });
  } catch (e) { discussionSansHistorique = true; }
  controler("discuterLlm — historique vide -> rejeté sans appel réseau", discussionSansHistorique, true);

  // Garde-fou de non-régression : l'API Claude rejette (HTTP 400) tout
  // `input_schema` de tool où un `type` est un tableau (ex. `["string",
  // "null"]`, pourtant du JSON Schema valide) — bug réel trouvé le
  // 2026-08-18 en testant la discussion en conditions réelles, jamais
  // détecté avant car aucun test ici ne touchait le réseau. Ce garde-fou
  // inspecte la VRAIE requête construite (capturée via `appelReseau`
  // injecté), pas une copie à la main du schéma qui pourrait diverger.
  function chercherTypeEnTableau(noeud, chemin) {
    if (Array.isArray(noeud)) {
      for (let i = 0; i < noeud.length; i++) {
        const trouve = chercherTypeEnTableau(noeud[i], chemin + "[" + i + "]");
        if (trouve) return trouve;
      }
      return null;
    }
    if (noeud && typeof noeud === "object") {
      if (Array.isArray(noeud.type)) return chemin + ".type";
      for (const cle in noeud) {
        if (!Object.prototype.hasOwnProperty.call(noeud, cle)) continue;
        const trouve = chercherTypeEnTableau(noeud[cle], chemin + "." + cle);
        if (trouve) return trouve;
      }
    }
    return null;
  }
  let requeteDiscussionCapturee = null;
  await window.discuterLlm([{ role: "user", texte: "test" }], {
    apiKey: "sk-test",
    appelReseau: function (requete) {
      requeteDiscussionCapturee = requete;
      return Promise.resolve({
        content: [{ type: "tool_use", name: "repondre_discussion", input: { message: "ok", phrase_a_essayer: "" } }],
      });
    },
  });
  controler("discuterLlm — aucun `type` en tableau dans le schéma envoyé à l'API (HTTP 400 sinon)",
    chercherTypeEnTableau(requeteDiscussionCapturee.tools, "tools"), null);

  const total = 20;
  if (echecs) {
    console.log("\n" + echecs + " cas en échec sur " + total + ".");
    process.exitCode = 1;
    return;
  }
  console.log(total + " cas de llm_bridge.js — tous conformes.");
}

main();

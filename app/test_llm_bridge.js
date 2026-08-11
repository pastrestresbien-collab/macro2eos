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
    { bump_direction: "haut" });

  controler("validation — hors vocabulaire de la question -> rejet entier (null)",
    window._llmBridgeInterne.validerReponses({ bump_direction: "gauche" }, questions), null);

  controler("validation — question jamais posée par le lexique -> rejet entier (null)",
    window._llmBridgeInterne.validerReponses({ inconnue: "x" }, questions), null);

  controler("validation — plusieurs candidats valides, tous conservés",
    window._llmBridgeInterne.validerReponses({ bump_direction: ["haut", "bas"] }, questions),
    { bump_direction: ["haut", "bas"] });

  const sortie = await window.interpreterLlm("bump le sub 5 vers le haut", questions, {
    apiKey: "sk-test",
    appelReseau: function () {
      return Promise.resolve({
        content: [{ type: "tool_use", name: "resoudre_ambiguites", input: { reponses: { bump_direction: "haut" } } }],
      });
    },
  });
  controler("interpreterLlm — bout en bout, réponse valide", sortie, { reponses: { bump_direction: "haut" } });

  let rejeteeHorsVocab = false;
  try {
    await window.interpreterLlm("bump le sub 5", questions, {
      apiKey: "sk-test",
      appelReseau: function () {
        return Promise.resolve({
          content: [{ type: "tool_use", name: "resoudre_ambiguites", input: { reponses: { bump_direction: "gauche" } } }],
        });
      },
    });
  } catch (e) { rejeteeHorsVocab = true; }
  controler("interpreterLlm — valeur hors vocabulaire -> rejeté (repli attendu côté appelant)", rejeteeHorsVocab, true);

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

  const total = 9;
  if (echecs) {
    console.log("\n" + echecs + " cas en échec sur " + total + ".");
    process.exitCode = 1;
    return;
  }
  console.log(total + " cas de llm_bridge.js — tous conformes.");
}

main();

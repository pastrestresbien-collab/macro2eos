// engine.js — fait tourner le VRAI traducteur (traducteur/traducteur.py +
// grammar/generateur.py) dans le navigateur, via Pyodide (Python compilé en
// WebAssembly). Ce n'est pas un port JS de la logique : c'est le code Python
// réel, celui que `traducteur/test_traducteur.py` vérifie, exécuté tel quel.
//
// Pourquoi Pyodide plutôt qu'un port JS : la logique de traduction (tolérance
// aux fautes restreinte au créneau, détection d'intention, rendu de la
// commande avec ses avertissements...) est déjà testée et corrigée côté
// Python. La réécrire en JS aurait recréé, dans un deuxième langage, tous les
// pièges déjà trouvés et corrigés une fois — dont deux qui ont produit des
// macros fausses en session (voir PLANNING.md #35, #36).
//
// Pourquoi les données SONT du JSON et pas du YAML : `grammar/modele.yaml`
// et `traducteur/lexique.yaml` restent la source, écrite à la main. Mais les
// charger dans Pyodide demanderait le paquet PyYAML compilé en WASM (~1 Mo de
// plus, une dépendance de plus). Le JSON ne demande rien d'autre que le module
// `json` de la bibliothèque standard, déjà présent. Donc : YAML reste la
// source, JSON est l'artefact — exactement le principe déjà en place pour
// `grammar/dist/*.json` (voir grammar/README.md). Régénéré par
// `app/build_data.sh`, jamais à la main.
//
// Le "runtime" Pyodide (moteur Python) est vendu dans app/vendor/pyodide/,
// pas chargé depuis un CDN : voir la note dans app/vendor/README.md pour la
// raison (accès réseau restreint dans l'environnement de développement de ce
// projet — voir CLAUDE.md règle n°1 — donc rien ne garantissait de pouvoir le
// tester une fois téléchargé depuis un CDN externe).

(function () {
  "use strict";

  // Chemin de base : ce fichier est chargé par app/prototype.html, donc les
  // chemins relatifs ci-dessous sont résolus depuis app/.
  var BASE = (function () {
    var scripts = document.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; i++) {
      if (/engine\.js(\?|$)/.test(scripts[i].src)) {
        return scripts[i].src.replace(/engine\.js(\?.*)?$/, "");
      }
    }
    return "./";
  })();

  // -- le pont Python : instancie le vrai traducteur à partir des données
  // chargées ci-dessous, convertit ses résultats (dataclasses) en JSON. Ce
  // code est spécifique à ce prototype — ce n'est PAS une copie d'un fichier
  // du dépôt, contrairement à generateur.py/traducteur.py/les .json.
  var PY_BRIDGE = [
    "import json, sys",
    "sys.path.insert(0, '/app/grammar')",
    "sys.path.insert(0, '/app/traducteur')",
    "from generateur import Generateur",
    "from traducteur import Traducteur",
    "",
    "with open('/app/data/modele.json', encoding='utf-8') as _f:",
    "    _modele = json.load(_f)",
    "with open('/app/data/lexique.json', encoding='utf-8') as _f:",
    "    _lex = json.load(_f)",
    "",
    "_gen = Generateur(_modele)",
    "_trad = Traducteur(_lex, generateur=_gen)",
    "",
    "def _option_vers_dict(o):",
    "    return {'cle': o.cle, 'libelle': o.libelle, 'detail': o.detail,",
    "            'demande_valeur': o.demande_valeur}",
    "",
    "def _question_vers_dict(q):",
    "    return {'id': q.id, 'texte': q.texte, 'pourquoi': q.pourquoi,",
    "            'options': [_option_vers_dict(o) for o in q.options]}",
    "",
    "def _hypothese_vers_dict(h):",
    "    return {'champ': h.champ, 'valeur': h.valeur, 'pourquoi': h.pourquoi,",
    "            'correction': _question_vers_dict(h.correction)}",
    "",
    "def traduire_json(phrase, reponses_json):",
    "    reponses = json.loads(reponses_json) if reponses_json else {}",
    "    trad = _trad.traduire(phrase, reponses=reponses)",
    "    out = {",
    "        'statut': trad.statut,",
    "        'intention': trad.intention,",
    "        'notes': trad.notes,",
    "        'non_reconnus': trad.non_reconnus,",
    "        'questions': [_question_vers_dict(q) for q in trad.questions],",
    "        'hypotheses': [_hypothese_vers_dict(h) for h in trad.hypotheses],",
    "        'commande': None,",
    "        'avertissements': [],",
    "    }",
    "    if trad.compris:",
    "        rendu = _trad.rendre(trad)",
    "        out['commande'] = rendu.commande",
    "        out['avertissements'] = rendu.avertissements",
    "    return json.dumps(out, ensure_ascii=False)",
    "",
  ].join("\n");

  var _enginePromise = null;

  async function fetchText(url) {
    var res = await fetch(url);
    if (!res.ok) throw new Error("échec de chargement de " + url + " (HTTP " + res.status + ")");
    return await res.text();
  }

  function bootEngine() {
    if (_enginePromise) return _enginePromise;
    _enginePromise = (async function () {
      if (typeof loadPyodide !== "function") {
        throw new Error("pyodide.js absent — vérifier app/vendor/pyodide/");
      }
      var pyodide = await loadPyodide({ indexURL: BASE + "vendor/pyodide/" });

      var fichiers = await Promise.all([
        fetchText(BASE + "data/generateur.py"),
        fetchText(BASE + "data/traducteur.py"),
        fetchText(BASE + "data/modele.json"),
        fetchText(BASE + "data/lexique.json"),
      ]);

      pyodide.FS.mkdirTree("/app/grammar");
      pyodide.FS.mkdirTree("/app/traducteur");
      pyodide.FS.mkdirTree("/app/data");
      pyodide.FS.writeFile("/app/grammar/generateur.py", fichiers[0]);
      pyodide.FS.writeFile("/app/traducteur/traducteur.py", fichiers[1]);
      pyodide.FS.writeFile("/app/data/modele.json", fichiers[2]);
      pyodide.FS.writeFile("/app/data/lexique.json", fichiers[3]);
      pyodide.FS.writeFile("/app/py_bridge.py", PY_BRIDGE);

      // `from ... import traduire_json` (et pas seulement `import py_bridge`) :
      // il faut que le nom soit directement dans les globals Python pour que
      // `pyodide.globals.get("traduire_json")` le trouve depuis JS.
      pyodide.runPython(
        "import sys\nsys.path.insert(0, '/app')\nfrom py_bridge import traduire_json\n"
      );

      window.MACRO2EOS_ENGINE_READY = true;
      return pyodide;
    })();
    _enginePromise.catch(function (err) {
      window.MACRO2EOS_ENGINE_ERROR = String((err && err.message) || err);
      console.error("moteur réel indisponible :", err);
    });
    return _enginePromise;
  }

  // API publique : { statut, intention, notes, non_reconnus, questions,
  //                  hypotheses, commande, avertissements }
  // Reflète exactement `traducteur.Traduction` + `generateur.Resultat` —
  // aucun champ n'est inventé ici, tous viennent du vrai code Python.
  window.traduireReel = async function (phrase, reponses) {
    var pyodide = await bootEngine();
    var fn = pyodide.globals.get("traduire_json");
    try {
      var out = fn(phrase, JSON.stringify(reponses || {}));
      return JSON.parse(out);
    } finally {
      fn.destroy();
    }
  };

  window.MACRO2EOS_ENGINE_READY = false;
  bootEngine();
})();

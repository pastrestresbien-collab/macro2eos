/**
 * Simulateur ETCnomad minimal pour tester le banc de test SANS nomad.
 *
 * Reproduit les comportements confirmés au banc réel (voir sources citées
 * inline) :
 *  - burst initial à la connexion TCP : show/name, user, état de cue actif,
 *    molette, sélection de canal, état live/blind (voir la fonction
 *    `envoyerBurstInitial` pour le détail et les sources)
 *  - répond à /eos/ping sur /eos/out/ping (mêmes arguments)
 *  - accuse la config de banque : /eos/fader/<b>/config/... → label + niveaux
 *  - ÉCHO FADER : un niveau reçu sur /eos/fader/<b>/<f> est renvoyé sur la
 *    même adresse (sans /out) après `--echo-delay` ms — défaut 500 ms,
 *    mesuré empiriquement à +522 ms au banc actif (corpus #139), et NON les
 *    ~3 s supposés dans l'étude de cadrage initiale (chiffre communautaire,
 *    jamais confirmé)
 *  - écho immédiat des touches sur /eos/out/key/<nom>
 *  - /eos/sub/<n> : reçu et journalisé, SANS écho — un vrai Eos ne republie
 *    jamais spontanément sur cette adresse (corpus #139,
 *    JOURNAL_observations_nomad.md), le retour d'état passe uniquement par
 *    les banques de faders
 *  - /eos/macro/<n>/fire et /eos/macro/fire : reçus et journalisés (niveau A,
 *    cf. JOURNAL_nomad_complements.md) ; aucun écho, car aucun n'est documenté
 *    ou observé pour ce déclenchement
 *  - ligne de commande (/eos/cmd, /eos/newcmd) : écho sur /eos/out/cmd ET
 *    /eos/out/user/<u>/cmd, chacun avec DEUX arguments (texte, flag_erreur_int)
 *    — format confirmé au banc actif, corpus #140. `flag_erreur_int` vaut 0
 *    par défaut (ce simulateur ne valide aucune syntaxe) ; `--erreur-pattern`
 *    permet de le forcer à 1 pour tester le chemin "refus" côté app — c'est
 *    une commodité de test, PAS un comportement observé sur un vrai Eos.
 *
 * Volontairement absent, faute de syntaxe exacte confirmée dans le corpus
 * (adresse observée en catégorie seulement, ou format d'argument non capturé) :
 * les 12 softkeys, l'état de cue précédente/en attente, /eos/out/color/hs,
 * le format exact de /eos/out/pantilt et /eos/out/xyz, /eos/out/event/locked,
 * et les événements LED (/eos/out/event/sub, /eos/out/event/cue/.../fire|stop).
 * Les inventer romprait la règle du dépôt : jamais de syntaxe non tranchée
 * présentée comme acquise (voir CLAUDE.md, `grammar/README.md`).
 *
 * ⚠ Ce simulateur ne remplace PAS la validation en conditions réelles
 * (gate de la phase 0) : R1 et R7 ne peuvent être levés que sur le vrai nomad.
 *
 * Usage : npm run fake-eos -- [--port 3032] [--framing 1.0|1.1] [--echo-delay 500] [--erreur-pattern <regex>]
 */

import { createServer, Socket } from "node:net";
import * as osc from "osc";

function cliOption(name: string): string | undefined {
  const index = process.argv.indexOf(`--${name}`);
  return index !== -1 ? process.argv[index + 1] : undefined;
}

const port = Number(cliOption("port") ?? 3032);
const framing = (cliOption("framing") ?? "1.0") as "1.0" | "1.1";
// 500 ms par défaut : mesuré à +522 ms au banc actif (corpus #139), corrige
// les "+3 s" supposés dans l'étude de cadrage initiale (jamais confirmés).
const echoDelayMs = Number(cliOption("echo-delay") ?? 500);
// Commodité de TEST, pas un comportement Eos : si la ligne de commande envoyée
// matche cette regex, flag_erreur_int est forcé à 1 dans l'écho /eos/out/cmd,
// pour exercer le chemin "refus" côté app (voir APP.md) sans vrai validateur
// de syntaxe. Aucune commande n'est refusée par défaut.
const erreurPatternRaw = cliOption("erreur-pattern");
const erreurPattern = erreurPatternRaw ? new RegExp(erreurPatternRaw) : null;

const SLIP_END = 0xc0;
const SLIP_ESC = 0xdb;
const SLIP_ESC_END = 0xdc;
const SLIP_ESC_ESC = 0xdd;

function frame(payload: Buffer): Buffer {
  if (framing === "1.0") {
    const header = Buffer.alloc(4);
    header.writeInt32BE(payload.length, 0);
    return Buffer.concat([header, payload]);
  }
  const out: number[] = [SLIP_END];
  for (const byte of payload) {
    if (byte === SLIP_END) out.push(SLIP_ESC, SLIP_ESC_END);
    else if (byte === SLIP_ESC) out.push(SLIP_ESC, SLIP_ESC_ESC);
    else out.push(byte);
  }
  out.push(SLIP_END);
  return Buffer.from(out);
}

function log(text: string): void {
  console.log(`[fake-eos] ${text}`);
}

const server = createServer((socket: Socket) => {
  log(`client connecté (${socket.remoteAddress}:${socket.remotePort})`);
  let rxBuffer = Buffer.alloc(0);

  function reply(address: string, ...args: osc.OscArgument[]): void {
    const payload = Buffer.from(osc.writeMessage({ address, args }, { metadata: true }));
    socket.write(frame(payload));
    log(`  → ${address} ${JSON.stringify(args.map((a) => a.value))}`);
  }

  // Le vrai Eos rejoue tout son état à chaque nouvelle connexion (~40 messages
  // en ~130 ms, JOURNAL_observations_nomad.md l.188-192) — c'est aussi ce qui
  // permet l'auto-détection de framing côté client (Eos parle le premier).
  // Seules les adresses ET le format d'argument confirmés par le manuel
  // officiel (chap.31 Show Control) sont reproduits ici ; voir le commentaire
  // en tête de fichier pour la liste de ce qui manque et pourquoi.
  reply("/eos/out/show/name", { type: "s", value: "fake-eos" });
  reply("/eos/out/user", { type: "i", value: 1 });
  reply("/eos/out/active/cue", { type: "f", value: 0.0 }); // aucune cue en cours
  reply("/eos/out/active/cue/text", { type: "s", value: "" });
  reply("/eos/out/active/chan", { type: "s", value: "" }); // aucun canal sélectionné
  reply("/eos/out/wheel", { type: "f", value: 0.0 }); // 0=coarse
  reply("/eos/out/switch", { type: "f", value: 0.0 });
  reply("/eos/out/event/state", { type: "i", value: 1 }); // 1=Live

  function handleMessage(msg: osc.OscMessage): void {
    log(`← ${msg.address} ${JSON.stringify(msg.args.map((a) => a.value))}`);

    if (msg.address === "/eos/ping") {
      reply("/eos/out/ping", ...msg.args);
      return;
    }

    if (msg.address === "/eos/get/version") {
      // format observé sur le vrai nomad 3.3.5 : deux strings + un int
      reply(
        "/eos/out/get/version",
        { type: "s", value: "fake-eos 0.1" },
        { type: "s", value: "0.1" },
        { type: "i", value: 0 }
      );
      return;
    }

    const configMatch = msg.address.match(/^\/eos\/fader\/(\d+)\/config\/(\d+)\/(\d+)$/);
    if (configMatch) {
      const [, bank, page, count] = configMatch;
      reply(`/eos/out/fader/${bank}`, { type: "s", value: page });
      for (let i = 1; i <= Number(count); i++) {
        reply(`/eos/out/fader/${bank}/${i}/name`, { type: "s", value: `Sub ${i}` });
      }
      return;
    }

    const levelMatch = msg.address.match(/^\/eos\/fader\/(\d+)\/(\d+)$/);
    if (levelMatch && msg.args.length > 0) {
      // écho différé, comme le vrai Eos (~3 s), sur l'adresse SANS /out
      const echoArgs = msg.args;
      setTimeout(() => reply(msg.address, ...echoArgs), echoDelayMs);
      return;
    }

    const subMatch = msg.address.match(/^\/eos\/sub\/(\d+)$/);
    if (subMatch && msg.args.length > 0) {
      // Pas d'écho ici : le journal terrain (JOURNAL_observations_nomad.md)
      // confirme qu'un vrai Eos ne republie jamais spontanément sur
      // /eos/sub/<n> — le retour d'état passe uniquement par les banques de
      // faders (/eos/out/fader/...). Republier ici serait un comportement
      // inventé, pas observé.
      return;
    }

    const macroFireMatch = msg.address.match(/^\/eos\/macro\/(\d+)\/fire$/);
    if (macroFireMatch || msg.address === "/eos/macro/fire") {
      // Adresse confirmée niveau A pour l'envoi (manuel v3.2.0 chap.31 + capture
      // de trafic réelle, cf. JOURNAL_nomad_complements.md). Aucun écho documenté
      // ou observé pour ce déclenchement : on accuse réception dans le log sans
      // inventer une adresse de retour.
      return;
    }

    const keyMatch = msg.address.match(/^\/eos\/key\/(.+)$/);
    if (keyMatch) {
      reply(`/eos/out/key/${keyMatch[1]}`, ...msg.args);
      return;
    }

    if (msg.address === "/eos/cmd" || msg.address === "/eos/newcmd") {
      const text = String(msg.args[0]?.value ?? "");
      const echo = `LIVE: ${text}`;
      // Format confirmé au banc actif (corpus #140) : (texte, flag_erreur_int),
      // diffusé à la fois sur /eos/out/cmd et /eos/out/user/<u>/cmd. flag=1
      // signifie "erreur de syntaxe" sur un vrai Eos ; ce simulateur ne valide
      // aucune syntaxe, donc flag=0 sauf si --erreur-pattern matche (commodité
      // de test, voir en tête de fichier).
      const erreur = erreurPattern !== null && erreurPattern.test(text) ? 1 : 0;
      reply("/eos/out/cmd", { type: "s", value: echo }, { type: "i", value: erreur });
      reply("/eos/out/user/1/cmd", { type: "s", value: echo }, { type: "i", value: erreur });
      return;
    }
  }

  socket.on("data", (chunk) => {
    rxBuffer = Buffer.concat([rxBuffer, chunk]);
    const packets: Buffer[] = [];
    if (framing === "1.0") {
      while (rxBuffer.length >= 4) {
        const length = rxBuffer.readInt32BE(0);
        if (length <= 0 || rxBuffer.length < 4 + length) break;
        packets.push(rxBuffer.subarray(4, 4 + length));
        rxBuffer = rxBuffer.subarray(4 + length);
      }
    } else {
      let endIndex: number;
      while ((endIndex = rxBuffer.indexOf(SLIP_END)) !== -1) {
        const raw = rxBuffer.subarray(0, endIndex);
        rxBuffer = rxBuffer.subarray(endIndex + 1);
        if (raw.length === 0) continue;
        const out: number[] = [];
        let escaped = false;
        for (const byte of raw) {
          if (escaped) {
            out.push(byte === SLIP_ESC_END ? SLIP_END : byte === SLIP_ESC_ESC ? SLIP_ESC : byte);
            escaped = false;
          } else if (byte === SLIP_ESC) escaped = true;
          else out.push(byte);
        }
        packets.push(Buffer.from(out));
      }
    }
    for (const packet of packets) {
      try {
        const decoded = osc.readPacket(packet, { metadata: true });
        if ("address" in decoded) handleMessage(decoded);
      } catch (err) {
        log(`paquet illisible : ${String(err)}`);
      }
    }
  });

  socket.on("close", () => log("client déconnecté"));
  socket.on("error", (err) => log(`erreur socket : ${err.message}`));
});

server.listen(port, "127.0.0.1", () => {
  log(`simulateur Eos en écoute sur 127.0.0.1:${port} (TCP OSC ${framing}, écho fader +${echoDelayMs} ms)`);
  if (erreurPattern) log(`  motif de refus simulé : ${erreurPattern} (commodité de test, pas un comportement Eos)`);
  log("Ctrl+C pour arrêter");
});

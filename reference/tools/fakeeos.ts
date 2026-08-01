/**
 * Simulateur ETCnomad minimal pour tester le banc de test SANS nomad.
 *
 * Reproduit les comportements documentés utiles à la phase 0 :
 *  - envoie un état initial dès la connexion TCP (comme le vrai Eos, qui
 *    diffuse show/name, cue active, softkeys, etc. — observé sur nomad 3.3.5)
 *  - répond à /eos/ping sur /eos/out/ping (mêmes arguments)
 *  - accuse la config de banque : /eos/fader/<b>/config/... → label + niveaux
 *  - ÉCHO FADER À +3 s : un niveau reçu sur /eos/fader/<b>/<f> est renvoyé
 *    3 s plus tard sur la même adresse (sans /out — comportement réel d'Eos,
 *    cf. Luminosus EosFaderBankBlock), pour valider l'anti-boucle en phase 2
 *  - écho immédiat des touches sur /eos/out/key/<nom>
 *
 * ⚠ Ce simulateur ne remplace PAS la validation en conditions réelles
 * (gate de la phase 0) : R1 et R7 ne peuvent être levés que sur le vrai nomad.
 *
 * Usage : npm run fake-eos -- [--port 3032] [--framing 1.0|1.1] [--echo-delay 3000]
 */

import { createServer, Socket } from "node:net";
import * as osc from "osc";

function cliOption(name: string): string | undefined {
  const index = process.argv.indexOf(`--${name}`);
  return index !== -1 ? process.argv[index + 1] : undefined;
}

const port = Number(cliOption("port") ?? 3032);
const framing = (cliOption("framing") ?? "1.0") as "1.0" | "1.1";
const echoDelayMs = Number(cliOption("echo-delay") ?? 3000);

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

  // le vrai Eos rejoue son état à chaque nouvelle connexion — c'est aussi ce
  // qui permet l'auto-détection de framing côté client (Eos parle le premier)
  reply("/eos/out/show/name", { type: "s", value: "fake-eos" });
  reply("/eos/out/user", { type: "i", value: 1 });

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
      const echoArgs = msg.args;
      setTimeout(() => reply(msg.address.replace("/eos/", "/eos/out/"), ...echoArgs), echoDelayMs);
      return;
    }

    const keyMatch = msg.address.match(/^\/eos\/key\/(.+)$/);
    if (keyMatch) {
      reply(`/eos/out/key/${keyMatch[1]}`, ...msg.args);
      return;
    }

    if (msg.address === "/eos/cmd" || msg.address === "/eos/newcmd") {
      const text = String(msg.args[0]?.value ?? "");
      reply("/eos/out/cmd", { type: "s", value: `LIVE: ${text}` });
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
  log("Ctrl+C pour arrêter");
});

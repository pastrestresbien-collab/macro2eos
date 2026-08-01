import { Socket } from "node:net";
import * as osc from "osc";

const sock = new Socket();

function send(address: string, args: osc.OscArgument[]) {
  const payload = Buffer.from(osc.writeMessage({ address, args }, { metadata: true }));
  const header = Buffer.alloc(4);
  header.writeInt32BE(payload.length, 0);
  sock.write(Buffer.concat([header, payload]));
  console.log("[test] envoyé:", address, JSON.stringify(args.map((a) => a.value)));
}

sock.connect(3033, "127.0.0.1", () => {
  console.log("[test] connecté");
  // Macro 1 confirmée (corpus + manuel v3.2.0 chap.31 "OSC Macro") : déclenchement
  send("/eos/macro/1/fire", [{ type: "f", value: 1.0 }]);
  setTimeout(() => send("/eos/macro/1/fire", [{ type: "f", value: 0.0 }]), 200);
  // Touche Go (eosKeys.ts: go_0 -> GO)
  setTimeout(() => send("/eos/key/go_0", []), 400);
});

let rx = Buffer.alloc(0);
sock.on("data", (chunk) => {
  rx = Buffer.concat([rx, chunk]);
  while (rx.length >= 4) {
    const len = rx.readInt32BE(0);
    if (len <= 0 || rx.length < 4 + len) break;
    const packet = rx.subarray(4, 4 + len);
    rx = rx.subarray(4 + len);
    try {
      const decoded: any = osc.readPacket(packet, { metadata: true });
      console.log("[test] reçu:", decoded.address, JSON.stringify((decoded.args || []).map((a: any) => a.value)));
    } catch (e) {
      console.log("[test] paquet illisible", e);
    }
  }
});

setTimeout(() => {
  console.log("[test] fin — aucune réponse ci-dessus pour /eos/macro/1/fire = non géré par le simulateur");
  sock.end();
  process.exit(0);
}, 2500);

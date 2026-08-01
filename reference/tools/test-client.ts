import { Socket } from "node:net";
import * as osc from "osc";

const sock = new Socket();
sock.connect(3032, "127.0.0.1", () => {
  console.log("[test] connecté");
  const cmd = 'Chan 10 Thru 20 Color 3/195 Enter';
  const payload = Buffer.from(osc.writeMessage(
    { address: "/eos/newcmd", args: [{ type: "s", value: cmd }] },
    { metadata: true }
  ));
  const header = Buffer.alloc(4);
  header.writeInt32BE(payload.length, 0);
  sock.write(Buffer.concat([header, payload]));
  console.log("[test] envoyé:", cmd);
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

setTimeout(() => { sock.end(); process.exit(0); }, 2000);

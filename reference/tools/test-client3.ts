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

const cmd1 = "Group 5 + 1 Thru 6 Color 3/195 Enter";
const cmd2 = "Record Color Palette 5 Label 195-Par LED Enter";

sock.connect(3034, "127.0.0.1", () => {
  console.log("[test] connecté");
  send("/eos/newcmd", [{ type: "s", value: cmd1 }]);
  setTimeout(() => send("/eos/newcmd", [{ type: "s", value: cmd2 }]), 300);
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

setTimeout(() => { sock.end(); process.exit(0); }, 1500);

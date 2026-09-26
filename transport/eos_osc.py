"""Client OSC/TCP minimal pour parler à Eos (ou à son simulateur `fakeeos.ts`).

Aucune dépendance externe : encode/décode OSC 1.0 à la main (stdlib uniquement),
avec le framing observé sur le simulateur et confirmé au banc (`reference/tools/`)
et dans le journal terrain (`reference/JOURNAL_observations_nomad.md`) — préfixe
de longueur 4 octets big-endian devant chaque paquet OSC.

Ne parle *que* transport : ce module ne connaît rien à la grammaire Eos. La
commande à envoyer vient de `grammar/generateur.py`.

    >>> client = EosClient("127.0.0.1", 3032)
    >>> client.connect()
    >>> client.absorber_burst_initial()
    >>> client.envoyer_commande("Chan 10 Thru 20 Color 3/195 Enter")
    >>> client.close()
"""
from __future__ import annotations

import socket
import struct
import time
from dataclasses import dataclass


def _pad4(data: bytes) -> bytes:
    """Complète `data` avec des octets nuls jusqu'au multiple de 4 suivant."""
    reste = len(data) % 4
    if reste == 0:
        return data
    return data + b"\x00" * (4 - reste)


def _encoder_chaine(valeur: str) -> bytes:
    return _pad4(valeur.encode("utf-8") + b"\x00")


def encoder_message(adresse: str, args: list) -> bytes:
    """Encode un message OSC 1.0 : adresse + tags de type + arguments.

    Types supportés : str -> 's', int -> 'i', float -> 'f' (ceux qu'utilise Eos
    dans `reference/GRAMMAIRE_ETC_EOS_CONSOLIDEE.md` §Show Control).
    """
    tags = ","
    corps = b""
    for a in args:
        if isinstance(a, str):
            tags += "s"
            corps += _encoder_chaine(a)
        elif isinstance(a, float):
            tags += "f"
            corps += struct.pack(">f", a)
        elif isinstance(a, int):
            tags += "i"
            corps += struct.pack(">i", a)
        else:
            raise TypeError(f"type OSC non supporté : {type(a)!r}")
    return _encoder_chaine(adresse) + _encoder_chaine(tags) + corps


def decoder_message(paquet: bytes) -> tuple[str, list]:
    """Décode un message OSC 1.0 en (adresse, liste d'arguments)."""

    def lire_chaine(buf: bytes, pos: int) -> tuple[str, int]:
        fin = buf.index(b"\x00", pos)
        valeur = buf[pos:fin].decode("utf-8")
        pos = fin + 1
        pos += (4 - pos % 4) % 4
        return valeur, pos

    adresse, pos = lire_chaine(paquet, 0)
    tags, pos = lire_chaine(paquet, pos)
    args: list = []
    for tag in tags[1:]:  # ignore la virgule initiale
        if tag == "s":
            valeur, pos = lire_chaine(paquet, pos)
            args.append(valeur)
        elif tag == "f":
            args.append(struct.unpack(">f", paquet[pos:pos + 4])[0])
            pos += 4
        elif tag == "i":
            args.append(struct.unpack(">i", paquet[pos:pos + 4])[0])
            pos += 4
        else:
            raise ValueError(f"tag OSC non supporté : {tag!r}")
    return adresse, args


@dataclass
class MessageRecu:
    adresse: str
    args: list


class EosClient:
    """Connexion TCP à Eos/ETCnomad (ou son simulateur), framing longueur 4 octets."""

    def __init__(self, host: str, port: int, timeout: float = 2.0) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout
        self._sock: socket.socket | None = None
        self._tampon = b""

    def connect(self) -> None:
        self._sock = socket.create_connection((self.host, self.port), timeout=self.timeout)

    def close(self) -> None:
        if self._sock is not None:
            self._sock.close()
            self._sock = None

    def envoyer(self, adresse: str, args: list) -> None:
        assert self._sock is not None, "connect() requis avant envoyer()"
        paquet = encoder_message(adresse, args)
        entete = struct.pack(">i", len(paquet))
        self._sock.sendall(entete + paquet)

    def envoyer_commande(self, commande: str, nouvelle_ligne: bool = True) -> None:
        """Envoie une ligne de commande Eos sur `/eos/newcmd` (ou `/eos/cmd`)."""
        adresse = "/eos/newcmd" if nouvelle_ligne else "/eos/cmd"
        self.envoyer(adresse, [commande])

    def _lire_octets(self, n: int, timeout: float) -> bytes | None:
        assert self._sock is not None
        self._sock.settimeout(timeout)
        while len(self._tampon) < n:
            try:
                chunk = self._sock.recv(4096)
            except (TimeoutError, socket.timeout):
                return None
            if not chunk:
                return None
            self._tampon += chunk
        donnees, self._tampon = self._tampon[:n], self._tampon[n:]
        return donnees

    def recevoir(self, timeout: float = 1.0) -> MessageRecu | None:
        """Lit un message OSC complet, ou None si rien n'arrive avant `timeout`."""
        entete = self._lire_octets(4, timeout)
        if entete is None:
            return None
        (longueur,) = struct.unpack(">i", entete)
        paquet = self._lire_octets(longueur, timeout)
        if paquet is None:
            return None
        adresse, args = decoder_message(paquet)
        return MessageRecu(adresse, args)

    def absorber_burst_initial(self, silence: float = 0.5) -> list[MessageRecu]:
        """Vide l'état initial diffusé à la connexion (APP.md, contrainte transport).

        Lit tant que des messages arrivent sans interruption > `silence` secondes.
        """
        messages: list[MessageRecu] = []
        while True:
            msg = self.recevoir(timeout=silence)
            if msg is None:
                break
            messages.append(msg)
        return messages

    def attendre_echo_cmd(self, timeout: float = 2.0) -> MessageRecu | None:
        """Attend spécifiquement l'écho `/eos/out/cmd` (accepté ou refusé)."""
        limite = time.monotonic() + timeout
        while time.monotonic() < limite:
            restant = limite - time.monotonic()
            msg = self.recevoir(timeout=max(restant, 0))
            if msg is None:
                return None
            if msg.adresse in ("/eos/out/cmd", "/eos/out/newcmd"):
                return msg
        return None

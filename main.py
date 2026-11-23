"""make.fun news-image-20261122 entry: writes the front page for Sunday 22 November 2026.

The page is drawn ahead of time by art/draw.py (Pillow) and committed as entry.png;
this program, standard library only and offline, copies those exact bytes to the
output folder, so both runs write the same file.
"""
import os
import struct
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
LIMIT = 1048576


def check_png(data):
    """Walk every chunk and its CRC, so a damaged file fails here, not at the gate."""
    if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) > LIMIT:
        raise SystemExit("entry.png is not a PNG under 1 MiB")
    pos = 8
    while pos < len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + length]
        (crc,) = struct.unpack(">I", data[pos + 8 + length:pos + 12 + length])
        if zlib.crc32(kind + body) != crc:
            raise SystemExit("bad CRC in chunk %r" % kind)
        if kind == b"IHDR":
            w, h = struct.unpack(">II", body[:8])
            if w > 1024 or h > 1024:
                raise SystemExit("image larger than 1024 px")
        pos += 12 + length
        if kind == b"IEND":
            return
    raise SystemExit("no IEND chunk")


def main():
    with open(os.path.join(HERE, "entry.png"), "rb") as f:
        data = f.read()
    check_png(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()

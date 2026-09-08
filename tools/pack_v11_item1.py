# -*- coding: utf-8 -*-
from pathlib import Path
import gzip, hashlib, shutil, struct, zipfile
from datetime import datetime

ROOT = Path(r"D:\newMir3")
mir3z = next(
    p
    for p in Path(r"D:\BaiduNetdiskDownload").glob("*传奇3z*")
    for p in [next(x for x in p.rglob("mir3z") if (x / "Source" / "145Client").is_dir())]
)
client_exe = mir3z / "客户端" / "Mir3.exe"
tip_dir = mir3z / "Source" / "145Client" / "bin" / "TipZeroRebuild"
tip_dir.mkdir(parents=True, exist_ok=True)
shutil.copy2(client_exe, tip_dir / "Mir3.exe")
shutil.copy2(client_exe, tip_dir / "Mir3Game.exe")
tip_exe = tip_dir / "Mir3.exe"

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1024 * 1024), b""):
            h.update(c)
    return h.digest()

def gzip_file(src, dst):
    with open(src, "rb") as fin, gzip.open(dst, "wb", compresslevel=9) as fout:
        shutil.copyfileobj(fin, fout)
    return dst.stat().st_size

def read_plist(path):
    entries = []
    data = path.read_bytes()
    i = 0
    n = len(data)
    while i < n:
        length = 0
        shift = 0
        while True:
            b = data[i]
            i += 1
            length |= (b & 0x7F) << shift
            if (b & 0x80) == 0:
                break
            shift += 7
        name = data[i : i + length].decode("utf-8")
        i += length
        clen = struct.unpack_from("<q", data, i)[0]
        i += 8
        cslen = struct.unpack_from("<i", data, i)[0]
        i += 4
        checksum = data[i : i + cslen]
        i += cslen
        entries.append([name, clen, checksum])
    return entries

def write_7bit_int(val):
    out = bytearray()
    while True:
        b = val & 0x7F
        val >>= 7
        if val:
            out.append(b | 0x80)
        else:
            out.append(b)
            break
    return bytes(out)

def write_plist(path, entries):
    buf = bytearray()
    for name, clen, checksum in entries:
        nb = name.encode("utf-8")
        buf += write_7bit_int(len(nb))
        buf += nb
        buf += struct.pack("<q", clen)
        buf += struct.pack("<i", len(checksum))
        buf += checksum
    path.write_bytes(buf)

raw = tip_exe.read_bytes()
assert "精炼等级".encode("utf-16le") in raw
assert "天怒之火".encode("utf-16le") in raw
assert "TIPZERO_ATKSPD_HIDE".encode("utf-16le") in raw
print("markers OK", tip_exe.stat().st_size, md5_file(tip_exe).hex())

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
latest_db = ROOT / "Database" / "ClientSystem.db"
base = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v10"
out = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v11"
zip_out = ROOT / "patches_ready_20260906" / "PC_upload_v11_wave4_item1.zip"
out.mkdir(parents=True, exist_ok=True)
for f in list(out.iterdir()):
    if f.is_file():
        f.unlink()

clen_mir3 = gzip_file(tip_exe, out / "Mir3.exe.gz")
clen_game = gzip_file(tip_exe, out / "Mir3Game.exe.gz")
clen_db = gzip_file(latest_db, out / "Data-ClientSystem.db.gz")
csum_exe = md5_file(tip_exe)
csum_db = md5_file(latest_db)
tip_md5 = csum_exe.hex()
tip_sz = tip_exe.stat().st_size

entries = read_plist(base / "PList.Bin")
ship = {
    "mir3.exe": (clen_mir3, csum_exe, "Mir3.exe"),
    "mir3game.exe": (clen_game, csum_exe, "Mir3Game.exe"),
    r"data\clientsystem.db": (clen_db, csum_db, r"Data\ClientSystem.db"),
}
found = set()
for e in entries:
    key = e[0].replace("/", "\\").lower()
    if key in ship:
        clen, csum, canon = ship[key]
        e[0] = canon
        e[1] = clen
        e[2] = csum
        found.add(key)
        print("UPDATED", canon, clen, csum.hex())
for key, (clen, csum, canon) in ship.items():
    if key not in found:
        entries.append([canon, clen, csum])
        print("APPENDED", canon)
write_plist(out / "PList.Bin", entries)

readme_lines = [
    f"PC 20260908 wave4-item1 pack v11 stamp={stamp}",
    "Fixes: suppress skill TIP UI for listed magics; restore jinglian level (n/6) tip (lost since v8).",
    f"Mir3.exe size={tip_sz} md5={tip_md5} refine=True tipzero=True skillSuppress=True",
    f"ClientSystem.db size={latest_db.stat().st_size} md5={csum_db.hex()}",
    "Flat 7091 overwrite: PList.Bin + Mir3.exe.gz + Mir3Game.exe.gz + Data-ClientSystem.db.gz",
    "NEVER overwrite Server.exe/Library.dll",
    f"  PList.Bin                 {(out / 'PList.Bin').stat().st_size}",
    f"  Mir3.exe.gz               {clen_mir3}",
    f"  Mir3Game.exe.gz           {clen_game}",
    f"  Data-ClientSystem.db.gz   {clen_db}",
    "",
]
(out / "README_OVERWRITE.txt").write_text("\n".join(readme_lines), encoding="utf-8")

if zip_out.exists():
    zip_out.unlink()
with zipfile.ZipFile(zip_out, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in sorted(out.iterdir()):
        if f.is_file():
            zf.write(f, f.name)
            print("ZIP", f.name, f.stat().st_size)
print("OUT", out)
print("ZIP", zip_out, zip_out.stat().st_size)
print("DONE")

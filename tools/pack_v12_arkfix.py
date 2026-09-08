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
tip_exe = mir3z / "Source" / "145Client" / "bin" / "TipZeroRebuild" / "Mir3.exe"
assert tip_exe.is_file()
# ensure Mir3Game.exe twin
shutil.copy2(tip_exe, tip_exe.with_name("Mir3Game.exe"))

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
assert "TIPZERO_ATKSPD_HIDE".encode("utf-16le") in raw
print("markers OK", tip_exe.stat().st_size, md5_file(tip_exe).hex())

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
latest_db = ROOT / "Database" / "ClientSystem.db"
base = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v11"
out = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v12"
zip_out = ROOT / "patches_ready_20260906" / "PC_upload_v12_arkfix.zip"
out.mkdir(parents=True, exist_ok=True)
for f in list(out.iterdir()):
    if f.is_file():
        f.unlink()

clen_mir3 = gzip_file(tip_exe, out / "Mir3.exe.gz")
clen_game = gzip_file(tip_exe.with_name("Mir3Game.exe"), out / "Mir3Game.exe.gz")
clen_db = gzip_file(latest_db, out / "Data-ClientSystem.db.gz")
csum_exe = md5_file(tip_exe)
csum_db = md5_file(latest_db)

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

readme = [
    f"PC 20260909 arkfix pack v12 stamp={stamp}",
    "Fixes: 道馆铁匠 remove 变废为宝+破空石 text; boots WearWeight/HandWeight/Comfort clear BagWeight+AC/MR;",
    "  CanDeathDrop 全能指环/幸运霸龙头盔/天掌靴子; 影魅之刃 craft BP1破山剑 BP2天神法杖 BP3泰轮拂尘;",
    "  全能指环 Image=535(力量戒指); 精炼等级 tip color orange; shoes 极品 no AC/MR via Server.ini;",
    f"Mir3.exe size={tip_exe.stat().st_size} md5={csum_exe.hex()}",
    f"ClientSystem.db size={latest_db.stat().st_size} md5={csum_db.hex()}",
    "Flat 7091 overwrite: PList.Bin + Mir3.exe.gz + Mir3Game.exe.gz + Data-ClientSystem.db.gz",
    "NEVER overwrite Server.exe/Library.dll",
    f"  PList.Bin                 {(out / 'PList.Bin').stat().st_size}",
    f"  Mir3.exe.gz               {clen_mir3}",
    f"  Mir3Game.exe.gz           {clen_game}",
    f"  Data-ClientSystem.db.gz   {clen_db}",
]
(out / "README_OVERWRITE.txt").write_text("\n".join(readme) + "\n", encoding="utf-8")

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

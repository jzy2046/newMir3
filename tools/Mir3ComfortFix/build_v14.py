# -*- coding: utf-8 -*-
import hashlib, gzip, shutil, struct, zipfile, os
from pathlib import Path
from datetime import datetime

ROOT = Path(r"D:\newMir3")
latest_db = ROOT / "Database" / "ClientSystem.db"
sys_db = ROOT / "Database" / "System.db"
assert latest_db.is_file() and sys_db.is_file()

mir3z = None
for p in Path(r"D:\BaiduNetdiskDownload").iterdir():
    if not p.is_dir():
        continue
    for c in p.rglob("mir3z"):
        if (c / "Source" / "145Client").is_dir():
            mir3z = c
            break
    if mir3z:
        break
print("mir3z", mir3z)

for dbdir in mir3z.rglob("System.db"):
    if "Backup" in str(dbdir):
        continue
    parent = dbdir.parent
    print("sync System to", parent)
    shutil.copy2(sys_db, parent / "System.db")
    shutil.copy2(latest_db, parent / "ClientSystem.db")
    print("  + ClientSystem")

v13 = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v13_x64restore"
raw_exe = gzip.open(v13 / "Mir3.exe.gz", "rb").read()
assert len(raw_exe) == 4130304, len(raw_exe)
print("x64 exe bytes", len(raw_exe), hashlib.md5(raw_exe).hexdigest())

live = Path(r"E:\Mir3_16000")
stamp0 = datetime.now().strftime("%Y%m%d_%H%M%S")
if (live / "Mir3.exe").stat().st_size == 3929600:
    bak = live / f"Mir3.exe.bak_x86_{stamp0}"
    shutil.copy2(live / "Mir3.exe", bak)
    print("backed x86 to", bak)
(live / "Mir3.exe").write_bytes(raw_exe)
(live / "Mir3Game.exe").write_bytes(raw_exe)
shutil.copy2(latest_db, live / "Data" / "ClientSystem.db")
print("LIVE Mir3.exe", (live / "Mir3.exe").stat().st_size, hashlib.md5((live / "Mir3.exe").read_bytes()).hexdigest())
print("LIVE Mir3Game.exe", (live / "Mir3Game.exe").stat().st_size)
print("LIVE ClientSystem", (live / "Data" / "ClientSystem.db").stat().st_size, hashlib.md5((live / "Data" / "ClientSystem.db").read_bytes()).hexdigest())

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

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
out = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v14_x64_comfort"
zip_out = ROOT / "patches_ready_20260906" / "PC_upload_v14_x64_comfort.zip"
out.mkdir(parents=True, exist_ok=True)
for f in list(out.iterdir()):
    if f.is_file():
        f.unlink()

tmp = ROOT / "tools" / "Mir3ComfortFix" / "x64_exe"
tmp.mkdir(exist_ok=True)
(tmp / "Mir3.exe").write_bytes(raw_exe)
(tmp / "Mir3Game.exe").write_bytes(raw_exe)

clen_mir3 = gzip_file(tmp / "Mir3.exe", out / "Mir3.exe.gz")
clen_game = gzip_file(tmp / "Mir3Game.exe", out / "Mir3Game.exe.gz")
clen_db = gzip_file(latest_db, out / "Data-ClientSystem.db.gz")
csum_exe = md5_file(tmp / "Mir3.exe")
csum_db = md5_file(latest_db)

base = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v13_x64restore"
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
    f"PC 20260909 x64+comfort pack v14 stamp={stamp}",
    "ROOT CAUSE (open fail): v11/v12 Mir3.exe were x86 (3929600) vs x64 d3dx9_43.dll -> BadImageFormatException.",
    "This pack: x64 Mir3.exe/Mir3Game.exe (4130304 from v9/v13) + ClientSystem with boots Comfort ItemInfoStat correct.",
    "Comfort (ItemInfoStat only; ItemInfo has NO Comfort column): cao1 pi2 wu3 chi4 tian5 elite7",
    "WearWeight=wear-burden HandWeight=wrist; BagWeight/AC/MR cleared on boots.",
    "USE THIS PACK ONLY for 7091 overwrite. NEVER use v11/v12 (x86 tip). NEVER Server.exe/Library.dll.",
    f"Mir3.exe size={len(raw_exe)} md5={csum_exe.hex()}",
    f"Mir3Game.exe size={len(raw_exe)} md5={csum_exe.hex()}",
    f"ClientSystem.db size={latest_db.stat().st_size} md5={csum_db.hex()}",
    "Flat: PList.Bin + Mir3.exe.gz + Mir3Game.exe.gz + Data-ClientSystem.db.gz",
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

# -*- coding: utf-8 -*-
"""PC_7091 ClientSystem-only overwrite (no 9GB, no bak)."""
from pathlib import Path
import gzip, hashlib, shutil, struct, zipfile
from datetime import datetime

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
ROOT = Path(r"D:\newMir3")
db = ROOT / "Database" / "ClientSystem.db"

def find_hot():
    for d in Path("D:/").iterdir():
        if d.is_dir() and (d / "PC_7091_overwrite_latest").is_dir():
            return d
    raise SystemExit("hot root not found")

HOT = find_hot()
pc = HOT / "PC_7091_overwrite_latest"

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
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
            b = data[i]; i += 1
            length |= (b & 0x7F) << shift
            if (b & 0x80) == 0: break
            shift += 7
        name = data[i:i+length].decode("utf-8"); i += length
        clen = struct.unpack_from("<q", data, i)[0]; i += 8
        cslen = struct.unpack_from("<i", data, i)[0]; i += 4
        checksum = data[i:i+cslen]; i += cslen
        entries.append([name, clen, checksum])
    return entries

def write_7bit_int(val):
    out = bytearray()
    while True:
        b = val & 0x7F
        val >>= 7
        if val: out.append(b | 0x80)
        else:
            out.append(b); break
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

def update_entry(entries, plist_name, clen, csum):
    key = plist_name.replace("/", "\\").lower()
    for e in entries:
        if e[0].replace("/", "\\").lower() == key:
            e[0] = plist_name; e[1] = clen; e[2] = csum
            return "updated"
    entries.append([plist_name, clen, csum])
    return "appended"

def clean_bak(pack):
    for junk in list(pack.iterdir()):
        if junk.is_file() and (".bak_" in junk.name or junk.name.endswith(".bak")):
            junk.unlink()
        elif junk.is_dir() and (junk.name.startswith("_bak") or ".bak_" in junk.name):
            shutil.rmtree(junk)

assert db.is_file() and pc.is_dir() and (pc / "PList.Bin").is_file()
clean_bak(pc)
entries = read_plist(pc / "PList.Bin")
assert len(entries) > 100, f"PC PList too small {len(entries)}"

gz_path = pc / "Data-ClientSystem.db.gz"
clen = gzip_file(db, gz_path)
csum = md5_file(db)
with gzip.open(gz_path, "rb") as f:
    assert f.read() == db.read_bytes()
action = update_entry(entries, r"Data\ClientSystem.db", clen, csum.hex() if False else csum)
# csum must be raw md5 digest bytes
action = update_entry(entries, r"Data\ClientSystem.db", clen, csum)
write_plist(pc / "PList.Bin", entries)
clean_bak(pc)

readme = [
    f"PC_7091 ClientSystem-only stamp={stamp}",
    "v12: clen=gz size; checksum=MD5(uncompressed ClientSystem.db)",
    f"Data\\ClientSystem.db clen={clen} md5={csum.hex()} action={action} entries={len(entries)}",
    "RestoreNewbieQuests: restore 68 newbie quests PT1; keep boss查询卷 sell=500; 霸王守卫 HP=5000; 地煞石/天罡石 sell=1",
    "Cover onto PC 7091 client root: Data-ClientSystem.db.gz + PList.Bin (and other existing gz files already in folder).",
    "NO bak files. Library/exe unchanged.",
]
(pc / "README_OVERWRITE.txt").write_text("\n".join(readme) + "\n", encoding="utf-8")

hist = HOT / "_history"
hist.mkdir(exist_ok=True)
zpath = HOT / "PC_7091_overwrite_latest.zip"
if zpath.exists():
    shutil.copy2(zpath, hist / f"PC_7091_overwrite_latest.zip_{stamp}")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in pc.iterdir():
        if f.is_file():
            zf.write(f, f.name)
print(f"PC updated Data\\ClientSystem.db {clen} {csum.hex()} action={action} entries={len(entries)}")
print(f"PC zip {zpath} {zpath.stat().st_size}")
print(f"DONE {stamp}")
print(f"PACK {pc}")

# -*- coding: utf-8 -*-
"""Thin Mobile ClientSystem-only overwrite (no 9GB rezip)."""
from pathlib import Path
import gzip, hashlib, shutil, struct, zipfile
from datetime import datetime

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
ROOT = Path(r"D:\newMir3")
db = ROOT / "Database" / "ClientSystem.db"

def find_hot():
    for d in Path("D:/").iterdir():
        if d.is_dir() and (d / "Mobile_overwrite_latest").is_dir():
            return d
    raise SystemExit("hot root not found")

HOT = find_hot()

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

def patch_folder(mob: Path):
    clean_bak(mob)
    assert (mob / "PList.Bin").is_file()
    entries = read_plist(mob / "PList.Bin")
    gz_path = mob / "Data-ClientSystem.db.gz"
    clen = gzip_file(db, gz_path)
    csum = md5_file(db)
    with gzip.open(gz_path, "rb") as f:
        assert f.read() == db.read_bytes()
    action = update_entry(entries, r"Data\ClientSystem.db", clen, csum)
    write_plist(mob / "PList.Bin", entries)
    clean_bak(mob)
    return action, clen, csum.hex(), len(entries)

hist = HOT / "_history"
hist.mkdir(exist_ok=True)

results = []
for name in ["Mobile_overwrite_latest", "Mobile_7081_overwrite_latest"]:
    mob = HOT / name
    if not mob.is_dir():
        print("SKIP missing", mob)
        continue
    action, clen, md5hex, n = patch_folder(mob)
    print(f"{name}: {action} clen={clen} md5={md5hex} entries={n}")
    results.append((name, action, clen, md5hex, n))

# Thin zip (ClientSystem only) — do NOT rebuild 9GB full zip
thin_dir = HOT / f"_thin_mobile_clientsystem_{stamp}"
thin_dir.mkdir(exist_ok=True)
src = HOT / "Mobile_overwrite_latest"
for fn in ["Data-ClientSystem.db.gz", "PList.Bin"]:
    shutil.copy2(src / fn, thin_dir / fn)
readme = [
    f"Mobile THIN ClientSystem-only stamp={stamp}",
    "v12: clen=gz size; checksum=MD5(uncompressed)",
    f"Data\\ClientSystem.db clen={results[0][2]} md5={results[0][3]}",
    "Cover onto http://43.226.60.100:7081/ root: Data-ClientSystem.db.gz + PList.Bin",
    "Full 9GB Mobile_overwrite_latest.zip NOT rebuilt (ClientSystem-only change).",
    "Also folders Mobile_overwrite_latest / Mobile_7081_overwrite_latest updated in place.",
]
(thin_dir / "README_OVERWRITE.txt").write_text("\n".join(readme) + "\n", encoding="utf-8")
thin_zip = HOT / f"Mobile_overwrite_latest_THIN_{stamp}.zip"
with zipfile.ZipFile(thin_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in thin_dir.iterdir():
        if f.is_file():
            zf.write(f, f.name)
# also copy to history alias
shutil.copy2(thin_zip, hist / thin_zip.name)
# stable thin latest name
stable = HOT / "Mobile_overwrite_latest_THIN.zip"
shutil.copy2(thin_zip, stable)
print("THIN zip", thin_zip, thin_zip.stat().st_size)
print("STABLE", stable)
print("DONE")

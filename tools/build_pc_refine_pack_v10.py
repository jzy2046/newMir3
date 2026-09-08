import gzip, hashlib, shutil, struct, zipfile
from datetime import datetime
from pathlib import Path

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.digest()

def sha256_hex(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def gzip_file(src, dst):
    with open(src, "rb") as fin, gzip.open(dst, "wb", compresslevel=9) as fout:
        shutil.copyfileobj(fin, fout)
    return Path(dst).stat().st_size

def read_plist(path):
    entries = []
    data = Path(path).read_bytes()
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
        name = data[i:i+length].decode("utf-8")
        i += length
        clen = struct.unpack_from("<q", data, i)[0]
        i += 8
        cslen = struct.unpack_from("<i", data, i)[0]
        i += 4
        checksum = data[i:i+cslen]
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
    Path(path).write_bytes(buf)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
latest_db = Path(r"D:\newMir3\Database\ClientSystem.db")
v9 = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_overwrite_v9")
out = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_overwrite_v10")
zip_out = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_v10_wave4.zip")
zip_alt = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_v10_wave4_gz.zip")

db_md5 = md5_file(latest_db).hex()
db_sz = latest_db.stat().st_size
sha16 = sha256_hex(latest_db)[:16].upper()
print("CLIENT_DB", db_sz, db_md5, sha16)

clen_mir3 = (out / "Mir3.exe.gz").stat().st_size
clen_game = (out / "Mir3Game.exe.gz").stat().st_size
with gzip.open(out / "Mir3.exe.gz", "rb") as f:
    exe_raw = f.read()
csum_exe = hashlib.md5(exe_raw).digest()
tip_md5 = csum_exe.hex()
tip_sz = len(exe_raw)
print("TIP_EXE", tip_sz, tip_md5)

clen_db = gzip_file(latest_db, out / "Data-ClientSystem.db.gz")
csum_db = md5_file(latest_db)
print("GZ_DB", clen_db)

entries = read_plist(v9 / "PList.Bin")
ship = {
    "mir3.exe": (clen_mir3, csum_exe, "Mir3.exe"),
    "mir3game.exe": (clen_game, csum_exe, "Mir3Game.exe"),
    "data\\clientsystem.db": (clen_db, csum_db, "Data\\ClientSystem.db"),
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

plist_path = out / "PList.Bin"
write_plist(plist_path, entries)

readme = "\n".join([
    f"PC 20260908 wave4 pack v10 stamp={stamp}",
    f"Mir3.exe size={tip_sz} md5={tip_md5} (same tip as v9; ClientSystem-only)",
    f"ClientSystem.db size={db_sz} md5={db_md5} sha16={sha16}",
    "Includes wave4 DB changes; flat 7091 overwrite format (gz).",
    "Server deploy: git pull Scripts+Database ONLY; NEVER overwrite Server.exe/Library.dll",
    "Overwrite on VPS 7091:",
    f"  PList.Bin                 {plist_path.stat().st_size}",
    f"  Mir3.exe.gz               {clen_mir3}",
    f"  Mir3Game.exe.gz           {clen_game}",
    f"  Data-ClientSystem.db.gz   {clen_db}",
    "Host: http://43.226.60.100:7091/",
    "",
])
(out / "README_OVERWRITE.txt").write_text(readme, encoding="utf-8")

for zpath in (zip_out, zip_alt):
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.iterdir()):
            if f.is_file():
                zf.write(f, f.name)
                print("ZIP", zpath.name, f.name, f.stat().st_size)
    print("ZIP_OUT", zpath, zpath.stat().st_size)

assert not (out / "Data").exists()
assert not (out / "ServerDatabase").exists()
v = read_plist(plist_path)
for e in v:
    key = e[0].replace("/", "\\").lower()
    if key in ship:
        expect_clen, expect_csum, _ = ship[key]
        assert e[1] == expect_clen
        assert e[2] == expect_csum
        print("VERIFY_OK", e[0], e[1], e[2].hex())
print("DONE")

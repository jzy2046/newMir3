# -*- coding: utf-8 -*-
from pathlib import Path
import gzip, hashlib, shutil, struct
from datetime import datetime

ROOT = Path(r"D:\newMir3")
pack = Path(r"D:\Mir3热更补丁\PC_7091_overwrite_latest")
db = ROOT / "Database" / "ClientSystem.db"
assert db.is_file(), db
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

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

plist_path = pack / "PList.Bin"
entries = read_plist(plist_path)
before = None
for e in entries:
    key = e[0].replace("/", "\\").lower()
    if key == r"data\clientsystem.db":
        before = (e[1], e[2].hex())
        break
print("BEFORE", before)

gz_path = pack / "Data-ClientSystem.db.gz"
clen = gzip_file(db, gz_path)
csum = md5_file(db)
raw = db.read_bytes()
with gzip.open(gz_path, "rb") as f:
    ud = f.read()
assert ud == raw
print("gz size(clen)=%s db size=%s uncomp_md5=%s" % (clen, db.stat().st_size, csum.hex()))

updated = False
for e in entries:
    key = e[0].replace("/", "\\").lower()
    if key == r"data\clientsystem.db":
        e[0] = r"Data\ClientSystem.db"
        e[1] = clen
        e[2] = csum
        updated = True
        print("UPDATED", e[0], e[1], e[2].hex())
if not updated:
    entries.append([r"Data\ClientSystem.db", clen, csum])
    print("APPENDED ClientSystem")

write_plist(plist_path, entries)

entries2 = read_plist(plist_path)
for e in entries2:
    if e[0].replace("/", "\\").lower() == r"data\clientsystem.db":
        assert e[1] == clen
        assert e[2] == csum
        print("VERIFY OK")

readme = pack / "README_OVERWRITE.txt"
txt = [
    f"PC_7091_overwrite_latest NPC hide stamp={stamp}",
    "v12: clen=gz size; checksum=MD5(uncompressed db) — NOT gz md5",
    f"BEFORE PList Data\\ClientSystem.db clen={before[0]} md5={before[1]}",
    f"AFTER  PList Data\\ClientSystem.db clen={clen} md5={csum.hex()}",
    f"ClientSystem.db size={db.stat().st_size} md5={csum.hex()}",
    f"Data-ClientSystem.db.gz size={clen}",
    "VERIFY: gunzip md5==PList; clen==gz size OK",
    "",
    "本轮改动:",
    "- 道馆 Map#7 隐藏重复综合服务 NPC#5657 (403,119) Display=True",
    "- 保留 #335 综合服务(401,119) 与 #66 行政官员(403,119)",
    "- 库内无「泡点」NPC；403,119 叠层实为 #66+#5657",
    "- 僵尸 Book DropInfo: Chance 无 0、行未删（222 条；相对 eight 备份仅 Chance/2）",
    "",
    "7091 手动覆盖（仅这 2 个）:",
    "  PList.Bin",
    "  Data-ClientSystem.db.gz",
    f"路径: {pack}",
    "不要动: Mir3.exe.gz / Mir3Game.exe.gz / Data-Diy-Mir3.dat.gz（本轮未改）",
    "",
    "服务端还需覆盖 System.db（Database+Data 已更新），重启服务端生效。勿登录 VPS。",
]
readme.write_text("\n".join(txt) + "\n", encoding="utf-8")
print("DONE stamp", stamp)

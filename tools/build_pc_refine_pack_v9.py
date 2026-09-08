# -*- coding: utf-8 -*-
"""Build PC_upload_overwrite_v9 evening pack (ClientSystem.db update)."""
import gzip, hashlib, shutil, struct, zipfile
from datetime import datetime
from pathlib import Path

def find_mir3z() -> Path:
    bd = Path(r"D:\BaiduNetdiskDownload")
    for c in bd.rglob("mir3z"):
        tip = c / "Source" / "145Client" / "bin" / "TipZeroRebuild" / "Mir3.exe"
        if c.is_dir() and tip.is_file():
            return c
    raise SystemExit("mir3z not found")

def find_client_dir(mir3z: Path) -> Path:
    for p in mir3z.iterdir():
        if p.is_dir() and (p / "Mir3.exe").is_file() and (p / "Data").is_dir():
            return p
    raise SystemExit("client dir not found")

def md5_file(path: Path) -> bytes:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.digest()

def md5_hex(path: Path) -> str:
    return md5_file(path).hex()

def sha256_hex(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def gzip_file(src: Path, dst: Path) -> int:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(src, "rb") as fin, gzip.open(dst, "wb", compresslevel=9) as fout:
        shutil.copyfileobj(fin, fout)
    return dst.stat().st_size

def read_plist(path: Path):
    entries = []
    data = path.read_bytes()
    i = 0
    n = len(data)
    while i < n:
        length = 0
        shift = 0
        while True:
            if i >= n:
                raise ValueError("truncated plist string length")
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

def write_7bit_int(val: int) -> bytes:
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

def write_plist(path: Path, entries):
    buf = bytearray()
    for name, clen, checksum in entries:
        nb = name.encode("utf-8")
        buf += write_7bit_int(len(nb))
        buf += nb
        buf += struct.pack("<q", clen)
        buf += struct.pack("<i", len(checksum))
        buf += checksum
    path.write_bytes(buf)

def main():
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mir3z = find_mir3z()
    tip_exe = mir3z / "Source" / "145Client" / "bin" / "TipZeroRebuild" / "Mir3.exe"
    tip_game = mir3z / "Source" / "145Client" / "bin" / "TipZeroRebuild" / "Mir3Game.exe"
    client_dir = find_client_dir(mir3z)
    client_db = client_dir / "Data" / "ClientSystem.db"
    latest_db = Path(r"D:\newMir3\Database\ClientSystem.db")
    clean_base = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_overwrite_v8")
    out = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_overwrite_v9")
    zip_out = Path(r"D:\newMir3\patches_ready_20260906\PC_upload_v9_evening.zip")

    print(f"MIR3Z={mir3z}")
    print(f"CLIENT_DIR={client_dir}")
    assert tip_exe.is_file(), tip_exe
    if not tip_game.is_file():
        shutil.copy2(tip_exe, tip_game)

    tip_md5 = md5_hex(tip_exe)
    tip_sz = tip_exe.stat().st_size
    print(f"TIP_EXE size={tip_sz} md5={tip_md5}")

    assert latest_db.is_file()
    shutil.copy2(latest_db, client_db)
    db_md5 = md5_hex(client_db)
    db_sz = client_db.stat().st_size
    db_sha = sha256_hex(client_db)
    sha16 = db_sha[:16].upper()
    print(f"CLIENT_DB size={db_sz} md5={db_md5} sha16={sha16}")

    base_plist = clean_base / "PList.Bin"
    assert base_plist.is_file(), base_plist
    entries = read_plist(base_plist)

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    mir3_gz = out / "Mir3.exe.gz"
    mir3game_gz = out / "Mir3Game.exe.gz"
    db_gz = out / "Data-ClientSystem.db.gz"
    clen_mir3 = gzip_file(tip_exe, mir3_gz)
    clen_game = gzip_file(tip_game, mir3game_gz)
    clen_db = gzip_file(client_db, db_gz)
    csum_exe = md5_file(tip_exe)
    csum_db = md5_file(client_db)

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
            print(f"UPDATED {canon} clen={clen}")
    for key, (clen, csum, canon) in ship.items():
        if key not in found:
            entries.append([canon, clen, csum])
            print(f"APPENDED {canon}")

    plist_path = out / "PList.Bin"
    write_plist(plist_path, entries)

    readme = "\n".join([
        f"PC 20260908 evening pack v9 stamp={stamp}",
        f"Mir3.exe size={tip_sz} md5={tip_md5}",
        f"ClientSystem.db size={db_sz} md5={db_md5} sha16={sha16}",
        "Includes evening DB: spawns, NPC move, boots, items, monsters HP/dmg, drops, mall, bracelets",
        "Server deploy: git pull Scripts+Database/Server.ini ONLY; never overwrite Server.exe/Library.dll",
        "Overwrite on VPS 7091:",
        f"  PList.Bin                 {plist_path.stat().st_size}",
        f"  Mir3.exe.gz               {clen_mir3}",
        f"  Mir3Game.exe.gz           {clen_game}",
        f"  Data-ClientSystem.db.gz   {clen_db}",
        "Host: http://43.226.60.100:7091/",
        "",
    ])
    (out / "README_OVERWRITE.txt").write_text(readme, encoding="utf-8")

    if zip_out.exists():
        zip_out.unlink()
    with zipfile.ZipFile(zip_out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.iterdir()):
            if f.is_file():
                zf.write(f, f.name)
                print(f"ZIP {f.name} {f.stat().st_size}")
    print(f"ZIP_OUT={zip_out} size={zip_out.stat().st_size}")
    print("DONE")

if __name__ == "__main__":
    main()

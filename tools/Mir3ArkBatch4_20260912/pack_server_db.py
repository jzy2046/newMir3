# -*- coding: utf-8 -*-
"""Refresh Server_overwrite_latest System.db (+ ClientSystem if present). No VPS login."""
from pathlib import Path
import shutil, gzip, hashlib
from datetime import datetime

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
ROOT = Path(r"D:\newMir3")
HOT = next(d for d in Path("D:/").iterdir() if d.is_dir() and (d / "Server_overwrite_latest").is_dir())
srv = HOT / "Server_overwrite_latest"
print("srv", srv)
for name in ["System.db", "ClientSystem.db"]:
    src = ROOT / "Database" / name
    if not src.is_file():
        continue
    # prefer plain or gz naming used in folder
    plain = srv / name
    gz = srv / f"{name}.gz"
    data_gz = srv / f"Database-{name}.gz"
    # copy plain if folder uses plain
    targets = []
    for p in srv.rglob("*"):
        if p.is_file() and (p.name == name or p.name == f"{name}.gz" or p.name.lower() == f"database-{name}".lower() or p.name == f"Data-{name}.gz"):
            targets.append(p)
    print(name, "targets", [str(t.relative_to(srv)) for t in targets])
    if not targets:
        # put System.db at root for ops
        shutil.copy2(src, srv / name)
        print("copied plain", name)
        continue
    for t in targets:
        if t.suffix == ".gz" or t.name.endswith(".gz"):
            with open(src, "rb") as fin, gzip.open(t, "wb", compresslevel=9) as fout:
                shutil.copyfileobj(fin, fout)
            print("gz wrote", t, t.stat().st_size)
        else:
            shutil.copy2(src, t)
            print("copied", t)
print("DONE", stamp)

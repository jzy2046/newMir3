# -*- coding: utf-8 -*-
from pathlib import Path
import gzip, hashlib, shutil, struct, zipfile
from datetime import datetime

ROOT = Path(r'D:\newMir3')
v16 = ROOT / 'patches_ready_20260909_talisman' / 'PC_upload_overwrite_v16_talisman'
v15 = ROOT / 'patches_ready_20260906' / 'PC_upload_overwrite_v15_x64_comfortvalue'
exe_dir = ROOT / 'tools' / 'Mir3TipFix_v17' / 'x64_exe'
latest_db = ROOT / 'Database' / 'ClientSystem.db'
out_root = ROOT / 'patches_ready_20260909_tipfix'
pc_out = out_root / 'PC_upload_overwrite_v17_tipfix'
mob_base = ROOT / 'patches_ready_20260906' / 'Mobile_upload_overwrite'
mob_out = out_root / 'Mobile_upload_overwrite_v17_tipfix'
zip_pc = out_root / 'PC_upload_v17_tipfix.zip'
zip_mob = out_root / 'Mobile_upload_v17_tipfix.zip'

def md5_file(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for c in iter(lambda: f.read(1024 * 1024), b''):
            h.update(c)
    return h.digest()

def gzip_file(src, dst):
    with open(src, 'rb') as fin, gzip.open(dst, 'wb', compresslevel=9) as fout:
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
        name = data[i:i+length].decode('utf-8')
        i += length
        clen = struct.unpack_from('<q', data, i)[0]
        i += 8
        cslen = struct.unpack_from('<i', data, i)[0]
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
        nb = name.encode('utf-8')
        buf += write_7bit_int(len(nb))
        buf += nb
        buf += struct.pack('<q', clen)
        buf += struct.pack('<i', len(checksum))
        buf += checksum
    path.write_bytes(buf)

assert (exe_dir / 'Mir3.exe').is_file() and latest_db.is_file()
base_plist = v16 if (v16 / 'PList.Bin').is_file() else v15
diy_src = v16 / 'Data-Diy-Mir3.dat.gz' if (v16 / 'Data-Diy-Mir3.dat.gz').is_file() else v15 / 'Data-Diy-Mir3.dat.gz'
raw = (exe_dir / 'Mir3.exe').read_bytes()
assert 4100000 <= len(raw) <= 4200000, len(raw)
pe = int.from_bytes(raw[0x3C:0x40], 'little')
assert int.from_bytes(raw[pe+4:pe+6], 'little') == 0x8664
assert b'ItemRefreshTime' in raw

stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
out_root.mkdir(parents=True, exist_ok=True)
for d in (pc_out, mob_out):
    if d.exists():
        for f in list(d.iterdir()):
            if f.is_file(): f.unlink()
    else:
        d.mkdir(parents=True)

clen_mir3 = gzip_file(exe_dir / 'Mir3.exe', pc_out / 'Mir3.exe.gz')
clen_game = gzip_file(exe_dir / 'Mir3Game.exe', pc_out / 'Mir3Game.exe.gz')
clen_db = gzip_file(latest_db, pc_out / 'Data-ClientSystem.db.gz')
shutil.copy2(diy_src, pc_out / 'Data-Diy-Mir3.dat.gz')
clen_diy = (pc_out / 'Data-Diy-Mir3.dat.gz').stat().st_size
diy_live = Path(r'E:\Mir3_16000\Data\Diy\Mir3.dat')
if diy_live.is_file():
    csum_diy = md5_file(diy_live)
else:
    with gzip.open(diy_src, 'rb') as g:
        csum_diy = hashlib.md5(g.read()).digest()
csum_exe = md5_file(exe_dir / 'Mir3.exe')
csum_db = md5_file(latest_db)

entries = read_plist(base_plist / 'PList.Bin')
ship = {
    'mir3.exe': (clen_mir3, csum_exe, 'Mir3.exe'),
    'mir3game.exe': (clen_game, csum_exe, 'Mir3Game.exe'),
    r'data\clientsystem.db': (clen_db, csum_db, r'Data\ClientSystem.db'),
    r'data\diy\mir3.dat': (clen_diy, csum_diy, r'Data\Diy\Mir3.dat'),
}
found=set()
for e in entries:
    key = e[0].replace('/','\\').lower()
    if key in ship:
        clen,csum,canon = ship[key]
        e[0],e[1],e[2] = canon,clen,csum
        found.add(key)
        print('UPDATED', canon, clen, csum.hex())
for key,(clen,csum,canon) in ship.items():
    if key not in found:
        entries.append([canon,clen,csum]); print('APPENDED', canon)
write_plist(pc_out / 'PList.Bin', entries)

(pc_out / 'README_OVERWRITE.txt').write_text('\n'.join([
    f'PC 20260909 tipfix pack v17 stamp={stamp}',
    'DELTA vs v16: NEW x64 Mir3.exe/Mir3Game.exe from Mir3Source@98e9ce3 (WeapEx tip + ItemRefreshTime).',
    'KEEP: ClientSystem.db (talisman), Diy ComfortValue=False.',
    f'Mir3.exe size={len(raw)} md5={csum_exe.hex()} PE=x64 ItemRefreshTime=YES',
    f'ClientSystem.db size={latest_db.stat().st_size} md5={csum_db.hex()}',
    'Flat 7091: PList.Bin + Mir3.exe.gz + Mir3Game.exe.gz + Data-ClientSystem.db.gz + Data-Diy-Mir3.dat.gz',
    'NEVER overwrite Server.exe/Library.dll',
    'NOTE: MIR3FIX_20260909 comment-only; binary marker ItemRefreshTime',
    f'  PList.Bin {(pc_out/"PList.Bin").stat().st_size}',
    f'  Mir3.exe.gz {clen_mir3}',
    f'  Mir3Game.exe.gz {clen_game}',
    f'  Data-ClientSystem.db.gz {clen_db}',
    f'  Data-Diy-Mir3.dat.gz {clen_diy}',
])+'\n', encoding='utf-8')

shutil.copy2(pc_out/'Data-ClientSystem.db.gz', mob_out/'Data-ClientSystem.db.gz')
if (mob_base/'PList.Bin').is_file():
    mob_entries = read_plist(mob_base/'PList.Bin')
    mfound=False
    for e in mob_entries:
        if 'clientsystem' in e[0].lower():
            e[0]=r'Data\ClientSystem.db'; e[1]=clen_db; e[2]=csum_db; mfound=True; print('MOB_UPDATED')
    if not mfound:
        mob_entries.append([r'Data\ClientSystem.db', clen_db, csum_db]); print('MOB_APPENDED')
    write_plist(mob_out/'PList.Bin', mob_entries)
(mob_out/'README_OVERWRITE.txt').write_text(
    f'Mobile v17 tipfix stamp={stamp}\nOnly ClientSystem.db (talisman). Tip fix is PC exe.\nmd5={csum_db.hex()} gz={clen_db}\n',
    encoding='utf-8')

for zpath, folder in [(zip_pc, pc_out),(zip_mob, mob_out)]:
    if zpath.exists(): zpath.unlink()
    with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(folder.iterdir()):
            if f.is_file():
                zf.write(f, f.name); print('ZIP', zpath.name, f.name, f.stat().st_size)

(out_root/'README.txt').write_text('\n'.join([
    f'patches_ready_20260909_tipfix stamp={stamp}',
    'v17 x64 tip/proficiency from 98e9ce3 + talisman ClientSystem + Diy',
    f'PC: {pc_out}',
    f'ZIP: {zip_pc}',
    'Upload flat to VPS 7091. Restart Server after ini+db.',
    'NEVER overwrite licensed Server.exe 82562560 without user OK',
])+'\n', encoding='utf-8')
print('OUT', out_root)
print('DONE', stamp, len(raw), csum_exe.hex())

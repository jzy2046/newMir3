# -*- coding: utf-8 -*-
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r'D:\mir3src')

def patch_store(path):
    p = ROOT / path
    t = p.read_text(encoding='utf-8')
    if 'count *= 1000' in t and '万年雪霜' in t:
        print('ALREADY store', path); return
    marker = '            var count = p.Count;'
    insert = (
        '            var count = p.Count;\n'
        '            // 20260908: 万年雪霜 100赞助币=1000个 (Price already 100 per purchase unit)\n'
        '            if (info.Item.ItemName == "万年雪霜")\n'
        '                count *= 1000;'
    )
    idx = t.find('public void MarketPlaceStoreBuy')
    if idx < 0:
        print('MISS method', path); return
    idx2 = t.find(marker, idx)
    if idx2 < 0:
        print('MISS marker', path); return
    t = t[:idx2] + insert + t[idx2+len(marker):]
    p.write_text(t, encoding='utf-8')
    print('OK store', path)

def patch_keys(path):
    p = ROOT / path
    t = p.read_text(encoding='utf-8')
    if '20260908: disable J dialog keybind' in t:
        print('ALREADY keys', path); return
    # flexible replace of Key1 = Keys.J / Keys.U in those cases
    import re
    t2, n1 = re.subn(
        r'(case KeyBindAction\.BonusPoolWindow:\s*\n\s*bind\.Category = "功能"\.Lang\(\);\s*\n\s*)bind\.Key1 = Keys\.J;',
        r'\1// 20260908: disable J dialog keybind\n                    bind.Key1 = Keys.None;',
        t, count=1)
    t3, n2 = re.subn(
        r'(case KeyBindAction\.WarWeaponWindow:\s*\n\s*bind\.Category = "功能"\.Lang\(\);\s*\n\s*)bind\.Key1 = Keys\.U;',
        r'\1// 20260908: disable U dialog keybind\n                    bind.Key1 = Keys.None;',
        t2, count=1)
    if n1==0 or n2==0:
        print(f'PARTIAL keys n1={n1} n2={n2} {path}')
        i=t.find('BonusPoolWindow'); print(repr(t[i:i+200]))
        i=t.find('WarWeaponWindow'); print(repr(t[i:i+200]))
        return
    p.write_text(t3, encoding='utf-8')
    print('OK keys', path)

for path in [
    r'Source/ServerLibrary/Models/Player/Marketplace.cs',
    r'Mir3Source/ServerLibrary/Models/Player/Marketplace.cs',
]:
    patch_store(path)

for path in [
    r'Source/145Client/Envir/CEnvir.cs',
    r'Mir3Source/145Client/Envir/CEnvir.cs',
]:
    patch_keys(path)

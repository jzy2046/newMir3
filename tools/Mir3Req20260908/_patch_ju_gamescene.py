# -*- coding: utf-8 -*-
import pathlib,re,sys
sys.stdout.reconfigure(encoding='utf-8')

def disable_cases(path):
    p=pathlib.Path(path)
    if not p.exists():
        print('MISS', path); return
    t=p.read_text(encoding='utf-8')
    if '20260908: disable BonusPool/WarWeapon' in t:
        print('ALREADY', path); return
    # Comment out the case bodies by wrapping with if(false) or commenting cases
    # Prefer: break immediately / remove Visible toggles
    patterns = [
        (r'case KeyBindAction\.BonusPoolWindow:\s*\n(?:.*\n){0,6}?\s*break;',
         'case KeyBindAction.BonusPoolWindow: // 20260908: disable BonusPool/WarWeapon J\n                        break;'),
        (r'case KeyBindAction\.WarWeaponWindow:\s*\n(?:.*\n){0,6}?\s*break;',
         'case KeyBindAction.WarWeaponWindow: // 20260908: disable BonusPool/WarWeapon U\n                        break;'),
    ]
    t2=t
    for pat, repl in patterns:
        t2, n = re.subn(pat, repl, t2, count=1)
        print(f'  {path} n={n} for {pat[:40]}')
    if t2!=t:
        p.write_text(t2, encoding='utf-8')
        print('OK', path)
    else:
        # show nearby
        for key in ['BonusPoolWindow','WarWeaponWindow']:
            i=t.find(key)
            print(key, repr(t[i:i+300]) if i>=0 else 'absent')

for path in [
    r'D:\newMir3\Source\145Client\Scenes\GameScene.cs',
    r'D:\newMir3\Source\Mir3.Mobile\Scenes\GameScene.cs',
    r'D:\mir3src\Source\145Client\Scenes\GameScene.cs',
    r'D:\mir3src\Mir3Source\145Client\Scenes\GameScene.cs',
]:
    disable_cases(path)

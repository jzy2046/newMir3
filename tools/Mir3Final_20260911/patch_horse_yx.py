# -*- coding: utf-8 -*-
from pathlib import Path
import re, shutil
from datetime import datetime
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

files = [
    Path(r"D:\newMir3\Scripts\Npc\义贤.py"),
    Path(r"D:\newMir3\Scripts\Npc\比奇城\义贤.py"),
]
for p in files:
    if not p.exists():
        print("MISSING", p)
        continue
    bak = Path(str(p) + f".bak_final_{stamp}")
    if not bak.exists():
        shutil.copy2(p, bak)
    t = p.read_text(encoding="utf-8")
    orig = t
    # overview sell list
    t = re.sub(r"赤兔\s*-\s*[\d,\.]+\s*金币", "赤兔 - 100 金币", t)
    lines = t.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        # After HorseType.Red in sell action, fix GiveGold large amounts
        if "HorseType.Red" in line and "enum" not in line.lower():
            # peek ahead
            for j in range(i + 1, min(i + 10, len(lines))):
                m = re.search(r"GiveGold\(Sender,\s*(\d+)\)", lines[j])
                if m and int(m.group(1)) >= 1000000:
                    lines[j] = re.sub(r"GiveGold\(Sender,\s*\d+\)", "GiveGold(Sender,100)", lines[j])
                    print(f"  {p.name}:{j+1} GiveGold -> 100")
                # 元宝 sell -> 100 gold
                if re.search(r"GiveGameGold\(Sender,\s*\d+\)", lines[j]) and any("REDHORSE" in lines[k] for k in range(max(i, j-5), j+1)):
                    lines[j] = re.sub(r"GiveGameGold\(Sender,\s*\d+\)", "GiveGold(Sender,100)", lines[j])
                    print(f"  {p.name}:{j+1} GiveGameGold -> GiveGold(100)")
                if re.search(r"elif\s*\(\s*horse\s*==", lines[j]) and j > i:
                    break
                if "HorseType.Black" in lines[j] or "HorseType.White" in lines[j] or "HorseType.Brown" in lines[j]:
                    if j > i + 1:
                        break
            # Red confirm dialog 金额 near 类型：赤兔
        if "类型：赤兔" in line:
            for j in range(i, min(i + 6, len(lines))):
                if re.search(r"金额：[\d,\.]+\s*金币", lines[j]):
                    old = lines[j]
                    lines[j] = re.sub(r"金额：[\d,\.]+\s*金币", "金额：100 金币", lines[j])
                    print(f"  dialog {p.name}:{j+1} {old.strip()} -> {lines[j].strip()}")
        i += 1
    # rebuild from mutated lines (out was wrong approach - use lines)
    # Actually we mutated lines in place while appending old to out - fix:
    t = "\n".join(lines)
    if orig.endswith("\n") and not t.endswith("\n"):
        t += "\n"
    p.write_text(t, encoding="utf-8")
    print("wrote", p, "changed=", t != orig)
    # evidence
    for n, line in enumerate(t.splitlines(), 1):
        if any(k in line for k in ("赤兔", "GiveGold(Sender,100)", "GiveGold(Sender,25000000)", "50000000", "金额：")):
            if any(k in line for k in ("赤兔", "GiveGold", "金额", "50000000", "SubGold")):
                print(f"  E{n}:{line.strip()}")

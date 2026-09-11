# -*- coding: utf-8 -*-
from pathlib import Path
import re, shutil
from datetime import datetime
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
files = list(Path(r"D:\newMir3\Scripts").rglob("马店.py")) + list(Path(r"D:\newMir3\Scripts").rglob("马夫.py"))
for p in files:
    if "Backup" in str(p): continue
    bak = Path(str(p) + f".bak_final_{stamp}")
    if not bak.exists(): shutil.copy2(p, bak)
    t = p.read_text(encoding="utf-8")
    orig = t
    lines = t.splitlines()
    # Buy Red: SubGold 100000000 -> 50000000, Gold check similarly
    for i, line in enumerate(lines):
        if "HorseType.Red" in line and "GiveHose" in line:
            # look back for SubGold
            for j in range(max(0,i-5), i):
                if re.search(r"SubGold\(Sender,\s*100000000\)", lines[j]):
                    lines[j] = re.sub(r"SubGold\(Sender,\s*\d+\)", "SubGold(Sender,50000000)", lines[j])
                    print(f"{p}: SubGold buy -> 50M @{j+1}")
                if re.search(r"Gold\s*<\s*100000000", lines[j]):
                    lines[j] = re.sub(r"100000000", "50000000", lines[j])
                    print(f"{p}: Gold check -> 50M @{j+1}")
        # Sell Red GiveGold
        if "HorseType.Red" in line:
            for j in range(i+1, min(i+6, len(lines))):
                m = re.search(r"GiveGold\(Sender,\s*(\d+)\)", lines[j])
                if m and int(m.group(1)) >= 1000000:
                    lines[j] = re.sub(r"GiveGold\(Sender,\s*\d+\)", "GiveGold(Sender,100)", lines[j])
                    print(f"{p}: sell GiveGold -> 100 @{j+1}")
                    break
                if "HorseType." in lines[j] and j > i: break
    # text prices for 赤兔
    t = "\n".join(lines)
    t = re.sub(r"(非常稀有的赤兔马（)\d+万金币）", r"\g<1>5000万金币）", t)
    t = re.sub(r"赤兔马\s*-\s*[\d,]+\s*金币", "赤兔马 - 50,000,000 金币", t)
    t = re.sub(r"金额：100,000,000 金币", "金额：50,000,000 金币", t)  # buy confirm if present
    # sell overview if any large 赤兔 sell text - optional
    if not t.endswith("\n") and orig.endswith("\n"): t += "\n"
    p.write_text(t, encoding="utf-8")
    print("wrote", p, "changed=", t != orig)

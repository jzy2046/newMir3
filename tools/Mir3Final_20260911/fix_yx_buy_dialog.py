# -*- coding: utf-8 -*-
from pathlib import Path
import re
files = [
    Path(r"D:\newMir3\Scripts\Npc\义贤.py"),
    Path(r"D:\newMir3\Scripts\Npc\比奇城\义贤.py"),
]
for p in files:
    t = p.read_text(encoding="utf-8")
    lines = t.splitlines()
    for i, line in enumerate(lines):
        if "类型：赤兔马" in line:
            for j in range(i, min(i+5, len(lines))):
                if "金额：100 金币" in lines[j]:
                    lines[j] = lines[j].replace("金额：100 金币", "金额：50,000,000 金币")
                    print(f"restored BUY dialog {p.name}:{j+1}")
    t2 = "\n".join(lines) + ("\n" if t.endswith("\n") else "")
    p.write_text(t2, encoding="utf-8")
    # evidence buy vs sell
    for n, line in enumerate(t2.splitlines(), 1):
        if "类型：赤兔" in line or (n>70 and n<90 and "金额" in line) or (n>210 and n<230 and "金额" in line) or "SubGold(Sender,50000000)" in line or (n>=277 and n<=284 and "GiveGold" in line):
            print(f"  {p.name}:{n}:{line.strip()}")

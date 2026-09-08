import sys, os
sys.stdout.reconfigure(encoding="utf-8")
keys = [
    "OnJKey", "OnUKey", "J键", "U键", "OnJ", "OnU",
    "大护身符", "护身符（大）", "结晶石", "首饰合成", "成功率", "阿斌",
]
for root, dirs, files in os.walk(r"D:\newMir3\Scripts"):
    for f in files:
        if not f.endswith(".py"):
            continue
        p = os.path.join(root, f)
        t = open(p, encoding="utf-8", errors="ignore").read()
        hits = [k for k in keys if k in t]
        if hits:
            print(p[12:], "=>", hits)
print("====小老板====")
print(open(r"D:\newMir3\Scripts\Npc\道馆\小老板.py", encoding="utf-8").read()[:3000])

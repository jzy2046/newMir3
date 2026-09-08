import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
print("====啊斌 head====")
t=open(r"D:\newMir3\Scripts\Npc\边境城市\啊斌.py",encoding="utf-8").read()
print("len",len(t))
for m in re.finditer(r".{0,20}(成功|石榴|结晶|概率|random|Rate).{0,40}", t):
    line=t[:m.start()].count("\n")+1
    print(f"L{line}: {m.group(0).replace(chr(10),' / ')}")
print("====啊彬 vs 啊斌 listeners====")
for p in [r"D:\newMir3\Scripts\Npc\边境城市\啊斌.py", r"D:\newMir3\Scripts\Npc\边境城市\啊彬.py"]:
    tt=open(p,encoding="utf-8").read()
    for m in re.finditer(r"NpcEvent\.add_listener.*", tt):
        print(p, m.group(0))
print("====J/U related====")
for p in [r"D:\newMir3\Scripts\Player\事件触发\行会触发.py", r"D:\newMir3\Scripts\Player\事件触发\物品使用.py", r"D:\newMir3\Scripts\Player\PlayerProcess.py"]:
    if not os.path.exists(p):
        print("missing",p); continue
    tt=open(p,encoding="utf-8").read()
    print("FILE",p,"len",len(tt))
    for m in re.finditer(r".{0,5}(OnJ|OnU|JKey|UKey|Guild|行会).{0,80}", tt):
        line=tt[:m.start()].count("\n")+1
        if line<200 or "OnJ" in m.group(0) or "OnU" in m.group(0) or "Key" in m.group(0):
            print(f"  L{line}: {m.group(0).replace(chr(10),' / ')[:120]}")
# search all PlayerEvent listeners
print("====All PlayerEvent listeners====")
for root,dirs,files in os.walk(r"D:\newMir3\Scripts"):
  for f in files:
    if not f.endswith(".py"): continue
    p=os.path.join(root,f)
    tt=open(p,encoding="utf-8",errors="ignore").read()
    for m in re.finditer(r"PlayerEvent\.add_listener\(\s*[\"']([^\"']+)[\"']", tt):
      print(p[12:], m.group(1))

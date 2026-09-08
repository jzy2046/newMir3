import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
# Search Source and Library strings - Library is dll, check Source
src=r"D:\newMir3\Source"
if os.path.isdir(src):
  print("Source dirs:", os.listdir(src)[:30])
else:
  print("no Source dir")
# search decompile / tools for Key
for root,dirs,files in os.walk(r"D:\newMir3\tools\_decompile"):
  for f in files:
    if f.endswith((".cs",".txt")) and ("Key" in f or "Dialog" in f or "Tip" in f):
      print(os.path.join(root,f))
# strings in Library via powershell Select-String won't work on binary easily
# read 啊斌 jewelry section
t=open(r"D:\newMir3\Scripts\Npc\边境城市\啊斌.py",encoding="utf-8").read().splitlines()
for i,l in enumerate(t):
  if any(k in l for k in ["首饰","合成","Refine","DialogType","石榴","Ore","成功率","40","ItemType"]):
    if 550 <= i+1 <= 720 or "DialogType" in l or "首饰合成" in l or "Menu == 2" in l or "Menu == 3" in l:
      print(f"{i+1}|{l}")
print("==== menus near start ====")
for i,l in enumerate(t[:120]):
  print(f"{i+1}|{l}")

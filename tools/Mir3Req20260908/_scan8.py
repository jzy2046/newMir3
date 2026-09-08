import sys, os
sys.stdout.reconfigure(encoding="utf-8")
# read tip divider section
p=r"D:\newMir3\Source\145Client\Scenes\GameScene.cs"
lines=open(p,encoding="utf-8",errors="ignore").readlines()
for i in range(4720, 4950):
  if i < len(lines):
    print(f"{i+1}|{lines[i].rstrip()}")
print("====find NPCAccessoryCombineDialog====")
for root,dirs,files in os.walk(r"D:\newMir3\Source"):
  for f in files:
    if "AccessoryCombine" in f or "ItemLabel" in f or "ItemInfo" in f and f.endswith(".cs"):
      print(os.path.join(root,f))

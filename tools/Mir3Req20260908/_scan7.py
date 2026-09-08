import sys, os
sys.stdout.reconfigure(encoding="utf-8")
p=r"D:\newMir3\Source\145Client\Scenes\GameScene.cs"
count=0
with open(p,encoding="utf-8",errors="ignore") as fh:
  for i,line in enumerate(fh,1):
    if any(k in line for k in ["AccessoryCombine","分割线","ItemTip","石榴","结晶","Identify","赞助币","元宝"]):
      print(f"{i}|{line.rstrip()[:180]}")
      count+=1
      if count>60: break
print("done", count)
# list csproj under Source
for root,dirs,files in os.walk(r"D:\newMir3\Source"):
  for f in files:
    if f.endswith(".csproj"):
      print("CSPROJ", os.path.join(root,f)[12:])

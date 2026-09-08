import sys
sys.stdout.reconfigure(encoding="utf-8")
lines=open(r"D:\newMir3\Source\145Client\Scenes\GameScene.cs",encoding="utf-8",errors="ignore").readlines()
for i in range(2746, 3120):
  print(f"{i+1}|{lines[i].rstrip()}")

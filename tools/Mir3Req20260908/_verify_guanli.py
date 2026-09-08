import sys
sys.stdout.reconfigure(encoding="utf-8")
lines=open(r"D:\newMir3\Scripts\Npc\管理中心.py",encoding="utf-8").read().splitlines()
# print Menu 4 and handlers and main menu
for i,l in enumerate(lines):
  if "Menu == 4" in l or "Menu == 111" in l or "Menu == 114" in l or "主菜单" in l or "碎片分解" in l or "技能书兑换" in l:
    print(f"{i+1}|{l}")
print("==== MENU4 BLOCK ====")
for i in range(216, 280):
  if i < len(lines):
    print(f"{i+1}|{lines[i]}")
print("==== HANDLER 111-114 ====")
for i,l in enumerate(lines):
  if "Menu == 111" in l:
    for j in range(i, i+40):
      print(f"{j+1}|{lines[j]}")
    break
print("==== MAIN ====")
for i,l in enumerate(lines):
  if "#主菜单" in l:
    for j in range(i, min(i+20,len(lines))):
      print(f"{j+1}|{lines[j]}")
    break

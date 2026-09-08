import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
p=r"D:\newMir3\Source\145Client\Scenes\GameScene.cs"
lines=open(p,encoding="utf-8",errors="ignore").readlines()
print("AddItemLabelDivider calls:")
for i,l in enumerate(lines,1):
  if "AddItemLabelDivider" in l:
    print(f"{i}|{l.rstrip()[:140]}")
print("====CreateItemLabel / ItemType equipment checks====")
for i,l in enumerate(lines,1):
  if any(k in l for k in ["CreateItemLabel","IsEquipment","ItemType.","装备","AddItemLabelDivider","MouseItem.Info.ItemType"]):
    if "CreateItemLabel" in l or "AddItemLabelDivider" in l or ("ItemType" in l and ("Weapon" in l or "Armour" in l or "Nothing" in l or "Consumable" in l or "Material" in l)):
      print(f"{i}|{l.rstrip()[:160]}")
# find CreateItemLabel function start
for i,l in enumerate(lines,1):
  if "void CreateItemLabel" in l or "CreateItemLabel(" in l and "void" in l:
    print("FOUND", i, l.strip())

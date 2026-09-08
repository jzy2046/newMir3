import sys,re
sys.stdout.reconfigure(encoding="utf-8")
t=open(r"D:\newMir3\Scripts\Npc\道馆技能付费鉴定.py",encoding="utf-8").read()
# show unique GameGold comparison patterns
pats=set(re.findall(r".{0,20}GameGold.{0,30}", t))
for p in sorted(pats)[:40]:
    print(repr(p))
print("--- SubGameGold unique ---")
pats2=set(re.findall(r"SubGameGold\([^)]+\)", t))
for p in sorted(pats2):
    print(p, t.count(p))

import sys, re, shutil
sys.stdout.reconfigure(encoding="utf-8")
p = r"D:\newMir3\Scripts\Npc\道馆技能付费鉴定.py"
shutil.copy2(p, p + ".bak_req20260908")
t = open(p, encoding="utf-8").read()
# User-facing 元宝 -> 赞助币
c1 = t.count("元宝")
t = t.replace("元宝", "赞助币")
# Cost 10 GameGold -> 100 for paid identify
# Patterns: GameGold < 10 / SubGameGold(Sender,10) near identify — but careful not to change unrelated
# Count patterns
print("after rename 赞助币", t.count("赞助币"))
print("GameGold < 10", t.count("GameGold < 10"))
print("SubGameGold(Sender,10)", t.count("SubGameGold(Sender,10)"))
print("花费10赞助币", t.count("花费10赞助币"))
# If all GameGold < 10 in this file are paid identify, bump to 100
t2 = t.replace("花费10赞助币", "花费100赞助币")
t2 = t2.replace("Sender.GameGold < 10)", "Sender.GameGold < 100)")
t2 = t2.replace("SubGameGold(Sender,10)", "SubGameGold(Sender,100)")
# also possible spacing
t2 = t2.replace("Sender.GameGold < 10 ", "Sender.GameGold < 100 ")
print("GameGold < 100", t2.count("GameGold < 100"))
print("SubGameGold(Sender,100)", t2.count("SubGameGold(Sender,100)"))
print("花费100赞助币", t2.count("花费100赞助币"))
print("remaining GameGold < 10", t2.count("GameGold < 10"))
open(p, "w", encoding="utf-8").write(t2)
dep = r"D:\newMir3\deploy_to_Mir3service\Scripts\Npc\道馆技能付费鉴定.py"
import os
if os.path.exists(os.path.dirname(dep)):
    shutil.copy2(p, dep)
    print("synced deploy identify")

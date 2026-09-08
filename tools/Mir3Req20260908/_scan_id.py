import sys, shutil, os, re
sys.stdout.reconfigure(encoding="utf-8")
# sync 管理中心 to deploy
src=r"D:\newMir3\Scripts\Npc\管理中心.py"
dep=r"D:\newMir3\deploy_to_Mir3service\Scripts\Npc\管理中心.py"
if os.path.exists(os.path.dirname(dep)):
    shutil.copy2(src, dep)
    print("synced 管理中心")

# paid identify: replace 元宝 display in 道馆技能付费鉴定 if any, and check GameGold cost 100
p=r"D:\newMir3\Scripts\Npc\道馆技能付费鉴定.py"
t=open(p,encoding="utf-8").read()
print("付费鉴定 元宝", t.count("元宝"), "GameGold", t.count("GameGold"), "赞助币", t.count("赞助币"))
# show first GameGold / 元宝 contexts
for k in ["元宝", "GameGold", "赞助"]:
    i=t.find(k)
    if i>=0:
        line=t[:i].count("\n")+1
        print(k, "first L", line, t[t.rfind("\n",0,i)+1:t.find("\n",i)][:120])

# Also check if there's a separate paid identify with GameGold 100
for root,dirs,files in os.walk(r"D:\newMir3\Scripts"):
  for f in files:
    if not f.endswith(".py"): continue
    pp=os.path.join(root,f)
    tt=open(pp,encoding="utf-8",errors="ignore").read()
    if "付费鉴定" in tt or ("鉴定" in f and "GameGold" in tt):
      if "GameGold" in tt or "元宝" in tt:
        print("FILE", pp[12:], "元宝", tt.count("元宝"), "GameGold", tt.count("GameGold"))

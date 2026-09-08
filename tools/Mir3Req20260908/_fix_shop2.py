import sys, shutil, os
sys.stdout.reconfigure(encoding="utf-8")
shop = r"D:\newMir3\Scripts\Npc\商店列表.py"
t = open(shop, encoding="utf-8").read()
t2 = t.replace("('大护身符',float(1)),", "('护身符（大）',float(1)),")
t2 = t2.replace("('大神圣护身符',float(1)),", "('神圣护身符（大）',float(1)),")
t2 = t2.replace("('大暗黑护身符',float(1)),", "('暗黑护身符（大）',float(1)),")
open(shop,"w",encoding="utf-8").write(t2)
print("replaced", t!=t2)
dep=r"D:\newMir3\deploy_to_Mir3service\Scripts\Npc\商店列表.py"
if os.path.exists(dep):
    shutil.copy2(shop, dep)
    print("synced")
print(t2[t2.find("zahuodiangoodslist"):])

import sys, re, shutil, datetime, os
sys.stdout.reconfigure(encoding="utf-8")
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
bak_dir = rf"D:\newMir3\Scripts\_bak_req20260908_{stamp}"
os.makedirs(bak_dir, exist_ok=True)

def backup(path):
    rel = os.path.relpath(path, r"D:\newMir3\Scripts")
    dest = os.path.join(bak_dir, rel.replace("\\","__"))
    shutil.copy2(path, dest)
    return dest

# ========== 1) 商店列表 ==========
shop = r"D:\newMir3\Scripts\Npc\商店列表.py"
backup(shop)
t = open(shop, encoding="utf-8").read()
# Replace zahuodiangoodslist
new_zahuo = '''zahuodiangoodslist=[
(\'大护身符\',float(1)),
(\'大神圣护身符\',float(1)),
(\'大暗黑护身符\',float(1)),
(\'灵魂护身符（小）\',float(1)),
]
'''
# try alternate names if needed - will verify in DB
t2, n = re.subn(r"zahuodiangoodslist=\[[^\]]*\]", new_zahuo.strip(), t, count=1, flags=re.S)
if n!=1:
    print("FAIL zahuo replace", n)
else:
    t=t2
    print("OK zahuo")

# Update yaodian - add specials; keep existing and append if missing
if "金创药（特）" not in t and "金疮药（特）" not in t:
    t = t.replace(
        "yaodiangoodslist=[\n('金创药（小）',float(1)),\n('金创药（中）',float(1)),\n('金创药（大）',float(1)),\n('魔法药（小）',float(1)),\n('魔法药（中）',float(1)),\n('魔法药（大）',float(1)),\n('太阳水',float(1))]",
        "yaodiangoodslist=[\n('金创药（小）',float(1)),\n('金创药（中）',float(1)),\n('金创药（大）',float(1)),\n('金创药（特）',float(1)),\n('魔法药（小）',float(1)),\n('魔法药（中）',float(1)),\n('魔法药（大）',float(1)),\n('魔法药（特）',float(1)),\n('太阳水',float(1)),\n('强效太阳水',float(1))]"
    )
    print("OK yaodian append")
else:
    print("yaodian already has specials?")
open(shop,"w",encoding="utf-8").write(t)

# ========== 2) 便捷传送 元宝->赞助币, remove 元宝地图传送 ==========
tp = r"D:\newMir3\Scripts\Npc\便捷传送.py"
backup(tp)
t = open(tp, encoding="utf-8").read()
# text replacements for display (keep GameGold API)
repls = [
    ("我这里可以用元宝兑换金币", "我这里可以用赞助币兑换金币"),
    ("元宝兑换", "赞助币兑换"),
    ("你没有足够的元宝", "你没有足够的赞助币"),
    ("费用10元宝起", "费用10赞助币起"),
    ("[元宝换金币:", "[赞助币换金币:"),
    ("元宝传送", "赞助币传送"),
]
for a,b in repls:
    c=t.count(a)
    t=t.replace(a,b)
    print(f"tp replace {a!r} -> {c}")

# Remove 元宝地图传送 section from main menu: lines with 元宝地图传送 header and [赞助币传送:50] / [元宝传送:50]
# After rename it may be 赞助币地图传送 if we replaced 元宝传送 inside 元宝地图传送 incorrectly
# Fix: 元宝地图传送 -> should be deleted entirely, not renamed
t = t.replace("赞助币地图传送", "元宝地图传送")  # undo if wrongly renamed from 元宝地图传送 containing 元宝传送 substring... 
# Actually "元宝地图传送".replace("元宝传送","赞助币传送") would become "赞助币传送图传送" - check
print("contains 元宝地图传送", "元宝地图传送" in t)
print("contains 赞助币传送图", "赞助币传送图" in open(tp,encoding='utf-8').read() if False else "")
# re-read careful - we already mutated. Check bad replace
if "赞助币传送图传送" in t:
    t = t.replace("赞助币传送图传送", "元宝地图传送")
    print("fixed bad replace")
# Remove menu block: the header and link for 元宝地图传送 / [赞助币传送:50] or [元宝传送:50]
t2 = re.sub(r"\s*<font color=\\\"0xffff0000\\\">元宝地图传送</font>\s*\n\s*\[赞助币传送:50\]\s*\n?", "\n", t)
t2 = re.sub(r"\s*<font color=\\\"0xffff0000\\\">元宝地图传送</font>\s*\n\s*\[元宝传送:50\]\s*\n?", "\n", t2)
# also plain without font
t2 = re.sub(r"\s*\[赞助币传送:50\]\s*\n?", "\n", t2)
if t2==t:
    print("WARN map teleport menu pattern not matched, dumping nearby")
    idx=t.find("地图传送")
    while idx>=0:
        print(repr(t[max(0,idx-80):idx+80]))
        idx=t.find("地图传送", idx+1)
else:
    t=t2
    print("OK removed 元宝地图传送 menu entry")

# Also disable Menu == 50 handler content? Keep handlers but menu gone is enough.
# Replace remaining standalone 元宝 that are user-facing (not comments)
# careful with 元宝 already handled
open(tp,"w",encoding="utf-8").write(t)
print("tp remaining 元宝 count", t.count("元宝"))

print("BAK", bak_dir)

import sys, re, shutil
sys.stdout.reconfigure(encoding="utf-8")
# Patch 便捷传送1 same as 便捷传送
for name in ["便捷传送1.py"]:
    tp = rf"D:\newMir3\Scripts\Npc\{name}"
    shutil.copy2(tp, tp + ".bak_req20260908")
    t = open(tp, encoding="utf-8").read()
    repls = [
        ("我这里可以用元宝兑换金币", "我这里可以用赞助币兑换金币"),
        ("元宝兑换", "赞助币兑换"),
        ("你没有足够的元宝", "你没有足够的赞助币"),
        ("费用10元宝起", "费用10赞助币起"),
        ("[元宝换金币:", "[赞助币换金币:"),
        ("元宝传送", "赞助币传送"),
    ]
    for a,b in repls:
        t = t.replace(a,b)
    if "赞助币传送图传送" in t:
        t = t.replace("赞助币传送图传送", "元宝地图传送")
    t2 = re.sub(r"\s*<font color=\\\"0xffff0000\\\">元宝地图传送</font>\s*\n\s*\[赞助币传送:50\]\s*\n?", "\n", t)
    t2 = re.sub(r"\s*<font color=\\\"0xffff0000\\\">元宝地图传送</font>\s*\n\s*\[元宝传送:50\]\s*\n?", "\n", t2)
    t2 = re.sub(r"\s*\[赞助币传送:50\]\s*\n?", "\n", t2)
    t = t2
    open(tp,"w",encoding="utf-8").write(t)
    print(name, "元宝 left", t.count("元宝"), "赞助币", t.count("赞助币"), "地图传送 menu gone", "[赞助币传送:50]" not in t and "[元宝传送:50]" not in t)

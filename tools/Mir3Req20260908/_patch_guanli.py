import sys, os, re, shutil, datetime
sys.stdout.reconfigure(encoding="utf-8")
path = r"D:\newMir3\Scripts\Npc\管理中心.py"
bak = path + ".bak_req20260908"
if not os.path.exists(bak):
    shutil.copy2(path, bak)

t = open(path, encoding="utf-8").read()

# Helper text template for skill book exchange (relics only)
def help_text(buttons):
    return (
        '<font color=\\"0xffffff00\\">1、</font>技能书兑换仅消耗遗物，无需击杀数量\\n'
        '\t\t\t<font color=\\"0xffffff00\\">2、</font>兑换后扣除对应遗物\\n'
        '\t\t\t<font color=\\"0xffffff00\\">3、</font>您可以兑换以下高级技能书籍（秘籍）：</font>\\n'
        '\t\t\t\\n'
        '\t\t\t<font color=\\"0xff00ccff\\">1000个遗物 兑换:</font>\\n'
        '\\n'
        '\t\t\t<font color=\\"0xff00ff00\\">「十方斩」</font>   <font color=\\"0xff00ff00\\">「魄冰刺」</font>   <font color=\\"0xff00ff00\\">「灵魂分裂」</font>\\n'
        '\t\t\t\\n'
        '\t\t\t<font color=\\"0xff00ccff\\">2000个遗物 兑换:</font>\\n'
        '\\n'
        '\t\t\t<font color=\\"0xff00ff00\\">「乾坤大挪移」</font> <font color=\\"0xff00ff00\\">「怒神霹雳」</font> <font color=\\"0xff00ff00\\">「移花接玉」</font>\\n'
        '\t\t\t\\n'
        '\t\t\t<font color=\\"0xff00ccff\\">3000个遗物 兑换:</font>\\n'
        '\\n'
        '\t\t\t<font color=\\"0xff00ff00\\">「铁布衫」</font>  <font color=\\"0xff00ff00\\">「焰天火雨」</font>  <font color=\\"0xff00ff00\\">「妙影无踪」</font>\\n'
        '\t\t\t\\n'
        '\t\t\t<font color=\\"0xffFF00CC\\">4000个遗物 兑换:</font>\\n'
        '\\n'
        '\t\t\t<font color=\\"0xff00ff00\\">「破血狂杀」</font>  <font color=\\"0xff00ff00\\">「凝血离魂」</font> <font color=\\"0xff00ff00\\">「阴阳法环」</font>\\n'
        '\\n'
        '\\n'
        f'\t\t\t{buttons}\\n'
        '\t\t\t'
    )

# Replace each class branch of Menu == 4
# Find from "elif (Menu == 4):" to "elif Menu in []:" or next major section
m4 = re.search(r"\telif \(Menu == 4\):", t)
if not m4:
    raise SystemExit("Menu 4 not found")
# find end: "elif Menu in []:" or "# 特色称号系统"
end = t.find("elif Menu in []:", m4.start())
if end < 0:
    end = t.find("# 特色称号系统", m4.start())
if end < 0:
    raise SystemExit("end of menu4 not found")

wizard_btns = "[［魄冰刺］:211] [［怒神霹雳］:212] [［焰天火雨］:213] [［凝血离魂］:214]"
tao_btns = "[［灵魂分裂］:311] [［移花接玉］:312] [［妙影无踪］:314] [［阴阳法环］:313]"
# Assassin: only remaining skills? All assassin-specific ones were deleted (鹰击/风之守护/狂涛涌泉/最后抵抗).
# Assassin players can still exchange nothing class-specific from rows - show same general help with no buttons or warrior ones?
# Keep assassin branch with note that assassin exclusive books removed; they can still use? Looking at original, assassin only had those 4 buttons.
# After deletion assassin has no exchangeable books in this NPC. Show help with empty buttons / close.
assassin_btns = "[关闭:0]"
warrior_btns = "[［十方斩］:111] [［乾坤大挪移］:112] [［铁布衫］:113] [［破血狂杀］:114]"

new_m4 = f'''\telif (Menu == 4):
\t\tif Sender.Class == Sender.Class.Wizard:
\t\t\tsay = """{help_text(wizard_btns)}"""
\t\telif Sender.Class == Sender.Class.Taoist:
\t\t\tsay = """{help_text(tao_btns)}"""
\t\telif Sender.Class == Sender.Class.Assassin:
\t\t\tsay = """{help_text(assassin_btns)}"""
\t\telse:
\t\t\tsay = """{help_text(warrior_btns)}"""
\t'''

t = t[:m4.start()] + new_m4 + t[end:]
print("replaced menu4, next starts with", repr(t[m4.start():m4.start()+40]))

# Rewrite exchange handlers: remove kill count; row4 uses 4000 relics; remove 411-414 assassin; remove 115/315 last-row specials
# Replace each Menu == 111 etc. block with simplified version

def relic_handler(menu, cost, item_name):
    return f'''\telif (Menu == {menu}):
\t\tif (Sender.GetItemCount("遗物") < {cost}):
\t\t\tsay = """你的遗物数量不足，请继续努力。
\t\t\t
\t\t\t[离开:0]"""
\t\telse:
\t\t\tSender.TakeItem("遗物",{cost})
\t\t\tSender.GiveItem("{item_name}",1)
\t\t\tsay = """恭喜你兑换成功。
\t\t\t
\t\t\t[离开:0]"""
'''

# Map of menu -> (cost, item)
exchanges = {
    111: (1000, "十方斩（秘籍）"),
    112: (2000, "乾坤大挪移（秘籍）"),
    113: (3000, "铁布衫（秘籍）"),
    114: (4000, "破血狂杀（秘籍）"),
    211: (1000, "魄冰刺（秘籍）"),
    212: (2000, "怒神霹雳（秘籍）"),
    213: (3000, "焰天火雨（秘籍）"),
    214: (4000, "凝血离魂（秘籍）"),
    311: (1000, "灵魂分裂（秘籍）"),
    312: (2000, "移花接玉（秘籍）"),
    314: (3000, "妙影无踪（秘籍）"),
    313: (4000, "阴阳法环（秘籍）"),
}

# Remove old handlers for 111-115, 211-214, 311-315, 411-414 by replacing with new ones
# Find start of elif (Menu == 111): through end of Menu == 414 block (before elif Menu == 15)

start_h = t.find("\telif (Menu == 111):")
if start_h < 0:
    raise SystemExit("handler 111 missing")
end_h = t.find("\telif (Menu == 15):", start_h)
if end_h < 0:
    raise SystemExit("menu 15 missing after handlers")

new_handlers = "\n".join(relic_handler(m,c,i) for m,(c,i) in exchanges.items()) + "\n"
t = t[:start_h] + new_handlers + t[end_h:]
print("replaced exchange handlers")

# Main menu cleanup
old_menu = '''\t\tsay = """[碎片分解:28]              [材料换书:13]              [军衔进阶:25] 
\t\t
\t\t[元宝经验:2]      [付费鉴定:34]      [元宝回收:300]
 \t\t
\t\t[首饰熔炼:15]       [装备刻名:27]    [技能书兑换:4]
\t\t
\t\t[生锈首饰:30]        [声望称号:1]   [特色称号:5]  [每日双倍:37]  

\t\t[一键特修:29]              [马店:302]               [在线泡点:301]  """'''

new_menu = '''\t\tsay = """[碎片分解:28]      [付费鉴定:34]      [首饰熔炼:15]
\t\t
\t\t[装备刻名:27]      [技能书兑换:4]      [生锈首饰:30]
\t\t
\t\t[每日双倍:37]      [一键特修:29]      [马店:302]"""'''

if old_menu not in t:
    # try flexible match
    m = re.search(r'\t\tsay = """\[碎片分解:28\].*?\[在线泡点:301\].*?"""', t, re.S)
    if not m:
        # show current else menu
        idx = t.rfind("#主菜单")
        print("CURRENT MENU AREA:")
        print(t[idx:idx+500])
        raise SystemExit("main menu pattern not found")
    t = t[:m.start()] + new_menu + t[m.end():]
    print("replaced main menu via regex")
else:
    t = t.replace(old_menu, new_menu)
    print("replaced main menu exact")

open(path, "w", encoding="utf-8").write(t)
print("DONE 管理中心 len", len(t))
# sanity
for k in ["鹰击", "风之守护", "狂涛涌泉", "最后抵抗", "材料换书", "军衔进阶", "元宝经验", "元宝回收", "声望称号", "特色称号:5", "在线泡点", "GV_KILLMON"]:
    print(k, "count", t.count(k))

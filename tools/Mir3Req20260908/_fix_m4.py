import sys, re
sys.stdout.reconfigure(encoding="utf-8")
path = r"D:\newMir3\Scripts\Npc\管理中心.py"
t = open(path, encoding="utf-8").read()

def make_say(buttons):
    # real newlines inside triple quotes
    return f'''say = """<font color=\\"0xffffff00\\">1、</font>技能书兑换仅消耗遗物，无需击杀数量
			<font color=\\"0xffffff00\\">2、</font>兑换后扣除对应遗物
			<font color=\\"0xffffff00\\">3、</font>您可以兑换以下高级技能书籍（秘籍）：
			
			<font color=\\"0xff00ccff\\">1000个遗物 兑换:</font>

			<font color=\\"0xff00ff00\\">「十方斩」</font>   <font color=\\"0xff00ff00\\">「魄冰刺」</font>   <font color=\\"0xff00ff00\\">「灵魂分裂」</font>
			
			<font color=\\"0xff00ccff\\">2000个遗物 兑换:</font>

			<font color=\\"0xff00ff00\\">「乾坤大挪移」</font> <font color=\\"0xff00ff00\\">「怒神霹雳」</font> <font color=\\"0xff00ff00\\">「移花接玉」</font>
			
			<font color=\\"0xff00ccff\\">3000个遗物 兑换:</font>

			<font color=\\"0xff00ff00\\">「铁布衫」</font>  <font color=\\"0xff00ff00\\">「焰天火雨」</font>  <font color=\\"0xff00ff00\\">「妙影无踪」</font>
			
			<font color=\\"0xffFF00CC\\">4000个遗物 兑换:</font>

			<font color=\\"0xff00ff00\\">「破血狂杀」</font>  <font color=\\"0xff00ff00\\">「凝血离魂」</font> <font color=\\"0xff00ff00\\">「阴阳法环」</font>


			{buttons}
			"""'''

wizard_btns = "[［魄冰刺］:211] [［怒神霹雳］:212] [［焰天火雨］:213] [［凝血离魂］:214]"
tao_btns = "[［灵魂分裂］:311] [［移花接玉］:312] [［妙影无踪］:314] [［阴阳法环］:313]"
assassin_btns = "[关闭:0]"
warrior_btns = "[［十方斩］:111] [［乾坤大挪移］:112] [［铁布衫］:113] [［破血狂杀］:114]"

new_m4 = f'''\telif (Menu == 4):
\t\tif Sender.Class == Sender.Class.Wizard:
\t\t\t{make_say(wizard_btns)}
\t\telif Sender.Class == Sender.Class.Taoist:
\t\t\t{make_say(tao_btns)}
\t\telif Sender.Class == Sender.Class.Assassin:
\t\t\t{make_say(assassin_btns)}
\t\telse:
\t\t\t{make_say(warrior_btns)}
\t'''

m4 = re.search(r"\telif \(Menu == 4\):", t)
end = t.find("elif Menu in []:", m4.start())
t = t[:m4.start()] + new_m4 + t[end:]
open(path,"w",encoding="utf-8").write(t)
# verify no literal backslash-n in menu4 say (except font escapes)
block = t[m4.start():t.find("elif Menu in []:", m4.start())]
print("literal \\\\n count in block", block.count("\\n"))
print("OK sample line:")
print(block.splitlines()[2][:120])

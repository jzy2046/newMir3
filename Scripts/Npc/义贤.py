# -*- coding: utf-8 -*-
#载入模块SYS
import sys
#引用模块的地址
from Globals import *
import collections
import clr
clr.AddReference("Library")
from Library import *
from Defines import *   #调用变量模块
import NpcEvent
from 主线任务奖励 import *
######################################################
#本函数为程序调用的固定格式 函数名和参数数量不要修改
#OnClick(Self, Sender, Menu)
##参数 Self：NPC的类
##   Sender：玩家的类
##     Menu：菜单的类
#####################################################
def OnClick(args):
	Self = args[0]
	Sender = args[1]
	Menu = args[2]
	Dict={}
#红名判断	
	if(Sender.Stats[Stat.PKPoint] > 199):
		say = """我不愿意和你这样的人进行交易。
		
		[关闭:0]"""	
#跳转菜单买马选择
	elif (Menu == 110):
 		say = """欢迎来到我的马厩。
			直接使用金币购买马匹，无需马牌，无等级限制。
			
			<font color=\"0xff00ff00\">『马匹属性介绍』</font>   
			 黄骠马：舒适+5
			 白马：舒适+5、负重+400，防魔御3-3,攻魔道：3-3
			 绝影：舒适+5、负重+800，防魔御5-5,攻魔道：5-5
			 赤兔马：舒适+5、负重+1600，防魔御8-8,攻魔道：8-8
			
			[买黄骠马:1]   （50万金币）
			[买的卢马:2]   （500万金币）
			[买名驹绝影:3] （5000万金币）
			[买名驹赤兔:4] （2亿金币）

			[我要卖马:5]

			[关闭:0]"""
#跳转菜单马匹购买
	elif (Menu == 1):
		say = """马匹购买信息：
		
			类型：黄骠马
			金额：500,000 金币
		
			如果你想买这匹马，请 [在这里签字:11]
		
			[返回:99]
			[关闭:0]"""	
	elif(Menu == 2):
		say = """马匹购买信息：
		
			类型：白马马
			金额：5,000,000 金币
		
			如果你想买这匹马，请 [在这里签字:21]
		
			[返回:99]
			[关闭:0]"""
	elif(Menu == 3):
		say = """马匹购买信息：
		
			类型：绝影马
			金额：50,000,000 金币
		
			如果你想买这匹马，请 [在这里签字:31]
		
			[返回:99]
			[关闭:0]"""
	elif(Menu == 4):
		say = """马匹购买信息：
		
			类型：赤兔马
			金额：200000000 金币
		
			如果你想买这匹马，请 [在这里签字:41]
		
			[返回:99]
			[关闭:0]"""
	elif(Menu == 11):
		if(Sender.Gold < 500000):
			say = """你买不起这匹马，
			等你有钱了再来吧。
			
			[返回:99]
			[关闭:0]"""
		elif(not(Sender.Character.Horse ==HorseType.None)):
			say = """你现在已经有一匹马了。
			如果你想买一匹新马，请卖掉你现有的马。
			
			[返回:99]
			[关闭:0]"""
		else:
			SubGold(Sender,500000)
			GiveHose(Sender,HorseType.Brown)
			say = """恭喜你买了一匹新马。
			请好好照顾它。
			
			[关闭:0]"""
	elif(Menu == 21):
		if(Sender.Gold < 5000000):
			say = """你买不起这匹马，
			等你有钱了再来吧。
			
			[返回:99]
			[关闭:0]"""
		elif(not(Sender.Character.Horse ==HorseType.None)):
			say = """你现在已经有一匹马了。
			如果你想买一匹新马，请卖掉你现有的马。
			
			[返回:99]
			[关闭:0]"""
		else:
			SubGold(Sender,5000000)
			GiveHose(Sender,HorseType.White)
			say = """恭喜你买了一匹新马。
			请好好照顾它。
			
			[关闭:0]"""
	elif(Menu == 31):
		if(Sender.Gold < 50000000):
			say = """你买不起这匹马，
			等你有钱了再来吧。
			
			[返回:99]
			[关闭:0]"""
		elif(not(Sender.Character.Horse ==HorseType.None)):
			say = """你现在已经有一匹马了。
			如果你想买一匹新马，请卖掉你现有的马。
			
			[返回:99]
			[关闭:0]"""
		else:
			SubGold(Sender,50000000)
			GiveHose(Sender,HorseType.Red)
			say = """恭喜你买了一匹新马。
			请好好照顾它。
			
			[关闭:0]"""
	elif(Menu == 41):
		if(Sender.Gold < 200000000):
			say ="""你的金币不够。
			请准备好足够的金币再来。
[返回:99]
			[关闭:0]"""
		elif(not(Sender.Character.Horse ==HorseType.None)):
			say = """你现在已经有一匹马了。
			如果你想买一匹新马，请卖掉你现有的马。
			
			[返回:99]
			[关闭:0]"""
		else:
			SubGold(Sender,200000000)
			GiveHose(Sender,HorseType.Black)
			say = """恭喜你买了一匹新马。
			请好好照顾它。
			
			[关闭:0]"""
#跳转菜单马匹出售			
	elif (Menu == 5):
		say = """看到一匹马将要被主人抛弃，我很难过。
		我的报价如下：
		
		黄骠马- 250,000 金币
		的卢 - 2,500,000 金币
		绝影 - 25,000,000 金币
		赤兔马 - 100,000,000 金币
		
		[返回:99]
		[卖马:51]
		
		[关闭:0]"""			
	elif(Menu == 51):
		horse = Sender.Character.Horse
		if(horse ==HorseType.None):
			say = """我没办法从你那买马。
			你目前一匹马也没有。
			
			[返回:99]
			[关闭:0]"""
		elif (horse == HorseType.Brown):
			say = """马匹出售信息：
			
			类型：黄骠马
			金额：250,000 金币
			
			如果你想卖这匹马，请 [在这里签字:511]
			
			[返回:99]
			[关闭:0]"""
		elif(horse == HorseType.White):
			say = """马匹出售信息：
			
			类型：白马
			金额：2,500,000 金币
			
			如果你想卖这匹马，请 [在这里签字:511]
			
			[返回:99]
			[关闭:0]"""
		elif(horse == HorseType.Red):
			if(PlayerGetV(Sender,GV_PLAYER_REDHORSE)==0):        #判断是否金币或者元宝购买，通过变量判断
				say = """马匹出售信息：
				
				类型：绝影
				金额：10,000,000 金币
				
				如果你想卖这匹马，请 [在这里签字:511]
				
				[返回:99]
				[关闭:0]"""
			else:
				say = """马匹出售信息：
				
				类型：绝影
				金额：5,000 元宝
				
				如果你想卖这匹马，请 [在这里签字:511]
				
				[返回:99]
				[关闭:0]"""
		elif(horse == HorseType.Black):
			if(PlayerGetV(Sender,GV_PLAYER_BLACKHORSE)==0):        #判断是否金币或者元宝购买，通过变量判断
				say = """马匹出售信息：
				
				类型：赤兔马
				金额：50,000,000 金币
				
				如果你想卖这匹马，请 [在这里签字:511]
				
				[返回:99]
				[关闭:0]"""
				
			else:
				say = """马匹出售信息：
				
				类型：赤兔马
				金额：10,000 元宝
				
				如果你想卖这匹马，请 [在这里签字:511]
				
				[返回:99]
				[关闭:0]"""
		else:
			return
#跳转菜单马匹卖出			
	elif(Menu == 511):
		horse = Sender.Character.Horse
		say = """你已经卖了你的马。
		即使你给它喂胡萝卜，它不再爱你了。
			
		[返回:99]
			
		[关闭:0]"""
		if(horse ==HorseType.None):
			say = """我没办法从你那买马。
			你目前一匹马也没有。
			
			[返回:99]
			[关闭:0]"""
		elif (horse == HorseType.Brown):
			GiveGold(Sender,250000)	
			GiveHose(Sender,HorseType.None)
		elif(horse == HorseType.White):
			GiveGold(Sender,2500000)
			GiveHose(Sender,HorseType.None)
		elif(horse == HorseType.Red):
			if(PlayerGetV(Sender,GV_PLAYER_REDHORSE)==0):        #判断是否金币或者元宝购买，通过变量判断 
				GiveGold(Sender,25000000)
				GiveHose(Sender,HorseType.None)
			else:
				PlayerSetV(Sender,GV_PLAYER_REDHORSE,0)   #卖马时将变量归0
				GiveGameGold(Sender,5000)
				GiveHose(Sender,HorseType.None)
		elif(horse == HorseType.Black):
			if(PlayerGetV(Sender,GV_PLAYER_BLACKHORSE)==0):        #判断是否金币或者元宝购买，通过变量判断
				GiveGold(Sender,100000000)
				GiveHose(Sender,HorseType.None)
			else:
				PlayerSetV(Sender,GV_PLAYER_BLACKHORSE,0)   #卖马时将变量归0
				GiveGameGold(Sender,10000)
				GiveHose(Sender,HorseType.None)
		else: 
			return	
	elif (Menu == 6):
		say = """王小二那个朋友的女儿？
			可怜的小八啊……太年轻了只知道工作，还死了老婆，唯一剩下的一个女儿也变成了那样，以后可怎么办呢！ 
			
			[能给我讲讲她女儿失踪的那天发生的事儿吗？:10]"""		
	elif (Menu == 10):
		PlayerSetV(Sender,BV_NQ_MAIN,118)
		Sender.Connection.ReceiveChat("任务日志更新！", MessageType.System)
		say = """丽灵唯一的爱好就是骑着马去散心！
			本来小八他对女儿太过疼爱所以一直把她关在家里，所以我劝他别把女儿憋出病来。
			于是小八就花巨额给女儿买了一匹的卢让她骑。丽灵骑上那匹一点杂色都没有的的卢绕着村子那么一转，所有年轻男子的视线就都被吸引过去了！
			真的是个非常可爱的女孩啊！唉……
			咳！现在不是不是说这种话的时候……丽灵那天晚上很晚才伏在马背上回到马厩……不……确切地说是马儿驮着那个已经没有了魂魄的孩子自己找回家的。
			马回来的方向是西北方，是 半兽洞穴 的方向。从半兽洞穴附近的杂草被马蹄踩过的情形看来就是在那附近遭遇了不幸！
			
			[结束:0]"""
#主菜单
	else:
		if(PlayerGetV(Sender,BV_NQ_MAIN)==117):
			say = """欢迎来到我的马厩。
				这里有很多的马可供挑选。
			
				[查看:110] 马厩
				
				[询问:6] 关于王丽灵的事情
				
				[关闭:0]"""
		else:
			say = """欢迎来到我的马厩。
				这里有很多的马可供挑选。
				
				[查看:110] 马厩
				
				[关闭:0]"""

	Dict['Say']=say                         #定义聊天框对话内容
	return Dict
#####################################################################
#public enum HorseType : byte
#    {
#        None,       没马
#        Brown,      黄骠马
#        White,      的卢
#        Red,        绝影
#        Black,      赤兔马
#    }
#####################################################################
##卖马判断函数
def GiveHose(Sender,type):	
	Sender.Character.Horse = type;
	Sender.RemoveMount();
	Sender.RefreshStats();
	if (Sender.Character.Horse != HorseType.None):
		Sender.Mount();
		
NpcEvent.add_listener(54,"OnClick",OnClick)

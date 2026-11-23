# -*- coding: utf-8 -*-
#载入模块SYS
import sys
#引用模块的地址
import Globals
import clr
clr.AddReference("Library")
from Library import *
import collections
import NpcEvent
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
		str = """我不愿意和你这样的人进行交易。
		
		[关闭:0]"""
#跳转菜单1杂货	
	elif (Menu == 1):
		Dict['Goods'] =goods                #定义可购买商品
		Dict['Types'] =types		        #定义类别
		Dict['DialogType'] = NPCDialogType.BuySell  #类型为Library.Enums里的买卖类
		str = """有需要的东西就买吧，我这里什么都有。
		
		[关闭:0]"""
#跳转菜单2				
	elif (Menu == 2):
		str = """有人说看到了在沙漠遇难的船。
				
		[关闭:0]"""	
#跳转菜单3卖				
	elif (Menu == 3):
		Dict['Types'] =types		        #定义类别
		Dict['DialogType'] = NPCDialogType.RootSell   #类型为Library.Enums里的修理类
		str = """闲置不用的物品我出高价回收。
		
		[返回:99]
		[关闭:0]"""		
#主菜单
	else:
		str = """欢迎光临。你有什么事？
		
		[查看:1] 商店杂货
		[出售:3] 杂货
		[交谈:2]

		[关闭:0]"""
	Dict['Say']=str                         #定义聊天框对话内容
	return Dict
#类型为 Library.Enums里的其他类			
types =[ItemType.Nothing]
#商品列表  '商品名称'  商品价格比例,固定格式为float(1.5)比例倍数
goodslist=[
('随机传送卷',float(1)),
('回城卷',float(1)),
('修复油',float(1)),
('蜡烛',float(1)),
('亮蜡烛',float(1)),
('亮火把',float(1)),
('生锈师承戒指',float(1)),
('生锈龙马戒指',float(1)),
('生锈青云戒指',float(1)),
('生锈破荒项链',float(1)),
('生锈魔云项链',float(1)),
('生锈定心项链',float(1)),
('生锈金棱手镯',float(1)),
('生锈思过手镯',float(1)),
('生锈世尊手镯',float(1)),
('师承戒指',float(1)),
('龙马戒指',float(1)),
('青云戒指',float(1)),
('破荒项链',float(1)),
('魔云项链',float(1)),
('定心项链',float(1)),
('金棱手镯',float(1)),
('思过手镯',float(1)),
('世尊手镯',float(1)),
('金刚魔法指环',float(1)),
('金刚精神戒指',float(1)),
('金刚魔法手镯',float(1)),
('金刚防御手镯',float(1)),
('金刚铃铛',float(1)),
('麒麟宝铠（男）',float(1)),
('麒麟宝铠（女）',float(1)),
('仙风神袍（男）',float(1)),
('仙风神袍（女）',float(1)),
('阴阳圣衣（男）',float(1)),
('阴阳圣衣（女）',float(1)),
('血花落照（血）',float(1)),
('血花落照（花）',float(1)),
('血花落照（落）',float(1)),
('血花落照（照）',float(1)),
('黑天暗云（黑）',float(1)),
('黑天暗云（天）',float(1)),
('黑天暗云（暗）',float(1)),
('黑天暗云（云）',float(1)),
('九宫云雾（九）',float(1)),
('九宫云雾（宫）',float(1)),
('九宫云雾（云）',float(1)),
('九宫云雾（雾）',float(1)),
('万里碧海（万）',float(1)),
('万里碧海（里）',float(1)),
('万里碧海（碧）',float(1)),
('万里碧海（海）',float(1)),
('六棱戒',float(1)),
('紫金环',float(1)),
('武圣之戒',float(1)),
('七彩金环',float(1)),
('心魔戒指',float(1)),
('魔灵戒指',float(1)),
('天机戒指',float(1)),
('毁灭手镯',float(1)),
('如来手镯',float(1)),
('魔令手镯',float(1)),
('铁炼腕',float(1)),
('英雄手套',float(1)),
('火玉手镯',float(1)),
('心念手镯',float(1)),
('天机戒指',float(1)),
('毁灭魔链',float(1)),
('乾坤一气',float(1)),
('昏暗风印',float(1)),
('魔令项链',float(1)),
]

goods = collections.OrderedDict(goodslist)

NpcEvent.add_listener(318,"OnClick",OnClick)
# -*- coding: utf-8 -*-
# 载入模块SYS
import sys
# 引用模块的地址
from Globals import *
import clr
import random

clr.AddReference("Library")
from Library import *
import collections
import NpcEvent

from Utils.PlayerUtils import *


######################################################
# 本函数为程序调用的固定格式 函数名和参数数量不要修改
# OnClick(Self, Sender, Menu)
##参数 Self：NPC的类
##   Sender：玩家的类
##     Menu：菜单的类
#####################################################

ADD_SLOTS = {
	401: EquipmentSlot.Weapon,
	402: EquipmentSlot.Necklace,
	403: EquipmentSlot.BraceletL,
	404: EquipmentSlot.BraceletR,
	405: EquipmentSlot.RingL,
	406: EquipmentSlot.RingR,
	407: EquipmentSlot.Armour,
	408: EquipmentSlot.Helmet,
	409: EquipmentSlot.Shoes,
}

ADD_SLOT_NAME = {
	EquipmentSlot.Weapon: '武器',
	EquipmentSlot.Necklace: '项链',
	EquipmentSlot.BraceletL: '左手镯',
	EquipmentSlot.BraceletR: '右手镯',
	EquipmentSlot.RingL: '左戒指',
	EquipmentSlot.RingR: '右戒指',
	EquipmentSlot.Armour: '衣服',
	EquipmentSlot.Helmet: '头盔',
	EquipmentSlot.Shoes: '鞋子',
}

ELE_ATK = [
	Stat.FireAttack,
	Stat.IceAttack,
	Stat.LightningAttack,
	Stat.WindAttack,
	Stat.HolyAttack,
	Stat.DarkAttack,
	Stat.PhantomAttack,
]

ELE_RES = [
	Stat.FireResistance,
	Stat.IceResistance,
	Stat.LightningResistance,
	Stat.WindResistance,
	Stat.HolyResistance,
	Stat.DarkResistance,
	Stat.PhantomResistance,
]

ELE_ATK_NAME = {
	Stat.FireAttack: '火',
	Stat.IceAttack: '冰',
	Stat.LightningAttack: '雷',
	Stat.WindAttack: '风',
	Stat.HolyAttack: '神圣',
	Stat.DarkAttack: '暗黑',
	Stat.PhantomAttack: '幻影',
}

ELE_RES_NAME = {
	Stat.FireResistance: '火',
	Stat.IceResistance: '冰',
	Stat.LightningResistance: '雷',
	Stat.WindResistance: '风',
	Stat.HolyResistance: '神圣',
	Stat.DarkResistance: '暗黑',
	Stat.PhantomResistance: '幻影',
}

# kind: 0血量 1蓝量 2防御 3魔御 4魔法躲避 5准确 6敏捷 7幸运 8攻击速度 9爆率加成
EXTRA_ADD_STATS = (
	(0, Stat.Health, '血量'),
	(1, Stat.Mana, '蓝量'),
	(2, Stat.MaxAC, '防御'),
	(3, Stat.MaxMR, '魔御'),
	(4, Stat.MagicEvade, '魔法躲避'),
	(5, Stat.Accuracy, '准确'),
	(6, Stat.Agility, '敏捷'),
	(7, Stat.Luck, '幸运'),
	(8, Stat.AttackSpeed, '攻击速度'),
	(9, Stat.DropRate, '爆率加成'),
)

REMOVE_STATS = (
	(0, Stat.MaxDC, '破坏'),
	(1, Stat.MaxMC, '自然'),
	(2, Stat.MaxSC, '灵魂'),
	(3, Stat.FireAttack, '攻击元素火'),
	(4, Stat.IceAttack, '攻击元素冰'),
	(5, Stat.LightningAttack, '攻击元素雷'),
	(6, Stat.WindAttack, '攻击元素风'),
	(7, Stat.HolyAttack, '攻击元素神圣'),
	(8, Stat.DarkAttack, '攻击元素暗黑'),
	(9, Stat.PhantomAttack, '攻击元素幻影'),
	(10, Stat.FireResistance, '强元素火'),
	(11, Stat.IceResistance, '强元素冰'),
	(12, Stat.LightningResistance, '强元素雷'),
	(13, Stat.WindResistance, '强元素风'),
	(14, Stat.HolyResistance, '强元素神圣'),
	(15, Stat.DarkResistance, '强元素暗黑'),
	(16, Stat.PhantomResistance, '强元素幻影'),
	(17, Stat.Health, '血量'),
	(18, Stat.Mana, '蓝量'),
	(19, Stat.MaxAC, '防御'),
	(20, Stat.MaxMR, '魔御'),
	(21, Stat.MagicEvade, '魔法躲避'),
	(22, Stat.Accuracy, '准确'),
	(23, Stat.Agility, '敏捷'),
	(24, Stat.Luck, '幸运'),
	(25, Stat.AttackSpeed, '攻击速度'),
	(26, Stat.DropRate, '爆率加成'),
)

SAY_ADD_MAIN = (
	'给装备加点\n\n'
	'请先穿戴要加点的装备，点一次增加 1 点，不需要任何消耗。\n'
	'去掉额外属性时，一次只扣 1 点，不会扣装备原来的属性。\n\n'
	'[武器:401] [衣服:407] [头盔:408] [鞋子:409]\n'
	'\n'
	'[项链:402]\n'
	'\n'
	'[左手镯:403] [右手镯:404]\n'
	'\n'
	'[左戒指:405] [右戒指:406]\n'
	'\n'
	'[返回:99]\n'
)

def stat_total(eq, stat):
	return int(eq.Info.Stats[stat]) + int(eq.Stats[stat])

def added_amount(eq, stat):
	total = 0
	for s in eq.AddedStats:
		if s.Stat == stat:
			total += int(s.Amount)
	return total

def cleanup_zero_stats(Sender, eq):
	# 金额为 0 的额外属性会让客户端显示 破坏 0-0，清掉后本来没有的属性就不再显示
	removed = 0
	for i in range(eq.AddedStats.Count - 1, -1, -1):
		s = eq.AddedStats[i]
		if int(s.Amount) == 0:
			s.Delete()
			removed += 1
	if removed > 0:
		eq.StatsChanged()
		Sender.ItemCompleteRefresh(eq.Index)
	return removed

def parse_add_kind(menu):
	# 510-599：显示某部位的加点选项 / 攻击元素 / 强元素 / 去掉额外属性
	if menu < 510 or menu > 599:
		return None
	body = menu - 510
	slot_off = body // 10
	kind = body % 10
	if slot_off > 8 or kind not in (1, 2, 7):
		return None
	return 401 + slot_off, kind

def parse_add_stat(menu):
	# 610-699：直接加点 破坏/全系魔法/自然/灵魂
	if menu < 610 or menu > 699:
		return None
	body = menu - 610
	slot_off = body // 10
	kind = body % 10
	if slot_off > 8 or kind < 3 or kind > 6:
		return None
	return 401 + slot_off, kind

def parse_add_ele(menu):
	# 710-799 攻击元素；810-899 强元素
	if menu >= 710 and menu <= 799:
		group = 'atk'
		body = menu - 710
	elif menu >= 810 and menu <= 899:
		group = 'res'
		body = menu - 810
	else:
		return None
	slot_off = body // 10
	ele_index = body % 10
	if slot_off > 8 or ele_index > 6:
		return None
	return 401 + slot_off, group, ele_index

def parse_add_extra(menu):
	# 1400-1499：血量/蓝量/防御/魔御/魔法躲避/准确/敏捷/幸运/攻击速度/爆率加成
	if menu < 1400 or menu > 1499:
		return None
	body = menu - 1400
	slot_off = body // 10
	kind = body % 10
	if slot_off > 8 or kind > 9:
		return None
	return 401 + slot_off, kind

def parse_remove_stat(menu):
	# 1100-1399：去掉额外属性
	if menu < 1100 or menu > 1399:
		return None
	body = menu - 1100
	slot_off = body // 30
	idx = body % 30
	if slot_off > 8 or idx > 26:
		return None
	return 401 + slot_off, idx

def say_add_slot(Sender, slot_menu):
	slot = ADD_SLOTS[slot_menu]
	eq = Sender.Equipment[int(slot)]
	if not eq:
		return '请先穿戴' + ADD_SLOT_NAME[slot] + '。\n\n[返回:2]\n'
	cleanup_zero_stats(Sender, eq)
	off = slot_menu - 401
	text = (
		'给装备加点\n\n'
		'当前：%s\n'
		'破坏 %d    自然 %d    灵魂 %d\n'
		'血量 %d    蓝量 %d    防御 %d-%d    魔御 %d-%d\n'
		'准确 %d    敏捷 %d    幸运 %d    攻速 %d    魔法躲避 %d    爆率加成 %d%%\n'
		'点一次增加 1 点，不消耗材料。\n\n'
		'[攻击元素:%d] [强元素:%d]\n'
		'\n'
		'[破坏:%d] [全系魔法:%d] [自然:%d] [灵魂:%d]\n'
		'\n'
		'[血量:%d] [蓝量:%d] [防御:%d] [魔御:%d]\n'
		'\n'
		'[准确:%d] [敏捷:%d] [幸运:%d] [攻速:%d]\n'
		'\n'
		'[魔法躲避:%d] [爆率加成:%d]\n'
		'\n'
		'[去掉额外属性:%d]\n'
		'\n'
		'[返回:2]\n'
	) % (
		eq.Info.ItemName,
		stat_total(eq, Stat.MaxDC),
		stat_total(eq, Stat.MaxMC),
		stat_total(eq, Stat.MaxSC),
		stat_total(eq, Stat.Health),
		stat_total(eq, Stat.Mana),
		stat_total(eq, Stat.MinAC),
		stat_total(eq, Stat.MaxAC),
		stat_total(eq, Stat.MinMR),
		stat_total(eq, Stat.MaxMR),
		stat_total(eq, Stat.Accuracy),
		stat_total(eq, Stat.Agility),
		stat_total(eq, Stat.Luck),
		stat_total(eq, Stat.AttackSpeed),
		stat_total(eq, Stat.MagicEvade),
		stat_total(eq, Stat.DropRate),
		510 + off * 10 + 1,
		510 + off * 10 + 2,
		610 + off * 10 + 3,
		610 + off * 10 + 4,
		610 + off * 10 + 5,
		610 + off * 10 + 6,
		1400 + off * 10 + 0,
		1400 + off * 10 + 1,
		1400 + off * 10 + 2,
		1400 + off * 10 + 3,
		1400 + off * 10 + 5,
		1400 + off * 10 + 6,
		1400 + off * 10 + 7,
		1400 + off * 10 + 8,
		1400 + off * 10 + 4,
		1400 + off * 10 + 9,
		510 + off * 10 + 7,
	)
	return text

def say_add_ele(Sender, slot_menu, group):
	slot = ADD_SLOTS[slot_menu]
	eq = Sender.Equipment[int(slot)]
	if not eq:
		return '请先穿戴' + ADD_SLOT_NAME[slot] + '。\n\n[返回:2]\n'
	cleanup_zero_stats(Sender, eq)
	off = slot_menu - 401
	if group == 'atk':
		title = '攻击元素'
		stats = ELE_ATK
		names = ELE_ATK_NAME
		base = 710
	else:
		title = '强元素'
		stats = ELE_RES
		names = ELE_RES_NAME
		base = 810
	currents = []
	links = []
	for i, st in enumerate(stats):
		currents.append('%s %d' % (names[st], stat_total(eq, st)))
		links.append('[%s:%d]' % (names[st], base + off * 10 + i))
	text = (
		'给装备加点\n\n'
		'当前：%s\n'
		'请选择要加的%s，点一次增加 1 点。\n'
		'当前：%s\n\n'
		'%s\n'
		'\n'
		'%s\n'
		'\n'
		'[返回:%d]\n'
	) % (
		eq.Info.ItemName,
		title,
		'、'.join(currents),
		' '.join(links[:4]),
		' '.join(links[4:]),
		slot_menu,
	)
	return text

def say_remove(Sender, slot_menu):
	slot = ADD_SLOTS[slot_menu]
	eq = Sender.Equipment[int(slot)]
	if not eq:
		return '请先穿戴' + ADD_SLOT_NAME[slot] + '。\n\n[返回:2]\n'
	cleanup_zero_stats(Sender, eq)
	off = slot_menu - 401
	lines = []
	links = []
	for idx, stat, label in REMOVE_STATS:
		amt = added_amount(eq, stat)
		if amt > 0:
			lines.append('%s 额外 %d' % (label, amt))
			links.append('[%s:%d]' % (label, 1100 + off * 30 + idx))
	text = (
		'去掉额外属性\n\n'
		'当前：%s\n'
		'只扣额外加成，一次 1 点，不会扣装备原来的属性。\n'
	) % eq.Info.ItemName
	if not links:
		text += '这件装备没有可去掉的额外属性。\n\n[返回:%d]\n' % slot_menu
		return text
	text += '当前额外：' + '、'.join(lines) + '\n\n'
	i = 0
	while i < len(links):
		text += ' '.join(links[i:i + 4]) + '\n\n'
		i += 4
	text += '[返回:%d]\n' % slot_menu
	return text

def do_add_stat(Sender, slot, stat, label):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要加点的' + ADD_SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	Sender.ItemStatsChangeRefresh(slot, stat, 1, StatSource.Added)
	cur = stat_total(eq, stat)
	Sender.Connection.ReceiveChat('加点成功！%s %s +1（当前 %d）' % (eq.Info.ItemName, label, cur), MessageType.System)
	return True

def do_add_magic(Sender, slot):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要加点的' + ADD_SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	Sender.ItemStatsChangeRefresh(slot, Stat.MaxMC, 1, StatSource.Added)
	Sender.ItemStatsChangeRefresh(slot, Stat.MaxSC, 1, StatSource.Added)
	Sender.Connection.ReceiveChat(
		'加点成功！%s 全系魔法 +1（自然 %d，灵魂 %d）' % (
			eq.Info.ItemName, stat_total(eq, Stat.MaxMC), stat_total(eq, Stat.MaxSC)
		),
		MessageType.System
	)
	return True

def do_remove_stat(Sender, slot, stat, label):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要去掉属性的' + ADD_SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	if added_amount(eq, stat) <= 0:
		Sender.Connection.ReceiveChat('%s 没有可去掉的额外%s' % (eq.Info.ItemName, label), MessageType.System)
		return False
	source = None
	for s in eq.AddedStats:
		if s.Stat == stat and int(s.Amount) > 0:
			source = s.StatSource
			break
	if source is None:
		Sender.Connection.ReceiveChat('%s 没有可去掉的额外%s' % (eq.Info.ItemName, label), MessageType.System)
		return False
	Sender.ItemStatsChangeRefresh(slot, stat, -1, source)
	cleanup_zero_stats(Sender, eq)
	left = added_amount(eq, stat)
	Sender.Connection.ReceiveChat('已去掉 %s 额外%s 1 点（剩余 %d）' % (eq.Info.ItemName, label, left), MessageType.System)
	return True

def OnClick(args):
	Self = args[0]
	Sender = args[1]
	Menu = args[2]
	Dict = {}

	if  (Menu == 1):
		say = """我在这寒冷的世界里研究出了一套印记的升级方法。

		[强化破坏印记:31] <font color=0xff00ff00>成功率：60%</font>	
		需要材料：<font color=0xff00ff00>破坏印记（限时）</font> * <font color=0xff00ff00>10个</font>
		需要材料：<font color=0xff00ff00>炼制结晶</font> * <font color=0xff00ff00>50</font>
		需要材料：<font color=0xff00ff00>魔晶石</font> * <font color=0xff00ff00>50</font>
		需要手续费：<font color=0xff00ff00>元宝</font> * <font color=0xff00ff00>100</font>	

		[强化自然印记:32] <font color=0xff00ff00>成功率：60%</font>	
		需要材料：<font color=0xff00ff00>自然印记（限时）</font> * <font color=0xff00ff00>10个</font>
		需要材料：<font color=0xff00ff00>炼制结晶</font> * <font color=0xff00ff00>50</font>
		需要材料：<font color=0xff00ff00>魔晶石</font> * <font color=0xff00ff00>50</font>
		需要手续费：<font color=0xff00ff00>元宝</font> * <font color=0xff00ff00>100</font>	

		[强化灵魂印记:33] <font color=0xff00ff00>成功率：60%</font>	
		需要材料：<font color=0xff00ff00>灵魂印记（限时）</font> * <font color=0xff00ff00>10个</font>
		需要材料：<font color=0xff00ff00>炼制结晶</font> * <font color=0xff00ff00>50</font>
		需要材料：<font color=0xff00ff00>魔晶石</font> * <font color=0xff00ff00>50</font>
		需要手续费：<font color=0xff00ff00>元宝</font> * <font color=0xff00ff00>100</font>	

		[强化神圣印记:34] <font color=0xff00ff00>成功率：50%</font>	
		需要材料：<font color=0xff00ff00>神圣印记（限时）</font> * <font color=0xff00ff00>10个</font>
		需要材料：<font color=0xff00ff00>炼制结晶</font> * <font color=0xff00ff00>50</font>
		需要材料：<font color=0xff00ff00>魔晶石</font> * <font color=0xff00ff00>50</font>
		需要手续费：<font color=0xff00ff00>元宝</font> * <font color=0xff00ff00>200</font>	

		[强化暗黑印记:35] <font color=0xff00ff00>成功率：50%</font>	
		需要材料：<font color=0xff00ff00>暗黑印记（限时）</font> * <font color=0xff00ff00>10个</font>
		需要材料：<font color=0xff00ff00>炼制结晶</font> * <font color=0xff00ff00>50</font>
		需要材料：<font color=0xff00ff00>魔晶石</font> * <font color=0xff00ff00>50</font>
		需要手续费：<font color=0xff00ff00>元宝</font> * <font color=0xff00ff00>200</font>	

		[强化幻影印记:36] <font color=0xff00ff00>成功率：50%</font>	
		需要材料：<font color=0xff00ff00>幻影印记（限时）</font> * <font color=0xff00ff00>10个</font>
		需要材料：<font color=0xff00ff00>炼制结晶</font> * <font color=0xff00ff00>50</font>
		需要材料：<font color=0xff00ff00>魔晶石</font> * <font color=0xff00ff00>50</font>
		需要手续费：<font color=0xff00ff00>元宝</font> * <font color=0xff00ff00>1000</font>	

		[返回:99]
		[离开:0]"""
	
	elif (Menu == 31):
		say = """注意：<font color=0xffFF00FF>失败后材料扣除，原升级材料和元宝不扣</font>
		强化破坏印记：破坏印记（限时）*10；炼制结晶*50；魔晶石*50；元宝100，几率60%！
        
		
		[请帮忙升级:311]
		[返回:99]
		"""
	elif (Menu == 311):
		#判断需要的元宝	
		if (Sender.GameGold < 100):
			say= """世界上的事情没有免费的，升级也是同样的，下次不要忘了带手续费来。
			
			[结束:0]
			"""
		#判断是否有要求的道具
		elif(Sender.GetItemCount("破坏印记（限时）") < 10):
			say ="""抱歉，无法为你升级，请问你带来了指定的升级物品了吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("炼制结晶") < 50):
			say ="""抱歉，无法为你升级，请问你带够了“炼制结晶”吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("魔晶石") < 50):
			say ="""抱歉，无法为你升级，你带够了“魔晶石”吗。
			
			[结束:0]
			"""

		else:
		#上面条件都达成，扣除费用和道具
			Sender.TakeItem("炼制结晶",50)
			Sender.TakeItem("魔晶石",50)
			select = random.randint(0,10)
			#设置获得物品的几率
			if select < 5:
				say ="""哦，非常抱歉！手抖了一下，升级失败，再来一次吧！
				
				[结束:0]
				"""
			else:
				SubGameGold(Sender,100)
				Sender.GiveItem("强化破坏印记",1)
				Sender.TakeItem("破坏印记（限时）",10)
				say = """恭喜你，升级成功。你的能力增强了！
								
				[结束:0]
				"""
	elif (Menu == 32):
		say = """注意：<font color=0xffFF00FF>失败后材料扣除，原升级材料和元宝不扣</font>
		强化自然印记：自然印记（限时）*10；炼制结晶*50；魔晶石*50；元宝100，几率60%！
        
		
		[请帮忙升级:321]
		[结束:0]
		"""
	elif (Menu == 321):
		#判断需要的金币	
		if (Sender.GameGold < 100):
			say= """世界上的事情没有免费的，升级也是同样的，下次不要忘了带手续费来。
			
			[结束:0]
			"""
		#判断是否有要求的道具
		elif(Sender.GetItemCount("自然印记（限时）") < 10):
			say ="""抱歉，无法为你升级，请问你带来了指定的升级物品了吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("炼制结晶") < 50):
			say ="""抱歉，无法为你升级，请问你带够了“炼制结晶”吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("魔晶石") < 50):
			say ="""抱歉，无法为你升级，你带够了“魔晶石”吗。
			
			[结束:0]
			"""

		else:
		#上面条件都达成，扣除费用和道具
			Sender.TakeItem("炼制结晶",50)
			Sender.TakeItem("魔晶石",50)
			select = random.randint(0,10)
			#设置获得物品的几率
			if select < 5:
				say ="""哦，非常抱歉！手抖了一下，升级失败，再来一次吧！
				
				[结束:0]
				"""
			else:
				SubGameGold(Sender,100)
				Sender.GiveItem("强化自然印记",1)
				Sender.TakeItem("自然印记（限时）",10)
				say = """恭喜你，升级成功。你的能力增强了！
								
				[结束:0]
				"""
	elif (Menu == 33):
		say = """注意：<font color=0xffFF00FF>失败后材料扣除，原升级材料和元宝不扣</font>
		强化灵魂印记：灵魂印记（限时）*10；炼制结晶*50；魔晶石*50；元宝100，几率60%！
        
		
		[请帮忙升级:331]
		[结束:0]
		"""
	elif (Menu == 331):
		if (Sender.GameGold < 100):
			say= """世界上的事情没有免费的，升级也是同样的，下次不要忘了带手续费来。
			
			[结束:0]
			"""
		#判断是否有要求的道具
		elif(Sender.GetItemCount("灵魂印记（限时）") < 10):
			say ="""抱歉，无法为你升级，请问你带来了指定的升级物品了吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("炼制结晶") < 50):
			say ="""抱歉，无法为你升级，请问你带够了“炼制结晶”吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("魔晶石") < 50):
			say ="""抱歉，无法为你升级，你带够了“魔晶石”吗。
			
			[结束:0]
			"""

		else:
		#上面条件都达成，扣除费用和道具
			Sender.TakeItem("炼制结晶",50)
			Sender.TakeItem("魔晶石",50)
			select = random.randint(0,10)
			#设置获得物品的几率
			if select < 5:
				say ="""哦，非常抱歉！手抖了一下，升级失败，再来一次吧！
				
				[结束:0]
				"""
			else:
				SubGameGold(Sender,100)
				Sender.GiveItem("强化灵魂印记",1)
				Sender.TakeItem("灵魂印记（限时）",10)
				say = """恭喜你，升级成功。你的能力增强了！
								
				[结束:0]
				"""
	elif (Menu == 34):
		say = """注意：<font color=0xffFF00FF>失败后材料扣除，原升级材料和元宝不扣</font>
		强化神圣印记：神圣印记（限时）*10；炼制结晶*50；魔晶石*50；元宝200，几率50%！
        
		
		[请帮忙升级:341]
		[结束:0]
		"""
	elif (Menu == 341):
		#判断需要的金币	
		if (Sender.GameGold < 200):
			say= """世界上的事情没有免费的，升级也是同样的，下次不要忘了带手续费来。
			
			[结束:0]
			"""
		#判断是否有要求的道具
		elif(Sender.GetItemCount("神圣印记（限时）") < 10):
			say ="""抱歉，无法为你升级，请问你带来了指定的升级物品了吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("炼制结晶") < 50):
			say ="""抱歉，无法为你升级，请问你带够了“炼制结晶”吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("魔晶石") < 50):
			say ="""抱歉，无法为你升级，你带够了“魔晶石”吗。
			
			[结束:0]
			"""

		else:
		#上面条件都达成，扣除费用和道具
			Sender.TakeItem("炼制结晶",50)
			Sender.TakeItem("魔晶石",50)
			select = random.randint(0,10)
			#设置获得物品的几率
			if select < 6:
				say ="""哦，非常抱歉！手抖了一下，升级失败，再来一次吧！
				
				[结束:0]
				"""
			else:
				SubGameGold(Sender,200)
				Sender.GiveItem("强化神圣印记",1)
				Sender.TakeItem("神圣印记（限时）",10)
				say = """恭喜你，升级成功。你的能力增强了！
								
				[结束:0]
				"""
	elif (Menu == 35):
		say = """注意：<font color=0xffFF00FF>失败后材料扣除，原升级材料和元宝不扣</font>
		强化暗黑印记：暗黑印记（限时）*10；炼制结晶*50；魔晶石*50；元宝200，几率50%！
        
		
		[请帮忙升级:351]
		[结束:0]
		"""
	elif (Menu == 351):
		#判断需要的金币	
		if (Sender.GameGold < 200):
			say= """世界上的事情没有免费的，升级也是同样的，下次不要忘了带手续费来。
			
			[结束:0]
			"""
		#判断是否有要求的道具
		elif(Sender.GetItemCount("暗黑印记（限时）") < 10):
			say ="""抱歉，无法为你升级，请问你带来了指定的升级物品了吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("炼制结晶") < 50):
			say ="""抱歉，无法为你升级，请问你带够了“炼制结晶”吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("魔晶石") < 50):
			say ="""抱歉，无法为你升级，你带够了“魔晶石”吗。
			
			[结束:0]
			"""

		else:
		#上面条件都达成，扣除费用和道具
			Sender.TakeItem("炼制结晶",50)
			Sender.TakeItem("魔晶石",50)
			select = random.randint(0,10)
			#设置获得物品的几率
			if select < 6:
				say ="""哦，非常抱歉！手抖了一下，升级失败，再来一次吧！
				
				[结束:0]
				"""
			else:
				SubGameGold(Sender,100)
				Sender.GiveItem("强化暗黑印记",1)
				Sender.TakeItem("暗黑印记（限时）",10)
				say = """恭喜你，升级成功。你的能力增强了！
								
				[结束:0]
				"""
	elif (Menu == 36):
		say = """注意：<font color=0xffFF00FF>失败后材料扣除，原升级材料和元宝不扣</font>
		强化幻影印记：幻影印记（限时）*10；炼制结晶*50；魔晶石*50；元宝500，几率50%！
        
		
		[请帮忙升级:361]
		[结束:0]
		"""
	elif (Menu == 361):
		#判断需要的金币	
		if (Sender.GameGold < 500):
			say= """世界上的事情没有免费的，升级也是同样的，下次不要忘了带手续费来。
			
			[结束:0]
			"""
		#判断是否有要求的道具
		elif(Sender.GetItemCount("幻影印记（限时）") < 10):
			say ="""抱歉，无法为你升级，请问你带来了指定的升级物品了吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("炼制结晶") < 50):
			say ="""抱歉，无法为你升级，请问你带够了“炼制结晶”吗。
			
			[结束:0]
			"""
		elif(Sender.GetItemCount("魔晶石") < 50):
			say ="""抱歉，无法为你升级，你带够了“魔晶石”吗。
			
			[结束:0]
			"""

		else:
		#上面条件都达成，扣除费用和道具
			Sender.TakeItem("炼制结晶",50)
			Sender.TakeItem("魔晶石",50)
			select = random.randint(0,10)
			#设置获得物品的几率
			if select < 6:
				say ="""哦，非常抱歉！手抖了一下，升级失败，再来一次吧！
				
				[结束:0]
				"""
			else:
				SubGameGold(Sender,500)
				Sender.GiveItem("强化幻影印记",1)
				Sender.TakeItem("幻影印记（限时）",10)
				say = """恭喜你，升级成功。你的能力增强了！
								
				[结束:0]
				"""

	elif (Menu == 2):
		say = SAY_ADD_MAIN
	elif (Menu in ADD_SLOTS):
		say = say_add_slot(Sender, Menu)
	else:
		parsed_kind = parse_add_kind(Menu)
		parsed_stat = parse_add_stat(Menu)
		parsed_ele = parse_add_ele(Menu)
		parsed_extra = parse_add_extra(Menu)
		parsed_remove = parse_remove_stat(Menu)
		if parsed_kind:
			slot_menu, kind = parsed_kind
			if kind == 1:
				say = say_add_ele(Sender, slot_menu, 'atk')
			elif kind == 2:
				say = say_add_ele(Sender, slot_menu, 'res')
			else:
				say = say_remove(Sender, slot_menu)
		elif parsed_stat:
			slot_menu, kind = parsed_stat
			slot = ADD_SLOTS[slot_menu]
			if kind == 3:
				do_add_stat(Sender, slot, Stat.MaxDC, '破坏')
			elif kind == 4:
				do_add_magic(Sender, slot)
			elif kind == 5:
				do_add_stat(Sender, slot, Stat.MaxMC, '自然')
			elif kind == 6:
				do_add_stat(Sender, slot, Stat.MaxSC, '灵魂')
			say = say_add_slot(Sender, slot_menu)
		elif parsed_ele:
			slot_menu, group, ele_index = parsed_ele
			slot = ADD_SLOTS[slot_menu]
			if group == 'atk':
				st = ELE_ATK[ele_index]
				do_add_stat(Sender, slot, st, '攻击元素' + ELE_ATK_NAME[st])
			else:
				st = ELE_RES[ele_index]
				do_add_stat(Sender, slot, st, '强元素' + ELE_RES_NAME[st])
			say = say_add_ele(Sender, slot_menu, group)
		elif parsed_extra:
			slot_menu, kind = parsed_extra
			slot = ADD_SLOTS[slot_menu]
			_i, stat, label = EXTRA_ADD_STATS[kind]
			do_add_stat(Sender, slot, stat, label)
			say = say_add_slot(Sender, slot_menu)
		elif parsed_remove:
			slot_menu, idx = parsed_remove
			slot = ADD_SLOTS[slot_menu]
			_i, stat, label = REMOVE_STATS[idx]
			do_remove_stat(Sender, slot, stat, label)
			say = say_remove(Sender, slot_menu)
		else:
			#主菜单
			say = """印记是特殊能力的证明。我有提升它的方法。
		当然我的技术不是很成熟，有很大几率会失败。
		
		[打探各类印记增强的方法:1]
		
		[给装备加点:2]
		
		[关闭:0]"""

	Dict['Say'] = say  # 定义聊天框对话内容
	return Dict

NpcEvent.add_listener(322, "OnClick", OnClick)
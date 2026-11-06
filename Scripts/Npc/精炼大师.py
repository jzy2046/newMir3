# -*- coding: utf-8 -*-
# 精炼大师：穿戴装备 + 背包地煞石/天罡石（消耗按冲刺等级）
from Globals import *
import clr, random
clr.AddReference('Library')
clr.AddReference('System')
from Library import *
import NpcEvent

STONE_DS = '地煞石'
STONE_TG = '天罡石'
MAX_LV = 6
SUCCESS = 1

JOBS = {
	1: (EquipmentSlot.Weapon, Stat.CriticalDamage, 5),
	2: (EquipmentSlot.Necklace, Stat.CriticalChance, 1),
	3: (EquipmentSlot.BraceletL, Stat.CriticalChance, 1),
	4: (EquipmentSlot.BraceletR, Stat.CriticalChance, 1),
	5: (EquipmentSlot.RingL, Stat.CriticalChance, 1),
	6: (EquipmentSlot.RingR, Stat.CriticalChance, 1),
	7: (EquipmentSlot.Armour, Stat.Health, 10),
	8: (EquipmentSlot.Helmet, Stat.Health, 10),
	9: (EquipmentSlot.Shoes, Stat.Health, 10),
}

SLOT_NAME = {
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

def enhance_amount(item, stat):
	total = 0
	for s in item.AddedStats:
		if s.Stat == stat and s.StatSource == StatSource.Enhancement:
			total += int(s.Amount)
	return total

def refine_level(item, stat, per):
	v = enhance_amount(item, stat)
	if stat == Stat.CriticalChance:
		thresholds = [1, 2, 3, 5, 7, 10]
		lv = 0
		for t in thresholds:
			if v >= t:
				lv += 1
		return lv
	return max(0, min(MAX_LV, v // per))

def stone_cost(next_try):
	ds = next_try
	tg = (next_try - 3) if next_try >= 4 else 0
	return ds, tg

def do_refine(Sender, slot, stat, per):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要精炼的' + SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	lv = refine_level(eq, stat, per)
	if lv >= MAX_LV:
		Sender.Connection.ReceiveChat('该装备精炼已满 (6/6)', MessageType.System)
		return False
	next_try = lv + 1
	ds_need, tg_need = stone_cost(next_try)
	if Sender.GetItemCount(STONE_DS) < ds_need:
		Sender.Connection.ReceiveChat('需要地煞石 x%d（冲+%d）' % (ds_need, next_try), MessageType.System)
		return False
	if tg_need > 0 and Sender.GetItemCount(STONE_TG) < tg_need:
		Sender.Connection.ReceiveChat('需要天罡石 x%d（冲+%d，必扣保级）' % (tg_need, next_try), MessageType.System)
		return False
	Sender.TakeItem(STONE_DS, ds_need)
	if tg_need > 0:
		Sender.TakeItem(STONE_TG, tg_need)
	roll = random.randint(1, 100)
	name = eq.Info.ItemName
	if roll <= SUCCESS:
		amount = per
		if stat == Stat.CriticalChance:
			amount = [1, 1, 1, 2, 2, 3][next_try - 1]
		Sender.ItemStatsChangeRefresh(slot, stat, amount, StatSource.Enhancement)
		nlv = lv + 1
		Sender.Connection.ReceiveChat('精炼成功！%s 精炼等级 (%d/%d)' % (name, nlv, MAX_LV), MessageType.System)
		return True
	if next_try >= 4:
		Sender.Connection.ReceiveChat('精炼失败（天罡石护持，等级不变）%s (%d/%d)' % (name, lv, MAX_LV), MessageType.Hint)
	else:
		Sender.Connection.ReceiveChat('精炼失败（前三阶不掉级）%s (%d/%d)' % (name, lv, MAX_LV), MessageType.Hint)
	return False

def do_reset(Sender, slot):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要重置的' + SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	removed = 0
	for i in range(eq.AddedStats.Count - 1, -1, -1):
		s = eq.AddedStats[i]
		if s.StatSource == StatSource.Enhancement:
			s.Delete()
			removed += 1
	eq.Level = 1
	eq.Experience = 0
	eq.StatsChanged()
	Sender.ItemCompleteRefresh(eq.Index)
	Sender.Connection.ReceiveChat('已重置精炼：%s（清除 %d 条，等级归0，不返材料）' % (eq.Info.ItemName, removed), MessageType.System)
	return True

def OnClick(args):
	Self = args[0]
	Sender = args[1]
	Menu = args[2]
	Dict = {}
	if Menu in JOBS:
		slot, stat, per = JOBS[Menu]
		do_refine(Sender, slot, stat, per)
	elif Menu >= 101 and Menu <= 109:
		slot, stat, per = JOBS[Menu - 100]
		do_reset(Sender, slot)
	say = (
		'精炼大师\n\n'
		'穿戴装备，背包放材料。最高6级。\n'
		'消耗按「冲刺等级」强制扣除：\n'
		'冲+1：地煞1\n'
		'冲+2：地煞2\n'
		'冲+3：地煞3\n'
		'冲+4：地煞4 + 天罡1（失败保级）\n'
		'冲+5：地煞5 + 天罡2（失败保级）\n'
		'冲+6：地煞6 + 天罡3（失败保级）\n'
		'前三阶失败不掉级；后三阶已扣天罡，失败同样保级。\n\n'
		'武器：每级+5%暴击伤害\n'
		'首饰暴击率：1级+1 2级+1 3级+1 4级+2 5级+2 6级+3（满级共+10%）\n'
		'衣/盔/鞋：每级+10生命\n'
		'重置=清空该部位精炼加成与等级，不返还材料。\n\n'
		'[精炼武器:1]   [精炼头盔:8]   [精炼鞋子:9]   [精炼衣服:7]  [精炼项链:2]\n'
		'\n'
		'[精炼左手镯:3] [精炼右手镯:4] [精炼左戒指:5] [精炼右戒指:6]\n'
		'\n'
		'\n'
		'[重置项链:102]  \n'
		'\n'
		'[重置左手镯:103] [重置右手镯:104] [重置左戒指:105] [重置右戒指:106]\n'
		'\n'
		'\n'
		'[离开:0]\n'
	)
	Dict['Say'] = say
	return Dict

NpcEvent.add_listener(5656, 'OnClick', OnClick)
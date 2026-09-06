# -*- coding: utf-8 -*-
# 精炼大师：穿戴装备 + 背包地煞石/天罡石
from Globals import *
import clr, random
clr.AddReference('Library')
clr.AddReference('System')
from Library import *
import NpcEvent

STONE_DS = '地煞石'
STONE_TG = '天罡石'
MAX_LV = 6
SUCCESS = 10

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
	return max(0, min(MAX_LV, v // per))

def do_refine(Sender, slot, stat, per):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要精炼的' + SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	lv = refine_level(eq, stat, per)
	if lv >= MAX_LV:
		Sender.Connection.ReceiveChat('该装备精炼已满 (6/6)', MessageType.System)
		return False
	if Sender.GetItemCount(STONE_DS) < 1:
		Sender.Connection.ReceiveChat('需要地煞石 x1', MessageType.System)
		return False
	# 前三阶(当前0/1/2，冲1/2/3)只扣地煞；后三阶才可选扣天罡保级
	next_try = lv + 1
	use_tg = (next_try > 3) and (Sender.GetItemCount(STONE_TG) >= 1)
	Sender.TakeItem(STONE_DS, 1)
	if use_tg:
		Sender.TakeItem(STONE_TG, 1)
	roll = random.randint(1, 100)
	name = eq.Info.ItemName
	if roll <= SUCCESS:
		Sender.ItemStatsChangeRefresh(slot, stat, per, StatSource.Enhancement)
		nlv = lv + 1
		Sender.Connection.ReceiveChat('精炼成功！%s 精炼等级 (%d/%d)' % (name, nlv, MAX_LV), MessageType.System)
		return True
	if use_tg:
		Sender.Connection.ReceiveChat('精炼失败（天罡石护持，等级不变）%s (%d/%d)' % (name, lv, MAX_LV), MessageType.Hint)
		return False
	if next_try <= 3:
		Sender.Connection.ReceiveChat('精炼失败（前三阶不掉级）%s (%d/%d)' % (name, lv, MAX_LV), MessageType.Hint)
		return False
	if lv > 0:
		Sender.ItemStatsChangeRefresh(slot, stat, -(lv * per), StatSource.Enhancement)
	Sender.Connection.ReceiveChat('精炼失败！%s 精炼等级已清零 (0/%d)' % (name, MAX_LV), MessageType.System)
	return False

def OnClick(args):
	Self = args[0]
	Sender = args[1]
	Menu = args[2]
	Dict = {}
	if Menu in JOBS:
		slot, stat, per = JOBS[Menu]
		do_refine(Sender, slot, stat, per)
		return
	say = (
		'精炼大师\n\n'
		'穿戴装备，背包放【地煞石】。成功率10%。最高6级。\n'
		'前三阶只扣地煞石；后三阶可放【天罡石】保级（失败不掉级）。\n\n'
		'武器：每级+5%暴击伤害\n'
		'首饰：每级+1%暴击几率\n'
		'衣/盔/鞋：每级+10生命\n\n'
		'失败：前三阶不掉级；后三阶仅地煞失败清零；带天罡失败不掉级。\n\n'
		'[精炼武器:1]\n'
		'[精炼项链:2]  [精炼左手镯:3]  [精炼右手镯:4]\n'
		'[精炼左戒指:5]  [精炼右戒指:6]\n'
		'[精炼衣服:7]  [精炼头盔:8]  [精炼鞋子:9]\n'
		'[离开:0]\n'
	)
	Dict['Say'] = say
	return Dict

NpcEvent.add_listener(5656, 'OnClick', OnClick)

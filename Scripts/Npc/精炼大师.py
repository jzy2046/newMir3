# -*- coding: utf-8 -*-
# 精炼大师：穿戴装备 + 背包地煞石/天罡石（消耗按冲刺等级）
# 衣服/头盔/鞋子：随机强元素（含原生最多3种）
# 强元素消耗：背包同名装 2/3/5 + 钢玉石100 + 魔晶石100
# 重置只清脚本精炼，不动银杏累计 / 武器熟练度 / 强元素
# 稀世武器等级满级后再升：破坏/全系魔法/元素三选一，同名武器x1，含已有升级最高+25
# 武器一键满级：等级拉满，破坏/全系魔法/元素三选一随机+10~17，钢玉石10+魔晶石10
# 更换项链/手镯/戒指/头盔攻击元素：只改 *Attack，不换装备，生锈材料各1共9个
# 装备兑换高级碎片 / 高级碎片兑换装备：菜单 1500-2015，不占用精炼/强元素/再升/换元素编号
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
MAX_ELE = 3
ELE_COST = (2, 3, 5)  # 第1/2/3个强元素：背包同名装
MAT_CORUNDUM = '钢玉石'
MAT_MAGIC = '魔晶石'
COST_CORUNDUM = 100
COST_MAGIC = 100
COST_MAX_CORUNDUM = 10
COST_MAX_MAGIC = 10
MAX_FURTHER = 25
INSTANT_MIN = 10
INSTANT_MAX = 17
PAGE_MAIN = 400
PAGE_REFINE = 401
PAGE_ELEMENT = 402
PAGE_FURTHER = 403
PAGE_INSTANT = 404
PAGE_CHANGE = 405
FURTHER_MENUS = {
	301: 'dc',
	302: 'magic',
	303: 'ele',
}
INSTANT_MENUS = {
	311: 'dc',
	312: 'magic',
	313: 'ele',
}
TRACK_NAME = {
	'dc': '破坏',
	'magic': '全系魔法',
	'ele': '元素',
}
SPECIAL_WEAPON_MAX = 13
SPECIAL_WEAPON_INDEXES = (80360, 80361, 80362)
COST_RUST = [
	'生锈定心项链',
	'生锈破荒项链',
	'生锈魔云项链',
	'生锈世尊手镯',
	'生锈思过手镯',
	'生锈金棱手镯',
	'生锈青云戒指',
	'生锈龙马戒指',
	'生锈师承戒指',
]
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
ELE_SLOTS = {
	201: EquipmentSlot.Armour,
	208: EquipmentSlot.Helmet,
	209: EquipmentSlot.Shoes,
}
CHANGE_SLOTS = {
	501: EquipmentSlot.Necklace,
	502: EquipmentSlot.BraceletL,
	503: EquipmentSlot.BraceletR,
	504: EquipmentSlot.RingL,
	505: EquipmentSlot.RingR,
	506: EquipmentSlot.Helmet,
}
ELE_STATS = [
	Stat.FireResistance,
	Stat.IceResistance,
	Stat.LightningResistance,
	Stat.WindResistance,
	Stat.HolyResistance,
	Stat.DarkResistance,
	Stat.PhantomResistance,
]
ELE_NAME = {
	Stat.FireResistance: '火',
	Stat.IceResistance: '冰',
	Stat.LightningResistance: '雷',
	Stat.WindResistance: '风',
	Stat.HolyResistance: '神圣',
	Stat.DarkResistance: '暗黑',
	Stat.PhantomResistance: '幻影',
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
ELE_ATK_NAME = {
	Stat.FireAttack: '火',
	Stat.IceAttack: '冰',
	Stat.LightningAttack: '雷',
	Stat.WindAttack: '风',
	Stat.HolyAttack: '神圣',
	Stat.DarkAttack: '暗黑',
	Stat.PhantomAttack: '幻影',
}
SKIP_ELE_SOURCES = (
	StatSource.Gem1,
	StatSource.Gem2,
	StatSource.Gem3,
	StatSource.Rune,
	StatSource.Enhancement,
	StatSource.Other,
)
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

FRAG = '高级碎片'
PAGE_EQ2FRAG = 1500
PAGE_FRAG2EQ = 1800
EQ2FRAG_CONFIRM = 1600
EQ2FRAG_EXEC = 1700
FRAG2EQ_TIER10 = 1801
FRAG2EQ_TIER50 = 1803
FRAG2EQ_CONFIRM = 1900
FRAG2EQ_EXEC = 2000

# (名称, 兑换得到的碎片数)
# 只收准确无前后缀的名字，变体（墨龙、诺玛之、元素后缀等）不会被扣除
EQ2FRAG_ITEMS = (
	('霹雷', 15),
	('龙纹剑', 15),
	('嗜魂法杖', 15),
	('屠龙', 25),
	('铁轮', 25),
	('逍遥扇', 25),
	('诺玛霹雷', 20),
	('诺玛铁轮', 20),
	('诺玛逍遥扇', 20),
	('天神法杖', 40),
	('破山剑', 40),
	('泰轮拂尘', 40),
	('流星项链', 10),
	('怨恨项链', 10),
	('气血项链', 10),
	('五行神镜', 10),
	('昆仑项链', 10),
	('霸王项链', 10),
	('真善项链', 10),
	('至善手镯', 10),
	('云龙手镯', 10),
	('登天手镯', 10),
	('旭日戒指', 10),
	('继承戒指', 10),
	('三桓戒指', 10),
)

# 分组菜单：菜单号, 数量, 标题, EQ2FRAG_ITEMS 下标范围
EQ2FRAG_GROUPS = (
	(1501, 15, '15个高级碎片', (0, 3)),
	(1502, 25, '25个高级碎片', (3, 6)),
	(1503, 20, '20个高级碎片', (6, 9)),
	(1504, 40, '40个高级碎片', (9, 12)),
	(1505, 10, '10个高级碎片', (12, 25)),
)

# (名称, 消耗碎片数, 分组说明)
# 虹魔套、魔血套按件列出，由玩家自选一件，不会随机给整套
FRAG2EQ_REWARDS = (
	('全能指环', 10, '单件'),
	('龙之手镯', 10, '单件'),
	('骑士手镯', 10, '单件'),
	('心灵手镯', 10, '单件'),
	('魔灵戒指', 10, '单件'),
	('魔令项链', 10, '单件'),
	('虹魔项链', 10, '虹魔套'),
	('虹魔手镯', 10, '虹魔套'),
	('虹魔戒指', 10, '虹魔套'),
	('魔血项链', 10, '魔血套'),
	('魔血手镯', 10, '魔血套'),
	('魔血戒指', 10, '魔血套'),
	('英雄手套', 50, '50个'),
	('心念手镯', 50, '50个'),
	('魔令手镯', 50, '50个'),
)

SAY_MAIN = (
	'精炼大师\n\n'
	'请选择要查看的功能。\n\n'
	'[装备精炼:401] [加强元素:402] [更换攻击元素:405] [武器满级再升:403]\n'
	'\n'
	'[装备兑换高级碎片:1500]   [高级碎片兑换装备:1800]\n'
	'\n'
	'\n'
	'[离开:0]\n'
)
SAY_REFINE = (
	'精炼\n\n'
	'穿戴装备，背包放材料。最高6级。\n'
	'消耗按「冲刺等级」强制扣除：\n'
	'精炼1级：地煞1-精炼2级：地煞2-精炼3级：地煞3\n'
	'精炼4级：地煞4 + 天罡1（失败保级）\n'
	'精炼5级：地煞5 + 天罡2（失败保级）\n'
	'精炼6级：地煞6 + 天罡3（失败保级）\n'
	'前三阶失败不掉级；后三阶已扣天罡，失败同样保级。\n\n'
	'武器：每级+5%暴击伤害\n'
	'首饰暴击率：1级+1 2级+1 3级+1 4级+2 5级+2 6级+3（满级共+10%）\n'
	'衣/盔/鞋：每级+10生命\n'
	'重置=只清该部位脚本精炼，不返材料。\n\n'
	'[精炼武器:1] [精炼头盔:8] [精炼鞋子:9] [精炼衣服:7] [精炼项链:2]\n'
	'\n'
	'[精炼左手镯:3] [精炼右手镯:4] [精炼左戒指:5] [精炼右戒指:6]\n'
	'\n'
	'[重置项链:102]\n'
	'\n'
	'[重置左手镯:103] [重置右手镯:104] [重置左戒指:105] [重置右戒指:106]\n'
	'\n'
	'[返回:400]\n'
)
SAY_ELEMENT = (
	'强元素\n\n'
	'强元素（仅衣/盔/鞋）：随机一种未有元素 +1衣服+2，含原生最多3种。\n'
	'第1个：同名装备2件 + 钢玉石100 + 魔晶石100\n'
	'第2个：同名装备3件 + 钢玉石100 + 魔晶石100\n'
	'第3个：同名装备5件 + 钢玉石100 + 魔晶石100\n'
	'材料只扣背包，不扣身上穿的。\n\n'
	'[强元素衣服:201] [强元素头盔:208] [强元素鞋子:209]\n'
	'\n'
	'[返回:400]\n'
)
SAY_CHANGE = (
	'更换攻击元素\n\n'
	'请先穿戴要更换的项链、手镯、戒指或头盔。\n'
	'只改装备上的攻击元素，不更换装备，数值不变。\n'
	'装备名称上的（火）等后缀不会改变，请看属性里的攻击元素。\n'
	'每次更换消耗以下材料各 1 个（共 9 个）：\n'
	'生锈定心项链、生锈破荒项链、生锈魔云项链、\n'
	'生锈世尊手镯、生锈思过手镯、生锈金棱手镯、\n'
	'生锈青云戒指、生锈龙马戒指、生锈师承戒指。\n\n'
	'[更换项链:501]\n'
	'\n'
	'[更换左手镯:502] [更换右手镯:503]\n'
	'\n'
	'[更换左戒指:504] [更换右戒指:505]\n'
	'\n'
	'[更换头盔:506]\n'
	'\n'
	'[返回:400]\n'
)
SAY_FURTHER = (
	'武器满级再升\n\n'
	'稀世武器等级满级后可再升：破坏、全系魔法、元素三选一，每次+1。\n'
	'每把武器只能选其中一项。每次消耗背包同名武器 1 把（可用已升级的）。\n'
	'含以前升级过的数值，该项最高 +25。\n\n'
	'[再升破坏:301] [再升全系魔法:302] [再升元素:303]\n'
	'\n'
	'[返回:400]\n'
)
SAY_INSTANT = (
	'武器一键满级\n\n'
	'将穿戴的稀世武器等级一键拉满，并在破坏、全系魔法、元素中选一项，随机 +10 到 +17。\n'
	'每把武器只能选一项，且只能使用一次。消耗：钢玉石 10 + 魔晶石 10。\n\n'
	'[一键满级破坏:311] [一键满级全系魔法:312] [一键满级元素:313]\n'
	'\n'
	'[返回:400]\n'
)

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

def ele_total(eq, stat):
	return int(eq.Info.Stats[stat]) + int(eq.Stats[stat])

def strong_ele_kinds(eq):
	n = 0
	for s in ELE_STATS:
		if ele_total(eq, s) > 0:
			n += 1
	return n

def added_stat(item, stat):
	total = 0
	for s in item.AddedStats:
		if s.Stat == stat:
			total += int(s.Amount)
	return total

def added_stat_src(item, stat, source):
	total = 0
	for s in item.AddedStats:
		if s.Stat == stat and s.StatSource == source:
			total += int(s.Amount)
	return total

def added_ele(item):
	total = 0
	for st in ELE_ATK:
		total += added_stat(item, st)
	return total

def added_ele_src(item, source):
	total = 0
	for st in ELE_ATK:
		total += added_stat_src(item, st, source)
	return total

def further_amount(eq, track):
	if track == 'dc':
		return added_stat(eq, Stat.MaxDC)
	if track == 'magic':
		return max(added_stat(eq, Stat.MaxMC), added_stat(eq, Stat.MaxSC))
	return added_ele(eq)

def further_track(eq):
	# 只按本脚本写入的 Combine 锁定选项，官方升级不锁线，但计入 +25 上限
	if added_stat_src(eq, Stat.MaxDC, StatSource.Combine) > 0:
		return 'dc'
	if added_stat_src(eq, Stat.MaxMC, StatSource.Combine) > 0 or added_stat_src(eq, Stat.MaxSC, StatSource.Combine) > 0:
		return 'magic'
	if added_ele_src(eq, StatSource.Combine) > 0:
		return 'ele'
	return None

def weapon_ele_stat(eq):
	st = eq.Stats.GetWeaponElement()
	if st != Stat.None:
		return st
	st = eq.Info.Stats.GetWeaponElement()
	if st != Stat.None:
		return st
	return None

def weapon_level_cap(eq):
	if int(eq.Info.Index) in SPECIAL_WEAPON_INDEXES:
		return SPECIAL_WEAPON_MAX
	return int(Globals.GameWeaponEXPInfoList.Count)

def is_weapon_level_max(eq):
	return int(eq.Level) >= weapon_level_cap(eq)

def change_ele_menu(slot_menu, ele_index):
	return 600 + (slot_menu - 501) * 10 + ele_index

def parse_change_ele_menu(menu):
	if menu < 600 or menu > 656:
		return None
	body = menu - 600
	slot_off = body // 10
	ele_index = body % 10
	if ele_index > 6 or slot_off > 5:
		return None
	return 501 + slot_off, ELE_ATK[ele_index]

def net_attack(eq, stat):
	# 只搬 Info + 可移动 AddedStats；宝石/符文/淬炼/临时加成不搬
	n = 0
	if eq.Info is not None:
		n += int(eq.Info.Stats[stat])
	for s in eq.AddedStats:
		if s.Stat == stat and s.StatSource not in SKIP_ELE_SOURCES:
			n += int(s.Amount)
	return n

def change_ele_state(eq):
	primary = None
	total = 0
	best = 0
	for st in ELE_ATK:
		amt = net_attack(eq, st)
		if amt > 0:
			total += amt
			if amt > best:
				best = amt
				primary = st
	return primary, total

def check_rust_cost(Sender):
	missing = []
	for name in COST_RUST:
		if Sender.GetItemCount(name) < 1:
			missing.append(name)
	if missing:
		Sender.Connection.ReceiveChat('材料不足，还需要：' + '、'.join(missing), MessageType.System)
		return False
	return True

def take_rust_cost(Sender):
	for name in COST_RUST:
		Sender.TakeItem(name, 1)

def do_change_element(Sender, slot, new_stat):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要更换的' + SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	cur, amount = change_ele_state(eq)
	if not cur or amount <= 0:
		Sender.Connection.ReceiveChat('%s 没有攻击元素，无法更换' % eq.Info.ItemName, MessageType.System)
		return False
	if new_stat == cur and net_attack(eq, new_stat) == amount:
		Sender.Connection.ReceiveChat('已经是%s元素，不用更换' % ELE_ATK_NAME[cur], MessageType.System)
		return False
	if not check_rust_cost(Sender):
		return False
	take_rust_cost(Sender)
	# 非武器的攻击元素来自 *Attack，按净值把旧元素抵成 0、加到新元素上，不改 Info、不写 WeaponElement
	for st in ELE_ATK:
		now = net_attack(eq, st)
		target = amount if st == new_stat else 0
		delta = target - now
		if delta != 0:
			eq.AddStat(st, delta, StatSource.Refine)
	for i in range(eq.AddedStats.Count - 1, -1, -1):
		s = eq.AddedStats[i]
		if s.StatSource == StatSource.Refine and s.Stat in ELE_ATK and int(s.Amount) == 0:
			s.Delete()
	Sender.ItemCompleteRefresh(eq.Index)
	Sender.Connection.ReceiveChat(
		'更换成功！%s 的攻击元素由%s换成%s（+%d）。名称后缀不会改，请看属性栏。' % (
			eq.Info.ItemName, ELE_ATK_NAME[cur], ELE_ATK_NAME[new_stat], amount
		),
		MessageType.System
	)
	return True

def say_change_slot(Sender, slot_menu):
	slot = CHANGE_SLOTS[slot_menu]
	eq = Sender.Equipment[int(slot)]
	if not eq:
		return '请先穿戴' + SLOT_NAME[slot] + '。\n\n[返回:405]\n'
	cur, amount = change_ele_state(eq)
	if not cur or amount <= 0:
		return '%s 没有攻击元素，无法更换。\n\n[返回:405]\n' % eq.Info.ItemName
	text = (
		'更换攻击元素\n\n'
		'当前：%s，%s +%d\n'
		'只改攻击元素，不更换装备。名称后缀不会改。\n'
		'请选择要换成的元素：\n\n'
	) % (eq.Info.ItemName, ELE_ATK_NAME[cur], amount)
	links = []
	for i, st in enumerate(ELE_ATK):
		if st == cur and net_attack(eq, st) == amount:
			continue
		links.append('[换成%s:%d]' % (ELE_ATK_NAME[st], change_ele_menu(slot_menu, i)))
	text += ' '.join(links[:4]) + '\n'
	if len(links) > 4:
		text += '\n' + ' '.join(links[4:]) + '\n'
	text += '\n[返回:405]\n'
	return text

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

def do_reset(Sender, slot, stat):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要重置的' + SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	removed = 0
	for i in range(eq.AddedStats.Count - 1, -1, -1):
		s = eq.AddedStats[i]
		if s.StatSource == StatSource.Enhancement and s.Stat == stat:
			s.Delete()
			removed += 1
	# 不动 eq.Level / eq.Experience（银杏累计、武器熟练度）
	# 不动强元素（StatSource.Added 的 *Resistance）
	eq.StatsChanged()
	Sender.ItemCompleteRefresh(eq.Index)
	Sender.Connection.ReceiveChat('已重置精炼：%s（清除 %d 条，不返材料；）' % (eq.Info.ItemName, removed), MessageType.System)
	return True

def do_add_element(Sender, slot):
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要附加强元素的' + SLOT_NAME.get(slot, '装备'), MessageType.System)
		return False
	kinds = strong_ele_kinds(eq)
	if kinds >= MAX_ELE:
		Sender.Connection.ReceiveChat('强元素已满（%d/%d，含原生）' % (kinds, MAX_ELE), MessageType.System)
		return False
	pool = [s for s in ELE_STATS if ele_total(eq, s) <= 0]
	if not pool:
		Sender.Connection.ReceiveChat('没有可附加的新强元素', MessageType.System)
		return False
	need = ELE_COST[kinds]
	mat = eq.Info.ItemName
	if Sender.GetItemCount(mat) < need:
		Sender.Connection.ReceiveChat('需要背包同名装备「%s」x%d（第%d个强元素）' % (mat, need, kinds + 1), MessageType.System)
		return False
	if Sender.GetItemCount(MAT_CORUNDUM) < COST_CORUNDUM:
		Sender.Connection.ReceiveChat('需要%s x%d' % (MAT_CORUNDUM, COST_CORUNDUM), MessageType.System)
		return False
	if Sender.GetItemCount(MAT_MAGIC) < COST_MAGIC:
		Sender.Connection.ReceiveChat('需要%s x%d' % (MAT_MAGIC, COST_MAGIC), MessageType.System)
		return False
	Sender.TakeItem(mat, need)
	Sender.TakeItem(MAT_CORUNDUM, COST_CORUNDUM)
	Sender.TakeItem(MAT_MAGIC, COST_MAGIC)
	picked = random.choice(pool)
	amount = 2 if slot == EquipmentSlot.Armour else 1
	Sender.ItemStatsChangeRefresh(slot, picked, amount, StatSource.Added)
	Sender.Connection.ReceiveChat(
		'附加成功！%s 获得强元素 %s +%d（%d/%d）' % (
			mat, ELE_NAME.get(picked, str(picked)), amount, kinds + 1, MAX_ELE
		),
		MessageType.System
	)
	return True

def do_weapon_further(Sender, track):
	slot = EquipmentSlot.Weapon
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要再升的武器', MessageType.System)
		return False
	if eq.Info.Rarity != Rarity.Elite:
		Sender.Connection.ReceiveChat('只有稀世武器，且武器等级满级后才能再升', MessageType.System)
		return False
	cap = weapon_level_cap(eq)
	if not is_weapon_level_max(eq):
		Sender.Connection.ReceiveChat('请先将稀世武器升到满级后再升（当前 %d/%d）' % (int(eq.Level), cap), MessageType.System)
		return False
	locked = further_track(eq)
	if locked and locked != track:
		Sender.Connection.ReceiveChat('这把武器已经选择了%s，只能升这一项' % TRACK_NAME[locked], MessageType.System)
		return False
	est = weapon_ele_stat(eq)
	if track == 'ele' and est is None:
		Sender.Connection.ReceiveChat('该武器没有元素，无法升元素', MessageType.System)
		return False
	cur = further_amount(eq, track)
	if cur >= MAX_FURTHER:
		Sender.Connection.ReceiveChat('%s再升已满（+%d，含已有升级）' % (TRACK_NAME[track], MAX_FURTHER), MessageType.System)
		return False
	mat = eq.Info.ItemName
	if Sender.GetItemCount(mat) < 1:
		Sender.Connection.ReceiveChat('需要背包同名武器「%s」x1' % mat, MessageType.System)
		return False
	Sender.TakeItem(mat, 1)
	if track == 'dc':
		Sender.ItemStatsChangeRefresh(slot, Stat.MaxDC, 1, StatSource.Combine)
	elif track == 'magic':
		if added_stat(eq, Stat.MaxMC) < MAX_FURTHER:
			Sender.ItemStatsChangeRefresh(slot, Stat.MaxMC, 1, StatSource.Combine)
		if added_stat(eq, Stat.MaxSC) < MAX_FURTHER:
			Sender.ItemStatsChangeRefresh(slot, Stat.MaxSC, 1, StatSource.Combine)
	else:
		Sender.ItemStatsChangeRefresh(slot, est, 1, StatSource.Combine)
	cur = further_amount(eq, track)
	if track == 'ele':
		msg = '再升成功！%s 元素%s +%d/%d' % (mat, ELE_ATK_NAME.get(est, ''), cur, MAX_FURTHER)
	else:
		msg = '再升成功！%s %s +%d/%d' % (mat, TRACK_NAME[track], cur, MAX_FURTHER)
	Sender.Connection.ReceiveChat(msg, MessageType.System)
	return True

def max_weapon_level(Sender, eq, slot):
	cap = weapon_level_cap(eq)
	eq.Level = cap
	eq.Experience = 0
	if (int(eq.Flags) & int(UserItemFlags.Refinable)) != 0:
		eq.Flags = eq.Flags & ~UserItemFlags.Refinable
	Sender.ItemCompleteRefresh(eq.Index)
	return cap

def do_weapon_instant(Sender, track):
	slot = EquipmentSlot.Weapon
	eq = Sender.Equipment[int(slot)]
	if not eq:
		Sender.Connection.ReceiveChat('请先穿戴要一键满级的武器', MessageType.System)
		return False
	if eq.Info.Rarity != Rarity.Elite:
		Sender.Connection.ReceiveChat('只有稀世武器才能一键满级', MessageType.System)
		return False
	locked = further_track(eq)
	if locked:
		Sender.Connection.ReceiveChat('这把武器已经再升过（%s），不能再用一键满级' % TRACK_NAME[locked], MessageType.System)
		return False
	est = weapon_ele_stat(eq)
	if track == 'ele' and est is None:
		Sender.Connection.ReceiveChat('该武器没有元素，无法选择元素', MessageType.System)
		return False
	cur = further_amount(eq, track)
	if cur >= MAX_FURTHER:
		Sender.Connection.ReceiveChat('%s已达上限（+%d，含已有升级）' % (TRACK_NAME[track], MAX_FURTHER), MessageType.System)
		return False
	if Sender.GetItemCount(MAT_CORUNDUM) < COST_MAX_CORUNDUM:
		Sender.Connection.ReceiveChat('需要%s x%d' % (MAT_CORUNDUM, COST_MAX_CORUNDUM), MessageType.System)
		return False
	if Sender.GetItemCount(MAT_MAGIC) < COST_MAX_MAGIC:
		Sender.Connection.ReceiveChat('需要%s x%d' % (MAT_MAGIC, COST_MAX_MAGIC), MessageType.System)
		return False
	room = MAX_FURTHER - cur
	amount = random.randint(INSTANT_MIN, INSTANT_MAX)
	if amount > room:
		amount = room
	Sender.TakeItem(MAT_CORUNDUM, COST_MAX_CORUNDUM)
	Sender.TakeItem(MAT_MAGIC, COST_MAX_MAGIC)
	cap = max_weapon_level(Sender, eq, slot)
	name = eq.Info.ItemName
	if track == 'dc':
		Sender.ItemStatsChangeRefresh(slot, Stat.MaxDC, amount, StatSource.Combine)
	elif track == 'magic':
		Sender.ItemStatsChangeRefresh(slot, Stat.MaxMC, amount, StatSource.Combine)
		Sender.ItemStatsChangeRefresh(slot, Stat.MaxSC, amount, StatSource.Combine)
	else:
		Sender.ItemStatsChangeRefresh(slot, est, amount, StatSource.Combine)
	cur = further_amount(eq, track)
	if track == 'ele':
		msg = '一键满级成功！%s 等级 %d，元素%s +%d（当前 +%d/%d）' % (name, cap, ELE_ATK_NAME.get(est, ''), amount, cur, MAX_FURTHER)
	else:
		msg = '一键满级成功！%s 等级 %d，%s +%d（当前 +%d/%d）' % (name, cap, TRACK_NAME[track], amount, cur, MAX_FURTHER)
	Sender.Connection.ReceiveChat(msg, MessageType.System)
	return True

def say_for_menu(Menu, Sender=None):
	if Menu in JOBS or (Menu >= 101 and Menu <= 109) or Menu == PAGE_REFINE:
		return SAY_REFINE
	if Menu in ELE_SLOTS or Menu == PAGE_ELEMENT:
		return SAY_ELEMENT
	if Menu in FURTHER_MENUS or Menu == PAGE_FURTHER:
		return SAY_FURTHER
	if Menu in INSTANT_MENUS or Menu == PAGE_INSTANT:
		return SAY_INSTANT
	if Menu == PAGE_CHANGE:
		return SAY_CHANGE
	if Menu in CHANGE_SLOTS and Sender is not None:
		return say_change_slot(Sender, Menu)
	parsed = parse_change_ele_menu(Menu)
	if parsed and Sender is not None:
		return say_change_slot(Sender, parsed[0])
	if Menu in CHANGE_SLOTS or parsed:
		return SAY_CHANGE
	return SAY_MAIN

def frag_line(Sender):
	n = int(Sender.GetItemCount(FRAG))
	return '你目前有高级碎片：%d\n' % n

def eq2frag_group_of_index(idx):
	for g in EQ2FRAG_GROUPS:
		start, end = g[3]
		if start <= idx < end:
			return g
	return None

def say_eq2frag_main(Sender):
	return (
		'把装备兑换成高级碎片。每次用包裹里的 1 件装备，立刻换到对应数量的碎片，不需要消耗金币。\n'
		'请先把要兑换的装备放进包裹，穿在身上的不会被扣除。\n\n'
		'兑换数量：\n'
		'霹雷、龙纹剑、嗜魂法杖：15个\n'
		'屠龙、铁轮、逍遥扇：25个\n'
		'诺玛霹雷、诺玛铁轮、诺玛逍遥扇：20个\n'
		'天神法杖、破山剑、泰轮拂尘：40个\n'
		'项链、手镯、戒指一类：10个\n\n'
		+ frag_line(Sender) +
		'\n'
		'[兑换10个:1505]\n'
		'[兑换15个:1501]\n'
		'[兑换20个:1503]\n'
		'[兑换25个:1502]\n'
		'[兑换40个:1504]\n'
		'\n'
		'[返回:400]\n'
	)

def say_eq2frag_group(Sender, group):
	menu, qty, title, rng = group
	start, end = rng
	lines = []
	i = start
	row = []
	while i < end:
		name, _q = EQ2FRAG_ITEMS[i]
		row.append('[%s:%d]' % (name, EQ2FRAG_CONFIRM + i))
		if len(row) >= 3:
			lines.append(' '.join(row))
			row = []
		i += 1
	if row:
		lines.append(' '.join(row))
	return (
		'以下装备每件可兑换 %s。点一件先确认，再扣除。\n\n' % title
		+ frag_line(Sender) +
		'\n'
		+ '\n'.join(lines) +
		'\n\n'
		'[返回:1500]\n'
	)

def say_eq2frag_confirm(Sender, idx):
	name, qty = EQ2FRAG_ITEMS[idx]
	g = eq2frag_group_of_index(idx)
	back = g[0] if g else PAGE_EQ2FRAG
	have = int(Sender.GetItemCount(name))
	return (
		'你要用 1 件%s 兑换 %d 个高级碎片吗？\n\n' % (name, qty)
		+ '包裹里的%s：%d\n' % (name, have)
		+ frag_line(Sender) +
		'\n'
		'[确认兑换:%d]\n' % (EQ2FRAG_EXEC + idx)
		+ '[返回:%d]\n' % back
	)

def say_eq2frag_result(Sender, idx, ok):
	name, qty = EQ2FRAG_ITEMS[idx]
	g = eq2frag_group_of_index(idx)
	back = g[0] if g else PAGE_EQ2FRAG
	if ok:
		body = '兑换成功。已扣除 1 件%s，获得 %d 个高级碎片。\n\n' % (name, qty)
	else:
		body = '你的包裹里没有%s，没有扣除任何物品。\n请把装备放进包裹后再来。\n\n' % name
	return (
		body
		+ frag_line(Sender) +
		'\n'
		'[继续兑换:%d]\n' % back
		+ '[返回:400]\n'
	)

def do_eq2frag(Sender, idx):
	name, qty = EQ2FRAG_ITEMS[idx]
	if int(Sender.GetItemCount(name)) < 1:
		return False
	Sender.TakeItem(name, 1)
	Sender.GiveItem(FRAG, qty)
	return True

def frag2eq_indexes_for_cost(cost):
	result = []
	i = 0
	while i < len(FRAG2EQ_REWARDS):
		if FRAG2EQ_REWARDS[i][1] == cost:
			result.append(i)
		i += 1
	return result

def frag2eq_cost_back(cost):
	if cost == 10:
		return FRAG2EQ_TIER10
	return FRAG2EQ_TIER50

def say_frag2eq_main(Sender):
	return (
		'用高级碎片兑换装备。每次兑换 1 件，必定成功，不需要金币和其他材料。\n\n'
		'10个：全能指环、铁炼腕、龙之手镯、骑士手镯、心灵手镯、魔灵戒指、魔令项链，或虹魔套、魔血套中的任意一件。\n'
		'50个：英雄手套、心念手镯、魔令手镯中的任意一件。\n\n'
		+ frag_line(Sender) +
		'\n'
		'[10个兑换一件:1801]\n'
		'[50个兑换一件:1803]\n'
		'\n'
		'[返回:400]\n'
	)

def say_frag2eq_tier(Sender, cost):
	idxs = frag2eq_indexes_for_cost(cost)
	if cost == 10:
		head = '10个高级碎片可以兑换下面任意一件。虹魔套、魔血套也是按件选，不会一次给整套。\n'
	else:
		head = '50个高级碎片可以兑换下面任意一件。\n'
	parts = []
	last_group = None
	row = []
	for idx in idxs:
		name, _c, group = FRAG2EQ_REWARDS[idx]
		if group != last_group:
			if row:
				parts.append(' '.join(row))
				row = []
			if group in ('单件', '虹魔套', '魔血套'):
				parts.append('')
				parts.append(group + '：')
			last_group = group
		row.append('[%s:%d]' % (name, FRAG2EQ_CONFIRM + idx))
		if len(row) >= 3:
			parts.append(' '.join(row))
			row = []
	if row:
		parts.append(' '.join(row))
	return (
		head + '\n'
		+ frag_line(Sender) +
		'\n'
		+ '\n'.join(parts) +
		'\n\n'
		'[返回:1800]\n'
	)

def say_frag2eq_confirm(Sender, idx):
	name, cost, _g = FRAG2EQ_REWARDS[idx]
	back = frag2eq_cost_back(cost)
	return (
		'你要用 %d 个高级碎片兑换 1 件%s吗？\n\n' % (cost, name)
		+ frag_line(Sender) +
		'\n'
		'[确认兑换:%d]\n' % (FRAG2EQ_EXEC + idx)
		+ '[返回:%d]\n' % back
	)

def say_frag2eq_result(Sender, idx, ok):
	name, cost, _g = FRAG2EQ_REWARDS[idx]
	back = frag2eq_cost_back(cost)
	if ok:
		body = '兑换成功。已扣除 %d 个高级碎片，获得 1 件%s。\n\n' % (cost, name)
	else:
		body = '你的高级碎片不足 %d 个，没有扣除任何物品。\n\n' % cost
	return (
		body
		+ frag_line(Sender) +
		'\n'
		'[继续兑换:%d]\n' % back
		+ '[返回:400]\n'
	)

def do_frag2eq(Sender, idx):
	name, cost, _g = FRAG2EQ_REWARDS[idx]
	if int(Sender.GetItemCount(FRAG)) < cost:
		return False
	Sender.TakeItem(FRAG, cost)
	Sender.GiveItem(name, 1)
	return True

def exchange_click(Sender, Menu):
	if Menu == PAGE_EQ2FRAG:
		return say_eq2frag_main(Sender)
	for g in EQ2FRAG_GROUPS:
		if g[0] == Menu:
			return say_eq2frag_group(Sender, g)
	if EQ2FRAG_CONFIRM <= Menu < EQ2FRAG_CONFIRM + len(EQ2FRAG_ITEMS):
		return say_eq2frag_confirm(Sender, Menu - EQ2FRAG_CONFIRM)
	if EQ2FRAG_EXEC <= Menu < EQ2FRAG_EXEC + len(EQ2FRAG_ITEMS):
		idx = Menu - EQ2FRAG_EXEC
		ok = do_eq2frag(Sender, idx)
		return say_eq2frag_result(Sender, idx, ok)
	if Menu == PAGE_FRAG2EQ:
		return say_frag2eq_main(Sender)
	if Menu == FRAG2EQ_TIER10:
		return say_frag2eq_tier(Sender, 10)
	if Menu == FRAG2EQ_TIER50:
		return say_frag2eq_tier(Sender, 50)
	if FRAG2EQ_CONFIRM <= Menu < FRAG2EQ_CONFIRM + len(FRAG2EQ_REWARDS):
		return say_frag2eq_confirm(Sender, Menu - FRAG2EQ_CONFIRM)
	if FRAG2EQ_EXEC <= Menu < FRAG2EQ_EXEC + len(FRAG2EQ_REWARDS):
		idx = Menu - FRAG2EQ_EXEC
		ok = do_frag2eq(Sender, idx)
		return say_frag2eq_result(Sender, idx, ok)
	return None

def OnClick(args):
	Self = args[0]
	Sender = args[1]
	Menu = args[2]
	Dict = {}
	ex_say = None
	if Menu in JOBS:
		slot, stat, per = JOBS[Menu]
		do_refine(Sender, slot, stat, per)
	elif Menu >= 101 and Menu <= 109:
		slot, stat, per = JOBS[Menu - 100]
		do_reset(Sender, slot, stat)
	elif Menu in ELE_SLOTS:
		do_add_element(Sender, ELE_SLOTS[Menu])
	elif Menu in FURTHER_MENUS:
		do_weapon_further(Sender, FURTHER_MENUS[Menu])
	elif Menu in INSTANT_MENUS:
		do_weapon_instant(Sender, INSTANT_MENUS[Menu])
	else:
		parsed = parse_change_ele_menu(Menu)
		if parsed:
			do_change_element(Sender, CHANGE_SLOTS[parsed[0]], parsed[1])
		else:
			ex_say = exchange_click(Sender, Menu)
	if ex_say is not None:
		Dict['Say'] = ex_say
	else:
		Dict['Say'] = say_for_menu(Menu, Sender)
	return Dict

NpcEvent.add_listener(5656, 'OnClick', OnClick)
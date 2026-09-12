# -*- coding: utf-8 -*-
#载入模块SYS
import sys

#商品列表  '商品名称'  商品价格比例,固定格式为float(1.0)比例倍数
shudiangoodslist =[
('火球术',float(1)),  # lv7
('火球术（秘籍）',float(1)),  # lv7
('基本剑术',float(1)),  # lv7
('基本剑术（秘籍）',float(1)),  # lv7
('治愈术',float(1)),  # lv7
('治愈术（秘籍）',float(1)),  # lv7
('精神力战法',float(1)),  # lv8
('精神力战法（秘籍）',float(1)),  # lv8
('霹雳掌',float(1)),  # lv8
('霹雳掌（秘籍）',float(1)),  # lv8
('冰月神掌',float(1)),  # lv9
('冰月神掌（秘籍）',float(1)),  # lv9
('风掌',float(1)),  # lv10
('风掌（秘籍）',float(1)),  # lv10
('抗拒火环',float(1)),  # lv12
('抗拒火环（秘籍）',float(1)),  # lv12
('施毒术',float(1)),  # lv12
('施毒术（秘籍）',float(1)),  # lv12
('灵魂火符',float(1)),  # lv13
('灵魂火符（秘籍）',float(1)),  # lv13
('诱惑之光',float(1)),  # lv13
('诱惑之光（秘籍）',float(1)),  # lv13
('攻杀剑术',float(1)),  # lv14
('攻杀剑术（秘籍）',float(1)),  # lv14
('瞬息移动',float(1)),  # lv14
('瞬息移动（秘籍）',float(1)),  # lv14
('月魂断玉',float(1)),  # lv14
('月魂断玉（秘籍）',float(1)),  # lv14
('大火球',float(1)),  # lv15
('大火球（秘籍）',float(1)),  # lv15
('雷电术',float(1)),  # lv16
('雷电术（秘籍）',float(1)),  # lv16
('冰月震天',float(1)),  # lv17
('冰月震天（秘籍）',float(1)),  # lv17
('召唤骷髅',float(1)),  # lv17
('召唤骷髅（秘籍）',float(1)),  # lv17
('击风',float(1)),  # lv18
('击风（秘籍）',float(1)),  # lv18
('刺杀剑术',float(1)),  # lv19
('刺杀剑术（秘籍）',float(1)),  # lv19
('地狱火',float(1)),  # lv20
('地狱火（秘籍）',float(1)),  # lv20
('隐身术',float(1)),  # lv20
('隐身术（秘籍）',float(1)),  # lv20
('疾光电影',float(1)),  # lv21
('疾光电影（秘籍）',float(1)),  # lv21
('幽灵盾',float(1)),  # lv21
('幽灵盾（秘籍）',float(1)),  # lv21
('冰沙掌',float(1)),  # lv22
('冰沙掌（秘籍）',float(1)),  # lv22
('风震天',float(1)),  # lv23
('风震天（秘籍）',float(1)),  # lv23
('集体隐身术',float(1)),  # lv23
('集体隐身术（秘籍）',float(1)),  # lv23
('半月弯刀',float(1)),  # lv24
('半月弯刀（秘籍）',float(1)),  # lv24
('火墙',float(1)),  # lv24
('火墙（秘籍）',float(1)),  # lv24
('月魂灵波',float(1)),  # lv24
('月魂灵波（秘籍）',float(1)),  # lv24
('神圣战甲术',float(1)),  # lv25
('神圣战甲术（秘籍）',float(1)),  # lv25
('圣言术',float(1)),  # lv26
('圣言术（秘籍）',float(1)),  # lv26
('困魔咒',float(1)),  # lv27
('困魔咒（秘籍）',float(1)),  # lv27
('野蛮冲撞',float(1)),  # lv27
('野蛮冲撞（秘籍）',float(1)),  # lv27
]

yaodiangoodslist=[
('金创药（小）',float(1)),
('金创药（中）',float(1)),
('金创药（大）',float(1)),
('金疮药（特）',float(1)),
('魔法药（小）',float(1)),
('魔法药（中）',float(1)),
('魔法药（大）',float(1)),
('魔法药（特）',float(1)),
('太阳水',float(1)),
('强效太阳水',float(1))]

wuqidiangoodslist=[
('木剑',float(1)),
('匕首',float(1)),
('青铜剑',float(1)),
('铁剑',float(1)),
('乌木剑',float(1)),
('青铜斧',float(1)),
('海魂',float(1)),
('半月',float(1)),
('斩马刀',float(1)),
('偃月',float(1)),
('降魔',float(1)),
('鹤嘴锄',float(1)),
]

shoushidiangoodslist=[
('六绝星环',float(1)),
('指环',float(1)),
('牛角戒指',float(1)),
('水晶魔戒',float(1)),
('古铜戒指',float(1)),
('蓝色水晶戒指',float(1)),
('黑色水晶戒指',float(1)),
('珍珠戒指',float(1)),
('蛇眼戒指',float(1)),
('魅力戒指',float(1)),
('道德戒指',float(1)),
('铁手镯',float(1)),
('小手镯',float(1)),
('银手镯',float(1)),
('皮制手套',float(1)),
('大手镯',float(1)),
('钢手镯',float(1)),
('黑檀手镯',float(1)),
('道士手镯',float(1)),
('魔法手镯',float(1)),
('坚固手套',float(1)),
('金项链',float(1)),
('传统项链',float(1)),
('白金项链',float(1)),
('黑色水晶项链',float(1)),
('黑檀项链',float(1)),
('黄色水晶项链',float(1)),
('灯笼项链',float(1)),
('魔鬼项链',float(1)),
('真善项链',float(1)),
('琥珀项链',float(1)),
('白色虎齿项链',float(1))]

buyidiangoodslist=[
('布衣（男）',float(1)),
('布衣（女）',float(1)),
('轻型盔甲（男）',float(1)),
('轻型盔甲（女）',float(1)),
('重盔甲（男）',float(1)),
('重盔甲（女）',float(1)),
('灵魂战衣（男）',float(1)),
('灵魂战衣（女）',float(1)),
('草鞋',float(1)),
('皮靴',float(1)),
('青铜头盔',float(1)),
('魔法头盔',float(1)),
('魔法长袍（男）',float(1)),
('魔法长袍（女）',float(1))]

zahuodiangoodslist=[
('蜡烛',float(1)),
('亮蜡烛',float(1)),
('火把',float(1)),
('亮火把',float(1)),
('回城卷',float(1)),
('随机传送卷',float(1)),
('黄色药粉（小）',float(1)),
('灰色药粉（小）',float(1)),
('护身符（小）',float(1)),
('护身符（火）',float(1)),
('护身符（冰）',float(1)),
('护身符（雷）',float(1)),
('护身符（风）',float(1)),
('护身符（幻影）',float(1)),
('护身符（暗黑）',float(1)),
('护身符（神圣）',float(1)),
('灵魂护身符（小）',float(1)),
]


# -*- coding: utf-8 -*-
#载入模块SYS
import sys
#引用模块的地址
from Globals import *
import collections
from Defines import *
import ServerEvent
import Server
import clr
import random
import Utils.ServerUtils as ServerUtils

from Ser import 死亡竞技场
from Ser import 死亡竞技场刷怪
#from Ser import 沙巴克攻城
from Ser import 沙巴克兵器商清理
from Ser import 沙巴克地下城
#from Ser import 庄园
#from Ser import 灶神
from Ser import 货郎
from Ser import 诺玛天眼
from Ser import 诺玛天牢
from Ser import 酷跑
from Ser import 跑船活动公告
from Ser import 怪物攻城
from Ser import 尸王攻城
#from Ser import 发送攻城战通知
from Ser import 跑船排名奖励
from Ser import 诺玛任务
from Ser import 定期清理怪物
from Ser import 沙巴克怪物攻城活动
from Ser import 新年舞会

clr.AddReference("Library")
clr.AddReference('System')
from Library import *
import Server.Envir.SEnvir as SEnvir
# 活动格式为 ((开始时间), (结束时间), 活动函数名)
# 时间格式为 (每周几, 几点, 几分)
# 注意 周日是0 周一是1 以此类推 周六是6
# 注意 时间使用24小时制 结束时间需要晚于开始时间
# 活动函数需要根据传入的bool参数判断是开启活动(True) 还是结束活动(False)
TimedEvents = [
               # ((5, 20, 50), (5, 22, 00), 尸王攻城.TestSpawn1),
               # ((5, 21, 00), (5, 22, 00), 尸王攻城.TestSpawn2),

               # ((6, 21, 00), (6, 22, 00), 发送攻城战通知.CreateArmsDealer),

               ((0, 22, 01), (0, 22, 02), 沙巴克兵器商清理.TestSpawn1),
               ((1, 22, 01), (1, 22, 02), 沙巴克兵器商清理.TestSpawn1),
               ((2, 22, 01), (2, 22, 02), 沙巴克兵器商清理.TestSpawn1),
               ((3, 22, 01), (3, 22, 02), 沙巴克兵器商清理.TestSpawn1),
               ((4, 22, 01), (4, 22, 02), 沙巴克兵器商清理.TestSpawn1),
               ((5, 22, 01), (5, 22, 02), 沙巴克兵器商清理.TestSpawn1),
               ((6, 22, 01), (6, 22, 02), 沙巴克兵器商清理.TestSpawn1),

               ((0, 23, 59), (0, 23, 59), 跑船排名奖励.TestSpawn1),

               # ((0, 19, 50), (0, 22, 00), 灶神.TestSpawn1),
               # ((0, 20, 00), (0, 22, 00), 灶神.TestSpawn2),
               # ((0, 20, 05), (0, 22, 00), 灶神.TestSpawn2),
               # ((0, 20, 10), (0, 22, 00), 灶神.TestSpawn2),
               # ((0, 20, 15), (0, 22, 00), 灶神.TestSpawn2),
               # ((0, 20, 20), (0, 22, 00), 灶神.TestSpawn2),

               # ((6, 21, 50), (6, 23, 59), 沙巴克怪物攻城活动.TestSpawn1),
               # ((6, 22, 00), (6, 23, 59), 沙巴克怪物攻城活动.TestSpawn2),
               # ((0, 21, 50), (0, 23, 59), 沙巴克怪物攻城活动.TestSpawn1),
               # ((0, 22, 00), (0, 23, 59), 沙巴克怪物攻城活动.TestSpawn2),
               # ((1, 21, 50), (1, 23, 59), 沙巴克怪物攻城活动.TestSpawn1),
               # ((1, 22, 00), (1, 23, 59), 沙巴克怪物攻城活动.TestSpawn2),

               # ((6, 18, 50), (6, 19, 20), 新年舞会.TestSpawn1),
               # ((6, 19, 00), (6, 19, 20), 新年舞会.TestSpawn2),
               # ((6, 19, 1), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 2), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 3), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 4), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 5), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 6), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 7), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 8), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 9), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 10), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 11), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 12), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 13), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 14), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 15), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 16), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 17), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 18), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 19), (6, 19, 20), 新年舞会.TestSpawn3),
               # ((6, 19, 3), (6, 19, 20), 新年舞会.TestSpawn4),
               # ((6, 19, 6), (6, 19, 20), 新年舞会.TestSpawn4),
               # ((6, 19, 9), (6, 19, 20), 新年舞会.TestSpawn4),
               # ((6, 19, 12), (6, 19, 20), 新年舞会.TestSpawn4),
               # ((6, 19, 15), (6, 19, 20), 新年舞会.TestSpawn4),
               # ((6, 19, 18), (6, 19, 20), 新年舞会.TestSpawn4),
               # ((6, 19, 18), (6, 19, 20), 新年舞会.TestSpawn5),
               # ((0, 18, 50), (0, 19, 20), 新年舞会.TestSpawn1),
               # ((0, 19, 00), (0, 19, 20), 新年舞会.TestSpawn2),
               # ((0, 19, 1), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 2), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 3), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 4), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 5), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 6), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 7), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 8), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 9), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 10), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 11), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 12), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 13), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 14), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 15), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 16), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 17), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 18), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 19), (0, 19, 20), 新年舞会.TestSpawn3),
               # ((0, 19, 3), (0, 19, 20), 新年舞会.TestSpawn4),
               # ((0, 19, 6), (0, 19, 20), 新年舞会.TestSpawn4),
               # ((0, 19, 9), (0, 19, 20), 新年舞会.TestSpawn4),
               # ((0, 19, 12), (0, 19, 20), 新年舞会.TestSpawn4),
               # ((0, 19, 15), (0, 19, 20), 新年舞会.TestSpawn4),
               # ((0, 19, 18), (0, 19, 20), 新年舞会.TestSpawn4),
               # ((0, 19, 18), (0, 19, 20), 新年舞会.TestSpawn5),
               # ((1, 18, 50), (1, 19, 20), 新年舞会.TestSpawn1),
               # ((1, 19, 00), (1, 19, 20), 新年舞会.TestSpawn2),
               # ((1, 19, 1), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 2), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 3), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 4), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 5), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 6), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 7), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 8), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 9), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 10), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 11), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 12), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 13), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 14), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 15), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 16), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 17), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 18), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 19), (1, 19, 20), 新年舞会.TestSpawn3),
               # ((1, 19, 3), (1, 19, 20), 新年舞会.TestSpawn4),
               # ((1, 19, 6), (1, 19, 20), 新年舞会.TestSpawn4),
               # ((1, 19, 9), (1, 19, 20), 新年舞会.TestSpawn4),
               # ((1, 19, 12), (1, 19, 20), 新年舞会.TestSpawn4),
               # ((1, 19, 15), (1, 19, 20), 新年舞会.TestSpawn4),
               # ((1, 19, 18), (1, 19, 20), 新年舞会.TestSpawn4),
               # ((1, 19, 18), (1, 19, 20), 新年舞会.TestSpawn5),

               ((0, 20, 02), (0, 23, 59), 货郎.TestSpawn1),
               ((1, 20, 02), (1, 23, 59), 货郎.TestSpawn1),
               ((2, 20, 02), (2, 23, 59), 货郎.TestSpawn1),
               ((3, 20, 02), (3, 23, 59), 货郎.TestSpawn1),
               ((4, 20, 02), (4, 23, 59), 货郎.TestSpawn1),
               ((5, 20, 02), (5, 23, 59), 货郎.TestSpawn1),
               ((6, 20, 02), (6, 23, 59), 货郎.TestSpawn1),

               ((0, 20, 50), (0, 21, 30), 跑船活动公告.TestSpawn1),
               ((0, 21, 00), (0, 21, 30), 跑船活动公告.TestSpawn2),

               ((1, 23, 00), (2, 00, 59), 诺玛任务.TestSpawn1),
               ((2, 2, 00), (2, 3, 59), 诺玛任务.TestSpawn1),
               ((2, 5, 00), (2, 6, 59), 诺玛任务.TestSpawn1),
               ((2, 8, 00), (2, 9, 59), 诺玛任务.TestSpawn1),
               ((2, 11, 00), (2, 12, 59), 诺玛任务.TestSpawn1),
               ((2, 14, 00), (2, 15, 59), 诺玛任务.TestSpawn1),
               ((2, 17, 00), (2, 18, 59), 诺玛任务.TestSpawn1),
               ((2, 20, 00), (2, 21, 59), 诺玛任务.TestSpawn1),
               
               ((3, 23, 00), (4, 00, 59), 诺玛任务.TestSpawn2),
               ((4, 2, 00), (4, 3, 59), 诺玛任务.TestSpawn2),
               ((4, 5, 00), (4, 5, 59), 诺玛任务.TestSpawn2),
               ((4, 8, 00), (4, 9, 59), 诺玛任务.TestSpawn2),
               ((4, 11, 00), (4, 12, 59), 诺玛任务.TestSpawn2),
               ((4, 14, 00), (4, 15, 59), 诺玛任务.TestSpawn2),
               ((4, 17, 00), (4, 18, 59), 诺玛任务.TestSpawn2),
               ((4, 20, 00), (4, 21, 59), 诺玛任务.TestSpawn2),
               ((4, 23, 00), (5, 1, 00), 诺玛任务.TestSpawn3),
               
               ((5, 20, 00), (5, 22, 00), 诺玛任务.TestSpawn3),
               ((5, 23, 00), (6, 1, 00), 诺玛任务.TestSpawn3),
               ((6, 2, 00), (6, 4, 00), 诺玛任务.TestSpawn3),
               ((6, 5, 00), (6, 7, 00), 诺玛任务.TestSpawn3),
               ((6, 8, 00), (6, 10, 00), 诺玛任务.TestSpawn3),
               ((6, 11, 00), (6, 13, 00), 诺玛任务.TestSpawn3),
               ((6, 14, 00), (6, 16, 00), 诺玛任务.TestSpawn3),
               ((6, 17, 00), (6, 19, 00), 诺玛任务.TestSpawn3),
               
               ((6, 20, 00), (6, 22, 00), 诺玛任务.TestSpawn4),
               ((6, 23, 00), (0, 1, 00), 诺玛任务.TestSpawn4),
               ((0, 2, 00), (0, 4, 00), 诺玛任务.TestSpawn4),
               ((0, 5, 00), (0, 7, 00), 诺玛任务.TestSpawn4),
               ((0, 8, 00), (0, 10, 00), 诺玛任务.TestSpawn4),
               ((0, 11, 00), (0, 13, 00), 诺玛任务.TestSpawn4),
               ((0, 14, 00), (0, 16, 00), 诺玛任务.TestSpawn4),
               ((0, 17, 00), (0, 19, 00), 诺玛任务.TestSpawn4),

               ((0, 00, 00), (0, 23, 59), 定期清理怪物.TestSpawn1),
               ((0, 4, 00), (0, 23, 59), 定期清理怪物.TestSpawn1),
               ((0, 8, 00), (0, 23, 59), 定期清理怪物.TestSpawn1),
               ((0, 12, 00), (0, 23, 59), 定期清理怪物.TestSpawn1),
               ((0, 16, 00), (0, 23, 59), 定期清理怪物.TestSpawn1),
               ((0, 20, 00), (0, 23, 59), 定期清理怪物.TestSpawn1),
               ((1, 00, 00), (1, 23, 59), 定期清理怪物.TestSpawn1),
               ((1, 4, 00), (1, 23, 59), 定期清理怪物.TestSpawn1),
               ((1, 8, 00), (1, 23, 59), 定期清理怪物.TestSpawn1),
               ((1, 12, 00), (1, 23, 59), 定期清理怪物.TestSpawn1),
               ((1, 16, 00), (1, 23, 59), 定期清理怪物.TestSpawn1),
               ((1, 20, 00), (1, 23, 59), 定期清理怪物.TestSpawn1),
               ((2, 00, 00), (2, 23, 59), 定期清理怪物.TestSpawn1),
               ((2, 4, 00), (2, 23, 59), 定期清理怪物.TestSpawn1),
               ((2, 8, 00), (2, 23, 59), 定期清理怪物.TestSpawn1),
               ((2, 12, 00), (2, 23, 59), 定期清理怪物.TestSpawn1),
               ((2, 16, 00), (2, 23, 59), 定期清理怪物.TestSpawn1),
               ((2, 20, 00), (2, 23, 59), 定期清理怪物.TestSpawn1),
               ((3, 00, 00), (3, 23, 59), 定期清理怪物.TestSpawn1),
               ((3, 4, 00), (3, 23, 59), 定期清理怪物.TestSpawn1),
               ((3, 8, 00), (3, 23, 59), 定期清理怪物.TestSpawn1),
               ((3, 12, 00), (3, 23, 59), 定期清理怪物.TestSpawn1),
               ((3, 16, 00), (3, 23, 59), 定期清理怪物.TestSpawn1),
               ((3, 20, 00), (3, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 00, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 4, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 8, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 12, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 16, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 20, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((4, 00, 00), (4, 23, 59), 定期清理怪物.TestSpawn1),
               ((5, 00, 00), (5, 23, 59), 定期清理怪物.TestSpawn1),
               ((5, 4, 00), (5, 23, 59), 定期清理怪物.TestSpawn1),
               ((5, 8, 00), (5, 23, 59), 定期清理怪物.TestSpawn1),
               ((5, 12, 00), (5, 23, 59), 定期清理怪物.TestSpawn1),
               ((5, 16, 00), (5, 23, 59), 定期清理怪物.TestSpawn1),
               ((5, 20, 00), (5, 23, 59), 定期清理怪物.TestSpawn1),
               ((6, 00, 00), (6, 23, 59), 定期清理怪物.TestSpawn1),
               ((6, 4, 00), (6, 23, 59), 定期清理怪物.TestSpawn1),
               ((6, 8, 00), (6, 23, 59), 定期清理怪物.TestSpawn1),
               ((6, 12, 00), (6, 23, 59), 定期清理怪物.TestSpawn1),
               ((6, 16, 00), (6, 23, 59), 定期清理怪物.TestSpawn1),
               ((6, 20, 00), (6, 23, 59), 定期清理怪物.TestSpawn1),
               ]

WeekTimedEvents = [
               [((6, 21, 50), (6, 21, 59), 死亡竞技场.doublePKTZ),
               ((6, 21, 55), (6, 21, 57), 死亡竞技场.doublePKTZ1),
               ((6, 22, 00), (6, 23, 59), 死亡竞技场.doublePK),
               ((6, 22, 01), (6, 23, 59), 死亡竞技场.doubleEXP),
               ((6, 22, 02), (6, 23, 59), 死亡竞技场.doubleEXP),
               ((6, 22, 03), (6, 23, 59), 死亡竞技场.doubleEXP),
               ((6, 22, 04), (6, 23, 59), 死亡竞技场.doubleEXP),
               ((6, 22, 06), (6, 23, 59), 死亡竞技场刷怪.TestSpawn1),
               ((6, 22, 12), (6, 23, 59), 死亡竞技场刷怪.TestSpawn2),
               ((6, 22, 18), (6, 23, 59), 死亡竞技场刷怪.TestSpawn3),
               ((6, 22, 24), (6, 23, 59), 死亡竞技场刷怪.TestSpawn4),
               ((6, 22, 30), (6, 23, 59), 死亡竞技场刷怪.TestSpawn5),
               ((6, 22, 36), (6, 23, 59), 死亡竞技场刷怪.TestSpawn6),
               ((6, 22, 42), (6, 23, 59), 死亡竞技场刷怪.TestSpawn7),
               ((6, 22, 48), (6, 23, 59), 死亡竞技场刷怪.TestSpawn8),
               ((6, 22, 54), (6, 23, 59), 死亡竞技场刷怪.TestSpawn9),],

               [((6, 21, 50), (6, 23, 59), 沙巴克地下城.TestSpawn1),
               ((6, 22, 00), (6, 23, 59), 沙巴克地下城.TestSpawn2),
               ((6, 22, 20), (6, 23, 59), 沙巴克地下城.TestSpawn3),
               ((6, 22, 40), (6, 23, 59), 沙巴克地下城.TestSpawn3),
               ((6, 23, 00), (6, 23, 59), 沙巴克地下城.TestSpawn4),
               ((6, 23, 20), (6, 23, 59), 沙巴克地下城.TestSpawn3),
               ((6, 23, 40), (6, 23, 59), 沙巴克地下城.TestSpawn5),],

               [((6, 22, 00), (6, 23, 00), 诺玛天眼.TestSpawn1),
               ((6, 22, 00), (6, 23, 00), 诺玛天牢.TestSpawn1),],

               [((6, 22, 00), (6, 22, 14), 酷跑.doublePKTZ),
               ((6, 22, 15), (6, 23, 00), 酷跑.doublePK),],

               ]

# 进入新的一分钟时触发此函数
def OnMinuteChange(args):
	#判断服务器时间
	day_of_Week = (int)(args[0].DayOfWeek)
	hour = args[0].Hour
	minute = args[0].Minute
	res = []

	#ServerUtils.SendMsgToAll("day={}， hour={}， minute={}".format(day_of_Week, hour, minute), MessageType.System)

	for event in TimedEvents:
		begin_time = event[0]
		end_time = event[1]

		if begin_time[0] == day_of_Week and begin_time[1] == hour and begin_time[2] == minute:
			# 开启活动
			res.append(event[2](True))
			continue
		if end_time[0] == day_of_Week and end_time[1] == hour and end_time[2] == minute:
			# 结束活动
			res.append(event[2](False))
			continue

	gregorianCalendar = System.Activator.CreateInstance(System.Globalization.GregorianCalendar)
	#获取指定日期是周数 CalendarWeekRule指定 第一周开始于该年的第一天，DayOfWeek指定每周第一天是星期几　
	weekOfYear= gregorianCalendar.GetWeekOfYear(SEnvir.Now, System.Globalization.CalendarWeekRule.FirstDay, System.DayOfWeek.Monday)
	for event in WeekTimedEvents[weekOfYear % len(WeekTimedEvents)]:
		begin_time = event[0]
		end_time = event[1]

		if begin_time[0] == day_of_Week and begin_time[1] == hour and begin_time[2] == minute:
			# 开启活动
			res.append(event[2](True))
			continue
		if end_time[0] == day_of_Week and end_time[1] == hour and end_time[2] == minute:
			# 结束活动
			res.append(event[2](False))
			continue

	return res

# 进入新的一天触发此函数
def OnDayChange(args): #args[0] 记录的是前一天的时间
	#判断服务器时间
	now = Server.Envir.SEnvir.Now.AddHours(12)
	day_of_Week = (int)(now.DayOfWeek)
	day_of_Month = (int)(now.Day)
	hour = args[0].Hour
	minute = args[0].Minute

	# 每日重置个人变量
	# 请移除PlayerProcess.py中OnDayChange()里面重置个人变量的语句
	# 并改为在这里进行重置
	# 这里复位所有玩家的某个变量 有多个变量需要重置的 都要写
	# SEnvir.ResetVariableForAllPlayers(变量名,默认值)
	SEnvir.ResetVariableForAllPlayers(TK_WXDZ_ONOFF,0)
	SEnvir.ResetVariableForAllPlayers(BV_QT_TODAY,0)  #每日任务复位
	SEnvir.ResetVariableForAllPlayers(BV_QT_KILLMON,0)  #每日任务杀怪复位
	SEnvir.ResetVariableForAllPlayers(BV_QT_KILLNUM,0)   #每日任务杀怪计数复位
	SEnvir.ResetVariableForAllPlayers(BV_NUM_DAILYTASK,0) #每日任务完成数量
	SEnvir.ResetVariableForAllPlayers(BV_NUM_DAILYRESET,0) #每日任务重置刷新
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_MIRILIBAO,0) #每日礼包领取重置
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_USE_ITEM_WAN,0) #每日丸使用时间重置
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_USE_ITEM_HUIHUNJUAN,0) #每日回魂卷使用时间重置
	SEnvir.ResetVariableForAllPlayers(GV_NEW_PLAYER_EXP_BUFF_COUNT, 0) #每日等级排行经验补助
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_SBKCMFW, 0) #沙巴克攻城天复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_CUNJIEPAOCHUANG, 0) #新春跑船活动复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_XINCHUNZHUFU, 0) #新春许愿活动
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_ZHIBOBIXUNZHANG, 0) #直播币兑换勋章每天限制
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_ZHIBOBISHENSHUI, 0) #直播币兑换神水每天限制
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_NUOMATIANLAOYI, 0) #恢复进诺玛天牢的限制
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_DANGAOCOUNT, 0) #雪球每日捐献复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_ZHIBOXUNZHANG, 0) #每天领取直播勋章复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_ARENAACCESS, 0) #死亡竞技场进入次数复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_DEATHMATCH, 0)  #死亡竞技场击杀人数复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_ONLINETIME, 0)  #玩家在线时长复位
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_COLLECT, 0)  #每天签到领取奖励复位
	GlobalSetV(GV_KILLMON_NUOMATIANLAO, 0) #恢复诺玛天牢的刷怪限制
	GlobalSetV(GV_BOSS_QINGDIANDANGAO, 0)  #雪球进度复位
	GlobalSetV(GV_BOSS_DANGAOSHUAXIN, 0)   #雪球每日刷新复位
	dicyihou = {}
	GlobalSetObV(GV_PLAYER_BAINIAN, dicyihou)  #领取城主拜年奖励复位
	#Sender.Connection.ReceiveChat("******玛法大陆迎来了新的一天******",MessageType.System)
	Server.Envir.SEnvir.Log("隔天调用成功")
	if(day_of_Week == 1):   #周判断
		OnWeekChange(args)
	if(day_of_Month == 1):                 #月判断
		OnMonthChange(args)
	
ResetVariable = [
GV_PLAYER_ZHOUPAOCHUANG,  #周跑船任务复位
GV_PLAYER_ZHOUJINGJICHANG, #周竞技场活动复位
GV_PLAYER_ZHOUKILLELITE,  #周精英任务复位
GV_KILLELITE_BSYSELITE, #半兽勇士
GV_KILLELITE_JXDJCELITE, #巨型多角虫
GV_KILLELITE_KLJYELITE, #骷髅精灵
GV_KILLELITE_SWELITE, #尸王
GV_KILLELITE_MYJJELITE, #蚂蚁将军
GV_KILLELITE_HJCELITE, #红甲虫
GV_KILLELITE_WMWSELITE, #沃玛卫士
GV_KILLELITE_XEQCELITE, #邪恶钳虫
GV_KILLELITE_BYZELITE, #白野猪
GV_KILLELITE_GGJELITE, #骨鬼将
GV_KILLELITE_BJSSELITE, #八角首领
GV_KILLELITE_DFLELITE, #大法老
GV_KILLELITE_SGWELITE, #神鬼王
GV_KILLELITE_HFTELITE, #护法天
GV_KILLELITE_PYGJELITE, #潘夜鬼将
GV_KILLELITE_FKMSDELITE, #疯狂魔神盗
GV_KILLELITE_ZTSJELITE, #震天首将
GV_KILLELITE_BWSWELITE, #霸王守卫
GV_KILLELITE_NMDZELITE, #诺玛队长
GV_KILLELITE_NMZZLELITE, #诺玛族长老
GV_PLAYER_ZHOUKILLBOSS, #周BOSS任务复位
GV_PLAYER_ZHOUKILLBOSS1, #周BOSS任务复位
GV_PLAYER_ZHOUKILLBOSS2, #周BOSS任务复位
GV_PLAYER_ZHOUKILLBOSS3, #周BOSS任务复位
GV_KILLBOSS_JSWBOSS, #僵尸王
GV_KILLBOSS_WMJZBOSS, #沃玛教主
GV_KILLBOSS_CLSBOSS, #触龙神
GV_KILLBOSS_CJHYZBOSS, #黑猪王
GV_KILLBOSS_KLJZBOSS, #骷髅教主
GV_KILLBOSS_CYEMBOSS, #赤月恶魔
GV_KILLBOSS_ZMJZBOSS, #祖玛教主
GV_KILLBOSS_PYNMWBOSS, #潘夜牛魔王
GV_KILLBOSS_ZTMSBOSS, #震天魔神
GV_KILLBOSS_BWJZBOSS, #霸王教主
GV_KILLBOSS_NMJZBOSS, #诺玛教主
GV_KILLBOSS_YHBOSS,   #蚁后
GV_KILLBOSS_NMWBOSS,  #驽马王
GV_PLAYER_ZHOUKILLXSJJBOSS, #周新人进阶任务
GV_PLAYER_PAOCHUANG, #跑船任务
GV_PLAYER_YIJIESHENJIAN, #跑船任务是否接到任务
GV_PLAYER_BUFFCOUNT, #BUFF购买限制
GV_PLAYER_PAOCHUANSHAGUAIJIFENG,
GV_PLAYER_SIGNIN,    #周签到复位
]
def OnWeekChange(args):
	SEnvir.ResetVariableForAllPlayers(ResetVariable,0)
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_LIUYIPAOKUARMOUR,0)
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_JINGJIARMOUR,0)
	GlobalSetV(GV_PLAYER_BUFF1, 0) #BUFF1
	GlobalSetV(GV_PLAYER_BUFF2, 0) #BUFF2
	GlobalSetV(GV_PLAYER_BUFF3, 0) #BUFF3
	GlobalSetV(GV_PLAYER_BUFF4, 0) #BUFF4
	GlobalSetV(GV_PLAYER_BUFF5, 0) #BUFF5
	GlobalSetV(GV_PLAYER_BUFF6, 0) #BUFF6
	GlobalSetV(GV_PLAYER_BUFF7, 0) #BUFF7
	GlobalSetV(GV_PLAYER_BUFF8, 0) #BUFF8
	GlobalSetV(GV_PLAYER_BUFF9, 0) #BUFF9
	GlobalSetV(GV_PLAYER_BUFF10, 0) #BUFF10
	GlobalSetV(GV_PLAYER_BUFF11, 0) #BUFF11
	Server.Envir.SEnvir.Log("隔周调用成功")
	
def OnMonthChange(args):
	#Sender.Connection.ReceiveChat("******玛法大陆迎来了新的一月******",MessageType.System)
	GlobalSetV(GV_PLAER_HUANHUAJUAN1, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN2, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN3, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN4, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN5, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN6, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN7, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN8, 0) #幻化卷购买限制
	GlobalSetV(GV_PLAER_HUANHUAJUAN9, 0) #幻化卷购买限制
	SEnvir.ResetVariableForAllPlayers(GV_PLAYER_XINNIANSZ,0) #新春时装个人购买限制
	GlobalSetV(GV_PLAYER_QJXINNIANSZN, 0) #新春时装男全局限制
	GlobalSetV(GV_PLAYER_QJXINNIANSZV, 0) #新春时装女全局限制
	Server.Envir.SEnvir.Log("隔月调用成功")
	
ServerEvent.add_listener("OnMinuteChange",OnMinuteChange)
ServerEvent.add_listener("OnDayChange",OnDayChange)

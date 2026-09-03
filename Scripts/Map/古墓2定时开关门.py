# -*- coding: utf-8 -*-
# 载入模块SYS
import sys
# 引用模块的地址
from Globals import *
import collections
from Defines import *
import PlayerEvent
import Server
import clr
import random
import Utils

clr.AddReference("Library")
clr.AddReference('System')
from Library import *
import Server.Envir.SEnvir as SEnvir


# 开启后多少秒关闭
OPEN_TIME = 10

# 2层地图序号
GUMU2_MAPS = [673,674,675,676,677]

# 2下3门点序号
GATES_1 = [3231,3232,3233,3234]
GATES_2 = [3235,3236,3237,3238]
GATES_3 = [3239,3240,3241,3242]
GATES_4 = [3243,3244,3245,3246]
GATES_5 = [3247,3248,3249,3250]

# 提示信息
PRE_MESSAGE = "前往古代坟墓3层的路很快就要关闭。(倒数{}秒)"
AFTER_MESSAGE = "前往古代坟墓3层的路已经关闭"
OPEN_MESSAGE = "前往古代坟墓3层的路: {} 已经开启"

def Gumu(interval):
	Utils.ServerUtils.SendMsgToMapOneArg([GUMU2_MAPS, PRE_MESSAGE.format(interval)])
	SEnvir.ScheduledCall("Map.古墓2定时开关门.ChangeGumuEntrance", SEnvir.Now.AddSeconds(interval), 'dont_care')


# 重置现在的门点
def CloseGumuGates(dont_care):
	for index1 in GATES_1:
		gate = SEnvir.GetMovementInfo(index1)
		if gate:
			gate.ExtraInfo = "关闭"
	Utils.ServerUtils.SendMsgToMapOneArg([673, AFTER_MESSAGE]);

	for index2 in GATES_2:
		gate = SEnvir.GetMovementInfo(index2)
		if gate:
			gate.ExtraInfo = "关闭"
	Utils.ServerUtils.SendMsgToMapOneArg([674, AFTER_MESSAGE]);

	for index3 in GATES_3:
		gate = SEnvir.GetMovementInfo(index3)
		if gate:
			gate.ExtraInfo = "关闭"
	Utils.ServerUtils.SendMsgToMapOneArg([675, AFTER_MESSAGE]);

	for index4 in GATES_4:
		gate = SEnvir.GetMovementInfo(index4)
		if gate:
			gate.ExtraInfo = "关闭"
	Utils.ServerUtils.SendMsgToMapOneArg([676, AFTER_MESSAGE]);

	for index5 in GATES_5:
		gate = SEnvir.GetMovementInfo(index5)
		if gate:
			gate.ExtraInfo = "关闭"
	Utils.ServerUtils.SendMsgToMapOneArg([677, AFTER_MESSAGE]);

# 开门
def ChangeGumuEntrance(dont_care):
	# 换门点
	# 每个2层地图 随机开启1个门点
	gate1 = SEnvir.GetMovementInfo(random.choice(GATES_1))
	gate1.ExtraInfo = "开启"
	Utils.ServerUtils.SendMsgToMapOneArg([673, OPEN_MESSAGE.format(gate1.SourceRegion.Description)])

	gate2 = SEnvir.GetMovementInfo(random.choice(GATES_2))
	gate2.ExtraInfo = "开启"
	Utils.ServerUtils.SendMsgToMapOneArg([674, OPEN_MESSAGE.format(gate2.SourceRegion.Description)])

	gate3 = SEnvir.GetMovementInfo(random.choice(GATES_3))
	gate3.ExtraInfo = "开启"
	Utils.ServerUtils.SendMsgToMapOneArg([675, OPEN_MESSAGE.format(gate3.SourceRegion.Description)])

	gate4 = SEnvir.GetMovementInfo(random.choice(GATES_4))
	gate4.ExtraInfo = "开启"
	Utils.ServerUtils.SendMsgToMapOneArg([676, OPEN_MESSAGE.format(gate4.SourceRegion.Description)])

	gate5 = SEnvir.GetMovementInfo(random.choice(GATES_5))
	gate5.ExtraInfo = "开启"
	Utils.ServerUtils.SendMsgToMapOneArg([677, OPEN_MESSAGE.format(gate5.SourceRegion.Description)])

	# 指定时间后关闭
	SEnvir.ScheduledCall("Map.古墓2定时开关门.CloseGumuGates", SEnvir.Now.AddSeconds(OPEN_TIME), 'dont_care')

	return


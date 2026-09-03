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

def ResetGumu3(dont_care):
	# 恢复4个机关
	SEnvir.ToggleNpcVisibility(314, True)
	SEnvir.ToggleNpcVisibility(315, True)
	SEnvir.ToggleNpcVisibility(316, True)
	SEnvir.ToggleNpcVisibility(317, True)

	# 移除石像特效
	npc = SEnvir.GetNpcObject(318)
	SEnvir.RemoveEffects(npc.ObjectID)

	# 发送提示信息
	Utils.ServerUtils.SendMsgToMapOneArg([678, "古墓3层的机关恢复了原状"])


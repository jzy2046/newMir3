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


def OnKillGumuBoss1():
	# 为石像添加抗拒火环的特效
	npc = SEnvir.GetNpcObject(318)
	SEnvir.AddEffect(npc.ObjectID, Effect.Repulsion)

	# 多少秒后重置古墓3的机关和石像
	interval = 300
	# 注意 按动4个机关会立刻刷出小BOSS
	# 谨慎调整小BOSS经验爆率 或者重置间隔 避免玩家无限刷小BOSS
	Utils.ServerUtils.SendMsgToMapOneArg([678, "护卫武士化为飞灰，石像发出了耀眼的光芒"])
	SEnvir.ScheduledCall("Map.古墓3重置NPC.ResetGumu3", SEnvir.Now.AddSeconds(interval), 'dont_care')
	
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

clr.AddReference("Library")
clr.AddReference('System')
from Library import *
import Server.Envir.SEnvir as SEnvir

GUMU_QUESTS = [172,173,174]  #需要完成任务的序号，指定的3个任务


# def OnCompleteQuest(args):
	# Sender=args[0]
	# UserQuest = args[1]
	# QuestInfo= UserQuest.QuestInfo
	# # Sender.Connection.ReceiveChat("你完成了任务: {}".format(QuestInfo.QuestName),MessageType.System)

	# # # 古墓任务
	# # if QuestInfo.Index in GUMU_QUESTS:
		# # GumuQuest(Sender, UserQuest, QuestInfo)

	# # return


# def GumuQuest(Sender, UserQuest, QuestInfo):
	# # if QuestInfo.Index == 172:
		# # # 古墓任务1 获取第一个字
		# # firstChar = random.randint(1, 24)
		# # UserQuest.ExtraInfo = say(firstChar)

		# # #Sender.Connection.ReceiveChat("你获取到了第1个字: {}".format(UserQuest.ExtraInfo),MessageType.System)
	# # elif QuestInfo.Index == 173:
		# # # 古墓任务2 获取第二个字
		# # firstChar = int(Sender.GetUserQuestByQuestIndex(172).ExtraInfo)
		# # # 不能跟第一个重复
		# # secondChar = random.randint(1, 24)
		# # while secondChar == firstChar:
			# # secondChar = random.randint(1, 24)

		# # UserQuest.ExtraInfo = say(secondChar)

		# # #Sender.Connection.ReceiveChat("你获取到了第2个字: {}".format(UserQuest.ExtraInfo),MessageType.System)
	# # elif QuestInfo.Index == 174:
		# # # 古墓任务2 获取第三个字
		# # firstChar = int(Sender.GetUserQuestByQuestIndex(172).ExtraInfo)
		# # secondChar = int(Sender.GetUserQuestByQuestIndex(173).ExtraInfo)
		# # # 不能跟第一个或第二个重复
		# # thirdChar = random.randint(1, 24)
		# # while thirdChar == firstChar or thirdChar == secondChar:
			# # thirdChar = random.randint(1, 24)

		# # UserQuest.ExtraInfo = say(thirdChar)

		# #Sender.Connection.ReceiveChat("你获取到了第3个字: {}".format(UserQuest.ExtraInfo),MessageType.System)

# PlayerEvent.add_listener("OnCompleteQuest",OnCompleteQuest)

# -*- coding: utf-8 -*-
#载入模块SYS
import sys
#引用模块的地址
from Globals import *
import collections
import clr
clr.AddReference("Library")
from Library import *
import NpcEvent
import random
import Server.Envir.SEnvir as SEnvir

def SendMsg(counter):
	# 公告信息延迟秒
	dalay = 300
	# 公告信息的内容
	lines = [
"纯公益，高度还原老板1.45，三端互通，微端下载！http://43.226.60.100:888/111.html官方下载地址！",
]
	###################下面的不用改################
	text = ""
	line_index = int(counter)

	if line_index is None:
		line_index = 0

	if line_index < 0:
		# 随机选一个
		text = random.choice(lines)
		line_index -= 1
	else:
		# 发送指定信息
		text = lines[line_index % len(lines)]
		
	BroadChat(text,MessageType.Notice)
	###################上面的不用改################

	# 自动定时发送公告
	SEnvir.DelayCall("Ser.系统公告.SendMsg", dalay, line_index + 1)



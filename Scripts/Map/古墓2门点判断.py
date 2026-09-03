# -*- coding: utf-8 -*-
import clr
clr.AddReference("Library")
from Library import *
import MapEvent
from Globals import *
import Server
from Library import *
import Server.Envir.SEnvir as SEnvir
		
def Gumu2(args):
	Movement=args[0]
	Sender = args[1]      #玩家
	
	if Movement and Movement.ExtraInfo:
		if Movement.ExtraInfo == "开启":
			return True
		else:
			Sender.Connection.ReceiveChat("感受到强大的力量阻止你进入",MessageType.System)

	return False     


# 3231为地图链接ID
MapEvent.add_listener(3231,"OnMovement",Gumu2)
MapEvent.add_listener(3232,"OnMovement",Gumu2)
MapEvent.add_listener(3233,"OnMovement",Gumu2)
MapEvent.add_listener(3234,"OnMovement",Gumu2)

MapEvent.add_listener(3235,"OnMovement",Gumu2)
MapEvent.add_listener(3236,"OnMovement",Gumu2)
MapEvent.add_listener(3237,"OnMovement",Gumu2)
MapEvent.add_listener(3238,"OnMovement",Gumu2)

MapEvent.add_listener(3239,"OnMovement",Gumu2)
MapEvent.add_listener(3240,"OnMovement",Gumu2)
MapEvent.add_listener(3241,"OnMovement",Gumu2)
MapEvent.add_listener(3242,"OnMovement",Gumu2)

MapEvent.add_listener(3243,"OnMovement",Gumu2)
MapEvent.add_listener(3244,"OnMovement",Gumu2)
MapEvent.add_listener(3245,"OnMovement",Gumu2)
MapEvent.add_listener(3246,"OnMovement",Gumu2)

MapEvent.add_listener(3247,"OnMovement",Gumu2)
MapEvent.add_listener(3248,"OnMovement",Gumu2)
MapEvent.add_listener(3249,"OnMovement",Gumu2)
MapEvent.add_listener(3250,"OnMovement",Gumu2)

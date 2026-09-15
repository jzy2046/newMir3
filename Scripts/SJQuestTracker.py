# -*- coding: utf-8 -*-
# Sync BV_NQ_SJKILL custom line onto engine QuestTracker (Hidden QuestInfo)
from Defines import *
try:
	from SJQuestIndexMap import SJ_QUEST_INDEX, SJ_QUEST_INDEXES
except Exception:
	SJ_QUEST_INDEX = {}
	SJ_QUEST_INDEXES = set()

def SyncSJQuestTracker(Sender):
	# Keep exactly one Hidden ghost-ship quest tracked for current BV_NQ_SJKILL.
	if not SJ_QUEST_INDEX:
		return
	try:
		bv = int(PlayerGetV(Sender, BV_NQ_SJKILL) or 0)
	except Exception:
		return
	want = SJ_QUEST_INDEX.get(bv)
	try:
		quests = list(Sender.Character.Quests)
	except Exception:
		return
	for uq in quests:
		try:
			qi = uq.QuestInfo
			if qi is None:
				continue
			idx = int(qi.Index)
			if idx not in SJ_QUEST_INDEXES:
				continue
			if want is not None and idx == want and (not uq.Completed):
				if not uq.Track:
					uq.Track = True
				continue
			Sender.QuestRemoveByUserQuestIndex(uq.Index)
		except Exception:
			pass
	if want is None:
		return
	has = False
	try:
		for uq in Sender.Character.Quests:
			if uq.QuestInfo is not None and int(uq.QuestInfo.Index) == want and (not uq.Completed):
				has = True
				uq.Track = True
				break
	except Exception:
		pass
	if not has:
		try:
			Sender.QuestAccept(want)
		except Exception:
			pass
		try:
			for uq in Sender.Character.Quests:
				if uq.QuestInfo is not None and int(uq.QuestInfo.Index) == want:
					uq.Track = True
					break
		except Exception:
			pass

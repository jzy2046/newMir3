# Drop adjust 2026-09-08

Applied all 23 checklist items via 	ools/Mir3DropAdjust20260908 (ServerTool + Library.dll).

- Backup: Database/Backup_drops_20260908_*
- Report: 	ools/Mir3DropAdjust20260908/apply_*.txt
- Counts: _whitelist/drop_adjust_20260908.txt
- Deleted items 急救丸*/清心丸* from System+ClientSystem; shop lines removed; quest random rewards remapped to 金创药/魔法药
- Deleted monster 僵尸王 (+ cascade Drop/Respawn/Stat)
- Gold unified to 10000 (mid) / 100000 (big); 诺玛教主 rare weapons Chance=10000 (1/10000)
- Name aliases used for 巨象兽/八脚首领/护法天/绿荫女神

VPS: pull main; if local Database dirty, stash/checkout System.db + ClientSystem.db before pull, then restart server.

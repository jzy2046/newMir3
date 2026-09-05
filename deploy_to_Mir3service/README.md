# Deploy to D:\Mir3service (live path from logs)

## What was wrong
- Live server logs reference D:\Mir3service\Scripts\... but that folder does NOT exist on this PC.
- Template 远程部署service still had OLD 商店列表.py (6011 bytes, Jan 2026) with 16 ItemInfo-missing goods → bookstore NRE when good.Item is null.
- mir3z fixed shop was 3029 bytes but syntax-broken (missing `]` on wuqidiangoodslist / zahuodiangoodslist). Now repaired (3031 bytes), 91 goods, **0 missing** vs D:\newMir3\Database\System.db ItemInfo.
- NpcEvent.trig_npc had no null guard on npc / npc.NPCInfo.
- mir3z/newMir3 Ser\定时活动.py OnDayChange used day_of_Month without defining it (deploy template 25517-byte copy already defined it).
- Log also shows 授权.license invalid — license issue separate; do not invent a license fix.

## Exact copy targets (from this folder → live D:\Mir3service)

Stop Server.exe first, then copy:

| This folder | → Live target |
|---|---|
| Scripts\Npc\商店列表.py | D:\Mir3service\Scripts\Npc\商店列表.py |
| Scripts\NpcEvent.py | D:\Mir3service\Scripts\NpcEvent.py |
| Scripts\Ser\定时活动.py | D:\Mir3service\Scripts\Ser\定时活动.py |
| Scripts\Npc\泰山\书店徐宝.py | D:\Mir3service\Scripts\Npc\泰山\书店徐宝.py |
| Scripts\Npc\比奇城\图书管理员.py | D:\Mir3service\Scripts\Npc\比奇城\图书管理员.py |
| Scripts\Npc\道馆\书*.py | D:\Mir3service\Scripts\Npc\道馆\ |
| Database\System.db | D:\Mir3service\Database\System.db |
| Database\ClientSystem.db | D:\Mir3service\Database\ClientSystem.db |
| optional_bin\Library.dll | D:\Mir3service\Library.dll (only if live loads side-by-side Library.dll; Costura-embedded Server.exe may ignore this) |

### 定时活动 note
- `定时活动.py` here is the mir3z/newMir3-sized copy with `day_of_Month = (int)(args[0].Day)` added in OnDayChange.
- If your live Scripts\Ser\定时活动.py is the larger ~25KB deploy variant, keep it (it already has day_of_Month). Alternate copy saved as `定时活动.DEPLOY_LARGER.py`.

### Server.exe rebuild
- ServerLibrary (Library.dll) rebuilt OK from mir3z Source with `if (good.Item == null) continue;`.
- Full Server.exe rebuild FAILED (DevExpress SvgImage resx / PyMetrics.resx). Not required if shop list has 0 missing items.

## Already synced on this PC
- D:\BaiduNetdiskDownload\3MIR3带假人版C#源码\远程部署service\ (Scripts shop/NpcEvent/bookstore NPCs + Database backed up then updated)
- D:\mir3src\远程部署service\ (same)
- D:\newMir3\Scripts\ (shop + NpcEvent + day_of_Month)

## After copy
1. Confirm D:\Mir3service exists (create or map from whatever the live host uses).
2. Backup live Database\*.db and Scripts before overwrite.
3. Restart Server.exe.
4. Test bookstore NPC buy dialog (泰山 书店徐宝 / other book NPCs).
5. If license log still complains about 授权.license — fix license separately.
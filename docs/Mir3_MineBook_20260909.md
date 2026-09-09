# Mir3 毒蛇/比奇矿洞书掉率x2 + 挖矿出矿率100% (2026-09-09)

## 约定确认
- DropInfo.Chance / MineInfo.Chance 均为 **1/N**：`Random.Next(Chance)==0`（掉落）或 `Random.Next(Chance...)<=0`（挖矿）
- 掉率翻倍 => Chance 减半（整数除法，最小 1）
- 出矿率 100% => MineInfo.Chance=1（仅 ItemType=Ore）

## 1) 毒蛇矿洞、比奇矿洞 技能书掉率 x2

### 地图集合（无字面“矿洞”名，按传送入口归类）
**比奇矿洞**（比奇城 Map#1 → 废矿矿山 D401*）：
Map#85–101（D401/D402/D403/D404/D405/D406、D411–D416、尸王殿 D401_001 等）

**毒蛇矿洞**（毒蛇山谷 Map#24 → 矿山 D42*/D43*/D45*）：
Map#103–129（D421/D422、D431–D436、D441–D444、D451/D452 及尸王殿）

### 变更
- 仅 ItemType=Book(14) 的 DropInfo
- 222 行 Chance 减半
- 怪物：老道僵尸/僧侣僵尸/僵尸2/3/4/雷电僵尸/尸王/尸王0
- 工具：tools/Mir3MineBook20260909
- 报告：tools/Mir3MineBook20260909/apply_20260909_215520.txt

### 注意
DropInfo 按怪物全局；上述僵尸/尸王在 **边境石矿 D14*** 也有刷新，故石矿同模板书掉率一并翻倍（引擎无法按地图拆 DropInfo，除非克隆怪物）。

## 2) 挖矿出矿率 100%
- 代码路径：`ServerLibrary/Models/Player/Aciton.cs` → `Mining()`  
  `SEnvir.Random.Next(info.Chance - info.Chance * Min(1, MiningSuccessRate/100)) <= 0`
- 数据：`MineInfo.Chance`（关联 MapInfo.Mining）
- 旧值：按矿种 400~10000（如铜矿500、铁矿600、黑铁1200~2000、金矿2500、钢玉/魔晶7000、石榴8000 等）
- 新值：**全部 Ore 行 Chance=1**（173 行）；非矿（秘密洞穴秘籍、深渊特殊物等 9 行）未改

## 交付
- 备份：Database/Backup_minebook_20260909_215520
- Database/System.db + ClientSystem.db（Data/ 已同步）
- 无 ServerLibrary 代码改动，无需重编 Library.dll
- 热更：D:\Mir3热更补丁\PC_7091_overwrite_latest\Data-ClientSystem.db.gz

## VPS
1. git pull newMir3（Database System.db + ClientSystem.db，及 Data/）
2. 不要覆盖 Users.db；按需保留 Server.ini listen
3. 重启服务端
4. 客户端覆盖 PC_7091_overwrite_latest（至少 Data-ClientSystem.db.gz）

# Mir3 五项修复报告 2026-09-09

## 1) 焰天火雨范围 +5 坐标位
- 根因: `Aciton.cs` MeteorShower 用 `GetTargets(..., 3)` 半径=3
- 修改: 半径 3 → 8（+5格）
- 文件: `ServerLibrary/Models/Player/Aciton.cs`
- 无限目标修复仍在: while 全取 possibleTargets，不再按 MeteorShowerTargetsCount 截断；Config 默认 9999

## 2) 移形换位技能书
- MagicType: GeoManipulation；MagicInfo Index=104 Name=移形换位 已存在
- 根因: 无 ItemType.Book / Shape=104 技能书，无法学习
- 修复: 新建 ItemInfo 移形换位 #122634 Shape=104（视觉克隆瞬息移动秘籍）
- 已同步 ClientSystem.db
- 学习路径: 使用书籍 → Shape 对应 MagicInfo.Index

## 3) 商店武器/首饰无法炼制升级
- 根因: 代码 Config.ShopNonRefinable 默认已是 false，NPC 购买路径也正确；但 **Server.ini 仍为 ShopNonRefinable=True**，运行时覆盖代码默认，购买时打上 UserItemFlags.NonRefinable
- 客户端提示「无法炼制/升级」来自物品 Flags.NonRefinable（非 ItemInfo）
- 修复: `D:\newMir3\Server.ini` → ShopNonRefinable=False（未提交 ini 到 git；VPS 必须改同名键）
- MarketPlace/元宝商城购买路径未强制 NonRefinable；问题主因是 NPC 商店 + ini
- 旧库存: 已买下的装备仍带 NonRefinable，需清旗或重买。可用工具/GM 清 Flags（见下方）

### VPS 必改 ini 键
```
ShopNonRefinable=False
```
改完重启服务端。不要只更新 Library.dll 而忘改 ini。

### 可选：清理已购 NonRefinable
对背包/仓库中「商店购入」且误标 NonRefinable 的装备执行 Flags &= ~NonRefinable（勿清书本 Book 的 NonRefinable）。

## 4) 黑度宫三层刷新 ×2
- Map Index=360 File=D1513 Desc=黑度宫三层
- 6 条 Respawn Count×2（石像狮子那条随后被删除）

## 5) 全图删除「石像狮子」刷新
- Monster#10111 石像狮子
- 删除 20 条 Respawn（真天宫/黑度宫等）

## 产物
- Library.dll → D:\newMir3\Library.dll（ServerLibrary Release）
- System.db / ClientSystem.db 已备份: Database\Backup_five_20260909_165522
- 热更目录: D:\Mir3热更补丁\PC_7091_overwrite_latest（ClientSystem）

## VPS 步骤
1. git pull newMir3（Library.dll + Database System/ClientSystem）
2. 确认 Server.ini: ShopNonRefinable=False
3. 覆盖 Database\System.db（Respawn/Magic/Item）— 勿动 Users.db
4. 重启服务端
5. 客户端热更拉取 PC_7091（ClientSystem.db）

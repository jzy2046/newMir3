# 护身符商店购买数量 2026-09-09

## 结论
本引擎 **NPC 商店购买上限 = ItemInfo.StackSize**，没有单独的 GoodsInfo.Count / NPCGood.Quantity 字段。

| 位置 | 说明 |
|------|------|
| ItemInfo.StackSize | 客户端买量框 MaxValue；服务端 NPCBuy 校验 Amount<=StackSize |
| NPCGood | 仅有 Item/Rate/Cost，无 Count |
| StoreInfo | 商城；护身符不在商城 |
| Scripts 商店列表 zahuodiangoodslist | 仅 (品名, Rate) |

## 已改行（Eight 012a043，本轮核实）
表: ItemInfo（System.db + ClientSystem.db）
条件: ItemType=Amulet，26 行 StackSize=1000

## 本轮动作
- newMir3 库无需再改（已是 1000）
- 同步 mir3z 服务端 Database（此前 Stack 仍为 100）
- 重写热更 Data-ClientSystem.db.gz；未动 PList.Bin（并行重生中）

## Commits
- 012a043 Eight: amulet StackSize=1000（即商店购买上限）

## VPS
1. git pull newMir3
2. 重启游戏服
3. 客户端热更 Data-ClientSystem.db.gz
4. 等新 PList.Bin 合并后再发完整包（旧 PList 可能导致不拉新 ClientSystem）

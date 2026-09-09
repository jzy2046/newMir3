# 僵尸书掉落排查报告 (2026-09-09 23:20 CST)

## 用户问题
僵尸为什么完全不出书？是否相关掉率被删？怀疑 f9b21a3 对 Chance/=2 时奇数/1 整除成 0，导致 `Random.Next(Chance)==0` 失效。

## 结论（先说）
**不是 Chance=0，也不是 DropInfo 被删。**
本地 `Database/System.db` / `Data/System.db`（及已推送的 f9b21a3）中，僵尸/尸王相关 Book 掉落 **222 行全部存在且 Chance≥100**，`chance0=0`，`chance_lt1=0`。
矿洞书掉率翻倍变更使用了 `Math.Max(1, oldChance/2)`，**不会**把 Chance 写成 0。

## 1) 当前 DropInfo 查询证据

探针：`tools/Mir3ZombieBookProbe`（MirDB Session 打开 System.db）

| 指标 | 当前 WT / HEAD(f9b21a3) | Backup_minebook_20260909_215520（变更前） |
|------|-------------------------|-------------------------------------------|
| total DropInfo | 5623 | 5623 |
| 僵尸/尸王 Book 行 | **222** | **222** |
| Chance=0 / <1 | **0 / 0** | **0 / 0** |
| 典型 Chance | 250(x77), 300(x40), 400(x29)… | 500(x77), 600(x40), 800(x29)…（恰为 2 倍） |

按怪统计（当前）：
- 老道僵尸 / 僧侣僵尸 / 僵尸2/3/4：各 31 本，ChanceMin=250
- 尸王：18 本，ChanceMin=100
- 尸王0：18 本，ChanceMin=200
- 雷电僵尸：31 本，ChanceMin=1000
- **僵尸鬼 (Mon#20012)：0 本（变更前也是 0）**
- **僧侣僵尸0 (Mon#100004)：0 本（变更前也是 0）**

样例：`Drop#766 老道僵尸/火球术 Chance=250`（备份为 500）；`Drop#4567 尸王/烈火剑法 Chance=200`（备份为 400）。DropSet 均为 0。

## 2) 与 Backup_minebook_* 对比
- 备份目录：`Database/Backup_minebook_20260909_215520`（apply 开始时拷贝，= 变更前）
- **行数未删**：222→222，总 DropInfo 5623→5623
- **Chance 精确减半**：500→250、600→300、800→400、2000→1000…（apply 日志 222 次 SET，无 `-> 0`）

## 3) Chance=0 修复？
**无需修复。** apply 代码（`tools/Mir3MineBook20260909/Program.cs`）：
```csharp
if (oldChance <= 1) { SKIP; continue; }
int neu = Math.Max(1, oldChance / 2);
```
无 Chance=0 行可修。

## 4) 是否整行删除？
**否。** 变更前后 book_rows 与 total_drops 一致。仅有两只怪本身从未配置书：僵尸鬼、僧侣僵尸0（与 minebook 无关）。

## 5) 交付 / VPS
- Git：`f9b21a3` 已在 `origin/main`（`Double book drops in Bichon/Snake mines...`）
- 含 `Database/System.db` + `ClientSystem.db` + `Data/` 同步 + 文档
- **无需新热更包**：掉落读服务端 System.db；ClientSystem 仅影响客户端掉率查询显示，f9b21a3 已带
- **VPS（勿由本机 SSH 登录；运维自行操作）**：
  1. `git pull` newMir3
  2. 勿覆盖 Users.db；保留 Server.ini listen
  3. **重启服务端** 使 System.db 生效
  4. 若客户端掉率面板仍显示旧值，再覆盖 PC 热更里的 ClientSystem（可选）

## 若玩家仍体感「完全不出」
1. 确认打的是有书的怪（老道/僧侣/僵尸2-4/尸王/雷电），不是 **僵尸鬼 / 僧侣僵尸0**
2. 普通书约 1/250～1/600，尸王较好约 1/100～1/250；未重启服务端则仍跑旧库
3. 如需给僵尸鬼/僧侣僵尸0 补书，需另开任务从同系怪克隆 DropInfo（本次未改）
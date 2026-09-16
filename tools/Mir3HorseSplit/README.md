# Horse attribute split (绝影/绝影战马 + 给亲友的红马/给宝贝的马)

## Root cause
`RefreshStats()` maps `HorseType` → `MonsterFlag` → **first** `MonsterInfo` with that flag.
Someone added `#100035` (绝影战马, BlackHorse) and `#100034` (给亲友的红马, RedHorse) with
lower Index than the classic `#100138`/`#100137`, so `FirstOrDefault` made **every**
`HorseType.Black` / `HorseType.Red` share those gift stats.

## Engine support (no new enum needed)
Live `Library.dll` already has `HorseType.DiyHorse1`–`DiyHorse40` and matching
`MonsterFlag.DiyHorseN`, fully wired in server `RefreshStats`.

## Mapping after fix
| Mount | HorseType | MonsterInfo | Flag |
|------|-----------|-------------|------|
| 绝影 (马厩/马牌) | Black | #100138 (named 赤兔马 historically; stats 1600/8-8) | BlackHorse |
| 绝影战马 (礼包 Shape68) | DiyHorse1 | #100035 | DiyHorse1 |
| 给亲友的红马 / 赤兔(推广 Shape67) | Red | #100034 | RedHorse |
| 给宝贝的马 (礼包 Shape69) | DiyHorse2 | #120369 | DiyHorse2 |

## Client appearance
`HorseFrame = DrawFrame + (int)(Horse-1)*5000` — DiyHorse1/2 would use wrong banks.
Patch client `PlayerObject.HorseFrame` so DiyHorse1→Black bank, DiyHorse2→Red bank.
See `patch_HorseFrame.cs.txt`. Requires Mir3Source client rebuild + hotupdate **Mir3.exe**
(NOT Server.exe). Library.dll / Server.exe need **not** change for this fix.

## VPS deploy
1. Pull newMir3
2. Cover Scripts + Database System.db (+ ClientSystem if clients need item Shape69)
3. Hotupdate ClientSystem.db for Shape69 item
4. After client patch build: hotupdate Mir3.exe / Mir3Game.exe
5. Restart server process (authorized Server.exe unchanged)

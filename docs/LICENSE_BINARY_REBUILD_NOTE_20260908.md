# CRITICAL: Never redeploy rebuilt Server.exe / Library.dll

## Rule
Mir3 `Server.exe` and `Library.dll` are **license-bound**. Recompiling from source and overwriting the authorized binaries causes startup failure: **授权无效**.

- Do **not** commit or deploy a freshly built `Server.exe` / `Library.dll` unless the license/auth process has been re-applied to that exact build.
- Prefer changes via `Server.ini`, `Database/*.db`, `Scripts/`, and client packs.
- Keep known-good authorized binaries; treat them as sealed artifacts.

## Incident (2026-09-08 / fefd37a batch2)
Batch2 rebuilt `Server.exe` (82562560 -> 82732032) and `Library.dll` (2157056 -> 2166272) for 万年雪霜×1000 and accessory code paths. That broke license checks. Config/DB alone would not show 授权无效.

## Fix commit
Restored authorized binaries from pre-fefd37a (`537f97e`) / `*.bak_batch2_20260908_182844`:

| File | Good size | Good SHA256 |
|------|----------:|-------------|
| Server.exe | 82562560 | AF5FD06E67379504804CF395A9F51403D1FA6D2D4EAD16A35882830BC86F180F |
| Library.dll | 2157056 | 4708146BABDFE9BE51E2C27D949A46741108E71AE44AACB635FE3D4C509BD0E5 |
| deploy_to_Mir3service/optional_bin/Library.dll | same as Library.dll | same |

## Kept without new server binaries
- `Server.ini`: `ShowSafeZone=False`; `Common/Superior/EliteItemSuccessRate=40` (AccessoryCombine base 40%)
- DB (`System.db` / `ClientSystem.db`): 结晶石 Effect=Crystal; 石榴石 Effect=Crystal; 天之怒火 desc cleared
- Client tip / J+U keybind disable (client-side only)

## Feature status after restore
| Feature | Status |
|---------|--------|
| ShowSafeZone off | OK (`Server.ini`) |
| AccessoryCombine 40% | OK (`Server.ini` ItemSuccessRate keys; licensed binary reads them) |
| 结晶石 +10% | OK expected (`ItemEffect.Crystal` already in licensed Library.dll + DB) |
| 万年雪霜 mall ×1000 | **BLOCKED** without re-licensed Server rebuild (`MarketPlaceStoreBuy` count*=1000). Prefer bootable server. Source patch may still exist under D:\mir3src — do not deploy that rebuild. |

## VPS / Mir3service restart
1. `git pull origin main` on the host that runs the server (path may be Mir3service or newMir3 deploy).
2. Confirm `Server.exe` size **82562560** and `Library.dll` size **2157056**. If you see 82732032 / 2166272, those are the broken rebuild — replace from this commit.
3. Keep batch2 `Server.ini` + Database files; do **not** roll those back.
4. Do **not** copy any rebuilt Server.exe/Library.dll from `tools/.../server_build` or local Debug output.
5. Restart `Server.exe`; confirm no 授权无效.

## Local junk (do not commit)
- `Server.exe.broken_batch2_fefd37a`, `Library.dll.broken_batch2_fefd37a` — quarantine of bad rebuild
- `*.bak_batch2_20260908_182844` — known-good copies used for restore

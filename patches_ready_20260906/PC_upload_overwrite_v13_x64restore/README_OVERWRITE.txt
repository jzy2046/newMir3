PC 20260909 x64restore pack v13 stamp=20260909_003825
ROOT CAUSE FIX: v11/v12 tip rebuild Mir3.exe/Mir3Game.exe were x86 (3929600) while client d3dx9_43.dll is x64 -> System.BadImageFormatException at D3DXCreateSprite on startup (no window).
Restored x64 Mir3 from PC_upload_overwrite_v9 (4130304) KEEP v12 ClientSystem.db.
NEVER overwrite Server.exe/Library.dll
Mir3.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da
Mir3Game.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da
ClientSystem.db size=8421136 md5=9a6a678a93a4fa14df1f8886472160de

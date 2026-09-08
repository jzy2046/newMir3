PC 20260909 x64+comfort pack v14
ROOT CAUSE (client won't open): v11/v12 Mir3.exe/Mir3Game.exe were x86 (size 3929600) while d3dx9_43.dll is x64 -> System.BadImageFormatException at D3DXCreateSprite.
THIS PACK: x64 Mir3.exe + Mir3Game.exe (size 4130304, same as v9/v13) + latest ClientSystem.db with boots Comfort correct.

Comfort is ItemInfoStat.Stat=Comfort (ItemInfo has NO Comfort column). Tip reads ItemInfoStat.
草鞋 Comfort+1; 皮靴+2; 五彩鞋+3; 赤飞靴子+4; 天掌靴子+5; 黑皮/绝地/月光/仙云/无影/武神 +7
WearWeight=穿戴负重; HandWeight=腕力; BagWeight/AC/MR cleared.

USE THIS PACK ONLY for 7091 flat overwrite. Do NOT use v11/v12 (x86 tip breaks open).
NEVER overwrite Server.exe / Library.dll.

Mir3.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da
Mir3Game.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da
ClientSystem.db size=8421136 md5=9a6a678a93a4fa14df1f8886472160de

Flat files:
  PList.Bin
  Mir3.exe.gz
  Mir3Game.exe.gz
  Data-ClientSystem.db.gz

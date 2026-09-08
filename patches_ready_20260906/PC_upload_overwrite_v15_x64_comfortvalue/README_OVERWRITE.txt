PC 20260909 x64+ComfortValue pack v15 stamp=20260909_014003
ROOT CAUSE (open fail): v11/v12 Mir3.exe were x86 (3929600) vs x64 d3dx9_43.dll -> BadImageFormatException.
This pack: x64 Mir3.exe/Mir3Game.exe (4130304 from v9/v13) + ClientSystem with boots Comfort ItemInfoStat correct.
ROOT CAUSE: Diy Mir3.dat ComfortValue=True tip /10 rounds 7->+1. FIX ComfortValue=False; ItemInfoStat stays 1/2/3/4/5/7.
WearWeight=wear-burden HandWeight=wrist; BagWeight/AC/MR cleared on boots.
USE for 7091 overwrite. x64 ONLY 4130304. NEVER x86. Includes Data-Diy-Mir3.dat.gz. NEVER Server.exe.
Mir3.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da
Mir3Game.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da
ClientSystem.db size=8421136 md5=9a6a678a93a4fa14df1f8886472160de
Diy Mir3.dat size=546 md5=5360f4c83e009d09a7d57519b8767b8d gz=237
Flat: PList.Bin + Mir3.exe.gz + Mir3Game.exe.gz + Data-ClientSystem.db.gz + Data-Diy-Mir3.dat.gz
  PList.Bin                 117813
  Mir3.exe.gz               2161137
  Mir3Game.exe.gz           2161141
  Data-ClientSystem.db.gz   8423745
  Data-Diy-Mir3.dat.gz      237

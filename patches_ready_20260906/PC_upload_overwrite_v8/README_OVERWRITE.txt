PC 20260908 batch2 LEFT pack v8 stamp=20260908_183007
Mir3.exe size=4130304 md5=a346c5a32c23bdcaaa59f792c6a577da IsEquipmentItemType=True
ClientSystem.db size=8418832 md5=ed191709f1eca8942931bc065b4aedd4 sha16=A5C82E75A571DCE9
PList.Bin size=117813 entries=2669
Includes: tip non-equip divider + J/U disable + ClientSystem (天之怒火 desc clear, 结晶石/石榴石 Crystal, 万年雪霜 store)
Server-side (NOT in this zip; deploy on 7091 separately): Server.ini ShowSafeZone=False + success rates 40%; Server.exe/Library.dll AccessoryCombine +10% crystal & 万年雪霜 x1000 buy
Overwrite these 4 files on VPS 7091 directory:
  PList.Bin                 117813
  Mir3.exe.gz               2161137
  Mir3Game.exe.gz           2161141
  Data-ClientSystem.db.gz   8421441
Host: http://43.226.60.100:7091/

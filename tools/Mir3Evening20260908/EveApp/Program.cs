using System.Collections;
using System.Drawing;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: EveApp <dry-run|apply>");
    return 1;
}
var doApply = args[0] == "apply";
var root = @"D:\newMir3";
var deps = Path.Combine(root, "tools", "_deps");
AssemblyLoadContext.Default.Resolving += (_, a) =>
{
    foreach (var d in new[] { deps, root })
    {
        var path = Path.Combine(d, (a.Name ?? "") + ".dll");
        if (File.Exists(path)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(path);
    }
    return null;
};

var lib = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root, "Library.dll"));
var sessionType = lib.GetType("MirDB.Session")!;
var modeType = lib.GetType("MirDB.SessionMode")!;
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
string Slash(string x) => Path.EndsInDirectorySeparator(x) ? x : x + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void Set(object o, string n, object? val) => o.GetType().GetProperty(n)!.SetValue(o, val);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

object? ses = null;
MethodInfo? FindCreate(Type t)
{
    var col = get.MakeGenericMethod(t).Invoke(ses!, null)!;
    return col.GetType().GetMethods().FirstOrDefault(mi => mi.Name == "CreateNewObject" && mi.GetParameters().Length == 0);
}

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_eve20260908_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-eve-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var iisType = lib.GetType("Library.SystemModels.ItemInfoStat")!;
var monType = lib.GetType("Library.SystemModels.MonsterInfo")!;
var misType = lib.GetType("Library.SystemModels.MonsterInfoStat")!;
var dropType = lib.GetType("Library.SystemModels.DropInfo")!;
var storeType = lib.GetType("Library.SystemModels.StoreInfo")!;
var npcType = lib.GetType("Library.SystemModels.NPCInfo")!;
var mapType = lib.GetType("Library.SystemModels.MapInfo")!;
var regionType = lib.GetType("Library.SystemModels.MapRegion")!;
var respawnType = lib.GetType("Library.SystemModels.RespawnInfo")!;
var craftType = lib.GetType("Library.SystemModels.CraftItemInfo")!;
var rarType = lib.GetType("Library.Rarity")!;
var itemTypeEnum = lib.GetType("Library.ItemType")!;
var statType = lib.GetType("Library.Stat")!;

var items = ListOf(ses, itemType);
var istats = ListOf(ses, iisType);
var mons = ListOf(ses, monType);
var mstats = ListOf(ses, misType);
var drops = ListOf(ses, dropType);
var stores = ListOf(ses, storeType);
var npcs = ListOf(ses, npcType);
var maps = ListOf(ses, mapType);
var respawns = ListOf(ses, respawnType);
var crafts = ListOf(ses, craftType);

int changes = 0;
object StatVal(string name) => Enum.Parse(statType, name);
object RarityVal(string name) => Enum.Parse(rarType, name);
object ItemTypeVal(string name) => Enum.Parse(itemTypeEnum, name);
object? FindItem(string name) => items.FirstOrDefault(i => S(i, "ItemName") == name);
object? FindMon(string name) => mons.FirstOrDefault(m => S(m, "MonsterName") == name);

void DeleteDbObj(object st)
{
    var del = st.GetType().GetMethod("Delete", Type.EmptyTypes);
    if (del != null) del.Invoke(st, null);
    else
    {
        try { Set(st, "IsTemporary", true); } catch { }
        try { Set(st, "Amount", 0); } catch { }
    }
}

object? EnsureStat(object item, string statName, int amount)
{
    var existing = istats.FirstOrDefault(st => ReferenceEquals(P(st, "Item"), item) && S(st, "Stat") == statName);
    if (existing != null)
    {
        var old = Iv(existing, "Amount");
        if (old != amount)
        {
            L($"STATSET {S(item,"ItemName")} {statName} {old}->{amount}");
            if (doApply) { Set(existing, "Amount", amount); changes++; }
        }
        else L($"STATOK {S(item,"ItemName")} {statName}={amount}");
        return existing;
    }
    L($"STATADD {S(item,"ItemName")} {statName}={amount}");
    if (!doApply) return null;
    var create = FindCreate(iisType)!;
    var col = get.MakeGenericMethod(iisType).Invoke(ses, null)!;
    var stNew = create.Invoke(col, null)!;
    Set(stNew, "Item", item);
    Set(stNew, "Stat", StatVal(statName));
    Set(stNew, "Amount", amount);
    istats.Add(stNew);
    changes++;
    return stNew;
}
void RemoveStat(object item, string statName)
{
    foreach (var st in istats.Where(st => ReferenceEquals(P(st, "Item"), item) && S(st, "Stat") == statName).ToList())
    {
        L($"STATDEL {S(item,"ItemName")} {statName}={Iv(st,"Amount")} idx={Iv(st,"Index")}");
        if (doApply) { DeleteDbObj(st); changes++; }
    }
}
void SetMonStat(object mon, string statName, int amount)
{
    var existing = mstats.FirstOrDefault(st => ReferenceEquals(P(st, "Monster"), mon) && S(st, "Stat") == statName);
    if (existing != null)
    {
        var old = Iv(existing, "Amount");
        if (old != amount)
        {
            L($"MSTATSET {S(mon,"MonsterName")} {statName} {old}->{amount}");
            if (doApply) { Set(existing, "Amount", amount); changes++; }
        }
        else L($"MSTATOK {S(mon,"MonsterName")} {statName}={amount}");
        return;
    }
    L($"MSTATADD {S(mon,"MonsterName")} {statName}={amount}");
    if (!doApply) return;
    var create = FindCreate(misType)!;
    var col = get.MakeGenericMethod(misType).Invoke(ses, null)!;
    var stNew = create.Invoke(col, null)!;
    Set(stNew, "Monster", mon);
    Set(stNew, "Stat", StatVal(statName));
    Set(stNew, "Amount", amount);
    mstats.Add(stNew);
    changes++;
}
void HalveMonStat(object mon, string statName)
{
    var existing = mstats.FirstOrDefault(st => ReferenceEquals(P(st, "Monster"), mon) && S(st, "Stat") == statName);
    if (existing == null) { L($"MSTAT_HALF_MISS {S(mon,"MonsterName")} {statName}"); return; }
    var old = Iv(existing, "Amount");
    var neu = old / 2;
    L($"MSTAT_HALF {S(mon,"MonsterName")} {statName} {old}->{neu}");
    if (doApply && old != neu) { Set(existing, "Amount", neu); changes++; }
}
void EnsureDrop(object mon, object item, int chance, int amount = 1)
{
    var existing = drops.FirstOrDefault(d => ReferenceEquals(P(d, "Monster"), mon) && ReferenceEquals(P(d, "Item"), item));
    if (existing != null)
    {
        var oldC = Iv(existing, "Chance");
        L($"DROPSET mon={S(mon,"MonsterName")} item={S(item,"ItemName")} Chance {oldC}->{chance}");
        if (doApply) { Set(existing, "Chance", chance); Set(existing, "Amount", amount); changes++; }
        return;
    }
    L($"DROPADD mon={S(mon,"MonsterName")} item={S(item,"ItemName")} Chance={chance}");
    if (!doApply) return;
    var create = FindCreate(dropType)!;
    var col = get.MakeGenericMethod(dropType).Invoke(ses, null)!;
    var d = create.Invoke(col, null)!;
    Set(d, "Monster", mon);
    Set(d, "Item", item);
    Set(d, "Chance", chance);
    Set(d, "Amount", amount);
    drops.Add(d);
    changes++;
}

// 1 Respawn
var multMaps = new Dictionary<string, int> {
    {"潘夜神殿3层-西部", 3}, {"潘夜神殿3层-东部", 2}, {"黑度宫2层", 3}, {"祖玛神殿5层", 3},
};
foreach (var r in respawns)
{
    var region = P(r, "Region");
    var map = region != null ? P(region, "Map") : null;
    var mdesc = S(map, "Description");
    if (!multMaps.TryGetValue(mdesc, out var mul)) continue;
    var old = Iv(r, "Count");
    var neu = checked(old * mul);
    L($"RESPAWN {mdesc} mon={S(P(r,"Monster"),"MonsterName")} Count {old}*{mul}={neu} idx={Iv(r,"Index")}");
    if (doApply) { Set(r, "Count", neu); changes++; }
}

// 2 Move NPC
var buyback = npcs.FirstOrDefault(n => Iv(n, "Index") == 333) ?? npcs.FirstOrDefault(n => S(n, "NPCName") == "装备回购");
var snowMap = maps.First(m => S(m, "Description") == "雪原村落");
if (buyback != null)
{
    var reg = P(buyback, "Region")!;
    var pts = P(reg, "PointRegion") as Point[];
    L($"NPC_BUYBACK before map={S(P(reg,"Map"),"Description")} pts={(pts==null?"":string.Join(";", pts.Select(p=>$"{p.X},{p.Y}")))}");
    if (doApply)
    {
        Set(reg, "Map", snowMap);
        Set(reg, "PointRegion", new[] { new Point(198, 115) });
        Set(reg, "Size", 1);
        Set(reg, "Description", "装备回购");
        changes++;
        L("MOVED 装备回购 -> 雪原村落 198,115");
    }
}
else L("NPC_BUYBACK MISS");

// 3 Boots
void BootSet(string name, int maxAc, int maxMr, int agility, int hand, int wear)
{
    var it = FindItem(name);
    if (it == null) { L("BOOT_MISS " + name); return; }
    EnsureStat(it, "MinAC", 0); EnsureStat(it, "MaxAC", maxAc);
    EnsureStat(it, "MinMR", 0); EnsureStat(it, "MaxMR", maxMr);
    EnsureStat(it, "Agility", agility);
    EnsureStat(it, "HandWeight", hand); EnsureStat(it, "WearWeight", wear);
}
BootSet("草鞋", 1, 1, 1, 2, 2);
BootSet("皮靴", 2, 2, 2, 3, 3);
BootSet("五彩鞋", 3, 2, 3, 4, 4);
BootSet("赤飞靴子", 4, 3, 4, 5, 5);
BootSet("黑皮靴子", 7, 7, 7, 10, 10);
BootSet("绝地靴", 7, 14, 3, 12, 12);
BootSet("月光鞋", 7, 3, 14, 12, 12);
BootSet("仙云靴", 7, 20, 0, 13, 13);
BootSet("无影靴", 7, 0, 20, 15, 15);
BootSet("武神之靴", 7, 11, 11, 15, 15);
L("BOOT_SOURCES https://mir3.17173.com/item/item10.htm ; http://games.sina.com.cn/z/mir3/2003-10-17/56185.shtml");

// 5 影魅
var ying = FindItem("影魅之刃");
if (ying != null)
{
    var minMc = istats.FirstOrDefault(st => ReferenceEquals(P(st,"Item"), ying) && S(st,"Stat")=="MinMC");
    var maxMc = istats.FirstOrDefault(st => ReferenceEquals(P(st,"Item"), ying) && S(st,"Stat")=="MaxMC");
    EnsureStat(ying, "MinSC", minMc != null ? Iv(minMc, "Amount") : 10);
    EnsureStat(ying, "MaxSC", maxMc != null ? Iv(maxMc, "Amount") : 20);
    EnsureStat(ying, "AttackSpeed", 2);
}

// 6 armor
foreach (var nm in new[] { "天赐战甲（男）", "天赐战甲（女）" })
{
    var it = FindItem(nm);
    if (it == null) { L("ARMOR_MISS " + nm); continue; }
    RemoveStat(it, "HealthPercent");
}

// 7 craft
var craft = crafts.FirstOrDefault(c => S(P(c, "Item"), "ItemName") == "影魅之刃");
if (craft != null)
{
    var poshan = FindItem("破山剑");
    var tianshen = FindItem("天神法杖");
    var tairun = FindItem("泰轮拂尘") ?? FindItem("泰伦拂尘");
    L($"CRAFT mats poshan={poshan!=null} tianshen={tianshen!=null} tairun={S(tairun,"ItemName")}");
    var i1 = P(craft, "Item1");
    if (poshan != null && (i1 == null || string.IsNullOrEmpty(S(i1, "ItemName"))))
    {
        L("CRAFTSET Item1=破山剑");
        if (doApply) { Set(craft, "Item1", poshan); Set(craft, "Amount1", 1); changes++; }
    }
    L("CRAFT_NOTE Item2-5 occupied; 天神法杖/泰轮拂尘 need extra craft slots -> PARTIAL");
}

// 8 hero gloves
var hero = FindItem("英雄手套");
if (hero != null)
{
    EnsureStat(hero, "MinAC", 0); EnsureStat(hero, "MaxAC", 5);
    EnsureStat(hero, "MinMR", 0); EnsureStat(hero, "MaxMR", 5);
    RemoveStat(hero, "HPRegenRate"); RemoveStat(hero, "RenounceHPLost");
}
// 9 铁炼腕
var tiel = FindItem("铁炼腕");
if (tiel != null)
{
    EnsureStat(tiel, "MinAC", 0); EnsureStat(tiel, "MaxAC", 4);
    EnsureStat(tiel, "MinMR", 0); EnsureStat(tiel, "MaxMR", 4);
    RemoveStat(tiel, "HPRegenRate");
}

// 14 HP
var hpTargets = new Dictionary<string, int> {
    {"潘夜鬼将",2500},{"潘夜牛魔王",15000},{"半兽勇士",500},{"骷髅精灵",500},{"骨鬼将",2500},
    {"骷髅教主",12000},{"八脚首领",2500},{"护法天",2500},{"祖玛教主",15000},{"触龙神",12000},
    {"邪恶钳虫",2500},{"沃玛卫士",2500},{"沃玛教主",12000},{"邪恶毒蛇",2500},{"白野猪",1500},
    {"超级黑野猪",12000},{"神鬼王",2500},{"赤月恶魔",15000},{"霸王守卫",2500},{"霸王教主",18000},
    {"震天首将",3000},{"黑度首将",3000},{"震天魔神",15000},{"疯狂魔神盗",2500},{"大法老",2500},
    {"诺玛突击队长",5000},{"诺玛教主",25000},
};
foreach (var kv in hpTargets)
{
    var mon = FindMon(kv.Key);
    if (mon == null) { L("MON_MISS " + kv.Key); continue; }
    SetMonStat(mon, "Health", kv.Value);
}
foreach (var nm in new[] { "沃玛教主","祖玛教主","触龙神","超级黑野猪","赤月恶魔","霸王教主","震天魔神","诺玛教主","骷髅教主" })
{
    var mon = FindMon(nm);
    if (mon == null) { L("DMG_MISS " + nm); continue; }
    foreach (var stn in new[] { "MinDC","MaxDC","MinMC","MaxMC","MinSC","MaxSC" })
        HalveMonStat(mon, stn);
}

// 11 mall
var curse = FindItem("诅咒之药水");
if (curse != null)
{
    var st = stores.FirstOrDefault(s => ReferenceEquals(P(s, "Item"), curse));
    if (st != null)
    {
        L($"STORESET 诅咒之药水 Price {S(st,"Price")}->10");
        if (doApply) { Set(st, "Price", 10); Set(st, "Available", true); try { Set(st, "Filter", ""); } catch {} changes++; }
    }
    else if (doApply)
    {
        L("STOREADD 诅咒之药水 Price=10");
        var create = FindCreate(storeType)!;
        var col = get.MakeGenericMethod(storeType).Invoke(ses, null)!;
        var neu = create.Invoke(col, null)!;
        Set(neu, "Item", curse); Set(neu, "Price", 10); Set(neu, "HuntGoldPrice", 0); Set(neu, "Available", true);
        try { Set(neu, "Filter", ""); } catch {}
        stores.Add(neu); changes++;
    }
    else L("STOREADD(dry) 诅咒之药水");
}

// 15 ring
object? quan = FindItem("全能指环");
if (quan == null && doApply)
{
    L("CREATE 全能指环");
    var create = FindCreate(itemType)!;
    var col = get.MakeGenericMethod(itemType).Invoke(ses, null)!;
    quan = create.Invoke(col, null)!;
    var refRing = FindItem("指环") ?? items.First(i => S(i,"ItemType")=="Ring");
    Set(quan, "ItemName", "全能指环");
    Set(quan, "ItemType", ItemTypeVal("Ring"));
    Set(quan, "Rarity", RarityVal("Elite"));
    Set(quan, "Image", Iv(refRing, "Image"));
    Set(quan, "Shape", Iv(refRing, "Shape"));
    Set(quan, "Weight", 1); Set(quan, "Durability", 5000); Set(quan, "Price", 30000);
    items.Add(quan); changes++;
}
quan = FindItem("全能指环") ?? quan;
if (quan != null)
{
    EnsureStat(quan, "MinMR", 1); EnsureStat(quan, "MaxMR", 5);
    EnsureStat(quan, "MinMC", 2); EnsureStat(quan, "MaxMC", 3);
    EnsureStat(quan, "MinSC", 2); EnsureStat(quan, "MaxSC", 3);
    EnsureStat(quan, "MinDC", 2); EnsureStat(quan, "MaxDC", 3);
    var zuma = FindMon("祖玛教主"); var chiyue = FindMon("赤月恶魔");
    if (zuma != null) EnsureDrop(zuma, quan, 1000);
    if (chiyue != null) EnsureDrop(chiyue, quan, 1000);
}
else if (!doApply) L("CREATE(dry) 全能指环");

// 16 shoes
object? tianzhang = FindItem("天掌靴子");
if (tianzhang == null && doApply)
{
    L("CREATE 天掌靴子");
    var create = FindCreate(itemType)!;
    var col = get.MakeGenericMethod(itemType).Invoke(ses, null)!;
    tianzhang = create.Invoke(col, null)!;
    var chifei = FindItem("赤飞靴子")!;
    Set(tianzhang, "ItemName", "天掌靴子");
    Set(tianzhang, "ItemType", ItemTypeVal("Shoes"));
    Set(tianzhang, "Rarity", RarityVal("Common"));
    Set(tianzhang, "Image", 1362);
    Set(tianzhang, "Shape", Iv(chifei, "Shape"));
    Set(tianzhang, "Weight", 10); Set(tianzhang, "Durability", 2000);
    Set(tianzhang, "RequiredAmount", 38); Set(tianzhang, "Price", 20000);
    items.Add(tianzhang); changes++;
}
tianzhang = FindItem("天掌靴子") ?? tianzhang;
if (tianzhang != null)
{
    EnsureStat(tianzhang, "MinAC", 0); EnsureStat(tianzhang, "MaxAC", 5);
    EnsureStat(tianzhang, "MinMR", 0); EnsureStat(tianzhang, "MaxMR", 4);
    EnsureStat(tianzhang, "Agility", 5);
    EnsureStat(tianzhang, "HandWeight", 4); EnsureStat(tianzhang, "WearWeight", 4);
    var zt = FindMon("震天首将"); var hd = FindMon("黑度首将");
    if (zt != null) EnsureDrop(zt, tianzhang, 100);
    if (hd != null) EnsureDrop(hd, tianzhang, 100);
}
else if (!doApply) L("CREATE(dry) 天掌靴子");

// 17 helmets
object? xingyun = FindItem("幸运霸龙头盔");
var balong = FindItem("霸龙头盔");
var zhufuBalong = FindItem("祝福霸龙头盔");
if (xingyun == null && doApply)
{
    L("CREATE 幸运霸龙头盔");
    var create = FindCreate(itemType)!;
    var col = get.MakeGenericMethod(itemType).Invoke(ses, null)!;
    xingyun = create.Invoke(col, null)!;
    var src = zhufuBalong ?? balong!;
    Set(xingyun, "ItemName", "幸运霸龙头盔");
    Set(xingyun, "ItemType", ItemTypeVal("Helmet"));
    Set(xingyun, "Rarity", RarityVal("Superior"));
    Set(xingyun, "Image", Iv(balong ?? src, "Image"));
    Set(xingyun, "Shape", Iv(balong ?? src, "Shape"));
    Set(xingyun, "Weight", Iv(src, "Weight"));
    Set(xingyun, "Durability", Iv(src, "Durability"));
    Set(xingyun, "Price", Iv(src, "Price"));
    items.Add(xingyun); changes++;
}
xingyun = FindItem("幸运霸龙头盔") ?? xingyun;
if (xingyun != null)
{
    EnsureStat(xingyun, "MinAC", 2); EnsureStat(xingyun, "MaxAC", 6);
    EnsureStat(xingyun, "MinMR", 1); EnsureStat(xingyun, "MaxMR", 2);
}
var zhufuDao = FindItem("祝福道士头盔");
if (zhufuDao != null)
{
    EnsureStat(zhufuDao, "MinAC", 1); EnsureStat(zhufuDao, "MaxAC", 2);
    EnsureStat(zhufuDao, "MinMR", 2); EnsureStat(zhufuDao, "MaxMR", 6);
}
var hufa = FindMon("护法天");
if (hufa != null)
{
    if (xingyun != null) EnsureDrop(hufa, xingyun, 100);
    if (zhufuDao != null) EnsureDrop(hufa, zhufuDao, 100);
}

// 19 bracelets
foreach (var nm in new[] { "如来手镯", "火玉手镯", "毁灭手镯" })
{
    var it = FindItem(nm);
    if (it == null) { L("BRACE_MISS " + nm); continue; }
    L($"BRACE desc [{S(it,"Description")}]");
    if (doApply) { Set(it, "Description", ""); changes++; L("BRACE cleared " + nm); }
}

// 20 relic
var relic = FindItem("遗物");
foreach (var nm in new[] { "诺玛骑兵", "诺玛司令", "诺玛抛石兵", "诺玛斧兵", "诺玛装甲兵" })
{
    var mon = FindMon(nm);
    if (mon == null || relic == null) { L($"RELIC_MISS {nm}"); continue; }
    EnsureDrop(mon, relic, 1);
}

if (doApply)
{
    var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
    save.Invoke(ses, new object[] { true, tool });
}
(ses as IDisposable)?.Dispose();

if (doApply)
{
    File.Copy(Path.Combine(work, "System.db"), sysDb, true);
    File.Copy(Path.Combine(work, "ClientSystem.db"), cliDb, true);
    void Sync(string dir, string label)
    {
        if (!Directory.Exists(dir)) { L(label + " MISSING"); return; }
        File.Copy(sysDb, Path.Combine(dir, "System.db"), true);
        var c = Path.Combine(dir, "ClientSystem.db");
        if (File.Exists(c)) File.Copy(cliDb, c, true);
        L("synced " + label + "=" + dir);
    }
    Sync(Path.Combine(root, "Data"), "Data");
    Sync(Path.Combine(root, "deploy_to_Mir3service", "Database"), "deploy_to_Mir3service/Database");
}
Directory.CreateDirectory(Path.Combine(root, "tools", "Mir3Evening20260908"));
File.WriteAllText(Path.Combine(root, "tools", "Mir3Evening20260908", "apply_" + stamp + ".txt"), report.ToString(), new UTF8Encoding(true));
L($"DONE changes={changes}");
return 0;

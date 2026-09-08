using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3Wave4 <dry-run|apply>");
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
bool Bv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v != null && Convert.ToBoolean(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void Set(object o, string n, object? val) => o.GetType().GetProperty(n)!.SetValue(o, val);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();
MethodInfo? FindCreate(Type t)
{
    var colType = get.MakeGenericMethod(t).ReturnType;
    return colType.GetMethods().FirstOrDefault(m => m.Name == "CreateNewObject" && m.GetParameters().Length == 0);
}

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
void L(string s) { Console.WriteLine(s); }

L($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_wave4_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-w4-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var magicType = lib.GetType("Library.SystemModels.MagicInfo")!;
var storeType = lib.GetType("Library.SystemModels.StoreInfo")!;
var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var statType = lib.GetType("Library.SystemModels.ItemInfoStat")!;
var monType = lib.GetType("Library.SystemModels.MonsterInfo")!;
var statEnum = lib.GetTypes().First(t => t.Name == "Stat" && t.IsEnum);

var magics = ListOf(ses, magicType);
var stores = ListOf(ses, storeType);
var items = ListOf(ses, itemType);
var stats = ListOf(ses, statType);
var mons = ListOf(ses, monType);

object? FindItem(string name) => items.FirstOrDefault(x => S(x, "ItemName") == name || S(x, "Name") == name);
object StatVal(string name) => Enum.Parse(statEnum, name);

int changes = 0;

// ---------- 1 Magic Description clear ----------
string[] skillNames = {
  "天怒之火","天之怒火","陨冰杀","电闪雷鸣","旋风墙","护身法盾","灵魂分裂","吸星大法","养生术","暗鬼阵","新传染","施毒大法","分身术","焰魔召唤术","魔焰强解术","君临步","屠龙斩","金刚之躯","快刀斩马","运气术","天雷锤","挑衅","破空斩"
};
foreach (var nm in skillNames)
{
    var hits = magics.Where(m => S(m, "Name") == nm).ToList();
    if (hits.Count == 0) { L("MAGIC_MISS " + nm); continue; }
    foreach (var m in hits)
    {
        var d = S(m, "Description");
        if (string.IsNullOrEmpty(d)) { L($"MAGIC_OK {nm} already clear"); continue; }
        L($"MAGIC_CLEAR {nm} descLen={d.Length}");
        if (doApply) { Set(m, "Description", ""); changes++; }
    }
}

// ---------- 4/5 Mall store ----------
void EnsureStore(string itemName, int price, string filter)
{
    var it = FindItem(itemName);
    if (it == null) { L("STORE_ITEM_MISS " + itemName); return; }
    var st = stores.FirstOrDefault(s => ReferenceEquals(P(s, "Item"), it));
    if (st == null)
    {
        L($"STORE_ADD {itemName} Price={price} Filter={filter}");
        if (!doApply) return;
        var create = FindCreate(storeType)!;
        var col = get.MakeGenericMethod(storeType).Invoke(ses, null)!;
        var neu = create.Invoke(col, null)!;
        Set(neu, "Item", it);
        Set(neu, "Price", price);
        Set(neu, "HuntGoldPrice", 0);
        Set(neu, "Available", true);
        try { Set(neu, "Filter", filter); } catch { }
        stores.Add(neu);
        changes++;
        return;
    }
    L($"STORE_SET {itemName} Price {S(st,"Price")}->{price} Filter '{S(st,"Filter")}'->'{filter}'");
    if (doApply)
    {
        Set(st, "Price", price);
        Set(st, "Available", true);
        try { Set(st, "Filter", filter); } catch { }
        changes++;
    }
}

EnsureStore("诅咒之药水", 100, "消耗品");
EnsureStore("万年雪霜", 100, "消耗品");

// Move ALL store items to 消耗品
foreach (var st in stores)
{
    var it = P(st, "Item");
    var iname = it == null ? "" : S(it, "ItemName");
    var f = S(st, "Filter");
    if (f != "消耗品")
    {
        L($"STORE_FILTER idx={Iv(st,"Index")} item={iname} '{f}'->'消耗品'");
        if (doApply) { try { Set(st, "Filter", "消耗品"); changes++; } catch { L("STORE_FILTER_FAIL"); } }
    }
}
L("STORE_NOTE 万年雪霜 give-count×1000 BLOCKED: StoreInfo has no Amount; MarketPlaceStoreBuy uses client Count*Price. Price=100 kept; StackSize already 9999. Prefer NPC pack workaround.");

// ---------- 6 Boots from sina 2005-03-31 ----------
// cols: AC, MR, Agility, 佩戴重量->BagWeight+WearWeight, 双手重量->HandWeight
var boots = new (string Name, int Ac, int Mr, int Agi, int Wear, int Hand)[]
{
    ("草鞋", 1, 1, 1, 6, 1),
    ("皮靴", 2, 2, 2, 8, 1),
    ("五彩鞋", 3, 2, 2, 8, 1),
    ("赤飞靴子", 4, 3, 3, 10, 2),
    ("天掌靴子", 5, 4, 4, 10, 2),
    ("黑皮靴子", 7, 7, 7, 12, 3),
    ("绝地靴", 7, 14, 3, 8, 1),
    ("月光鞋", 7, 3, 14, 8, 2),
    ("仙云靴", 7, 20, 0, 12, 4),
    ("无影靴", 7, 0, 20, 12, 4),
    ("武神之靴", 7, 11, 11, 12, 4),
};

void SetItemStat(object item, string statName, int amount)
{
    var existing = stats.FirstOrDefault(s => ReferenceEquals(P(s, "Item"), item) && S(s, "Stat") == statName);
    if (existing != null)
    {
        var cur = Iv(existing, "Amount");
        if (cur == amount) { L($"STATOK {S(item,"ItemName")} {statName}={amount}"); return; }
        L($"STATSET {S(item,"ItemName")} {statName} {cur}->{amount}");
        if (doApply) { Set(existing, "Amount", amount); changes++; }
        return;
    }
    if (amount == 0) { L($"STATSKIP0 {S(item,"ItemName")} {statName}"); return; }
    L($"STATADD {S(item,"ItemName")} {statName}={amount}");
    if (!doApply) return;
    var create = FindCreate(statType)!;
    var col = get.MakeGenericMethod(statType).Invoke(ses, null)!;
    var neu = create.Invoke(col, null)!;
    Set(neu, "Item", item);
    Set(neu, "Stat", StatVal(statName));
    Set(neu, "Amount", amount);
    stats.Add(neu);
    changes++;
}

foreach (var b in boots)
{
    var it = FindItem(b.Name);
    if (it == null) { L("BOOT_MISS " + b.Name); continue; }
    // keep Item.Weight as 佩戴重量 (site weight column)
    if (Iv(it, "Weight") != b.Wear)
    {
        L($"BOOT_WEIGHT {b.Name} {S(it,"Weight")}->{b.Wear}");
        if (doApply) { Set(it, "Weight", b.Wear); changes++; }
    }
    SetItemStat(it, "MinAC", 0);
    SetItemStat(it, "MaxAC", b.Ac);
    SetItemStat(it, "MinMR", 0);
    SetItemStat(it, "MaxMR", b.Mr);
    SetItemStat(it, "Agility", b.Agi);
    SetItemStat(it, "BagWeight", b.Wear);
    SetItemStat(it, "WearWeight", b.Wear);
    SetItemStat(it, "HandWeight", b.Hand);
}
L("BOOT_SOURCE https://games.sina.com.cn/o/z/mir3/2005-03-31/217194.shtml map 佩戴重量->BagWeight/WearWeight 双手重量->HandWeight");

// ---------- C) no-death-drop flags ----------
string[] flagItems = { "全能指环", "幸运霸龙头盔" };
string[] flagProps = { "CanDrop", "CanDeathDrop", "NoDeathDrop", "BindOnEquip", "Bound", "StartItem", "NoDuraLoss", "CanTrade", "CanStore", "CanRepair", "CanSell", "CanAuction" };
foreach (var nm in flagItems)
{
    var it = FindItem(nm);
    if (it == null) { L("FLAG_MISS " + nm); continue; }
    L($"FLAG_ITEM {nm} idx={Iv(it,"Index")}");
    foreach (var pn in flagProps)
    {
        var prop = itemType.GetProperty(pn);
        if (prop == null) continue;
        var val = prop.GetValue(it);
        L($"  PROP {pn}={val} type={prop.PropertyType.Name}");
    }
    // also dump bool-ish
    foreach (var prop in itemType.GetProperties())
    {
        if (prop.PropertyType == typeof(bool) || prop.PropertyType.Name.Contains("Flag") || prop.Name.Contains("Drop") || prop.Name.Contains("Bind") || prop.Name.Contains("Bound") || prop.Name.Contains("Death"))
            L($"  BOOLISH {prop.Name}={prop.GetValue(it)}");
    }
}

// Try clear death-drop protection: typically CanDeathDrop=true means CAN drop; false means won't drop.
// Or NoDeathDrop flag. We'll set CanDeathDrop=true if exists, NoDeathDrop=false, Bound-like false.
foreach (var nm in flagItems)
{
    var it = FindItem(nm);
    if (it == null) continue;
    void TrySetBool(string pn, bool want)
    {
        var prop = itemType.GetProperty(pn);
        if (prop == null || prop.PropertyType != typeof(bool)) return;
        var cur = (bool)prop.GetValue(it)!;
        if (cur == want) { L($"FLAG_OK {nm}.{pn}={want}"); return; }
        L($"FLAG_SET {nm}.{pn} {cur}->{want}");
        if (doApply) { Set(it, pn, want); changes++; }
    }
    TrySetBool("CanDeathDrop", true);
    TrySetBool("NoDeathDrop", false);
    TrySetBool("Bound", false);
    TrySetBool("BindOnEquip", false);
}

// ---------- D) 全能指环 Image ----------
var ring = FindItem("全能指环");
if (ring != null)
{
    L($"RING 全能指环 Image={S(ring,"Image")} Shape={S(ring,"Shape")} Effect={S(ring,"Effect")}");
    // list rings with similar Image values near red-square look candidates
    var rings = items.Where(x => S(x, "ItemType") == "Ring").Select(x => new { Name = S(x, "ItemName"), Image = Iv(x, "Image"), Shape = Iv(x, "Shape"), Idx = Iv(x, "Index") }).OrderBy(x => x.Image).ToList();
    foreach (var r in rings.Where(r => r.Image is >= 50 and <= 120 || r.Name.Contains("霸") || r.Name.Contains("指环") || r.Name.Contains("恢复") || r.Name.Contains("力量") || r.Name.Contains("紫碧") || r.Name.Contains("珊瑚") || r.Name.Contains("金")))
        L($"RINGCAND {r.Idx} {r.Name} Image={r.Image} Shape={r.Shape}");
}

// ---------- A) Monster 地天灭亡 Boss flag if any ----------
foreach (var mon in mons.Where(m => S(m, "MonsterName").Contains("地天") || S(m, "MonsterName").Contains("灭亡")))
{
    L($"MON {Iv(mon,"Index")} {S(mon,"MonsterName")} IsBoss={S(mon,"IsBoss")} CanCall={S(mon,"CanCall")} CallMonster={S(mon,"CallMonster")}");
    foreach (var prop in monType.GetProperties())
        if (prop.Name.Contains("Boss") || prop.Name.Contains("Track") || prop.Name == "AI")
            L($"  MPROP {prop.Name}={prop.GetValue(mon)}");
}


// D set Image to 力量戒指 (chunky gold + red face) — user icon match
{
    var ringFix = FindItem("全能指环");
    var look = FindItem("力量戒指") ?? FindItem("珊瑚戒指");
    if (ringFix != null && look != null)
    {
        var from = Iv(ringFix, "Image"); var to = Iv(look, "Image");
        L($"RING_IMAGE 全能指环 {from}->{to} (from {S(look,"ItemName")})");
        if (doApply && from != to) { Set(ringFix, "Image", to); try { Set(ringFix, "Shape", Iv(look, "Shape")); } catch {} changes++; }
    }
}

L($"changes={changes}");

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
L("DONE");
return 0;

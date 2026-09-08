using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("probe" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3ArkFix20260908 <probe|apply>");
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
void Set(object o, string n, object? val)
{
    var prop = o.GetType().GetProperty(n)!;
    var t = Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType;
    if (val != null && t.IsEnum && val is not Enum) prop.SetValue(o, Enum.Parse(t, val.ToString()!));
    else if (val != null && t != val.GetType() && t != typeof(object)) prop.SetValue(o, Convert.ChangeType(val, t));
    else prop.SetValue(o, val);
}
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var outDir = Path.Combine(root, "tools", "Mir3ArkFix20260908");
Directory.CreateDirectory(outDir);
var logPath = Path.Combine(outDir, $"log_{args[0]}_{stamp}.txt");
var log = new StreamWriter(logPath, false, new UTF8Encoding(true)) { AutoFlush = true };
void L(string s) { Console.WriteLine(s); log.WriteLine(s); }
L($"mode={(doApply ? "apply" : "probe")} stamp={stamp}");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_arkfix_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-ark-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var statType = lib.GetType("Library.SystemModels.ItemInfoStat")!;
var craftType = lib.GetType("Library.SystemModels.CraftItemInfo")!;
var statEnum = lib.GetTypes().First(t => t.Name == "Stat" && t.IsEnum);
var rarityEnum = itemType.GetProperty("Rarity")!.PropertyType;

var items = ListOf(ses, itemType);
var stats = ListOf(ses, statType);
var crafts = ListOf(ses, craftType);
var createStat = get.MakeGenericMethod(statType).Invoke(ses, null)!.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;
var createCraft = get.MakeGenericMethod(craftType).Invoke(ses, null)!.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;

object? FindItem(string name) => items.FirstOrDefault(x => S(x, "ItemName") == name);
object? FindItemContains(string name) => items.FirstOrDefault(x => S(x, "ItemName").Contains(name));
int changes = 0;

// ===== Dump types that look like random/excellent =====
L("=== TYPES random/excellent/added ===");
foreach (var t in lib.GetTypes().Where(t => (t.Namespace ?? "").Contains("SystemModels")).OrderBy(t => t.Name))
{
    var n = t.Name;
    if (n.Contains("Random", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Excel", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Added", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Bonus", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Weight", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Range", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Affix", StringComparison.OrdinalIgnoreCase) ||
        n.Contains("Stat", StringComparison.OrdinalIgnoreCase))
        L("TYPE " + t.FullName);
}

L("=== ItemInfo props Drop/Bind/Death/Stat ===");
foreach (var prop in itemType.GetProperties().OrderBy(p => p.Name))
{
    var n = prop.Name;
    if (n.Contains("Drop") || n.Contains("Bind") || n.Contains("Bound") || n.Contains("Death") ||
        n.Contains("Stat") || n.Contains("Random") || n.Contains("Excel") || n.Contains("Added") ||
        n.Contains("Image") || n.Contains("Shape") || n.Contains("Rarity") || n.Contains("Required") ||
        n.Contains("Durab") || n.Contains("Weight") || n.Contains("Can"))
        L($"ITEMPROP {n}:{prop.PropertyType.Name}");
}

void UpsertStat(object item, string sn, int amount)
{
    var existing = stats.FirstOrDefault(s => ReferenceEquals(P(s, "Item"), item) && S(s, "Stat") == sn);
    if (existing != null)
    {
        var cur = Iv(existing, "Amount");
        if (cur == amount) { L($"STATOK {S(item,"ItemName")} {sn}={amount}"); return; }
        L($"STATSET {S(item,"ItemName")} {sn} {cur}->{amount}");
        if (doApply) { Set(existing, "Amount", amount); changes++; }
        return;
    }
    if (amount == 0) { L($"STATZERO_SKIP_CREATE {S(item,"ItemName")} {sn}"); return; }
    L($"STATADD {S(item,"ItemName")} {sn}={amount}");
    if (doApply)
    {
        var row = createStat.Invoke(get.MakeGenericMethod(statType).Invoke(ses, null)!, null)!;
        row.GetType().GetProperty("Item")!.SetValue(row, item);
        Set(row, "Stat", sn);
        Set(row, "Amount", amount);
        stats.Add(row);
        changes++;
    }
}

void ZeroOrDeleteStat(object item, string sn)
{
    var existing = stats.FirstOrDefault(s => ReferenceEquals(P(s, "Item"), item) && S(s, "Stat") == sn);
    if (existing == null) { L($"STATMISS {S(item,"ItemName")} {sn}"); return; }
    var cur = Iv(existing, "Amount");
    if (cur == 0) { L($"STATOK {S(item,"ItemName")} {sn}=0"); return; }
    L($"STATSET {S(item,"ItemName")} {sn} {cur}->0");
    if (doApply) { Set(existing, "Amount", 0); changes++; }
}

// ===== BOOTS exact =====
// Comfort, WearWeight (穿戴负重), HandWeight (腕力); BagWeight=0; AC/MR=0
// Weight, NeedLevel, Durability*1000, Elite for 稀世
var boots = new (string Name, int Lv, int Wt, int Comfort, int Wear, int Hand, int Dur, bool Elite)[]
{
    ("草鞋", 6, 1, 1, 1, 1, 6, false),
    ("皮靴", 16, 1, 2, 2, 1, 8, false),
    ("五彩鞋", 26, 1, 3, 2, 3, 8, false),
    ("赤飞靴子", 33, 2, 4, 3, 3, 10, false),
    ("天掌靴子", 38, 2, 5, 4, 4, 10, false),
    ("黑皮靴子", 0, 3, 7, 7, 7, 12, true),
    ("绝地靴", 0, 1, 7, 14, 3, 8, true),
    ("月光鞋", 0, 2, 7, 3, 14, 8, true),
    ("仙云靴", 0, 4, 7, 20, 0, 12, true),
    ("无影靴", 0, 4, 7, 0, 20, 12, true),
    ("武神之靴", 0, 4, 7, 11, 11, 12, true),
};

L("=== BOOTS BEFORE ===");
foreach (var b in boots)
{
    var it = FindItem(b.Name);
    if (it == null) { L("BOOT_MISS " + b.Name); continue; }
    var st = stats.Where(s => ReferenceEquals(P(s, "Item"), it)).Select(s => $"{S(s,"Stat")}={Iv(s,"Amount")}").OrderBy(x => x);
    L($"BOOT {b.Name} idx={Iv(it,"Index")} Rarity={S(it,"Rarity")} ReqAmt={S(it,"RequiredAmount")} Wt={S(it,"Weight")} Dur={S(it,"Durability")} STATS[{string.Join(",", st)}]");
}

foreach (var b in boots)
{
    var it = FindItem(b.Name);
    if (it == null) { L("BOOT_MISS " + b.Name); continue; }
    // base props
    if (b.Elite)
    {
        if (S(it, "Rarity") != "Elite")
        {
            L($"RARITY {b.Name} {S(it,"Rarity")}->Elite");
            if (doApply) { Set(it, "Rarity", "Elite"); changes++; }
        }
        else L($"RARITYOK {b.Name}=Elite");
    }
    // RequiredAmount = Lv (0 for elite if Lv=0 — keep or clear?)
    if (b.Lv > 0)
    {
        var curLv = Iv(it, "RequiredAmount");
        if (curLv != b.Lv)
        {
            L($"REQ {b.Name} {curLv}->{b.Lv}");
            if (doApply) { Set(it, "RequiredAmount", b.Lv); changes++; }
        }
        else L($"REQOK {b.Name}={b.Lv}");
    }
    var curWt = Iv(it, "Weight");
    if (curWt != b.Wt) { L($"WEIGHT {b.Name} {curWt}->{b.Wt}"); if (doApply) { Set(it, "Weight", b.Wt); changes++; } }
    else L($"WEIGHTOK {b.Name}={b.Wt}");
    var wantDur = b.Dur * 1000;
    var curDur = Iv(it, "Durability");
    if (curDur != wantDur) { L($"DUR {b.Name} {curDur}->{wantDur}"); if (doApply) { Set(it, "Durability", wantDur); changes++; } }
    else L($"DUROK {b.Name}={wantDur}");

    UpsertStat(it, "Comfort", b.Comfort);
    UpsertStat(it, "WearWeight", b.Wear);
    UpsertStat(it, "HandWeight", b.Hand);
    // clear wrong bag weight & AC/MR
    ZeroOrDeleteStat(it, "BagWeight");
    ZeroOrDeleteStat(it, "MinAC");
    ZeroOrDeleteStat(it, "MaxAC");
    ZeroOrDeleteStat(it, "MinMR");
    ZeroOrDeleteStat(it, "MaxMR");
}

// Also zero AC/MR on ALL shoes ItemType
L("=== ALL SHOES AC/MR wipe ===");
foreach (var it in items.Where(i => S(i, "ItemType") == "Shoes"))
{
    foreach (var sn in new[] { "MinAC", "MaxAC", "MinMR", "MaxMR" })
        ZeroOrDeleteStat(it, sn);
}

// ===== Death drop flags =====
string[] flagItems = { "全能指环", "幸运霸龙头盔", "天掌靴子" };
L("=== DEATH DROP FLAGS ===");
foreach (var nm in flagItems)
{
    var it = FindItem(nm);
    if (it == null) { L("FLAG_MISS " + nm); continue; }
    L($"FLAG_ITEM {nm} idx={Iv(it,"Index")}");
    foreach (var prop in itemType.GetProperties())
    {
        if (prop.PropertyType == typeof(bool) || prop.Name.Contains("Drop") || prop.Name.Contains("Bind") || prop.Name.Contains("Bound") || prop.Name.Contains("Death"))
            L($"  BOOLISH {prop.Name}={prop.GetValue(it)} type={prop.PropertyType.Name}");
    }
    void TrySetBool(string pn, bool want)
    {
        var prop = itemType.GetProperty(pn);
        if (prop == null || prop.PropertyType != typeof(bool)) { L($"FLAG_NOPROP {nm}.{pn}"); return; }
        var cur = (bool)prop.GetValue(it)!;
        if (cur == want) { L($"FLAG_OK {nm}.{pn}={want}"); return; }
        L($"FLAG_SET {nm}.{pn} {cur}->{want}");
        if (doApply) { Set(it, pn, want); changes++; }
    }
    TrySetBool("CanDeathDrop", true);
    TrySetBool("NoDeathDrop", false);
    TrySetBool("CanDrop", true);
    // Don't force Bound=false if it's intentional bind - user only asked remove 死亡不会掉落
}

// ===== 全能指环 Image =====
L("=== RING IMAGE ===");
var ring = FindItem("全能指环");
if (ring != null)
{
    L($"RING 全能指环 Image={S(ring,"Image")} Shape={S(ring,"Shape")} Effect={S(ring,"Effect")}");
    var rings = items.Where(x => S(x, "ItemType") == "Ring")
        .Select(x => new { Name = S(x, "ItemName"), Image = Iv(x, "Image"), Shape = Iv(x, "Shape"), Idx = Iv(x, "Index") })
        .OrderBy(x => x.Image).ToList();
    foreach (var r in rings.Where(r =>
        r.Name.Contains("力量") || r.Name.Contains("珊瑚") || r.Name.Contains("紫碧") ||
        r.Name.Contains("金") || r.Name.Contains("霸") || r.Name.Contains("指环") ||
        r.Image is >= 470 and <= 600))
        L($"RINGCAND {r.Idx} {r.Name} Image={r.Image} Shape={r.Shape}");
    // Prefer 力量戒指 (gold+red) Image=535 from prior probe; verify still
    var look = FindItem("力量戒指") ?? FindItem("珊瑚戒指");
    if (look != null)
    {
        var from = Iv(ring, "Image"); var to = Iv(look, "Image");
        L($"RING_IMAGE 全能指环 {from}->{to} (from {S(look,"ItemName")})");
        if (from != to)
        {
            if (doApply) { Set(ring, "Image", to); try { Set(ring, "Shape", Iv(look, "Shape")); } catch { } changes++; }
        }
        else L("RING_IMAGE_OK already " + to);
    }
}

// ===== 影魅之刃 craft =====
L("=== CRAFT 影魅 BEFORE ===");
foreach (var c in crafts)
{
    var item = P(c, "Item");
    if (S(item, "ItemName") != "影魅之刃") continue;
    L($"CRAFT idx={Iv(c,"Index")} BP={S(c,"Blueprint")} rate={S(c,"SuccessRate")} gold={S(c,"GoldCost")} lv={S(c,"LevelNeeded")} sort={S(c,"SortNumber")} targetAmt={S(c,"TargetAmount")} time={S(c,"TimeCost")} exp={S(c,"GainExp")}");
    for (int k = 1; k <= 5; k++)
        L($"  Item{k}={S(P(c,"Item"+k),"ItemName")} Amount={S(c,"Amount"+k)}");
    foreach (var prop in craftType.GetProperties().OrderBy(p => p.Name))
        L($"  CPROP {prop.Name}={prop.GetValue(c)}");
}

var matNames = new[] { "血花落照", "黑天暗云", "九宫云雾", "万里碧海" };
var matItems = matNames.Select(n => FindItem(n) ?? throw new Exception("missing mat " + n)).ToArray();
var weps = new (int Bp, string Wep)[]
{
    (1, "破山剑"),
    (2, "天神法杖"),
    (3, "泰轮拂尘"),
};
// Also accept 泰伦 if 泰轮 missing
object ResolveWep(string n)
{
    var it = FindItem(n);
    if (it != null) return it;
    if (n == "泰轮拂尘")
    {
        it = FindItem("泰伦拂尘") ?? FindItemContains("泰伦") ?? FindItemContains("泰轮");
        if (it != null) { L("WEP_ALIAS " + n + " -> " + S(it, "ItemName")); return it; }
    }
    throw new Exception("missing weapon " + n);
}

var ymCrafts = crafts.Where(c => S(P(c, "Item"), "ItemName") == "影魅之刃").ToList();
var ymItem = FindItem("影魅之刃") ?? throw new Exception("影魅之刃 missing");

// Template from existing craft row if any
object? template = ymCrafts.FirstOrDefault();

foreach (var (bp, wepName) in weps)
{
    var wep = ResolveWep(wepName);
    var row = ymCrafts.FirstOrDefault(c => Iv(c, "Blueprint") == bp);
    if (row == null)
    {
        L($"CRAFT_CREATE BP={bp} wep={S(wep,"ItemName")}");
        if (doApply)
        {
            row = createCraft.Invoke(get.MakeGenericMethod(craftType).Invoke(ses, null)!, null)!;
            row.GetType().GetProperty("Item")!.SetValue(row, ymItem);
            Set(row, "Blueprint", bp);
            // copy template attrs
            if (template != null)
            {
                foreach (var pn in new[] { "SuccessRate", "GoldCost", "LevelNeeded", "SortNumber", "TargetAmount", "TimeCost", "GainExp", "TargetItemType" })
                {
                    try { var v = P(template, pn); if (v != null) Set(row, pn, v); } catch { }
                }
            }
            else
            {
                Set(row, "SuccessRate", 100);
                Set(row, "GoldCost", 600000000);
                Set(row, "LevelNeeded", 5);
                Set(row, "SortNumber", bp);
                Set(row, "TargetAmount", 1);
                Set(row, "TimeCost", 30);
                Set(row, "GainExp", 500);
            }
            Set(row, "SortNumber", bp);
            crafts.Add(row);
            ymCrafts.Add(row);
            changes++;
        }
        else continue;
    }
    else L($"CRAFT_EXIST BP={bp} idx={Iv(row,"Index")}");

    if (row == null) continue;
    // Set Item1 = weapon, Item2-5 = mats
    void SetSlot(object craft, int slot, object? item, int amount)
    {
        var cur = P(craft, "Item" + slot);
        var curName = S(cur, "ItemName");
        var wantName = S(item, "ItemName");
        if (curName != wantName)
        {
            L($"CRAFT_SET BP={Iv(craft,"Blueprint")} Item{slot} '{curName}'->'{wantName}'");
            if (doApply) { craft.GetType().GetProperty("Item" + slot)!.SetValue(craft, item); changes++; }
        }
        else L($"CRAFT_OK BP={Iv(craft,"Blueprint")} Item{slot}={wantName}");
        var curAmt = Iv(craft, "Amount" + slot);
        if (curAmt != amount)
        {
            L($"CRAFT_AMT BP={Iv(craft,"Blueprint")} Amount{slot} {curAmt}->{amount}");
            if (doApply) { Set(craft, "Amount" + slot, amount); changes++; }
        }
    }
    SetSlot(row, 1, wep, 1);
    for (int i = 0; i < 4; i++)
        SetSlot(row, i + 2, matItems[i], 1);
}

// Remove extra 影魅 craft rows that aren't BP 1/2/3
foreach (var c in ymCrafts.ToList())
{
    var bp = Iv(c, "Blueprint");
    if (bp is >= 1 and <= 3) continue;
    L($"CRAFT_EXTRA_BP idx={Iv(c,"Index")} BP={bp} — leave (not deleting unknown)");
}

// ===== 极品 / random pools for shoes =====
L("=== EXCELLENT / RANDOM pools ===");
// Try known type names
string[] candTypeNames = {
    "Library.SystemModels.RandomStatInfo",
    "Library.SystemModels.ItemRandomStatInfo",
    "Library.SystemModels.ItemStatWeightInfo",
    "Library.SystemModels.StatWeightInfo",
    "Library.SystemModels.ExcellentStatInfo",
    "Library.SystemModels.ItemExcelentStatInfo",
    "Library.SystemModels.FixedStatInfo",
    "Library.SystemModels.ItemFixedStatInfo",
    "Library.SystemModels.ItemAttributeInfo",
    "Library.SystemModels.AttributeInfo",
    "Library.SystemModels.ItemLevelStatInfo",
};
foreach (var tn in candTypeNames)
{
    var t = lib.GetType(tn);
    L($"CAND {(t == null ? "MISS" : "HIT")} {tn}");
}
// Broader dump of all SystemModels
foreach (var t in lib.GetTypes().Where(t => (t.Namespace ?? "") == "Library.SystemModels").OrderBy(t => t.Name))
    L("SM " + t.Name);

// Check ItemInfo for MaxStats / StatsChance style props and values on boots
L("=== BOOT ItemInfo random-ish props ===");
foreach (var b in boots)
{
    var it = FindItem(b.Name);
    if (it == null) continue;
    foreach (var prop in itemType.GetProperties())
    {
        var n = prop.Name;
        if (n.Contains("Stat", StringComparison.OrdinalIgnoreCase) ||
            n.Contains("Random", StringComparison.OrdinalIgnoreCase) ||
            n.Contains("Excel", StringComparison.OrdinalIgnoreCase) ||
            n.Contains("Added", StringComparison.OrdinalIgnoreCase) ||
            n.Contains("Bonus", StringComparison.OrdinalIgnoreCase) ||
            n.Contains("Chance", StringComparison.OrdinalIgnoreCase))
            L($"  {b.Name}.{n}={prop.GetValue(it)}");
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
        if (File.Exists(c) || Directory.Exists(dir))
            File.Copy(cliDb, c, true);
        L("synced " + label + "=" + dir);
    }
    Sync(Path.Combine(root, "Data"), "Data");
    Sync(Path.Combine(root, "deploy_to_Mir3service", "Database"), "deploy_to_Mir3service/Database");
}
L("DONE log=" + logPath);
return 0;

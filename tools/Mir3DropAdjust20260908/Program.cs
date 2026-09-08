using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Security.Cryptography;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: t <dry-run|apply>");
    return 1;
}
var doApply = args[0] == "apply";
var root = @"D:\newMir3";
var toolDir = Path.Combine(root, "tools", "Mir3DropAdjust20260908");
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
var dbObjectType = lib.GetType("MirDB.DBObject")!;
var monType = lib.GetType("Library.SystemModels.MonsterInfo")!;
var dropType = lib.GetType("Library.SystemModels.DropInfo")!;
var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var respawnType = lib.GetType("Library.SystemModels.RespawnInfo")!;
var statType = lib.GetType("Library.SystemModels.MonsterInfoStat")!;
var questDetailType = lib.GetTypes().FirstOrDefault(t => t.Name == "QuestTaskMonsterDetails");
var monDiyType = lib.GetTypes().FirstOrDefault(t => t.Name == "MonDiyAiAction");
var monAnimType = lib.GetTypes().FirstOrDefault(t => t.Name == "MonAnimationFrame");
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);

string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void SetP(object o, string n, object? v)
{
    var prop = o.GetType().GetProperty(n) ?? throw new Exception("no prop " + n);
    if (v == null) { prop.SetValue(o, null); return; }
    var t = Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType;
    if (t.IsEnum) prop.SetValue(o, Enum.Parse(t, v.ToString()!));
    else if (t == typeof(bool)) prop.SetValue(o, Convert.ToBoolean(v));
    else if (t == typeof(int)) prop.SetValue(o, Convert.ToInt32(v));
    else if (t == typeof(string)) prop.SetValue(o, v.ToString());
    else prop.SetValue(o, Convert.ChangeType(v, t));
}
string Hex16(string path) => Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(path)))[..16];

void InvokeDelete(object session, object obj)
{
    var fast = sessionType.GetMethod("FastDelete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)!;
    fast.Invoke(session, new[] { obj });
    var collField = dbObjectType.GetField("_Collection", BindingFlags.Instance | BindingFlags.NonPublic)!;
    var coll = collField.GetValue(obj)!;
    var del = coll.GetType().GetMethod("Delete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)!;
    del.Invoke(coll, new[] { obj });
}
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var aliases = new Dictionary<string, string>();
var deleteMons = new List<string>();
var deleteItemPrefix = new List<string>();
var attrMarkers = new List<string>();
var virtueItems = new List<string>();
string goldItemName = "\u91d1\u5e01";
int goldMid = 10000, goldBig = 100000;
var goldMidMons = new List<string>();
var goldBigMons = new List<string>();
var addRare = new List<(string mon, List<string> items, int chance)>();
var removes = new List<(string mon, List<string> items, string mode)>();
var setAmounts = new List<(string mon, string item, int amount)>();
var removeLv44 = new List<string>();

string section = "";
foreach (var raw in File.ReadAllLines(Path.Combine(toolDir, "rules.txt"), Encoding.UTF8))
{
    var line = raw.Trim();
    if (line.Length == 0 || line.StartsWith("#")) continue;
    if (line.StartsWith("[") && line.EndsWith("]")) { section = line[1..^1]; continue; }
    switch (section)
    {
        case "ALIASES":
            var ap = line.Split('=', 2); if (ap.Length == 2) aliases[ap[0].Trim()] = ap[1].Trim(); break;
        case "DELETE_MONSTERS": deleteMons.Add(line); break;
        case "DELETE_ITEM_PREFIX": deleteItemPrefix.Add(line); break;
        case "ATTR_MARKERS": attrMarkers.Add(line); break;
        case "VIRTUE_ITEMS": virtueItems.Add(line); break;
        case "GOLD":
            if (line.StartsWith("item=")) goldItemName = line[5..];
            else if (line.StartsWith("mid_amount=")) goldMid = int.Parse(line[11..]);
            else if (line.StartsWith("big_amount=")) goldBig = int.Parse(line[11..]);
            break;
        case "GOLD_MID": goldMidMons.Add(line); break;
        case "GOLD_BIG": goldBigMons.Add(line); break;
        case "ADD_RARE":
        {
            var parts = line.Split('|');
            addRare.Add((parts[0], parts[1].Split(',').Select(x => x.Trim()).Where(x => x.Length > 0).ToList(), int.Parse(parts[2])));
            break;
        }
        case "REMOVE":
        {
            var parts = line.Split('|');
            removes.Add((parts[0], parts[1].Split(',').Select(x => x.Trim()).Where(x => x.Length > 0).ToList(), parts.Length > 2 ? parts[2] : "exact"));
            break;
        }
        case "SET_AMOUNT":
        {
            var parts = line.Split('|');
            setAmounts.Add((parts[0], parts[1], int.Parse(parts[2])));
            break;
        }
        case "REMOVE_LV44_ARMOUR": removeLv44.Add(line); break;
    }
}
string ResolveMon(string name) => aliases.TryGetValue(name, out var a) ? a : name;

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
var counts = new Dictionary<string, int>();
void Inc(string k, int n = 1) => counts[k] = counts.GetValueOrDefault(k) + n;
report.AppendLine($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");

var bakDir = Path.Combine(root, "Database", "Backup_drops_20260908_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(bakDir, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(bakDir, "ClientSystem.db"), true);
report.AppendLine("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3drop-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work); Directory.CreateDirectory(work + "_bak");
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(work + "_bak") });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
try { sessionType.GetProperty("BackUp")!.SetValue(ses, false); } catch { }

var dropColl = get.MakeGenericMethod(dropType).Invoke(ses, null)!;
var mons = ListOf(ses, monType);
var drops = ListOf(ses, dropType);
var items = ListOf(ses, itemType);
var respawns = ListOf(ses, respawnType);
var stats = ListOf(ses, statType);
var createDrop = dropColl.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;

object? FindMonExact(string name)
{
    var r = ResolveMon(name);
    return mons.FirstOrDefault(m => S(m, "MonsterName") == r);
}
List<object> FindItemsExact(string name) => items.Where(i => S(i, "ItemName") == name).ToList();
List<object> FindItemsContains(string name) => items.Where(i => S(i, "ItemName").Contains(name)).ToList();

var toDeleteDrops = new HashSet<object>();
var toDeleteMons = new List<object>();
var toDeleteItems = new List<object>();
var skipped = new List<string>();
var doneRules = new List<string>();
var amountUpdates = new List<(object drop, int newAmt, string reason)>();
var goldUpdates = new List<(object drop, int newAmt, string reason)>();
var goldCreates = new List<(object mon, object item, int amt, string reason)>();
var rareCreates = new List<(object mon, object item, int chance, string reason)>();

void MarkDropRemove(object drop, string reason)
{
    if (toDeleteDrops.Add(drop))
    {
        Inc(reason.Split(':')[0]);
        report.AppendLine($"DEL Drop mon=[{S(P(drop, "Monster"), "MonsterName")}] item=[{S(P(drop, "Item"), "ItemName")}] C={Iv(drop, "Chance")} A={Iv(drop, "Amount")} reason={reason}");
    }
}

int ruleIdx = 0;
foreach (var (monName, itemNames, mode) in removes)
{
    ruleIdx++;
    var mon = FindMonExact(monName);
    if (mon == null) { skipped.Add($"REMOVE mon missing: {monName}"); report.AppendLine($"SKIP mon [{monName}]"); continue; }
    int hit = 0;
    foreach (var iname in itemNames)
    {
        var matchedItems = mode == "contains" ? FindItemsContains(iname) : FindItemsExact(iname);
        if (matchedItems.Count == 0) matchedItems = FindItemsContains(iname);
        if (matchedItems.Count == 0) { skipped.Add($"REMOVE item missing under {monName}: {iname}"); continue; }
        var ids = matchedItems.Select(i => Iv(i, "Index")).ToHashSet();
        foreach (var d in drops)
        {
            if (!ReferenceEquals(P(d, "Monster"), mon)) continue;
            var it = P(d, "Item"); if (it == null) continue;
            if (ids.Contains(Iv(it, "Index")))
            { MarkDropRemove(d, $"REMOVE:{monName}->{iname}"); hit++; }
        }
    }
    doneRules.Add($"REMOVE {ResolveMon(monName)} hits={hit}");
}

int attrHits = 0;
foreach (var d in drops)
{
    var it = P(d, "Item"); if (it == null) continue;
    var n = S(it, "ItemName");
    if (attrMarkers.Any(a => n.Contains(a)))
    { MarkDropRemove(d, "ATTR"); attrHits++; }
}
doneRules.Add($"ATTR candidates={attrHits}");

var virtueIds = items.Where(i => virtueItems.Any(v => S(i, "ItemName") == v)).Select(i => Iv(i, "Index")).ToHashSet();
int virtueHits = 0;
foreach (var d in drops)
{
    var it = P(d, "Item"); if (it == null) continue;
    if (virtueIds.Contains(Iv(it, "Index")))
    { MarkDropRemove(d, "VIRTUE"); virtueHits++; }
}
doneRules.Add($"VIRTUE hits={virtueHits}");

// delete item prefixes: remove ALL drops then delete ItemInfo
var delItemObjs = new List<object>();
foreach (var prefix in deleteItemPrefix)
{
    var matched = items.Where(i => S(i, "ItemName").StartsWith(prefix, StringComparison.Ordinal) || S(i, "ItemName") == prefix).ToList();
    if (matched.Count == 0) { skipped.Add($"DELETE_ITEM missing prefix: {prefix}"); continue; }
    var ids = matched.Select(i => Iv(i, "Index")).ToHashSet();
    int dh = 0;
    foreach (var d in drops)
    {
        var it = P(d, "Item"); if (it == null) continue;
        if (ids.Contains(Iv(it, "Index"))) { MarkDropRemove(d, $"DELITEM:{prefix}"); dh++; }
    }
    foreach (var it in matched) { delItemObjs.Add(it); report.AppendLine($"DEL ItemInfo #{Iv(it, "Index")} [{S(it, "ItemName")}]"); }
    doneRules.Add($"DELITEM {prefix} items={matched.Count} drops={dh}");
}

// lv44 armour drops
var lv44Ids = items.Where(i => S(i, "ItemType") == "Armour" && Iv(i, "RequiredAmount") == 44 && S(i, "RequiredType") == "Level")
    .Select(i => Iv(i, "Index")).ToHashSet();
report.AppendLine($"lv44ArmourCount={lv44Ids.Count}");
foreach (var monName in removeLv44.Distinct())
{
    var mon = FindMonExact(monName);
    if (mon == null) { skipped.Add($"LV44 mon missing: {monName}"); continue; }
    int hit = 0;
    foreach (var d in drops)
    {
        if (!ReferenceEquals(P(d, "Monster"), mon)) continue;
        var it = P(d, "Item"); if (it == null) continue;
        if (lv44Ids.Contains(Iv(it, "Index"))) { MarkDropRemove(d, $"LV44:{ResolveMon(monName)}"); hit++; }
    }
    doneRules.Add($"LV44 {ResolveMon(monName)} hits={hit}");
}

// set amounts
foreach (var (monName, itemName, amount) in setAmounts)
{
    var mon = FindMonExact(monName);
    if (mon == null) { skipped.Add($"SET_AMOUNT mon missing: {monName}"); continue; }
    var its = FindItemsExact(itemName);
    if (its.Count == 0) { skipped.Add($"SET_AMOUNT item missing: {itemName}"); continue; }
    var ids = its.Select(i => Iv(i, "Index")).ToHashSet();
    int hit = 0;
    foreach (var d in drops)
    {
        if (!ReferenceEquals(P(d, "Monster"), mon)) continue;
        var it = P(d, "Item"); if (it == null) continue;
        if (!ids.Contains(Iv(it, "Index"))) continue;
        if (toDeleteDrops.Contains(d)) continue;
        amountUpdates.Add((d, amount, $"SETAMT:{ResolveMon(monName)}->{itemName}"));
        report.AppendLine($"SET Amount mon=[{ResolveMon(monName)}] item=[{itemName}] {Iv(d, "Amount")}->{amount}");
        hit++; Inc("SET_AMOUNT");
    }
    if (hit == 0) skipped.Add($"SET_AMOUNT no drop: {monName}->{itemName}");
    doneRules.Add($"SET_AMOUNT {ResolveMon(monName)}->{itemName} hits={hit}");
}

// gold unify
var goldItem = items.FirstOrDefault(i => S(i, "ItemName") == goldItemName) ?? items.FirstOrDefault(i => Iv(i, "Index") == 1);
if (goldItem == null) skipped.Add("GOLD item missing");
else
{
    void UpsertGold(string monName, int amount, string tag)
    {
        var mon = FindMonExact(monName);
        if (mon == null) { skipped.Add($"GOLD mon missing: {monName}"); return; }
        var existing = drops.Where(d => ReferenceEquals(P(d, "Monster"), mon) && ReferenceEquals(P(d, "Item"), goldItem)).ToList();
        if (existing.Count == 0)
        {
            goldCreates.Add((mon, goldItem, amount, tag));
            report.AppendLine($"NEW Gold mon=[{ResolveMon(monName)}] Amount={amount}");
            Inc(tag + "_new");
        }
        else
        {
            // keep first, update; remove extras
            for (int i = 0; i < existing.Count; i++)
            {
                if (i == 0)
                {
                    goldUpdates.Add((existing[i], amount, tag));
                    report.AppendLine($"SET Gold mon=[{ResolveMon(monName)}] C={Iv(existing[i], "Chance")} A {Iv(existing[i], "Amount")}->{amount}");
                    Inc(tag + "_upd");
                }
                else MarkDropRemove(existing[i], $"GOLD_DUP:{ResolveMon(monName)}");
            }
        }
        doneRules.Add($"GOLD {tag} {ResolveMon(monName)} -> {amount}");
    }
    foreach (var m in goldMidMons) UpsertGold(m, goldMid, "GOLD_MID");
    foreach (var m in goldBigMons) UpsertGold(m, goldBig, "GOLD_BIG");
}

// add rare
foreach (var (monName, itemNames, chance) in addRare)
{
    var mon = FindMonExact(monName);
    if (mon == null) { skipped.Add($"ADD_RARE mon missing: {monName}"); continue; }
    foreach (var iname in itemNames)
    {
        var its = FindItemsExact(iname);
        if (its.Count == 0) { skipped.Add($"ADD_RARE item missing: {iname}"); continue; }
        var item = its[0];
        var exists = drops.Any(d => ReferenceEquals(P(d, "Monster"), mon) && ReferenceEquals(P(d, "Item"), item) && !toDeleteDrops.Contains(d));
        if (exists) { report.AppendLine($"OK rare exists mon=[{ResolveMon(monName)}] item=[{iname}]"); continue; }
        rareCreates.Add((mon, item, chance, $"RARE:{iname}"));
        report.AppendLine($"NEW Rare mon=[{ResolveMon(monName)}] item=[{iname}] Chance={chance}");
        Inc("RARE_NEW");
    }
    doneRules.Add($"ADD_RARE {ResolveMon(monName)}");
}

// delete monsters cascade plan
foreach (var monName in deleteMons)
{
    var mon = FindMonExact(monName);
    if (mon == null) { skipped.Add($"DELETE_MON missing: {monName}"); continue; }
    toDeleteMons.Add(mon);
    foreach (var d in drops.Where(d => ReferenceEquals(P(d, "Monster"), mon)))
        MarkDropRemove(d, $"DELMON_DROP:{ResolveMon(monName)}");
    report.AppendLine($"DEL MonsterInfo #{Iv(mon, "Index")} [{S(mon, "MonsterName")}]");
    Inc("DEL_MON");
    doneRules.Add($"DELETE_MON {ResolveMon(monName)}");
}

// script grep for delete items
var scriptHits = new List<string>();
var scriptsRoot = Path.Combine(root, "Scripts");
if (Directory.Exists(scriptsRoot))
{
    foreach (var prefix in deleteItemPrefix)
    {
        foreach (var file in Directory.EnumerateFiles(scriptsRoot, "*.py", SearchOption.AllDirectories))
        {
            string text;
            try { text = File.ReadAllText(file, Encoding.UTF8); } catch { continue; }
            if (text.Contains(prefix))
                scriptHits.Add($"{file.Substring(root.Length).TrimStart('\\', '/')}: contains {prefix}");
        }
    }
}
report.AppendLine($"scriptHits={scriptHits.Count}");
foreach (var h in scriptHits.Take(50)) report.AppendLine("SCRIPT " + h);

report.AppendLine("---- summary counts ----");
foreach (var kv in counts.OrderBy(k => k.Key)) report.AppendLine($"{kv.Key}={kv.Value}");
report.AppendLine($"toDeleteDrops={toDeleteDrops.Count} amountUpdates={amountUpdates.Count} goldUpdates={goldUpdates.Count} goldCreates={goldCreates.Count} rareCreates={rareCreates.Count} delItems={delItemObjs.Count} delMons={toDeleteMons.Count}");
report.AppendLine("---- skipped ----");
foreach (var s in skipped) report.AppendLine("SKIP " + s);
report.AppendLine("---- done rules ----");
foreach (var d in doneRules) report.AppendLine("DONE " + d);

var reportPath = Path.Combine(toolDir, $"{(doApply ? "apply" : "dry")}_{stamp}.txt");
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));
Console.WriteLine(report.ToString());
Console.WriteLine("report=" + reportPath);

if (!doApply)
{
    (ses as IDisposable)?.Dispose();
    return 0;
}

// APPLY
foreach (var (drop, amt, reason) in amountUpdates)
{
    if (toDeleteDrops.Contains(drop)) continue;
    SetP(drop, "Amount", amt);
}
foreach (var (drop, amt, reason) in goldUpdates)
{
    if (toDeleteDrops.Contains(drop)) continue;
    SetP(drop, "Amount", amt);
    SetP(drop, "Chance", 1);
    SetP(drop, "DropGroup", 0);
    SetP(drop, "DropSet", 0);
}
foreach (var (mon, item, amt, reason) in goldCreates)
{
    var nd = createDrop.Invoke(dropColl, null)!;
    SetP(nd, "Monster", mon);
    SetP(nd, "Item", item);
    SetP(nd, "Chance", 1);
    SetP(nd, "Amount", amt);
    SetP(nd, "DropGroup", 0);
    SetP(nd, "DropSet", 0);
    SetP(nd, "PartOnly", false);
    SetP(nd, "EasterEvent", false);
    try { SetP(nd, "StrMonsterName", S(mon, "MonsterName")); } catch { }
    try { SetP(nd, "StrItemName", S(item, "ItemName")); } catch { }
}
foreach (var (mon, item, chance, reason) in rareCreates)
{
    var nd = createDrop.Invoke(dropColl, null)!;
    SetP(nd, "Monster", mon);
    SetP(nd, "Item", item);
    SetP(nd, "Chance", chance);
    SetP(nd, "Amount", 1);
    SetP(nd, "DropGroup", 0);
    SetP(nd, "DropSet", 0);
    SetP(nd, "PartOnly", false);
    SetP(nd, "EasterEvent", false);
    try { SetP(nd, "StrMonsterName", S(mon, "MonsterName")); } catch { }
    try { SetP(nd, "StrItemName", S(item, "ItemName")); } catch { }
}

// cascade delete monsters related rows then monster
var cascade = new List<object>();
foreach (var mon in toDeleteMons)
{
    foreach (var stRow in stats.Where(st => ReferenceEquals(P(st, "Monster"), mon))) cascade.Add(stRow);
    foreach (var rs in respawns.Where(r => ReferenceEquals(P(r, "Monster"), mon))) cascade.Add(rs);
    if (questDetailType != null)
        foreach (var qd in ListOf(ses, questDetailType).Where(qd => ReferenceEquals(P(qd, "Monster"), mon))) cascade.Add(qd);
    if (monDiyType != null)
        foreach (var x in ListOf(ses, monDiyType).Where(x => ReferenceEquals(P(x, "Monster"), mon))) cascade.Add(x);
    if (monAnimType != null)
        foreach (var x in ListOf(ses, monAnimType).Where(x => ReferenceEquals(P(x, "Monster"), mon))) cascade.Add(x);
}
foreach (var d in toDeleteDrops) InvokeDelete(ses, d);
foreach (var obj in cascade) InvokeDelete(ses, obj);
foreach (var mon in toDeleteMons) InvokeDelete(ses, mon);
foreach (var it in delItemObjs) InvokeDelete(ses, it);

sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();

void CopyPair(string destDir)
{
    Directory.CreateDirectory(destDir);
    File.Copy(Path.Combine(work, "System.db"), Path.Combine(destDir, "System.db"), true);
    File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(destDir, "ClientSystem.db"), true);
}
CopyPair(Path.Combine(root, "Database"));
if (Directory.Exists(Path.Combine(root, "Data"))) CopyPair(Path.Combine(root, "Data"));

var deploy = Path.Combine(root, "deploy_to_Mir3service");
if (Directory.Exists(deploy))
{
    foreach (var sub in new[] { "Database", "Data", "" })
    {
        var dir = string.IsNullOrEmpty(sub) ? deploy : Path.Combine(deploy, sub);
        if (File.Exists(Path.Combine(dir, "System.db")) || sub == "Database")
        {
            try { CopyPair(dir); report.AppendLine("synced deploy " + dir); } catch (Exception ex) { report.AppendLine("deploy skip " + dir + " " + ex.Message); }
        }
    }
}

// mir3z
string? mir3z = null;
foreach (var ptxt in new[] { Path.Combine(root, "tools", "_mir3z_path.txt"), Path.Combine(root, "tools", "_mir3z_server_root.txt") })
{
    if (File.Exists(ptxt)) { mir3z = File.ReadAllText(ptxt, Encoding.UTF8).Trim(); if (!string.IsNullOrEmpty(mir3z)) break; }
}
if (!string.IsNullOrEmpty(mir3z) && Directory.Exists(mir3z))
{
    string? mzSys = null;
    foreach (var exe in Directory.GetFiles(mir3z, "Server.exe", SearchOption.AllDirectories))
    {
        if (exe.Contains("\\Source\\") || exe.Contains("\\obj\\")) continue;
        var cand = Path.Combine(Path.GetDirectoryName(exe)!, "Database", "System.db");
        if (File.Exists(cand)) { mzSys = cand; break; }
    }
    if (mzSys != null)
    {
        var mzDir = Path.GetDirectoryName(mzSys)!;
        var mzBak = Path.Combine(mzDir, "Backup_drops_20260908_" + stamp);
        Directory.CreateDirectory(mzBak);
        File.Copy(mzSys, Path.Combine(mzBak, "System.db"), true);
        var mzCli = Path.Combine(mzDir, "ClientSystem.db");
        if (File.Exists(mzCli)) File.Copy(mzCli, Path.Combine(mzBak, "ClientSystem.db"), true);
        File.Copy(Path.Combine(work, "System.db"), mzSys, true);
        if (File.Exists(mzCli)) File.Copy(Path.Combine(work, "ClientSystem.db"), mzCli, true);
        report.AppendLine("synced mir3z " + mzSys);
    }
    else report.AppendLine("mir3z System.db not found under " + mir3z);
}

var sysHex = Hex16(Path.Combine(root, "Database", "System.db"));
report.AppendLine("System.db sha16=" + sysHex);
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));

var wlDir = Path.Combine(root, "_whitelist");
Directory.CreateDirectory(wlDir);
var wl = new StringBuilder();
wl.AppendLine("drop_adjust_20260908");
wl.AppendLine("stamp=" + stamp);
wl.AppendLine("System.db_sha16=" + sysHex);
foreach (var kv in counts.OrderBy(k => k.Key)) wl.AppendLine($"{kv.Key}={kv.Value}");
wl.AppendLine($"drops_removed={toDeleteDrops.Count}");
wl.AppendLine($"amount_updates={amountUpdates.Count}");
wl.AppendLine($"gold_updates={goldUpdates.Count}");
wl.AppendLine($"gold_creates={goldCreates.Count}");
wl.AppendLine($"rare_creates={rareCreates.Count}");
wl.AppendLine($"items_deleted={delItemObjs.Count}");
wl.AppendLine($"monsters_deleted={toDeleteMons.Count}");
wl.AppendLine("skipped:");
foreach (var s in skipped) wl.AppendLine("  " + s);
File.WriteAllText(Path.Combine(wlDir, "drop_adjust_20260908.txt"), wl.ToString(), new UTF8Encoding(false));

var docsDir = Path.Combine(root, "docs");
if (Directory.Exists(docsDir))
{
    File.WriteAllText(Path.Combine(docsDir, "drop_adjust_20260908.md"),
        "# Drop adjust 2026-09-08\n\nApplied checklist of 23 monster/drop changes via tools/Mir3DropAdjust20260908.\n\nSee `_whitelist/drop_adjust_20260908.txt` and tool apply report.\n",
        new UTF8Encoding(false));
}

Console.WriteLine("APPLY OK sha16=" + sysHex);
return 0;

using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3ComfortFix <dry-run|apply>");
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
MethodInfo? FindCreate(Type t)
{
    var colType = get.MakeGenericMethod(t).ReturnType;
    return colType.GetMethods().FirstOrDefault(m => m.Name == "CreateNewObject" && m.GetParameters().Length == 0);
}

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var logPath = Path.Combine(root, "tools", "Mir3ComfortFix", $"log_{args[0]}_{stamp}.txt");
var log = new StreamWriter(logPath, false, new UTF8Encoding(true)) { AutoFlush = true };
void L(string s) { Console.WriteLine(s); log.WriteLine(s); }
L($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_comfort_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-comfort-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var statType = lib.GetType("Library.SystemModels.ItemInfoStat")!;
var statEnum = lib.GetTypes().First(t => t.Name == "Stat" && t.IsEnum);
var items = ListOf(ses, itemType);
var stats = ListOf(ses, statType);
object StatVal(string name) => Enum.Parse(statEnum, name);
int changes = 0;

void UpsertStat(object item, string statName, int amount)
{
    var existing = stats.Where(s => ReferenceEquals(P(s, "Item"), item) && S(s, "Stat") == statName).ToList();
    if (existing.Count > 1)
    {
        L($"STATDUP {S(item,"ItemName")} {statName} count={existing.Count} keeping first");
        // keep first, zero extras on apply
        for (int i = 1; i < existing.Count; i++)
        {
            L($"STATDUPZERO {S(item,"ItemName")} {statName} idx={Iv(existing[i],"Index")}");
            if (doApply) { Set(existing[i], "Amount", 0); changes++; }
        }
    }
    var row = existing.FirstOrDefault();
    if (row != null)
    {
        var cur = Iv(row, "Amount");
        if (cur == amount) { L($"STATOK {S(item,"ItemName")} {statName}={amount}"); return; }
        L($"STATSET {S(item,"ItemName")} {statName} {cur}->{amount}");
        if (doApply) { Set(row, "Amount", amount); changes++; }
        return;
    }
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

// Exact targets: Comfort + WearWeight(穿戴负重) + HandWeight(腕力); keep Weight/NeedLevel/Dur as previously set
var boots = new (string Name, int Comfort, int Wear, int Hand)[]
{
    ("草鞋", 1, 1, 1),
    ("皮靴", 2, 2, 1),
    ("五彩鞋", 3, 2, 3),
    ("赤飞靴子", 4, 3, 3),
    ("天掌靴子", 5, 4, 4),
    ("黑皮靴子", 7, 7, 7),
    ("绝地靴", 7, 14, 3),
    ("月光鞋", 7, 3, 14),
    ("仙云靴", 7, 20, 0),
    ("无影靴", 7, 0, 20),
    ("武神之靴", 7, 11, 11),
};

L("=== BEFORE ===");
foreach (var b in boots)
{
    var it = items.FirstOrDefault(x => S(x, "ItemName") == b.Name);
    if (it == null) { L("MISS " + b.Name); continue; }
    var st = stats.Where(s => ReferenceEquals(P(s, "Item"), it))
        .Where(s => new[]{"Comfort","WearWeight","HandWeight","BagWeight","MaxAC","MaxMR"}.Contains(S(s,"Stat")))
        .Select(s => S(s,"Stat")+"="+Iv(s,"Amount")).OrderBy(x=>x);
    L($"BEFORE {b.Name} Shape={Iv(it,"Shape")} Wt={Iv(it,"Weight")} Dur={Iv(it,"Durability")} Req={Iv(it,"RequiredAmount")} [{string.Join(",", st)}]");
}

L("=== APPLY Comfort/Wear/Hand ===");
foreach (var b in boots)
{
    var it = items.FirstOrDefault(x => S(x, "ItemName") == b.Name);
    if (it == null) { L("MISS " + b.Name); continue; }
    UpsertStat(it, "Comfort", b.Comfort);
    UpsertStat(it, "WearWeight", b.Wear);
    UpsertStat(it, "HandWeight", b.Hand);
    UpsertStat(it, "BagWeight", 0);
}

L("=== AFTER ===");
foreach (var b in boots)
{
    var it = items.FirstOrDefault(x => S(x, "ItemName") == b.Name);
    if (it == null) continue;
    var comfort = stats.Where(s => ReferenceEquals(P(s,"Item"), it) && S(s,"Stat")=="Comfort").Select(s => Iv(s,"Amount")).ToList();
    var wear = stats.Where(s => ReferenceEquals(P(s,"Item"), it) && S(s,"Stat")=="WearWeight").Select(s => Iv(s,"Amount")).FirstOrDefault();
    var hand = stats.Where(s => ReferenceEquals(P(s,"Item"), it) && S(s,"Stat")=="HandWeight").Select(s => Iv(s,"Amount")).FirstOrDefault();
    var ok = comfort.Count == 1 && comfort[0] == b.Comfort && wear == b.Wear && hand == b.Hand;
    L($"AFTER {b.Name} Comfort={string.Join("/",comfort)} want={b.Comfort} Wear={wear} Hand={hand} {(ok?"OK":"BAD")}");
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
        if (!Directory.Exists(dir)) { L(label + " MISSING " + dir); return; }
        File.Copy(sysDb, Path.Combine(dir, "System.db"), true);
        var c = Path.Combine(dir, "ClientSystem.db");
        if (File.Exists(c) || label.Contains("Data") || label.Contains("deploy") || label.Contains("mir3z"))
            File.Copy(cliDb, Path.Combine(dir, "ClientSystem.db"), true);
        L("synced " + label + "=" + dir);
    }
    Sync(Path.Combine(root, "Data"), "Data");
    Sync(Path.Combine(root, "deploy_to_Mir3service", "Database"), "deploy_to_Mir3service/Database");
    // mir3z
    var mir3zRoot = File.ReadAllText(Path.Combine(root, "tools", "_mir3z_resolved.txt")).Trim();
    Sync(Path.Combine(mir3zRoot, "Database"), "mir3z/Database");
    var mir3zData = Path.Combine(mir3zRoot, "Data");
    if (Directory.Exists(mir3zData)) Sync(mir3zData, "mir3z/Data");
    // live client Data
    var live = @"E:\Mir3_16000\Data";
    if (Directory.Exists(live))
    {
        File.Copy(cliDb, Path.Combine(live, "ClientSystem.db"), true);
        L("synced live ClientSystem=" + live);
    }
}
L("log=" + logPath);
L("DONE");
return 0;

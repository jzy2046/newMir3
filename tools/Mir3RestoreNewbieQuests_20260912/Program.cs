using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
var toolDir = Path.Combine(root, "tools", "Mir3RestoreNewbieQuests_20260912");
var deps = Path.Combine(root, "tools", "_deps");
var bakSrc = Path.Combine(root, "Database", "Backup_arkbatch4_20260912_144120");
var modeArg = args.Length > 0 ? args[0] : "dry-run";
var doApply = modeArg == "apply";
var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L("mode=" + modeArg + " stamp=" + stamp);
L("backupSrc=" + bakSrc);

if (!File.Exists(Path.Combine(bakSrc, "System.db")) || !File.Exists(Path.Combine(bakSrc, "ClientSystem.db")))
    throw new FileNotFoundException("backup missing System/ClientSystem under " + bakSrc);

AssemblyLoadContext.Default.Resolving += (_, a) =>
{
    foreach (var d in new[] { deps, root })
    {
        var p = Path.Combine(d, (a.Name ?? "") + ".dll");
        if (File.Exists(p)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(p);
    }
    return null;
};
var lib = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root, "Library.dll"));
var sessionType = lib.GetType("MirDB.Session")!;
var modeType = lib.GetType("MirDB.SessionMode")!;
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void SetP(object o, string n, object? v)
{
    var prop = o.GetType().GetProperty(n) ?? throw new Exception("no prop " + n);
    if (v == null) { prop.SetValue(o, null); return; }
    var t = Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType;
    if (t.IsEnum) prop.SetValue(o, Enum.Parse(t, v.ToString()!));
    else if (t == typeof(decimal)) prop.SetValue(o, Convert.ToDecimal(v));
    else if (t == typeof(bool)) prop.SetValue(o, Convert.ToBoolean(v));
    else if (t == typeof(int)) prop.SetValue(o, Convert.ToInt32(v));
    else if (t == typeof(string)) prop.SetValue(o, v.ToString());
    else prop.SetValue(o, Convert.ChangeType(v, t));
}
string S(object? o, string n) => Convert.ToString(P(o, n)) ?? "";
int Iv(object? o, string n) { var v = P(o, n); return v == null ? 0 : Convert.ToInt32(v); }
decimal Dv(object? o, string n) { var v = P(o, n); return v == null ? 0m : Convert.ToDecimal(v); }
List<object> Coll(object ses, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(ses, null)!).Cast<object>().ToList();

// Expected deleted quest indices from ArkBatch4
var expectIds = new HashSet<int>();
for (int i = 410; i <= 413; i++) expectIds.Add(i);
for (int i = 418; i <= 481; i++) expectIds.Add(i);
L("expectQuestIds=" + expectIds.Count);

// Safety backup of CURRENT (post-delete) DB before overwrite
var safetyBak = Path.Combine(root, "Database", "Backup_before_restore_newbie_" + stamp);
Directory.CreateDirectory(safetyBak);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(safetyBak, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(safetyBak, "ClientSystem.db"), true);
L("safetyBak=" + safetyBak);

var work = Path.Combine(toolDir, "_work_" + stamp);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
// Restore from pre-delete backup (has all newbie quests + old prices)
File.Copy(Path.Combine(bakSrc, "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(bakSrc, "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);
L("work seeded from backup");

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var itemT = lib.GetType("Library.SystemModels.ItemInfo")!;
var monT = lib.GetType("Library.SystemModels.MonsterInfo")!;
var monStatT = lib.GetType("Library.SystemModels.MonsterInfoStat")!;
var questT = lib.GetType("Library.SystemModels.QuestInfo")!;
var npcT = lib.GetType("Library.SystemModels.NPCInfo")!;
var statEnum = lib.GetType("Library.Stat")!;
var healthStat = Enum.Parse(statEnum, "Health");

var items = Coll(ses, itemT);
var mons = Coll(ses, monT);
var monStats = Coll(ses, monStatT);
var quests = Coll(ses, questT);
var npcs = Coll(ses, npcT);
L($"loaded items={items.Count} mons={mons.Count} quests={quests.Count} npcs={npcs.Count}");

var restored = quests.Where(q => expectIds.Contains(Iv(q, "Index"))).OrderBy(q => Iv(q, "Index")).ToList();
L("restoredQuestRows_in_work=" + restored.Count);
foreach (var q in restored)
    L($"QUEST [{Iv(q,"Index")}] {S(q,"QuestName")} start={S(P(q,"StartNPC"),"NPCName")} finish={S(P(q,"FinishNPC"),"NPCName")}");
var missing = expectIds.Where(id => !restored.Any(q => Iv(q, "Index") == id)).ToList();
if (missing.Count > 0) L("WARN missing ids in backup: " + string.Join(",", missing));

// Count NPC Start/Finish links to those quests
int npcLinks = 0;
foreach (var n in npcs)
{
    foreach (var propName in new[] { "StartQuests", "FinishQuests" })
    {
        if (P(n, propName) is not IEnumerable en) continue;
        foreach (var q in en.Cast<object>())
        {
            if (q != null && expectIds.Contains(Iv(q, "Index")))
            {
                npcLinks++;
                L($"NPC_LINK {S(n,"NPCName")}#{Iv(n,"Index")} {propName} quest#{Iv(q,"Index")}");
            }
        }
    }
}
L("npcLinksToRestoredQuests=" + npcLinks);

// Re-apply ONLY batch4 non-quest changes
L("\n=== reapply boss查询卷 Price=500 ===");
var bossItems = items.Where(x => Iv(x, "Index") == 122584 || S(x, "ItemName").Contains("查询卷")).ToList();
L("bossItems=" + bossItems.Count);
foreach (var it in bossItems)
{
    L($"BEFORE idx={Iv(it,"Index")} name={S(it,"ItemName")} Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")}");
    if (doApply)
    {
        SetP(it, "Price", 500);
        SetP(it, "SellRate", 1m);
        SetP(it, "CanSell", true);
    }
    L($"AFTER  Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")} sell={(long)(Iv(it,"Price")*Dv(it,"SellRate"))}");
}

L("\n=== reapply 霸王守卫 HP=5000 ===");
var guards = mons.Where(x => S(x, "MonsterName") == "霸王守卫").ToList();
L("guards=" + guards.Count);
foreach (var m in guards)
{
    var stats = monStats.Where(s => {
        var mon = P(s, "Monster");
        return mon != null && Iv(mon, "Index") == Iv(m, "Index") && Equals(P(s, "Stat"), healthStat);
    }).ToList();
    foreach (var st in stats)
    {
        L($"Health BEFORE={P(st,"Amount")}");
        if (doApply) SetP(st, "Amount", 5000);
        L($"Health AFTER={P(st,"Amount")}");
    }
    if (stats.Count == 0) L("WARN no Health stat");
}

L("\n=== reapply 地煞石/天罡石 Price=1 ===");
var stones = items.Where(x => {
    var n = S(x, "ItemName");
    return n == "地煞石" || n == "天罡石" || Iv(x,"Index")==122585 || Iv(x,"Index")==122586;
}).ToList();
L("stones=" + stones.Count);
foreach (var it in stones)
{
    L($"BEFORE idx={Iv(it,"Index")} name={S(it,"ItemName")} Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")}");
    if (doApply)
    {
        SetP(it, "Price", 1);
        SetP(it, "SellRate", 1m);
        SetP(it, "CanSell", true);
    }
    L($"AFTER  Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")}");
}

if (doApply)
{
    var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })
        ?? throw new InvalidOperationException("Save missing");
    save.Invoke(ses, new object[] { true, tool });
    L("saved");
}
(ses as IDisposable)?.Dispose();

if (doApply)
{
    // verify reopen
    var work2 = Path.Combine(toolDir, "_verify_" + stamp);
    Directory.CreateDirectory(work2); Directory.CreateDirectory(work2 + "_bak");
    File.Copy(Path.Combine(work, "System.db"), Path.Combine(work2, "System.db"), true);
    File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(work2, "ClientSystem.db"), true);
    var ses2 = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work2), Slash(work2 + "_bak") });
    sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses2, null);
    sessionType.GetProperty("BackUp")!.SetValue(ses2, false);
    var items2 = Coll(ses2, itemT);
    var mons2 = Coll(ses2, monT);
    var monStats2 = Coll(ses2, monStatT);
    var quests2 = Coll(ses2, questT);
    var npcs2 = Coll(ses2, npcT);

    void CheckItem(int idx, int expectPrice)
    {
        var it = items2.First(x => Iv(x, "Index") == idx);
        L($"VERIFY ITEM {idx} {S(it,"ItemName")} Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")} sell={(long)(Iv(it,"Price")*Dv(it,"SellRate"))} expectPrice={expectPrice}");
    }
    CheckItem(122584, 500);
    CheckItem(122585, 1);
    CheckItem(122586, 1);

    var g = mons2.First(x => S(x, "MonsterName") == "霸王守卫");
    var hs = monStats2.Where(s => Iv(P(s,"Monster"),"Index")==Iv(g,"Index") && Equals(P(s,"Stat"), healthStat)).ToList();
    foreach (var h in hs) L($"VERIFY MON Health={P(h,"Amount")}");

    var got = quests2.Where(q => expectIds.Contains(Iv(q, "Index"))).ToList();
    L($"VERIFY restoredQuests={got.Count}/{expectIds.Count} totalQuests={quests2.Count}");
    var stillMissing = expectIds.Where(id => !got.Any(q => Iv(q,"Index")==id)).ToList();
    if (stillMissing.Count > 0) L("VERIFY FAIL missing=" + string.Join(",", stillMissing));

    int links2 = 0;
    foreach (var n in npcs2)
    {
        foreach (var propName in new[] { "StartQuests", "FinishQuests" })
        {
            if (P(n, propName) is not IEnumerable en) continue;
            foreach (var q in en.Cast<object>())
                if (q != null && expectIds.Contains(Iv(q, "Index"))) links2++;
        }
    }
    L("VERIFY npcLinks=" + links2);

    int broken = 0;
    foreach (var n in npcs2)
    {
        foreach (var propName in new[] { "StartQuests", "FinishQuests" })
        {
            if (P(n, propName) is not IEnumerable en) continue;
            foreach (var q in en.Cast<object>())
            {
                if (q == null) { broken++; continue; }
                if (!quests2.Any(x => Iv(x, "Index") == Iv(q, "Index"))) broken++;
            }
        }
    }
    L("VERIFY brokenNpcQuestLinks=" + broken);
    (ses2 as IDisposable)?.Dispose();

    foreach (var name in new[] { "System.db", "ClientSystem.db" })
    {
        File.Copy(Path.Combine(work, name), Path.Combine(root, "Database", name), true);
        var data = Path.Combine(root, "Data", name);
        if (Directory.Exists(Path.GetDirectoryName(data)!))
            File.Copy(Path.Combine(work, name), data, true);
        var deploy = Path.Combine(root, "deploy_to_Mir3service", "Database", name);
        if (Directory.Exists(Path.GetDirectoryName(deploy)!))
            File.Copy(Path.Combine(work, name), deploy, true);
    }
    L("copied to Database + Data + deploy_to_Mir3service/Database");
}

var reportPath = Path.Combine(toolDir, (doApply ? "apply_" : "dry_") + stamp + ".txt");
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));
L("REPORT=" + reportPath);
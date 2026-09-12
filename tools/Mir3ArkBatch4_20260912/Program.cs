using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
var toolDir = Path.Combine(root, "tools", "Mir3ArkBatch4_20260912");
var deps = Path.Combine(root, "tools", "_deps");
var modeArg = args.Length > 0 ? args[0] : "dry-run";
var doApply = modeArg == "apply";
var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L("mode=" + modeArg + " stamp=" + stamp);

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
var dbObjectType = lib.GetType("MirDB.DBObject")!;
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

void InvokeDelete(object session, object obj)
{
    // Prefer DBObject.Delete() which handles associations
    var del = obj.GetType().GetMethod("Delete", Type.EmptyTypes);
    if (del != null) { del.Invoke(obj, null); return; }
    var fast = sessionType.GetMethod("FastDelete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)
        ?? throw new InvalidOperationException("no Delete");
    fast.Invoke(session, new[] { obj });
}

var bakDir = Path.Combine(root, "Database", "Backup_arkbatch4_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(bakDir, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(toolDir, "_work_" + stamp);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var itemT = lib.GetType("Library.SystemModels.ItemInfo")!;
var monT = lib.GetType("Library.SystemModels.MonsterInfo")!;
var monStatT = lib.GetType("Library.SystemModels.MonsterInfoStat")!;
var questT = lib.GetType("Library.SystemModels.QuestInfo")!;
var taskT = lib.GetType("Library.SystemModels.QuestTask")!;
var rewardT = lib.GetType("Library.SystemModels.QuestReward")!;
var reqT = lib.GetType("Library.SystemModels.QuestRequirement")!;
var monDetT = lib.GetType("Library.SystemModels.QuestTaskMonsterDetails")!;
var npcT = lib.GetType("Library.SystemModels.NPCInfo")!;
var statEnum = lib.GetType("Library.Stat")!;
var healthStat = Enum.Parse(statEnum, "Health");

var items = Coll(ses, itemT);
var mons = Coll(ses, monT);
var monStats = Coll(ses, monStatT);
var quests = Coll(ses, questT);
var tasks = Coll(ses, taskT);
var rewards = Coll(ses, rewardT);
var reqs = Coll(ses, reqT);
var monDets = Coll(ses, monDetT);
var npcs = Coll(ses, npcT);
L($"loaded items={items.Count} mons={mons.Count} quests={quests.Count} tasks={tasks.Count}");

// ========== 1) boss查询卷 sell 500 gold ==========
// Formula: sellGold = (long)(Price * count * SellRate) when Durability==0
// Set Price=500, SellRate=1 => NPC sell = 500
L("\n=== 1 boss查询卷 Price ===");
var bossItems = items.Where(x => {
    var n = S(x, "ItemName");
    return n == "boss查询卷" || Iv(x, "Index") == 122584 || (n.Contains("查询卷") && n.Contains("boss", StringComparison.OrdinalIgnoreCase));
}).ToList();
L("bossItems=" + bossItems.Count);
foreach (var it in bossItems)
{
    var beforeP = Iv(it, "Price");
    var beforeR = Dv(it, "SellRate");
    var beforeSell = (long)(beforeP * beforeR);
    L($"BEFORE idx={Iv(it,"Index")} name={S(it,"ItemName")} Price={beforeP} SellRate={beforeR} Durability={Iv(it,"Durability")} CanSell={P(it,"CanSell")} sellGold~={beforeSell}");
    if (doApply)
    {
        SetP(it, "Price", 500);
        SetP(it, "SellRate", 1m);
        SetP(it, "CanSell", true);
    }
    L($"AFTER  idx={Iv(it,"Index")} Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")} sellGold~={(long)(Iv(it,"Price")*Dv(it,"SellRate"))}");
}
L("推广礼包 grants same item name boss查询卷 via Shape=67 script — no separate item copy.");

// ========== 2) 霸王守卫 HP=5000 ==========
L("\n=== 2 霸王守卫 HP ===");
var guards = mons.Where(x => S(x, "MonsterName") == "霸王守卫").ToList();
L("guards=" + guards.Count);
foreach (var m in guards)
{
    L($"MON idx={Iv(m,"Index")} name={S(m,"MonsterName")} Level={Iv(m,"Level")}");
    var stats = monStats.Where(s => {
        var mon = P(s, "Monster");
        return mon != null && Iv(mon, "Index") == Iv(m, "Index") && Equals(P(s, "Stat"), healthStat);
    }).ToList();
    if (stats.Count == 0)
    {
        // try via association
        if (P(m, "MonsterInfoStats") is IEnumerable en)
            stats = en.Cast<object>().Where(s => Equals(P(s, "Stat"), healthStat)).ToList();
    }
    foreach (var st in stats)
    {
        L($"  Health BEFORE Amount={P(st,"Amount")}");
        if (doApply) SetP(st, "Amount", 5000);
        L($"  Health AFTER  Amount={P(st,"Amount")}");
    }
    if (stats.Count == 0) L("  WARN no Health stat found");
}

// ========== 3) 地煞石 / 天罡石 Price=1, SellRate=1 ==========
L("\n=== 3 地煞石/天罡石 Price ===");
var stones = items.Where(x => {
    var n = S(x, "ItemName");
    return n == "地煞石" || n == "天罡石" || n.StartsWith("地煞石") || n.StartsWith("天罡石");
}).ToList();
L("stones=" + stones.Count);
foreach (var it in stones)
{
    var beforeP = Iv(it, "Price");
    var beforeR = Dv(it, "SellRate");
    L($"BEFORE idx={Iv(it,"Index")} name={S(it,"ItemName")} Price={beforeP} SellRate={beforeR} sellGold~={(long)(beforeP*beforeR)}");
    if (doApply)
    {
        SetP(it, "Price", 1);
        SetP(it, "SellRate", 1m);
        SetP(it, "CanSell", true);
    }
    L($"AFTER  idx={Iv(it,"Index")} Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")} sellGold~={(long)(Iv(it,"Price")*Dv(it,"SellRate"))}");
}

// ========== 4) Delete all 新手任务 ==========
L("\n=== 4 Delete newbie quests ===");
var newbie = quests.Where(q => S(q, "QuestName").Contains("新手") || S(q, "QuestName").Contains("序章") || S(q, "QuestName").Contains("引导")).OrderBy(q => Iv(q, "Index")).ToList();
// also name pattern 新手任务
L("newbieQuests=" + newbie.Count);
var newbieIds = newbie.Select(q => Iv(q, "Index")).ToHashSet();
foreach (var q in newbie)
    L($"DEL_QUEST [{Iv(q,"Index")}] {S(q,"QuestName")} type={S(q,"QuestType")} start={S(P(q,"StartNPC"),"NPCName")}");

var delMon = monDets.Where(d => { var t = P(d, "Task"); var q = t == null ? null : P(t, "Quest"); return q != null && newbieIds.Contains(Iv(q, "Index")); }).ToList();
var delTasks = tasks.Where(t => { var q = P(t, "Quest"); return q != null && newbieIds.Contains(Iv(q, "Index")); }).ToList();
var delRewards = rewards.Where(r => { var q = P(r, "Quest"); return q != null && newbieIds.Contains(Iv(q, "Index")); }).ToList();
var delReqs = reqs.Where(r => { var q = P(r, "Quest"); return q != null && newbieIds.Contains(Iv(q, "Index")); }).ToList();
L($"related monDets={delMon.Count} tasks={delTasks.Count} rewards={delRewards.Count} reqs={delReqs.Count}");

// Clear NPC StartQuests/FinishQuests associations pointing to newbie (before delete)
int npcCleared = 0;
foreach (var n in npcs)
{
    foreach (var propName in new[] { "StartQuests", "FinishQuests" })
    {
        var coll = P(n, propName);
        if (coll is not IEnumerable en) continue;
        var toRemove = en.Cast<object>().Where(q => newbieIds.Contains(Iv(q, "Index"))).ToList();
        foreach (var q in toRemove)
        {
            // Association collections usually support Remove
            var rm = coll.GetType().GetMethod("Remove", new[] { q.GetType() })
                  ?? coll.GetType().GetMethod("Remove", new[] { typeof(object) })
                  ?? coll.GetType().GetMethods().FirstOrDefault(m => m.Name == "Remove" && m.GetParameters().Length == 1);
            if (rm != null)
            {
                if (doApply) rm.Invoke(coll, new[] { q });
                npcCleared++;
                L($"NPC clear {S(n,"NPCName")}#{Iv(n,"Index")} {propName} quest#{Iv(q,"Index")}");
            }
            else
            {
                // try set Quest.StartNPC / FinishNPC null via deleting quest later
                L($"NPC link {S(n,"NPCName")}#{Iv(n,"Index")} {propName} quest#{Iv(q,"Index")} (no Remove; rely on quest Delete)");
            }
        }
    }
}
L("npcClearedCalls=" + npcCleared);

if (doApply)
{
    foreach (var o in delMon) InvokeDelete(ses, o);
    foreach (var o in delTasks) InvokeDelete(ses, o);
    foreach (var o in delRewards) InvokeDelete(ses, o);
    foreach (var o in delReqs) InvokeDelete(ses, o);
    foreach (var o in newbie) InvokeDelete(ses, o);
    L("deleted quests + related rows");

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

    void CheckItem(int idx, int expectPrice, decimal expectRate)
    {
        var it = items2.First(x => Iv(x, "Index") == idx);
        L($"VERIFY ITEM {idx} {S(it,"ItemName")} Price={Iv(it,"Price")} SellRate={Dv(it,"SellRate")} sell={(long)(Iv(it,"Price")*Dv(it,"SellRate"))} expectPrice={expectPrice} expectSell={(long)(expectPrice*expectRate)}");
    }
    CheckItem(122584, 500, 1m);
    CheckItem(122585, 1, 1m);
    CheckItem(122586, 1, 1m);

    var g = mons2.First(x => S(x, "MonsterName") == "霸王守卫");
    var hs = monStats2.Where(s => Iv(P(s,"Monster"),"Index")==Iv(g,"Index") && Equals(P(s,"Stat"), healthStat)).ToList();
    foreach (var h in hs) L($"VERIFY MON Health={P(h,"Amount")}");

    var remainNewbie = quests2.Where(q => S(q, "QuestName").Contains("新手")).ToList();
    L($"VERIFY remainNewbie={remainNewbie.Count} totalQuests={quests2.Count}");

    // NPC broken links?
    int broken = 0;
    foreach (var n in npcs2)
    {
        foreach (var propName in new[] { "StartQuests", "FinishQuests" })
        {
            if (P(n, propName) is not IEnumerable en) continue;
            foreach (var q in en.Cast<object>())
            {
                if (q == null) { broken++; L($"BROKEN null quest on NPC {S(n,"NPCName")} {propName}"); continue; }
                var qid = Iv(q, "Index");
                if (!quests2.Any(x => Iv(x, "Index") == qid))
                { broken++; L($"BROKEN quest#{qid} on NPC {S(n,"NPCName")} {propName}"); }
            }
        }
    }
    L("VERIFY brokenNpcQuestLinks=" + broken);
    (ses2 as IDisposable)?.Dispose();

    // copy back
    foreach (var name in new[] { "System.db", "ClientSystem.db" })
    {
        File.Copy(Path.Combine(work, name), Path.Combine(root, "Database", name), true);
        var data = Path.Combine(root, "Data", name);
        if (File.Exists(Path.GetDirectoryName(data)!))
            File.Copy(Path.Combine(work, name), data, true);
        var deploy = Path.Combine(root, "deploy_to_Mir3service", "Database", name);
        if (Directory.Exists(Path.GetDirectoryName(deploy)!))
            File.Copy(Path.Combine(work, name), deploy, true);
    }
    L("copied to Database (+ Data/deploy if present)");
}

var reportPath = Path.Combine(toolDir, (doApply ? "apply_" : "dry_") + stamp + ".txt");
File.WriteAllText(reportPath, report.ToString(), Encoding.UTF8);
L("REPORT=" + reportPath);
return doApply ? 0 : 0;

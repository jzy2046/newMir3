using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Security.Cryptography;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3QuestFix <dry-run|apply>");
    return 1;
}
var apply = args[0] == "apply";
var root = @"D:\newMir3";
var deps = Path.Combine(root, "tools", "_deps");
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
object? RP(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
string RS(object? o, string n) => Convert.ToString(RP(o, n)) ?? "";
int RI(object? o, string n) { var v = RP(o, n); return v == null ? 0 : Convert.ToInt32(v); }
void SP(object o, string n, object? v) => o.GetType().GetProperty(n)!.SetValue(o, v);
string Hex16(string path) => Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(path)))[..16];
bool IsNewbie(string name) => name.Contains("新手任务", StringComparison.Ordinal);

void InvokeDelete(object session, object obj)
{
    var fast = sessionType.GetMethod("FastDelete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)
        ?? throw new InvalidOperationException("Session.FastDelete missing");
    fast.Invoke(session, new[] { obj });
    var collField = dbObjectType.GetField("_Collection", BindingFlags.Instance | BindingFlags.NonPublic)
        ?? throw new InvalidOperationException("_Collection missing");
    var coll = collField.GetValue(obj) ?? throw new InvalidOperationException("Collection null");
    var del = coll.GetType().GetMethod("Delete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)
        ?? throw new InvalidOperationException("Collection.Delete missing");
    del.Invoke(coll, new[] { obj });
}

object Open(string work)
{
    Directory.CreateDirectory(work);
    Directory.CreateDirectory(work + "_bak");
    var s = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(work + "_bak") });
    sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(s, null);
    sessionType.GetProperty("BackUp")!.SetValue(s, false);
    return s;
}

Type T(string n) => lib.GetType("Library.SystemModels." + n)!;
List<object> Coll(object ses, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(ses, null)!).Cast<object>().ToList();

var report = new StringBuilder();
var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var stampHuman = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
report.AppendLine("Mir3 Quest Fix (no-respawn delete + newbie StartNPC null delete + chain cleanup)");
report.AppendLine("mode=" + (apply ? "apply" : "dry-run"));
report.AppendLine("stamp=" + stampHuman + " (machine local Asia/Shanghai)");
report.AppendLine("db=D:\\newMir3\\Database\\System.db");

var bak = Path.Combine(root, "Database", "Backup_quest_fix_" + stamp);
if (apply)
{
    Directory.CreateDirectory(bak);
    foreach (var name in new[] { "System.db", "ClientSystem.db" })
    {
        var src = Path.Combine(root, "Database", name);
        if (File.Exists(src)) File.Copy(src, Path.Combine(bak, name), true);
    }
    report.AppendLine("backup=" + bak);
}

var work = Path.Combine(Path.GetTempPath(), "questfix-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);

var ses = Open(work);
var questT = T("QuestInfo");
var taskT = T("QuestTask");
var rewardT = T("QuestReward");
var reqT = T("QuestRequirement");
var monDetT = T("QuestTaskMonsterDetails");
var respawnT = T("RespawnInfo");
var itemT = T("ItemInfo");
var monT = T("MonsterInfo");
var npcT = T("NPCInfo");

var quests = Coll(ses, questT);
var tasks = Coll(ses, taskT);
var rewards = Coll(ses, rewardT);
var reqs = Coll(ses, reqT);
var monDets = Coll(ses, monDetT);
var respawns = Coll(ses, respawnT);
var items = Coll(ses, itemT);
var mons = Coll(ses, monT);
var npcs = Coll(ses, npcT);

report.AppendLine($"before quests={quests.Count} tasks={tasks.Count} rewards={rewards.Count} reqs={reqs.Count} monDets={monDets.Count}");

var monWithRespawn = new HashSet<int>();
foreach (var r in respawns)
{
    var m = RP(r, "Monster");
    if (m == null) continue;
    if (Convert.ToBoolean(RP(r, "EventSpawn") ?? false)) continue;
    monWithRespawn.Add(RI(m, "Index"));
}

var questByIdx = quests.ToDictionary(q => RI(q, "Index"));
var deleteIds = new HashSet<int>();
var deleteReasons = new Dictionary<int, string>();

void MarkDelete(int qid, string reason)
{
    if (!questByIdx.ContainsKey(qid)) return;
    deleteIds.Add(qid);
    deleteReasons[qid] = reason;
}

// Rule 1 explicit
foreach (var (qid, reason) in new[] {
    (5, "explicit: kill target 副本-赤月恶魔1 has no non-Event RespawnInfo"),
    (7, "explicit: kill target 副本-沃玛教主1 has no non-Event RespawnInfo"),
    (35, "explicit: kill target 副本-霸王教主1 has no non-Event RespawnInfo"),
}) MarkDelete(qid, reason);

// Rule 1 re-scan: quests whose kill targets ALL lack non-Event Respawn (and no GainItem/other completable tasks with valid targets)
foreach (var q in quests)
{
    var qid = RI(q, "Index");
    if (deleteIds.Contains(qid)) continue;
    var qTasks = tasks.Where(t => RP(t, "Quest") != null && RI(RP(t, "Quest")!, "Index") == qid).ToList();
    if (qTasks.Count == 0) continue;
    var dets = monDets.Where(d =>
    {
        var t = RP(d, "Task");
        return t != null && RP(t, "Quest") != null && RI(RP(t, "Quest")!, "Index") == qid;
    }).ToList();

    // only-kill-no-respawn: every task is KillMonster (or has mon dets), and every monDet monster lacks respawn (or null)
    bool hasGainOrOther = qTasks.Any(t =>
    {
        var kind = RS(t, "Task");
        if (kind == "GainItem")
        {
            var item = RP(t, "ItemParameter");
            return item != null; // valid collect
        }
        return kind is not ("KillMonster" or "Kill");
    });
    if (hasGainOrOther) continue;
    if (dets.Count == 0) continue; // kill with no mon dets = different issue; not this rule
    bool allNoRespawn = dets.All(d =>
    {
        var mon = RP(d, "Monster");
        if (mon == null) return true;
        return !monWithRespawn.Contains(RI(mon, "Index"));
    });
    if (allNoRespawn)
        MarkDelete(qid, "re-scan: all kill MonDets lack non-Event RespawnInfo (unfarmable-only)");
}

// Rule 2A: newbie with null/missing StartNPC
foreach (var q in quests)
{
    var qid = RI(q, "Index");
    if (deleteIds.Contains(qid)) continue;
    var name = RS(q, "QuestName");
    if (!IsNewbie(name)) continue;
    var sn = RP(q, "StartNPC");
    if (sn == null)
        MarkDelete(qid, "newbie: StartNPC is null");
    else
    {
        // missing from NPCInfo — association should still resolve if present; treat null Index-not-in-dict
        var snIdx = RI(sn, "Index");
        if (!npcs.Any(n => RI(n, "Index") == snIdx))
            MarkDelete(qid, $"newbie: StartNPC Index={snIdx} not in NPCInfo");
    }
}

// Explicit confirm 414-417
foreach (var qid in new[] { 414, 415, 416, 417 })
    MarkDelete(qid, deleteReasons.TryGetValue(qid, out var r) ? r : "newbie: StartNPC null (explicit PT1-5..PT1-8)");

report.AppendLine();
report.AppendLine("=== DELETED QUESTS (planned) ===");
var delQuests = quests.Where(q => deleteIds.Contains(RI(q, "Index"))).OrderBy(q => RI(q, "Index")).ToList();
foreach (var q in delQuests)
{
    var qid = RI(q, "Index");
    report.AppendLine($"DEL_QUEST [{qid}] {RS(q, "QuestName")} type={RS(q, "QuestType")} | {deleteReasons[qid]}");
}
report.AppendLine($"delete_quest_count={delQuests.Count}");

// Cascade children of deleted quests
var delMon = monDets.Where(d =>
{
    var t = RP(d, "Task");
    var q = t == null ? null : RP(t, "Quest");
    return q != null && deleteIds.Contains(RI(q, "Index"));
}).ToList();
var delTasks = tasks.Where(t => { var q = RP(t, "Quest"); return q != null && deleteIds.Contains(RI(q, "Index")); }).ToList();
var delRewards = rewards.Where(r => { var q = RP(r, "Quest"); return q != null && deleteIds.Contains(RI(q, "Index")); }).ToList();
var delReqsOwned = reqs.Where(r => { var q = RP(r, "Quest"); return q != null && deleteIds.Contains(RI(q, "Index")); }).ToList();

// Req links FROM surviving quests pointing TO deleted quests
var delReqsPointing = reqs.Where(r =>
{
    var reqType = RS(r, "Requirement");
    if (reqType is not ("NotAccepted" or "HaveCompleted" or "HaveNotCompleted")) return false;
    var qp = RP(r, "QuestParameter");
    if (qp == null) return false;
    var qpid = RI(qp, "Index");
    if (!deleteIds.Contains(qpid)) return false;
    // if owned by deleted quest already counted
    var owner = RP(r, "Quest");
    if (owner != null && deleteIds.Contains(RI(owner, "Index"))) return false;
    return true;
}).ToList();

report.AppendLine($"cascade monDets={delMon.Count} tasks={delTasks.Count} rewards={delRewards.Count} reqsOwned={delReqsOwned.Count} reqsPointingAtDeleted={delReqsPointing.Count}");

// Retarget: PT1-9 (418) HaveCompleted was 417 → set to 413 (PT1-4) to keep chain
object? req418 = null;
object? quest413 = questByIdx.TryGetValue(413, out var q413) ? q413 : null;
object? quest418 = questByIdx.TryGetValue(418, out var q418) ? q418 : null;
foreach (var r in delReqsPointing.ToList())
{
    var owner = RP(r, "Quest");
    var qp = RP(r, "QuestParameter");
    report.AppendLine($"REQ_POINTING_DELETED Req#{RI(r, "Index")} ownerQ={(owner == null ? "?" : RI(owner, "Index").ToString())} '{(owner == null ? "" : RS(owner, "QuestName"))}' {RS(r, "Requirement")} -> [{RI(qp!, "Index")}] {RS(qp!, "QuestName")}");
    if (owner != null && RI(owner, "Index") == 418 && RS(r, "Requirement") == "HaveCompleted" && qp != null && RI(qp, "Index") == 417 && quest413 != null)
    {
        req418 = r;
    }
}

var tasksRemoved = new List<string>();
var tasksReplaced = new List<string>();
var finishNpcFixed = new List<string>();
var newbieUntouched = new List<string>();

// Rule 2B/2C for remaining newbie quests (not deleted)
foreach (var q in quests.Where(q => IsNewbie(RS(q, "QuestName")) && !deleteIds.Contains(RI(q, "Index"))).OrderBy(q => RI(q, "Index")))
{
    var qid = RI(q, "Index");
    var name = RS(q, "QuestName");
    var sn = RP(q, "StartNPC");
    var fn = RP(q, "FinishNPC");
    var qTasks = tasks.Where(t => RP(t, "Quest") != null && RI(RP(t, "Quest")!, "Index") == qid).ToList();

    // C) FinishNPC null but StartNPC exists
    if (fn == null && sn != null)
    {
        finishNpcFixed.Add($"Q[{qid}] {name}: FinishNPC null -> set to StartNPC [{RI(sn, "Index")}] {RS(sn, "NPCName")}");
        if (apply) SP(q, "FinishNPC", sn);
    }

    // B) broken tasks
    var broken = new List<object>();
    var good = new List<object>();
    foreach (var t in qTasks)
    {
        var kind = RS(t, "Task");
        bool isBroken = false;
        string why = "";
        if (kind == "GainItem")
        {
            var item = RP(t, "ItemParameter");
            if (item == null) { isBroken = true; why = "GainItem ItemParameter=null"; }
            else if (!items.Any(i => RI(i, "Index") == RI(item, "Index"))) { isBroken = true; why = $"GainItem item#{RI(item, "Index")} missing ItemInfo"; }
        }
        else if (kind is "KillMonster" or "Kill")
        {
            var dets = monDets.Where(d => RP(d, "Task") != null && RI(RP(d, "Task")!, "Index") == RI(t, "Index")).ToList();
            if (dets.Count == 0) { isBroken = true; why = "KillMonster with no MonDet"; }
            else
            {
                // task broken if ALL its mon dets are null/missing/no-respawn
                bool anyFarmable = false;
                foreach (var d in dets)
                {
                    var mon = RP(d, "Monster");
                    if (mon == null) continue;
                    if (!mons.Any(m => RI(m, "Index") == RI(mon, "Index"))) continue;
                    if (monWithRespawn.Contains(RI(mon, "Index"))) anyFarmable = true;
                }
                if (!anyFarmable) { isBroken = true; why = "KillMonster all targets missing/null/no-respawn"; }
            }
        }
        if (isBroken) { broken.Add(t); tasksRemoved.Add($"Q[{qid}] {name} Task#{RI(t, "Index")} {kind}: {why}"); }
        else good.Add(t);
    }

    if (broken.Count > 0 && good.Count > 0)
    {
        // delete only broken tasks (+ their mon dets)
        foreach (var t in broken)
        {
            var tid = RI(t, "Index");
            foreach (var d in monDets.Where(d => RP(d, "Task") != null && RI(RP(d, "Task")!, "Index") == tid).ToList())
            {
                if (apply) InvokeDelete(ses, d);
                delMon.Remove(d);
            }
            if (apply) InvokeDelete(ses, t);
        }
    }
    else if (broken.Count > 0 && good.Count == 0)
    {
        // ALL broken → replace with valid early-game kill mirroring PT1-1 (deer 10001)
        var templateQ = questByIdx.TryGetValue(410, out var tq) ? tq : null;
        object? templateTask = null;
        object? templateDet = null;
        object? templateMon = null;
        if (templateQ != null)
        {
            templateTask = tasks.FirstOrDefault(t => RP(t, "Quest") != null && RI(RP(t, "Quest")!, "Index") == 410 && RS(t, "Task") == "KillMonster");
            if (templateTask != null)
                templateDet = monDets.FirstOrDefault(d => RP(d, "Task") != null && RI(RP(d, "Task")!, "Index") == RI(templateTask, "Index"));
            templateMon = templateDet == null ? null : RP(templateDet, "Monster");
        }
        if (templateMon == null)
            templateMon = mons.FirstOrDefault(m => RI(m, "Index") == 10001 && monWithRespawn.Contains(10001));

        // delete all broken tasks first
        foreach (var t in broken)
        {
            var tid = RI(t, "Index");
            foreach (var d in monDets.Where(d => RP(d, "Task") != null && RI(RP(d, "Task")!, "Index") == tid).ToList())
                if (apply) InvokeDelete(ses, d);
            if (apply) InvokeDelete(ses, t);
        }

        if (templateMon != null && apply)
        {
            var taskColl = get.MakeGenericMethod(taskT).Invoke(ses, null)!;
            var detColl = get.MakeGenericMethod(monDetT).Invoke(ses, null)!;
            var createTask = taskColl.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;
            var createDet = detColl.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;
            var nt = createTask.Invoke(taskColl, null)!;
            SP(nt, "Quest", q);
            // Task enum
            var taskEnumType = lib.GetType("Library.SystemModels.QuestTaskType") ?? nt.GetType().GetProperty("Task")!.PropertyType;
            SP(nt, "Task", Enum.Parse(taskEnumType, "KillMonster"));
            SP(nt, "Amount", 1);
            var nd = createDet.Invoke(detColl, null)!;
            SP(nd, "Task", nt);
            SP(nd, "Monster", templateMon);
            SP(nd, "Amount", 1);
            SP(nd, "Chance", templateDet != null ? RI(templateDet, "Chance") : 100);
            tasksReplaced.Add($"Q[{qid}] {name}: ALL tasks broken -> replaced with KillMonster x1 [{RI(templateMon, "Index")}] {RS(templateMon, "MonsterName")}");
        }
        else if (templateMon != null)
            tasksReplaced.Add($"Q[{qid}] {name}: ALL tasks broken -> WOULD replace with KillMonster x1 [{RI(templateMon, "Index")}] {RS(templateMon, "MonsterName")}");
        else
            tasksReplaced.Add($"Q[{qid}] {name}: ALL tasks broken -> FAILED to find replacement monster");
    }
    else
    {
        newbieUntouched.Add($"Q[{qid}] {name} StartNPC=[{(sn == null ? "?" : RI(sn, "Index").ToString())}]{(sn == null ? "" : RS(sn, "NPCName"))} tasks={qTasks.Count} OK");
    }
}

report.AppendLine();
report.AppendLine("=== TASKS REMOVED (broken only, quest kept) ===");
if (tasksRemoved.Count == 0) report.AppendLine("(none)");
foreach (var s in tasksRemoved) report.AppendLine(s);
report.AppendLine("=== TASKS REPLACED (old all-broken -> new) ===");
if (tasksReplaced.Count == 0) report.AppendLine("(none)");
foreach (var s in tasksReplaced) report.AppendLine(s);
report.AppendLine("=== FinishNPC FIXED ===");
if (finishNpcFixed.Count == 0) report.AppendLine("(none)");
foreach (var s in finishNpcFixed) report.AppendLine(s);
report.AppendLine($"=== NEWBIE LEFT UNTOUCHED ({newbieUntouched.Count}) ===");
foreach (var s in newbieUntouched) report.AppendLine(s);

if (!apply)
{
    // still note retarget plan
    if (req418 != null && quest413 != null)
        report.AppendLine($"RETARGET Req#{RI(req418, "Index")} Q418 HaveCompleted 417 -> 413 (dry-run)");
    else if (delReqsPointing.Any(r => { var o = RP(r, "Quest"); return o != null && RI(o, "Index") == 418; }))
        report.AppendLine("RETARGET planned for Q418 HaveCompleted -> 413");
    else
        report.AppendLine("RETARGET: no Q418 HaveCompleted->417 found (or already gone)");

    var dryPath = Path.Combine(root, "tools", "Mir3QuestFix", "dryrun_" + stamp + ".txt");
    File.WriteAllText(dryPath, report.ToString(), new UTF8Encoding(true));
    Console.WriteLine(report.ToString());
    Console.WriteLine("DRY=" + dryPath);
    (ses as IDisposable)?.Dispose();
    try { Directory.Delete(work, true); } catch { }
    try { Directory.Delete(work + "_bak", true); } catch { }
    return 0;
}

// APPLY deletes
int deletedCalls = 0;
foreach (var o in delMon) { InvokeDelete(ses, o); deletedCalls++; }
foreach (var o in delTasks) { InvokeDelete(ses, o); deletedCalls++; }
foreach (var o in delRewards) { InvokeDelete(ses, o); deletedCalls++; }
foreach (var o in delReqsOwned) { InvokeDelete(ses, o); deletedCalls++; }

// Retarget 418 before deleting pointing reqs
if (req418 != null && quest413 != null)
{
    var old = RP(req418, "QuestParameter");
    SP(req418, "QuestParameter", quest413);
    report.AppendLine($"RETARGET Req#{RI(req418, "Index")} Q418 HaveCompleted [{(old == null ? 0 : RI(old, "Index"))}] -> [413] {RS(quest413, "QuestName")}");
    delReqsPointing.Remove(req418);
}

foreach (var o in delReqsPointing) { InvokeDelete(ses, o); deletedCalls++; report.AppendLine($"DEL_REQ_POINTING Req#{RI(o, "Index")}"); }
foreach (var o in delQuests) { InvokeDelete(ses, o); deletedCalls++; }
report.AppendLine("deleted_calls=" + deletedCalls);

var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })
    ?? throw new InvalidOperationException("Save(bool, SessionMode) missing");
save.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();

// Verify + re-scan
var ses2 = Open(work);
var quests2 = Coll(ses2, questT);
var tasks2 = Coll(ses2, taskT);
var rewards2 = Coll(ses2, rewardT);
var reqs2 = Coll(ses2, reqT);
var monDets2 = Coll(ses2, monDetT);
var respawns2 = Coll(ses2, respawnT);
var items2 = Coll(ses2, itemT);
var mons2 = Coll(ses2, monT);
var npcs2 = Coll(ses2, npcT);
var maps2 = Coll(ses2, T("MapInfo"));
var regions2 = Coll(ses2, T("MapRegion"));

var monWithRespawn2 = new HashSet<int>();
foreach (var r in respawns2)
{
    var m = RP(r, "Monster");
    if (m == null) continue;
    if (Convert.ToBoolean(RP(r, "EventSpawn") ?? false)) continue;
    monWithRespawn2.Add(RI(m, "Index"));
}
var questByIdx2 = quests2.ToDictionary(q => RI(q, "Index"));
var npcByIdx2 = npcs2.ToDictionary(n => RI(n, "Index"));
var itemByIdx2 = items2.ToDictionary(i => RI(i, "Index"));
var monByIdx2 = mons2.ToDictionary(m => RI(m, "Index"));

var hardRows = new List<string>();
var softRows = new List<string>();
int hardStartNpcNull = 0;
int softNoRespawn = 0;

foreach (var q in quests2)
{
    var qid = RI(q, "Index");
    var qname = RS(q, "QuestName");
    var sn = RP(q, "StartNPC");
    if (sn == null) { hardRows.Add($"NPC/Start Q[{qid}] {qname}"); hardStartNpcNull++; }
    else if (!npcByIdx2.ContainsKey(RI(sn, "Index"))) hardRows.Add($"NPC/Start-missing Q[{qid}] {qname}");
    var fn = RP(q, "FinishNPC");
    if (fn == null) hardRows.Add($"NPC/Finish Q[{qid}] {qname}");
    else if (!npcByIdx2.ContainsKey(RI(fn, "Index"))) hardRows.Add($"NPC/Finish-missing Q[{qid}] {qname}");
}
foreach (var t in tasks2)
{
    var q = RP(t, "Quest");
    if (q == null) continue;
    if (RS(t, "Task") == "GainItem" && RP(t, "ItemParameter") == null)
        hardRows.Add($"Item/GainItem Q[{RI(q, "Index")}] Task#{RI(t, "Index")}");
}
foreach (var d in monDets2)
{
    var task = RP(d, "Task");
    var q = task == null ? null : RP(task, "Quest");
    if (q == null) continue;
    var mon = RP(d, "Monster");
    if (mon == null) hardRows.Add($"Monster/Kill-null Q[{RI(q, "Index")}] Det#{RI(d, "Index")}");
    else if (!monByIdx2.ContainsKey(RI(mon, "Index"))) hardRows.Add($"Monster/Kill-missing Q[{RI(q, "Index")}]");
    else if (!monWithRespawn2.Contains(RI(mon, "Index")))
    {
        softRows.Add($"Monster/NoRespawn Q[{RI(q, "Index")}] {RS(q, "QuestName")} mon=[{RI(mon, "Index")}] {RS(mon, "MonsterName")}");
        softNoRespawn++;
    }
}
foreach (var r in reqs2)
{
    var reqType = RS(r, "Requirement");
    if (reqType is not ("NotAccepted" or "HaveCompleted" or "HaveNotCompleted")) continue;
    var qp = RP(r, "QuestParameter");
    var q = RP(r, "Quest");
    if (qp == null) hardRows.Add($"Other/QuestReq-null Req#{RI(r, "Index")}");
    else if (!questByIdx2.ContainsKey(RI(qp, "Index")))
        hardRows.Add($"Other/QuestReq-missing Req#{RI(r, "Index")} {reqType} -> {RI(qp, "Index")} owner={(q == null ? "?" : RI(q, "Index").ToString())}");
}

report.AppendLine();
report.AppendLine("=== AFTER / RE-SCAN ===");
report.AppendLine($"after quests={quests2.Count} tasks={tasks2.Count} rewards={rewards2.Count} reqs={reqs2.Count} monDets={monDets2.Count}");
report.AppendLine($"gone_check Q5={!questByIdx2.ContainsKey(5)} Q7={!questByIdx2.ContainsKey(7)} Q35={!questByIdx2.ContainsKey(35)} Q414={!questByIdx2.ContainsKey(414)} Q415={!questByIdx2.ContainsKey(415)} Q416={!questByIdx2.ContainsKey(416)} Q417={!questByIdx2.ContainsKey(417)}");
report.AppendLine($"hard_refs={hardRows.Count} soft_NoRespawn={softNoRespawn} hard_StartNPC_null={hardStartNpcNull}");
report.AppendLine("=== HARD rows (first 80) ===");
foreach (var s in hardRows.Take(80)) report.AppendLine("  " + s);
if (hardRows.Count > 80) report.AppendLine($"  ... +{hardRows.Count - 80} more");
report.AppendLine("=== SOFT NoRespawn (first 40) ===");
foreach (var s in softRows.Take(40)) report.AppendLine("  " + s);
if (softRows.Count > 40) report.AppendLine($"  ... +{softRows.Count - 40} more");

// Q418 chain check
if (questByIdx2.TryGetValue(418, out var q418b))
{
    foreach (var r in reqs2.Where(r => RP(r, "Quest") != null && RI(RP(r, "Quest")!, "Index") == 418))
        report.AppendLine($"Q418 Req#{RI(r, "Index")} {RS(r, "Requirement")} qp={(RP(r, "QuestParameter") == null ? "null" : $"[{RI(RP(r, "QuestParameter")!, "Index")}] {RS(RP(r, "QuestParameter")!, "QuestName")}")}");
}

(ses2 as IDisposable)?.Dispose();

// Sync System.db to Database + Data (primary). ClientSystem: only if Save rewrote; still copy System.db always.
foreach (var name in new[] { "System.db" })
{
    File.Copy(Path.Combine(work, name), Path.Combine(root, "Database", name), true);
    var dataDir = Path.Combine(root, "Data");
    if (Directory.Exists(dataDir))
        File.Copy(Path.Combine(work, name), Path.Combine(dataDir, name), true);
}
// ClientSystem: check whether quest tables live there by comparing size change; still sync Database ClientSystem from work (Save may touch it) but note quests usually server-only
File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(root, "Database", "ClientSystem.db"), true);
var dataCli = Path.Combine(root, "Data", "ClientSystem.db");
if (File.Exists(dataCli))
    File.Copy(Path.Combine(work, "ClientSystem.db"), dataCli, true);

report.AppendLine();
report.AppendLine("=== SYNCED ===");
report.AppendLine("Database\\System.db sha=" + Hex16(Path.Combine(root, "Database", "System.db")));
report.AppendLine("Data\\System.db sha=" + Hex16(Path.Combine(root, "Data", "System.db")));
report.AppendLine("Database\\ClientSystem.db sha=" + Hex16(Path.Combine(root, "Database", "ClientSystem.db")));
report.AppendLine("note: quests live in server System.db; ClientSystem synced because Session.Save rewrites both work copies");

// optional mir3z
string? mir3z = null;
foreach (var hintName in new[] { "_mir3z_path.txt", "_mir3z_server_root.txt", "_mir3z_resolved.txt" })
{
    var hint = Path.Combine(root, "tools", hintName);
    if (!File.Exists(hint)) continue;
    var line = File.ReadAllText(hint, Encoding.UTF8).Trim().Trim('\uFEFF');
    if (Directory.Exists(line)) { mir3z = line; break; }
}
report.AppendLine("mir3zRoot=" + (mir3z ?? "(null)"));
if (mir3z != null)
{
    try
    {
        foreach (var cand in Directory.GetDirectories(mir3z, "Database", SearchOption.AllDirectories))
        {
            if (!File.Exists(Path.Combine(cand, "System.db"))) continue;
            if (cand.Contains("Backup_", StringComparison.OrdinalIgnoreCase)) continue;
            var sysLen = new FileInfo(Path.Combine(cand, "System.db")).Length;
            if (sysLen < 100_000) continue;
            File.Copy(Path.Combine(work, "System.db"), Path.Combine(cand, "System.db"), true);
            report.AppendLine("mir3z-synced " + Path.Combine(cand, "System.db"));
        }
    }
    catch (Exception ex) { report.AppendLine("mir3z-sync-skip: " + ex.Message); }
}

report.AppendLine("commit/push=NOT done (per instructions prefer leave files ready)");
report.AppendLine("NOTE: Server restart required to reload System.db");

var reportPath = Path.Combine(root, "_whitelist", "quest_fix_20260907.txt");
Directory.CreateDirectory(Path.GetDirectoryName(reportPath)!);
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(true));
var toolReport = Path.Combine(root, "tools", "Mir3QuestFix", "apply_report_" + stamp + ".txt");
File.WriteAllText(toolReport, report.ToString(), new UTF8Encoding(true));
Console.WriteLine(report.ToString());
Console.WriteLine("REPORT=" + reportPath);
try { Directory.Delete(work, true); } catch { }
try { Directory.Delete(work + "_bak", true); } catch { }
return 0;

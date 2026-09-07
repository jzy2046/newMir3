using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3DelFubenNpc <dry-run|apply>");
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
var dbObjectType = lib.GetType("MirDB.DBObject")!;
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
string Slash(string x) => Path.EndsInDirectorySeparator(x) ? x : x + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
bool Bv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v != null && Convert.ToBoolean(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);

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

var keepIndex = new HashSet<int> { 30, 5656 };

bool IsKeep(object n)
{
    var idx = Iv(n, "Index");
    var name = S(n, "NPCName");
    if (keepIndex.Contains(idx)) return true;
    if (name is "道馆精炼大师" or "义贤" or "万事通") return true;
    if (name is "宠物管理员" or "『宠物管理员』" or "图书管理员" or "沙巴克管理员") return true;
    if (name == "活动管理员") return true;
    if (name.Contains("死亡竞技")) return true;
    if (name.Contains("精炼")) return true;
    return false;
}

bool IsClearFuben(object n, out string reason)
{
    reason = "";
    if (IsKeep(n)) return false;
    var name = S(n, "NPCName");
    var file = S(n, "FileName");
    var region = P(n, "Region");
    var rdesc = S(region, "Description");
    var map = P(region, "Map");
    var mapDesc = S(map, "Description");
    var mapFile = S(map, "FileName");

    if (name.Contains("副本")) { reason = "name_has_fuben"; return true; }
    if ((rdesc.Contains("副本") || mapDesc.Contains("副本")) &&
        (name.Contains("管理员") || name.Contains("传送") || name.Contains("入口") || name.Contains("出口") || rdesc.Contains("副本NPC") || rdesc.Contains("副本管理")))
    {
        reason = "region_map_fuben_admin"; return true;
    }
    var dungeonAdmins = new[] {
        "蜈蚣巢穴管理员", "石阁庙管理员", "神舰管理员", "赤月管理员",
        "潘夜神殿管理员", "潘夜石窟管理员", "诺玛教主管理员",
        "诺玛遗址管理员", "赤月山谷管理员", "地下魔宫管理员",
        "幽灵船管理员", "沃玛宫殿管理员", "真天宫管理员",
        "祖玛宫殿管理员", "黑度宫管理员", "『荒村』副本管理员",
        "『活动管理员』阿珍"
    };
    if (dungeonAdmins.Any(x => name == x)) { reason = "known_dungeon_admin"; return true; }
    if (name.EndsWith("管理员") && (rdesc.Contains("副本") || mapDesc.Contains("副本")))
    { reason = "admin_on_fuben_region"; return true; }
    return false;
}

bool IsBorderline(object n, out string reason)
{
    reason = "";
    if (IsKeep(n)) return false;
    var region = P(n, "Region");
    var rdesc = S(region, "Description");
    var map = P(region, "Map");
    var mapDesc = S(map, "Description");
    if (rdesc.Contains("副本") || mapDesc.Contains("副本"))
    {
        reason = "on_fuben_map_not_admin";
        return true;
    }
    return false;
}

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
report.AppendLine($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");
report.AppendLine("scope=NPCInfo with fuben in name/region/map OR known dungeon-instance admins; cascade orphan MapRegion");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_fuben_npc_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
report.AppendLine("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-fuben-npc-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var npcType = lib.GetType("Library.SystemModels.NPCInfo")!;
var respawnType = lib.GetType("Library.SystemModels.RespawnInfo")!;
var moveType = lib.GetType("Library.SystemModels.MovementInfo")!;
var safeType = lib.GetType("Library.SystemModels.SafeZoneInfo")!;
var questType = lib.GetType("Library.SystemModels.QuestInfo")!;

var npcs = ListOf(ses, npcType);
var respawns = ListOf(ses, respawnType);
var moves = ListOf(ses, moveType);
var safes = ListOf(ses, safeType);
var quests = ListOf(ses, questType);

var targets = new List<object>();
var borderline = new List<(object n, string reason)>();
foreach (var n in npcs.OrderBy(x => Iv(x, "Index")))
{
    if (IsClearFuben(n, out var reason))
    {
        targets.Add(n);
        var region = P(n, "Region");
        var map = P(region, "Map");
        report.AppendLine($"HIT idx={Iv(n,"Index")} name={S(n,"NPCName")} file={S(n,"FileName")} region={Iv(region,"Index")}/{S(region,"Description")} map={S(map,"Description")} display={Bv(n,"Display")} reason={reason}");
    }
    else if (IsBorderline(n, out var br))
    {
        borderline.Add((n, br));
        var region = P(n, "Region");
        var map = P(region, "Map");
        report.AppendLine($"BORDERLINE idx={Iv(n,"Index")} name={S(n,"NPCName")} region={Iv(region,"Index")}/{S(region,"Description")} map={S(map,"Description")} reason={br}");
    }
}
report.AppendLine($"matched_npc_count={targets.Count}");
report.AppendLine($"borderline_count={borderline.Count}");
report.AppendLine("safety_admin30_present=" + npcs.Count(n => Iv(n, "Index") == 30));
report.AppendLine("safety_refine_present=" + npcs.Count(n => Iv(n, "Index") == 5656 || S(n, "NPCName").Contains("精炼大师")));

var toDelete = new List<(string kind, object obj, string detail)>();
var regionsToConsider = new List<object>();

foreach (var npc in targets)
{
    var name = S(npc, "NPCName");
    foreach (var q in quests)
    {
        if (ReferenceEquals(P(q, "StartNPC"), npc) || ReferenceEquals(P(q, "FinishNPC"), npc))
            report.AppendLine($"WARN quest links NPC idx={Iv(npc,"Index")} {name} questIdx={Iv(q,"Index")} {S(q,"QuestName")}");
    }
    var region = P(npc, "Region");
    var map = P(region, "Map");
    toDelete.Add(("NPCInfo", npc, $"idx={Iv(npc,"Index")} name={name} map={S(map,"Description")}"));
    if (region != null) regionsToConsider.Add(region);
}

foreach (var rr in regionsToConsider.Distinct())
{
    bool sharedNpc = npcs.Any(n => !targets.Contains(n) && ReferenceEquals(P(n, "Region"), rr));
    bool sharedRs = respawns.Any(r => ReferenceEquals(P(r, "Region"), rr));
    bool sharedMv = moves.Any(mv => ReferenceEquals(P(mv, "SourceRegion"), rr) || ReferenceEquals(P(mv, "DestinationRegion"), rr));
    bool sharedSz = safes.Any(sz => ReferenceEquals(P(sz, "Region"), rr) || ReferenceEquals(P(sz, "BindRegion"), rr));
    report.AppendLine($"npcRegion {Iv(rr,"Index")}/{S(rr,"Description")} sharedNpc={sharedNpc} sharedRs={sharedRs} sharedMv={sharedMv} sharedSz={sharedSz}");
    if (!sharedNpc && !sharedRs && !sharedMv && !sharedSz)
        toDelete.Add(("MapRegion(npc)", rr, $"idx={Iv(rr,"Index")} {S(rr,"Description")}"));
    else
        report.AppendLine($"  KEEP MapRegion {Iv(rr,"Index")} (shared)");
}

report.AppendLine("---- delete plan ----");
foreach (var g in toDelete.GroupBy(x => x.kind))
    report.AppendLine($"{g.Key}: {g.Count()}");
foreach (var (kind, obj, detail) in toDelete)
    report.AppendLine($"  DEL {kind} {detail}");

var toolDir = Path.Combine(root, "tools", "Mir3DelFubenNpc");
Directory.CreateDirectory(toolDir);
var reportPath = Path.Combine(toolDir, (doApply ? "apply_" : "dry_") + stamp + ".txt");
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));
Console.WriteLine(report.ToString());

if (!doApply)
{
    Console.WriteLine("dry-run only; report=" + reportPath);
    try { Directory.Delete(work, true); } catch { }
    try { Directory.Delete(workBak, true); } catch { }
    return 0;
}

int deletedCount = 0;
foreach (var (kind, obj, detail) in toDelete)
{
    InvokeDelete(ses, obj);
    deletedCount++;
}
var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
save.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();

File.Copy(Path.Combine(work, "System.db"), sysDb, true);
File.Copy(Path.Combine(work, "ClientSystem.db"), cliDb, true);

var dataSys = Path.Combine(root, "Data", "System.db");
var dataCli = Path.Combine(root, "Data", "ClientSystem.db");
if (File.Exists(dataSys)) File.Copy(sysDb, dataSys, true);
if (File.Exists(dataCli)) File.Copy(cliDb, dataCli, true);

report.AppendLine($"deleted_calls={deletedCount}");
report.AppendLine("saved System.db + ClientSystem.db (+ Data if present)");

var wl = Path.Combine(root, "_whitelist", "npc_fuben_deleted_" + DateTime.Now.ToString("yyyyMMdd") + ".txt");
var wlSb = new StringBuilder();
wlSb.AppendLine("# Deleted dungeon/instance NPCs " + stamp);
wlSb.AppendLine("# Index Name Map");
foreach (var (kind, obj, detail) in toDelete.Where(x => x.kind == "NPCInfo"))
    wlSb.AppendLine(detail);
wlSb.AppendLine();
wlSb.AppendLine("# Borderline kept (not deleted):");
foreach (var (n, br) in borderline)
{
    var region = P(n, "Region");
    var map = P(region, "Map");
    wlSb.AppendLine($"KEEP idx={Iv(n,"Index")} name={S(n,"NPCName")} map={S(map,"Description")} region={S(region,"Description")} reason={br}");
}
wlSb.AppendLine();
wlSb.AppendLine($"deleted_npc={toDelete.Count(x => x.kind == "NPCInfo")}");
wlSb.AppendLine($"deleted_region={toDelete.Count(x => x.kind.StartsWith("MapRegion"))}");
wlSb.AppendLine("backup=" + bakDir);
File.WriteAllText(wl, wlSb.ToString(), new UTF8Encoding(false));
report.AppendLine("whitelist=" + wl);
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));

Console.WriteLine($"APPLY OK deleted={deletedCount} report={reportPath} whitelist={wl}");
try { Directory.Delete(work, true); } catch { }
try { Directory.Delete(workBak, true); } catch { }
return 0;

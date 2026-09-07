using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3HideFubenNpc <dry-run|apply>");
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
void SetB(object o, string n, bool val) => o.GetType().GetProperty(n)!.SetValue(o, val);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var keepIndex = new HashSet<int> { 30, 224, 5656 };
var keepNames = new HashSet<string> { "\u9053\u9986\u7cbe\u70bc\u5927\u5e08", "\u4e49\u8d24", "\u4e07\u4e8b\u901a", "\u5ba0\u7269\u7ba1\u7406\u5458", "\u300e\u5ba0\u7269\u7ba1\u7406\u5458\u300f", "\u56fe\u4e66\u7ba1\u7406\u5458", "\u6c99\u5df4\u514b\u7ba1\u7406\u5458", "\u6d3b\u52a8\u7ba1\u7406\u5458" };
bool IsKeep(object n)
{
    var idx = Iv(n, "Index");
    var name = S(n, "NPCName");
    if (keepIndex.Contains(idx)) return true;
    if (keepNames.Contains(name)) return true;
    if (name.Contains("\u6b7b\u4ea1\u7ade\u6280")) return true;
    if (name.Contains("\u7cbe\u70bc")) return true;
    return false;
}

var known = new HashSet<string> { "\u8708\u86a3\u5de2\u7a74\u7ba1\u7406\u5458", "\u77f3\u9601\u5e99\u7ba1\u7406\u5458", "\u795e\u8230\u7ba1\u7406\u5458", "\u8d64\u6708\u7ba1\u7406\u5458", "\u6f58\u591c\u795e\u6bbf\u7ba1\u7406\u5458", "\u6f58\u591c\u77f3\u7a9f\u7ba1\u7406\u5458", "\u8bfa\u739b\u6559\u4e3b\u7ba1\u7406\u5458", "\u8bfa\u739b\u9057\u5740\u7ba1\u7406\u5458", "\u8d64\u6708\u5c71\u8c37\u7ba1\u7406\u5458", "\u5730\u4e0b\u9b54\u5bab\u7ba1\u7406\u5458", "\u5e7d\u7075\u8239\u7ba1\u7406\u5458", "\u6c83\u739b\u5bab\u6bbf\u7ba1\u7406\u5458", "\u771f\u5929\u5bab\u7ba1\u7406\u5458", "\u7956\u739b\u5bab\u6bbf\u7ba1\u7406\u5458", "\u9ed1\u5ea6\u5bab\u7ba1\u7406\u5458", "\u300e\u8352\u6751\u300f\u526f\u672c\u7ba1\u7406\u5458", "\u300e\u6d3b\u52a8\u7ba1\u7406\u5458\u300f\u963f\u73cd" };
var knownIdx = new HashSet<int> { 353, 379, 384, 385, 386, 387, 388, 389, 392 };

bool IsHideTarget(object n, out string reason)
{
    reason = "";
    if (IsKeep(n)) return false;
    var idx = Iv(n, "Index");
    var name = S(n, "NPCName");
    var region = P(n, "Region");
    var rdesc = S(region, "Description");
    var map = P(region, "Map");
    var mapDesc = S(map, "Description");

    if (knownIdx.Contains(idx)) { reason = "known_idx"; return true; }
    if (known.Contains(name)) { reason = "known_name"; return true; }
    if (name.Contains("\u526f\u672c") && name.Contains("\u7ba1\u7406")) { reason = "name_fuben_admin"; return true; }
    if (name.EndsWith("\u7ba1\u7406\u5458") && (rdesc.Contains("\u526f\u672c") || mapDesc.Contains("\u526f\u672c") || rdesc.Contains("\u526f\u672cNPC")))
    { reason = "admin_on_fuben"; return true; }
    if ((rdesc.Contains("\u526f\u672cNPC") || rdesc.Contains("\u526f\u672c\u7ba1\u7406")) && name.Contains("\u7ba1\u7406"))
    { reason = "region_fuben_admin"; return true; }
    return false;
}

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
report.AppendLine($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");
report.AppendLine("scope=hide dungeon/fuben admin NPCs via Display=True (CreateNPCs skips)");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_hide_fuben_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
report.AppendLine("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-hide-fuben-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var npcType = lib.GetType("Library.SystemModels.NPCInfo")!;
var npcs = ListOf(ses, npcType);

var targets = new List<object>();
foreach (var n in npcs.OrderBy(x => Iv(x, "Index")))
{
    if (!IsHideTarget(n, out var reason)) continue;
    targets.Add(n);
    var region = P(n, "Region");
    var map = P(region, "Map");
    report.AppendLine($"HIT idx={Iv(n,"Index")} name={S(n,"NPCName")} display={Bv(n,"Display")} map={S(map,"Description")} region={Iv(region,"Index")}/{S(region,"Description")} reason={reason}");
}
report.AppendLine($"matched_npc_count={targets.Count}");
report.AppendLine("safety_admin30_present=" + npcs.Count(n => Iv(n, "Index") == 30));
report.AppendLine("safety_refine_present=" + npcs.Count(n => Iv(n, "Index") == 5656 || S(n, "NPCName").Contains("\u7cbe\u70bc\u5927\u5e08")));
var n387 = npcs.FirstOrDefault(n => Iv(n, "Index") == 387);
report.AppendLine(n387 == null ? "probe_387=ABSENT" : $"probe_387=PRESENT name={S(n387,"NPCName")} display={Bv(n387,"Display")}");

foreach (var n in npcs.OrderBy(x => Iv(x, "Index")))
{
    var name = S(n, "NPCName");
    if (!name.Contains("\u7ba1\u7406")) continue;
    if (targets.Contains(n)) continue;
    var region = P(n, "Region");
    var map = P(region, "Map");
    report.AppendLine($"OTHER_ADMIN idx={Iv(n,"Index")} name={name} display={Bv(n,"Display")} map={S(map,"Description")} region={S(region,"Description")}");
}

var toolDir = Path.Combine(root, "tools", "Mir3HideFubenNpc");
Directory.CreateDirectory(toolDir);

if (!doApply)
{
    Console.WriteLine(report.ToString());
    Console.WriteLine("dry-run only");
    File.WriteAllText(Path.Combine(toolDir, "dry_" + stamp + ".txt"), report.ToString(), new UTF8Encoding(false));
    try { Directory.Delete(work, true); } catch { }
    try { Directory.Delete(workBak, true); } catch { }
    return 0;
}

int changed = 0;
foreach (var n in targets)
{
    var before = Bv(n, "Display");
    if (!before)
    {
        SetB(n, "Display", true);
        changed++;
    }
    report.AppendLine($"SET idx={Iv(n,"Index")} name={S(n,"NPCName")} Display {before} -> {Bv(n,"Display")}");
}

var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
save.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();

File.Copy(Path.Combine(work, "System.db"), sysDb, true);
File.Copy(Path.Combine(work, "ClientSystem.db"), cliDb, true);

void Sync(string dir, string label)
{
    if (!Directory.Exists(dir)) { report.AppendLine(label + " MISSING"); return; }
    File.Copy(sysDb, Path.Combine(dir, "System.db"), true);
    var c = Path.Combine(dir, "ClientSystem.db");
    if (File.Exists(c)) File.Copy(cliDb, c, true);
    report.AppendLine("synced " + label + "=" + dir);
}

Sync(Path.Combine(root, "Data"), "Data");
Sync(Path.Combine(root, "deploy_to_Mir3service", "Database"), "deploy_to_Mir3service/Database");

string? mir3zDb = null;
var resolved = Path.Combine(root, "tools", "_mir3z_resolved.txt");
if (File.Exists(resolved))
{
    var basePath = File.ReadAllText(resolved).Trim();
    var cand1 = Path.Combine(basePath, "\u670d\u52a1\u7aef", "Database");
    var cand2 = Path.Combine(basePath, "Database");
    if (File.Exists(Path.Combine(cand1, "System.db"))) mir3zDb = cand1;
    else if (File.Exists(Path.Combine(cand2, "System.db"))) mir3zDb = cand2;
}
if (mir3zDb != null) Sync(mir3zDb, "mir3z");
else report.AppendLine("mir3z Database NOT found/synced");

report.AppendLine($"changed_display={changed}");
report.AppendLine("APPLY OK");
var reportPath = Path.Combine(toolDir, "apply_" + stamp + ".txt");
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));
Console.WriteLine(report.ToString());
Console.WriteLine("report=" + reportPath);
try { Directory.Delete(work, true); } catch { }
try { Directory.Delete(workBak, true); } catch { }
return 0;

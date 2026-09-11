from pathlib import Path
Path(r"D:\newMir3\tools\Mir3Final_20260911\Program.cs").write_text(r'''using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;
Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
var deps = Path.Combine(root, "tools", "_deps");
AssemblyLoadContext.Default.Resolving += (_, a) => {
  foreach (var d in new[] { deps, root }) {
    var path = Path.Combine(d, (a.Name ?? "") + ".dll");
    if (File.Exists(path)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(path);
  }
  return null;
};
var lib = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root, "Library.dll"));
var sessionType = lib.GetType("MirDB.Session")!;
var modeType = lib.GetType("MirDB.SessionMode")!;
var toolMode = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
string Slash(string x) => Path.EndsInDirectorySeparator(x) ? x : x + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
bool Bv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v != null && Convert.ToBoolean(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void SetB(object o, string n, bool v) => o.GetType().GetProperty(n)!.SetValue(o, v);
void Del(object o) => o.GetType().GetMethod("Delete", Type.EmptyTypes)!.Invoke(o, null);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var mode = args.Length > 0 ? args[0] : "dry-run";
var doApply = mode == "apply";
var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L("mode=" + mode + " stamp=" + stamp);

var bakDir = Path.Combine(root, "Database", "Backup_final_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(bakDir, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-final-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);
var ses = ctor.Invoke(new object[] { toolMode, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

string wst = "\u4e07\u4e8b\u901a";
string weg = "\u6c83\u5c14\u9601";
string xbsm = "\u897f\u90e8\u6c99\u6f20";
string gj = "\u6302\u673a";

// CustomBuff 挂机
var buffT = lib.GetType("Library.SystemModels.CustomBuffInfo")!;
Console.WriteLine("CustomBuff props=" + string.Join(",", buffT.GetProperties().Select(p=>p.Name)));
var buffs = ListOf(ses, buffT);
foreach (var b in buffs.Where(x => S(x,"BuffName").Contains(gj) || Iv(x,"Index")==143)) {
  L($"BUFF before idx={Iv(b,"Index")} name={S(b,"BuffName")} props dump:");
  foreach (var pr in buffT.GetProperties()) {
    try { L($"  {pr.Name}={pr.GetValue(b)}"); } catch {}
  }
}

// Hide 万事通
var npcT = lib.GetType("Library.SystemModels.NPCInfo")!;
var npcs = ListOf(ses, npcT);
var wstNpcs = npcs.Where(x => S(x,"NPCName").Contains(wst)).ToList();
L($"万事通 count={wstNpcs.Count}");
foreach (var n in wstNpcs) {
  L($"  before idx={Iv(n,"Index")} name={S(n,"NPCName")} Display={Bv(n,"Display")}");
  if (doApply) { SetB(n, "Display", true); L($"  after Display={Bv(n,"Display")}"); }
}

// Hide/delete 沃尔阁
var wegNpcs = npcs.Where(x => S(x,"NPCName").Contains(weg)).ToList();
L($"沃尔阁 count={wegNpcs.Count}");
foreach (var n in wegNpcs) {
  L($"  before idx={Iv(n,"Index")} name={S(n,"NPCName")} Display={Bv(n,"Display")}");
  if (doApply) {
    // prefer delete if unique
    try { Del(n); L("  DELETED"); }
    catch (Exception ex) { SetB(n, "Display", true); L("  hide Display=True fallback err="+ex.Message); }
  }
}

// 西部沙漠 map + movements + spawns + npcs
var mapT = lib.GetType("Library.SystemModels.MapInfo")!;
var maps = ListOf(ses, mapT).Where(x => S(x,"Description") == xbsm || (S(x,"Description").Contains(xbsm) && S(x,"FileName")=="XS01")).ToList();
L($"西部沙漠 maps={maps.Count}");
foreach (var m in maps) L($"  MAP idx={Iv(m,"Index")} desc={S(m,"Description")} file={S(m,"FileName")}");

var moveT = lib.GetType("Library.SystemModels.MovementInfo")!;
var moves = ListOf(ses, moveT);
var westMoves = new List<object>();
foreach (var o in moves) {
  var dest = P(o, "DestinationRegion"); var src = P(o, "SourceRegion");
  var dm = P(dest, "Map"); var sm = P(src, "Map");
  if (S(dm,"Description")==xbsm || S(sm,"Description")==xbsm || S(dm,"FileName")=="XS01" || S(sm,"FileName")=="XS01")
    westMoves.Add(o);
}
L($"west movements={westMoves.Count}");
foreach (var o in westMoves) {
  var dest = P(o, "DestinationRegion"); var src = P(o, "SourceRegion");
  L($"  MOVE idx={Iv(o,"Index")} dest={S(P(dest,"Map"),"Description")}|{S(P(dest,"Map"),"FileName")} src={S(P(src,"Map"),"Description")}|{S(P(src,"Map"),"FileName")}");
}

var spawnT = lib.GetType("Library.SystemModels.RespawnInfo")!;
var westSpawns = new List<object>();
foreach (var o in ListOf(ses, spawnT)) {
  var region = P(o, "Region"); var map = P(region, "Map");
  if (S(map,"Description")==xbsm || S(map,"FileName")=="XS01") westSpawns.Add(o);
}
L($"west spawns={westSpawns.Count}");
foreach (var o in westSpawns.Take(30)) L($"  SPAWN idx={Iv(o,"Index")} mon={S(P(o,"Monster"),"MonsterName")}");

var westNpcs = new List<object>();
foreach (var o in npcs) {
  var region = P(o, "Region"); var map = P(region, "Map");
  if (S(map,"Description")==xbsm || S(map,"FileName")=="XS01") westNpcs.Add(o);
}
L($"west npcs={westNpcs.Count}");
foreach (var o in westNpcs) L($"  NPC idx={Iv(o,"Index")} name={S(o,"NPCName")}");

// MiniMap / SafeZone / etc?
foreach (var tn in new[]{"Library.SystemModels.SafeZoneInfo","Library.SystemModels.MiniMapRegion","Library.SystemModels.MapRegion","Library.SystemModels.QuestInfo","Library.SystemModels.NPCPage"}) {
  var t = lib.GetType(tn);
  L("type " + tn + " => " + (t?.FullName ?? "null"));
}

if (doApply) {
  // Delete west movements
  foreach (var o in westMoves.ToList()) { try { Del(o); L("DEL MOVE "+Iv(o,"Index")); } catch (Exception ex) { L("FAIL MOVE "+ex.Message); } }
  foreach (var o in westSpawns.ToList()) { try { Del(o); L("DEL SPAWN "+Iv(o,"Index")); } catch (Exception ex) { L("FAIL SPAWN "+ex.Message); } }
  foreach (var o in westNpcs.ToList()) { try { Del(o); L("DEL NPC "+Iv(o,"Index")); } catch (Exception ex) { SetB(o,"Display",true); L("HIDE NPC "+Iv(o,"Index")+" "+ex.Message); } }
  // Delete map last
  foreach (var m in maps.ToList()) { try { Del(m); L("DEL MAP "+Iv(m,"Index")); } catch (Exception ex) { L("FAIL MAP "+ex.Message+" -> try leave but unreachable"); } }
  // Delete AFK custom buff
  foreach (var b in buffs.Where(x => S(x,"BuffName").Contains(gj)).ToList()) {
    try { Del(b); L("DEL BUFF "+Iv(b,"Index")+" "+S(b,"BuffName")); }
    catch (Exception ex) { L("FAIL BUFF "+ex.Message); }
  }
  var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
  save.Invoke(ses, new object[] { true, toolMode });
  (ses as IDisposable)?.Dispose();
  File.Copy(Path.Combine(work, "System.db"), Path.Combine(root, "Database", "System.db"), true);
  File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(root, "Database", "ClientSystem.db"), true);
  foreach (var dest in new[] {
    Path.Combine(root, "Data", "System.db"),
    Path.Combine(root, "Data", "ClientSystem.db"),
    Path.Combine(root, "deploy_to_Mir3service", "Database", "System.db"),
    Path.Combine(root, "deploy_to_Mir3service", "Database", "ClientSystem.db"),
  }) {
    if (!File.Exists(Path.GetDirectoryName(dest)!)) continue;
    var src = dest.Contains("ClientSystem") ? Path.Combine(root, "Database", "ClientSystem.db") : Path.Combine(root, "Database", "System.db");
    if (File.Exists(Path.GetDirectoryName(dest)!)) {
      Directory.CreateDirectory(Path.GetDirectoryName(dest)!);
      File.Copy(src, dest, true);
      L("sync " + dest);
    }
  }
} else {
  (ses as IDisposable)?.Dispose();
}
File.WriteAllText(Path.Combine(root, "tools", "Mir3Final_20260911", mode.Replace("-","_") + "_" + stamp + ".txt"), report.ToString(), new UTF8Encoding(false));
L("DONE");
try { Directory.Delete(work, true); } catch {}
try { Directory.Delete(workBak, true); } catch {}
''', encoding='utf-8')
print('wrote apply Program.cs')

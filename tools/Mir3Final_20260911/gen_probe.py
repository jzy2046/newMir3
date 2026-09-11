from pathlib import Path
cs = r"""using System.Collections;
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
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var work = Path.Combine(Path.GetTempPath(), "mir3-probe-final-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);
var ses = ctor.Invoke(new object[] { toolMode, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);

string gj = "\u6302\u673a";
string wst = "\u4e07\u4e8b\u901a";
string weg = "\u6c83\u5c14\u9601";
string xbsm = "\u897f\u90e8\u6c99\u6f20";
string sha = "\u6c99\u6f20";

var npcT = lib.GetType("Library.SystemModels.NPCInfo")!;
var npcs = ListOf(ses, npcT);
Console.WriteLine("NPC total=" + npcs.Count);
foreach (var o in npcs.Where(x => S(x,"NPCName").Contains(wst) || S(x,"NPCName").Contains(weg))) {
  var region = P(o, "Region"); var map = P(region, "Map");
  Console.WriteLine($"NPC idx={Iv(o,"Index")} name={S(o,"NPCName")} Display={Bv(o,"Display")} map={S(map,"Description")}|{S(map,"FileName")} region={Iv(region,"Index")}");
}
var mapT = lib.GetType("Library.SystemModels.MapInfo")!;
var maps = ListOf(ses, mapT);
Console.WriteLine("MAP total=" + maps.Count);
foreach (var m in maps.Where(x => S(x,"Description").Contains(sha) || S(x,"Description").Contains(xbsm))) {
  Console.WriteLine($"MAP idx={Iv(m,"Index")} desc={S(m,"Description")} file={S(m,"FileName")}");
}
var itemT = lib.GetType("Library.SystemModels.ItemInfo")!;
foreach (var o in ListOf(ses, itemT).Where(x => S(x,"ItemName").Contains(gj))) {
  Console.WriteLine($"ITEM idx={Iv(o,"Index")} name={S(o,"ItemName")} type={S(o,"ItemType")}");
}
foreach (var tn in new[]{"Library.SystemModels.BuffInfo","Library.SystemModels.CustomBuffInfo","Library.SystemModels.MagicInfo"}) {
  var t = lib.GetType(tn);
  Console.WriteLine("type " + tn + " => " + (t?.FullName ?? "null"));
  if (t == null) continue;
  foreach (var o in ListOf(ses, t).Where(x => (S(x,"BuffName")+S(x,"Name")+S(x,"Description")+S(x,"MagicName")).Contains(gj))) {
    Console.WriteLine($"  HIT {tn} idx={Iv(o,"Index")} n={S(o,"BuffName")}|{S(o,"Name")}|{S(o,"MagicName")}|{S(o,"Description")}");
  }
}
var moveT = lib.GetType("Library.SystemModels.MovementInfo");
if (moveT != null) {
  Console.WriteLine("Movement props=" + string.Join(",", moveT.GetProperties().Select(p=>p.Name)));
  int hit=0;
  foreach (var o in ListOf(ses, moveT)) {
    var dest = P(o, "Destination") ?? P(o, "DestinationRegion") ?? P(o, "Region");
    var map = P(dest, "Map") ?? dest;
    var src = P(o, "Source") ?? P(o, "SourceRegion");
    var sm = P(src, "Map");
    if (S(map,"Description").Contains(xbsm) || S(sm,"Description").Contains(xbsm) || S(map,"Description").Contains(sha) || S(sm,"Description").Contains(sha)) {
      Console.WriteLine($"MOVE idx={Iv(o,"Index")} dest={S(map,"Description")}|{S(map,"FileName")} src={S(sm,"Description")}|{S(sm,"FileName")}");
      hit++;
    }
  }
  Console.WriteLine("movement_hits="+hit);
}
var spawnT = lib.GetType("Library.SystemModels.RespawnInfo");
if (spawnT != null) {
  Console.WriteLine("Respawn props=" + string.Join(",", spawnT.GetProperties().Select(p=>p.Name).Take(25)));
  int hit=0;
  foreach (var o in ListOf(ses, spawnT)) {
    var region = P(o, "Region") ?? P(o, "MapRegion");
    var map = P(region, "Map") ?? P(o, "Map");
    if (S(map,"Description").Contains(xbsm) || S(map,"Description").Contains(sha)) {
      if (hit < 40) Console.WriteLine($"SPAWN idx={Iv(o,"Index")} map={S(map,"Description")} mon={S(P(o,"Monster"),"MonsterName")}");
      hit++;
    }
  }
  Console.WriteLine("spawn_hits="+hit);
}
int nh=0;
foreach (var o in npcs) {
  var region = P(o, "Region"); var map = P(region, "Map");
  if (S(map,"Description").Contains(xbsm) || S(map,"Description").Contains(sha)) {
    Console.WriteLine($"NPC-DESERT idx={Iv(o,"Index")} name={S(o,"NPCName")} map={S(map,"Description")} Display={Bv(o,"Display")}");
    nh++;
  }
}
Console.WriteLine("npc_on_desert="+nh);
(ses as IDisposable)?.Dispose();
try { Directory.Delete(work, true); } catch {}
try { Directory.Delete(workBak, true); } catch {}
"""
Path(r"D:\newMir3\tools\Mir3Final_20260911\Program.cs").write_text(cs, encoding="utf-8")
print("ok", len(cs))

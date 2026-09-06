using System.Collections;
using System.Drawing;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;
Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
var deps = Path.Combine(root, "tools", "_deps");
AssemblyLoadContext.Default.Resolving += (_, a) => {
  foreach (var d in new[] { deps, root }) {
    var p = Path.Combine(d, (a.Name ?? "") + ".dll");
    if (File.Exists(p)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(p);
  }
  return null;
};
var lib = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root, "Library.dll"));
string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
var st = lib.GetType("MirDB.Session")!;
var sm = lib.GetType("MirDB.SessionMode")!;
var mode = Enum.Parse(sm, "ServerTool");
var work = Path.Combine(Path.GetTempPath(), "refnpc" + Guid.NewGuid().ToString("N")[..8]);
var bak = work + "_b"; Directory.CreateDirectory(work); Directory.CreateDirectory(bak);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);
var ctor = st.GetConstructor(new[] { sm, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var session = ctor.Invoke(new object[] { mode, new[] { lib }, false, "", Slash(work), Slash(bak) });
st.GetMethod("Init", Type.EmptyTypes)!.Invoke(session, null);
try { st.GetProperty("BackUp")!.SetValue(session, false); } catch { }
var get = st.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
object Col(Type t) => get.MakeGenericMethod(t).Invoke(session, null)!;
void Save() => st.GetMethod("Save", new[] { typeof(bool), sm })!.Invoke(session, new object[] { true, mode });

var mapT = lib.GetType("Library.SystemModels.MapInfo")!;
object? map7 = null;
foreach (var o in (IEnumerable)Col(mapT))
  if (Convert.ToInt32(o.GetType().GetProperty("Index")!.GetValue(o)) == 7) { map7 = o; break; }
if (map7 == null) throw new Exception("map7 missing");

var regT = lib.GetType("Library.SystemModels.MapRegion")!;
var regs = Col(regT);
object? region = null;
foreach (var o in (IEnumerable)regs) {
  var desc = o.GetType().GetProperty("Description")!.GetValue(o)?.ToString() ?? "";
  if (desc == "精炼大师") { region = o; break; }
}
if (region == null) {
  region = regs.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!.Invoke(regs, null)!;
  region.GetType().GetProperty("Map")!.SetValue(region, map7);
  region.GetType().GetProperty("Description")!.SetValue(region, "精炼大师");
  try { region.GetType().GetProperty("ServerDescription")!.SetValue(region, "精炼大师"); } catch { }
  region.GetType().GetProperty("PointRegion")!.SetValue(region, new Point[] { new Point(403, 133) });
  Console.WriteLine("created region #" + region.GetType().GetProperty("Index")!.GetValue(region));
} else {
  region.GetType().GetProperty("Map")!.SetValue(region, map7);
  region.GetType().GetProperty("PointRegion")!.SetValue(region, new Point[] { new Point(403, 133) });
  Console.WriteLine("updated region #" + region.GetType().GetProperty("Index")!.GetValue(region));
}

var npcT = lib.GetType("Library.SystemModels.NPCInfo")!;
var npcs = Col(npcT);
object? npc = null;
foreach (var o in ((IEnumerable)npcs).Cast<object>().ToList()) {
  var fn = o.GetType().GetProperty("NPCFile")?.GetValue(o)?.ToString() ?? "";
  var nn = o.GetType().GetProperty("NPCName")?.GetValue(o)?.ToString() ?? "";
  if (fn == "精炼大师" || nn == "精炼大师") { npc = o; break; }
}
if (npc == null) {
  npc = npcs.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!.Invoke(npcs, null)!;
  Console.WriteLine("creating npc");
}
npc.GetType().GetProperty("NPCName")!.SetValue(npc, "精炼大师");
npc.GetType().GetProperty("NPCFile")!.SetValue(npc, "精炼大师");
npc.GetType().GetProperty("Region")!.SetValue(npc, region);
npc.GetType().GetProperty("Image")!.SetValue(npc, 2);
npc.GetType().GetProperty("Display")!.SetValue(npc, false);
var npcIdx = Convert.ToInt32(npc.GetType().GetProperty("Index")!.GetValue(npc));
Console.WriteLine("NPC #" + npcIdx);
File.WriteAllText(Path.Combine(root, "tools", "_refine_npc_index.txt"), npcIdx.ToString(), new UTF8Encoding(false));

Save();
(session as IDisposable)?.Dispose();
File.Copy(Path.Combine(work, "System.db"), Path.Combine(root, "Database", "System.db"), true);
File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(root, "Database", "ClientSystem.db"), true);
var mz = File.ReadAllText(Path.Combine(root, "tools", "_mir3z_path.txt"), Encoding.UTF8).Trim();
foreach (var exe in Directory.GetFiles(mz, "Server.exe", SearchOption.AllDirectories)) {
  if (exe.Contains("\\Source\\") || exe.Contains("\\obj\\")) continue;
  var dir = Path.GetDirectoryName(exe)!;
  var mzSys = Path.Combine(dir, "Database", "System.db");
  if (!File.Exists(mzSys)) continue;
  File.Copy(Path.Combine(work, "System.db"), mzSys, true);
  var mzCli = Path.Combine(dir, "Database", "ClientSystem.db");
  if (File.Exists(mzCli)) File.Copy(Path.Combine(work, "ClientSystem.db"), mzCli, true);
  // also client folders ClientSystem
  Console.WriteLine("synced " + mzSys);
  break;
}
Console.WriteLine("OK");

// Run on Jon2046 from a net8 console next to Library.dll, OR:
//   cd D:\newMir3\tools\Mir3HorseSplit && dotnet new console -n ApplyHorseSplit -f net8.0 --force
//   copy this file over Program.cs, reference ..\..\Library.dll, then dotnet run
using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;
Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
if (!Directory.Exists(root)) root = Directory.GetCurrentDirectory();
while (root != null && !File.Exists(Path.Combine(root, "Library.dll")))
  root = Directory.GetParent(root)?.FullName;
if (root == null || !File.Exists(Path.Combine(root, "Library.dll")))
  throw new Exception("Library.dll not found; run under D:\\newMir3");
var deps = Path.Combine(root, "tools", "_deps");
AssemblyLoadContext.Default.Resolving += (_, a) => {
  foreach (var d in new[] { deps, root }) {
    var p = Path.Combine(d, (a.Name ?? "") + ".dll");
    if (File.Exists(p)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(p);
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
void Set(object o, string n, object? v) => o.GetType().GetProperty(n)!.SetValue(o, v);
List<object> ListOf(object ses, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(ses, null)!).Cast<object>().ToList();

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var bak = Path.Combine(root, "Database", "Backup_horse_split_" + stamp);
Directory.CreateDirectory(bak);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(bak, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(bak, "ClientSystem.db"), true);
Console.WriteLine("backup=" + bak);

var work = Path.Combine(Path.GetTempPath(), "hs" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work); Directory.CreateDirectory(work + "_b");
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);
var ses = ctor.Invoke(new object[] { toolMode, new[] { lib }, false, "", Slash(work), Slash(work + "_b") });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
try { sessionType.GetProperty("BackUp")!.SetValue(ses, false); } catch {}

var monT = lib.GetType("Library.SystemModels.MonsterInfo")!;
var monStatT = lib.GetType("Library.SystemModels.MonsterInfoStat")!;
var itemT = lib.GetType("Library.SystemModels.ItemInfo")!;
var flagType = lib.GetTypes().First(t => t.Name == "MonsterFlag" && t.IsEnum);
var statType = lib.GetTypes().First(t => t.Name == "Stat" && t.IsEnum);
object Flag(string name) => Enum.Parse(flagType, name);
object StatE(string name) => Enum.Parse(statType, name);

var mons = ListOf(ses, monT);
var items = ListOf(ses, itemT);

// 绝影战马 #100035 -> DiyHorse1
var monWar = mons.First(m => Iv(m, "Index") == 100035 || S(m, "MonsterName") == "绝影战马");
Set(monWar, "Flag", Flag("DiyHorse1"));
Set(monWar, "MonsterName", "绝影战马");
Console.WriteLine($"DiyHorse1 <= #{Iv(monWar,"Index")}");

// 给宝贝的马 DiyHorse2
mons = ListOf(ses, monT);
var monBaby = mons.FirstOrDefault(m => Convert.ToString(m.GetType().GetProperty("Flag")?.GetValue(m)) == "DiyHorse2" || S(m, "MonsterName") == "给宝贝的马");
if (monBaby == null) {
  var coll = get.MakeGenericMethod(monT).Invoke(ses, null)!;
  monBaby = coll.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!.Invoke(coll, null)!;
  Console.WriteLine("created #" + Iv(monBaby, "Index"));
}
Set(monBaby!, "Flag", Flag("DiyHorse2"));
Set(monBaby!, "MonsterName", "给宝贝的马");
try { Set(monBaby!, "ViewRange", 7); } catch {}

var monStats = ListOf(ses, monStatT);
var babyIdx = Iv(monBaby!, "Index");
foreach (var ms in monStats.Where(ms => {
  var m = ms.GetType().GetProperty("Monster")?.GetValue(ms);
  return m != null && Iv(m, "Index") == babyIdx;
}).ToList()) {
  try { ms.GetType().GetMethod("Delete")?.Invoke(ms, null); } catch {}
}
var babyStats = new Dictionary<string, int> {
  ["Comfort"] = 15, ["BagWeight"] = 1200,
  ["MinAC"] = 12, ["MaxAC"] = 12, ["MinMR"] = 12, ["MaxMR"] = 12,
  ["MinDC"] = 12, ["MaxDC"] = 12, ["MinMC"] = 12, ["MaxMC"] = 12,
  ["MinSC"] = 12, ["MaxSC"] = 12, ["TeleportRing"] = 1, ["DropRate"] = 150,
};
var statColl = get.MakeGenericMethod(monStatT).Invoke(ses, null)!;
var statCreate = statColl.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;
foreach (var kv in babyStats) {
  var ms = statCreate.Invoke(statColl, null)!;
  Set(ms, "Monster", monBaby);
  Set(ms, "Stat", StatE(kv.Key));
  Set(ms, "Amount", kv.Value);
}

// Item Shape wiring
var packJY = items.First(x => Iv(x, "Index") == 122637 || S(x, "ItemName") == "绝影战马礼包");
Set(packJY, "Shape", 68); Set(packJY, "Image", 1344);
var packBaby = items.First(x => Iv(x, "Index") == 122638 || S(x, "ItemName") == "给宝贝的马礼包");
Set(packBaby, "Shape", 69); Set(packBaby, "Image", 1344);
try { Set(packBaby, "Description", "使用后获得给宝贝的马（替换当前坐骑，属性独立于给亲友的红马）"); } catch {}

mons = ListOf(ses, monT);
foreach (var want in new[] { "BlackHorse", "RedHorse", "DiyHorse1", "DiyHorse2" }) {
  var hit = mons.Where(m => Convert.ToString(m.GetType().GetProperty("Flag")?.GetValue(m)) == want).OrderBy(m => Iv(m, "Index")).FirstOrDefault();
  Console.WriteLine($"WIN {want} => {(hit == null ? "NULL" : $"#{Iv(hit,"Index")} {S(hit,"MonsterName")}")}");
}

var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType }) ?? sessionType.GetMethod("Save", new[] { typeof(bool) });
if (save!.GetParameters().Length == 2) save.Invoke(ses, new object[] { true, toolMode });
else save.Invoke(ses, new object[] { true });
(ses as IDisposable)?.Dispose();

File.Copy(Path.Combine(work, "System.db"), Path.Combine(root, "Database", "System.db"), true);
File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(root, "Database", "ClientSystem.db"), true);
foreach (var dest in new[] {
  Path.Combine(root, "Data", "System.db"), Path.Combine(root, "Data", "ClientSystem.db"),
  Path.Combine(root, "deploy_to_Mir3service", "Database", "System.db"),
  Path.Combine(root, "deploy_to_Mir3service", "Database", "ClientSystem.db"),
  Path.Combine(@"D:\Mir3Source", "145Client", "Data", "ClientSystem.db"),
}) {
  var dir = Path.GetDirectoryName(dest)!;
  if (!Directory.Exists(dir)) continue;
  if (dest.Contains("Mir3Source") && !dest.Contains("ClientSystem")) continue;
  var src = dest.Contains("ClientSystem") ? Path.Combine(root, "Database", "ClientSystem.db") : Path.Combine(root, "Database", "System.db");
  File.Copy(src, dest, true);
  Console.WriteLine("sync " + dest);
}
try { Directory.Delete(work, true); } catch {}
try { Directory.Delete(work + "_b", true); } catch {}

// Patch Scripts
var script = Path.Combine(root, "Scripts", "Player", "事件触发", "物品使用.py");
var py = File.ReadAllText(script, Encoding.UTF8);
if (!py.Contains("HorseType.DiyHorse1")) {
  py = py.Replace("Sender.Character.Horse = HorseType.Black\n\t\t\tSender.RemoveMount()\n\t\t\tSender.RefreshStats()\n\t\t\tSender.Mount()\n\t\t\tSender.Connection.ReceiveChat('获得绝影战马",
                  "Sender.Character.Horse = HorseType.DiyHorse1\n\t\t\tSender.RemoveMount()\n\t\t\tSender.RefreshStats()\n\t\t\tSender.Mount()\n\t\t\tSender.Connection.ReceiveChat('获得绝影战马");
}
if (!py.Contains("Shape == 69")) {
  var needle = "\telif(Item.Info.Shape == 67):";
  var block = "\telif(Item.Info.Shape == 69): #给宝贝的马礼包 -> DiyHorse2\n\t\tSender.Character.Horse = HorseType.DiyHorse2\n\t\tSender.RemoveMount()\n\t\tSender.RefreshStats()\n\t\tSender.Mount()\n\t\tSender.Connection.ReceiveChat('获得给宝贝的马（已替换原坐骑）', MessageType.System)\n\t\treturn True\n" + needle;
  // try tab variants
  if (py.Contains("\t\telif(Item.Info.Shape == 67):")) {
    needle = "\t\telif(Item.Info.Shape == 67):";
    block = "\t\telif(Item.Info.Shape == 69): #给宝贝的马礼包 -> DiyHorse2\n\t\t\tSender.Character.Horse = HorseType.DiyHorse2\n\t\t\tSender.RemoveMount()\n\t\t\tSender.RefreshStats()\n\t\t\tSender.Mount()\n\t\t\tSender.Connection.ReceiveChat('获得给宝贝的马（已替换原坐骑）', MessageType.System)\n\t\t\treturn True\n" + needle;
  }
  if (!py.Contains(needle)) throw new Exception("Shape 67 needle missing for Shape 69 insert");
  py = py.Replace(needle, block, 1);
}
File.WriteAllText(script, py, new UTF8Encoding(encoderShouldEmitUTF8Identifier: false));
var dep = Path.Combine(root, "deploy_to_Mir3service", "Scripts", "Player", "事件触发", "物品使用.py");
if (Directory.Exists(Path.GetDirectoryName(dep)!)) {
  Directory.CreateDirectory(Path.GetDirectoryName(dep)!);
  File.Copy(script, dep, true);
}
Console.WriteLine("scripts patched");
Console.WriteLine("DONE — also apply tools/Mir3HorseSplit/patch_HorseFrame.cs.txt in Mir3Source client for black/red looks");

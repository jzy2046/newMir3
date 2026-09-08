# -*- coding: utf-8 -*-
import base64, pathlib
# Minimal batch2 C# - Chinese as \u escapes only in the generated C#
cs = r'''using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;
Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply")) { Console.Error.WriteLine("usage: batch2 <dry-run|apply>"); return 1; }
var doApply = args[0] == "apply";
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
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
string Slash(string x) => Path.EndsInDirectorySeparator(x) ? x : x + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void Set(object o, string n, object? val) => o.GetType().GetProperty(n)!.SetValue(o, val);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();
var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L($"mode={(doApply?"apply":"dry-run")} stamp={stamp}");
var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_req20260908_batch2_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);
var work = Path.Combine(Path.GetTempPath(), "mir3-b2-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work); Directory.CreateDirectory(work+"_bak");
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);
var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(work+"_bak") });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);
var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var magicType = lib.GetType("Library.SystemModels.MagicInfo")!;
var storeType = lib.GetType("Library.SystemModels.StoreInfo")!;
var effectEnum = lib.GetTypes().First(t => t.Name == "ItemEffect" && t.IsEnum);
var items = ListOf(ses, itemType);
var magics = ListOf(ses, magicType);
var stores = ListOf(ses, storeType);
int changes = 0;
string NTianNu = "\u5929\u4e4b\u6012\u706b"; // 天之怒火
string NTianNu2 = "\u5929\u6012\u4e4b\u706b"; // 天怒之火
string NNuHuo = "\u6012\u706b"; // 怒火
string NTian = "\u5929"; // 天
string NGarnet = "\u77f3\u69b4\u77f3"; // 石榴石
string NJing = "\u7ed3\u6676\u77f3"; // 结晶石
string NSnow = "\u4e07\u5e74\u96ea\u971c"; // 万年雪霜
foreach (var mg in magics) {
  var name = S(mg, "Name");
  if (!(name == NTianNu || name == NTianNu2 || (name.Contains(NNuHuo) && name.Contains(NTian)))) continue;
  var desc = S(mg, "Description");
  L($"MAGIC Clear name=[{name}] descLen={desc.Length}");
  if (doApply && !string.IsNullOrEmpty(desc)) { Set(mg, "Description", ""); changes++; }
}
var crystalEff = Enum.Parse(effectEnum, "Crystal");
var garnet = items.FirstOrDefault(x => S(x, "ItemName") == NGarnet);
L($"garnet={(garnet==null?"MISS":$"idx={Iv(garnet,"Index")} Effect={S(garnet,"Effect")}")}");
if (garnet != null) {
  L($"SET garnet Effect {S(garnet,"Effect")} -> Crystal");
  if (doApply) { Set(garnet, "Effect", crystalEff); changes++; }
}
var jing = items.FirstOrDefault(x => S(x, "ItemName") == NJing);
L($"jing={(jing==null?"MISS":$"idx={Iv(jing,"Index")} Effect={S(jing,"Effect")}")}");
MethodInfo? FindCreate(Type t) {
  var col = get.MakeGenericMethod(t).Invoke(ses, null)!;
  return col.GetType().GetMethods().FirstOrDefault(mi => mi.Name == "CreateNewObject" && mi.GetParameters().Length == 0);
}
if (jing == null && garnet != null) {
  var create = FindCreate(itemType);
  L($"Create ItemInfo={create!=null}");
  if (doApply && create != null) {
    var col = get.MakeGenericMethod(itemType).Invoke(ses, null)!;
    var it = create.Invoke(col, null)!;
    Set(it, "ItemName", NJing);
    Set(it, "ItemType", P(garnet, "ItemType")!);
    Set(it, "Effect", crystalEff);
    Set(it, "StackSize", Iv(garnet, "StackSize") > 0 ? Iv(garnet, "StackSize") : 999);
    Set(it, "Price", Iv(garnet, "Price"));
    Set(it, "Weight", Math.Max(1, Iv(garnet, "Weight")));
    Set(it, "Image", Iv(garnet, "Image"));
    Set(it, "Durability", Iv(garnet, "Durability"));
    Set(it, "Shape", Iv(garnet, "Shape"));
    foreach (var pn in new[]{"CanSell","CanStore","CanTrade","CanDrop","CanDeathDrop","CanTreasure"})
      if (it.GetType().GetProperty(pn)!=null && garnet.GetType().GetProperty(pn)!=null)
        Set(it, pn, P(garnet, pn)!);
    L($"CREATED jing idx={Iv(it,"Index")} Effect={S(it,"Effect")} Stack={S(it,"StackSize")} Image={S(it,"Image")}");
    changes++;
  }
} else if (jing != null) {
  L($"SET jing Effect {S(jing,"Effect")} -> Crystal");
  if (doApply) { Set(jing, "Effect", crystalEff); changes++; }
}
foreach (var sh in stores.Where(s => S(P(s,"Item"),"ItemName")==NSnow))
  L($"STORE snow idx={Iv(sh,"Index")} Price={S(sh,"Price")} Avail={S(sh,"Available")} itemStack={S(P(sh,"Item"),"StackSize")}");
L($"changes={changes}");
if (!doApply) {
  File.WriteAllText(Path.Combine(root,"tools","Mir3Req20260908","dry_batch2_"+stamp+".txt"), report.ToString(), new UTF8Encoding(false));
  (ses as IDisposable)?.Dispose();
  return 0;
}
var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
save.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();
File.Copy(Path.Combine(work,"System.db"), sysDb, true);
File.Copy(Path.Combine(work,"ClientSystem.db"), cliDb, true);
void Sync(string dir, string label) {
  if (!Directory.Exists(dir)) { L(label+" MISSING"); return; }
  File.Copy(sysDb, Path.Combine(dir,"System.db"), true);
  var c=Path.Combine(dir,"ClientSystem.db");
  if (File.Exists(c)) File.Copy(cliDb, c, true);
  L("synced "+label+"="+dir);
}
Sync(Path.Combine(root,"Data"),"Data");
Sync(Path.Combine(root,"deploy_to_Mir3service","Database"),"deploy_to_Mir3service/Database");
File.WriteAllText(Path.Combine(root,"tools","Mir3Req20260908","apply_batch2_"+stamp+".txt"), report.ToString(), new UTF8Encoding(false));
L("APPLIED ok changes="+changes);
return 0;
'''
pathlib.Path(r'tools/Mir3Req20260908/Batch2App/Program.cs').write_text(cs, encoding='utf-8')
print('wrote Program.cs', len(cs))

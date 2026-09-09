using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Security.Cryptography;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
var toolRoot = Path.Combine(root, "tools", "Mir3ShipAllowTT");
var deps = Path.Combine(root, "tools", "_deps");
Directory.CreateDirectory(toolRoot);

AssemblyLoadContext.Default.Resolving += (_, a) =>
{
    foreach (var d in new[] { deps, root })
    {
        var pth = Path.Combine(d, (a.Name ?? "") + ".dll");
        if (File.Exists(pth)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(pth);
    }
    return null;
};

var lib = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root, "Library.dll"));
var sessionType = lib.GetType("MirDB.Session")!;
var modeType = lib.GetType("MirDB.SessionMode")!;
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
var mapType = lib.GetType("Library.SystemModels.MapInfo")!;

string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
object? Prop(object o, string n) => o.GetType().GetProperty(n)?.GetValue(o);
void SetProp(object o, string n, object? v)
{
    var pr = o.GetType().GetProperty(n);
    if (pr == null || !pr.CanWrite) return;
    try
    {
        var t = Nullable.GetUnderlyingType(pr.PropertyType) ?? pr.PropertyType;
        if (v != null && t.IsEnum && v is not Enum) pr.SetValue(o, Enum.Parse(t, v.ToString()!));
        else if (v != null && t != typeof(string) && t.IsValueType && v.GetType() != t) pr.SetValue(o, Convert.ChangeType(v, t));
        else pr.SetValue(o, v);
    }
    catch { }
}
string Hex16(string path) => Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(path)))[..16];

object Open(string workDir)
{
    Directory.CreateDirectory(workDir);
    Directory.CreateDirectory(workDir + "_bak");
    var s = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(workDir), Slash(workDir + "_bak") });
    sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(s, null);
    try { sessionType.GetProperty("BackUp")!.SetValue(s, false); } catch { }
    return s;
}
List<object> Coll(object s, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(s, null)!).Cast<object>().ToList();

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
report.AppendLine("Mir3ShipAllowTT " + stamp);

// Backup Database + Data System.db
var bakDir = Path.Combine(root, "Database", "Backup_shipAllowTT_" + stamp);
Directory.CreateDirectory(bakDir);
foreach (var name in new[] { "System.db", "ClientSystem.db" })
{
    var src = Path.Combine(root, "Database", name);
    if (File.Exists(src)) File.Copy(src, Path.Combine(bakDir, name), true);
}
var dataBakDir = Path.Combine(root, "Data", "Backup_shipAllowTT_" + stamp);
Directory.CreateDirectory(dataBakDir);
foreach (var name in new[] { "System.db", "ClientSystem.db" })
{
    var src = Path.Combine(root, "Data", name);
    if (File.Exists(src)) File.Copy(src, Path.Combine(dataBakDir, name), true);
}
report.AppendLine("backupDir=" + bakDir);
report.AppendLine("dataBakDir=" + dataBakDir);

// Work on a temp copy of Database
var work = Path.Combine(Path.GetTempPath(), "ship-tt-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
var cliSrc = Path.Combine(root, "Database", "ClientSystem.db");
if (File.Exists(cliSrc)) File.Copy(cliSrc, Path.Combine(work, "ClientSystem.db"), true);

var ses = Open(work);
var maps = Coll(ses, mapType);
report.AppendLine("mapsTotal=" + maps.Count);

// 神舰
string shipKey = "\u795e\u8230";
string[] extraKeys = { "\u795e\u79d8\u8239", "MysteryShip", "mysteries", "Mystery", "ShenJian", "shenjian" };
// Known mystery-ship related MapInfo indexes if Description lacks keyword (from investigator regions)
int[] knownIndexes = { }; // leave empty; Description/FileName match is primary

bool IsShip(object m)
{
    var desc = S(m, "Description");
    var file = S(m, "FileName");
    if (desc.IndexOf(shipKey, StringComparison.Ordinal) >= 0) return true;
    if (file.IndexOf(shipKey, StringComparison.Ordinal) >= 0) return true;
    foreach (var k in extraKeys)
    {
        if (!string.IsNullOrEmpty(k) && (desc.IndexOf(k, StringComparison.OrdinalIgnoreCase) >= 0 || file.IndexOf(k, StringComparison.OrdinalIgnoreCase) >= 0))
            return true;
    }
    try
    {
        int idx = Convert.ToInt32(Prop(m, "Index"));
        if (knownIndexes.Contains(idx)) return true;
    }
    catch { }
    return false;
}

int changed = 0, already = 0, scannedShip = 0;
foreach (var m in maps)
{
    if (!IsShip(m)) continue;
    scannedShip++;
    bool allow = false;
    try { allow = Convert.ToBoolean(Prop(m, "AllowTT")); } catch { }
    var line = $"[{S(m, "Index")}] Desc={S(m, "Description")} File={S(m, "FileName")} AllowTT={allow}";
    report.AppendLine("HIT " + line);
    Console.WriteLine("HIT " + line);
    if (allow)
    {
        SetProp(m, "AllowTT", false);
        changed++;
        report.AppendLine("  -> AllowTT=false");
    }
    else already++;
}

report.AppendLine($"scannedShip={scannedShip} changed={changed} alreadyFalse={already}");
Console.WriteLine($"scannedShip={scannedShip} changed={changed} alreadyFalse={already}");

var save = sessionType.GetMethods().Where(m => m.Name == "Save").OrderByDescending(m => m.GetParameters().Length).First();
var pars = save.GetParameters();
object?[] saveArgs;
if (pars.Length == 2 && pars[0].ParameterType == typeof(bool) && pars[1].ParameterType == modeType)
    saveArgs = new object?[] { true, tool };
else if (pars.Length == 1 && pars[0].ParameterType == typeof(bool))
    saveArgs = new object?[] { true };
else if (pars.Length == 0)
    saveArgs = Array.Empty<object?>();
else
{
    saveArgs = new object?[pars.Length];
    for (int i = 0; i < pars.Length; i++)
    {
        if (pars[i].ParameterType == typeof(bool)) saveArgs[i] = true;
        else if (pars[i].ParameterType == modeType) saveArgs[i] = tool;
        else if (pars[i].HasDefaultValue) saveArgs[i] = pars[i].DefaultValue;
        else saveArgs[i] = null;
    }
}
save.Invoke(ses, saveArgs);
report.AppendLine("saved work=" + work);

// Copy System.db back to Database + Data (MapInfo is server System.db; still sync both)
var newSys = Path.Combine(work, "System.db");
File.Copy(newSys, Path.Combine(root, "Database", "System.db"), true);
File.Copy(newSys, Path.Combine(root, "Data", "System.db"), true);
report.AppendLine("synced Database\\System.db + Data\\System.db");
report.AppendLine("System.db sha16=" + Hex16(Path.Combine(root, "Database", "System.db")));

// Try VPS path if present
string[] vpsCandidates = {
    @"D:\Mir3service\Database\System.db",
    @"D:\Mir3service\System.db",
    @"E:\Mir3service\Database\System.db",
};
foreach (var vp in vpsCandidates)
{
    if (File.Exists(vp))
    {
        var vb = vp + ".bak_shipAllowTT_" + stamp;
        File.Copy(vp, vb, true);
        File.Copy(newSys, vp, true);
        report.AppendLine("VPS synced " + vp + " bak=" + vb);
        Console.WriteLine("VPS synced " + vp);
    }
}
if (!vpsCandidates.Any(File.Exists))
{
    report.AppendLine("VPS path D:\\Mir3service not present on this PC — skip");
    Console.WriteLine("VPS path not present — skip");
}

// Verify reopen
var verifyWork = Path.Combine(Path.GetTempPath(), "ship-tt-v-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(verifyWork);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(verifyWork, "System.db"), true);
var vses = Open(verifyWork);
var vmaps = Coll(vses, mapType).Where(IsShip).ToList();
foreach (var m in vmaps)
{
    bool allow = Convert.ToBoolean(Prop(m, "AllowTT"));
    report.AppendLine($"VERIFY [{S(m, "Index")}] {S(m, "Description")} AllowTT={allow}");
    Console.WriteLine($"VERIFY [{S(m, "Index")}] {S(m, "Description")} AllowTT={allow}");
    if (allow) report.AppendLine("WARN still AllowTT=true");
}

var logPath = Path.Combine(toolRoot, "apply_log_" + stamp + ".txt");
File.WriteAllText(logPath, report.ToString(), Encoding.UTF8);
Console.WriteLine("LOG=" + logPath);
Console.WriteLine("DONE changed=" + changed);
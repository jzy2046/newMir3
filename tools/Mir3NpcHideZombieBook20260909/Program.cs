using System.Collections;
using System.Drawing;
using System.Reflection;
using System.Runtime.Loader;
using System.Security.Cryptography;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3NpcHideZombieBook20260909 <dry-run|apply>");
    return 1;
}
var doApply = args[0] == "apply";
var root = @"D:\newMir3";
var toolDir = Path.Combine(root, "tools", "Mir3NpcHideZombieBook20260909");
var deps = Path.Combine(root, "tools", "_deps");
var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L($"Mir3NpcHideZombieBook20260909 {(doApply ? "APPLY" : "DRY")} {stamp}");

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

string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
object? Prop(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void SetProp(object o, string n, object? v)
{
    var pr = o.GetType().GetProperty(n)!;
    var t = Nullable.GetUnderlyingType(pr.PropertyType) ?? pr.PropertyType;
    if (v != null && t.IsEnum && v is not Enum) pr.SetValue(o, Enum.Parse(t, v.ToString()!));
    else if (v != null && t != typeof(string) && t.IsValueType && v.GetType() != t)
        pr.SetValue(o, Convert.ChangeType(v, t));
    else pr.SetValue(o, v);
}
string S(object? o, string n) => Convert.ToString(Prop(o, n)) ?? "";
int I(object? o, string n) { var v = Prop(o, n); return v == null ? 0 : Convert.ToInt32(v); }
bool B(object? o, string n) { var v = Prop(o, n); return v != null && Convert.ToBoolean(v); }
string Pts(object? region)
{
    var arr = Prop(region, "PointRegion") as Point[];
    if (arr == null || arr.Length == 0) return "null";
    return string.Join(";", arr.Select(pt => pt.X + "," + pt.Y));
}
bool Near(object? region, int xmin, int xmax, int ymin, int ymax)
{
    var arr = Prop(region, "PointRegion") as Point[];
    if (arr == null) return false;
    return arr.Any(pt => pt.X >= xmin && pt.X <= xmax && pt.Y >= ymin && pt.Y <= ymax);
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
void Save(object s)
{
    var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
    save.Invoke(s, new object[] { true, tool });
}

var npcT = lib.GetType("Library.SystemModels.NPCInfo")!;
var mapT = lib.GetType("Library.SystemModels.MapInfo")!;
var regionT = lib.GetType("Library.SystemModels.MapRegion")!;
var monT = lib.GetType("Library.SystemModels.MonsterInfo")!;
var itemT = lib.GetType("Library.SystemModels.ItemInfo")!;
var dropT = lib.GetType("Library.SystemModels.DropInfo")!;

const int ItemTypeBook = 14;
string nZonghe = "\u7efc\u5408\u670d\u52a1"; // 综合服务
string nPaodian = "\u6ce1\u70b9"; // 泡点
string nAdmin = "\u884c\u653f\u5b98\u5458"; // 行政官员
string[] zombieKeys = new[] {
    "\u50f5\u5c38", // 僵尸
    "\u5c38\u738b", // 尸王
    "\u90aa\u9053\u50f5\u5c38",
    "\u50e7\u4fa3\u50f5\u5c38",
};

// Backup on apply
string bakDir = "";
if (doApply)
{
    bakDir = Path.Combine(root, "Database", "Backup_npchide_zombiebook_" + stamp);
    Directory.CreateDirectory(bakDir);
    foreach (var name in new[] { "System.db", "ClientSystem.db" })
    {
        var src = Path.Combine(root, "Database", name);
        if (File.Exists(src)) File.Copy(src, Path.Combine(bakDir, name), true);
    }
    var dataBak = Path.Combine(root, "Data", "Backup_npchide_zombiebook_" + stamp);
    Directory.CreateDirectory(dataBak);
    foreach (var name in new[] { "System.db", "ClientSystem.db" })
    {
        var src = Path.Combine(root, "Data", name);
        if (File.Exists(src)) File.Copy(src, Path.Combine(dataBak, name), true);
    }
    L("backup=" + bakDir);
}

var work = Path.Combine(Path.GetTempPath(), "npchide-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
var cliSrc = Path.Combine(root, "Database", "ClientSystem.db");
if (File.Exists(cliSrc)) File.Copy(cliSrc, Path.Combine(work, "ClientSystem.db"), true);

var ses = Open(work);
var npcs = Coll(ses, npcT);
var maps = Coll(ses, mapT);
var regions = Coll(ses, regionT);
var mons = Coll(ses, monT);
var items = Coll(ses, itemT);
var drops = Coll(ses, dropT);

L("=== 1) Map#7 NPCs / Regions near X=400-410 Y=115-125 ===");
var map7 = maps.FirstOrDefault(m => I(m, "Index") == 7);
L($"Map#7 desc={S(map7,"Description")} file={S(map7,"FileName")}");

var nearNpcs = new List<object>();
foreach (var n in npcs)
{
    var region = Prop(n, "Region");
    var map = Prop(region, "Map");
    if (map == null || I(map, "Index") != 7) continue;
    if (!Near(region, 400, 410, 115, 125)) continue;
    nearNpcs.Add(n);
    L($"NPC#{I(n,"Index")} Name={S(n,"NPCName")} Display={B(n,"Display")} Reg#{I(region,"Index")} desc={S(region,"Description")} pts={Pts(region)}");
}
L($"near_npc_count={nearNpcs.Count}");

L("=== Regions on Map#7 near box (even without NPC) ===");
foreach (var r in regions)
{
    var map = Prop(r, "Map");
    if (map == null || I(map, "Index") != 7) continue;
    if (!Near(r, 400, 410, 115, 125)) continue;
    L($"Reg#{I(r,"Index")} desc={S(r,"Description")} pts={Pts(r)}");
}

// Identify keep vs hide
var keep335 = npcs.FirstOrDefault(x => I(x, "Index") == 335);
var keep66 = npcs.FirstOrDefault(x => I(x, "Index") == 66);
L($"KEEP #335 {S(keep335,"NPCName")} Display={B(keep335,"Display")} pts={Pts(Prop(keep335,"Region"))}");
L($"KEEP #66 {S(keep66,"NPCName")} Display={B(keep66,"Display")} pts={Pts(Prop(keep66,"Region"))}");

var hideTargets = new List<object>();
foreach (var n in nearNpcs)
{
    var idx = I(n, "Index");
    var name = S(n, "NPCName");
    if (idx == 335 || idx == 66) continue; // keep real ones
    bool isDupZonghe = name.Contains(nZonghe);
    bool isPaodian = name.Contains(nPaodian) || name.Contains("\u7ecf\u9a8c\u6ce1") /*经验泡*/;
    // also match exact stacked coords around 403,120
    bool stacked = Near(Prop(n, "Region"), 402, 404, 119, 121);
    if ((isDupZonghe || isPaodian) && (stacked || Near(Prop(n, "Region"), 400, 410, 115, 125)))
    {
        hideTargets.Add(n);
        L($"HIDE_CANDIDATE NPC#{idx} Name={name} Display={B(n,"Display")} pts={Pts(Prop(n,"Region"))} reason={(isDupZonghe?"dup_zonghe":"")}{(isPaodian?"paodian":"")}");
    }
}

// If nothing matched by name near box, also list ALL 综合服务 and 泡点 on map7
L("=== ALL Map7 综合服务 / 泡点 NPCs ===");
foreach (var n in npcs)
{
    var region = Prop(n, "Region");
    var map = Prop(region, "Map");
    if (map == null || I(map, "Index") != 7) continue;
    var name = S(n, "NPCName");
    if (!(name.Contains(nZonghe) || name.Contains(nPaodian) || name.Contains(nAdmin))) continue;
    L($"MAP7 NPC#{I(n,"Index")} Name={name} Display={B(n,"Display")} Reg#{I(region,"Index")} pts={Pts(region)}");
}

L("=== 2) Zombie book DropInfo ===");
var zombieMons = mons.Where(m =>
{
    var nm = S(m, "MonsterName");
    return zombieKeys.Any(k => nm.Contains(k));
}).ToList();
L($"zombie_mon_count={zombieMons.Count}");
foreach (var m in zombieMons.OrderBy(m => I(m, "Index")))
    L($"  Mon#{I(m,"Index")} {S(m,"MonsterName")}");

var zombieSet = new HashSet<object>(zombieMons);
var bookIssues = new List<(object drop, object mon, object item, int chance)>();
int bookOk = 0, bookZero = 0, bookMissingMons = 0;
var monWithBook = new HashSet<int>();
foreach (var d in drops)
{
    var mon = Prop(d, "Monster");
    var item = Prop(d, "Item");
    if (mon == null || item == null) continue;
    if (!zombieSet.Contains(mon) && !zombieKeys.Any(k => S(mon, "MonsterName").Contains(k))) continue;
    var itVal = Convert.ToInt32(Prop(item, "ItemType") ?? -1);
    var iname = S(item, "ItemName");
    bool isBook = itVal == ItemTypeBook || iname.Contains("\u4e66") || iname.Contains("\u79d8\u7c4d");
    if (!isBook) continue;
    int ch = I(d, "Chance");
    monWithBook.Add(I(mon, "Index"));
    L($"Drop#{I(d,"Index")} Mon={S(mon,"MonsterName")} Item={iname} Type={itVal} Chance={ch} Amount={I(d,"Amount")} DropSet={I(d,"DropSet")}");
    if (ch < 1)
    {
        bookZero++;
        bookIssues.Add((d, mon, item, ch));
    }
    else bookOk++;
}
foreach (var m in zombieMons)
{
    if (!monWithBook.Contains(I(m, "Index")))
    {
        bookMissingMons++;
        L($"NO_BOOK_DROP Mon#{I(m,"Index")} {S(m,"MonsterName")}");
    }
}
L($"book_ok={bookOk} book_chance_lt1={bookZero} zombies_missing_book={bookMissingMons}");

// Also scan ALL drops with Chance<1 Book type (broader)
L("=== ALL DropInfo Book with Chance<1 (any mon) ===");
int allBad = 0;
foreach (var d in drops)
{
    var item = Prop(d, "Item");
    if (item == null) continue;
    var itVal = Convert.ToInt32(Prop(item, "ItemType") ?? -1);
    var iname = S(item, "ItemName");
    bool isBook = itVal == ItemTypeBook || iname.Contains("\u4e66");
    if (!isBook) continue;
    int ch = I(d, "Chance");
    if (ch >= 1) continue;
    allBad++;
    var mon = Prop(d, "Monster");
    L($"BAD Drop#{I(d,"Index")} Mon={S(mon,"MonsterName")} Item={iname} Chance={ch}");
    if (!bookIssues.Any(x => ReferenceEquals(x.drop, d)))
        bookIssues.Add((d, mon!, item, ch));
}
L($"all_book_chance_lt1={allBad}");

if (doApply)
{
    L("=== APPLY NPC HIDE Display=True ===");
    int hid = 0;
    foreach (var n in hideTargets)
    {
        var before = B(n, "Display");
        SetProp(n, "Display", true);
        hid++;
        L($"SET NPC#{I(n,"Index")} {S(n,"NPCName")} Display {before}->{B(n,"Display")} pts={Pts(Prop(n,"Region"))}");
    }
    L($"npc_hidden={hid}");

    L("=== APPLY Book Chance fix Chance<1 -> 1 ===");
    int fixedCh = 0;
    foreach (var (drop, mon, item, old) in bookIssues)
    {
        SetProp(drop, "Chance", 1);
        fixedCh++;
        L($"SET Drop#{I(drop,"Index")} {S(mon,"MonsterName")}/{S(item,"ItemName")} Chance {old}->1");
    }
    L($"book_chance_fixed={fixedCh}");

    // If zombies missing books entirely, try restore from recent backup
    if (bookMissingMons > 0 && zombieMons.Count > 0)
    {
        L("=== Attempt restore missing zombie books from Backup_minebook_* ===");
        var bakCandidates = Directory.GetDirectories(Path.Combine(root, "Database"), "Backup_minebook_*")
            .Concat(Directory.GetDirectories(Path.Combine(root, "Database"), "Backup_eight_*"))
            .OrderByDescending(x => x).ToList();
        L("bak_candidates=" + string.Join(",", bakCandidates.Take(5)));
        // Just report — restoration of deleted rows needs separate session; note for parent
        L("NOTE: if rows deleted, need cross-session copy; see report. Skipping auto-create unless Chance-only fix insufficient.");
    }

    Save(ses);
    File.Copy(Path.Combine(work, "System.db"), Path.Combine(root, "Database", "System.db"), true);
    var dataSys = Path.Combine(root, "Data", "System.db");
    if (File.Exists(dataSys)) File.Copy(Path.Combine(work, "System.db"), dataSys, true);
    L("saved System.db");

    // Sync ClientSystem for NPC Display only
    L("=== Sync ClientSystem NPC Display ===");
    var workCli = Path.Combine(Path.GetTempPath(), "npchide-cli-" + Guid.NewGuid().ToString("N")[..8]);
    Directory.CreateDirectory(workCli);
    // Session expects System.db filename
    File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(workCli, "System.db"), true);
    var sesC = Open(workCli);
    var npcsC = Coll(sesC, npcT);
    int cliHid = 0;
    foreach (var n in hideTargets)
    {
        var idx = I(n, "Index");
        var c = npcsC.FirstOrDefault(x => I(x, "Index") == idx);
        if (c == null) { L($"CLI miss NPC#{idx}"); continue; }
        var before = B(c, "Display");
        SetProp(c, "Display", true);
        cliHid++;
        L($"CLI SET NPC#{idx} Display {before}->{B(c,"Display")}");
    }
    Save(sesC);
    (sesC as IDisposable)?.Dispose();
    File.Copy(Path.Combine(workCli, "System.db"), Path.Combine(root, "Database", "ClientSystem.db"), true);
    var dataCli = Path.Combine(root, "Data", "ClientSystem.db");
    if (File.Exists(dataCli)) File.Copy(Path.Combine(workCli, "System.db"), dataCli, true);
    L($"cli_npc_hidden={cliHid}");
    L("ClientSystem.sha16=" + Hex16(Path.Combine(root, "Database", "ClientSystem.db")));
    try { Directory.Delete(workCli, true); } catch { }
    try { Directory.Delete(workCli + "_bak", true); } catch { }
}

(ses as IDisposable)?.Dispose();
try { Directory.Delete(work, true); } catch { }
try { Directory.Delete(work + "_bak", true); } catch { }

var outPath = Path.Combine(toolDir, (doApply ? "apply_" : "dry_") + stamp + ".txt");
File.WriteAllText(outPath, report.ToString(), new UTF8Encoding(false));
L("report=" + outPath);
return 0;

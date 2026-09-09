using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: t <dry-run|apply>");
    return 1;
}
var doApply = args[0] == "apply";
var root = @"D:\newMir3";
var toolDir = Path.Combine(root, "tools", "Mir3MineBook20260909");
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
var mapType = lib.GetType("Library.SystemModels.MapInfo")!;
var dropType = lib.GetType("Library.SystemModels.DropInfo")!;
var respawnType = lib.GetType("Library.SystemModels.RespawnInfo")!;
var mineType = lib.GetType("Library.SystemModels.MineInfo")!;
var moveType = lib.GetType("Library.SystemModels.MovementInfo")!;
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);

string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
void SetP(object o, string n, object? v)
{
    var prop = o.GetType().GetProperty(n) ?? throw new Exception("no prop " + n);
    if (v == null) { prop.SetValue(o, null); return; }
    var t = Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType;
    if (t.IsEnum) prop.SetValue(o, Enum.Parse(t, v.ToString()!));
    else if (t == typeof(bool)) prop.SetValue(o, Convert.ToBoolean(v));
    else if (t == typeof(int)) prop.SetValue(o, Convert.ToInt32(v));
    else if (t == typeof(string)) prop.SetValue(o, v.ToString());
    else prop.SetValue(o, Convert.ChangeType(v, t));
}
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
report.AppendLine($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");
report.AppendLine("Chance convention: Random.Next(Chance)==0 => 1/N; double rate => Chance/=2");
report.AppendLine("Mining: Random.Next(MineInfo.Chance)<=0 with MiningSuccessRate; Chance=1 => 100%");

var bakDir = Path.Combine(root, "Database", "Backup_minebook_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(bakDir, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(bakDir, "ClientSystem.db"), true);
report.AppendLine("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3minebook-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work); Directory.CreateDirectory(work + "_bak");
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(work + "_bak") });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
try { sessionType.GetProperty("BackUp")!.SetValue(ses, false); } catch { }

var maps = ListOf(ses, mapType);
var mapByIdx = maps.ToDictionary(m => Iv(m, "Index"), m => m);
var respawns = ListOf(ses, respawnType);
var drops = ListOf(ses, dropType);
var mines = ListOf(ses, mineType);
var moves = ListOf(ses, moveType);

// Build adjacency
var adj = new Dictionary<int, HashSet<int>>();
void AddEdge(int a, int b)
{
    if (a == 0 || b == 0) return;
    if (!adj.TryGetValue(a, out var sa)) { sa = new HashSet<int>(); adj[a] = sa; }
    if (!adj.TryGetValue(b, out var sb)) { sb = new HashSet<int>(); adj[b] = sb; }
    sa.Add(b); sb.Add(a);
}
foreach (var mv in moves)
{
    var srcReg = P(mv, "SourceRegion");
    var dstReg = P(mv, "DestinationRegion");
    var srcMap = srcReg == null ? null : P(srcReg, "Map");
    var dstMap = dstReg == null ? null : P(dstReg, "Map");
    AddEdge(srcMap == null ? 0 : Iv(srcMap, "Index"), dstMap == null ? 0 : Iv(dstMap, "Index"));
}

HashSet<int> BfsMine(int start, Func<object, bool> fileOk)
{
    var vis = new HashSet<int>();
    var q = new Queue<int>();
    q.Enqueue(start); vis.Add(start);
    while (q.Count > 0)
    {
        var cur = q.Dequeue();
        if (!adj.TryGetValue(cur, out var ns)) continue;
        foreach (var n in ns)
        {
            if (vis.Contains(n)) continue;
            if (!mapByIdx.TryGetValue(n, out var mo)) continue;
            // stay inside dungeon: allow if fileOk OR already connected dungeon child of start set
            var file = S(mo, "FileName");
            // never walk back to overworld towns
            var desc = S(mo, "Description");
            if (n == 1 || n == 24 || n == 5 || n == 6 || n == 25 || n == 26) continue; // towns/overworld
            if (!fileOk(mo) && !file.StartsWith("D4", StringComparison.OrdinalIgnoreCase) && !file.StartsWith("D45", StringComparison.OrdinalIgnoreCase)
                && !file.StartsWith("D42", StringComparison.OrdinalIgnoreCase) && !file.StartsWith("D43", StringComparison.OrdinalIgnoreCase)
                && !file.StartsWith("D41", StringComparison.OrdinalIgnoreCase) && !file.StartsWith("D40", StringComparison.OrdinalIgnoreCase)
                && !file.Contains("D431") && !file.Contains("D421") && !file.Contains("D451") && !file.Contains("D401")
                && !file.Contains("D411") && !file.Contains("D441") && !file.Contains("D443") && !file.Contains("D413")
                && !file.Contains("D422") && !file.Contains("D452") && !file.Contains("D402") && !file.Contains("D403")
                && !file.Contains("D404") && !file.Contains("D405") && !file.Contains("D406") && !file.Contains("D432")
                && !file.Contains("D433") && !file.Contains("D434") && !file.Contains("D435") && !file.Contains("D436")
                && !file.Contains("D412") && !file.Contains("D414") && !file.Contains("D442") && !file.Contains("D444"))
                continue;
            if (!fileOk(mo)) continue;
            vis.Add(n); q.Enqueue(n);
        }
    }
    return vis;
}

bool IsBireFile(object mo)
{
    var f = S(mo, "FileName").ToUpperInvariant();
    // D401-D406, D411-D41x (not D42/D43/D45)
    return f.StartsWith("D401") || f.StartsWith("D402") || f.StartsWith("D403") || f.StartsWith("D404")
        || f.StartsWith("D405") || f.StartsWith("D406") || f.StartsWith("D411") || f.StartsWith("D412")
        || f.StartsWith("D413") || f.StartsWith("D414") || f.StartsWith("D415") || f.StartsWith("D416");
}
bool IsSnakeFile(object mo)
{
    var f = S(mo, "FileName").ToUpperInvariant();
    return f.StartsWith("D421") || f.StartsWith("D422") || f.StartsWith("D423") || f.StartsWith("D424")
        || f.StartsWith("D431") || f.StartsWith("D432") || f.StartsWith("D433") || f.StartsWith("D434")
        || f.StartsWith("D435") || f.StartsWith("D436") || f.StartsWith("D441") || f.StartsWith("D442")
        || f.StartsWith("D443") || f.StartsWith("D444") || f.StartsWith("D451") || f.StartsWith("D452")
        || f.StartsWith("D453") || f.StartsWith("D454");
}

var bireMaps = BfsMine(85, IsBireFile);
var snakeMaps = new HashSet<int>();
foreach (var s in new[] { 103, 108, 126 })
    foreach (var x in BfsMine(s, IsSnakeFile)) snakeMaps.Add(x);

// Ensure seeds included
bireMaps.Add(85);
snakeMaps.Add(103); snakeMaps.Add(108); snakeMaps.Add(126);

var targetMapIdx = new HashSet<int>(bireMaps.Concat(snakeMaps));
var targetMapSet = new HashSet<object>(targetMapIdx.Where(i => mapByIdx.ContainsKey(i)).Select(i => mapByIdx[i]));

report.AppendLine("=== 比奇矿洞 maps (from 比奇城->废矿矿山 D401*) ===");
foreach (var i in bireMaps.OrderBy(x => x))
{
    if (!mapByIdx.TryGetValue(i, out var m)) continue;
    report.AppendLine($"BIRE Map#{i} File={S(m,"FileName")} Desc={S(m,"Description")} CanMine={Convert.ToBoolean(P(m,"CanMine")??false)}");
}
report.AppendLine("=== 毒蛇矿洞 maps (from 毒蛇山谷->矿山 D42*/D43*/D45*) ===");
foreach (var i in snakeMaps.OrderBy(x => x))
{
    if (!mapByIdx.TryGetValue(i, out var m)) continue;
    report.AppendLine($"SNAKE Map#{i} File={S(m,"FileName")} Desc={S(m,"Description")} CanMine={Convert.ToBoolean(P(m,"CanMine")??false)}");
}

var monOnMaps = new Dictionary<object, HashSet<string>>();
foreach (var r in respawns)
{
    var mon = P(r, "Monster");
    if (mon == null) continue;
    object? mapObj = null;
    var region = P(r, "Region");
    if (region != null) mapObj = P(region, "Map");
    int mapId = Iv(r, "MapID");
    bool onTarget = false;
    string mapLabel = "";
    if (mapObj != null && targetMapSet.Contains(mapObj))
    {
        onTarget = true;
        int mi = Iv(mapObj, "Index");
        string which = bireMaps.Contains(mi) ? "BIRE" : "SNAKE";
        mapLabel = $"{which} Map#{mi} {S(mapObj,"Description")}";
    }
    else if (mapId != 0 && targetMapIdx.Contains(mapId))
    {
        onTarget = true;
        string which = bireMaps.Contains(mapId) ? "BIRE" : "SNAKE";
        mapLabel = $"{which} MapID={mapId}";
    }
    if (!onTarget) continue;
    if (!monOnMaps.TryGetValue(mon, out var set)) { set = new HashSet<string>(); monOnMaps[mon] = set; }
    set.Add(mapLabel);
}

report.AppendLine($"=== MONSTERS on target mines: {monOnMaps.Count} ===");
foreach (var kv in monOnMaps.OrderBy(x => S(x.Key, "MonsterName")))
    report.AppendLine($"Mon#{Iv(kv.Key,"Index")} {S(kv.Key,"MonsterName")} @ {string.Join("; ", kv.Value)}");

const int ItemTypeBook = 14;
string bookChar = "\u4e66";
string miji = "\u79d8\u7c4d"; // 秘籍
report.AppendLine("=== BOOK/秘籍 DROPS (Chance=1/N) ===");
var bookDrops = new List<(object drop, object mon, object item, int oldChance)>();
foreach (var d in drops)
{
    var mon = P(d, "Monster");
    var item = P(d, "Item");
    if (mon == null || item == null) continue;
    if (!monOnMaps.ContainsKey(mon)) continue;
    var it = P(item, "ItemType");
    int itVal = it == null ? -1 : Convert.ToInt32(it);
    var iname = S(item, "ItemName");
    bool isBook = itVal == ItemTypeBook || iname.Contains(bookChar) || iname.Contains(miji);
    if (!isBook) continue;
    int ch = Iv(d, "Chance");
    bookDrops.Add((d, mon, item, ch));
    report.AppendLine($"Drop#{Iv(d,"Index")} Mon={S(mon,"MonsterName")} Item={iname} Type={itVal} Chance={ch} Amount={Iv(d,"Amount")} DropSet={Iv(d,"DropSet")}");
}

report.AppendLine($"=== MINE INFO ore rows (ItemType Ore=13) count check ===");
var mineRows = new List<(object mine, int oldChance, string itemName, int itemType)>();
int oreType = 13;
foreach (var mi in mines.OrderBy(x => Iv(x, "Index")))
{
    var map = P(mi, "Map");
    var item = P(mi, "Item");
    int ch = Iv(mi, "Chance");
    int itVal = item == null ? -1 : Convert.ToInt32(P(item, "ItemType") ?? -1);
    string iname = S(item, "ItemName");
    mineRows.Add((mi, ch, iname, itVal));
}
report.AppendLine($"total MineInfo={mineRows.Count}; ore-typed={mineRows.Count(x => x.itemType == oreType)}; non1={mineRows.Count(x => x.oldChance != 1)}");
foreach (var g in mineRows.GroupBy(x => x.oldChance).OrderBy(g => g.Key))
    report.AppendLine($"  Chance={g.Key} count={g.Count()} examples={string.Join(",", g.Take(3).Select(x => x.itemName))}");

if (doApply)
{
    report.AppendLine("=== APPLY BOOK CHANCE HALVE (target mine maps only) ===");
    int changedBooks = 0;
    foreach (var (drop, mon, item, oldChance) in bookDrops)
    {
        if (oldChance <= 1) { report.AppendLine($"SKIP Drop#{Iv(drop,"Index")} Chance={oldChance}"); continue; }
        int neu = Math.Max(1, oldChance / 2);
        SetP(drop, "Chance", neu);
        changedBooks++;
        report.AppendLine($"SET Drop#{Iv(drop,"Index")} {S(mon,"MonsterName")}/{S(item,"ItemName")} Chance {oldChance} -> {neu}");
    }
    report.AppendLine($"book_drops_changed={changedBooks}");

    report.AppendLine("=== APPLY MINE CHANCE=1 for Ore ItemType only ===");
    // Mining(): Random.Next(info.Chance...)<=0; Chance is 1/N. Chance=1 => always yield ore.
    // Only ItemType.Ore (13); leave book/special MineInfo untouched.
    int changedMines = 0, skippedNonOre = 0;
    foreach (var (mine, oldChance, iname, itVal) in mineRows)
    {
        if (itVal != oreType) { skippedNonOre++; continue; }
        if (oldChance == 1) continue;
        SetP(mine, "Chance", 1);
        changedMines++;
        var map = P(mine, "Map");
        report.AppendLine($"SET Mine#{Iv(mine, "Index")} Map#{(map == null ? 0 : Iv(map, "Index"))} {S(map, "Description")} Item={iname} Type={itVal} Chance {oldChance} -> 1");
    }
    report.AppendLine($"mine_ore_rows_changed={changedMines} skipped_non_ore={skippedNonOre}");
    report.AppendLine("NOTE: DropInfo is per-Monster; zombie/shiwang also in stone mines D14* so books there also double.");

    sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!.Invoke(ses, new object[] { true, tool });
    File.Copy(Path.Combine(work, "System.db"), Path.Combine(root, "Database", "System.db"), true);
    File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(root, "Database", "ClientSystem.db"), true);
    var dataSys = Path.Combine(root, "Data", "System.db");
    var dataCli = Path.Combine(root, "Data", "ClientSystem.db");
    if (File.Exists(dataSys)) File.Copy(Path.Combine(work, "System.db"), dataSys, true);
    if (File.Exists(dataCli)) File.Copy(Path.Combine(work, "ClientSystem.db"), dataCli, true);
    report.AppendLine("saved System.db + ClientSystem.db (+ Data sync if present)");
}

var outPath = Path.Combine(toolDir, (doApply ? "apply_" : "dry_") + stamp + ".txt");
File.WriteAllText(outPath, report.ToString(), new UTF8Encoding(false));
Console.WriteLine(report.ToString());
Console.WriteLine("report=" + outPath);
return 0;

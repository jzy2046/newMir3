using System.Collections;
using System.Globalization;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3Cleanup <dry-run|apply> [--repo <path>]");
    return 1;
}

var apply = args[0] == "apply";
var repo = @"D:\newMir3";
for (var i = 1; i < args.Length; i++)
{
    if (args[i] == "--repo" && i + 1 < args.Length) repo = Path.GetFullPath(args[++i]);
}

var systemDb = Path.Combine(repo, "Database", "System.db");
var clientDb = Path.Combine(repo, "Database", "ClientSystem.db");
var dataSystemDb = Path.Combine(repo, "Data", "System.db");
var dataClientDb = Path.Combine(repo, "Data", "ClientSystem.db");
var itemWhitelistPath = Path.Combine(repo, "_whitelist", "items.csv");
var monsterWhitelistPath = Path.Combine(repo, "_whitelist", "monsters.csv");
var reportPath = Path.Combine(repo, "_whitelist", "cleanup-report.txt");

if (!File.Exists(systemDb)) { Console.Error.WriteLine("missing " + systemDb); return 1; }
if (!File.Exists(itemWhitelistPath) || !File.Exists(monsterWhitelistPath))
{
    Console.Error.WriteLine("missing whitelist csv under _whitelist/");
    return 1;
}

var keepItems = LoadCsvColumn(itemWhitelistPath, "ItemName");
var keepMonsters = LoadCsvColumn(monsterWhitelistPath, "MonsterName");
var keepMonsterImages = LoadCsvColumn(monsterWhitelistPath, "Image");
Console.WriteLine($"whitelist items={keepItems.Count} monsters={keepMonsters.Count} images={keepMonsterImages.Count}");

RegisterResolver(repo);
var library = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(repo, "Library.dll"));
var sessionType = library.GetType("MirDB.Session")!;
var sessionModeType = library.GetType("MirDB.SessionMode")!;
var toolMode = Enum.Parse(sessionModeType, "ServerTool"); // SaveSystem/Delete only work in ServerTool
var itemType = library.GetType("Library.SystemModels.ItemInfo")!;
var monsterType = library.GetType("Library.SystemModels.MonsterInfo")!;
var setType = library.GetType("Library.SystemModels.SetInfo")!;
var dropType = library.GetType("Library.SystemModels.DropInfo")!;
var dbObjectType = library.GetType("MirDB.DBObject")!;

// Work on a temp copy, then replace on apply (safer)
var workRoot = Path.Combine(Path.GetTempPath(), "mir3-cleanup-" + Guid.NewGuid().ToString("N"));
var backupRoot = Path.Combine(Path.GetTempPath(), "mir3-cleanup-bak-" + Guid.NewGuid().ToString("N"));
Directory.CreateDirectory(workRoot);
Directory.CreateDirectory(backupRoot);
var workDb = Path.Combine(workRoot, "System.db");
File.Copy(systemDb, workDb, overwrite: true);
File.Copy(clientDb, Path.Combine(workRoot, "ClientSystem.db"), overwrite: true);
Console.WriteLine("workRoot files: " + string.Join(", ", Directory.GetFiles(workRoot).Select(Path.GetFileName)));

object session;
try
{
    var ctor = sessionType.GetConstructor(new[]
    {
        sessionModeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string)
    })!;
    session = ctor.Invoke(new object[]
    {
        toolMode,
        new[] { library },
        false,
        string.Empty,
        EnsureSlash(workRoot),
        EnsureSlash(backupRoot),
    });
    sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(session, null);
    // System tables are writable only in ServerTool; skip rotating.gz backups during bulk cleanup
    sessionType.GetProperty("BackUp")!.SetValue(session, false);
    Console.WriteLine("Mode=" + sessionType.GetProperty("Mode")!.GetValue(session) + " BackUp=false");
}
catch (Exception ex)
{
    Console.Error.WriteLine("session init failed: " + (ex.InnerException ?? ex).Message);
    TryDeleteDir(workRoot); TryDeleteDir(backupRoot);
    return 1;
}

var report = new StringBuilder();
report.AppendLine($"mode={(apply ? "apply" : "dry-run")}");
report.AppendLine($"repo={repo}");
report.AppendLine($"systemDb={systemDb}");

var items = GetCollection(sessionType, session, itemType).ToList();
var monsters = GetCollection(sessionType, session, monsterType).ToList();
var sets = GetCollection(sessionType, session, setType).ToList();
var drops = GetCollection(sessionType, session, dropType).ToList();

report.AppendLine($"before items={items.Count} monsters={monsters.Count} sets={sets.Count} drops={drops.Count}");

var deleteItems = new List<object>();
var keepItemObjs = new HashSet<object>();
foreach (var item in items)
{
    var name = ReadString(item, "ItemName");
    if (keepItems.Contains(name)) keepItemObjs.Add(item);
    else deleteItems.Add(item);
}

var deleteMonsters = new List<object>();
var keepMonsterObjs = new HashSet<object>();
foreach (var mon in monsters)
{
    var name = ReadString(mon, "MonsterName");
    // Whitelist is authoritative by Chinese MonsterName only (Image match is too loose).
    if (keepMonsters.Contains(name))
        keepMonsterObjs.Add(mon);
    else
        deleteMonsters.Add(mon);
}

var deleteDrops = new List<object>();
foreach (var drop in drops)
{
    var item = ReadProp(drop, "Item");
    var mon = ReadProp(drop, "Monster");
    var strItem = TryReadString(drop, "StrItemName");
    var strMon = TryReadString(drop, "StrMonsterName");
    var itemDead = item == null || deleteItems.Contains(item) || (strItem != null && strItem.Length > 0 && !keepItems.Contains(strItem));
    var monDead = mon == null || deleteMonsters.Contains(mon) || (strMon != null && strMon.Length > 0 && !keepMonsters.Contains(strMon));
    // keep drop only if both ends are keepers (or null with empty str meaning unresolved - delete those too if dangling)
    if (itemDead || monDead) deleteDrops.Add(drop);
}

report.AppendLine($"delete items={deleteItems.Count} keep={keepItemObjs.Count}");
report.AppendLine($"delete monsters={deleteMonsters.Count} keep={keepMonsterObjs.Count}");
report.AppendLine($"delete sets={sets.Count} (all)");
report.AppendLine($"delete drops={deleteDrops.Count}");

foreach (var name in deleteItems.Select(i => ReadString(i, "ItemName")).OrderBy(x => x).Take(30))
    report.AppendLine("  del-item " + name);
foreach (var name in deleteMonsters.Select(m => ReadString(m, "MonsterName")).OrderBy(x => x).Take(30))
    report.AppendLine("  del-mon " + name);

var missingItems = keepItems.Where(n => items.All(i => ReadString(i, "ItemName") != n)).OrderBy(x => x).ToList();
var missingMons = keepMonsters.Where(n => monsters.All(m => ReadString(m, "MonsterName") != n)).OrderBy(x => x).ToList();
report.AppendLine($"whitelist-missing-in-db items={missingItems.Count} monsters={missingMons.Count}");

if (!apply)
{
    File.WriteAllText(reportPath, report.ToString(), Encoding.UTF8);
    Console.WriteLine(report.ToString());
    Console.WriteLine("dry-run only; wrote " + reportPath);
    (session as IDisposable)?.Dispose();
    TryDeleteDir(workRoot); TryDeleteDir(backupRoot);
    return 0;
}

// delete order: drops -> sets -> items/monsters
// Use FastDelete + Collection.Delete (public Delete() NREs on null DBBindingList during association clear)
int deleted = 0;
foreach (var d in deleteDrops) { InvokeDelete(sessionType, session, dbObjectType, d); deleted++; }
foreach (var s in sets) { InvokeDelete(sessionType, session, dbObjectType, s); deleted++; }
foreach (var i in deleteItems) { InvokeDelete(sessionType, session, dbObjectType, i); deleted++; }
foreach (var m in deleteMonsters) { InvokeDelete(sessionType, session, dbObjectType, m); deleted++; }

// Save(bool, mode) runs SaveObjects then Commit -> SaveSystem + SaveClientSystem (ServerTool only)
var systemPath = Convert.ToString(sessionType.GetProperty("SystemPath")!.GetValue(session));
Console.WriteLine("SystemPath=" + systemPath);
var save = sessionType.GetMethod("Save", new[] { typeof(bool), sessionModeType })
    ?? throw new InvalidOperationException("Save(bool, SessionMode) missing");
Console.WriteLine("calling Save(true, ServerTool)");
save.Invoke(session, new object[] { true, toolMode });
var workHash = Convert.ToHexString(System.Security.Cryptography.SHA256.HashData(File.ReadAllBytes(workDb))).ToLowerInvariant();
Console.WriteLine("workDbHashAfterSave=" + workHash + " size=" + new FileInfo(workDb).Length);
(session as IDisposable)?.Dispose();

// replace live DBs from work copies (System + ClientSystem are distinct files)
var workClientDb = Path.Combine(workRoot, "ClientSystem.db");
File.Copy(workDb, systemDb, overwrite: true);
if (File.Exists(workClientDb)) File.Copy(workClientDb, clientDb, overwrite: true);
else File.Copy(workDb, clientDb, overwrite: true);
if (File.Exists(dataSystemDb)) File.Copy(systemDb, dataSystemDb, overwrite: true);
if (File.Exists(dataClientDb)) File.Copy(clientDb, dataClientDb, overwrite: true);

report.AppendLine($"deleted_calls={deleted}");
report.AppendLine("saved System.db + ClientSystem.db (+ Data copies if present)");
File.WriteAllText(reportPath, report.ToString(), Encoding.UTF8);
Console.WriteLine(report.ToString());

TryDeleteDir(workRoot); TryDeleteDir(backupRoot);
return 0;

static HashSet<string> LoadCsvColumn(string path, string column)
{
    var set = new HashSet<string>(StringComparer.Ordinal);
    using var reader = new StreamReader(path, Encoding.UTF8, detectEncodingFromByteOrderMarks: true);
    var header = reader.ReadLine() ?? throw new InvalidOperationException("empty csv " + path);
    var cols = SplitCsv(header);
    var idx = Array.FindIndex(cols, c => string.Equals(c.Trim().Trim('"'), column, StringComparison.OrdinalIgnoreCase));
    if (idx < 0) return set;
    string? line;
    while ((line = reader.ReadLine()) != null)
    {
        if (string.IsNullOrWhiteSpace(line)) continue;
        var parts = SplitCsv(line);
        if (idx >= parts.Length) continue;
        var v = parts[idx].Trim().Trim('"');
        if (v.Length > 0) set.Add(v);
    }
    return set;
}

static string[] SplitCsv(string line)
{
    // simple CSV: our whitelist has no quoted commas in names for ItemName col mostly; handle quotes
    var list = new List<string>();
    var sb = new StringBuilder();
    bool q = false;
    for (int i = 0; i < line.Length; i++)
    {
        var c = line[i];
        if (c == '"') { q = !q; continue; }
        if (c == ',' && !q) { list.Add(sb.ToString()); sb.Clear(); continue; }
        sb.Append(c);
    }
    list.Add(sb.ToString());
    return list.ToArray();
}

static void RegisterResolver(string repo)
{
    AssemblyLoadContext.Default.Resolving += (_, a) =>
    {
        if (string.IsNullOrWhiteSpace(a.Name)) return null;
        var p = Path.Combine(repo, a.Name + ".dll");
        return File.Exists(p) ? AssemblyLoadContext.Default.LoadFromAssemblyPath(p) : null;
    };
}

static IEnumerable<object> GetCollection(Type sessionType, object session, Type entityType)
{
    var getCollection = sessionType.GetMethods(BindingFlags.Instance | BindingFlags.Public)
        .Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
    var col = getCollection.MakeGenericMethod(entityType).Invoke(session, null)!;
    return ((IEnumerable)col).Cast<object>();
}

static object? ReadProp(object source, string name) =>
    source.GetType().GetProperty(name, BindingFlags.Instance | BindingFlags.Public)?.GetValue(source);

static string ReadString(object source, string name)
{
    var v = ReadProp(source, name);
    return Convert.ToString(v, CultureInfo.InvariantCulture) ?? "";
}

static string? TryReadString(object source, string name)
{
    var p = source.GetType().GetProperty(name, BindingFlags.Instance | BindingFlags.Public);
    if (p == null) return null;
    return Convert.ToString(p.GetValue(source), CultureInfo.InvariantCulture);
}

static void InvokeDelete(Type sessionType, object session, Type dbObjectType, object obj)
{
    // FastDelete marks IsTemporary+IsDeleted without walking Association links (avoids NRE on null lists)
    var fast = sessionType.GetMethod("FastDelete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)
        ?? throw new InvalidOperationException("Session.FastDelete missing");
    fast.Invoke(session, new[] { obj });

    // Remove from Binding so GetSaveData omits it
    var collField = dbObjectType.GetField("_Collection", BindingFlags.Instance | BindingFlags.NonPublic)
        ?? throw new InvalidOperationException("_Collection missing");
    var coll = collField.GetValue(obj) ?? throw new InvalidOperationException("Collection null");
    var del = coll.GetType().GetMethod("Delete", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic, binder: null, types: new[] { dbObjectType }, modifiers: null)
        ?? throw new InvalidOperationException("Collection.Delete missing");
    del.Invoke(coll, new[] { obj });
}

static string EnsureSlash(string path) => Path.EndsInDirectorySeparator(path) ? path : path + Path.DirectorySeparatorChar;

static void TryDeleteDir(string path)
{
    try { if (Directory.Exists(path)) Directory.Delete(path, true); } catch { /* ignore */ }
}










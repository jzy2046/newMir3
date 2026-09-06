using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Security.Cryptography;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
var deps = Path.Combine(root, "tools", "_deps");
AssemblyLoadContext.Default.Resolving += (_, a) =>
{
    foreach (var d in new[] { deps, root })
    {
        var p = Path.Combine(d, (a.Name ?? "") + ".dll");
        if (File.Exists(p)) return AssemblyLoadContext.Default.LoadFromAssemblyPath(p);
    }
    return null;
};

var lib = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root, "Library.dll"));
var sessionType = lib.GetType("MirDB.Session")!;
var modeType = lib.GetType("MirDB.SessionMode")!;
var monType = lib.GetType("Library.SystemModels.MonsterInfo")!;
var dropType = lib.GetType("Library.SystemModels.DropInfo")!;
var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);

string Slash(string p) => Path.EndsInDirectorySeparator(p) ? p : p + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
bool B(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v != null && Convert.ToBoolean(v); }
object? P(object o, string n) => o.GetType().GetProperty(n)?.GetValue(o);
void SetP(object o, string n, object? v)
{
    var prop = o.GetType().GetProperty(n) ?? throw new Exception("no prop " + n);
    if (v == null) { prop.SetValue(o, null); return; }
    var t = Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType;
    if (t.IsEnum) prop.SetValue(o, Enum.Parse(t, v.ToString()!));
    else if (t == typeof(bool)) prop.SetValue(o, Convert.ToBoolean(v));
    else if (t == typeof(int)) prop.SetValue(o, Convert.ToInt32(v));
    else if (typeof(string) == t) prop.SetValue(o, v.ToString());
    else prop.SetValue(o, Convert.ChangeType(v, t));
}
string Hex16(string path) => Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(path)))[..16];

object Open(string work)
{
    Directory.CreateDirectory(work);
    Directory.CreateDirectory(work + "_bak");
    var s = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(work + "_bak") });
    sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(s, null);
    try { sessionType.GetProperty("BackUp")!.SetValue(s, false); } catch { }
    return s;
}
void Save(object ses) => sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!.Invoke(ses, new object[] { true, tool });

// Classification (documented):
//   小BOSS: Index in [20000,30000) OR name starts with "副本-" OR (Index>=100000 && Level<100)
//   大BOSS: Index in [30000,100000) OR (Index>=100000 && !副本- && Level>=100)
// Rationale: open-world Mir3 Index bands (2xxxx卫士/将, 3xxxx教主); 杀怪.py marks 副本-* as 小BOSS elites.
string Tier(object m)
{
    var idx = Iv(m, "Index");
    var name = S(m, "MonsterName");
    var level = Iv(m, "Level");
    if (idx >= 20000 && idx < 30000) return "小";
    if (idx >= 30000 && idx < 100000) return "大";
    if (name.StartsWith("副本-", StringComparison.Ordinal)) return "小";
    if (idx >= 100000 && level >= 100) return "大";
    return "小";
}

const int DiShaIdx = 122585;
const int TianGangIdx = 122586;
const int Chance = 1; // always drop, same as boss 金币 guaranteed material pattern
const int SrcAgiImage = 4002;
const int SrcMDefImage = 4025;

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var bakDir = Path.Combine(root, "Database", "Backup_boss_stone_drop_" + stamp);
Directory.CreateDirectory(bakDir);
foreach (var name in new[] { "System.db", "ClientSystem.db" })
    File.Copy(Path.Combine(root, "Database", name), Path.Combine(bakDir, name), true);
Console.WriteLine("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "bossstonedrop-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);

var ses = Open(work);
var monColl = get.MakeGenericMethod(monType).Invoke(ses, null)!;
var dropColl = get.MakeGenericMethod(dropType).Invoke(ses, null)!;
var itemColl = get.MakeGenericMethod(itemType).Invoke(ses, null)!;
var mons = ((IEnumerable)monColl).Cast<object>().ToList();
var drops = ((IEnumerable)dropColl).Cast<object>().ToList();
var items = ((IEnumerable)itemColl).Cast<object>().ToList();

var diSha = items.FirstOrDefault(x => Iv(x, "Index") == DiShaIdx) ?? throw new Exception("missing 地煞石 #122585");
var tianGang = items.FirstOrDefault(x => Iv(x, "Index") == TianGangIdx) ?? throw new Exception("missing 天罡石 #122586");

// Ensure icons if sibling not done / Image still 0
bool iconChanged = false;
if (Iv(diSha, "Image") <= 0)
{
    SetP(diSha, "Image", SrcAgiImage);
    SetP(diSha, "Shape", 0);
    iconChanged = true;
    Console.WriteLine($"ICON SET 地煞 Image={SrcAgiImage}");
}
else Console.WriteLine($"ICON OK 地煞 Image={Iv(diSha,"Image")} Shape={Iv(diSha,"Shape")}");
if (Iv(tianGang, "Image") <= 0)
{
    SetP(tianGang, "Image", SrcMDefImage);
    SetP(tianGang, "Shape", 0);
    iconChanged = true;
    Console.WriteLine($"ICON SET 天罡 Image={SrcMDefImage}");
}
else Console.WriteLine($"ICON OK 天罡 Image={Iv(tianGang,"Image")} Shape={Iv(tianGang,"Shape")}");

var bosses = mons.Where(m => B(m, "IsBoss")).OrderBy(m => Iv(m, "Index")).ToList();
Console.WriteLine($"bossCount={bosses.Count} Chance={Chance}");

var createDrop = dropColl.GetType().GetMethod("CreateNewObject", Type.EmptyTypes)!;

int created = 0, updated = 0, smallN = 0, bigN = 0;
var report = new StringBuilder();
report.AppendLine("convention=Index[20000,30000)=小; [30000,100000)=大; 副本-*=小; else Index>=100000&&Level>=100=大 else 小");
report.AppendLine($"Chance={Chance} (always; peer=boss金币 Chance=1)");
report.AppendLine("小: 地煞 Amount=5, 天罡 Amount=1");
report.AppendLine("大: 地煞 Amount=10, 天罡 Amount=5");
report.AppendLine($"iconChanged={iconChanged}");

foreach (var mon in bosses)
{
    var tier = Tier(mon);
    if (tier == "小") smallN++; else bigN++;
    int amtDi = tier == "小" ? 5 : 10;
    int amtTian = tier == "小" ? 1 : 5;
    var mid = Iv(mon, "Index");
    var mname = S(mon, "MonsterName");

    void Upsert(object item, int itemIdx, int amount, string label)
    {
        var existing = drops.FirstOrDefault(d =>
        {
            var m = P(d, "Monster");
            var it = P(d, "Item");
            return m != null && it != null && Iv(m, "Index") == mid && Iv(it, "Index") == itemIdx;
        });
        if (existing != null)
        {
            var oldAmt = Iv(existing, "Amount");
            var oldChance = Iv(existing, "Chance");
            if (oldAmt != amount || oldChance != Chance)
            {
                SetP(existing, "Amount", amount);
                SetP(existing, "Chance", Chance);
                SetP(existing, "DropGroup", 0);
                SetP(existing, "DropSet", 0);
                SetP(existing, "PartOnly", false);
                SetP(existing, "EasterEvent", false);
                updated++;
                report.AppendLine($"UPD [{mid}] {mname} {tier} {label} Amt {oldAmt}->{amount} Chance {oldChance}->{Chance}");
            }
            else
            {
                report.AppendLine($"OK  [{mid}] {mname} {tier} {label} Amt={amount} Chance={Chance}");
            }
            return;
        }
        var nd = createDrop.Invoke(dropColl, null)!;
        SetP(nd, "Monster", mon);
        SetP(nd, "Item", item);
        SetP(nd, "Chance", Chance);
        SetP(nd, "Amount", amount);
        SetP(nd, "DropGroup", 0);
        SetP(nd, "DropSet", 0);
        SetP(nd, "PartOnly", false);
        SetP(nd, "EasterEvent", false);
        try { SetP(nd, "StrMonsterName", mname); } catch { }
        try { SetP(nd, "StrItemName", S(item, "ItemName")); } catch { }
        created++;
        drops.Add(nd);
        report.AppendLine($"NEW [{mid}] {mname} {tier} {label} Amt={amount} Chance={Chance}");
    }

    Upsert(diSha, DiShaIdx, amtDi, "地煞石");
    Upsert(tianGang, TianGangIdx, amtTian, "天罡石");
}

Console.WriteLine($"smallBosses={smallN} bigBosses={bigN} created={created} updated={updated}");
report.AppendLine($"summary small={smallN} big={bigN} created={created} updated={updated} monstersTouched={bosses.Count}");

Save(ses);
(ses as IDisposable)?.Dispose();

foreach (var dirName in new[] { "Database", "Data" })
{
    File.Copy(Path.Combine(work, "System.db"), Path.Combine(root, dirName, "System.db"), true);
    File.Copy(Path.Combine(work, "ClientSystem.db"), Path.Combine(root, dirName, "ClientSystem.db"), true);
    Console.WriteLine($"synced {dirName}/ System={Hex16(Path.Combine(root, dirName, "System.db"))} Client={Hex16(Path.Combine(root, dirName, "ClientSystem.db"))}");
}

// Verify reopen
var vwork = Path.Combine(Path.GetTempPath(), "bossstonedrop-v-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(vwork);
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(vwork, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(vwork, "ClientSystem.db"), true);
var vses = Open(vwork);
var vdrops = ((IEnumerable)get.MakeGenericMethod(dropType).Invoke(vses, null)!).Cast<object>().ToList();
var vmons = ((IEnumerable)get.MakeGenericMethod(monType).Invoke(vses, null)!).Cast<object>().ToList();
var vbosses = vmons.Where(m => B(m, "IsBoss")).ToList();
int vSmall = 0, vBig = 0, vOk = 0, vBad = 0;
foreach (var mon in vbosses)
{
    var tier = Tier(mon);
    if (tier == "小") vSmall++; else vBig++;
    int wantDi = tier == "小" ? 5 : 10;
    int wantTian = tier == "小" ? 1 : 5;
    var mid = Iv(mon, "Index");
    foreach (var (itemIdx, wantAmt, label) in new[] { (DiShaIdx, wantDi, "地煞"), (TianGangIdx, wantTian, "天罡") })
    {
        var hit = vdrops.FirstOrDefault(d =>
        {
            var m = P(d, "Monster"); var it = P(d, "Item");
            return m != null && it != null && Iv(m, "Index") == mid && Iv(it, "Index") == itemIdx;
        });
        if (hit == null || Iv(hit, "Amount") != wantAmt || Iv(hit, "Chance") != Chance)
        {
            vBad++;
            Console.WriteLine($"VERIFY FAIL [{mid}] {S(mon,"MonsterName")} {label}");
        }
        else vOk++;
    }
}
Console.WriteLine($"VERIFY okPairs={vOk} bad={vBad} small={vSmall} big={vBig}");
(vses as IDisposable)?.Dispose();

var reportPath = Path.Combine(root, "tools", "Mir3BossStoneDrop", $"apply_{stamp}.txt");
File.WriteAllText(reportPath, report.ToString(), new UTF8Encoding(false));
Console.WriteLine("report=" + reportPath);
if (vBad > 0) throw new Exception("verify failed");
Console.WriteLine("OK");

using System.Collections;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
var root = @"D:\newMir3";
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
var tool = Enum.Parse(modeType, "ServerTool");
var ctor = sessionType.GetConstructor(new[] { modeType, typeof(Assembly[]), typeof(bool), typeof(string), typeof(string), typeof(string) })!;
var get = sessionType.GetMethods().Single(m => m.Name == "GetCollection" && m.IsGenericMethodDefinition && m.GetParameters().Length == 0);
string Slash(string x) => Path.EndsInDirectorySeparator(x) ? x : x + Path.DirectorySeparatorChar;
string S(object? o, string n) => o == null ? "" : Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o)) ?? "";
int Iv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v == null ? 0 : Convert.ToInt32(v); }
bool Bv(object? o, string n) { var v = o?.GetType().GetProperty(n)?.GetValue(o); return v != null && Convert.ToBoolean(v); }
object? P(object? o, string n) => o?.GetType().GetProperty(n)?.GetValue(o);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var work = Path.Combine(Path.GetTempPath(), "mir3-req-probe-" + Guid.NewGuid().ToString("N")[..8]);
Directory.CreateDirectory(work); Directory.CreateDirectory(work + "_bak");
File.Copy(Path.Combine(root, "Database", "System.db"), Path.Combine(work, "System.db"), true);
File.Copy(Path.Combine(root, "Database", "ClientSystem.db"), Path.Combine(work, "ClientSystem.db"), true);
var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(work + "_bak") });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var sb = new StringBuilder();
void L(string s) { sb.AppendLine(s); Console.WriteLine(s); }

var npcType = lib.GetType("Library.SystemModels.NPCInfo")!;
var mapRegionType = lib.GetType("Library.SystemModels.MapRegion")!;
var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var monType = lib.GetType("Library.SystemModels.MonsterInfo")!;
var dropType = lib.GetType("Library.SystemModels.DropInfo")!;
var magicType = lib.GetType("Library.SystemModels.MagicInfo")!;

var npcs = ListOf(ses, npcType);
var items = ListOf(ses, itemType);
var mons = ListOf(ses, monType);
var drops = ListOf(ses, dropType);
var magics = ListOf(ses, magicType);

L("=== NPC props sample ===");
foreach (var pr in npcs.First().GetType().GetProperties().Select(x => x.Name).OrderBy(x => x))
    L("NPCProp " + pr);

string[] npcNeedles = { "活动管理员", "财叔", "宠物管理员", "宝石合成", "管理中心", "综合服务", "寄售商", "钱老板", "钱掌柜", "阿斌", "杂货", "道馆" };
L("=== NPCs matching ===");
foreach (var n in npcs.OrderBy(x => Iv(x, "Index")))
{
    var name = S(n, "NPCName");
    var file = S(n, "FileName");
    var region = P(n, "Region");
    var map = P(region, "Map");
    var mapDesc = S(map, "Description");
    var hit = npcNeedles.Any(k => name.Contains(k) || file.Contains(k));
    if (!hit && mapDesc.Contains("道馆")) hit = true;
    if (!hit && (name.Contains("管理员") || name.Contains("综合"))) hit = true;
    if (!hit) continue;
    var loc = P(n, "CurrentLocation") ?? P(n, "Location");
    L("NPC idx=" + Iv(n, "Index") + " name=" + name + " file=" + file + " display=" + Bv(n, "Display")
      + " Image=" + S(n, "Image") + " loc=" + loc + " region=" + Iv(region, "Index") + "/" + S(region, "Description")
      + " map=" + mapDesc);
}

L("=== MapRegion daoguan ===");
foreach (var r in ListOf(ses, mapRegionType).OrderBy(x => Iv(x, "Index")))
{
    var desc = S(r, "Description");
    var map = P(r, "Map");
    var mapDesc = S(map, "Description");
    if (!(desc.Contains("道馆") || mapDesc.Contains("道馆"))) continue;
    L("REG idx=" + Iv(r, "Index") + " desc=" + desc + " map=" + Iv(map, "Index") + "/" + mapDesc);
}

L("=== Items ===");
string[] itemNeedles = { "天罡石", "地煞石", "金色栗子", "结晶石", "石榴石", "大护身符", "灵魂护身符", "牛角", "万年雪霜", "金疮药", "魔法药", "强效太阳水", "裁决之杖", "骨玉权杖", "无极棍", "磨光片", "魔光片", "遗物" };
foreach (var it in items.OrderBy(x => Iv(x, "Index")))
{
    var name = S(it, "ItemName");
    if (!itemNeedles.Any(k => name.Contains(k))) continue;
    L("ITEM idx=" + Iv(it, "Index") + " name=" + name + " type=" + S(it, "ItemType") + " effect=" + S(it, "Effect")
      + " image=" + S(it, "Image") + " price=" + S(it, "Price") + " dur=" + S(it, "Durability") + " stack=" + S(it, "StackSize"));
}
L("=== ItemInfo props ===");
foreach (var pr in items.First().GetType().GetProperties().Select(x => x.Name).OrderBy(x => x)) L("ItemProp " + pr);

L("=== Monsters ===");
string[] monNeedles = { "黑度守将", "诺玛突击", "超强骷髅", "召唤骷髅" };
foreach (var m in mons.OrderBy(x => Iv(x, "Index")))
{
    var name = S(m, "MonsterName");
    if (!monNeedles.Any(k => name.Contains(k))) continue;
    L("MON idx=" + Iv(m, "Index") + " name=" + name);
    foreach (var pr in m.GetType().GetProperties().Select(x => x.Name).Where(x => x.Contains("Image") || x.Contains("File") || x.Contains("Shape") || x.Contains("Body") || x.Contains("Model") || x == "Index" || x.Contains("Name")).OrderBy(x => x))
        L("  " + pr + "=" + S(m, pr));
}

L("=== Drops ===");
foreach (var d in drops)
{
    var mon = P(d, "Monster");
    var item = P(d, "Item");
    var mn = S(mon, "MonsterName");
    var iname = S(item, "ItemName");
    if (!(mn.Contains("黑度守将") || mn.Contains("诺玛突击") || iname == "裁决之杖" || iname == "骨玉权杖" || iname == "无极棍")) continue;
    L("DROP mon=" + mn + " item=" + iname + " Chance=" + S(d, "Chance") + " Amount=" + S(d, "Amount"));
}

L("=== Magics ===");
string[] skills = { "天怒之火", "陨冰杀", "电闪雷鸣", "旋风墙", "护身法盾", "灵魂分裂", "吸星大法", "养生术", "暗鬼阵", "新传染", "施毒大法", "分身术", "焰魔召唤术", "魔焰强解术", "君临步", "屠龙斩", "金刚之躯", "快刀斩马", "运气术", "天雷锤", "挑衅", "破空斩" };
foreach (var mg in magics.OrderBy(x => Iv(x, "Index")))
{
    var name = S(mg, "Name");
    if (!skills.Any(k => name.Contains(k))) continue;
    L("MAGIC idx=" + Iv(mg, "Index") + " name=" + name);
}
L("=== MagicInfo props ===");
if (magics.Count > 0)
    foreach (var pr in magics[0].GetType().GetProperties().Select(x => x.Name).OrderBy(x => x)) L("MagicProp " + pr);

L("=== SystemModels interesting ===");
foreach (var t in lib.GetTypes().Where(t => t.FullName != null && t.FullName.Contains("SystemModels")).Select(t => t.FullName!).OrderBy(x => x))
{
    if (t.Contains("Shop") || t.Contains("Store") || t.Contains("Safe") || t.Contains("Craft") || t.Contains("Jewel") || t.Contains("Mall") || t.Contains("Market") || t.Contains("NPC") || t.Contains("Fix") || t.Contains("Compose") || t.Contains("Success") || t.Contains("Gem"))
        L(t);
}

foreach (var typeName in new[] { "Library.SystemModels.StoreInfo", "Library.SystemModels.ShopInfo", "Library.SystemModels.SafeZoneInfo", "Library.SystemModels.NPCPage" })
{
    var t = lib.GetType(typeName);
    if (t == null) { L("MISSING " + typeName); continue; }
    var list = ListOf(ses, t);
    L("TYPE " + typeName + " count=" + list.Count);
    if (list.Count == 0) continue;
    foreach (var pr in list[0].GetType().GetProperties().Select(x => x.Name).OrderBy(x => x)) L("  prop " + pr);
    int shown = 0;
    foreach (var sh in list)
    {
        var item = P(sh, "Item") ?? P(sh, "ItemInfo");
        var iname = item != null ? S(item, "ItemName") : (S(sh, "ItemName") + S(sh, "Name") + S(sh, "Description"));
        if (typeName.Contains("Safe"))
        {
            var map = P(sh, "Info") ?? P(sh, "BindInfo") ?? P(sh, "Region");
            var md = S(P(map, "Map"), "Description") + S(map, "Description");
            if (!md.Contains("道馆") && !S(sh, "Description").Contains("道馆")) continue;
            L("SAFE " + string.Join(";", sh.GetType().GetProperties().Select(pr => pr.Name + "=" + S(sh, pr.Name))));
            continue;
        }
        if (!(iname.Contains("万年雪霜") || iname.Contains("金疮药") || iname.Contains("魔法药") || iname.Contains("强效太阳水") || iname.Contains("护身符") || iname.Contains("牛角") || iname.Contains("石榴") || iname.Contains("结晶"))) continue;
        L("ROW " + typeName.Split('.').Last() + " item=" + iname + " " + string.Join(";", sh.GetType().GetProperties().Where(pr => pr.Name is "Price" or "Cost" or "Filter" or "Type" or "Source" or "Bound" or "Index" or "HuntGoldPrice" or "GameGoldPrice" or "Count").Select(pr => pr.Name + "=" + S(sh, pr.Name))));
        shown++;
        if (shown > 80) break;
    }
}

var outPath = Path.Combine(root, "tools", "Mir3Req20260908", "probe_out.txt");
File.WriteAllText(outPath, sb.ToString(), new UTF8Encoding(false));
L("WROTE " + outPath);
(ses as IDisposable)?.Dispose();
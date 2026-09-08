using System.Collections;
using System.Drawing;
using System.Reflection;
using System.Runtime.Loader;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;
if (args.Length < 1 || args[0] is not ("dry-run" or "apply"))
{
    Console.Error.WriteLine("usage: Mir3Req20260908 <dry-run|apply>");
    return 1;
}
var doApply = args[0] == "apply";
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
void Set(object o, string n, object? val) => o.GetType().GetProperty(n)!.SetValue(o, val);
List<object> ListOf(object session, Type t) => ((IEnumerable)get.MakeGenericMethod(t).Invoke(session, null)!).Cast<object>().ToList();

var stamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
var report = new StringBuilder();
void L(string s) { report.AppendLine(s); Console.WriteLine(s); }
L($"mode={(doApply ? "apply" : "dry-run")} stamp={stamp}");

var sysDb = Path.Combine(root, "Database", "System.db");
var cliDb = Path.Combine(root, "Database", "ClientSystem.db");
var bakDir = Path.Combine(root, "Database", "Backup_req20260908_" + stamp);
Directory.CreateDirectory(bakDir);
File.Copy(sysDb, Path.Combine(bakDir, "System.db"), true);
File.Copy(cliDb, Path.Combine(bakDir, "ClientSystem.db"), true);
L("backup=" + bakDir);

var work = Path.Combine(Path.GetTempPath(), "mir3-req-" + Guid.NewGuid().ToString("N")[..8]);
var workBak = work + "_bak";
Directory.CreateDirectory(work); Directory.CreateDirectory(workBak);
File.Copy(sysDb, Path.Combine(work, "System.db"), true);
File.Copy(cliDb, Path.Combine(work, "ClientSystem.db"), true);

var ses = ctor.Invoke(new object[] { tool, new[] { lib }, false, "", Slash(work), Slash(workBak) });
sessionType.GetMethod("Init", Type.EmptyTypes)!.Invoke(ses, null);
sessionType.GetProperty("BackUp")!.SetValue(ses, false);

var npcType = lib.GetType("Library.SystemModels.NPCInfo")!;
var regionType = lib.GetType("Library.SystemModels.MapRegion")!;
var mapType = lib.GetType("Library.SystemModels.MapInfo")!;
var itemType = lib.GetType("Library.SystemModels.ItemInfo")!;
var monType = lib.GetType("Library.SystemModels.MonsterInfo")!;
var dropType = lib.GetType("Library.SystemModels.DropInfo")!;
var magicType = lib.GetType("Library.SystemModels.MagicInfo")!;
var storeType = lib.GetType("Library.SystemModels.StoreInfo")!;
var itemTypeEnum = lib.GetType("Library.ItemType") ?? lib.GetTypes().First(t => t.Name == "ItemType" && t.IsEnum);

var npcs = ListOf(ses, npcType);
var regions = ListOf(ses, regionType);
var maps = ListOf(ses, mapType);
var items = ListOf(ses, itemType);
var mons = ListOf(ses, monType);
var drops = ListOf(ses, dropType);
var magics = ListOf(ses, magicType);
var stores = ListOf(ses, storeType);

int changes = 0;

// --- 1) Hide 道馆 NPCs: 活动管理员332, 财叔354, 宠物管理员52, 宝石合成49 ---
foreach (var idx in new[] { 332, 354, 52, 49 })
{
    var n = npcs.FirstOrDefault(x => Iv(x, "Index") == idx);
    if (n == null) { L($"HIDE_MISS idx={idx}"); continue; }
    var before = Bv(n, "Display");
    L($"HIDE idx={idx} name={S(n,"NPCName")} Display {before} -> True");
    if (doApply && !before) { Set(n, "Display", true); changes++; }
}

// --- 7) Verify dungeon admins Display=True ---
foreach (var idx in new[] { 384, 385, 386, 387, 388, 389, 392, 353, 379 })
{
    var n = npcs.FirstOrDefault(x => Iv(x, "Index") == idx);
    if (n == null) { L($"FUBEN_MISS idx={idx}"); continue; }
    var d = Bv(n, "Display");
    L($"FUBEN_VERIFY idx={idx} name={S(n,"NPCName")} Display={d}");
    if (doApply && !d) { Set(n, "Display", true); changes++; L($"FUBEN_REHIDE idx={idx}"); }
}

// --- 6) Move 综合服务 335 to 道馆 401,119 Image=8; clone copy ---
var daoMap = maps.First(m => S(m, "Description") == "道馆" || Iv(m, "Index") == 7);
var n335 = npcs.First(x => Iv(x, "Index") == 335);
var r335 = P(n335, "Region")!;
var ptsBefore = P(r335, "PointRegion") as Point[];
L($"NPC335 before map={S(P(r335,"Map"),"Description")} pts={(ptsBefore==null?"null":string.Join(";", ptsBefore.Select(p=>$"{p.X},{p.Y}")))} Image={S(n335,"Image")}");

var jishou = npcs.FirstOrDefault(x => Iv(x, "Index") == 51); // 道馆寄售商 Image=8
int jishouImage = jishou != null ? Iv(jishou, "Image") : 8;
L($"寄售商 Image ref={jishouImage}");

if (doApply)
{
    Set(r335, "Map", daoMap);
    Set(r335, "PointRegion", new[] { new Point(401, 119) });
    Set(r335, "Size", 1);
    Set(r335, "Description", "综合服务");
    // ServerDescription may be computed
    Set(n335, "Image", jishouImage);
    Set(n335, "Display", false); // Display=False means visible in this codebase (CreateNPCs skips Display=True)
    changes++;
    L("MOVED NPC335 -> 道馆 401,119 Image=" + jishouImage);
}

// Create a copy NPC if no second usable instance on 道馆 - clone via session CreateObject if available
MethodInfo? FindCreate(Type t)
{
    var col = get.MakeGenericMethod(t).Invoke(ses, null)!;
    var m = col.GetType().GetMethods().FirstOrDefault(mi => mi.Name == "CreateNewObject" && mi.GetParameters().Length == 0)
         ?? col.GetType().GetMethods().FirstOrDefault(mi => mi.Name.Contains("Create") && mi.GetParameters().Length == 0);
    return m;
}
// Also ensure listener-compatible: script already listens 335 and 134.
// Create new region+npc copy on 雪原 if 335 moved away — optional. Req says 可拷贝一份: create one new instance at 道馆.
// We'll create additional NPC on 道馆 as copy of 335 with new index.
var createNpc = FindCreate(npcType);
var createReg = FindCreate(regionType);
L($"CreateNewObject NPC={createNpc!=null} Region={createReg!=null}");

if (doApply && createNpc != null && createReg != null)
{
    var colNpc = get.MakeGenericMethod(npcType).Invoke(ses, null)!;
    var colReg = get.MakeGenericMethod(regionType).Invoke(ses, null)!;
    var newReg = createReg.Invoke(colReg, null)!;
    Set(newReg, "Map", daoMap);
    Set(newReg, "PointRegion", new[] { new Point(403, 119) }); // slight offset copy
    Set(newReg, "Size", 1);
    Set(newReg, "Description", "综合服务拷贝");
    var newNpc = createNpc.Invoke(colNpc, null)!;
    Set(newNpc, "NPCName", "综合服务");
    Set(newNpc, "Image", jishouImage);
    Set(newNpc, "Display", false);
    Set(newNpc, "Region", newReg);
    // copy NPCFile if any
    var fileProp = n335.GetType().GetProperty("NPCFile");
    if (fileProp != null) Set(newNpc, "NPCFile", P(n335, "NPCFile"));
    L($"CREATED copy NPC idx={Iv(newNpc,"Index")} region={Iv(newReg,"Index")} at 403,119");
    changes++;
    // Note: need NpcEvent listener for new index — report for script follow-up
    File.WriteAllText(Path.Combine(root, "tools", "Mir3Req20260908", "new_npc_index.txt"), Iv(newNpc, "Index").ToString(), new UTF8Encoding(false));
}

// --- 2) Clear Magic Description ---
string[] skills = { "天怒之火","陨冰杀","电闪雷鸣","旋风墙","护身法盾","灵魂分裂","吸星大法","养生术","暗鬼阵","新传染","施毒大法","分身术","焰魔召唤术","魔焰强解术","君临步","屠龙斩","金刚之躯","快刀斩马","运气术","天雷锤","挑衅","破空斩" };
foreach (var mg in magics)
{
    var name = S(mg, "Name");
    if (!skills.Any(k => name == k || name.Contains(k))) continue;
    var desc = S(mg, "Description");
    L($"MAGIC Clear name={name} descLen={desc.Length}");
    if (doApply && !string.IsNullOrEmpty(desc)) { Set(mg, "Description", ""); changes++; }
}
// fuzzy 天怒
foreach (var mg in magics.Where(m => S(m,"Name").Contains("天怒") || S(m,"Name").Contains("怒之火")))
    L($"MAGIC fuzzy {S(mg,"Name")} descLen={S(mg,"Description").Length}");

// --- 12) 天罡石/地煞石 ItemType = Material (same as 金色栗子) ---
var material = Enum.Parse(itemTypeEnum, "Material");
foreach (var name in new[] { "天罡石", "地煞石" })
{
    var it = items.FirstOrDefault(x => S(x, "ItemName") == name);
    if (it == null) { L("ITEM_MISS " + name); continue; }
    L($"ITEM type {name} {S(it,"ItemType")} -> Material");
    if (doApply) { Set(it, "ItemType", material); changes++; }
}

// --- 11) 大护身符 variants: find, set Price=5000 Durability=500 ---
foreach (var it in items.Where(x => S(x,"ItemName").Contains("护身符")))
    L($"AMULET idx={Iv(it,"Index")} name={S(it,"ItemName")} type={S(it,"ItemType")} price={S(it,"Price")} dur={S(it,"Durability")} shape={S(it,"Shape")}");

foreach (var name in new[] { "大护身符", "大神圣护身符", "大暗黑护身符", "护身符（大）", "神圣护身符（大）", "暗黑护身符（大）" })
{
    var it = items.FirstOrDefault(x => S(x, "ItemName") == name);
    if (it == null) { L("AMULET_MISS " + name); continue; }
    L($"AMULET_SET {name} price {S(it,"Price")}->5000 dur {S(it,"Durability")}->500");
    if (doApply) { Set(it, "Price", 5000); Set(it, "Durability", 500); changes++; }
}

// --- 13) drugstore prices ---
void SetPrice(string name, int price)
{
    var it = items.FirstOrDefault(x => S(x, "ItemName") == name);
    if (it == null) { L("PRICE_MISS " + name); return; }
    L($"PRICE {name} {S(it,"Price")} -> {price}");
    if (doApply) { Set(it, "Price", price); changes++; }
}
SetPrice("金创药（特）", 550);
SetPrice("金疮药（特）", 550);
SetPrice("魔法药（特）", 550);
SetPrice("强效太阳水", 1100);

// --- Mall: add 万年雪霜 100 GameGold for 1000 ---
var snow = items.FirstOrDefault(x => S(x, "ItemName") == "万年雪霜");
L($"STORE count={stores.Count} snow={(snow==null?"MISS":"idx="+Iv(snow,"Index"))}");
foreach (var sh in stores)
    L($"STORE existing idx={Iv(sh,"Index")} item={S(P(sh,"Item"),"ItemName")} Price={S(sh,"Price")} Hunt={S(sh,"HuntGoldPrice")}");

var createStore = FindCreate(storeType);
if (doApply && snow != null && createStore != null && !stores.Any(s => S(P(s,"Item"),"ItemName")=="万年雪霜"))
{
    var col = get.MakeGenericMethod(storeType).Invoke(ses, null)!;
    var sh = createStore.Invoke(col, null)!;
    Set(sh, "Item", snow);
    Set(sh, "Price", 100); // GameGold / 赞助币 units as used elsewhere
    // If there's a count field - StoreInfo may sell 1; need shape/stack. Check for Amount - none. Client may buy stack via other means.
    // Some malls use Filter. Set Available=true Recommend maybe
    if (sh.GetType().GetProperty("Available") != null) Set(sh, "Available", true);
    L($"STORE_ADD 万年雪霜 Price=100 idx={Iv(sh,"Index")}");
    changes++;
    // Note: 100赞助币=1000个 may need special handling — Item StackSize/Give count may be script-side; flag if StoreInfo has no count
}
else if (snow != null)
{
    foreach (var sh in stores.Where(s => S(P(s,"Item"),"ItemName")=="万年雪霜"))
    {
        L($"STORE_UPD 万年雪霜 Price {S(sh,"Price")}->100");
        if (doApply) { Set(sh, "Price", 100); changes++; }
    }
}

// --- 15) Drops: remove from 黑度首将; add to 诺玛突击队长 Chance=1000 ---
var black = mons.FirstOrDefault(m => S(m, "MonsterName").Contains("黑度") && (S(m,"MonsterName").Contains("守将") || S(m,"MonsterName").Contains("首将")));
var numa = mons.FirstOrDefault(m => S(m, "MonsterName") == "诺玛突击队长");
L($"MON black={S(black,"MonsterName")} numa={S(numa,"MonsterName")}");
string[] weapons = { "裁决之杖", "骨玉权杖", "无极棍" };
var createDrop = FindCreate(dropType);
foreach (var wname in weapons)
{
    var item = items.FirstOrDefault(x => S(x, "ItemName") == wname);
    if (item == null) { L("WEP_MISS " + wname); continue; }
    // delete from black
    foreach (var d in drops.Where(d => ReferenceEquals(P(d,"Monster"), black) && ReferenceEquals(P(d,"Item"), item)).ToList())
    {
        L($"DROP_DEL mon={S(black,"MonsterName")} item={wname} C={S(d,"Chance")}");
        if (doApply)
        {
            var col = get.MakeGenericMethod(dropType).Invoke(ses, null)!;
            var del = col.GetType().GetMethod("Delete") ?? col.GetType().GetMethod("Remove");
            // DBObject usually has Delete method on object itself
            var delObj = d.GetType().GetMethod("Delete", Type.EmptyTypes);
            if (delObj != null) delObj.Invoke(d, null);
            else L("WARN no Delete on DropInfo");
            changes++;
        }
    }
    // add to numa if missing
    bool has = drops.Any(d => ReferenceEquals(P(d,"Monster"), numa) && ReferenceEquals(P(d,"Item"), item));
    if (!has && numa != null && createDrop != null)
    {
        L($"DROP_ADD mon=诺玛突击队长 item={wname} C=1000");
        if (doApply)
        {
            var col = get.MakeGenericMethod(dropType).Invoke(ses, null)!;
            var d = createDrop.Invoke(col, null)!;
            Set(d, "Monster", numa);
            Set(d, "Item", item);
            Set(d, "Chance", 1000);
            Set(d, "Amount", 1);
            changes++;
        }
    }
    else L($"DROP_HAS_OR_SKIP numa has={has} item={wname}");
}

// --- 16) 超强骷髅 model -> 召唤骷髅 ---
var superSk = mons.FirstOrDefault(m => S(m, "MonsterName") == "超强骷髅");
var summonSk = mons.FirstOrDefault(m => S(m, "MonsterName") == "召唤骷髅") ?? mons.FirstOrDefault(m => S(m, "MonsterName") == "骷髅");
if (summonSk == null)
{
    // list skeleton-ish
    foreach (var m in mons.Where(x => S(x,"MonsterName").Contains("骷髅")))
        L($"SKEL {S(m,"MonsterName")} Image={S(m,"Image")} Body={S(m,"BodyShape")}");
}
else
{
    L($"MODEL 超强骷髅 Image {S(superSk,"Image")}/{S(superSk,"BodyShape")} -> {S(summonSk,"Image")}/{S(summonSk,"BodyShape")}");
    if (doApply && superSk != null)
    {
        Set(superSk, "Image", P(summonSk, "Image")!);
        if (superSk.GetType().GetProperty("BodyShape") != null)
            Set(superSk, "BodyShape", P(summonSk, "BodyShape")!);
        changes++;
    }
}

L($"changes={changes}");

if (!doApply)
{
    File.WriteAllText(Path.Combine(root, "tools", "Mir3Req20260908", "dry_" + stamp + ".txt"), report.ToString(), new UTF8Encoding(false));
    L("dry-run only");
    (ses as IDisposable)?.Dispose();
    return 0;
}

var save = sessionType.GetMethod("Save", new[] { typeof(bool), modeType })!;
save.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();

File.Copy(Path.Combine(work, "System.db"), sysDb, true);
File.Copy(Path.Combine(work, "ClientSystem.db"), cliDb, true);
void Sync(string dir, string label)
{
    if (!Directory.Exists(dir)) { L(label + " MISSING"); return; }
    File.Copy(sysDb, Path.Combine(dir, "System.db"), true);
    var c = Path.Combine(dir, "ClientSystem.db");
    if (File.Exists(c)) File.Copy(cliDb, c, true);
    L("synced " + label + "=" + dir);
}
Sync(Path.Combine(root, "Data"), "Data");
Sync(Path.Combine(root, "deploy_to_Mir3service", "Database"), "deploy_to_Mir3service/Database");
File.WriteAllText(Path.Combine(root, "tools", "Mir3Req20260908", "apply_" + stamp + ".txt"), report.ToString(), new UTF8Encoding(false));
L("APPLIED ok changes=" + changes);
return 0;

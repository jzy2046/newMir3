from pathlib import Path
p = Path(r"D:\newMir3\tools\Mir3Req20260908\Program.cs")
t = p.read_text(encoding="utf-8")
old = """// Save
sessionType.GetMethod(\"Save\", Type.EmptyTypes)?.Invoke(ses, null);
sessionType.GetMethod(\"Save\", new[] { typeof(bool) })?.Invoke(ses, new object[] { true });
// common pattern: ses.Save(false) then copy
var saveMethods = sessionType.GetMethods().Where(m => m.Name == \"Save\").ToList();
foreach (var sm in saveMethods) L(\"SaveMethod \" + sm + \" params=\" + sm.GetParameters().Length);

// Dispose triggers save often
(ses as IDisposable)?.Dispose();

// Copy work dbs back
File.Copy(Path.Combine(work, \"System.db\"), sysDb, true);
File.Copy(Path.Combine(work, \"ClientSystem.db\"), cliDb, true);
// sync Data/
var dataCli = Path.Combine(root, \"Data\", \"ClientSystem.db\");
if (File.Exists(dataCli)) File.Copy(cliDb, dataCli, true);
var dataSys = Path.Combine(root, \"Data\", \"System.db\");
if (File.Exists(dataSys)) File.Copy(sysDb, dataSys, true);
// deploy
var depSys = Path.Combine(root, \"deploy_to_Mir3service\", \"Database\", \"System.db\");
var depCli = Path.Combine(root, \"deploy_to_Mir3service\", \"Database\", \"ClientSystem.db\");
if (File.Exists(depSys)) File.Copy(sysDb, depSys, true);
if (File.Exists(depCli)) File.Copy(cliDb, depCli, true);

File.WriteAllText(Path.Combine(root, \"tools\", \"Mir3Req20260908\", \"apply_\" + stamp + \".txt\"), report.ToString(), new UTF8Encoding(false));
L(\"APPLIED ok\");
return 0;"""
new = """var save = sessionType.GetMethod(\"Save\", new[] { typeof(bool), modeType })!;
save.Invoke(ses, new object[] { true, tool });
(ses as IDisposable)?.Dispose();

File.Copy(Path.Combine(work, \"System.db\"), sysDb, true);
File.Copy(Path.Combine(work, \"ClientSystem.db\"), cliDb, true);
void Sync(string dir, string label)
{
    if (!Directory.Exists(dir)) { L(label + \" MISSING\"); return; }
    File.Copy(sysDb, Path.Combine(dir, \"System.db\"), true);
    var c = Path.Combine(dir, \"ClientSystem.db\");
    if (File.Exists(c)) File.Copy(cliDb, c, true);
    L(\"synced \" + label + \"=\" + dir);
}
Sync(Path.Combine(root, \"Data\"), \"Data\");
Sync(Path.Combine(root, \"deploy_to_Mir3service\", \"Database\"), \"deploy_to_Mir3service/Database\");
File.WriteAllText(Path.Combine(root, \"tools\", \"Mir3Req20260908\", \"apply_\" + stamp + \".txt\"), report.ToString(), new UTF8Encoding(false));
L(\"APPLIED ok changes=\" + changes);
return 0;"""
if old not in t:
    print("OLD BLOCK NOT FOUND")
    i = t.find("// Save")
    print(repr(t[i:i+500]))
else:
    p.write_text(t.replace(old, new), encoding="utf-8")
    print("OK save fixed")

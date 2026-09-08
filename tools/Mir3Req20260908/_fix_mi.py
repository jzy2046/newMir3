import pathlib
p = pathlib.Path(r"D:\newMir3\tools\Mir3Req20260908\Program.cs")
t = p.read_text(encoding="utf-8")
t = t.replace("object? FindCreate(Type t)", "MethodInfo? FindCreate(Type t)")
t = t.replace(
"""object? FindCreate(Type t)
{
    var col = get.MakeGenericMethod(t).Invoke(ses, null)!;
    var m = col.GetType().GetMethods().FirstOrDefault(mi => mi.Name == \"CreateNewObject\" && mi.GetParameters().Length == 0)
         ?? col.GetType().GetMethods().FirstOrDefault(mi => mi.Name.Contains(\"Create\") && mi.GetParameters().Length == 0);
    return m;
}""",
"""MethodInfo? FindCreate(Type t)
{
    var col = get.MakeGenericMethod(t).Invoke(ses, null)!;
    return col.GetType().GetMethods().FirstOrDefault(mi => mi.Name == \"CreateNewObject\" && mi.GetParameters().Length == 0)
        ?? col.GetType().GetMethods().FirstOrDefault(mi => mi.Name.Contains(\"Create\") && mi.GetParameters().Length == 0);
}""")
# simpler: just fix signature if replace failed
if "MethodInfo? FindCreate" not in t:
    t = t.replace("object? FindCreate(Type t)", "MethodInfo? FindCreate(Type t)")
p.write_text(t, encoding="utf-8")
print("MethodInfo?", "MethodInfo? FindCreate" in t)
print("object? FindCreate", "object? FindCreate" in t)

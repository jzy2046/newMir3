from pathlib import Path
p = Path(r"D:\newMir3\tools\Mir3Req20260908\Program.cs")
t = p.read_text(encoding="utf-8")
# Replace summon lookup block more loosely
needle = 'var summonSk = mons.FirstOrDefault(m => S(m, "MonsterName") == "召唤骷髅" || S(m, "MonsterName").Contains("召唤骷髅"));'
if needle not in t:
    print("needle missing")
    # show nearby
    i = t.find("超强骷髅")
    print(repr(t[i:i+400]))
else:
    t = t.replace(
        'var summonSk = mons.FirstOrDefault(m => S(m, "MonsterName") == "召唤骷髅" || S(m, "MonsterName").Contains("召唤骷髅"));',
        'var summonSk = mons.FirstOrDefault(m => S(m, "MonsterName") == "召唤骷髅") ?? mons.FirstOrDefault(m => S(m, "MonsterName") == "骷髅");'
    )
    p.write_text(t, encoding="utf-8")
    print("OK fallback to 骷髅")

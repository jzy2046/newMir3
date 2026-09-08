# -*- coding: utf-8 -*-
"""Wave4 item1 fix: suppress skill tips + restore 精炼等级 tip; rebuild TipZero; pack v11."""
from __future__ import annotations
import gzip, hashlib, shutil, struct, zipfile, subprocess, re
from datetime import datetime
from pathlib import Path

ROOT = Path(r"D:\newMir3")
MIR3Z = next(
    p
    for p in Path(r"D:\BaiduNetdiskDownload").glob("*传奇3z*")
    for p in [next(x for x in p.rglob("mir3z") if (x / "Source" / "145Client").is_dir())]
)
PC_GS = MIR3Z / "Source" / "145Client" / "Scenes" / "GameScene.cs"
MOB_GS = MIR3Z / "Source" / "Mir3.Mobile" / "Client" / "Scenes" / "GameScene.cs"
TRACK_PC = ROOT / "Source" / "145Client" / "Scenes" / "GameScene.cs"
TRACK_MOB = ROOT / "Source" / "Mir3.Mobile" / "Scenes" / "GameScene.cs"
TIP_OUT = MIR3Z / "Source" / "145Client" / "bin" / "TipZeroRebuild"
CSPROJ = MIR3Z / "Source" / "145Client" / "145Client.csproj"
MSBUILD = Path(r"C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe")

SKILLS = [
    "天怒之火", "天之怒火", "陨冰杀", "电闪雷鸣", "旋风墙", "护身法盾", "灵魂分裂",
    "吸星大法", "养生术", "暗鬼阵", "新传染", "施毒大法", "分身术", "焰魔召唤术",
    "魔焰强解术", "君临步", "屠龙斩", "金刚之躯", "快刀斩马", "运气术", "天雷锤",
    "挑衅", "破空斩",
]

REFINE_MARKER = "REFINELV_TIP_20260908"
SKILL_MARKER = "SKILL_TIP_SUPPRESS_20260908"

REFINE_BLOCK = r'''
            // ''' + REFINE_MARKER + r''' — 精炼大师 tip: 精炼等级： (n/6)
            if (MouseItem?.FullItemStats != null)
            {
                Stat refineTrack = Stat.None;
                int refinePer = 0;
                switch (displayInfo.ItemType)
                {
                    case ItemType.Weapon:
                        refineTrack = Stat.CriticalDamage; refinePer = 5; break;
                    case ItemType.Necklace:
                    case ItemType.Bracelet:
                    case ItemType.Ring:
                        refineTrack = Stat.CriticalChance; refinePer = 1; break;
                    case ItemType.Armour:
                    case ItemType.Helmet:
                    case ItemType.Shoes:
                        refineTrack = Stat.Health; refinePer = 10; break;
                }
                if (refinePer > 0)
                {
                    int refineAmount = 0;
                    foreach (FullItemStat fis in MouseItem.FullItemStats)
                    {
                        if (fis.StatSource == StatSource.Enhancement && fis.Stat == refineTrack)
                            refineAmount += fis.Amount;
                    }
                    int refineLv = refineAmount / refinePer;
                    if (refineLv < 0) refineLv = 0;
                    if (refineLv > 6) refineLv = 6;
                    label = new DXLabel
                    {
                        ForeColour = Color.MediumPurple,
                        Location = new Point(4, ItemLabel.DisplayArea.Bottom),
                        Parent = ItemLabel,
                        Text = string.Format("精炼等级： ({0}/6)", refineLv),
                    };
                    ItemLabel.Size = new Size(label.DisplayArea.Right + 4 > ItemLabel.Size.Width ? label.DisplayArea.Right + 4 : ItemLabel.Size.Width,
                        label.DisplayArea.Bottom > ItemLabel.Size.Height ? label.DisplayArea.Bottom : ItemLabel.Size.Height);
                    ItemLabel.Size = new Size(ItemLabel.Size.Width, ItemLabel.Size.Height + 3);
                }
            }
'''

SKILL_HELPER = r'''
        // ''' + SKILL_MARKER + r'''
        private static readonly System.Collections.Generic.HashSet<string> SuppressMagicTipNames = new System.Collections.Generic.HashSet<string>
        {
            ''' + ",\n            ".join(f'@"{s}"' for s in SKILLS) + r'''
        };
        private static bool ShouldSuppressMagicTip(MagicInfo info)
        {
            if (info == null) return true;
            string n = info.Name;
            return !string.IsNullOrEmpty(n) && SuppressMagicTipNames.Contains(n);
        }
'''


def patch_gamescene(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    changed = False

    if REFINE_MARKER not in text:
        # insert refine tip just before switch (displayInfo.ItemType) that has case ItemType.Weapon + NonRefinable
        anchor = "switch (displayInfo.ItemType)\n            {\n                case ItemType.Weapon:\n                    if ((MouseItem.Flags & UserItemFlags.NonRefinable) == UserItemFlags.NonRefinable) break;"
        # allow slight whitespace variance
        m = re.search(
            r"switch\s*\(\s*displayInfo\.ItemType\s*\)\s*\{\s*case\s+ItemType\.Weapon\s*:\s*if\s*\(\(MouseItem\.Flags\s*&\s*UserItemFlags\.NonRefinable\)\s*==\s*UserItemFlags\.NonRefinable\)\s*break;",
            text,
            re.S,
        )
        if not m:
            # looser: find first NonRefinable break under Weapon in tip
            idx = text.find("case ItemType.Weapon:\n                    if ((MouseItem.Flags & UserItemFlags.NonRefinable)")
            if idx < 0:
                idx = text.find("case ItemType.Weapon:")
                # find NonRefinable near it
            if idx < 0:
                raise SystemExit(f"refine anchor not found in {path}")
            # walk back to switch
            sw = text.rfind("switch (displayInfo.ItemType)", 0, idx)
            if sw < 0:
                raise SystemExit(f"switch anchor not found in {path}")
            text = text[:sw] + REFINE_BLOCK + "\n            " + text[sw:]
        else:
            text = text[: m.start()] + REFINE_BLOCK + "\n            " + text[m.start() :]
        changed = True
        print(f"  + refine tip inserted: {path}")
    else:
        print(f"  = refine tip already present: {path}")

    if SKILL_MARKER not in text:
        # insert helper before CreateMagicLabel
        needle = "        private void CreateMagicLabel()"
        if needle not in text:
            raise SystemExit(f"CreateMagicLabel not found in {path}")
        text = text.replace(needle, SKILL_HELPER + "\n" + needle, 1)
        # early return inside CreateMagicLabel
        old = "        private void CreateMagicLabel()\n        {\n            if (MouseMagic != null)\n            {"
        new = (
            "        private void CreateMagicLabel()\n        {\n"
            "            if (ShouldSuppressMagicTip(MouseMagic)) return; // " + SKILL_MARKER + "\n"
            "            if (MouseMagic != null)\n            {"
        )
        if old not in text:
            # try without exact indent of brace block
            old2 = "        private void CreateMagicLabel()\n        {\n            if (MouseMagic == null) return;"
            if old2 in text:
                text = text.replace(
                    old2,
                    "        private void CreateMagicLabel()\n        {\n            if (ShouldSuppressMagicTip(MouseMagic)) return; // "
                    + SKILL_MARKER
                    + "\n            if (MouseMagic == null) return;",
                    1,
                )
            else:
                # after opening brace of CreateMagicLabel
                m2 = re.search(r"private void CreateMagicLabel\(\)\s*\{\s*", text)
                if not m2:
                    raise SystemExit(f"cannot patch CreateMagicLabel body in {path}")
                insert_at = m2.end()
                text = (
                    text[:insert_at]
                    + "\n            if (ShouldSuppressMagicTip(MouseMagic)) return; // "
                    + SKILL_MARKER
                    + "\n"
                    + text[insert_at:]
                )
        else:
            text = text.replace(old, new, 1)
        changed = True
        print(f"  + skill tip suppress inserted: {path}")
    else:
        print(f"  = skill tip suppress already present: {path}")

    if text != orig:
        path.write_text(text, encoding="utf-8")
        changed = True
    return changed


def md5_file(path: Path) -> bytes:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.digest()


def gzip_file(src: Path, dst: Path) -> int:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(src, "rb") as fin, gzip.open(dst, "wb", compresslevel=9) as fout:
        shutil.copyfileobj(fin, fout)
    return dst.stat().st_size


def read_plist(path: Path):
    entries = []
    data = path.read_bytes()
    i = 0
    n = len(data)
    while i < n:
        length = 0
        shift = 0
        while True:
            b = data[i]
            i += 1
            length |= (b & 0x7F) << shift
            if (b & 0x80) == 0:
                break
            shift += 7
        name = data[i : i + length].decode("utf-8")
        i += length
        clen = struct.unpack_from("<q", data, i)[0]
        i += 8
        cslen = struct.unpack_from("<i", data, i)[0]
        i += 4
        checksum = data[i : i + cslen]
        i += cslen
        entries.append([name, clen, checksum])
    return entries


def write_7bit_int(val: int) -> bytes:
    out = bytearray()
    while True:
        b = val & 0x7F
        val >>= 7
        if val:
            out.append(b | 0x80)
        else:
            out.append(b)
            break
    return bytes(out)


def write_plist(path: Path, entries):
    buf = bytearray()
    for name, clen, checksum in entries:
        nb = name.encode("utf-8")
        buf += write_7bit_int(len(nb))
        buf += nb
        buf += struct.pack("<q", clen)
        buf += struct.pack("<i", len(checksum))
        buf += checksum
    path.write_bytes(buf)


def main():
    print("MIR3Z", MIR3Z)
    assert PC_GS.is_file(), PC_GS
    assert MOB_GS.is_file(), MOB_GS
    assert MSBUILD.is_file(), MSBUILD

    print("PATCH PC")
    patch_gamescene(PC_GS)
    print("PATCH MOBILE")
    patch_gamescene(MOB_GS)

    # sync tracked copies in newMir3
    TRACK_PC.parent.mkdir(parents=True, exist_ok=True)
    TRACK_MOB.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PC_GS, TRACK_PC)
    # mobile tracked path differs; copy content
    shutil.copy2(MOB_GS, TRACK_MOB)
    print("synced tracked GameScene copies")

    # rebuild tip client into TipZeroRebuild
    TIP_OUT.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(MSBUILD),
        str(CSPROJ),
        "/t:Rebuild",
        "/p:Configuration=Release",
        f"/p:OutputPath={TIP_OUT}\\",
        "/v:m",
        "/nologo",
    ]
    print("BUILD", " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    (ROOT / "tools" / "wave4_item1_build_out.txt").write_text(
        (r.stdout or "") + "\n" + (r.stderr or ""), encoding="utf-8"
    )
    print("build exit", r.returncode)
    if r.returncode != 0:
        print(r.stdout[-2000:] if r.stdout else "")
        print(r.stderr[-2000:] if r.stderr else "")
        raise SystemExit("MSBuild failed")

    tip_exe = TIP_OUT / "Mir3.exe"
    tip_game = TIP_OUT / "Mir3Game.exe"
    assert tip_exe.is_file(), tip_exe
    if not tip_game.is_file():
        shutil.copy2(tip_exe, tip_game)

    raw = tip_exe.read_bytes()
    has_refine = "精炼等级".encode("utf-16le") in raw
    has_suppress = SKILL_MARKER.encode("utf-16le") in raw or "天怒之火".encode("utf-16le") in raw
    has_tipzero = "TIPZERO_ATKSPD_HIDE".encode("utf-16le") in raw
    tip_md5 = md5_file(tip_exe).hex()
    print(f"TIP size={tip_exe.stat().st_size} md5={tip_md5} refine={has_refine} suppress={has_suppress} tipzero={has_tipzero}")
    if not has_refine:
        raise SystemExit("精炼等级 marker missing from rebuilt tip exe")

    # pack v11 flat
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    latest_db = ROOT / "Database" / "ClientSystem.db"
    base = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v10"
    out = ROOT / "patches_ready_20260906" / "PC_upload_overwrite_v11"
    zip_out = ROOT / "patches_ready_20260906" / "PC_upload_v11_wave4_item1.zip"
    out.mkdir(parents=True, exist_ok=True)
    for f in list(out.iterdir()):
        if f.is_file():
            f.unlink()

    clen_mir3 = gzip_file(tip_exe, out / "Mir3.exe.gz")
    clen_game = gzip_file(tip_exe, out / "Mir3Game.exe.gz")  # same bytes
    clen_db = gzip_file(latest_db, out / "Data-ClientSystem.db.gz")
    csum_exe = md5_file(tip_exe)
    csum_db = md5_file(latest_db)

    entries = read_plist(base / "PList.Bin")
    ship = {
        "mir3.exe": (clen_mir3, csum_exe, "Mir3.exe"),
        "mir3game.exe": (clen_game, csum_exe, "Mir3Game.exe"),
        r"data\clientsystem.db": (clen_db, csum_db, r"Data\ClientSystem.db"),
    }
    found = set()
    for e in entries:
        key = e[0].replace("/", "\\").lower()
        if key in ship:
            clen, csum, canon = ship[key]
            e[0] = canon
            e[1] = clen
            e[2] = csum
            found.add(key)
            print("UPDATED", canon, clen, csum.hex())
    for key, (clen, csum, canon) in ship.items():
        if key not in found:
            entries.append([canon, clen, csum])
            print("APPENDED", canon)

    write_plist(out / "PList.Bin", entries)
    readme = "\n".join(
        [
            f"PC 20260908 wave4-item1 pack v11 stamp={stamp}",
            "Fixes: suppress skill TIP UI for listed magics; restore 精炼等级：(n/6) tip.",
            f"Mir3.exe size={tip_exe.stat().st_size} md5={tip_md5} refine={has_refine} tipzero={has_tipzero}",
            f"ClientSystem.db size={latest_db.stat().st_size} md5={csum_db.hex()}",
            "Flat 7091 overwrite: PList.Bin + Mir3.exe.gz + Mir3Game.exe.gz + Data-ClientSystem.db.gz",
            "NEVER overwrite Server.exe/Library.dll",
            f"  PList.Bin                 {(out / 'PList.Bin').stat().st_size}",
            f"  Mir3.exe.gz               {clen_mir3}",
            f"  Mir3Game.exe.gz           {clen_game}",
            f"  Data-ClientSystem.db.gz   {clen_db}",
            "",
        ]
    )
    (out / "README_OVERWRITE.txt").write_text(readme, encoding="utf-8")

    if zip_out.exists():
        zip_out.unlink()
    with zipfile.ZipFile(zip_out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.iterdir()):
            if f.is_file():
                zf.write(f, f.name)
                print("ZIP", f.name, f.stat().st_size)
    print("ZIP_OUT", zip_out, zip_out.stat().st_size)
    print("OUT_DIR", out)
    print("DONE")


if __name__ == "__main__":
    main()

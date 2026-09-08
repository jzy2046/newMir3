import sys, os
sys.stdout.reconfigure(encoding="utf-8")
needles = ["AccessoryCombine", "石榴石", "结晶石", "CombineSuccess", "Accessory", "SafeZone", "分割线", "ItemTip", "GameGold", "Identify"]
roots = [r"D:\newMir3\Source", r"D:\newMir3\tools\_decompile", r"D:\newMir3\tools\_src_mirdb"]
for root in roots:
  if not os.path.isdir(root):
    print("skip", root); continue
  for dirpath, dirs, files in os.walk(root):
    # prune huge
    dirs[:] = [d for d in dirs if d not in (".git","node_modules","bin","obj")]
    for f in files:
      if not f.endswith((".cs",".xaml",".py",".txt",".md")): continue
      p=os.path.join(dirpath,f)
      try:
        # only read smaller files partially
        size=os.path.getsize(p)
        if size>5_000_000: continue
        with open(p,encoding="utf-8",errors="ignore") as fh:
          data=fh.read()
      except: continue
      hits=[k for k in needles if k in data]
      if hits:
        print(p[12:], "=>", hits)

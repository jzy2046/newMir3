# VPS NPC scripts (IronPython Lib)

Server.exe uses IronPython 2.7 to load Scripts\main.py. Do NOT install Python 3. Do NOT need C:\Python27.

## After git pull

1. Copy the whole Scripts folder (must include Scripts\Lib) next to Server.exe on the VPS.
   Example: D:\Mirserver3\Mir3\Scripts
2. Restart Server.exe
3. Console should show loading PY scripts timing (jia zai PY jiao ben). Should NOT show:
   NpcEvent Error loading plugin : KeyError
   D-key plugin delay KeyError

## Lib sources

- IronPython 2.7.12 Lib (github.com/IronLanguages/ironpython2 ipy-2.7.12)
- xlrd 1.2.0, xlwt 1.3.0, xlutils 2.0.0
- IronPython.Modules.dll and IronPython.SQLite.dll already sit next to Server.exe

## Residual risk

- If Database\TaskLists xls is missing, NPC can talk but quest table reads fail
- Shitu system also uses xlrd/xlutils
- requests egg is no longer on sys.path; current scripts do not import requests

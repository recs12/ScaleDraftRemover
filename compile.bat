:: Set this file for compiling the executable.
:: So it can be added to the user custom theme in solidedge.
ipyc.exe /main:__main__.py ^
scale.py ^
Interop.SolidEdge.dll ^
/embed ^
/out:ScaleDraftRemover ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:icon.ico

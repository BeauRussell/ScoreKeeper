from cx_Freeze import setup, Executable

base = "Win32GUI"    

executables = [Executable("scorekeeper.py", base=base)]

packages = ["tkinter", "scoreEntryTab", "settingsTab", "yaml"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ScoreKeeper",
    options = options,
    version = "0.1",
    description = 'A program to keep scores throughout a season.',
    executables = executables
)
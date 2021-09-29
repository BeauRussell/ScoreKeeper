from cx_Freeze import setup, Executable

base = None    

executables = [Executable("scorekeeper.py", base=base)]

packages = ["tkinter", "scoreEntryTab", "settingsTab", "pyyaml"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ScoreKeeper",
    options = options,
    version = "0.02",
    description = 'A program to keep scores throughout a season.',
    executables = executables
)
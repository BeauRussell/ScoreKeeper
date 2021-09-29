from cx_Freeze import setup, Executable

base = None    

executables = [Executable("scorekeeper.py", base=base)]

packages = ["idna", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ScoreKeeper",
    options = options,
    version = "0.01",
    description = 'A program to keep scores throughout a season.',
    executables = executables
)
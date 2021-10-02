from cx_Freeze import setup, Executable

base = "Win32GUI"    

executables = [Executable("scorekeeper.py", base=base)]

includeFiles = ['refresh.png']
packages = ["tkinter", "yaml", "os", "PIL"]
options = {
    'build_exe': {    
        'packages':packages,
        'include_files': includeFiles
    },    
}

setup(
    name = "ScoreKeeper",
    options = options,
    version = "1.0",
    description = 'A program to keep scores throughout a season.',
    executables = executables
)
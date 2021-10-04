from tkinter import *
from tkinter import ttk

from scoreEntryTab import *
from settingsTab import *
from gameSettingsTab import *
from data import checkOrCreateRequiredFiles
from licensing import getAuthenticated

class ScoreKeeper(Tk):
    def __init__(self):
        # Create games directory if it does not exist
        checkOrCreateRequiredFiles()

        getAuthenticated()

        Tk.__init__(self)
        self.geometry("500x275")
        self.title("ScoreKeeper")

        notebook = ttk.Notebook(self, height=250, width=450)

        score_entry_frame = ScoreEntryTab(notebook)
        game_settings_frame = GameSettingsTab(notebook)
        settings_frame = SettingsTab(notebook)
        score_entry_frame.pack(fill="both", expand=1)
        game_settings_frame.pack(fill="both", expand=1)
        settings_frame.pack(fill="both", expand=1)

        notebook.add(score_entry_frame, text="Score Entry")
        notebook.add(game_settings_frame, text="Game Settings")
        notebook.add(settings_frame, text="Settings")
        notebook.pack()



app = ScoreKeeper()
app.mainloop()
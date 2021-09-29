from tkinter import *
from tkinter import ttk

from scoreEntryTab import *

class ScoreKeeper(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x275")
        self.title("ScoreKeeper")

        notebook = ttk.Notebook(self, height=300, width=500)

        score_entry_frame = ScoreEntryTab(notebook)
        settings_frame = Frame(notebook)
        score_entry_frame.pack(fill="both", expand=1)
        settings_frame.pack(fill="both", expand=1)

        notebook.add(score_entry_frame, text="Score Entry")
        notebook.add(settings_frame, text="Settings")
        notebook.pack()



app = ScoreKeeper()
app.mainloop()
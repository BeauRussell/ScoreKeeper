from tkinter import *
from tkinter import ttk

from data import saveSettings, loadGames

class SettingsTab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.build_widgets()
        
        
    def build_widgets(self):
        self.build_games_input()

        self.submit_button = Button(self, text="Update", command=self.on_save)
        self.submit_button.grid (row=50, column=2, pady=10)
        

    def build_games_input(self):
        self.game_title = Label(self, text="List of Games (Separated by Commas)")
        self.game_list = Text(self, width=25, height=5)
        games_saved = loadGames()
        if games_saved:
            games_saved = ", ".join(games_saved)
            self.game_list.insert(END, games_saved)

        self.game_title.grid(column=0, row=0)
        self.game_list.grid(column=0, row=1, columnspan=2)

    
    def on_save(self):
        data = {
            "games": []
        }
        games = self.game_list.get("1.0", END).split(",")
        for game in games:
            name = game.strip()
            name = name.strip('\n')
            data["games"].append(name)

        saveSettings(data)

    
    def validate_int(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
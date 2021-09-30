from tkinter import *
from tkinter import ttk

from data import loadGames, checkForOrCreateSpecificGameDirectory, checkForOrCreateSeasonDirectory

class ScoreEntryTab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.build_widgets()
        
        
    def build_widgets(self):
        self.build_game_input()

        self.build_score_inputs()

        self.submit_button = Button(self, text="Update", command=self.on_save)
        self.submit_button.grid (row=50, column=2, pady=10)
        

    def build_game_input(self):
        self.game_title = Label(self, text="Game")

        verify_intcmd = (self.register(self.validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        choices = loadGames()
        if not choices:
            choices = ['-- No Games Set Up --']

        self.game = StringVar(self)
        self.game.set(choices[0])
        self.game_widget = OptionMenu(self, self.game, *choices)

        self.season_label = Label(self, text="Season #:")
        self.season_number = Entry(self, width="2")
        self.season_number.insert(0, "Kills")
        self.season_number = Entry(self, validate = 'key', validatecommand = verify_intcmd)

        self.game_title.grid(row=0,column=0)
        self.game_widget.grid(row=0,column=1)
        self.season_label.grid(row=0,column=2)
        self.season_number.grid(row=0,column=3)

    
    def build_score_inputs(self):
        self.team_name_label = Label(self, text="Team Name")
        self.team_name_entry = Entry(self, width="32", justify="center")

        verify_intcmd = (self.register(self.validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.custom_scores_label = Label(self, text="Custom Scores")
        self.custom_scores_key_label = Label(self, text="Score Key")
        self.custom_scores_value_label = Label(self, text="Score Value")

        self.custom_score_label_1 = Label(self, text="Score #1")
        self.custom_score_name_1 = Entry(self)
        self.custom_score_name_1.insert(0, "Kills")
        self.custom_score_value_1 = Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_1.insert(0, "0")

        self.custom_score_label_2 = Label(self, text="Score #2")
        self.custom_score_name_2 = Entry(self)
        self.custom_score_value_2 = Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_2.insert(0, "0")

        self.custom_score_label_3 = Label(self, text="Score #3")
        self.custom_score_name_3 = Entry(self)
        self.custom_score_value_3 = Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_3.insert(0, "0")

        self.custom_score_label_4 = Label(self, text="Score #4")
        self.custom_score_name_4 = Entry(self)
        self.custom_score_value_4 = Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_4.insert(0, "0")

        self.custom_score_label_5 = Label(self, text="Score #5")
        self.custom_score_name_5 = Entry(self)
        self.custom_score_value_5 = Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_5.insert(0, "0")

        # Team name entry placement
        self.team_name_label.grid(row=1,column=0, pady=10)
        self.team_name_entry.grid(row=1,column=1, columnspan=2)

        # Custom Scores Headers placement
        self.custom_scores_label.grid(row=2,column=0)
        self.custom_scores_key_label.grid(row=2,column=1)
        self.custom_scores_value_label.grid(row=2,column=2)

        # Custom Score #1 placement
        self.custom_score_label_1.grid(row=3,column=0)
        self.custom_score_name_1.grid(row=3,column=1)
        self.custom_score_value_1.grid(row=3,column=2)
        
        # Custom Score #2 placement
        self.custom_score_label_2.grid(row=4,column=0)
        self.custom_score_name_2.grid(row=4,column=1)
        self.custom_score_value_2.grid(row=4,column=2)
        
        # Custom Score #3 placement
        self.custom_score_label_3.grid(row=5,column=0)
        self.custom_score_name_3.grid(row=5,column=1)
        self.custom_score_value_3.grid(row=5,column=2)
        
        # Custom Score #4 placement
        self.custom_score_label_4.grid(row=6,column=0)
        self.custom_score_name_4.grid(row=6,column=1)
        self.custom_score_value_4.grid(row=6,column=2)
        
        # Custom Score #5 placement
        self.custom_score_label_5.grid(row=7,column=0)
        self.custom_score_name_5.grid(row=7,column=1)
        self.custom_score_value_5.grid(row=7,column=2)

    
    def on_save(self):
        data = {
            'game': self.game.get(),
            'team': self.team_name_entry.get(),
            'season': self.season_number.get(),
            'custom1': {'name': self.custom_score_name_1.get(), 'value': self.custom_score_value_1.get()},
            'custom2': {'name': self.custom_score_name_2.get(), 'value': self.custom_score_value_2.get()},
            'custom3': {'name': self.custom_score_name_3.get(), 'value': self.custom_score_value_3.get()},
            'custom4': {'name': self.custom_score_name_4.get(), 'value': self.custom_score_value_4.get()},
            'custom5': {'name': self.custom_score_name_5.get(), 'value': self.custom_score_value_5.get()}
        }

        path = checkForOrCreateSpecificGameDirectory(data["game"])
        path = checkForOrCreateSeasonDirectory(path, data["season"])
        print(data)

    
    def validate_int(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
import tkinter as tk

class ScoreKeeper(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x300")
        self.title("ScoreKeeper")

        self.build_widgets()
        
        
    def build_widgets(self):
        self.build_game_input()

        self.build_score_inputs()

        self.submit_button = tk.Button(self, text="Update", command=self.on_save)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)

        


    def build_game_input(self):
        self.game_title = tk.Label(self, text="Game")

        verify_intcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        choices = ["Hunt: Showdown"]
        self.game = tk.StringVar(self)
        self.game.set("Hunt: Showdown")
        self.game_widget = tk.OptionMenu(self, self.game, *choices)

        self.season_label = tk.Label(self, text="Season #:")
        self.season_number = tk.Entry(self)
        self.season_number.insert(0, "Kills")
        self.season_number = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)

        self.game_title.place(x=200, y=20)
        self.game_widget.place(x=250, y=20)
        self.season_label.place(x=450, y=20)
        self.season_number.place(x=500, y=20)

    
    def build_score_inputs(self):
        self.team_name_label = tk.Label(self, text="Team Name")
        self.team_name_entry = tk.Entry(self, width="128", justify="center")

        verify_intcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.custom_scores_label = tk.Label(self, text="Custom Scores")
        self.custom_scores_key_label = tk.Label(self, text="Score Key")
        self.custom_scores_value_label = tk.Label(self, text="Score Value")

        self.custom_score_label_1 = tk.Label(self, text="Score #1")
        self.custom_score_name_1 = tk.Entry(self)
        self.custom_score_name_1.insert(0, "Kills")
        self.custom_score_value_1 = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_1.insert(0, "0")

        self.custom_score_label_2 = tk.Label(self, text="Score #2")
        self.custom_score_name_2 = tk.Entry(self)
        self.custom_score_value_2 = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_2.insert(0, "0")

        self.custom_score_label_3 = tk.Label(self, text="Score #3")
        self.custom_score_name_3 = tk.Entry(self)
        self.custom_score_value_3 = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_3.insert(0, "0")

        self.custom_score_label_4 = tk.Label(self, text="Score #4")
        self.custom_score_name_4 = tk.Entry(self)
        self.custom_score_value_4 = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_4.insert(0, "0")

        self.custom_score_label_5 = tk.Label(self, text="Score #5")
        self.custom_score_name_5 = tk.Entry(self)
        self.custom_score_value_5 = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_5.insert(0, "0")

        # Team name entry placement
        self.team_name_label.place(x=350, y=60)
        self.team_name_entry.place(x=10, y=80)

        # Custom Scores Headers placement
        self.custom_scores_label.place(x=350, y=100)
        self.custom_scores_key_label.place(x=275, y=120)
        self.custom_scores_value_label.place(x=400, y=120)

        # Custom Score #1 placement
        self.custom_score_label_1.place(x=200, y=140)
        self.custom_score_name_1.place(x=275, y=140)
        self.custom_score_value_1.place(x=400, y=140)
        
        # Custom Score #2 placement
        self.custom_score_label_2.place(x=200, y=160)
        self.custom_score_name_2.place(x=275, y=160)
        self.custom_score_value_2.place(x=400, y=160)
        
        # Custom Score #3 placement
        self.custom_score_label_3.place(x=200, y=180)
        self.custom_score_name_3.place(x=275, y=180)
        self.custom_score_value_3.place(x=400, y=180)
        
        # Custom Score #4 placement
        self.custom_score_label_4.place(x=200, y=200)
        self.custom_score_name_4.place(x=275, y=200)
        self.custom_score_value_4.place(x=400, y=200)
        
        # Custom Score #5 placement
        self.custom_score_label_5.place(x=200, y=220)
        self.custom_score_name_5.place(x=275, y=220)
        self.custom_score_value_5.place(x=400, y=220)

    
    def on_save(self):
        data = {
            'game': ''.join( e for e in self.game.get() if e.isalnum()),
            'team': self.team_name_entry.get(),
            'season': self.season_number.get(),
            'custom1': {'name': self.custom_score_name_1.get(), 'value': self.custom_score_value_1.get()},
            'custom2': {'name': self.custom_score_name_2.get(), 'value': self.custom_score_value_2.get()},
            'custom3': {'name': self.custom_score_name_3.get(), 'value': self.custom_score_value_3.get()},
            'custom4': {'name': self.custom_score_name_4.get(), 'value': self.custom_score_value_4.get()},
            'custom5': {'name': self.custom_score_name_5.get(), 'value': self.custom_score_value_5.get()}
        }
        print(data)


    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False



app = ScoreKeeper()
app.mainloop()
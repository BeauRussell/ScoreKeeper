import tkinter as tk

class ScoreKeeper(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x200")
        self.title("ScoreKeeper")

        self.build_widgets()
        
        
    def build_widgets(self):
        self.build_game_input()

        self.build_score_inputs()

        self.submit_button = tk.Button(self, text="Update", command=self.on_save)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)

        


    def build_game_input(self):
        self.game_title = tk.Label(self, text="Game")
        
        choices = ["Hunt: Showdown"]
        self.game = tk.StringVar(self)
        self.game.set("Hunt: Showdown")
        self.game_widget = tk.OptionMenu(self, self.game, *choices)

        self.game_title.pack()
        self.game_widget.pack()

    
    def build_score_inputs(self):
        self.team_name_label = tk.Label(self, text="Team Name")
        self.team_name_entry = tk.Entry(self, width="128", justify="center")

        verify_intcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.custom_scores_label = tk.Label(self, text="Custom Scores")
        self.custom_scores_key_label = tk.Label(self, text="Score Key")
        self.custom_scores_value_label = tk.Label(self, text="Score Value")

        self.custom_score_label_1 = tk.Label(self, text="Score #1")
        self.custom_score_name_1 = tk.Entry(self)
        self.custom_score_value_1 = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.custom_score_value_1.insert(0, "0")

        # Team name entry placement
        self.team_name_label.pack()
        self.team_name_entry.pack()

        # Custom Scores Headers placement
        self.custom_scores_label.place(x=350, y=100)
        self.custom_scores_key_label.place(x=275, y=120)
        self.custom_scores_value_label.place(x=400, y=120)

        # Custom Score #1 placement
        self.custom_score_label_1.place(x=200, y=140)
        self.custom_score_name_1.place(x=275, y=140)
        self.custom_score_value_1.place(x=400, y=140)

    
    def on_save(self):
        data = {
            'game': ''.join( e for e in self.game.get() if e.isalnum()),
            'team': self.team_name_entry.get(),
            'custom1': {'name': self.custom_score_name_1.get(), 'value': self.custom_score_value_1.get()}
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
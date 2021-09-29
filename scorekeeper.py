import tkinter as tk

class ScoreKeeper(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x200")
        self.title("ScoreKeeper")

        self.build_widgets()
        
        

    def build_widgets(self):
        self.build_game_input()

        self.submit_button = tk.Button(self, text="Update", command=self.on_save)
        self.submit_button.pack()

        verify_intcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.number = tk.Entry(self, validate = 'key', validatecommand = verify_intcmd)
        self.number.insert(0, "0")
        self.number.pack()



    def build_game_input(self):
        self.game_title = tk.Label(self, text="Game")
        
        choices = ["Hunt: Showdown"]
        self.game = tk.StringVar(self)
        self.game.set("Hunt: Showdown")
        self.game_widget = tk.OptionMenu(self, self.game, *choices)


        self.game_title.pack()
        self.game_widget.pack()

    
    def on_save(self):
        data = {
            'game': ''.join( e for e in self.variable.get() if e.isalnum()),
            'number': int(self.number.get())
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
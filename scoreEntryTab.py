from tkinter import *
from PIL import Image, ImageTk

from data import loadGames, loadTeams, checkForOrCreateSpecificGameDirectory, checkForOrCreateSeasonDirectory, getGameRules, saveScore

class ScoreEntryTab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.build_widgets()
        
        
    def build_widgets(self):
        refresh = Image.open("refresh.png").resize((20, 20))
        self.refresh_image = ImageTk.PhotoImage(refresh)
        self.build_game_input()

        self.build_score_inputs()

        self.submit_button = Button(self, text="Update", command=self.on_save)
        self.submit_button.grid (row=50, column=2, pady=10)
        

    def build_game_input(self):
        self.game_title = Label(self, text="Game")

        # Set up Button to Reset the Game Menu
        self.update_games_button = Button(self, image=self.refresh_image, command=self.resetGameMenu, height=20, width=20)

        verify_intcmd = (self.register(self.validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        choices = loadGames()
        if not choices:
            choices = ['-- No Games Set Up --']

        self.game = StringVar(self)
        self.game.set(choices[0])
        self.game_widget = OptionMenu(self, self.game, *choices, command=self.reloadScoreWidgets)

        self.season_label = Label(self, text="Season #:")
        self.season_number = Entry(self, validate = 'key', validatecommand = verify_intcmd, width="2")
        self.season_number.insert(0, "1")

        self.game_title.grid(row=0,column=0)
        self.game_widget.grid(row=0,column=1)
        self.update_games_button.grid (row=0, column=2)
        self.season_label.grid(row=0,column=3)
        self.season_number.grid(row=0,column=4)

    
    def build_score_inputs(self):
        self.team_name_label = Label(self, text="Team Name")

        # Pull Team names from settings
        choices = loadTeams()
        if not choices:
            choices = ['-- No Teams Set Up --']

        self.team = StringVar(self)
        self.team.set(choices[0])
        self.team_widget = OptionMenu(self, self.team, *choices)

        # Set up Button to Reset the Game Menu
        self.update_teams_button = Button(self, image=self.refresh_image, command=self.resetTeamMenu, height=20, width=20)

        verify_intcmd = (self.register(self.validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        rules = getGameRules(self.game.get())

        self.custom_scores_label = Label(self, text="Custom Scores")
        self.custom_scores_key_label = Label(self, text="Score Key")
        self.custom_scores_value_label = Label(self, text="Score Point Value")

        self.custom_score_label_1 = Label(self, text="Score #1")
        self.custom_score_name_1 = Label(self, text = rules["custom1"]["name"] if rules else "N/A")
        self.custom_score_value_1 = Entry(self, validate = 'key', validatecommand = verify_intcmd)

        self.custom_score_label_2 = Label(self, text="Score #2")
        self.custom_score_name_2 = Label(self, text = rules["custom2"]["name"] if rules else "N/A")
        self.custom_score_value_2 = Entry(self, validate = 'key', validatecommand = verify_intcmd)

        self.custom_score_label_3 = Label(self, text = "Score #3")
        self.custom_score_name_3 = Label(self, text = rules["custom3"]["name"] if rules else "N/A")
        self.custom_score_value_3 = Entry(self, validate = 'key', validatecommand = verify_intcmd)

        self.custom_score_label_4 = Label(self, text="Score #4")
        self.custom_score_name_4 = Label(self, text = rules["custom4"]["name"] if rules else "N/A")
        self.custom_score_value_4 = Entry(self, validate = 'key', validatecommand = verify_intcmd)

        self.custom_score_label_5 = Label(self, text="Score #5")
        self.custom_score_name_5 = Label(self, text = rules["custom5"]["name"] if rules else "N/A")
        self.custom_score_value_5 = Entry(self, validate = 'key', validatecommand = verify_intcmd)

        # Team name entry placement
        self.team_name_label.grid(row=1,column=0, pady=10)
        self.team_widget.grid(row=1,column=1)
        self.update_teams_button.grid(row=1,column=2)

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
        path = checkForOrCreateSpecificGameDirectory(self.game.get())
        path = checkForOrCreateSeasonDirectory(path, self.season_number.get())
        scores = [self.custom_score_value_1.get(), self.custom_score_value_2.get(), self.custom_score_value_3.get(), self.custom_score_value_4.get(), self.custom_score_value_5.get()]
        saveScore(path, self.team.get(), scores)

    
    def validate_int(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False


    def resetGameMenu(self):
        menu = self.game_widget["menu"]
        menu.delete(0, "end")
        for game in loadGames():
            menu.add_command(label=game, command=lambda value=game: self.game.set(value))


    def resetTeamMenu(self):
        menu = self.team_widget["menu"]
        menu.delete(0, "end")
        for team in loadTeams():
            menu.add_command(label=team, command=lambda value=team: self.team.set(value))


    def reloadScoreWidgets(self, *args):
        rules = getGameRules(self.game.get())
        self.custom_score_name_1['text'] = rules["custom1"]["name"]
        self.custom_score_name_2['text'] = rules["custom2"]["name"]
        self.custom_score_name_3['text'] = rules["custom3"]["name"]
        self.custom_score_name_4['text'] = rules["custom4"]["name"]
        self.custom_score_name_5['text'] = rules["custom5"]["name"]

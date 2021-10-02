import yaml
import os

def saveSettings(data, path=""):
    with open(r'./settings.yml', 'w') as file:
        yaml.dump(data, file)


def saveGameSettings(game, data):
    path = checkForOrCreateSpecificGameDirectory(game)
    path = path + '/settings.yml'
    with open(path, 'w') as file:
        yaml.dump(data, file)


def loadGames():
    with open(r'./settings.yml') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
        if not load is None and "games" in load:
            return load['games']
        else:
            return False


def loadTeams():
    with open(r'./settings.yml') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
        if not load is None and "teams" in load:
            return load['teams']
        else:
            return False


def checkOrCreateRequiredFiles():
    if not os.path.exists('./games'):
        os.makedirs('./games')
    if not os.path.exists('./settings.yml'):
        open('./settings.yml', 'w+').close()


def checkForOrCreateSpecificGameDirectory(game):
    scrubbed_game = ''.join( e for e in game if e.isalnum())
    path = './games/' + scrubbed_game
    if not os.path.exists(path):
        os.makedirs(path)
    
    return path


def checkForOrCreateSeasonDirectory(path, season):
    path = path + '/Season' + season
    if not os.path.exists(path):
        os.makedirs(path)

    return path


def getGameRules(game):
    path = checkForOrCreateSpecificGameDirectory(game)
    path = path + '/settings.yml'

    if not os.path.exists(path):
        return False
    
    with open(path) as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
        return load


def saveScore(path, team, scores):
    scores_file = path + '/scores.yml'
    if not os.path.exists(scores_file):
        open(scores_file, 'w+').close()
    
    with open(scores_file, 'r+') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
        if not load:
            load = {}

        if not team in load:
            load[team] = []
        load[team].append(scores)
        yaml.dump(load, file)
    
    processPoints(path)


def processPoints(path):
    scores_file = path + '/scores.yml'
    leaderboard_file = path + '/leaderboard.yml'
    settings_file = path + '/../settings.yml'

    if not os.path.exists(leaderboard_file):
        open(leaderboard_file, 'w+').close()
    
    with open(scores_file, 'r') as file:
        scores = yaml.load(file, Loader=yaml.FullLoader)
    
    with open(settings_file, 'r') as file:
        settings = yaml.load(file, Loader=yaml.FullLoader)

    totals = []
    for team in scores:
        totals.append([team, calculatePoints(scores[team], settings), len(scores[team])])
        
    leaderboard = sorted(totals,key=lambda l:l[1], reverse=True)
    with open(leaderboard_file, 'w+') as file:
        yaml.dump(leaderboard, file)



def calculatePoints(scores, settings):
    points = 0
    for game in scores:
        for index, score in enumerate(game):
            custom_num = index + 1
            if settings["custom" + str(custom_num)]["name"] == 'N/A':
                continue

            multiplier = int(settings["custom" + str(custom_num)]["value"])
            points = points + (multiplier * int(score))
    
    return points

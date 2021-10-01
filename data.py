import yaml
import os

def saveSettings(data):
    with open(r'./settings.yml', 'w') as file:
        yaml.dump(data, file)


def saveGameSettings(game, data):
    path = checkForOrCreateSpecificGameDirectory(game)
    path = path + 'settings.yml'
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

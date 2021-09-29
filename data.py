import yaml
import os

def saveSettings(data):
    print(data)
    with open(r'./settings.yml', 'w') as file:
        yaml.dump(data, file)


def loadGames():
    with open(r'./settings.yml') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
        return load['games']

def checkAndCreateGameDirectory():
    if not os.path.exists('./games'):
        os.makedirs('./games')

def checkForOrCreateSpecificGameDirectory(game):
    scrubbed_game = ''.join( e for e in game if e.isalnum())
    path = './games/' + scrubbed_game
    if not os.path.exists(path):
        os.makedirs(path)
    
    return path
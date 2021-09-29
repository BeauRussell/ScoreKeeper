import yaml

def saveSettings(data):
    print(data)
    with open(r'./settings.yml', 'w') as file:
        yaml.dump(data, file)


def loadGames():
    with open(r'./settings.yml') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
        return load['games']
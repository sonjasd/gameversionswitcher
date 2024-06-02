import csv
import os
import yaml
from time import sleep

# config paths
cfg = "configs/config.yaml"

def addGame(cfg):
    with open(cfg, "r") as f:
        data = yaml.safe_load(f)
        sapps_path = data["SteamApps"]
    while True:
        gamename = input("\nEnter game name: ")
        if not os.path.exists(sapps_path + gamename):
            print("\nInvalid game name, please enter it as in steamapps folder")
            sleep(1)
        if not os.path.exists(f'configs/games/{gamename}'):
            os.makedirs(f'configs/games/{gamename}')

            # make a file to save information about saved game instances
            data = [
                ['ID', 'Name', "Current"]
            ]
            with open(f'configs/games/{gamename}/instances.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            break

        else:
            print("\nGame already added!")
            sleep(1)

def greeter():
    print("\nWelcome to Game Version Switcher")
    printedLine = '\n[0] Add new game '
    folderslist = os.listdir('configs/games')

    amountGames = len(folderslist)

    for game in range(0, amountGames):
        printedLine += f'[{game+1}] {folderslist[game]} '
    
    print(printedLine)
    selection = input('\n')
    
    if selection == "0":
        addGame(cfg=cfg)
    else:
        print("selected here")


#check for config
if not os.path.exists(cfg):
    steamapps = input("Enter SteamApps path: ")
    if not steamapps.endswith("/"):
        steamapps += "/"
    if not steamapps.endswith('common/'):
        steamapps += "common/"
    data = {
    'SteamApps':steamapps
    }

    with open(cfg, 'w',) as f :
        yaml.dump(data,f,sort_keys=False)

if not os.path.exists('configs/games'):
    addGame(cfg=cfg)
    while True:
        greeter()
else:
    while True:
        greeter()
        


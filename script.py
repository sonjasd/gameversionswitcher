import csv
import os
import yaml
from time import sleep

def greeter():
    return

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
            break
        else:
            print("\nGame already added!")
            sleep(1)

# config paths
gamescfg = "configs/games.csv"
cfg = "configs/config.yaml"

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

#check for games cfg
if not os.path.exists(gamescfg):
    data = [
    ['Game', 'Path']
    ]

    with open(gamescfg, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


#check for games in games cfg and add if doesnt exist
with open(gamescfg, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader, None) 
    has_data = any(row for row in reader)
    
    if header and has_data:
        greeter()
    else:
        addGame(cfg=cfg)
        


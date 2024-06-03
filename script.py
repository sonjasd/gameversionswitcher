import csv
import os
import yaml
import pandas as pd
from pandas import *
from time import sleep

print("\nWelcome to Game Version Switcher")

# config paths
cfg = "configs/config.yaml"

def selectedGame(game):
    while True:
        csvpath = f'configs/games/{game}/instances.csv'
        print("\nSelected game: " + game)
        print("\n[1] View instances [2] Create instance [3] Delete instance")
        selection = input("\n")

        if selection not in ["1", "2", "3"]:
            print("\nInvalid selection. Valid options: 1, 2, 3")
        else:
            selection = int(selection)
            match selection:
                case 1:
                    # check if instances exist
                    with open(csvpath, "r") as file:
                        line_count = sum(1 for line in file)
                    if line_count <= 1:
                        print("\nNo instances found.")

                    # else, read and print instances from csv file
                    else:


                        # doesnt work

                        data = read_csv(csvpath)
                        instances = data['Name'].tolist()

                        printedString = 'Instances found'
                        for instance in instances:
                            printedString += f' : {instance}'

                            
                        return
                    
                    break

                #create instance
                case 2:

                    def count_lines(filename):
                        df = pd.read_csv(filename)
                        return len(df) + 1

                    filename = csvpath
                    line_count = count_lines(filename)

                    id = line_count + 1

                    instanceName = input("\nEnter a name for new instance: ")
                    new_row = [str(id), instanceName, 'True']

                    with open(csvpath, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(new_row)
                        
                    break

                #delete instance
                case 3:
                    break


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
        selectedGame(game=folderslist[int(selection)-1])

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
        


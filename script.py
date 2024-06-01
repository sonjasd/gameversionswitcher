import csv
import os

def greeter():
    return

def addGame():
    gamename = input("Enter game name: ")
    gamename = input("Enter game path: ")

# config paths
gamescfg = "configs/games.csv"

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
        addGame()
        


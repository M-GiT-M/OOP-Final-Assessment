import json
import os
from Classing.Character import Character

#Saving the Game
def save_game(player, filename = "save_game.json"):
    #Saving the current game statistics and details to a file
    try:
        #Converting the player to dictionary
        player_data = player.save_character()

        #Saving the player to the file
        with open(filename, "w") as f:
            json.dump(player_data, f, indent = 2)

        print(f"Game Saved - {filename}!")
        return True
    except Exception as e:
        print(f"Having Trouble Saving the Game: {e}")
        return False
    
#Loading a Saved Game from a File
def load_game(filename = "save_game.json"):
    #Loading a game from a file
    try:
        #Checks for file existance
        if not os.path.exists(filename):
            print(f"Game File {filename} - Not Found!")
            return None
        
        #Loading the game
        with open(filename, 'r') as f:
            player_data = json.load(f)

        #'Restoring' player details
        player = Character.character_dict(player_data)

        print(f"Game File {filename} - Loaded Successfully!")
        return player
    except json.JSONDecodeError:
        print(f"{filename} Error: INVALID JSON DATA.")
        return None
    except Exception as e:
        print(f"Error: UNABLE TO LOAD GAME {e}")
        return None
from Classing.Character import Character
from Classing.Enemy import Enemy, Ogre, Witch, Giant
from Classing.Item import Item
from SaveLoad.saveload import save_game, load_game
from .Combat import combat

def main_menu():
    #Creating a loop of the game
    while True:
        print("\n======= RPG Adventure Game =======")
        print("1 - Start")
        print("2 - Exit")
        choice = input("Enter your Choice: ")
        if choice == "1":
            name = input("Enter your Hero's Name: ")
            player = Character(name)
            #Giving the player a starter-kit
            player.add_item(Item("Stick", "Wooden Stick - Power = 1"))
            combat(player, Enemy("Ogre"))
        elif choice == "2":
            print("Exiting the Game - Goodbye!")
            quit()
        else:
            print("Invalid Choice.")
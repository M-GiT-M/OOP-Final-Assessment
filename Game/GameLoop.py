from Classing.Character import Character
from Classing.Enemy import Enemy, Ogre, Witch, Giant
from Classing.Item import Item
from SaveLoad.saveload import save_game, load_game
from .Combat import combat

def main_menu():
    #Creating a loop of the game
    while True:
        print("\n" + "=" * 25)
        print("RPG Adventure Game")
        print("=" * 25)
        print("1 - New Game")
        print("2 - Load Game")
        print("3 - Exit")

        choice = input("Enter your Choice: ")

        #New Game
        if choice == "1":
            name = input("Enter your Hero's Name: ")
            player = Character(name)

            #Giving the player a starter-kit
            player.add_item(Item("Stick", "Basic Wooden Stick", attack = 3))
            player.add_item(Item("Tunic Garment", "Basic tunic that provides minimal protection", defense = 1))
            player.add_item(Item("Health Potion", "Restores a small amount of health", consumable = True, effect = "Health", effect_amount = 10))
            player.add_item(Item("Herb", "Magical Medicinal Herb"))
            player.add_item(Item("Empty Vial", "A Strong glass container for potions"))

            game_loop(player)

        #Loading the Game
        elif choice == "2":
            player = load_game()
            if player:
                game_loop(player)
            
        #Exitting the Game
        elif choice == "3":
            print("Hope you Enjoyed the Game! See you Again!")
            quit()

        else:
            print("Invalid Option - Please Choose one of the Listed Options")

def game_loop(player):
    pass
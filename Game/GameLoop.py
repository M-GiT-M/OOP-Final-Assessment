from Classing.Character import Character
from Classing.Enemy import Enemy, Ogre, Witch, Giant
from Classing.Item import Item
from SaveLoad.saveload import save_game, load_game
from .Combat import combat
from .Crafting import get_all_recipes

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
    #Main loop for the adventure game
    recipes = get_all_recipes()

    while player.is_alive():
        print("\n" + "=" * 25)
        print(f"ADVENTURE MENU - {player.name}")
        print(f"HP: {player.hp}/{player.max_hp} | Strength: {player.strength}")
        print("=" * 25)
        print("1 - Battle Ogre")
        print("2 - Battle Witch")
        print("3 - Battle Giant")
        print("4 - Open Inventory")
        print("5 - Use Item")
        print("6 - Equip Item")
        print("7 - Craft Item")
        print("8 - Save Game")
        print("9 - Return to Main Menu") 

        choice = input("Enter your Option: ")

        #Battle with an Ogre
        if choice == "1":
            result = combat(player, Ogre())
            if result == "Defeat":
                print("Game Over!")
                break

        #Battle with a Witch
        if choice == "2":
            result = combat(player, Witch())
            if result == "Defeat":
                print("Game Over!")
                break

        #Batlle with a Giant
        if choice == "3":
            result = combat(player, Giant())
            if result == "Defeat":
                print("Game Over!")
                break

        #Open Inventory
        elif choice == "4":
            player.show_inventory()

        #Use Item - i.e. Consumables
        elif choice == "5":
            player.show_inventory()
            if player.inventory:
                try:
                    item_index = int(input("Enter Item Number to Use (0 to Cancel): ")) - 1
                    if item_index != -1:
                        player.use_item(item_index)
                except ValueError:
                    print("Invalid Option - Please Enter a Valid Number.")

        #Equip Item - i.e. Armor, Weapon
        elif choice == "6":
            player.show_inventory()
            if player.inventory:
                try:
                    item_index = int(input("Enter Item Number to Use (0 to Cancel): ")) - 1
                    if item_index != -1:
                        player.equip_item(item_index)
                except ValueError:
                    print("Invalid Option - Please Enter a Valid Number.")

        #Craft an Item 
        elif choice == "7":
            #Display all available items that can be crafted
            print("\n======= CRAFTING RECIPES =======")
            recipe_names = list(recipes.keys())
            for i, recipe_name in enumerate(recipe_names):
                recipe = recipes[recipe_name]
                print(f"{i+1} - {recipe_name}, Requires: {', '.join(recipe.crafting_items)}")

            #Taking player's choice
            try:
                recipe_index = int(input("\n Enter Recipe Number to Craft (0 to Cancel): ")) - 1
                if 0 <= recipe_index < len(recipe_names):
                    recipe_name = recipe_names[recipe_index]
                    player.craft_item(recipe_name, recipes)
            except ValueError:
                print("Inavlid Option - Please Enter a Valid Number.")

        #Saving the Game
        elif choice == "8":
            save_game(player)

        #Main Menu
        elif choice == "9":
            break

        else:
            print("Invalid Choice - Please enter a number between 1-9.")
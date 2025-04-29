import random

def combat(player, enemy):
    print(f"\n======= BATTLE: {player.name} vs {enemy.name} =======")

    while player.is_alive() and enemy.is_alive():
        #Player's Turn
        print(f"\n{player.name}'s turn - Current HP: {player.hp}/{player.max_hp}")
        print("\n Choose your move:")
        print("1 - Attack")
        print("2 - Use Item")
        print("3 - Equip Item")
        print("4 - Open Inventory")
        print("5 - Defend (Damage Reduced by 50% Next Turn)")
        print("6 - Try to Escape")
        
        defending = False

        while True:
            move = input("Enter a Choice: ")
            #Attack
            if move == "1":
                player.attack(enemy)
            
            #Use Item
            elif move == "2":
                player.show_inventory()
                if player.inventory():
                    try:
                        item_index = int(input("Enter item number to use (0 to exit): ")) - 1
                        if item_index == -1:
                            continue
                        if player.use_item(item_index):
                            break
                    except ValueError:
                        print("Invalid Option - Please Enter a Valid Number.")
                else:
                    print("Inventory Empty.")
                continue

            #Equip Item
            elif move == "3":
                player.show_inventory()
                if player.inventory:
                    try:
                        item_index = int(input("Enter item number to use (0 to exit): ")) -1
                        if item_index == -1:
                            continue
                        if player.equip_item(item_index):
                            break
                    except ValueError:
                        print("Invalid Option - Please Enter a Valid Number.")
                else:
                    print("Inventory Empty.")

            #Open Inventory
            elif move == "4":
                player.show_inventory()
                continue

            #Defend
            elif move == "5":
                print(f"{player.name} remains defensive against the enemy!")
                defending = True
                break

            #Escape Attempt
            elif move == "6":
                chance_escape = 0.25
                if random.random() <= chance_escape:
                    print("Successful Escape!")
                    return
                else:
                    print("Failed Escape")
                    break
            else:
                print("Invalid Choice. Please enter a number between 1-6.")

        #If enemy is alive, their turn proceeds
        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn - Current HP: {enemy.hp}")

            #Damage reduction if player is defending
            if defending:
                og_defense = player.current_defense_shield()
                #Temporary extra defense for the upcoming attack
                player.__class__.current_defense_shield = lambda self: og_defense * 2
                enemy.attack(player)

                #Removing the extra defense after attack
                player.__class__.current_defense_shield = lambda self: og_defense
            else:
                enemy.attack(player)

    #Battle Over
    if player.is_alive():
        print(f"\nCongratulations! You have defeated the {enemy.name}!")

        #Checking for any drops
        dropped_item = enemy.drop_item()
        if dropped_item:
            print(f"\n{enemy.name} Dropped: {dropped_item}")
            print(f"Do You Wish to Collect this Item?")
            print("1 - Yes")
            print("2 - No")

            while True:
                choice = input("Enter your Choice: ")
                if choice == "1":
                    player.add_item(dropped_item)
                    break
                elif choice == "2":
                    print("Item not Collected.")
                    break
                else:
                    print("Invalid Option - Please Enter a number between 1-2")
        return "Victory!"
    else:
        print(f"\nYou have been defeated by {enemy.name}")
        print("Better Luck Next Time!")
        return "Defeat"
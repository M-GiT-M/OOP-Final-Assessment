import random

def combat(player, enemy):
    print(f"\n {enemy.name} has Appeared!")
    while player.is_alive() and enemy.is_alive():
        #Player's move
        print("\n Choose your move:")
        print("1 - Attack")
        print("2 - Open Inventory")
        print("3 - Escape")
        move = input("Enter a Number: ")

        if move == "1":
            player.attack(enemy)
        elif move == "2":
            player.show_inventory()
            continue
            #Allows the player to decide how to play their next move after checking the inventory
        elif move == "3":
            if random.random() < 0.5:
                #Generates a random number between 0-1 as a 50% chance of escaping
                print("Successful Escape!")
                return
            else:
                print("Failed Escape")
        else:
            print("Invalid Action. Please enter a number between 1-3.")
            continue

        #If enemy is alive, their turn proceeds
        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn:")
            enemy.attack(player)

    if player.is_alive():
        print(f"\nCongratulations! You have defeated the {enemy.name}!")
    else:
        print("\nYou have been defeated. Good Try!")
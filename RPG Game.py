import random

class Item: 
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}" if self.description else self.name
    
class Character:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
        self.inventory = []
        #This stores the item objects

    def is_alive(self):
        if self.hp > 0:
            return f"{self.name} is alive."
    
    def attack(self, enemy):
        damage = random.randint(5, 15)
        print(f"{self.name} attacks {enemy.name} with {damage} Damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} Damage! - Current HP: {self.hp}")

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("No Items in the Inventory")
        else:
            for item in self.inventory:
                print(f" * {item}")

class Enemy:
    def __init__(self, name, hp = 50):
        self.name = name
        self.hp = hp

    def is_alive(self):
        if self.hp > 0:
            return f"{self.name} is alive."
        
    def attack(self, character):
        damage = random.randint(5, 10)
        print(f"{self.name} attacks {character.name} with {damage} Damage!")
        character.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} Damage! - Current HP: {self.hp}")

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
import random

class Item: 
    def __init__(self, name, description = "", attack = 0, defense = 0, consumable = False, effect = None, effect_amount = 0, crafting_items = None):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.consumable = consumable
        self.effect = effect
        #Effect on Strength, Health, etc. 
        self.effect_amount = effect_amount
        self.crafting_items = crafting_items
        #The components required for crafting the item

    def __str__(self):
        item_details = f"{self.name}: {self.description}" if self.description else self.name
        if self.attack > 0:
            item_details += f" | Attack: +{self.attack}"
            #Adds on to the current attack power if the item has an attack power greater than 0
        if self.defense > 0:
            item_details += f" | Defense: +{self.defense}"
            #Adds on to the current defense shield if the item has a defense power greater than 0
        if self.consumable:
            item_details += f" | Consumable: {self.effect} +{self.effect_amount}"
            #Adds a consumable amount if the item is a consumable
        return item_details
    
    def save_item(self):
        #Saving the item to a dictionary
        return {
            "Name": self.name,
            "Description": self.description,
            "Attack Power": self.attack,
            "Defense Shield": self.defense,
            "Consumable": self.consumable,
            "Effect": self.effect,
            "Effect Amount": self.effect_amount,
            "Crafting Items": self.crafting_items
        }
    
    @staticmethod
    def item_dict(data):
        #Creates an item from the dictionary when loading
        return Item(
            name = data["Name"],
            description = data["Description"],
            attack = data["Attack Power"],
            defense = data["Defense Shield"],
            consumable = data["Consumable"],
            effect = data["Effect"],
            effect_amount = data["Effect Amount"],
            crafting_items = data["Crafting Items"]
        )
    
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

if __name__ == "__main__":
    main_menu()
import random
from .Item import Item

class Character:
    def __init__(self, name, hp = 100, max_hp = 100, strength = 10):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.inventory = []
        #This stores the item objects
        self.weapon_equipped = None
        self.armor_equipped = None
        #Default is that nothing is equipped

    def is_alive(self):
        if self.hp > 0:
            return f"{self.name} is alive."
        
    def current_attack_power(self):
        #Calculates the total attack power and including any weapons equipped
        normal_attack = self.strength
        #Checks if a weapon is equipped or not to add to the total attack power
        if self.weapon_equipped:
            weapon_attack = self.weapon_equipped.attack
        else:
            weapon_attack = 0
        return normal_attack + weapon_attack
    
    def current_defense_shield(self):
        #Calculates the total defense shiled and including any armor equipped
        normal_defense = 0
        #Checks if armor is equipped or not to add to the total defense shield
        if self.armor_equipped:
            armor_defense = self.armor_equipped.defense
        else:
            armor_defense = 0
        return normal_defense + armor_defense
    
    def attack(self, enemy):
        #Calculates the extra damage when a weapon is added
        damage = random.randint(self.current_attack_power() - 2, self.current_attack_power() + 5)
        #Damage when critical hits or headshots made (15% chance occuring)
        if random.random() < 0.15:
            damage = int(damage * 1.75)
            print(f"CRITICAL DAMAGE! - dealt by {self.name}")
        #In the case the enemy has extra defense its applied
        damage = max(1, damage - enemy.current_defense_shield())

        #Player Attacking Dialogue 
        print(f"{self.name} attacks {enemy.name} with {damage} Damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        #Checks if there is a damage reduction due to armor applied
        reduced_damage = max(1, damage - self.current_defense_shield())
        self.hp -= reduced_damage
        print(f"{self.name} takes {damage} Damage! - Current HP: {self.hp}")

    def add_item(self, item):
        #Adding items or collectables to the Inventory
        self.inventory.append(item)
        print(f"{item.name} - added to Inventory")

    def use_item(self, item_i):
        #Using a consumable
        if 0 <= item_i < len(self.inventory):
            item = self.inventory[item_i]
            #Checks if the item is a consumable or not and if it is being applied to health or strength
            if item.effect == "Health":
                #Increases/Heals HP of the Player
                old_hp = self.hp
                self.hp = min(self.max_hp, self.hp + item.effect_amount)
                print(f"{item.name} Consumed - HP Restored: {self.hp - old_hp}!")
                #Removes the consumable once consumed
                self.inventory.pop(item_i)
            elif item.effect == "Strength":
                #Provides a volatile boost to strength
                self.strength += item.effect_amount
                print(f"{item.name} Consumed - Strength Boosted By: {item.effect_amount}!")
                self.inventory.pop(item_i)
            return True
        else:
            print(f"Invalid Use of {item.name}.")
            return False
        
    def equip_item(self, item_i):
        #Using a weapon or applying armor
        if 0 <= item_i < len(self.inventory):
            item = self.inventory[item_i]
            if item.attack > 0:
                #Checks if a weapon is equipped to proceed with equipping a new weapon from the inventory
                if self.weapon_equipped:
                    #Adds the old weapon to the inventory
                    self.inventory.append(self.weapon_equipped)
                    print(f"{self.weapon_equipped} - Unequipped to Inventory.")
                self.weapon_equipped = item
                #Removes the newly equipped weapon from inventory
                self.inventory.pop(item_i)
                print(f"{item.name} - Weapon Equipped.")
                return True
            elif item.defense > 0:
                #Checks if armor is equipped to proceed with equipping new armor from the inventory
                if self.armor_equipped:
                    #Adds the old armor to the inventory
                    self.inventory.append(self.armor_equipped)
                    print(f"{self.armor_equipped} - Unequipped to Inventory")
                self.armor_equipped = item
                #Removes the newly equipped armor from inventory
                self.inventory.pop(item_i)
                print(f"{item.name} - Armor Equipped.")
                return True
            else:
                #If the item is not armor or a weapon
                print(f"Invalid Use of {item.name}.")
                return False
        else:
            #When the wrong index is input
            print(f"Invalid Item Index.")
            return False

    def show_inventory(self):
        print("\n ======= Inventory =======")
        if not self.inventory:
            print("No Items in Inventory")
        else:
            for i, item in enumerate(self.inventory):
                print(f"{i+1} - {item}")

        print("\n ======= Equipped Items =======")
        #Checks if there is a weapon equipped and informs the user
        if self.weapon_equipped:
            print(f"Weapon Equipped: {self.weapon_equipped}")
        else:
            print(f"Weapon Equipped: None")

        #Checks if there is armor equipped and informs the user
        if self.armor_equipped:
            print(f"Armor Equipped: {self.armor_equipped}")
        else:
            print(f"Armor Equipped: None")

    def craft_item(self, recipe, all_recipes):
    #Crafting an item usingt the components in Inventory
        #Checks if the recipe exists
        if recipe not in all_recipes:
            print(f"{recipe} - Not Found.")
            return False
        
        recipe_item = all_recipes[recipe]
        components_needed = recipe_item.crafting_items

        #Ensures the player has all the necessary crafting items
        components = []
        for component in components_needed:
            found = False
            #Iterates over the inventory for the components needed for this specific item
            for i, item in enumerate(self.inventory):
                if item.name == component and i not in components:
                    #Adds the component found to the list of components
                    components.append(i)
                    found = True
                    break
            if not found:
                print(f"Missing Component: {component}")
                return False
        
        #Removing Components - from the highest index to avoid issues
        components.sort(reverse = True)
        for index in components:
            self.inventory.pop(index)

        #Adding the crafted item to inventory
        item_made = Item(
            recipe_item.name,
            recipe_item.description,
            recipe_item.attack,
            recipe_item.defense,
            recipe_item.consumable,
            recipe_item.effect,
            recipe_item.effect_amount,
        )
        self.inventory.append(item_made)
        print(f"Successfully Crafted - {item_made.name}!")
        return True
            
    def save_character(self):
        #Saving the character to a dictionary 
        return {
            "Name": self.name,
            "HP": self.hp,
            "Max_HP": self.max_hp,
            "Strength": self.strength,
            "Inventory": [item.save_item() for item in self.inventory],
            "Weapon Equipped": self.weapon_equipped.save_item() if self.weapon_equipped else None,
            "Armor Equipped": self.armor_equipped.save_item() if self.armor_equipped else None,
        }
    
    @staticmethod
    def character_dict(data):
        #Creates a character from dictionary when loading
        character = Character(
            name = data["Name"],
            hp = data["HP"],
            max_hp = data["Max_HP"],
            strength = data["Strength"],
        )
        character.inventory = [Item.item_dict(item_data) for item_data in data ["Inventory"]]

        if data["Weapon Equipped"]:
            character.weapon_equipped = Item.item_dict(data["Weapon Equipped"])
        if data["Armor Equipped"]:
            character.armor_equipped = Item.item_dict(data["Armor Equipped"])
        return character
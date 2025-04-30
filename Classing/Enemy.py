import random
from abc import ABC, abstractmethod
from .Item import Item

class Enemy(ABC):
    def __init__(self, name, hp = 50, attack_power = 5, defense = 0):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        #Items that could drop from the enemies - to be used by the player
        self.drops = []

    def is_alive(self):
        if self.hp > 0:
            return f"{self.name} is alive."
        
    def get_defense(self):
        return self.defense
    
    @abstractmethod
    def attack(self, character):
        #SubClasses (different enemies) will have different attack methods
        pass

    def take_damage(self, damage):
        #Checks if there is a defense reduction applied
        reduced_damage = max(1, damage - self.defense)
        self.hp -= reduced_damage
        print(f"{self.name} takes {reduced_damage} Damage! - Current HP: {self.hp}")

    def drop_item(self):
        #Checks if the enemy dropped an item
        if not self.drops:
            return None
        
        #Creates a probbality of the enemy dropping and item
        roll = random.random()
        total_prob = 0

        for item, prob in self.drops:
            total_prob += prob
            if roll <= total_prob:
                #Creates a copy of the item with random stats - with 25% Variarion
                variation = random.uniform(0.8, 1.25) 

                #Creates and drops the new item
                dropped_item = Item(
                    item.name,
                    item.description,
                    int(item.attack * variation) if item.attack else 0,
                    int(item.defense * variation) if item.defense else 0,
                    item.consumable,
                    item.effect,
                    int(item.effect_amount * variation) if item.effect_amount else 0
                )
                return dropped_item
        return None

class Ogre(Enemy):
    def __init__(self):
        super().__init__("Ogre", hp = 70, attack_power = 7, defense = 2)

        #Setting up the probability of drops 
        self.drops = [
            (Item("Ogre Bat", "A Wooden Bat with Spiky Thorns", attack = 5), 0.25),
            (Item("Almighty Strand", "A Strand of the Ogre's Hair", defense = 4), 0.3),
            (Item("Strength Potion", "Temporary Boost to Strength", consumable = True, effect = "Strength", effect_amount = 5), 0.15),
            (Item("Health Potion", "Health Restoration", consumable = True, effect = "Health", effect_amount = 4), 0.2)
        ]
    def attack(self, character):
        #Ogre has the chance to perform a Powerful Body Slam
        damage = random.randint(self.attack_power - 1, self.attack_power + 3)

        #A 15% Chance for the Special Body Slam to Occur
        if random.random() < 0.15:
            print(f"{self.name} performs his special BODY SLAM!!!")
            #50% Damage increase
            damage = int(damage * 1.5)

            #Damage Reduction Applied - Subtracting some shield due to Body Slam
            defense_ignored = min(2, character.current_defense_shield())
            reduced_damage = max(1, damage - (character.current_defense_shield() - defense_ignored))
            print(f"{self.name} attacks {character.name} with {reduced_damage} Damage! - {defense_ignored} Defense Ignored.")
            character.take_damage(reduced_damage)
        else:
            #Applying Character Defense Reduction
            reduced_damage = max(1, damage - character.current_defense_shield())
            print(f"{self.name} attacks {character.name} with {reduced_damage} Damage!")
            character.take_damage(reduced_damage)

class Witch(Enemy):
    def __init__(self):
        super().__init__("Witch", hp = 40, attack_power = 4, defense = 8)

        #Setting up the probablity of Drops
        self.drops = [
            (Item("The Raven Dagger", "The Blade Enchanted with the Power of Ravens", attack = 7), 0.25),
            (Item("Poison Apple", "An extra but dangerous Boost to Health", defense = 2), 0.4),
            (Item("Gamma Vial", "Restores Health Swiftly", consumable = True, effect = "Health", effect_amount = 25), 0.15)
        ]
    
    def attack(self, character):
        #Witch has the chance to perform her deadly and silencing Banshee CACKLE
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)

        #A 30% Chance for the Banshee Cackle
        if random.random() < 0.3:
            print(f"{self.name} performs her silencing Banshee Cackle!")
            #Increases damage by 65%
            damage = damage * 0.65

            #Damage Reduction Applied 
            reduced_damage = max(1, int(damage - character.current_defense_shield()))
            print(f"{self.name} attacks {character.name} with {reduced_damage} Damage!")
            character.take_damage(reduced_damage)

            #Second Cackle
            reduced_damage = max(1, int(damage - character.current_defense_shield()))
            print(f"{self.name} attacks {character.name} once more {reduced_damage} Damage!")
            character.take_damage(reduced_damage)
        else:
            #Applying Character Damage Reduction
            reduced_damage = max(1, damage - character.current_defense_shield())
            print(f"{self.name} attacks {character.name} with {reduced_damage} Damage!")
            character.take_damage(reduced_damage)

class Giant(Enemy):
    def __init__(self):
        super().__init__("Giant", hp = 150, attack_power = 10, defense = 7)

        #Setting up the probability of Drops
        self.drops = [
            (Item("Giant Scale Armor", "Armor from the Giant's Scales", defense = 10), 0.4),
            (Item("Giant Molar Sword", "A sword crafted by the Giant's Dense Molar", attack = 10), 0.4),
            (Item("Giant Health Potion", "Restores a large amount of Health Power", consumable = True, effect = "Health", effect_amount = 50), 0.45),
            (Item("Giant's Strength", "Immense Strength Boost", consumable = True, effect = "Strength", effect_amount = 12), 0.1)
        ]

    def attack(self, character):
        #Giant has 2 different attack types
        attack_types = random.randint(1, 2)

        #Giant Stomp
        if attack_types == 1:
            damage = random.randint(self.attack_power - 2, self.attack_power + 2)
            reduced_damage = max(1, damage - character.current_defense_shield())
            print(f"{self.name} STOMPS {character.name} with its Giant Feet dealing {reduced_damage} Damage!")
            character.take_damage(reduced_damage)

        #Giant Smoosh
        elif attack_types == 2:
            damage = random.randint(self.attack_power - 4, self.attack_power)
            #Giant Smoosh has a chance of happening twice
            if random.random() < 0.4:
                print(f"{self.name} with the Great Giant Smoosh!")
                reduced_damage = max(1, damage - character.current_defense_shield())
                print(f"{self.name} smooshes twice with {reduced_damage} Damage EACH TIME!")
                character.take_damage(reduced_damage)
                character.take_damage(reduced_damage)
            else:
                reduced_damage = max(1, damage - character.current_defense_shield())
                print(f"{self.name} smooshes {character.name} dealing {reduced_damage} Damage!")
                character.take_damage(reduced_damage)
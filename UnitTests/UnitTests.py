import unittest
import random
import os
import sys
from pathlib import Path

current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

try:
    from Classing.Character import Character
    from Classing.Enemy import Enemy, Ogre, Witch, Giant
    from Classing.Item import Item
    from SaveLoad.saveload import save_game, load_game
    from Game.Crafting import get_all_recipes
except ImportError as e:
    print(f"Import Error: {e}")
    print(f"Current sys.path: {sys.path}")

class RPGTest(unittest.TestCase):
    def setUp(self):
        #Setting Up the Test Fixtures
        self.player = Character("Player 1")
        self.ogre = Ogre()
        self.witch = Witch()
        self.giant = Giant()

        #Integrating items for testing
        self.health_potion = Item("Test Potion", "Health Restoration", consumable = True, effect = "Health", effect_amount = 20)
        self.armor = Item("Test Armor", "Testing Armor", defense = 5)
        self.sword = Item("Test Sword", "Testing Sword", attack = 5)

    def test_character(self):
        #Testing a character and character attributes
        self.assertEqual(self.player.name, "Player 1")
        self.assertEqual(self.player.hp, 100)
        self.assertEqual(self.player.max_hp, 100)
        self.assertTrue(self.player.is_alive())

    def test_inventory(self):
        #Testing Adding Items
        initial_total = len(self.player.inventory)
        self.player.add_item(self.sword)
        #Adding on to Inventory
        self.assertEqual(len(self.player.inventory), initial_total + 1)

        #Testing Equipping Items
        self.player.equip_item(initial_total)
        self.assertEqual(self.player.weapon_equipped, self.sword)
        #Inventory Decreases
        self.assertEqual(len(self.player.inventory), initial_total)

        #Testing with consumsbles
        self.player.add_item(self.health_potion)
        #Reducing the HP to test potion's effect
        self.player.hp = 50
        self.player.use_item(initial_total)
        #After using the health potion, the HP should increase by 20
        self.assertEqual(self.player.hp, 70)

    def test_combat(self):
        #Testing the player's attack
        enemy_initial_hp = self.ogre.hp
        #Equipping the sword from the inventory
        self.player.equip_item(0)
        self.player.attack(self.ogre)
        self.assertLess(self.ogre.hp, enemy_initial_hp)

        #Testing the enemy's attack
        player_initial_hp = self.player.hp
        self.ogre.attack(self.player)
        self.assertLess(self.player.hp, player_initial_hp)

        #Testing the defense shield system
        self.player.add_item(self.armor)
        #Equipping the Armor
        self.player.equip_item(0)
        player_initial_hp = self.player.hp
        self.ogre.attack(self.player)
        #Damage Reduction after Armor Used
        self.assertGreater(self.player.hp, player_initial_hp - 10)

    def test_drops(self):
        #Forcing the drop by modifying probability
        og_random = random.random
        random.random = lambda: 0.1

        dropped_item = self.ogre.drop_item()
        self.assertIsNotNone(dropped_item)
        self.assertIn(dropped_item.name, ["Ogre Bat", "Almighty Strand", "Strength Potion"])

        #Restoring the og probability
        random.random = og_random

    def test_consumables(self):
        #Adding consumable to Inventory
        health_potion = Item("Health Potion", "Health Restoration", consumable = True, effect = "Health", effect_amount = 25)
        strength_potion = Item("Strength Potion", "Strength Boost", consumable = True, effect = "Strength", effect_amount = 5)
        
        #Adding to inventory
        self.player.add_item(health_potion)
        self.player.add_item(strength_potion)

        #Testing the Health Potion
        self.player.hp = 50
        og_hp = self.player.hp
        self.player.use_item(0)
        self.assertEqual(self.player.hp, og_hp + 25)

        #Testing the Strength Potion
        og_strength = self.player.strength
        self.player.use_item(0)
        self.assertEqual(self.player.strength, og_strength + 5)

    def test_crafting(self):
        #Adding the crafting components
        self.player.add_item(Item("Herb", "Magical Medicinal Herb"))
        self.player.add_item(Item("Empty Vial", "A Strong glass container for potions"))

        #Displaying the recipes
        recipes = get_all_recipes()

        #Test crafting health potion
        inventory_initial = len(self.player.inventory)
        result = self.player.craft_item("Health Potion", recipes)
        self.assertTrue(result)

        #Checking if items are available in Inventory
        self.assertEqual(len(self.player.inventory), inventory_initial - 1)

        #Finding the potion in Inventory
        potion_found = False
        for item in self.player.inventory:
            if item.name == "Health Potion":
                potion_found = True
                break
        self.assertTrue(potion_found)

    def SaveLoad_game(self):
        #Giving the player some details
        self.player.hp = 85
        self.player.add_item(self.sword)
        self.player.equip_item(0)
        self.player.add_item(self.health_potion)

        #Saving the game
        save_filename = "test_save.json"
        save_result = save_game(self.player, save_filename)
        self.assertTrue(save_result)
        self.assertTrue(os.path.exists(save_filename))

        #Loading the game
        load_player = load_game(save_filename)
        self.assertIsNotNone(load_player)

        #Checking the data was stored correctly
        self.assertEqual(load_player.name, self.player.name)
        self.assertEqual(load_player.hp, self.hp)
        self.assertEqual(len(load_player.inventory), len(self.player.inventory))
        self.assertEqual(load_player.weapon_equipped.name, self.player.weapon_equipped.name)

        #Cleaning the test file
        if os.path.exists(save_filename):
            os.remove(save_filename)

    def test_enemies(self):
        #Testing they have different attributes from one another
        self.assertNotEqual(self.ogre.hp, self.witch.hp)
        self.assertNotEqual(self.ogre.attack_power, self.witch.attack_power)

        #Testing the different drop inventories of each enemy
        ogre_drops = [item.name for item, _ in self.ogre.drops]
        witch_drops = [item.name for item, _ in self.witch.drops]
        giant_drops = [item.name for item, _ in self.giant.drops]

        #Testing different drops
        self.assertNotEqual(set(ogre_drops), set(witch_drops))
        self.assertNotEqual(set(witch_drops), set(giant_drops))

if __name__ == "__main__":
    unittest.main()
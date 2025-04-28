# OOP Final Assessment

50% Submission - RPG Game

# Set-Up
- Integrated the starter code file by typing it in to add personal modifications
- Willing to create an enticing dialogue
- Understanding the requirements and following the criteria, facing a bit of difficulty as the requirements are a lot and are     not ordered.
- Set up a 3-day Plan to complete the project and fulfill all the requirements asked.

# Day 1 - April 28
- Started by initialising the classes: Item, Character and Enemy.
  # Item Class
    - Enhanced the Item class to show more detail and saved it to a dictionary with all its details
    - By saving to dictionary I enable the user to start a new game or load an existing game with all details stored
  # Character Class
    - Set a max_hp so that even if armor is equipped and consumables are taken, the hp stays realistic
    - Created methods to know the current attack power and the currenr defense shield to enable the user to plan future               decisions
    - Set critical hits with a chance of 15% happening, once it occurs the damage is increased by 75%
    - Added any extra attack power or defense power when checking for current attack power and defense shield
    - Created a consumable method to use them for either Strength or Health
    - Created an equip method to equip armor (considered existing armor to be unequipped first) and to equip a weapon                (considered existing weapons to be uneqipped first)
    - When the player opens the inventory it also gives details of the items currently equipped/in-use
    - Created a craft method for potion/consumable making to increase health and checkec if the player has reuired components
    - Also saved character to a dictionary with all of its details, if a game is loaded all details are still available
  # Enemy Parent Class
    - 
- Planning to finish the Item, Character and Parent Enemy Class, while focusing on subclasses (different enemies) tomorrow.

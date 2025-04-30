# OOP Final Assessment

50% Submission - RPG Game

# Set-Up
- Integrated the starter code file by typing it in to add personal modifications
- Willing to create an enticing dialogue
- Understanding the requirements and following the criteria, facing a bit of difficulty as the requirements are a lot and are     not ordered.
- Set up a 3-day Plan to complete the project and fulfill all the requirements asked.

# Game Instructions
  # 1-Running the Game
    - The file 'Main.py' should be run using the terminal: python Main.py
  # 2-Playing The Game
    - The main menu should load along with an introduction:
      1 - New Game
      2 - Load Game
      3 - Exit
    - 1 - New Game:
      - Start by inputting 1, then entering hero name and the hero begins with a starter kit
    - 2 - Adventure Menu:
      - 9 Options will display, 3 to battle with enemies, 4 to handle items and 2 are game functions
  # 3-How Combat Works
    - Begins with 'Your Turn', with a few options to select from
    - Then the enemy's turn proceeds (Only if hero is still alive)
    - Defend reduces the damage taken from enemy but on the next round
    - Escape, a 25% chance to flee from the battle
  # 4-Save & Load
    - When the game is saved, the player's stats are saved into 'save_game.json'
    - To load the game, u must return to main menu and 'save_game.json' must exist - an error will appear indicating otherwise

==============================================================================================================================================

# Day 1 - April 28
- Started by initialising the classes: Item, Character and Enemy.
  # Item Class
    - Enhanced the Item class to show more detail and saved it to a dictionary with all its details
    - By saving to dictionary I enable the user to start a new game or load an existing game with all details stored
  # Character Class
    - Set a max_hp so that even if armor is equipped and consumables are taken, the hp stays realistic
    - Created methods to know the current attack power and the currenr defense shield to enable the user to plan future decisions
    - Set critical hits with a chance of 15% happening, once it occurs the damage is increased by 75%
    - Added any extra attack power or defense power when checking for current attack power and defense shield
    - Created a consumable method to use them for either Strength or Health
    - Created an equip method to equip armor (considered existing armor to be unequipped first) and to equip a weapon                (considered existing weapons to be uneqipped first)
    - When the player opens the inventory it also gives details of the items currently equipped/in-use
    - Created a craft method for potion/consumable making to increase health and checkec if the player has reuired components
    - Also saved character to a dictionary with all of its details, if a game is loaded all details are still available
  # Enemy Parent Class
    - Created a list of drops which are items that when dropped can be taken and used by the player
    - Created an abstractmethod for the attack method to be later integrated specifically to each enemy
    - Method of items dropped created with a random probabilty and random attack/defense amount it recieves
    - Will implement different enemies that have unique attack power and attributes
    - Planning on making 3-5 enemies like a dragon, ogre, giant, wizard and minotaur.
 
- Day 1 Complete - 40% of Project completed with the essential classes defined, a clear layout of the game has been strategically thought of and I am inventing new ideas as I go along.
- Having difficulty on how to save/load game but with research will figure it out, already started by saving character and items to dictionaries

# Day 2 - April 29
- Will work on the Enemy Subclasses to create different enemies and on the save/load game.
- Settled on 3 Different Enemies: Ogre, Witch and Giant
  # Ogre
    - Made the ogre have greater attack power than defense (supposing an ogre is not the brightest)
    - Created 4 Different drops with different chances of happening, two increasing attack/strength and two increasing                defense/health
    - Gave the ogre a special 'Body Slam' attack, with a 15% chance of occuring and ignoring some shield from the character
  # Witch
    - Made the Witch have grreater defense shield than attack power as a Witch generally casts protection spells
    - Created 3 different drops with different chances of occuring, 2 increasing health/defense and 1 for attack power
    - Gave the witch a special 'Banshee Cackle' attack with the chance of occuring twice
  # Giant
    - Made the giant have immense health power and attack power, as it the Giant is Giant.
    - Created 4 different drops with difference chances of happening, 2 for health/defense and 2 for attack/strength
    - Gavr the Giant 2 special attacks 'Giant Stomp' and 'Giant Smoosh' with the chance of the giant smoosh occuring twice
  # Save/Load
    - Used try and except to handle errors, it converts the information or current statistics to dictionary to save to a file, using JSON
    - Also used try and except to handle errors for loading, it first checks if the filename exists to then take the information on it and            store it to the player

- After looking at the criteria I realised I missed an important requirement, which was to separate the code into readable        parts and to also increase professionalism. I faced a few difficulties planning how to efficiently segregate my code, but was   able to fulfill the requirement and will continue building on this project in these newly segregated areas.

  # Combat Dialogue
    - Made 6 total options to include using/equipping items and the choice to attack/defend, plus other options.
    - Used try and except to handle errors
    - Also indicates who's turn it is
    - If a player chooses to defend, they recieve a temporary shield bonus (2x their current shield)
  # Crafting Items
    - Created a function that displays all available crafts and their recipes in a dictionary, for optimal and efficient use
    - Mainly Health/Defense Oriented since Drops are going to provide more strength/attack enhancing items
    - Some recipes include health potions and armor
    - Created different levels of health potions for further depth
  # Game Loop
    - Started with the Main Menu Section, which is the inro to the Game with 3 options: New Game, Load Game or to Exit
    - Gave all plaeyrs a 'starter kit' to be able to combat the enemies realistically, mixing different item enhancements
    - Then built the actual game, with 9 different options: 3 to battle the different enemies, 4 for item check/use and 2 that are game               functions like save and returning to Main Menu
    - When choosing to craft an item, the recipes are shown, so the player can check that and then proceed to Inventory to see if they are            capable of crafting the desired item.
    - Used Try and Except to handle errors efficiently

- Day 2 Complete - 80% of Project Completed, by finalising the main loop/cpmbat of the game, creating a main menu and introducing items that      can be crafted or collected as drops.
- Will implement the unit tests tomorrow and then go over documentation and the README file to polish. On the 4th Day I will conduct a final      review of all code and ensure the code is logical and efficient, as well as, fulfilling of the criteria.

# Day 3 - April 30
- Will Integrate unittests today and mention how to run them, as well as, include game instructions in the readme file
  # Unit Tests
    - Had trouble when testing the instances made, had 7 failures intitially due to logical errors, reduced to 1 failure and 3 errors, then            finally fixed all errors.
    - Had issues with importing classes from the different modules, had to use 'Path' from 'pathlib' - to counter the issues i used try and            except as an efficient way of handling
    - Created 9 testing sections, to target all elements of my code/game
    # How to Run
      - typing python -m unittest UnitTests/UnitTests.py in the terminal
      - or simply running it if on a software like vscode
      - Should run 7 tests and all should run smoothly - 'Ok'

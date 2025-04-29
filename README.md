# OOP Final Assessment

50% Submission - RPG Game

# Set-Up
- Integrated the starter code file by typing it in to add personal modifications
- Willing to create an enticing dialogue
- Understanding the requirements and following the criteria, facing a bit of difficulty as the requirements are a lot and are     not ordered.
- Set up a 3-day Plan to complete the project and fulfill all the requirements asked.

# Game Instructions

# Unit Test Instructions 

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
   - Used try and except to handle errors, it converts the information or current statistics to dictionary to save to a file,        using JSON
   - Also used try and except to handle errors for loading, it first checks if the filename exists to then take the information      on it and store it to the player

- After looking at the criteria I realised I missed an important requirement, which was to separate the code into readable        parts and to also increase professionalism. I faced a few difficulties planning how to efficiently segregate my code, but was   able to fulfill the requirement and will continue building on this project in these newly segregated areas.

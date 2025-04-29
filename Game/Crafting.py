from Classing.Item import Item

def get_all_recipes():
    #Returns all recipes in a dictionary
    recipes = {
        "Strong Health Potion": Item(
            "Strong Health Potion",
            "Restores a Large amount of Health",
            consumable = True,
            effect = "Health",
            effect_amount = 50,
            crafting_items = ["Health Potion", "Empty Vial"]
        ),
        "Health Potion": Item(
            "Health Potion",
            "Restores Health",
            consumable = True,
            effect = "Health",
            effect_value = 25,
            crafting_items = ["Herb", "Empty Vial"]
        ),
        "Strength Potion": Item(
            "Strength Potion",
            "Increases Strength Temporarily",
            consumable = True,
            effect = "Strength",
            effect_amount = "5",
            crafting_items = ["Rare Herb", "Empty Vial"]
        ),
        "Leather Armor": Item(
            "Leather Armor",
            "Decent Armor made of Leather",
            defense = 3,
            crafting_items = ["Leather Scrap", "Leather Scrap"]
        )
    }
    return recipes
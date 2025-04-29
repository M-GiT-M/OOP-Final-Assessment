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
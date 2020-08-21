class Magic_Items():
    def __init__(self, name, price, page, rarity, item_type):
        self.name = name
        self.price = price
        self.page = page
        self.rarity = rarity
        self.item_type = item_type

    def describe(self):
        print(f'{self.name}, price: {self.price}, page: {self.page}, rarity: {self.rarity}, type: {self.item_type}')
        

# Instantiate the items
spell_scroll_level_0 = Magic_Items('Spell Scroll Level 0', 10, 200, 'Common', 'Consumable')
ammunition_1 = Magic_Items('Ammuniton +1 (Each)', 25, 150, 'Uncommon', 'Consumable')
potion_of_healing = Magic_Items('Potion of Healing', 50, 187, 'Common', 'Consumable')
quaals_feather_token_anchor = Magic_Items("Quaal's Feather Token Anchor", 50, 188, 'Rare', 'Consumable')
spell_scroll_level_1 = Magic_Items('Spell Scroll Level 1', 60, 200, 'Common', 'Consumable')
philter_of_love = Magic_Items('Philter of Love', 90, 184, 'Uncommon', 'Consumable')
ammunition_2 = Magic_Items('Ammunition +2 (Each)', 100, 150, 'Rare', 'Consumable')
potion_of_poison = Magic_Items('Potion of Posion', 100, 188, 'Uncommon', 'Consumable')

magic_items = [
    spell_scroll_level_0,
    ammunition_1,
    potion_of_healing,
    quaals_feather_token_anchor,
    spell_scroll_level_1
]
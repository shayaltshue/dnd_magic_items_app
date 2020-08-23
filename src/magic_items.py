class Magic_Item():
    def __init__(self, name, price, page, rarity, item_type):
        self.name = name
        self.price = price
        self.page = page
        self.rarity = rarity
        self.item_type = item_type

    def describe(self):
        print(f'{self.name}, price: {self.price}, page: {self.page}, rarity: {self.rarity}, type: {self.item_type}')


# Instantiate the items
spell_scroll_level_0 = Magic_Item('Spell Scroll Level 0', 10, 200, 'Common', 'Consumable')
potion_of_healing = Magic_Item('Potion of Healing', 50, 187, 'Common', 'Consumable')
quaals_feather_token_anchor = Magic_Item("Quaal's Feather Token Anchor", 50, 188, 'Rare', 'Consumable')
spell_scroll_level_1 = Magic_Item('Spell Scroll Level 1', 60, 200, 'Common', 'Consumable')
philter_of_love = Magic_Item('Philter of Love', 90, 184, 'Uncommon', 'Consumable')
potion_of_poison = Magic_Item('Potion of Posion', 100, 188, 'Uncommon', 'Consumable')
ammunition_1 = Magic_Item('Ammuniton +1 (Each)', 25, 150, 'Uncommon', 'Consumable')
ammunition_2 = Magic_Item('Ammunition +2 (Each)', 100, 150, 'Rare', 'Consumable')
ammunition_3 = Magic_Item('Ammunition +3 (Each)', 400, 150, 'Very Rare', 'Consumable')
dust_of_dryness = Magic_Item('Dust of Drynss (1 pellet)', 120, 166, 'Uncommon', 'Consumable')
elixer_of_health = Magic_Item('Elixir of Health', 120, 168, 'Rare', 'Consumable')
keoghtoms_ointment = Magic_Item("Keoghtom's Ointment", 120, 179, 'Uncommon', 'Consumable')
spell_scroll_level_2 = Magic_Item('Spell Scroll Level 2', 120, 200, 'Uncommon', 'Consumable')
potion_of_fire_breath = Magic_Item('Potion of Fire Breath', 150, 187, 'Uncommon', 'Consumable')
potion_of_greater_healing = Magic_Item('Potion of Greater Healing', 150, 187, 'Uncommon', 'Consumable')
potion_of_climbing = Magic_Item('Potion of Climbing', 180, 187, 'Common', 'Consumable')
potion_of_heroism = Magic_Item('Potion of Heroism', 180, 187, 'Common', 'Consumable')
potion_of_Invisibility = Magic_Item('Potion of Invisibility', 180, 188, 'Very Rare', 'Consumable')
potion_of_mind_reading = Magic_Item('Potion of Mind Reading', 180, 188, 'Rare', 'Consumable')
potion_of_water_breathing = Magic_Item('Potion of Water Breathing', 180, 188, 'Uncommon', 'Consumable')
scroll_of_protection = Magic_Item('Scroll of Protection', 180, 199, 'Rare', 'Consumable')
nolzurs_marvelous_pigments = Magic_Item("Nolzur's Marvelous Pigments", 200, 183, 'Very Rare', 'Consumable')
potion_of_animal_friendship = Magic_Item('Potion of Animal Friendship', 200, 187, 'Uncommon', 'Consumable')
spell_scroll_level_3 = Magic_Item('Spell Scroll Level 3', 200, 200, 'Uncommon', 'Consumable')
quaals_feather_token_fan = Magic_Item("Quaal's Feather Token Fan", 250, 188, 'Rare', 'Consumable')
quaals_feather_token_whip = Magic_Item("Quaal's Feather Token Whip", 250, 188, 'Rare', 'Consumable')
potion_of_diminution = Magic_Item('Potion of Diminution', 270, 187, 'Rare', 'Consumable')
potion_of_growth = Magic_Item('Potion of Growth', 270, 187, 'Uncommon', 'Consumable')
dust_of_disappearance = Magic_Item('Dust of Disappearance', 300, 166, 'Uncommon', 'Consumable')
necklace_of_fireballs_1 = Magic_Item('Necklace of Fireballs (One Bead)', 300, 182, 'Rare', 'Consumable')
potion_of_gaseous_form = Magic_Item('Potion of Gaseous Form', 300, 187, 'Rare', 'Consumable')
potion_of_resistance = Magic_Item('Potion of Resistance', 300, 187, 'Uncommon', 'Consumable')
universal_solvent = Magic_Item('Universal Solvent', 300, 209, 'Legendary', 'Consumable')
spell_scroll_level_4 = Magic_Item('Spell Scroll Level 4', 320, 200, 'Rare', 'Consumable')
potion_of_speed = Magic_Item('Potion of Speed', 450, 174, 'Rare', 'Consumable')
sovereign_glue = Magic_Item('Sovereign Glue', 400, 200, 'Legendary', 'Consumable')
horn_of_blasting = Magic_Item('Horn of Blasting', 450, 174, 'Rare', 'Consumable')
potion_of_superior_healing = Magic_Item('Potion of Superior Healing', 450, 187, 'Very Rare', 'Consumable')
dust_of_sneezing_and_choking = Magic_Item('Potion of Sneezing and Choking', 450, 187, 'Very Rare', 'Consumable')
necklace_of_fireballs_2 = Magic_Item('Necklace of Fireballs (Two Beads)', 480, 182, 'Rare', 'Consumable')
oil_of_slipperiness = Magic_Item('Oil of Slipperiness', 480, 184, 'Uncommon', 'Consumable')
potion_of_flying = Magic_Item('Potion of Flying', 500, 187, 'Very Rare', 'Consumable')
arrow_of_slaying = Magic_Item('Arrow of Slaying (Each)', 600, 152, 'Very Rare', 'Consumable')
spell_scroll_level_5 = Magic_Item('Spell Scroll Level 5', 640, 200, 'Rare', 'Consumable')
bead_of_force = Magic_Item('Bead of Force', 960, 167, 'Rare', 'Consumable')
elemental_gem = Magic_Item('Elemental Gem', 690, 167, 'Uncommon', 'Consumable')
necklace_of_fireballs_3 = Magic_Item('Necklace of Fireballs (Three Beads', 960, 182, 'Rare', 'Consumable')
potion_of_clairvoyance = Magic_Item('Potion of Clairvoyance', 960, 187, 'Rare', 'Consumable')
potion_of_vitality = Magic_Item('Potion of Vitality', 960, 188, 'Very Rare', 'Consumable')
spell_scroll_level_6 = Magic_Item('Spell Scroll Level 6', 1280, 200, 'Very Rare', 'Consumable')
potion_of_supreme_healing = Magic_Item('Potion of Supreme Healing', 1350, 187, 'Very Rare', 'Consumable')
chime_of_opening = Magic_Item('Chime of Opening', 1500, 158, 'Rare', 'Consumable')
necklace_of_fireballs_4 = Magic_Item('Necklace of Fireballs (Four Beads)', 1600, 182, 'Rare', 'Consumable')
oil_of_etherealness = Magic_Item('Oil of Etherealness', 1920, 183, 'Rare', 'Consumable')
ioun_stone_absorption = Magic_Item('Ioun Stone Absorption', 2400, 177, 'Very Rare', 'Consumable')
spell_scroll_level_7 = Magic_Item('Spell Scroll Level 7', 2560, 200, 'Very Rare', 'Consumable')
quaals_feather_token_bird = Magic_Item("Quaal's Feather Token Bird", 3000, 188, 'Rare', 'Consumable')
quaals_feather_token_swan_boat = Magic_Item("Quaal's Feather Token Swan Boat", 3000, 188, 'Rare', 'Consumable')
oil_of_sharpness = Magic_Item('Oil of Sharpness', 32000, 184, 'Very Rare', 'Consumable')
necklace_of_fireballs_5 = Magic_Item('Necklace of Fireballs (Five Beads)', 3840, 182, 'Rare', 'Consumable')
potion_of_invulnerability = Magic_Item('Potion of Invulnerability', 3840, 188, 'Rare', 'Consumable')
gem_of_brightness = Magic_Item('Gem of Brightness', 5000, 171, 'Uncommon', 'Consumable')
spell_scroll_level_8 = Magic_Item('Spell Scroll Level 8', 5120, 200, 'Very Rare', 'Consumable')
deck_of_illusions = Magic_Item('Deck of Illusions', 6120, 161, 'Uncommon', 'Consumable')
necklace_of_fireballs_6 = Magic_Item('Necklace of Fireballs (6 Beads)', 7680, 182, 'Rare', 'Consumable')
spell_scroll_level_9 = Magic_Item('Spell Scroll Level 9', 10240, 200, 'Legendary', 'Consumable')
ioun_stone_greater_absorption = Magic_Item('Ioun Sone Greater Absorption', 31000, 177, 'Legendary', 'Consumable')
rod_of_absorption = Magic_Item('Rod of Absorption', 50000, 195, 'Very Rare', 'Consumable')
talisman_of_ultimate_evil = Magic_Item('Talisman of Ultimate Evil', 61440, 207, 'Legendary', 'Consumable')
robe_of_useful_items = Magic_Item('Robe of Useful Items', 'Items * 5', 195, 'Uncommon', 'Consumable')

armor_1 = Magic_Item('+1 Armor', 1500, 152, 'Rare', 'Combat')
shield_1 = Magic_Item('+1 Shield', 1500, 200, 'Uncommon', 'Combat')
weapon_1 = Magic_Item('+1 Weapon', 1000, 213, 'Uncommon' 'Combat')
armor_2 = Magic_Item('+2 Armor', 6000, 152, 'Very Rare', 'Combat')
shield_2 = Magic_Item('+2 Shield', 6000, 200, 'Rare', 'Combat')
weapon_2 = Magic_Item('+2 Weapon', 4000, 213, 'Rare', 'Combat')
armor_3 = Magic_Item('+3 Armor', 24000, 152, 'Legendary', 'Combat')
shield_3 = Magic_Item('+3 Shield', 24000, 200, 'Very Rare', 'Combat')
weapon_3 = Magic_Item('+3 Weapon', 16000, 213, 'Very Rare', 'Combat')
adamantine_armor = Magic_Item('Adamantine Armor', 500, 150, 'Uncommon', 'Combat')
alchemy_jug = Magic_Item('Alchemy Jug', 6000, 150, 'Uncommon', 'Non-Combat')


magic_items = [
    spell_scroll_level_0,
    ammunition_1,
    potion_of_healing,
    quaals_feather_token_anchor,
    spell_scroll_level_1,
    philter_of_love,
    ammunition_2,
    potion_of_poison,
    ammunition_1,
    ammunition_2,
    ammunition_3,
    dust_of_dryness,
    elixer_of_health,
    keoghtoms_ointment,
    spell_scroll_level_2,
    potion_of_fire_breath,
    potion_of_greater_healing,
    potion_of_climbing,
    potion_of_heroism,
    potion_of_Invisibility,
    potion_of_mind_reading,
    potion_of_water_breathing,
    scroll_of_protection,
    nolzurs_marvelous_pigments,
    potion_of_animal_friendship,
    spell_scroll_level_3,
    quaals_feather_token_fan,
    quaals_feather_token_whip,
    potion_of_diminution,
    potion_of_growth,
    dust_of_disappearance,
    necklace_of_fireballs_1,
    potion_of_gaseous_form,
    potion_of_resistance,
    universal_solvent,
    spell_scroll_level_4,
    potion_of_speed,
    sovereign_glue,
    horn_of_blasting,
    potion_of_superior_healing,
    dust_of_sneezing_and_choking,
    necklace_of_fireballs_2,
    oil_of_slipperiness,
    potion_of_flying,
    arrow_of_slaying,
    spell_scroll_level_5,
    bead_of_force,
    elemental_gem,
    necklace_of_fireballs_3,
    potion_of_clairvoyance,
    potion_of_vitality,
    spell_scroll_level_6,
    potion_of_supreme_healing,
    chime_of_opening,
    necklace_of_fireballs_4,
    oil_of_etherealness,
    ioun_stone_absorption,
    spell_scroll_level_7,
    quaals_feather_token_bird,
    quaals_feather_token_swan_boat,
    oil_of_sharpness,
    necklace_of_fireballs_5,
    potion_of_invulnerability,
    gem_of_brightness,
    spell_scroll_level_8,
    deck_of_illusions,
    necklace_of_fireballs_6,
    spell_scroll_level_9,
    ioun_stone_greater_absorption,
    rod_of_absorption,
    talisman_of_ultimate_evil,
    robe_of_useful_items,

    armor_1,
    shield_1,
    weapon_1,
    armor_2,
    shield_2,
    weapon_2,
    armor_3,
    shield_3,
    weapon_3,
    adamantine_armor,
    alchemy_jug
]
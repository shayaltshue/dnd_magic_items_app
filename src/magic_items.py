class Magic_Item:
    def __init__(self, name, price, page, rarity, item_type):
        self.name = name
        self.price = price
        self.page = page
        self.rarity = rarity
        self.item_type = item_type

    def describe(self):
        print(
            f"{self.name}, price: {self.price}, page: {self.page}, rarity: {self.rarity}, item type: {self.item_type}"
        )


# Instantiating Consumable Items
spell_scroll_level_0 = Magic_Item(
    "Spell Scroll Level 0", 10, 200, "Common", "Consumable"
)
potion_of_healing = Magic_Item("Potion of Healing", 50, 187, "Common", "Consumable")
quaals_feather_token_anchor = Magic_Item(
    "Quaal's Feather Token Anchor", 50, 188, "Rare", "Consumable"
)
spell_scroll_level_1 = Magic_Item(
    "Spell Scroll Level 1", 60, 200, "Common", "Consumable"
)
philter_of_love = Magic_Item("Philter of Love", 90, 184, "Uncommon", "Consumable")
potion_of_poison = Magic_Item("Potion of Poison", 100, 188, "Uncommon", "Consumable")
ammunition_1 = Magic_Item("Ammunition +1 (Each)", 25, 150, "Uncommon", "Consumable")
ammunition_2 = Magic_Item("Ammunition +2 (Each)", 100, 150, "Rare", "Consumable")
ammunition_3 = Magic_Item("Ammunition +3 (Each)", 400, 150, "Very Rare", "Consumable")
dust_of_dryness = Magic_Item(
    "Dust of Drynss (1 pellet)", 120, 166, "Uncommon", "Consumable"
)
elixer_of_health = Magic_Item("Elixir of Health", 120, 168, "Rare", "Consumable")
keoghtoms_ointment = Magic_Item(
    "Keoghtom's Ointment", 120, 179, "Uncommon", "Consumable"
)
spell_scroll_level_2 = Magic_Item(
    "Spell Scroll Level 2", 120, 200, "Uncommon", "Consumable"
)
potion_of_fire_breath = Magic_Item(
    "Potion of Fire Breath", 150, 187, "Uncommon", "Consumable"
)
potion_of_greater_healing = Magic_Item(
    "Potion of Greater Healing", 150, 187, "Uncommon", "Consumable"
)
potion_of_climbing = Magic_Item("Potion of Climbing", 180, 187, "Common", "Consumable")
potion_of_heroism = Magic_Item("Potion of Heroism", 180, 187, "Common", "Consumable")
potion_of_Invisibility = Magic_Item(
    "Potion of Invisibility", 180, 188, "Very Rare", "Consumable"
)
potion_of_mind_reading = Magic_Item(
    "Potion of Mind Reading", 180, 188, "Rare", "Consumable"
)
potion_of_water_breathing = Magic_Item(
    "Potion of Water Breathing", 180, 188, "Uncommon", "Consumable"
)
scroll_of_protection = Magic_Item(
    "Scroll of Protection", 180, 199, "Rare", "Consumable"
)
nolzurs_marvelous_pigments = Magic_Item(
    "Nolzur's Marvelous Pigments", 200, 183, "Very Rare", "Consumable"
)
potion_of_animal_friendship = Magic_Item(
    "Potion of Animal Friendship", 200, 187, "Uncommon", "Consumable"
)
spell_scroll_level_3 = Magic_Item(
    "Spell Scroll Level 3", 200, 200, "Uncommon", "Consumable"
)
quaals_feather_token_fan = Magic_Item(
    "Quaal's Feather Token Fan", 250, 188, "Rare", "Consumable"
)
quaals_feather_token_whip = Magic_Item(
    "Quaal's Feather Token Whip", 250, 188, "Rare", "Consumable"
)
potion_of_diminution = Magic_Item(
    "Potion of Diminution", 270, 187, "Rare", "Consumable"
)
potion_of_growth = Magic_Item("Potion of Growth", 270, 187, "Uncommon", "Consumable")
dust_of_disappearance = Magic_Item(
    "Dust of Disappearance", 300, 166, "Uncommon", "Consumable"
)
necklace_of_fireballs_1 = Magic_Item(
    "Necklace of Fireballs (One Bead)", 300, 182, "Rare", "Consumable"
)
potion_of_gaseous_form = Magic_Item(
    "Potion of Gaseous Form", 300, 187, "Rare", "Consumable"
)
potion_of_resistance = Magic_Item(
    "Potion of Resistance", 300, 187, "Uncommon", "Consumable"
)
universal_solvent = Magic_Item("Universal Solvent", 300, 209, "Legendary", "Consumable")
spell_scroll_level_4 = Magic_Item(
    "Spell Scroll Level 4", 320, 200, "Rare", "Consumable"
)
potion_of_speed = Magic_Item("Potion of Speed", 450, 174, "Rare", "Consumable")
sovereign_glue = Magic_Item("Sovereign Glue", 400, 200, "Legendary", "Consumable")
horn_of_blasting = Magic_Item("Horn of Blasting", 450, 174, "Rare", "Consumable")
potion_of_superior_healing = Magic_Item(
    "Potion of Superior Healing", 450, 187, "Very Rare", "Consumable"
)
dust_of_sneezing_and_choking = Magic_Item(
    "Potion of Sneezing and Choking", 450, 187, "Very Rare", "Consumable"
)
necklace_of_fireballs_2 = Magic_Item(
    "Necklace of Fireballs (Two Beads)", 480, 182, "Rare", "Consumable"
)
oil_of_slipperiness = Magic_Item(
    "Oil of Slipperiness", 480, 184, "Uncommon", "Consumable"
)
potion_of_flying = Magic_Item("Potion of Flying", 500, 187, "Very Rare", "Consumable")
arrow_of_slaying = Magic_Item(
    "Arrow of Slaying (Each)", 600, 152, "Very Rare", "Consumable"
)
spell_scroll_level_5 = Magic_Item(
    "Spell Scroll Level 5", 640, 200, "Rare", "Consumable"
)
bead_of_force = Magic_Item("Bead of Force", 960, 167, "Rare", "Consumable")
elemental_gem = Magic_Item("Elemental Gem", 690, 167, "Uncommon", "Consumable")
necklace_of_fireballs_3 = Magic_Item(
    "Necklace of Fireballs (Three Beads", 960, 182, "Rare", "Consumable"
)
potion_of_clairvoyance = Magic_Item(
    "Potion of Clairvoyance", 960, 187, "Rare", "Consumable"
)
potion_of_vitality = Magic_Item(
    "Potion of Vitality", 960, 188, "Very Rare", "Consumable"
)
spell_scroll_level_6 = Magic_Item(
    "Spell Scroll Level 6", 1280, 200, "Very Rare", "Consumable"
)
potion_of_supreme_healing = Magic_Item(
    "Potion of Supreme Healing", 1350, 187, "Very Rare", "Consumable"
)
chime_of_opening = Magic_Item("Chime of Opening", 1500, 158, "Rare", "Consumable")
necklace_of_fireballs_4 = Magic_Item(
    "Necklace of Fireballs (Four Beads)", 1600, 182, "Rare", "Consumable"
)
oil_of_etherealness = Magic_Item("Oil of Etherealness", 1920, 183, "Rare", "Consumable")
ioun_stone_absorption = Magic_Item(
    "Ioun Stone Absorption", 2400, 177, "Very Rare", "Consumable"
)
spell_scroll_level_7 = Magic_Item(
    "Spell Scroll Level 7", 2560, 200, "Very Rare", "Consumable"
)
quaals_feather_token_bird = Magic_Item(
    "Quaal's Feather Token Bird", 3000, 188, "Rare", "Consumable"
)
quaals_feather_token_swan_boat = Magic_Item(
    "Quaal's Feather Token Swan Boat", 3000, 188, "Rare", "Consumable"
)
oil_of_sharpness = Magic_Item("Oil of Sharpness", 32000, 184, "Very Rare", "Consumable")
necklace_of_fireballs_5 = Magic_Item(
    "Necklace of Fireballs (Five Beads)", 3840, 182, "Rare", "Consumable"
)
potion_of_invulnerability = Magic_Item(
    "Potion of Invulnerability", 3840, 188, "Rare", "Consumable"
)
gem_of_brightness = Magic_Item("Gem of Brightness", 5000, 171, "Uncommon", "Consumable")
spell_scroll_level_8 = Magic_Item(
    "Spell Scroll Level 8", 5120, 200, "Very Rare", "Consumable"
)
deck_of_illusions = Magic_Item("Deck of Illusions", 6120, 161, "Uncommon", "Consumable")
necklace_of_fireballs_6 = Magic_Item(
    "Necklace of Fireballs (6 Beads)", 7680, 182, "Rare", "Consumable"
)
spell_scroll_level_9 = Magic_Item(
    "Spell Scroll Level 9", 10240, 200, "Legendary", "Consumable"
)
ioun_stone_greater_absorption = Magic_Item(
    "Ioun Stone Greater Absorption", 31000, 177, "Legendary", "Consumable"
)
rod_of_absorption = Magic_Item(
    "Rod of Absorption", 50000, 195, "Very Rare", "Consumable"
)
talisman_of_ultimate_evil = Magic_Item(
    "Talisman of Ultimate Evil", 61440, 207, "Legendary", "Consumable"
)
robe_of_useful_items = Magic_Item(
    "Robe of Useful Items", "Items * 5", 195, "Uncommon", "Consumable"
)

# Instantiating Combat Items
vicious_weapon = Magic_Item("Vicious Weapon", 350, 209, "Rare", "Combat")
adamantine_armor = Magic_Item("Adamantine Armor", 500, 150, "Uncommon", "Combat")
mithiral_armor = Magic_Item("Mithral Armor", 800, 182, "Uncommon", "Combat")
weapon_1 = Magic_Item("+1 Weapon", 1000, 213, "Uncommon", "Combat")
sword_of_life_stealing = Magic_Item(
    "Sword of Life-Stealing", 1000, 206, "Rare", "Combat"
)
ioun_stone_protection = Magic_Item("Ioun Stone Protection", 1200, 177, "Rare", "Combat")
wand_of_the_war_mage_1 = Magic_Item(
    "Wand of the War Mage +1", 1200, 212, "Uncommon", "Combat"
)
bracers_of_archery = Magic_Item("Bracers of Archery", 1500, 156, "Uncommon", "Combat")
circlet_of_blasting = Magic_Item("Circlet of Blasting", 1500, 158, "Uncommon", "Combat")
javelin_of_lightning = Magic_Item(
    "Javelin of Lightning", 1500, 178, "Uncommon", "Combat"
)
prayer_bead_smiting = Magic_Item("Prayer Bead - Smiting", 1500, 182, "Rare", "Combat")
wind_fan = Magic_Item("Wind Fan", 1500, 213, "Uncommon", "Combat")
sword_of_sharpness = Magic_Item("Sword of Sharpness", 1700, 206, "Rare", "Combat")
staff_of_the_adder = Magic_Item("Staff of the Adder", 1800, 203, "Uncommon", "Combat")
dancing_sword = Magic_Item("Dancing Sword", 2000, 160, "Very Rare", "Combat")
glamoured_studded_leather = Magic_Item(
    "Glamoured Studded Leather", 2000, 172, "Rare", "Combat"
)
pipes_of_the_sewers = Magic_Item("Pipes of the Sewers", 2000, 185, "Uncommon", "Combat")
prayer_bead_bless = Magic_Item("Prayer Bead - Bless", 2000, 182, "Rare", "Combat")
saddle_of_the_cavalier = Magic_Item(
    "Saddle of the Cavalier", 2000, 199, "Uncommon", "Combat"
)
sword_of_wounding = Magic_Item("Sword of Wounding", 2000, 207, "Rare", "Combat")
frost_brand = Magic_Item("Frost Brand", 2200, 171, "Very Rare", "Combat")
dagger_of_venom = Magic_Item("Dagger of Venom", 2500, 160, "Rare", "Combat")
gloves_of_missile_snaring = Magic_Item(
    "Gloves of Missile Snaring", 3000, 172, "Uncommon", "Combat"
)
ioun_stone_agility = Magic_Item("Ioun Stone Agility", 3000, 177, "Very Rare", "Combat")
ioun_stone_fortitude = Magic_Item(
    "Ioun Stone Fortitude", 3000, 177, "Very Rare", "Combat"
)
ioun_stone_insight = Magic_Item("Ioun Stone Insight", 3000, 177, "Very Rare", "Combat")
ioun_stone_intellect = Magic_Item(
    "Ioun Stone Intellect", 3000, 177, "Very Rare", "Combat"
)
ioun_stone_leadership = Magic_Item(
    "Ioun Stone Leadership", 3000, 177, "Very Rare", "Combat"
)
ioun_stone_strength = Magic_Item(
    "Ioun Stone Strength", 3000, 177, "Very Rare", "Combat"
)
staff_of_withering = Magic_Item("Staff of Withering", 3000, 205, "Rare", "Combat")
cloak_of_protection = Magic_Item("Cloak of Protection", 3500, 159, "Uncommon", "Combat")
oathbow = Magic_Item("Oathbow", 3500, 183, "Very Rare", "Combat")
ring_of_protection = Magic_Item("Ring of Protection", 3500, 191, "Rare", "Combat")
weapon_2 = Magic_Item("+2 Weapon", 4000, 213, "Rare", "Combat")
boots_of_speed = Magic_Item("Boots of Speed", 4000, 155, "Rare", "Combat")
dragon_scale_mail = Magic_Item("Dragon Scale Mail", 4000, 165, "Very Rare", "Combat")
elven_chain = Magic_Item("Elven Chain", 4000, 168, "Rare", "Combat")
ioun_stone_regeneration = Magic_Item(
    "Ioun Stone Regeneration", 4000, 177, "Legendary", "Combat"
)
iron_bands_of_bilarro = Magic_Item("Iron Bands of Bilarro", 4000, 177, "Rare", "Combat")
prayer_bead_curing = Magic_Item("Prayer Bead - Curing", 4000, 182, "Rare", "Combat")
rope_of_entanglement = Magic_Item("Rope of Entanglement", 4000, 197, "Rare", "Combat")
wand_of_enemy_detection = Magic_Item(
    "Wand of Enemy Detection", 4000, 210, "Rare", "Combat"
)
luckstone = Magic_Item("Luckstone", 4200, 205, "Uncommon", "Combat")
wand_of_the_war_mage_2 = Magic_Item(
    "Wand of the War Mage +2", 4800, 212, "Rare", "Combat"
)
flame_tongue = Magic_Item("Flame Tongue", 5000, 170, "Rare", "Combat")
periapt_of_wound_closure = Magic_Item(
    "Periapt of Wound Closure", 5000, 184, "Uncommon", "Combat"
)
ring_of_evasion = Magic_Item("Ring of Evasion", 5000, 191, "Rare", "Combat")
ring_of_the_ram = Magic_Item("Ring of the Ram", 5000, 193, "Rare", "Combat")
tentacle_rod = Magic_Item("Tentacle Rod", 5000, 208, "Rare", "Combat")
animated_shield = Magic_Item("Animated Shield", 6000, 151, "Very Rare", "Combat")
armor_of_resistance = Magic_Item("Armor of Resistance", 6000, 152, "Rare", "Combat")
arrow_catching_shield = Magic_Item("Arrow-Catching Shield", 6000, 152, "Rare", "Combat")
belt_of_dwarvenkind = Magic_Item("Belt of Dwarvenkind", 6000, 155, "Rare", "Combat")
bracers_of_defence = Magic_Item("Bracers of Defense", 6000, 156, "Rare", "Combat")
ioun_stone_reserve = Magic_Item("Ioun Stone Reserve", 6000, 177, "Rare", "Combat")
pearl_of_power = Magic_Item("Pearl of Power", 6000, 184, "Uncommon", "Combat")
pipes_of_haunting = Magic_Item("Pipes of Haunting", 6000, 185, "Uncommon", "Combat")
ring_of_resistance = Magic_Item("Ring of Resistance", 6000, 192, "Rare", "Combat")
robe_of_scintillating_colors = Magic_Item(
    "Robe of Scintillating Colors", 6000, 194, "Very Rare", "Combat"
)
scimitar_of_speed = Magic_Item("Scimitar of Speed", 6000, 199, "Very Rare", "Combat")
shield_of_missile_attraction = Magic_Item(
    "Shield of Missile Attraction", 6000, 200, "Rare", "Combat"
)
giant_slayer = Magic_Item("Giant Slayer", 7000, 172, "Rare", "Combat")
mace_of_smiting = Magic_Item("Mace of Smiting", 7000, 179, "Rare", "Combat")
brooch_of_shielding = Magic_Item("Brooch of Shielding", 7500, 156, "Uncommon", "Combat")
amulet_of_health = Magic_Item("Amulet of Health", 8000, 150, "Rare", "Combat")
dragon_slayer = Magic_Item("Dragon Slayer", 8000, 166, "Rare", "Combat")
gauntlets_of_ogre_power = Magic_Item(
    "Gauntlets of Ogre Power", 8000, 171, "Uncommon", "Combat"
)
headband_of_intellect = Magic_Item(
    "Headband of Intellect", 8000, 173, "Uncommon", "Combat"
)
mace_of_disruption = Magic_Item("Mace of Disruption", 8000, 179, "Rare", "Combat")
mace_of_terror = Magic_Item("Mace of Terror", 8000, 180, "Rare", "Combat")
nine_lives_stealer = Magic_Item(
    "Nine Lives Stealer (Fully Charged)", 8000, 183, "Very Rare", "Combat"
)
wand_of_magic_missile = Magic_Item(
    "Wand of Magic Missiles", 8000, 211, "Uncommon", "Combat"
)
wand_of_web = Magic_Item("Wand of Web", 8000, 212, "Uncommon", "Combat")
staff_of_thunder_and_lightning = Magic_Item(
    "Staff of Thunder and Lightning", 10000, 204, "Very Rare", "Combat"
)
wand_of_blinding = Magic_Item("Wand of Binding", 10000, 209, "Rare", "Combat")
wand_of_fear = Magic_Item("Wand of Fear", 10000, 210, "Rare", "Combat")
ioun_stone_awareness = Magic_Item("Ioun Stone Awareness", 12000, 177, "Rare", "Combat")
rod_of_the_pact_keeper = Magic_Item(
    "Rod of the Pact Keeper +1", 12000, 197, "Rare", "Combat"
)
staff_of_charming = Magic_Item("Staff of Charming", 12000, 201, "Rare", "Combat")
sunblade = Magic_Item("Sunblade", 12000, 205, "Rare", "Combat")
staff_of_healing = Magic_Item("Staff of Healing", 13000, 202, "Rare", "Combat")
ring_of_shooting_stars = Magic_Item(
    "Ring of Shooting Stars", 14000, 192, "Very Rare", "Combat"
)
ioun_stone_mastery = Magic_Item("Ioun Stone Mastery", 15000, 177, "Legendary", "Combat")
weapon_3 = Magic_Item("+3 Weapon", 16000, 213, "Very Rare", "Combat")
hammer_of_thunderbolts = Magic_Item(
    "Hammer of Thunderbolts", 16000, 173, "Legendary", "Combat"
)
rod_of_the_pact_keeper_2 = Magic_Item(
    "Rod of the Pact Keeper +2", 16000, 197, "Rare", "Combat"
)
staff_of_fire = Magic_Item("Staff of Fire", 16000, 201, "Very Rare", "Combat")
staff_of_swarming_insects = Magic_Item(
    "Staff of Swarming Insects", 16000, 203, "Rare", "Combat"
)
wand_of_paralysis = Magic_Item("Wand of Paralysis", 16000, 211, "Rare", "Combat")
ring_of_fire_elemental_command = Magic_Item(
    "Ring of Fire Elemental Command", 17000, 190, "Legendary", "Combat"
)
dwarven_thrower = Magic_Item("Dwarven Thrower", 18000, 167, "Very Rare", "Combat")
wand_of_the_war_mage_3 = Magic_Item(
    "Wand of the War Mage +3", 19200, 212, "Very Rare", "Combat"
)
efreeti_chain = Magic_Item("Efreeti Chain", 20000, 167, "Legendary", "Combat")
ring_of_free_action = Magic_Item("Ring of Free Action", 20000, 191, "Rare", "Combat")
sentinel_shield = Magic_Item("Sentinel Shield", 20000, 199, "Uncommon", "Combat")
staff_of_striking = Magic_Item("Staff of Striking", 21000, 203, "Very Rare", "Combat")
ring_of_spell_storing = Magic_Item(
    "Ring of Spell Storing", 24000, 192, "Rare", "Combat"
)
vorporal_sword = Magic_Item("Vorpal Sword", 24000, 209, "Legendary", "Combat")
ring_of_water_elemental_command = Magic_Item(
    "Ring of Water Elemental Command", 25000, 191, "Legendary", "Combat"
)
rod_of_alertness = Magic_Item("Rod of Alertness", 25000, 195, "Very Rare", "Combat")
staff_of_frost = Magic_Item("Staff of Frost", 26000, 201, "Very Rare", "Combat")
instrument_of_the_bards_fochulan_bandlore = Magic_Item(
    "Instrument of the Bards - Fochulan Bandlore", 26500, 176, "Uncommon", "Combat"
)
instrument_of_the_bards_mac_fuirmidh_cittern = Magic_Item(
    "Instrument of the Bards - Mac-Fuirmidh Cittern", 27000, 176, "Uncommon", "Combat"
)
rod_of_lordly_might = Magic_Item(
    "Rod of Lordly Might", 28000, 195, "Legendary", "Combat"
)
rod_of_the_pact_keeper_3 = Magic_Item(
    "Rod of the Pact Keeper +3", 28000, 197, "Very Rare", "Combat"
)
instrument_of_the_bards_doss_lute = Magic_Item(
    "Instrument of the Bards - Doss Lute", 28500, 176, "Uncommon", "Combat"
)
instrument_of_the_bards_canaith_mandolin = Magic_Item(
    "Instrument of the Bards - Canaith Mandolin", 30000, 176, "Rare", "Combat"
)
mantle_of_spell_resistance = Magic_Item(
    "Mantle of Spell Resistance", 30000, 180, "Rare", "Combat"
)
ring_of_spell_turning = Magic_Item(
    "Ring of Spell Turning", 30000, 193, "Legendary", "Combat"
)
prayer_bead_favor = Magic_Item("Prayer Bead - Favor", 32000, 182, "Rare", "Combat")
wand_of_fireballs = Magic_Item("Wand of Fireballs", 32000, 210, "Rare", "Combat")
wand_of_lightning_bolts = Magic_Item(
    "Wand of Lightning Bolts", 32000, 211, "Rare", "Combat"
)
wand_of_polymorph = Magic_Item("Wand of Polymorph", 32000, 211, "Very Rare", "Combat")
instrument_of_the_bards_cli_lyre = Magic_Item(
    "Instrument of the Bards - Cli Lyre", 35000, 176, "Rare", "Combat"
)
scarab_of_protection = Magic_Item(
    "Scarab of Protection", 36000, 199, "Legendary", "Combat"
)
sword_of_answering = Magic_Item("Sword of Answering", 36000, 206, "Legendary", "Combat")
staff_of_the_woodlands = Magic_Item(
    "Staff of the Woodlands", 44000, 204, "Rare", "Combat"
)
spellguard_shield = Magic_Item("Spellguard Shield", 50000, 201, "Very Rare", "Combat")
cloak_of_displacement = Magic_Item(
    "Cloak of Displacement", 60000, 158, "Rare", "Combat"
)
robe_of_stars = Magic_Item("Robe of Stars", 60000, 194, "Very Rare", "Combat")
weapon_of_warning = Magic_Item("Weapon of Warning", 60000, 213, "Uncommon", "Combat")
prayer_bead_wind_walking = Magic_Item(
    "Prayer Bead - Wind Walking", 96000, 182, "Rare", "Combat"
)
instrument_of_the_bards_anstruth_harp = Magic_Item(
    "Instrument of the Bards - Anstruth Harp", 109000, 176, "Very Rare", "Combat"
)
instrument_of_the_bards_ollamh_harp = Magic_Item(
    "Instrument of the Bards - Ollamh Harp", 125000, 176, "Legendary", "Combat"
)
prayer_bead_summons = Magic_Item("Prayer Bead - Summons", 128000, 182, "Rare", "Combat")
holy_avenger = Magic_Item("Holy Avenger", 165000, 174, "Legendary", "Combat")

# Instantiating Non-Combat Items
helm_of_comprehend_languages = Magic_Item(
    "Helm of Comprehend Languages", 500, 173, "Uncommon", "Non-Combat"
)
driftglobe = Magic_Item("Driftglobe", 750, 166, "Uncommon", "Non-Combat")
trident_of_fish_command = Magic_Item(
    "Trident of Fish Command", 800, 209, "Uncommon", "Non-Combat"
)
cap_of_water_breathing = Magic_Item(
    "Cap of Water Breathing", 1000, 157, "Uncommon", "Non-Combat"
)
eversmoking_bottle = Magic_Item(
    "Eversmoking Bottle", 1000, 168, "Uncommon", "Non-Combat"
)
quiver_of_ehlonna = Magic_Item("Quiver of Ehlonna", 1000, 189, "Uncommon", "Non-Combat")
ioun_stone_sustenance = Magic_Item(
    "Ioun Stone Sustenance", 1000, 177, "Rare", "Non-Combat"
)
ring_of_warmth = Magic_Item("Ring of Warmth", 1000, 193, "Uncommon", "Non-Combat")
goggles_of_night = Magic_Item("Goggles of Night", 1500, 172, "Uncommon", "Non-Combat")
horseshoes_of_the_zephyr = Magic_Item(
    "Horseshoes of the Zephyr", 1500, 175, "Very Rare", "Non-Combat"
)
mariners_armor = Magic_Item("Mariner's Armor", 1500, 181, "Uncommon", "Non-Combat")
necklace_of_adaptation = Magic_Item(
    "Necklace of Adaptation", 1500, 182, "Uncommon", "Non-Combat"
)
ring_of_water_walking = Magic_Item(
    "Ring of Water Walking", 1500, 193, "Uncommon", "Non-Combat"
)
wand_of_magic_detection = Magic_Item(
    "Wand of Magic Detection", 1500, 211, "Uncommon", "Non-Combat"
)
wand_of_secrets = Magic_Item("Wand of Secrets", 1500, 211, "Uncommon", "Non-Combat")
gloves_of_swimming_and_climbing = Magic_Item(
    "Gloves of Swimming and Climbing", 2000, 172, "uncommon", "Non-Combat"
)
hewards_handy_haversack = Magic_Item(
    "Heward's Handy Haversack", 2000, 174, "Rare", "Non-Combat"
)
rope_of_climbing = Magic_Item("Rope of Climbing", 2000, 197, "Uncommon", "Non-Combat")
ring_of_feather_falling = Magic_Item(
    "Ring of Feather Falling", 2000, 191, "Rare", "Non-Combat"
)
boots_of_elvenking = Magic_Item(
    "Boots of Elvenkind", 2500, 155, "Uncommon", "Non-Combat"
)
eyes_of_minute_seeing = Magic_Item(
    "Eyes of Minute Seeing", 2500, 155, "Uncommon", "Non-Combat"
)
eyes_of_the_eagle = Magic_Item("Eyes of the Eagle", 2500, 168, "Uncommon", "Non-Combat")
ring_of_jumping = Magic_Item("Ring of Jumping", 2500, 191, "Uncommon", "Non-Combat")
dimensional_shackles = Magic_Item(
    "Dimensional Shackles", 3000, 165, "Rare", "Non-Combat"
)
eyes_of_charming = Magic_Item("Eyes of Charming", 3000, 168, "Uncommon", "Non-Combat")
medallion_of_thoughts = Magic_Item(
    "Medallion of Thoughts", 3000, 181, "Uncommon", "Non-Combat"
)
ring_of_swimming = Magic_Item("Ring of Swimming", 3000, 193, "Uncommon", "Non-Combat")
bag_of_holding = Magic_Item("Bag of Holding", 4000, 153, "Uncommon", "Non-Combat")
boots_of_levitation = Magic_Item("Boots of Levitation", 4000, 153, "Rare", "Non-Combat")
ring_of_animal_influence = Magic_Item(
    "Ring of Animal Influence", 4000, 189, "Rare", "Non-Combat"
)
boots_of_striding_and_springing = Magic_Item(
    "Boots of Striding and Springing", 5000, 156, "Uncommon", "Non-Combat"
)
cloak_of_arachnida = Magic_Item(
    "Cloak of Arachnida", 5000, 156, "Uncommon", "Non-Combat"
)
cloak_of_elvenking = Magic_Item(
    "Cloak of Elvenkind", 5000, 158, "Uncommon", "Non-Combat"
)
gloves_of_thievery = Magic_Item(
    "Gloves of Thievery", 5000, 172, "Uncommon", "Non-Combat"
)
hat_of_disguise = Magic_Item("Hat of Disguise", 5000, 173, "Uncommon", "Non-Combat")
horseshoes_of_speed = Magic_Item("Horseshoes of Speed", 5000, 175, "Rare", "Non-Combat")
immovable_rod = Magic_Item("Immovable Rod", 5000, 175, "Uncommon", "Non-Combat")
lantern_of_revealing = Magic_Item(
    "Lantern of Revealing", 5000, 179, "Uncommon", "Non-Combat"
)
periapt_of_health = Magic_Item("Periapt of Health", 5000, 185, "Uncommon", "Non-Combat")
periapt_of_proof_against_poison = Magic_Item(
    "Periapt of Proof Against Poison", 5000, 184, "Rare", "Non-Combat"
)
slippers_of_spider_climbing = Magic_Item(
    "Slippers of Spider Climbing", 5000, 200, "Uncommon", "Non-Combat"
)
cloak_of_the_bat = Magic_Item("Cloak of the Bat", 6000, 159, "Rare", "Non-Combat")
cloak_of_the_manta_ray = Magic_Item(
    "Cloak of the Manta Ray", 6000, 159, "Uncommon", "Non-Combat"
)
ring_of_x_ray_vision = Magic_Item(
    "Ring of X-Ray Vision", 6000, 193, "Rare", "Non-Combat"
)
cape_of_the_mountebank = Magic_Item(
    "Cape of the Mountebank", 8000, 157, "Rare", "Non-Combat"
)
portable_hole = Magic_Item("Portable Hole", 8000, 185, "Rare", "Non-Combat")
apparatus_of_kwalish = Magic_Item(
    "Apparatus of Kwalish", 10000, 151, "Legendary", "Non-Combat"
)
boots_of_the_winterlands = Magic_Item(
    "Boots of the Winterlands", 10000, 156, "Uncommon", "Non-Combat"
)
folding_boat = Magic_Item("Folding Boat", 10000, 170, "Rare", "Non-Combat")
ring_of_invisibility = Magic_Item(
    "Ring of Invisibility", 10000, 191, "Legendary", "Non-Combat"
)
helm_of_telepathy = Magic_Item(
    "Helm of Telepathy", 12000, 174, "Uncommon", "Non-Combat"
)
cube_of_force = Magic_Item("Cube of Force", 16000, 159, "Rare", "Non-Combat")
ring_of_mind_shielding = Magic_Item(
    "Ring of Mind Shielding", 16000, 191, "Uncommon", "Non-Combat"
)
rod_of_rulership = Magic_Item("Rod of Rulership", 16000, 197, "Rare", "Non-Combat")
mirror_of_life_trapping = Magic_Item(
    "Mirror of Life Trapping", 18000, 181, "Very Rare", "Non-Combat"
)
amulet_of_proof_against_detection_and_location = Magic_Item(
    "amulet_of_proof_against_detection_and_location",
    20000,
    150,
    "Uncommon",
    "Non-Combat",
)
robe_of_eyes = Magic_Item("Robe of Eyes", 30000, 193, "Rare", "Non-Combat")
gem_of_seeing = Magic_Item("Gem of Seeing", 32000, 193, "Rare", "Non-Combat")
plate_armor_of_etherealness = Magic_Item(
    "Plate Armor of Etherealness", 48000, 185, "Legendary", "Non-Combat"
)

# Instantiating Summoning Items
ivory_goat_travail = Magic_Item("Ivory Goat (Travail)", 400, 169, "Rare", "Summoning")
golden_lion = Magic_Item("Golden Lion (Each)", 600, 169, "Rare", "Summoning")
ivory_goat_traveling = Magic_Item(
    "Ivory Goat (Traveling)", 1000, 169, "Rare", "Summoning"
)
staff_of_the_python = Magic_Item(
    "Staff of the Python", 2000, 204, "Uncommon", "Summoning"
)
onyx_dog = Magic_Item("Onyx Dog", 3000, 170, "Rare", "Summoning")
silver_raven = Magic_Item("Silver Raven", 5000, 170, "Uncommon", "Summoning")
silver_horn_of_valhalla = Magic_Item(
    "Silver Horn of Valhalla", 5600, 175, "Rare", "Summoning"
)
marble_elephant = Magic_Item("Marble Elephant", 6000, 170, "Rare", "Summoning")
bowl_of_commanding_water_elementals = Magic_Item(
    "Bowl of Commanding Water Elementals", 8000, 156, "Rare", "Summoning"
)
brazier_of_commanding_fire_elementals = Magic_Item(
    "Brazier of Commanding Fire Elementals", 8000, 156, "Rare", "Summoning"
)
censer_of_controlling_air_elementals = Magic_Item(
    "Censer of Controlling Air Elementals", 8000, 158, "Rare", "Summoning"
)
stone_of_controlling_earth_elmentals = Magic_Item(
    "Stone of Controlling Earth Elementals", 8000, 175, "Rare", "Summoning"
)
brass_horn_of_valhalla = Magic_Item(
    "Brass Horn of Valhalla", 11200, 175, "Very Rare", "Summoning"
)
iron_horn_of_valhalla = Magic_Item(
    "Iron Horn of Valhalla", 14000, 175, "Legendary", "Summoning"
)
ivory_goat_terror = Magic_Item("Ivory Goat (Terror)", 20000, 169, "Rare", "Summoning")

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
    vicious_weapon,
    adamantine_armor,
    mithiral_armor,
    weapon_1,
    sword_of_life_stealing,
    ioun_stone_protection,
    wand_of_the_war_mage_1,
    bracers_of_archery,
    circlet_of_blasting,
    javelin_of_lightning,
    prayer_bead_smiting,
    wind_fan,
    sword_of_sharpness,
    staff_of_the_adder,
    dancing_sword,
    glamoured_studded_leather,
    pipes_of_the_sewers,
    prayer_bead_bless,
    saddle_of_the_cavalier,
    sword_of_wounding,
    frost_brand,
    dagger_of_venom,
    gloves_of_missile_snaring,
    ioun_stone_agility,
    ioun_stone_fortitude,
    ioun_stone_insight,
    ioun_stone_intellect,
    ioun_stone_leadership,
    ioun_stone_strength,
    staff_of_withering,
    cloak_of_protection,
    oathbow,
    ring_of_protection,
    weapon_2,
    boots_of_speed,
    dragon_scale_mail,
    elven_chain,
    ioun_stone_regeneration,
    iron_bands_of_bilarro,
    prayer_bead_curing,
    rope_of_entanglement,
    wand_of_enemy_detection,
    luckstone,
    wand_of_the_war_mage_2,
    flame_tongue,
    periapt_of_wound_closure,
    ring_of_evasion,
    ring_of_the_ram,
    tentacle_rod,
    animated_shield,
    armor_of_resistance,
    arrow_catching_shield,
    belt_of_dwarvenkind,
    bracers_of_defence,
    ioun_stone_reserve,
    pearl_of_power,
    pipes_of_haunting,
    ring_of_resistance,
    robe_of_scintillating_colors,
    scimitar_of_speed,
    shield_of_missile_attraction,
    giant_slayer,
    mace_of_smiting,
    brooch_of_shielding,
    amulet_of_health,
    dragon_slayer,
    gauntlets_of_ogre_power,
    headband_of_intellect,
    mace_of_disruption,
    mace_of_terror,
    nine_lives_stealer,
    wand_of_magic_missile,
    wand_of_web,
    staff_of_thunder_and_lightning,
    wand_of_blinding,
    wand_of_fear,
    ioun_stone_awareness,
    rod_of_the_pact_keeper,
    staff_of_charming,
    sunblade,
    staff_of_healing,
    ring_of_shooting_stars,
    ioun_stone_mastery,
    weapon_3,
    hammer_of_thunderbolts,
    rod_of_the_pact_keeper_2,
    staff_of_fire,
    staff_of_swarming_insects,
    wand_of_paralysis,
    ring_of_fire_elemental_command,
    dwarven_thrower,
    wand_of_the_war_mage_3,
    efreeti_chain,
    ring_of_free_action,
    sentinel_shield,
    staff_of_striking,
    ring_of_spell_storing,
    vorporal_sword,
    ring_of_water_elemental_command,
    rod_of_alertness,
    staff_of_frost,
    instrument_of_the_bards_fochulan_bandlore,
    instrument_of_the_bards_mac_fuirmidh_cittern,
    rod_of_lordly_might,
    rod_of_the_pact_keeper_3,
    instrument_of_the_bards_doss_lute,
    instrument_of_the_bards_canaith_mandolin,
    mantle_of_spell_resistance,
    ring_of_spell_turning,
    prayer_bead_favor,
    wand_of_fireballs,
    wand_of_lightning_bolts,
    wand_of_polymorph,
    instrument_of_the_bards_cli_lyre,
    scarab_of_protection,
    sword_of_answering,
    staff_of_the_woodlands,
    spellguard_shield,
    cloak_of_displacement,
    robe_of_stars,
    weapon_of_warning,
    prayer_bead_wind_walking,
    instrument_of_the_bards_anstruth_harp,
    instrument_of_the_bards_ollamh_harp,
    prayer_bead_summons,
    holy_avenger,
    helm_of_comprehend_languages,
    driftglobe,
    trident_of_fish_command,
    cap_of_water_breathing,
    eversmoking_bottle,
    quiver_of_ehlonna,
    ioun_stone_sustenance,
    ring_of_warmth,
    goggles_of_night,
    horseshoes_of_the_zephyr,
    mariners_armor,
    necklace_of_adaptation,
    ring_of_water_walking,
    wand_of_magic_detection,
    wand_of_secrets,
    gloves_of_swimming_and_climbing,
    hewards_handy_haversack,
    rope_of_climbing,
    ring_of_feather_falling,
    boots_of_elvenking,
    eyes_of_minute_seeing,
    eyes_of_the_eagle,
    ring_of_jumping,
    dimensional_shackles,
    eyes_of_charming,
    medallion_of_thoughts,
    ring_of_swimming,
    bag_of_holding,
    boots_of_levitation,
    ring_of_animal_influence,
    boots_of_striding_and_springing,
    cloak_of_arachnida,
    cloak_of_elvenking,
    gloves_of_thievery,
    hat_of_disguise,
    horseshoes_of_speed,
    immovable_rod,
    lantern_of_revealing,
    periapt_of_health,
    periapt_of_proof_against_poison,
    slippers_of_spider_climbing,
    cloak_of_the_bat,
    cloak_of_the_manta_ray,
    ring_of_x_ray_vision,
    cape_of_the_mountebank,
    portable_hole,
    apparatus_of_kwalish,
    boots_of_the_winterlands,
    folding_boat,
    ring_of_invisibility,
    helm_of_telepathy,
    cube_of_force,
    ring_of_mind_shielding,
    rod_of_rulership,
    mirror_of_life_trapping,
    amulet_of_proof_against_detection_and_location,
    robe_of_eyes,
    gem_of_seeing,
    plate_armor_of_etherealness,
    ivory_goat_travail,
    golden_lion,
    ivory_goat_traveling,
    staff_of_the_python,
    onyx_dog,
    silver_raven,
    silver_horn_of_valhalla,
    marble_elephant,
    bowl_of_commanding_water_elementals,
    brazier_of_commanding_fire_elementals,
    censer_of_controlling_air_elementals,
    stone_of_controlling_earth_elmentals,
    brass_horn_of_valhalla,
    iron_horn_of_valhalla,
    ivory_goat_terror,
]

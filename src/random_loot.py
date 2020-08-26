from src.magic_items import magic_items
import random


def randomized_loot_by_rarity(num_of_items, rarity, item_type):
    # Filter by item_type
    item_type_filter = []
    if item_type != "":
        for key in magic_items:
            if key.lower() == item_type.lower():
                item_type_filter = magic_items[key]
    else:
        for key in magic_items:
            item_type_filter.extend(magic_items[key])
    # Create a new list of items filtered by the specified rarity
    rarity_filter = []
    for item in item_type_filter:
        if item.rarity.lower() == rarity.lower():
            rarity_filter.append(item)
    # Select a number of randomized items from the filtered list based on the number specified
    randomized_items = []
    for n in range(num_of_items):
        randomized_items.append(random.choice(rarity_filter))
    return randomized_items

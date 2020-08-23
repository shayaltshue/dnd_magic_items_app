from src.magic_items import magic_items


def find_item(item_name):
    for item in magic_items:
        if item.name.str.contains(item_name):
            return item

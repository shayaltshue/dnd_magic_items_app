from src.magic_items import magic_items


def find_item(item_name):
    all_items = []
    for key in magic_items:
        all_items.extend(magic_items[key])
    results = []
    for item in all_items:
        if item_name.lower() in item.name.lower():
            results.append(item)
    return results

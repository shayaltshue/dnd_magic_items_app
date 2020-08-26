from src.magic_items import magic_items


def find_item(item_name):
    results = []
    for item in magic_items:
        if item_name.lower() in item.name.lower():
            results.append(item)
    return results

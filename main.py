from src.random_loot import randomized_loot_by_rarity

def greet():
    print('Welcome to the Magic Item Generator/Searcher!')
    print('\n')

def show_menu():
    print('''What would you like to do?
    \t type "search" to find a specific magic item
    \t type "loot" to generate magic item loot
    \t type "exit" to quit the application''')

greet()

run_app = True

while(run_app):
    show_menu()
    user_input =input("type what action you would like to take here: ")

    if user_input.lower() == 'search':
        pass

    elif user_input.lower() == 'loot':
        num_items = int(input('How many items? '))
        rarity = input("What rarity? Options are: Common, Uncommon, Rare, Legendary: ")
        item_type = input('What type of magic item? Options are: Consumable, Combat, non-Combat. Leave blank if no preference: ')

        items = randomized_loot_by_rarity(num_items, rarity, item_type)
        print('-----------------------')
        print('Items:')
        for item in items:
            item.describe()
        print('-----------------------')
        print('\n')

    elif user_input.lower() == 'exit':
        print('Thanks for using the Magic Item Generator/Finder!')
        break


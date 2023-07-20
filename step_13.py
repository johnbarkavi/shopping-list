import os

with open ('data_file.txt', 'r') as f:
    shop_products = f.read().splitlines()

fruits = shop_products[:2]
vegetables = shop_products [3:6]
citrus_fruits = shop_products[6:8]



def clear_terminal():
    """Clears the terminal window."""
    os.system('cls' if os.name == 'nt' else 'clear')


EXIT_COMMANDS = ('q', 'quit', 'exit', 'ex')

shopping_list = list()




def help():
    print("You can exit with 'q' or 'quit' or 'exit' ro 'ex'")


def beautify_list(product_list: list) -> list:
    for product in product_list:
        print(f"-{product}")


def add_to_list(product_list: list, product: str) -> None:
    product_list.append(product)


def remove_item(product_list: list, product: str):
    if product in product_list:
        product_list.remove(product)
        print(f"{product} has removed")
    else:
        print('item dose not exist')

def search_item(product_list: list, product: str):
    if product not in product_list:
        print(f"{product} is not in your list")
    else:
        print(f"{product} is in your list")

def show_category(category_list: list, category: str):
    if category in category_list:
        print(category)
    else:
        print('wrong category, please choose againe')

while True:
    welcome = '---------- welcome to our amazing shop ----------'
    print(welcome.center(100))
    item = input("please enter item you want to add to your list: ").casefold()
    clear_terminal()



# exit commands
    if item in EXIT_COMMANDS:
        beautify_list(shopping_list)
        clear_terminal()

        break
    elif item == 'help':
        help()
        clear_terminal()
    elif item in shopping_list:
        input(f"{item} had added before: press ENTER to continue")
        clear_terminal()

    elif item == "show":
        beautify_list(shopping_list)
        clear_terminal()

    elif item == "remove":
        user_remove_item = input("please enter item you want to remove it : ")
        remove_item(shopping_list, user_remove_item)
        clear_terminal()



else:
    add_to_list(shopping_list, item)
print(f"{item} added tp shopping list, total item: {len(shopping_list)}")
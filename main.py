from product import *

# === Main menu loop ===
while True:
    print(
        """
Menu
1. Register Product
2. List All Stock
3. List Category
4. Search Product
5. Remove Product
6. Update Product
7. Export Stock

0. Exit
"""
    )
    option = input("Choose an option: ")

    action = menu_actions.get(option)

    if action:
        title, func = action
        if title:
            print(f"\n{title}")
        func(stock)
    else:
        print("Invalid option! Please try again.")

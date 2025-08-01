from product import *

stock = []

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

0. Exit
"""
    )
    option = input("Choose an option: ")

    if option == "1":
        print("\n--- Register Product ---")
        register(stock)

    elif option == "2":
        print("\n--- Stock ---")
        list_stock(stock)

    elif option == "3":
        print("\n--- Category ---")
        list_category(stock)

    elif option == "4":
        print("\n--- Search Product ---")
        search_product(stock)

    elif option == "5":
        print("\n--- Remove Product ---")
        remove_product(stock)

    elif option == "6":
        print("\n--- Update Product ---")
        update_register(stock)

    elif option == "0":
        print("Exiting the system...")
        break
    else:
        print("Invalid option! Please try again.")

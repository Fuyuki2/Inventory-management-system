stock = []


def register(stock):
    product_id = int(input("Enter the product ID: "))
    name = input("Enter the product name: ")
    quantity = int(input("Enter the product quantity: "))
    category = input("Enter the product category: ")
    product = {
        "product_id": product_id,
        "name": name,
        "quantity": quantity,
        "category": category
    }
    stock.append(product)
    print(f"Product {name} successfully registered!")


def update_register(stock):
    product_id = int(input("Enter the product ID: "))
    for product in stock:
        if product['product_id'] == product_id:
            product['product_id'] = int(input("Enter the new product ID: "))
            product['name'] = input("Enter the new product name: ")
            product['quantity'] = int(input("Enter the new product quantity: "))
            print(f"Product {product['name']} successfully updated!")


def list_stock(stock):
    if not stock:
        print("Stock is empty!")
    else:
        for product in stock:
            print(
                f"ID: {product['product_id']} | Name: {product['name']} | Quantity: {product['quantity']} | Category: {product['category']}"
            )


def remove_product(stock):
    product_id = int(input("Enter the product ID: "))
    found = False
    for i, product in enumerate(stock):
        if product['product_id'] == product_id:
            found = True
            stock.pop(i)
            print(f"Product {product['name']} removed!")
            break

    if not found:
        print("Product not found!")


while True:
    print("""
Menu
1. Register Product
2. List All Stock
3. List Category
4. Search Product
5. Remove Product
6. Update Product

0. Exit
""")
    option = input("Choose an option: ")

    if option == "1":
        register(stock)

    elif option == "2":
        print("\n--- Stock ---")
        list_stock(stock)

    elif option == "3":
        remove_product(stock)

    elif option == "4":
        update_register(stock)

    elif option == "0":
        print("Exiting the system...")
        break
    else:
        print("Invalid option! Please try again.")
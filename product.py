import json
import csv

stock = []


def register(stock):
    product_id = int(input("Enter the product ID: "))
    for product in stock:
        if product["product_id"] == product_id:
            print("ID already exists!")
            return
    name = input("Enter the product name: ")
    quantity = int(input("Enter the product quantity: "))
    category = input("Enter the product category: ")
    product = {
        "product_id": product_id,
        "name": name,
        "quantity": quantity,
        "category": category,
    }
    stock.append(product)
    print(f"Product {name} successfully registered!")


def update_register(stock):
    product_id = int(input("Enter the product ID: "))
    for product in stock:
        if product["product_id"] == product_id:
            product["product_id"] = int(input("Enter the new product ID: "))
            product["name"] = input("Enter the new product name: ")
            product["quantity"] = int(input("Enter the new product quantity: "))
            print(f"Product {product['name']} successfully updated!")


def list_stock(stock):
    if not stock:
        print("Stock is empty!")
    else:
        for product in stock:
            print(
                f"ID: {product['product_id']} | Name: {product['name']} | Quantity: {product['quantity']} | Category: {product['category']}"
            )


def list_category(stock):
    category = input("Enter the category: ")
    found = False
    for product in stock:
        if product["category"] == category:
            print(
                f"ID: {product['product_id']} | Name: {product['name']} | Quantity: {product['quantity']} | Category: {product['category']}"
            )
            found = True
        if not found:
            print("Category not found!")


def search_product(stock):
    product_id = input("Enter the product ID: ")
    found = False
    for product in stock:
        if product["product_id"] == product_id:
            print(
                f"ID: {product['product_id']} | Name: {product['name']} | Quantity: {product['quantity']} | Category: {product['category']}"
            )
            found = True
        if not found:
            print("Product not found!")


def remove_product(stock):
    product_id = int(input("Enter the product ID: "))
    found = False
    for i, product in enumerate(stock):
        if product["product_id"] == product_id:
            found = True
            stock.pop(i)
            print(f"Product {product['name']} removed!")
            break

    if not found:
        print("Product not found!")


def export_to_json(stock):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"stock_export_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(stock, file, indent=4)


def export_to_csv(stock):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"stock_export_{timestamp}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["product_id", "name", "quantity", "category"])

        for product in stock:
            writer.writerow(
                [
                    product["product_id"],
                    product["name"],
                    product["quantity"],
                    product["category"],
                ]
            )


def export_stock(stock):
    while True:
        print(
            """
        1. Export to JSON
        2. Export to CSV
        0. Exit
        """
        )
        option = input("Choose an option: ")
        if option == "1":
            export_to_json(stock)
            print("Stock exported to JSON successfully!")
            break
        elif option == "2":
            export_to_csv(stock)
            print("Stock exported to CSV successfully!")
            break
        elif option == "0":
            break
        else:
            print("Invalid option! Please try again.")

import json
import csv

# Initialize stock and id count
stock = []
id_count = 0


# Function to register a new product
def register(stock):
    global id_count
    id_count += 1
    product_id = f"PROD-{id_count:05d}"
    # Ask for product information
    name = input("Enter the product name: ")
    quantity = int(input("Enter the product quantity: "))
    category = input("Enter the product category: ")

    # Create a dictionary with the product information
    product = {
        "product_id": product_id,
        "name": name,
        "quantity": quantity,
        "category": category,
    }
    # Add the product to the stock list
    stock.append(product)
    print(f"Product {name} successfully registered!")


# Function to update a product
def update_register(stock):
    product_id = input("Enter the product ID: ")
    for product in stock:
        if product["product_id"] == product_id:
            # Update product information
            product["category"] = input("Enter the new product category: ")
            product["name"] = input("Enter the new product name: ")
            product["quantity"] = int(input("Enter the new product quantity: "))
            print(f"Product {product['name']} successfully updated!")


# Function to remove a product from stock
def remove_product(stock):
    product_id = input("Enter the product ID: ")
    found = False
    for i, product in enumerate(stock):
        if product["product_id"] == product_id:
            found = True
            stock.pop(i)
            print(f"Product {product['name']} removed!")
            break

    if not found:
        print("Product not found!")


# Function to list all products in stock
def list_stock(stock):
    if not stock:
        print("Stock is empty!")
    else:
        for product in stock:
            print(
                f"ID: {product['product_id']} | Name: {product['name']} | Quantity: {product['quantity']} | Category: {product['category']}"
            )


# Function to list products by category
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


# Function to search for a product by ID
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


# Function to export stock to JSON
def export_to_json(stock):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"stock_export_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(stock, file, indent=4)


# Function to export stock to CSV
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


# Menu to choose export format
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


def exit_program():
    print("Exiting the program...")
    exit()


menu_actions = {
    "1": ("--- Register Product ---", register),
    "2": ("--- Stock ---", list_stock),
    "3": ("--- Category ---", list_category),
    "4": ("--- Search Product ---", search_product),
    "5": ("--- Remove Product ---", remove_product),
    "6": ("--- Update Product ---", update_register),
    "7": ("--- Export Stock ---", export_stock),
    "0": ("", exit_program),
}

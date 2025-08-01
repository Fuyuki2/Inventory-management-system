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

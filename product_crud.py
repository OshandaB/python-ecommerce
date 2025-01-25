from product import Product

#create a product object
product1 = Product("Phone", 34000, 10)
print(product1.get_details())

is_update_or_create = input("Do you want to update product or create a new product? (update/create): ")

if is_update_or_create == "create":
    #create a new product
    name = input("Enter the name of the product: ")
    price = input("Enter the price of the product: ")
    quantity = input("Enter the quantity of the product: ")
    product2 = Product(name, price, quantity)
    print(product2.get_details())
else:
    #update the product
    new_price = input("Enter the new price of the product: ")
    new_quantity = input("Enter the new quantity of the product: ")
    product1.update_price(new_price)
    product1.update_quantity(new_quantity)
    print(product1.get_details())
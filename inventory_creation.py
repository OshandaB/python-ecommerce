from product import Product
from inventory import Inventory

name = input("Enter the name of the product: ")
price = input("Enter the price of the product: ")
quantity = input("Enter the quantity of the product: ")

product1 = Product(name, price, quantity)
print(product1.get_details())

inventory = Inventory()

inventory.addProduct(product1)
print(inventory.checkStock(product1))

inventory.removeProduct(product1)


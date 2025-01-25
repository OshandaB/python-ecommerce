from product import Product

#create a product object
product1 = Product("Phone", 34000, 10)
print(product1.get_details())

#update the price of the product
product1.update_price(35000)
print(product1.get_details())
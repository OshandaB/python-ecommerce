from customer import Customer
from order import Order
from product import Product

#create a products
product1 = Product("Phone", 34000, 10)
product2 = Product("Laptop", 45000, 5)

#create a customer
customer1 = Customer("John", "Colombo", "0771234567")

#create an order
order1 = Order(customer1)
order1.add_product(product1)
order1.add_product(product2)

#calculate the total price
total = order1.calculate_total()
print(f"Total price: Rs{total}")

#Genarate and print order summary
print(order1.generate_order_summary())

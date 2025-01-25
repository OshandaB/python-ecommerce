from customer import Customer
from order import Order
from product import Product

def get_product_details():
    name = input("Enter product name: ")
    price = float(input(f"Enter price for {name}: "))
    quantity = int(input(f"Enter quantity available for {name}: "))
    return Product(name, price, quantity)

def get_customer_details():
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    phone = input("Enter customer phone number: ")
    return Customer(name, address, phone)

print("Welcome to the E commerce!")

print("\n--- Customer Details ---")
customer = get_customer_details()

products = []
num_products = int(input("How many products would you like to add? "))
for _ in range(num_products):
    product = get_product_details()
    products.append(product)

order = Order(customer)

print("\n--- Add Products to Order ---")
for product in products:
    print(f"Product: {product.name}, Price: Rs{product.price}, Available Quantity: {product.quantity}")
    add_to_order = input(f"Would you like to add {product.name} to the order? (yes/no): ").strip().lower()
    if add_to_order == "yes":
        order.add_product(product)

total = order.calculate_total()
print(f"\nTotal price: Rs{total}")

print("\n--- Order Summary ---")
print(order.generate_summary())

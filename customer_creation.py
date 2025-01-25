from customer import Customer

#create a customer object
customer1 = Customer('Alice',"Galle",'0763884997')
print(customer1.get_details())

is_update_or_create = input("Do you want to update customer or create a new customer? (update/create): ")

if is_update_or_create == "create":
    #create a new customer
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of customer: ")
    contact = input("Enter the contact of customer: ")
    customer2 = Customer(name, address, contact)
    print(customer2.get_details())
else:
    #update the customer
    new_name = input("Enter the new name of the customer: ")
    new_address = input("Enter the new address of the customer: ")
    new_contact = input("Enter the new contact of the customer: ")
    customer1.update_name(new_name)
    customer1.update_address(new_address)
    customer1.update_contact(new_contact)

    print(customer1.get_details())



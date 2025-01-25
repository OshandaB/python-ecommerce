class Customer:
    def __init__(self,name,address,contact):
       self.name=name
       self.address=address
       self.contact=contact

    def get_details(self):
      return f"Customer name: {self.name}, Customer address: {self.address}, Customer contact: {self.contact}"       

customer1=Customer('Alice', "Weligama","076858484")
customer2=Customer('Bob',"Galle","076858484")

print(customer1.get_details())
print(customer2.get_details())

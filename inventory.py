from product import Product
class Inventory:
    def __init__(self):
        self.products = {}

    def addProduct(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def removeProduct(self, product):
        if product.name in self.products:
            if self.products[product.name].quantity >= product.quantity:
                self.products[product.name].quantity -= product.quantity
            else:
                print("Insufficient stock for "+product.name)
        else:
            print("Product "+product.name+" not found.")

    def checkStock(self, product):
        if product.name in self.products:
            return self.products[product.name].quantity
        else:
            return 0
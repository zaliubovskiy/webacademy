class Store:
    def show_price(self, products):
        print("Price List")
        print("==================")
        for product in products:
            print(f"{product.name} ---> {product.show_price()} USD")
            print("")

    def show_quantity(self, products):
        print("Availability")
        print("============")
        for product in products:
            print(f"{product.name} ---> {product.show_quantity()}")
            print("")


class Product:
    def __init__(self, id, name, price, quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_price(self):
        return self.price

    def show_quantity(self):
        return self.quantity

    def add_to_bag(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            return f"The product {self.name} is out of stock"

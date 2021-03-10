class Store:
    def __init__(self, city, products):
        self.city = city
        self.products = products

    def show_pricelist(self):
        print(f"Price List for store in {self.city}")
        print("============================")

        # If it is physical product- shows the price
        # If it is subscription -> shows price for the selected duration
        for product in self.products:
            if isinstance(product, Item) and product.quantity != 0:
                print(f"{product.name} ---> {product.show_price()} USD")
            elif isinstance(product, Subscription):
                print(f"{product.name} ---> {product.show_price()} USD")
        print("============================")

    def show_availability(self):
        print(f"Availability in {self.city}")
        print("==================")
        for product in self.products:

            # Shows availability only for Items, subscription is alway available
            if isinstance(product, Item):
                print(f"{product.name} ---> {product.show_quantity()}")
                print("")
        print("============================")


class Product:
    def __init__(self, id, name, price: int):
        self.id = id
        self.name = name
        self.price = price

    def show_price(self):
        return f"{self.price} USD"


# Class for physical products like iPhones or MacBooks
class Item(Product):
    def __init__(self, id, name, price: int, quantity: int = 0):
        super().__init__(id, name, price)
        self.quantity = quantity

    def show_quantity(self):
        return f"{self.quantity} items left in stock"

    def add_to_bag(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            return f"The product {self.name} is out of stock"


# Class for subscriptions like Apple Music or Apple One
class Subscription(Product):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)

    def subscribe(self, duration=1):
        if duration == 1:
            mon = "month"
        elif duration > 1:
            mon = "months"
        else:
            return print(f"Please enter valid duration (from 1 to 60")
        return print(f"You have subscribed to the {self.name} for {duration} {mon}")

    def show_price(self, duration=1):
        if duration == 1:
            return print(f"The price is {self.price}USD/month")
        elif duration > 1:
            return print(f"The price for {duration} months is {self.price * duration} USD")
        else:
            return print(f"Please enter valid duration (from 1 to 60")


# Class for old devices specially for "Trade in" discount program
class OldDevice(Product):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)

    def trade_in(self):
        self.price *= (-1)
        return self.price

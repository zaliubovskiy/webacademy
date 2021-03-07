class Buyer:
    def __init__(self, id, name="Anonymous", wallet=0, currency="USD", bag=None):
        if bag is None:
            bag = []
        self.id = id
        self.name = name
        self.wallet = wallet
        self.currency = currency
        self.bag = bag

    def add_to_bag(self, product):
        self.bag.append(product)
        product.add_to_bag()

    def checkout(self, seller):
        for i in self.bag:
            self.wallet -= i.price
            seller.balance += i.price
        print(f"Thank you for your purchase!")
        self.bag.clear()

    def show_bag(self):
        if self.bag:
            total = 0
            print(f"Your bag contains {len(self.bag)} items")
            print(f"=========================")
            for i in self.bag:
                print(i.name)
                total += i.price
            print("==========================")
            print(f"Total amount - {total} USD")
        else:
            return print(f"Your bag is empty")

    def get_balance(self):
        return print(f"Your balance now is {self.wallet}")


class Seller:
    def __init__(self, balance=0):
        self.balance = balance
        self.currency = "USD"

    def get_balance(self):
        return print(f"Your balance now is {self.balance}")

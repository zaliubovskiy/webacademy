import transactions
# Module "transactions" needed only for the transaction operation:
# (buyer's balance "-" the total amount of the bag) and
# (seller's balance "+" the total amount of the bag)
# It is not used in other modules, so there is no risk of "Circular Import Issue"


class Buyer:
    def __init__(self, id, name, wallet: int = 0, currency="USD"):
        self.bag = []
        self.id = id
        self.name = name
        self.wallet = wallet
        self.currency = currency
        # Used as a "Trade-in" discount for the purchase (optional)
        self.old_device = None

    def add_to_bag(self, product):
        self.bag.append(product)
        product.add_to_bag()

    def subscribe(self, subscription, duration=1):
        self.bag.append(subscription)
        subscription.subscribe(duration)

    # Only shows what's in the bag. Doesn't purchase anything
    def show_bag(self):
        if self.old_device:
            self.old_device.name += " *Trade-in*"
            self.old_device.trade_in()
            self.bag.append(self.old_device)
        elif self.bag:
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

    def show_balance(self):
        if self.currency in transactions.supportable_currencies:
            return print(f"Your balance is {self.wallet} {self.currency}")
        else:
            return print(f"Sorry, we don't support your currency. Only {transactions.supportable_currencies}")

    def show_currency(self):
        return print(f"Your currency is {self.currency}")

    # Purchase process in this method:
    def checkout(self, seller):
        if self.bag:
            for i in self.bag:
                seller.balance += i.price
                new_price = i.price

                # Is there a way to use this in the "program module"?
                converter = transactions.CurrencyExchange(currency_to=self.currency)
                if self.currency != "USD":
                    new_price = converter.convert(new_price)
                self.wallet -= new_price

            self.bag.clear()
            return print(f"{self.name}, thank you for your purchase!\n"
                         f"All of it will be delivered to {seller.city}")
        else:
            return print(f"Your bag is empty")


class Seller:
    def __init__(self, city, balance=0):
        self.balance = balance
        self.city = city.city
        self.currency = "USD"

    def get_balance(self):
        return print(f"Your balance now is {self.balance} {self.currency}")

    def show_currency(self):
        return print(f"Our currency is {self.currency}")

    def show_location(self):
        return print(f"We are located at {self.city}")

    def show_pricelist(self):
        return self.city.show_pricelist()

    def show_availability(self):
        return self.city.show_availability()

    def city(self):
        return self.city

import products
import accounts
# import transactions - imported in "accounts" module, it's not used anywhere but that module.


# All products including Items, Subscriptions, and OldDevices:
# Maybe try [dict] the next time?

# Items
iphone_12 = products.Item(1, "Apple iPhone 12", 1000, 15)
airpods = products.Item(2, "Apple AirPods 2", 200, 40)
ipad = products.Item(3, "Apple iPad Pro", 800, 12)
macbook = products.Item(4, "Apple MacBook Air 3", 2000, 5)
watch = products.Item(5, "Apple Watch Series 6", 400, 46)

# Subscriptions
music = products.Subscription(6, "Apple Music", 3)
tv = products.Subscription(7, "Apple TV", 10)
icloud = products.Subscription(8, "iCloud Storage 50 GB", 3)

# Old Devices
iphone_6 = products.OldDevice(9, "iPhone 6", 200)
iphone_7 = products.OldDevice(9, "iPhone 7", 250)
iphone_8 = products.OldDevice(11, "iPhone 8", 300)


# Lists of availability in stores in different cities
products_kyiv = [iphone_12, airpods, ipad, macbook, watch, music, tv, icloud]
products_lviv = [iphone_12, airpods, watch, music, tv, icloud]
products_rivne = [iphone_12, music, icloud]


# Stores by names of its cities
kyiv = products.Store("Kyiv", products_kyiv)
lviv = products.Store("Lviv", products_lviv)
rivne = products.Store("Rivne", products_rivne)


if __name__ == "__main__":
    jackson = accounts.Buyer(1, "Jackson", 20000, "CAD")
    tyson = accounts.Buyer(2, "Tyson", 30000, "EUR")
    jordan = accounts.Buyer(3, "Jordan", 1000000, "UAH")

    kyiv_seller = accounts.Seller(kyiv, 50000)
    rivne_seller = accounts.Seller(rivne, 7777)
    lviv_seller = accounts.Seller(lviv)

    jackson.add_to_bag(airpods)
    jackson.subscribe(icloud)
    jackson.show_bag()
    jackson.show_balance()
    jackson.show_currency()
    jackson.show_balance()
    jackson.checkout(kyiv_seller)
    jackson.show_balance()
    kyiv_seller.get_balance()

    jordan.show_balance()
    jordan.add_to_bag(watch)
    jordan.checkout(lviv_seller)
    jordan.show_balance()
    lviv_seller.get_balance()

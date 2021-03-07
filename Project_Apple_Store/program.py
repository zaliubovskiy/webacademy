import products
import accounts


iphone = products.Product(1, "Apple iPhone 6", 600, 15)
airpods = products.Product(2, "Apple AirPods 2", 200, 40)
ipad = products.Product(3, "Apple iPad Pro", 800, 12)
macbook = products.Product(4, "Apple MacBook Air 3", 2000, 5)
watch = products.Product(5, "Apple Watch Series 6", 400, 46)

list_of_all = [iphone, airpods, ipad, macbook, watch]

if __name__ == "__main__":
    # products.Store().show_price(list_of_all)
    # products.Store().show_quantity(list_of_all)
    maxim = accounts.Buyer(1, "Maxim", 20000)
    superseller = accounts.Seller(50000)
    maxim.add_to_bag(airpods)
    maxim.add_to_bag(macbook)
    maxim.add_to_bag(ipad)
    maxim.show_bag()
    maxim.checkout(superseller)
    maxim.get_balance()
    superseller.get_balance()

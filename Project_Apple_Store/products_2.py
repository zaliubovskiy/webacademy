# iphone = Product(1, "Apple iPhone 6", 600, 15)
# airpods = Product(2, "Apple AirPods 2", 200, 40)
# ipad = Product(3, "Apple iPad Pro", 800, 12)
# macbook = Product(4, "Apple MacBook Air 3", 2000, 5)
# watch = Product(5, "Apple Watch Series 6", 400, 46)


class Store:
    def __init__(self):
        self._products = {
            1: {"name": "Apple iPhone 6",
                "price": 600,
                "quantity": 15
                },
            2: {"name": "Apple AirPods 2",
                "price": 200,
                "quantity": 40
                },
            3: {"name": "Apple iPad Pro",
                "price": 800,
                "quantity": 12
                },
            4: {"name": "Apple MacBook Air 3",
                "price": 2000,
                "quantity": 5
                },
            5: {"name": "Apple Watch Series 6",
                "price": 400,
                "quantity": 46
                }
        }

    def products(self):
        return [Product(id_) for id_ in sorted(self._products)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info

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


# class Product:
#     def __init__(self, id, name, price, quantity=0):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def show_price(self):
#         return self.price
#
#     def show_quantity(self):
#         return self.quantity
#
#     def add_to_bag(self):
#         if self.quantity > 0:
#             self.quantity -= 1
#         else:
#             return f"The product {self.name} is out of stock"

# Q1: Design & create an online store
# - Store name and price
# - Track total products
# - Create static method to calculate discount


class product:
    count = 0


    def __init__(self,name,price):
        self.name = name
        self.price = price
        product.count +=1

    def get_info(self):
        print(f"Name of the product {self.name} and price is Rs. {self.price}")
    @classmethod
    def get_count(cls):
        print(f"Total Number of Products = {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"Discounted Price = {price - (price*discount)/100}")


p1 = product("Laptop" , 160000)
p2 = product("Mobile" , 80000)
p3 = product("charger" , 1200)

p1.get_info()
p2.get_info()
p3.get_info()
product.get_count()
p1.calc_discount(160000,15)
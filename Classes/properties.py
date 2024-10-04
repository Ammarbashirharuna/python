class Product:
    def __init__(self, price):
        self.price = price


    @property
    def price(self):
        return self.set_price


    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price can not be negative.")
        self.set_price = value
        #using property method


product = Product(210)
print(product.price)
class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannnot be negative.")
        self.__price = value


product = Product(10)
print(product.price)

# when defining properties we do not always have to define getter and setter

# print(product.__class__.__name__)
# print(type(product).__name__)

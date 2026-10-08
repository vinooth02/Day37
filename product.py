class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discount(self, discount):
        discount_amount = self.price * discount / 100
        final_price = self.price - discount_amount

        return final_price
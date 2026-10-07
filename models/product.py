"""Model Product — Minggu 04.
Class induk yang menyimpan data dan perilaku dasar semua produk.
"""


class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self._price = price
        self._stock = stock

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            raise ValueError("Insufficient stock")
        self._stock -= quantity

    def subtotal(self, quantity):
        return self._price * quantity

    def get_description(self):
        return self.name


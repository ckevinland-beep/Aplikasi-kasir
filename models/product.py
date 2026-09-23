"""Model Product — Minggu 03 (Encapsulation).

price dan stock tidak lagi dapat diubah langsung dari luar.
Setiap perubahan harus lewat method yang menjaga aturannya.
"""


class Product:
    def __init__(self, code, name, price, stock):
    #attribut
        self.code = code
        self.name = name
        # Garis bawah = penanda: ini state internal, jangan disentuh dari luar.
        self._price = price
        self._stock = stock

    @property
    def price(self):
        # Boleh dibaca, tidak boleh ditulis langsung.
        return self._price

    @property
    def stock(self):
        return self._stock

    def subtotal(self, quantity):
        return self._price * quantity
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
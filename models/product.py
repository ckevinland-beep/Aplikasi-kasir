"""Model Product — Minggu 02. 
Satu class yang menyatukan DATA produk (attribute) dan 
PERILAKU produk (method) dalam satu tempat. 
""" 

class Product:
    def __init__(self, code, name, price, stock):
    #attribut
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

    def subtotal(self, quantity):
        #method
        return self.price * quantity

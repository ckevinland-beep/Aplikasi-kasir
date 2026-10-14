"""Simple Cashier — Minggu 04 (Inheritance & Polymorphism).

Menguji Product, FoodProduct, dan DigitalProduct
dengan inheritance, overriding, dan polymorphism.
"""

from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct
from services.action_history import ActionHistory
from services.order_queue import OrderQueue

products = [
    Product("P001", "Indomie", 3000, 20),
    FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"),
    DigitalProduct("D001", "E-Book Python", 50000, 99),
]

print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print()

print("--- Polymorphism ---")

# Satu list berisi tiga jenis object.
# Setiap object menjalankan get_description()
# sesuai dengan class masing-masing.
for item in products:
    print(item.code, "|", item.get_description())

print()

print("--- Yang diwarisi dari Product ---")

roti = products[1]

# subtotal() diwarisi dari Product.
print("Subtotal 3 Roti:", roti.subtotal(3))

# expiry_date hanya dimiliki oleh FoodProduct.
print("Kedaluwarsa Roti:", roti.expiry_date)

print()

print("--- Encapsulation Minggu 03 tetap berlaku di subclass ---")

# price tetap read-only.
try:
    roti.price = 1
except AttributeError:
    print("FoodProduct.price tetap read-only.")

# Harga negatif tetap ditolak.
try:
    roti.change_price(-1000)
except ValueError as error:
    print("FoodProduct.change_price(-1000) ->", error)

# Pengurangan stock melebihi persediaan tetap ditolak.
try:
    roti.reduce_stock(999)
except ValueError as error:
    print("FoodProduct.reduce_stock(999) ->", error)

# Pengurangan stock yang valid.
roti.reduce_stock(3)
print("Stock Roti setelah terjual 3:", roti.stock)

print()
print("--- Antrean order (FIFO) ---")
# Order sungguhan baru dibuat di Minggu 10.
# Untuk sekarang cukup teks sederhana sebagai penanda antrean.
queue = OrderQueue()
queue.enqueue("ORD-001 Indomie x2")
queue.enqueue("ORD-002 Teh Botol x1")
queue.enqueue("ORD-003 Roti x3")
print("Masuk : ORD-001, ORD-002, ORD-003")
print("Keluar :", queue.dequeue())
print("Keluar :", queue.dequeue())
print("Keluar :", queue.dequeue())
print("Antrean kosong ->", queue.dequeue(), "(tidak error)")
print("Yang pertama masuk, pertama juga dilayani.")

print()
print("--- Riwayat tindakan (LIFO) ---")
history = ActionHistory()
history.push("tambah Indomie x2")
history.push("tambah Teh Botol x1")
history.push("tambah Roti x3")
print("Dilakukan :", "tambah Indomie x2, tambah Teh Botol x1, tambah Roti x3")
print("Undo :", history.pop())
print("Undo :", history.pop())
print("Undo :", history.pop())
print("Riwayat kosong ->", history.pop(), "(tidak error)")
print("Yang terakhir dilakukan, pertama dibatalkan.")
print()
print("--- Queue vs Stack ---")
print("Queue (antrean order) : FIFO -> masuk A B C, keluar A B C")
print("Stack (undo) : LIFO -> masuk A B C, keluar C B A")
print()
print("--- Mengapa dictionary untuk katalog? ---")
print("Katalog dicari berdasarkan code -> dictionary, satu langkah.")
print("Daftar tampilan mementingkan urutan -> list.")
print("Hasil pencarian bisa nol/satu/banyak -> list.")
print("Antrean order dilayani berurutan -> queue (deque).")
print("Undo membatalkan yang terakhir -> stack (list).")

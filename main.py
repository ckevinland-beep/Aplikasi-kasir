
"""Simple Cashier - Minggu 06 (List, Dictionary, Stack & Queue)."""

from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct
from models.product_catalog import ProductCatalog
from services.action_history import ActionHistory
from services.order_queue import OrderQueue


# Katalog produk menggunakan dictionary.
catalog = ProductCatalog()
catalog.add(Product("P001", "Indomie", 3000, 20))
catalog.add(FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"))
catalog.add(DigitalProduct("D001", "E-Book Python", 50000, 99))

products = catalog.all()

print("=========================")
print("     SIMPLE CASHIER")
print("=========================")

print("\n--- Katalog Produk (Dictionary) ---")
for item in products:
    print(item.code, "|", item.get_description())

print("\nCari produk dengan kode P001:")
print(catalog.get("P001").get_description())

print("\nCari produk dengan nama Roti:")
for item in catalog.search("roti"):
    print(item.get_description())

print("\n--- Inheritance & Polymorphism ---")
roti = catalog.get("F001")
print("Subtotal 3 Roti:", roti.subtotal(3))
print("Kedaluwarsa Roti:", roti.expiry_date)

print("\n--- Validasi Produk ---")
try:
    roti.price = 1
except AttributeError:
    print("Harga tetap read-only.")

try:
    roti.change_price(-1000)
except ValueError as error:
    print("Harga negatif ditolak:", error)

try:
    roti.reduce_stock(999)
except ValueError as error:
    print("Stok berlebih ditolak:", error)

roti.reduce_stock(3)
print("Stok Roti setelah terjual 3:", roti.stock)

print("\n--- Antrean Order (FIFO) ---")
queue = OrderQueue()
queue.enqueue("ORD-001 Indomie x2")
queue.enqueue("ORD-002 Teh Botol x1")
queue.enqueue("ORD-003 Roti x3")

print("Keluar:", queue.dequeue())
print("Keluar:", queue.dequeue())
print("Keluar:", queue.dequeue())
print("Antrean kosong:", queue.dequeue())

print("\n--- Riwayat Tindakan (LIFO) ---")
history = ActionHistory()
history.push("tambah Indomie x2")
history.push("tambah Teh Botol x1")
history.push("tambah Roti x3")

print("Undo:", history.pop())
print("Undo:", history.pop())
print("Undo:", history.pop())
print("Riwayat kosong:", history.pop())

print("\n--- Struktur Data ---")
print("Dictionary: menyimpan dan mencari produk berdasarkan kode.")
print("List: menampilkan daftar produk.")
print("Queue: order pertama masuk, pertama dilayani (FIFO).")
print("Stack: tindakan terakhir dilakukan, pertama dibatalkan (LIFO).")

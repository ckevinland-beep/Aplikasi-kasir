"""Simple Cashier - Minggu 09 (Database Persistence).

Program demonstrasi materi Minggu 02-09 secara berurutan.
"""

from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct
from models.product_catalog import ProductCatalog
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from services.action_history import ActionHistory
from services.order_queue import OrderQueue


def judul(teks):
    print()
    print("---", teks, "---")


print("=========================")
print("     SIMPLE CASHIER")
print("   Week 09 - SQLite")
print("=========================")

# ------------------------------------------------------------------
# Minggu 02-03 - Class, Object, Encapsulation
# ------------------------------------------------------------------
judul("W02-03 Class, Object, Encapsulation")

contoh = Product("P000", "Contoh", 3000, 20)
print("subtotal(2)      :", contoh.subtotal(2))

try:
    contoh.price = -5000
except AttributeError:
    print("price = -5000              : ditolak (read-only property)")

try:
    contoh.change_price(-5000)
except ValueError as error:
    print("change_price(-5000):", error)

try:
    contoh.reduce_stock(999)
except ValueError as error:
    print("reduce_stock(999):", error)

# ------------------------------------------------------------------
# Minggu 04 - Inheritance & Polymorphism
# ------------------------------------------------------------------
judul("W04 Inheritance & Polymorphism")

varian = [
    Product("P001", "Indomie", 3000, 20),
    FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"),
    DigitalProduct("D001", "E-Book Python", 50000, 99),
]

# Satu loop, tiga hasil berbeda, tanpa memeriksa jenis produk.
for item in varian:
    print(f"{item.code:5} {item.get_description()}")

# ------------------------------------------------------------------
# Minggu 09 - Repository & Database
# ------------------------------------------------------------------
judul("W09 Repository & Database")

product_repository = ProductRepository()
order_repository = OrderRepository()

catalog = ProductCatalog()

for product in product_repository.load():
    catalog.add(product)

print("Dimuat dari SQLite :", len(catalog.all()), "produk")
print("get('P001')         :", product_repository.get("P001").name)
print("get('P999')         :", product_repository.get("P999"))

# ------------------------------------------------------------------
# Minggu 05 - List & Dictionary
# ------------------------------------------------------------------
judul("W05 Catalog: List & Dictionary")

for item in catalog.all():
    print(f"{item.code:5} {item.name:12} {item.price:>6} stock {item.stock}")

print()
print("get('P001')               :", catalog.get("P001").name, "(dictionary, satu langkah)")
print("get('P999')               :", catalog.get("P999"), "(tidak error)")
print("search('teh')             :", [p.name for p in catalog.search("teh")])
print("search('TEH')             :", [p.name for p in catalog.search("TEH")])
print("search('kopi')            :", catalog.search("kopi"), "(tidak ditemukan)")

# ------------------------------------------------------------------
# Minggu 06 - Stack & Queue
# ------------------------------------------------------------------
judul("W06 Queue (FIFO) vs Stack (LIFO)")

queue = OrderQueue()
history = ActionHistory()

for penanda in ["A", "B", "C"]:
    queue.enqueue(penanda)
    history.push(penanda)

print("Masuk                     : A B C")
print("Queue keluar              :", queue.dequeue(), queue.dequeue(), queue.dequeue(), "(FIFO)")
print("Stack keluar              :", history.pop(), history.pop(), history.pop(), "(LIFO)")
print("Queue kosong              :", queue.dequeue(), "| Stack kosong:", history.pop())

# ------------------------------------------------------------------
# Alur penuh - Object -> Struktur Data -> Repository -> Database
# ------------------------------------------------------------------
judul("Alur penuh: Object -> Struktur Data -> Repository -> Database")

indomie = catalog.get("P001")
jumlah = 3

print("Stock Indomie sebelum :", indomie.stock)

if indomie.stock >= jumlah:
    indomie.reduce_stock(jumlah)
    history.push(f"jual Indomie x{jumlah}")

    order = {
        "order_id": order_repository.next_order_id(),
        "total": indomie.subtotal(jumlah),
        "status": "QUEUED",
        "items": [
            {
                "code": indomie.code,
                "quantity": jumlah,
            }
        ],
    }

    queue.enqueue(order)
    order_repository.save(queue.dequeue())
    product_repository.save(catalog.all())

    print("Stock Indomie sesudah :", indomie.stock)
    print("Order tersimpan       :", order["order_id"], "total", order["total"])

    segar = ProductRepository().get("P001")
    print("Stock Indomie di database :", segar.stock)

    orders = OrderRepository().load()
    print("Jumlah order tersimpan     :", len(orders))

    if orders:
        terakhir = orders[-1]
        print(
            "Order terakhir             :",
            terakhir["order_id"],
            terakhir["status"],
            "dengan",
            len(terakhir["items"]),
            "item",
        )
else:
    print("Stock tidak cukup - penjualan dilewati.")

# ------------------------------------------------------------------
# Rantai konsep yang harus bisa dijelaskan
# ------------------------------------------------------------------
judul("Rantai yang harus bisa dijelaskan")
print("Class -> Object -> Data Structure -> Repository -> Database")
print("Berubah : repositories/ (CSV/JSON -> SQL)")
print("Tetap   : models/, services/ - tidak satu baris pun disentuh")

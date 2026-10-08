"""Simple Cashier — Minggu 05 (List & Dictionary).

Menguji ProductCatalog dengan dictionary sebagai penyimpan
dan list sebagai hasil tampilan serta pencarian.
"""

from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct
from models.product_catalog import ProductCatalog


catalog = ProductCatalog()

catalog.add(Product("P001", "Indomie", 3000, 20))
catalog.add(Product("P002", "Teh Botol", 4000, 15))
catalog.add(Product("P003", "Teh Kotak", 3500, 10))
catalog.add(FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"))
catalog.add(DigitalProduct("D001", "E-Book Python", 50000, 99))


print("=========================")
print("     SIMPLE CASHIER      ")
print("=========================")
print()


print("--- Daftar produk ---")

# all() mengembalikan list.
# Yang dibutuhkan di sini adalah urutan produk.
for item in catalog.all():
    print(item.code, "|", item.get_description())

print()


print("--- Ambil produk lewat code ---")

# Dictionary memungkinkan pencarian berdasarkan code
# tanpa perlu menelusuri seluruh produk.
found = catalog.get("F001")

if found is not None:
    print("catalog.get('F001') ->", found.get_description())

missing = catalog.get("P999")

print("catalog.get('P999') ->", missing, "(tidak error, hanya None)")

print()


print("--- Cari produk lewat nama ---")

# Pencarian berdasarkan potongan nama.
# Huruf besar dan kecil tidak dibedakan.
for keyword in ["teh", "TEH", "mie", "kopi"]:
    hasil = catalog.search(keyword)
    nama = [item.name for item in hasil] if hasil else "tidak ditemukan"
    print(f"search({keyword!r}) -> {nama}")

print()


print("--- Hapus produk ---")

catalog.remove("P002")

print(
    "Setelah remove('P002'):",
    [item.code for item in catalog.all()]
)

# Menghapus code yang sudah tidak ada tidak menyebabkan error.
catalog.remove("P002")

print("remove('P002') sekali lagi tidak menjatuhkan program.")

print()


print("--- Mengapa dictionary untuk katalog? ---")

print("Katalog dicari berdasarkan code -> dictionary, satu langkah.")
print("Daftar tampilan mementingkan urutan -> list.")
print("Hasil pencarian bisa nol/satu/banyak -> list.")
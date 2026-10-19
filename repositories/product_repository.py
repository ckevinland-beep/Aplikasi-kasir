"""ProductRepository — Minggu 07 (File Handling).

Satu-satunya bagian program yang tahu bahwa produk
kebetulan disimpan dalam file CSV.
"""

import csv

from models.product import Product

FIELDNAMES = ["code", "name", "price", "stock"]


class ProductRepository:
    def __init__(self, path):
        self.path = path

    def load(self):
        products = []

        try:
            with open(self.path, newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    products.append(
                        Product(
                            row["code"],
                            row["name"],
                            int(row["price"]),
                            int(row["stock"]),
                        )
                    )
        except FileNotFoundError:
            return []

        return products

    def save(self, products):
        with open(self.path, "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=FIELDNAMES
            )
            writer.writeheader()

            for product in products:
                writer.writerow(
                    {
                        "code": product.code,
                        "name": product.name,
                        "price": product.price,
                        "stock": product.stock,
                    }
                )

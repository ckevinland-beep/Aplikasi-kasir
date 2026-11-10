import sqlite3

from models.product import Product
from repositories.database import DATABASE_PATH, get_connection


class ProductRepository:
    def __init__(self, path=DATABASE_PATH):
        self.path = path

    def load(self):
        products = []

        try:
            with get_connection(self.path) as connection:
                rows = connection.execute(
                    "SELECT code, name, price, stock FROM products"
                ).fetchall()
        except sqlite3.OperationalError:
            return []

        for row in rows:
            products.append(
                Product(row["code"], row["name"], row["price"], row["stock"])
            )

        return products

    def save(self, products):
        with get_connection(self.path) as connection:
            for product in products:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO products (code, name, price, stock)
                    VALUES (?, ?, ?, ?)
                    """,
                    (product.code, product.name, product.price, product.stock),
                )

    def get(self, code):
        with get_connection(self.path) as connection:
            row = connection.execute(
                "SELECT code, name, price, stock FROM products WHERE code = ?",
                (code,),
            ).fetchone()

        if row is None:
            return None

        return Product(row["code"], row["name"], row["price"], row["stock"])

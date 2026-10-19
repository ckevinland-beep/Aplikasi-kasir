"""OrderRepository — Minggu 07 (File Handling).

Order disimpan sebagai JSON, bukan CSV.
Alasannya: order berisi daftar item di dalamnya,
dan bentuk bersarang seperti itu tidak muat dalam tabel CSV.
"""

import json


class OrderRepository:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            with open(self.path) as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save(self, orders):
        with open(self.path, "w") as file:
            json.dump(orders, file, indent=4)

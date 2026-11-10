# Simple Cashier

Aplikasi kasir sederhana berbasis Python untuk mempelajari konsep Object-Oriented Programming (OOP), struktur data, file handling, dan database persistence.

## Fitur

- Pengelolaan data produk.
- Encapsulation melalui property dan validasi.
- Inheritance dan polymorphism.
- Product catalog menggunakan list dan dictionary.
- Struktur data Stack dan Queue.
- Penyimpanan data menggunakan SQLite.
- Penyimpanan riwayat order beserta detail item.

## Menjalankan Aplikasi

Pastikan Python sudah terpasang.

Jalankan aplikasi:

```bash
python main.py
```

Inisialisasi database:

```bash
python -m scripts.init_db
```

Database SQLite akan disimpan di `data/cashier.db`.

## Struktur Proyek

```text
cashier-app/
├── data/
│   ├── products.csv
│   └── schema.sql
├── models/
├── repositories/
│   ├── database.py
│   ├── order_repository.py
│   └── product_repository.py
├── scripts/
│   └── init_db.py
├── services/
├── main.py
└── README.md
```

## Weekly Progress

| Minggu | Materi | Status |
|---|---|---|
| 01-08 | Materi dan checkpoint sebelumnya | Selesai |
| 09 | Database Persistence menggunakan SQLite | Selesai |

## Teknologi

- Python
- SQLite
- Git dan GitHub
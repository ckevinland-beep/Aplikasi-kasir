"""OrderQueue — Minggu 06 (Queue / FIFO).

Konteks bisnis: antrean order di dapur.
Order yang masuk lebih dulu harus dikerjakan lebih dulu.
"""

from collections import deque


class OrderQueue:
    def __init__(self):
        # deque: menambah di belakang dan mengambil dari depan
        # sama-sama murah. List biasa lambat saat mengambil dari depan.
        self.items = deque()
        
    def enqueue(self, order):
        # Masuk lewat belakang antrean.
        self.items.append(order)
        
    def dequeue(self):
        # Keluar lewat depan antrean.
        if not self.items:
            return None
        self.items.popleft()
         
    def is_empty(self):
        return not self.items
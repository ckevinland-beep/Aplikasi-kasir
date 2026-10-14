"""ActionHistory — Minggu 06 (Stack / LIFO).

Konteks bisnis: riwayat tindakan kasir untuk keperluan undo.
Yang dibatalkan selalu tindakan yang paling terakhir dilakukan.
"""


class ActionHistory:
    def __init__(self):
        # List sudah cukup: menambah dan mengambil
        # sama-sama terjadi di ujung yang sama.
        self.actions = []
        
    def push(self, action):
        # Tindakan baru ditumpuk di atas.
        self.actions.append(action)
        
    def pop(self):
        # Yang diambil adalah tumpukan paling atas.
        if not self.actions:
            return None
        return self.actions.pop()

    def is_empty(self):
        return not self.actions
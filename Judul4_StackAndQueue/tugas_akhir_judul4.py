class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1
    
    def is_full(self):
        return self.top_idx == self.MAX - 1
    
    def push(self, x):
        if self.is_full():
            print("Stack penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x

    def pop(self):
        if self.is_empty():
            return None
        val = self.st[self.top_idx]
        self.top_idx -= 1
        return val
    
    def peek(self):
        if self.is_empty():
            return None
        return self.st[self.top_idx]
    
    def display(self):
        if self.is_empty():
            print("(kosong)")
            return
        for i in range(self.top_idx, -1, -1):
            print(f"  - {self.st[i]}")

class TextEditor:
    def __init__(self):
        self.teks = ""
        self.undo_stack = StackArray()
        self.redo_stack = StackArray()

    def ketik(self, tambahan):
        self.undo_stack.push(self.teks)
        self.redo_stack = StackArray()
        self.teks += tambahan
        print(f"Teks sekarang: \"{self.teks}\"")

    def hapus(self, jumlah=1):
        if len(self.teks) == 0:
            print("Tidak ada teks untuk dihapus!")
            return
        self.undo_stack.push(self.teks)
        self.redo_stack = StackArray()
        self.teks = self.teks[:-jumlah]
        print(f"Teks sekarang: \"{self.teks}\"")

    def undo(self):
        if self.undo_stack.is_empty():
            print("Tidak ada aksi yang bisa di-undo!")
            return
        self.redo_stack.push(self.teks)
        self.teks = self.undo_stack.pop()
        print(f"Undo berhasil. Teks sekarang: \"{self.teks}\"")

    def redo(self):
        if self.redo_stack.is_empty():
            print("Tidak ada aksi yang bisa di-redo!")
            return
        self.undo_stack.push(self.teks)
        self.teks = self.redo_stack.pop()
        print(f"Redo berhasil. Teks sekarang: \"{self.teks}\"")

    def tampilkan(self):
        print(f"\nTeks aktif   : \"{self.teks}\"")
        print("Riwayat Undo :")
        self.undo_stack.display()
        print("Riwayat Redo :")
        self.redo_stack.display()

def main():
    editor = TextEditor()
    pilih = 0
    while pilih != 6:
        print("\n=== TEKS EDITOR DENGAN UNDO/REDO ===")
        print("1. Ketik teks")
        print("2. Hapus karakter terakhir")
        print("3. Undo")
        print("4. Redo")
        print("5. Tampilkan status editor")
        print("6. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            teks = input("Masukkan teks yang ingin diketik: ")
            editor.ketik(teks)
        elif pilih == 2:
            try:
                jumlah = int(input("Hapus berapa karakter? "))
                editor.hapus(jumlah)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            editor.undo()
        elif pilih == 4:
            editor.redo()
        elif pilih == 5:
            editor.tampilkan()
        elif pilih == 6:
            pilih = 6
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, npm, nama):
        idx = self.hash_function(npm)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == npm:
                    self.table[i].value = nama
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = npm
                self.table[i].value = nama
                self.table[i].state = SlotState.OCCUPIED
                return True
        return False

    def search(self, npm):
        idx = self.hash_function(npm)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == npm:
                return self.table[i]
        return None

    def remove_key(self, npm):
        entry = self.search(npm)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\n=== Data Absensi Mahasiswa ===")
        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("Kosong")
            elif self.table[i].state == SlotState.DELETED:
                print("Absensi Dibatalkan")
            else:
                print(f"NPM {self.table[i].key} ({self.table[i].value})")

def main():
    absen = HashMapOpenAddressing()
    absen.insert(2515001, "Andi hadir")
    absen.insert(2515002, "Budi hadir")
    absen.insert(2515003, "Citra hadir")
    absen.insert(2515004, "Dewi izin")


    while True:
        print("\n=== Menu Absensi ===")
        print("1. Cari  \n2. Hapus  \n3. Tampilkan \n4. Keluar")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            npm = int(input("Masukkan NPM: "))
            hasil = absen.search(npm)
            if hasil is not None:
                print(f"NPM {hasil.key}: {hasil.value}")
            else:
                print("Mahasiswa tidak ditemukan.")

        elif pilihan == "2":
            absen.display()

        elif pilihan == "3":
            npm = int(input("Masukkan NPM yang dihapus: "))
            if absen.remove_key(npm):
                print(f"Absensi NPM {npm} berhasil dibatalkan.")
            else:
                print("NPM tidak ditemukan.")

        elif pilihan == "4":
            break

if __name__ == "__main__":
    main()

class Node:
    def __init__(self, terjual, judul):
        self.key = terjual
        self.judul = judul
        self.left = None
        self.right = None


class LeaderboardBuku:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, judul):
        if root is None:
            return Node(key, judul)
        if key < root.key:
            root.left = self.insert_node(root.left, key, judul)
        else:
            root.right = self.insert_node(root.right, key, judul)
        return root

    def insert(self, terjual, judul):
        self.root = self.insert_node(self.root, terjual, judul)

    def find_min_node(self, root):
        while root.left:
            root = root.left
        return root

    def cari_key_by_judul(self, root, judul):
        if root is None:
            return None
        if root.judul.lower() == judul.lower():
            return root.key
        left = self.cari_key_by_judul(root.left, judul)
        return left if left is not None else self.cari_key_by_judul(root.right, judul)

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            s = self.find_min_node(root.right)
            root.key, root.judul = s.key, s.judul
            root.right = self.delete_node(root.right, s.key)
        return root

    def hapus_by_judul(self, judul):
        key = self.cari_key_by_judul(self.root, judul)
        if key is None:
            return False
        self.root = self.delete_node(self.root, key)
        return True

    def ranking(self, root, hasil):
        if root is None:
            return
        self.ranking(root.right, hasil)
        hasil.append(root)
        self.ranking(root.left, hasil)

    def terlaris(self):
        r = self.root
        while r and r.right:
            r = r.right
        return r

    def total(self, root):
        if root is None:
            return 0
        return root.key + self.total(root.left) + self.total(root.right)


def cetak_ranking(lb):
    hasil = []
    lb.ranking(lb.root, hasil)
    if not hasil:
        print("Leaderboard masih kosong.")
        return
    print(f"\n{'#':<4} {'Judul Buku':<30} {'Terjual'}")
    print("-" * 45)
    for i, n in enumerate(hasil, 1):
        print(f"{i:<4} {n.judul:<30} {n.key:,}")


def main():
    lb = LeaderboardBuku()

    pilih = 0
    while pilih != 5:
        print("\n=== Leaderboard Buku Terlaris ===")
        print("1. Tambah buku")
        print("2. Lihat ranking")
        print("3. Hapus buku")
        print("4. Info terlaris & total terjual")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue


        if pilih == 1:
            judul = input("Judul buku    : ").strip()
            try:
                jual = int(input("Jumlah terjual: "))
                lb.insert(jual, judul)
                print(f"'{judul}' ditambahkan.")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            cetak_ranking(lb)

        elif pilih == 3:
            cetak_ranking(lb)
            judul = input("\nMasukkan judul yang dihapus: ").strip()
            if lb.hapus_by_judul(judul):
                print(f"'{judul}' berhasil dihapus.")
            else:
                print(f"Judul '{judul}' tidak ditemukan.")

        elif pilih == 4:
            if lb.root is None:
                print("Leaderboard masih kosong.")
            else:
                t = lb.terlaris()
                print(f"Terlaris: {t.judul} dengan penjualan {t.key:,} buah buku")
                print(f"Total buku terjual: {lb.total(lb.root):,} buah buku")

        elif pilih == 5:
            print("Selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
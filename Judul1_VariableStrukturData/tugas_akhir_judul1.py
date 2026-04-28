class Node:
    def __init__(self, halaman):
        self.halaman = halaman 
        self.prev = None
        self.next = None
 
class RiwayatBrowser:
    def __init__(self):
        self.head = None
        self.current = None
 
    def kunjungi(self, halaman):
        baru = Node(halaman)
        if not self.head:
            self.head = baru
            self.current = baru
        else:
            self.current.next = None
            self.current.next = baru
            baru.prev = self.current
            self.current = baru
        print(f"Membuka: '{halaman}'")
 
    def tampilkan_riwayat(self):
        if not self.head:
            print("Belum ada riwayat")
            return
        print("Riwayat Browsing:")
        temp = self.head
        while temp:
            if temp == self.current:
                print("->", temp.halaman, "(sedang dibuka)")
            else:
                print("  ", temp.halaman)
            temp = temp.next
        print()
 
    def kembali(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Kembali ke: '{self.current.halaman}'")
        else:
            print("Tidak ada halaman sebelumnya")
 
    def maju(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Maju ke: '{self.current.halaman}'")
        else:
            print("Tidak ada halaman berikutnya")
 
browser = RiwayatBrowser()
 
while True:
    print("==== Riwayat Browsing ====")
    print("1. Kunjungi halaman baru")
    print("2. Lihat riwayat")
    print("3. Kembali (Back)")
    print("4. Maju (Forward)")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
 
    if pilihan == "1":
        halaman = input("Masukkan nama halaman: ")
        browser.kunjungi(halaman)
    elif pilihan == "2":
        browser.tampilkan_riwayat()
    elif pilihan == "3":
        browser.kembali()
    elif pilihan == "4":
        browser.maju()
    elif pilihan == "5":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")

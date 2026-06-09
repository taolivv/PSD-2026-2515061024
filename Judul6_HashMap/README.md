# Sistem Absensi Mahasiswa Menggunakan Struktur Data Hash Map Open Addressing

## Deskripsi Singkat
Program ini merupakan simulasi sistem absensi mahasiswa sederhana yang dilengkapi dengan fitur pencarian, penghapusan, dan tampilan data. Pengguna dapat mencari data mahasiswa berdasarkan NPM, membatalkan absensi mahasiswa tertentu, serta menampilkan seluruh data absensi.
Program ini mengimplementasikan struktur data Hash Map dengan metode Open Addressing dan Linear Probing sebagai dasar penyimpanan data absensi karena kemampuannya menyimpan dan mengambil data secara efisien dengan kompleksitas waktu rata-rata O(1). Setiap mahasiswa diidentifikasi menggunakan NPM sebagai key dan data absensi sebagai value. Ketika terjadi tabrakan (collision), program secara otomatis mencari slot kosong berikutnya menggunakan teknik linear probing. Ketika data dihapus, slot tidak dikosongkan sepenuhnya melainkan ditandai sebagai DELETED menggunakan mekanisme tombstone agar proses pencarian data lain yang melewati slot tersebut tetap berjalan dengan benar.

## Source Code
<img width="1648" height="4244" alt="code6 FIX" src="https://github.com/user-attachments/assets/7dcae9bb-0cef-4129-af86-92e6b30b5a12" />

Pada baris 1–4, didefinisikan kelas SlotState yang berfungsi sebagai penanda kondisi setiap slot dalam tabel hash. Terdapat tiga konstanta yaitu EMPTY bernilai 0 yang menandakan slot belum pernah diisi, OCCUPIED bernilai 1 yang menandakan slot sedang berisi data, dan DELETED bernilai 2 yang menandakan slot pernah berisi data namun telah dihapus. Bagian ini berfungsi sebagai fondasi logika pengelolaan slot agar operasi pencarian tidak terhenti secara keliru pada slot yang telah dihapus.

Pada baris 6–10, didefinisikan kelas Entry yang merepresentasikan satu slot dalam tabel hash. Method __init__ pada baris 7–10 menginisialisasi tiga atribut yaitu key yang menyimpan NPM mahasiswa, value yang menyimpan data absensi mahasiswa, dan state yang diset ke SlotState.EMPTY secara default. Bagian ini berfungsi sebagai unit penyimpanan data individual dalam tabel hash.

Pada baris 12–18, didefinisikan kelas HashMapOpenAddressing sebagai inti dari program. Method __init__ pada baris 13–15 menerima parameter size dengan nilai default 10, kemudian menginisialisasi atribut SIZE sebagai ukuran tabel dan table berupa list yang berisi objek Entry sebanyak SIZE elemen. Pada baris 17–18, method hash_function menghitung indeks slot menggunakan rumus (key % self.SIZE + self.SIZE) % self.SIZE untuk memastikan hasil selalu bernilai positif. Bagian ini berfungsi sebagai inisialisasi struktur data utama dan fungsi pemetaan key ke indeks tabel.

Pada baris 20–39, didefinisikan method insert yang menerima parameter npm dan nama. Baris 21 menghitung indeks awal menggunakan hash_function, sedangkan baris 22 menginisialisasi variabel first_deleted bernilai -1 sebagai penanda slot DELETED pertama yang ditemukan. Perulangan for pada baris 23–38 melakukan iterasi sebanyak SIZE langkah menggunakan teknik linear probing. Jika slot berstatus OCCUPIED dan NPM yang tersimpan sama, data absensi diperbarui dan method mengembalikan True (baris 25–28). Jika slot berstatus DELETED, indeksnya disimpan ke first_deleted agar dapat digunakan kembali (baris 29–31). Jika slot berstatus EMPTY, data disimpan pada slot tersebut atau pada slot DELETED pertama yang ditemukan (baris 32–38). Jika seluruh tabel telah penuh, maka pada baris 39 method mengembalikan False. Bagian ini berfungsi untuk menyimpan data ke dalam tabel hash dengan penanganan collision menggunakan linear probing.

Pada baris 41–49, didefinisikan method search yang menerima parameter npm. Baris 42 menghitung indeks awal menggunakan hash_function. Perulangan for pada baris 43–48 melakukan iterasi sebanyak SIZE langkah. Jika slot berstatus EMPTY, pencarian dihentikan dan method mengembalikan None karena data dipastikan tidak ada (baris 45–46). Jika slot berstatus OCCUPIED dan NPM yang dicari ditemukan, objek Entry dikembalikan (baris 47–48). Slot berstatus DELETED dilewati tanpa menghentikan pencarian agar data yang melewati slot tersebut akibat linear probing tetap dapat ditemukan. Bagian ini berfungsi untuk mencari data berdasarkan NPM secara efisien.

Pada baris 51–56, didefinisikan method remove_key yang menerima parameter npm. Baris 52 memanggil method search untuk mencari data dengan NPM yang sesuai. Jika data tidak ditemukan, method mengembalikan False (baris 53–54). Jika ditemukan, atribut state dari data tersebut diubah menjadi SlotState.DELETED tanpa menghapus NPM dan data absensi secara fisik (baris 55–56). Teknik ini disebut tombstone deletion yang memastikan rantai linear probing tidak terputus sehingga data lain yang tersimpan setelah slot tersebut masih dapat ditemukan. Bagian ini berfungsi untuk menghapus data tanpa merusak integritas struktur data hash map.

Pada baris 58–67, didefinisikan method display yang mencetak seluruh isi tabel hash. Baris 59 menampilkan judul data absensi mahasiswa. Perulangan for pada baris 60–67 mengiterasi setiap slot dari indeks 0 hingga SIZE-1. Setiap slot dicetak dengan label Kosong jika berstatus EMPTY (baris 62–63), label Absensi Dibatalkan jika berstatus DELETED (baris 64–65), atau menampilkan informasi NPM dan status absensi jika berstatus OCCUPIED (baris 67). Bagian ini berfungsi untuk menampilkan kondisi terkini seluruh data yang tersimpan dalam tabel hash berdasarkan indeks slot.

Pada baris 69–101, didefinisikan fungsi main sebagai pengatur jalannya program secara keseluruhan. Baris 70 membuat objek HashMapOpenAddressing, kemudian pada baris 71–74 dimasukkan empat data awal absensi mahasiswa yaitu NPM 2515001 (Andi hadir), 2515002 (Budi hadir), 2515003 (Citra hadir), dan 2515004 (Dewi izin). Selanjutnya pada baris 77–80 ditampilkan menu utama yang terdiri dari empat pilihan yaitu Cari, Hapus, Tampilkan, dan Keluar.

Jika pengguna memilih menu 1 (Cari) pada baris 82–88, program meminta input NPM yang ingin dicari (baris 83), kemudian melakukan pencarian menggunakan method search (baris 84). Jika data ditemukan, program menampilkan informasi absensi mahasiswa (baris 85–86). Jika tidak ditemukan, program menampilkan pesan "Mahasiswa tidak ditemukan." (baris 87–88).

Jika pengguna memilih menu 2 (Tampilkan) pada baris 90–91, program memanggil method display untuk menampilkan seluruh isi tabel hash.

Jika pengguna memilih menu 3 (Hapus) pada baris 93–98, program meminta input NPM yang ingin dihapus (baris 94). Kemudian method remove_key dipanggil untuk membatalkan absensi mahasiswa tersebut (baris 95). Jika berhasil, program menampilkan pesan bahwa absensi NPM tersebut berhasil dibatalkan (baris 96). Jika data tidak ditemukan, program menampilkan pesan "NPM tidak ditemukan." (baris 98).

Jika pengguna memilih menu 4 (Keluar) pada baris 100–101, perulangan dihentikan menggunakan perintah break sehingga program selesai dijalankan.

Pada baris 103–104, terdapat blok kondisi if __name__ == "__main__": yang digunakan untuk memastikan fungsi main() hanya dipanggil dan dijalankan ketika file dieksekusi secara langsung. Jika file diimpor ke program lain, maka fungsi main() tidak akan otomatis dijalankan. Bagian ini berfungsi sebagai titik masuk utama program sesuai praktik penulisan kode Python yang baik dan benar.

## Output Program
<img width="505" height="232" alt="Screenshot 2026-06-09 204916" src="https://github.com/user-attachments/assets/e703a144-1c00-446d-9ddc-501d83cfcf08" />

Program dimulai dengan langsung menyimpan empat data absensi awal ke dalam tabel hash, kemudian menampilkan menu utama yang terdiri dari empat pilihan. Pengguna memasukkan angka sesuai pilihan yang diinginkan untuk menjalankan fitur yang tersedia.
Jika pengguna memilih pilihan 1, program meminta input NPM yang ingin dicari. Jika NPM ditemukan dalam tabel, program mencetak informasi absensi mahasiswa tersebut. Misalnya pengguna memasukkan NPM 2515001, maka program mencetak: NPM 2515001: Andi hadir. Jika NPM tidak terdaftar, program mencetak pesan Mahasiswa tidak ditemukan.
<img width="583" height="501" alt="Screenshot 2026-06-09 204922" src="https://github.com/user-attachments/assets/519b8176-20e0-40a3-b54b-a78d5289cc17" />

Jika pengguna memilih pilihan 2, program menampilkan seluruh isi tabel hash dari slot 0 hingga slot 9. Slot yang belum pernah diisi ditampilkan sebagai Kosong, slot yang datanya telah dihapus ditampilkan sebagai Absensi Dibatalkan, dan slot yang berisi data aktif ditampilkan dengan format NPM [key] ([value]).
<img width="658" height="736" alt="Screenshot 2026-06-09 204942" src="https://github.com/user-attachments/assets/80f494f9-65ff-486e-b844-31821f2a67e8" />

Jika pengguna memilih pilihan 3, program meminta input NPM yang absensinya ingin dihapus. Jika NPM ditemukan, slot yang bersangkutan ditandai sebagai DELETED dan program mencetak konfirmasi misalnya: Absensi NPM 2515002 berhasil dibatalkan. Jika NPM tidak ditemukan, program mencetak pesan NPM tidak ditemukan. Slot yang ditandai DELETED tidak menghentikan pencarian data lain yang melewatinya akibat proses linear probing sebelumnya.
<img width="400" height="170" alt="Screenshot 2026-06-09 204946" src="https://github.com/user-attachments/assets/091b4941-0170-4597-8211-e2d91fe8eebd" />

Jika pengguna memilih pilihan 4, perulangan dihentikan dan program berakhir.


## Link YouTube
[]

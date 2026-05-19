# Teks Editor dengan Fitur Undo/Redo Menggunakan Struktur Data Stack

## Deskripsi Singkat
Program ini merupakan simulasi teks editor sederhana yang dilengkapi dengan fitur undo dan redo. Pengguna dapat mengetik teks, menghapus karakter terakhir, membatalkan aksi terakhir menggunakan undo, maupun mengulangi aksi yang telah dibatalkan menggunakan redo melalui menu interaktif yang tersedia.
Program ini mengimplementasikan struktur data Stack (tumpukan) sebagai dasar mekanisme undo/redo karena sifatnya yang LIFO (Last In, First Out), yaitu data yang terakhir dimasukkan akan pertama kali dikeluarkan. Setiap kali pengguna melakukan perubahan pada teks, kondisi teks sebelumnya disimpan ke dalam undo_stack. Ketika pengguna memilih undo, kondisi tersebut dipulihkan dan kondisi teks saat itu dipindahkan ke redo_stack agar dapat dikembalikan kembali. Dengan pendekatan ini, riwayat pengeditan teks dapat dikelola secara efisien tanpa perlu menyimpan seluruh riwayat secara manual.

## Source Code
<img width="1294" height="4890" alt="CODE4" src="https://github.com/user-attachments/assets/f597d3d7-e00d-4179-89a2-721b36250ea1" />
Pada baris 1–38, didefinisikan kelas StackArray yang berfungsi sebagai implementasi stack berbasis array. Baris 2–5 mendefinisikan method init yang menginisialisasi stack dengan ukuran maksimum melalui parameter max_size, membuat array berisi None sebanyak MAX elemen, dan menetapkan top_idx dengan nilai -1 yang menandakan stack dalam kondisi kosong. Baris 7–8 mendefinisikan method is_empty yang mengembalikan True jika top_idx bernilai -1. Baris 10–11 mendefinisikan method is_full yang mengembalikan True jika top_idx sudah mencapai MAX - 1. Bagian ini berfungsi sebagai fondasi struktur data yang akan digunakan oleh teks editor.
Pada baris 13–25, didefinisikan method push dan pop. Baris 13–18 mendefinisikan method push yang menerima parameter x, memeriksa terlebih dahulu apakah stack penuh menggunakan is_full(). Jika penuh, program mencetak “Stack penuh” dan menghentikan eksekusi dengan return. Jika tidak penuh, top_idx dinaikkan sebesar 1 kemudian nilai x disimpan pada posisi top_idx tersebut. Baris 20–25 mendefinisikan method pop yang memeriksa apakah stack kosong menggunakan is_empty(). Jika kosong, method mengembalikan None. Jika tidak, nilai pada posisi top_idx disimpan ke variabel val, top_idx dikurangi 1, kemudian val dikembalikan sebagai hasil. Bagian ini berfungsi untuk menambahkan dan mengambil data dari stack sesuai prinsip LIFO.
Pada baris 27–38, didefinisikan method peek dan display. Baris 27–30 mendefinisikan method peek yang mengembalikan nilai teratas stack tanpa menghapusnya, atau None jika stack kosong. Baris 32–38 mendefinisikan method display yang mencetak “(kosong)” jika stack kosong, atau mencetak seluruh isi stack dari atas ke bawah menggunakan perulangan for dari top_idx hingga indeks 0 secara terbalik. Bagian ini berfungsi untuk keperluan inspeksi isi stack tanpa mengubah kondisinya.
Pada baris 39–49, didefinisikan kelas TextEditor yang merupakan inti dari program teks editor. Baris 41–43 mendefinisikan method init yang menginisialisasi teks awal sebagai string kosong, serta membuat dua stack terpisah yaitu undo_stack dan redo_stack menggunakan StackArray(). Baris 45–49 mendefinisikan method ketik yang menerima parameter tambahan. Baris 46–47 menekan kondisi teks saat ini ke undo_stack sebelum perubahan dilakukan. Karena ini merupakan aksi baru, redo_stack dikosongkan dengan membuat objek StackArray() yang baru agar riwayat redo tidak bercampur dengan aksi berbeda. Baris 48–49 menggabungkan teks saat ini dengan tambahan baru kemudian mencetak kondisi teks terkini. Bagian ini berfungsi untuk mencatat setiap pengetikan ke dalam riwayat undo.
Pada baris 51–58, didefinisikan method hapus. Baris 52–54 memeriksa apakah teks saat ini kosong. Jika kosong, program mencetak pesan peringatan dan menghentikan eksekusi. Baris 55–58 menekan kondisi teks ke undo_stack, mengosongkan redo_stack, memotong karakter terakhir sebanyak jumlah yang diminta menggunakan slicing teks[:-jumlah], kemudian mencetak kondisi teks terkini. Bagian ini berfungsi untuk menghapus karakter terakhir pada teks sambil tetap menyimpan riwayat untuk keperluan undo.
Pada baris 60–66, didefinisikan method undo. Baris 61–63 memeriksa apakah undo_stack kosong. Jika kosong, program mencetak pesan bahwa tidak ada aksi yang bisa di-undo. Baris 64–66 menekan kondisi teks saat ini ke redo_stack agar bisa dikembalikan, mengembalikan kondisi teks ke kondisi sebelumnya menggunakan pop dari undo_stack, kemudian mencetak teks setelah undo berhasil. Bagian ini berfungsi untuk membatalkan aksi terakhir dan memindahkan kondisi terkini ke redo_stack.
Pada baris 68–74, didefinisikan method redo. Baris 69–71 memeriksa apakah redo_stack kosong. Jika kosong, program mencetak pesan bahwa tidak ada aksi yang bisa di-redo. Baris 72–74 menekan kondisi teks saat ini ke undo_stack, mengembalikan kondisi teks ke kondisi redo menggunakan pop dari redo_stack, kemudian mencetak teks setelah redo berhasil. Bagian ini berfungsi untuk mengulangi aksi yang sebelumnya telah dibatalkan.
Pada baris 76–81, didefinisikan method tampilkan. Baris 77 mencetak teks aktif saat ini. Baris 78–81 mencetak label “Riwayat Undo :” diikuti isi undo_stack, kemudian mencetak label “Riwayat Redo :” diikuti isi redo_stack. Bagian ini berfungsi untuk memberikan gambaran menyeluruh tentang kondisi editor beserta riwayat aksinya kepada pengguna.
Pada baris 83–118, didefinisikan fungsi main sebagai pengatur jalannya program secara keseluruhan. Baris 83–85 membuat objek editor dari kelas TextEditor dan menginisialisasi variabel pilih dengan nilai 0. Baris 86–118 menjalankan perulangan while selama pilih tidak sama dengan 6. Baris 86–93 mencetak menu utama yang terdiri dari enam pilihan yaitu ketik teks, hapus karakter terakhir, undo, redo, tampilkan status editor, dan keluar. Baris 94–98 menggunakan blok try-except untuk menerima input pilihan dari pengguna dan menangani ValueError jika pengguna memasukkan bukan angka.
Baris 99–118 menangani setiap pilihan menggunakan struktur if-elif-else. Baris 99–101 menangani pilihan 1 dengan meminta input teks dari pengguna kemudian memanggil editor.ketik(). Baris 102–107 menangani pilihan 2 dengan meminta jumlah karakter yang ingin dihapus dalam blok try-except kemudian memanggil editor.hapus(). Baris 108–109 menangani pilihan 3 dengan memanggil editor.undo(). Baris 110–111 menangani pilihan 4 dengan memanggil editor.redo(). Baris 112–113 menangani pilihan 5 dengan memanggil editor.tampilkan(). Baris 114–116 menangani pilihan 6 dengan mengubah nilai pilih menjadi 6 dan mencetak pesan program selesai. Baris 117–118 menangani pilihan di luar rentang 1–6 dengan mencetak pesan pilihan tidak valid. Bagian ini berfungsi sebagai antarmuka interaktif yang menghubungkan pengguna dengan seluruh fitur teks editor.
Pada baris 120–121, terdapat blok kondisi if name == “main” yang digunakan untuk memastikan fungsi main() hanya dipanggil dan dijalankan ketika file ini dieksekusi secara langsung. Jika file ini diimpor oleh program lain, maka fungsi main() tidak akan otomatis berjalan. Bagian ini berfungsi sebagai titik masuk utama program sesuai dengan praktik penulisan kode Python yang baik dan benar.

## Output Program
Program dimulai dengan menampilkan menu utama yang terdiri dari enam pilihan. Pengguna kemudian memilih aksi yang ingin dilakukan dengan memasukkan angka sesuai menu yang tersedia.

<img width="268" height="131" alt="Screenshot 2026-05-19 220331" src="https://github.com/user-attachments/assets/731a5408-b765-48e7-a277-9454ea596ed7" />

Jika pengguna memasukkan input selain angka, program akan menampilkan pesan “Input tidak valid!” kemudian menampilkan kembali menu dan meminta input ulang hingga pengguna memasukkan pilihan yang valid.

<img width="281" height="141" alt="Screenshot 2026-05-19 220337" src="https://github.com/user-attachments/assets/6a45412a-2379-4ee2-9d73-f68017c21e4e" />

Jika pengguna memilih pilihan 1, program meminta teks yang ingin diketik. Setelah teks dimasukkan, program menampilkan kondisi teks terkini. Misalnya pengguna mengetik “Halo Dunia”, maka program mencetak: Teks sekarang: “Halo Dunia”. Setiap pengetikan baru akan ditambahkan ke teks yang sudah ada.

<img width="255" height="139" alt="Screenshot 2026-05-19 220342" src="https://github.com/user-attachments/assets/104c19cb-253f-4d50-8139-eeb044629c60" />

Jika pengguna memilih pilihan 2, program meminta jumlah karakter yang ingin dihapus dari akhir teks. Misalnya teks saat ini adalah “Halo Dunia” dan pengguna menghapus 5 karakter, maka program mencetak: Teks sekarang: “Halo”. Jika teks kosong, program akan mencetak pesan “Tidak ada teks untuk dihapus!”.

<img width="283" height="132" alt="Screenshot 2026-05-19 220349" src="https://github.com/user-attachments/assets/9a164714-0901-4b95-930d-0d42584f0ebd" />

Jika pengguna memilih pilihan 3, program akan membatalkan aksi terakhir dan memulihkan teks ke kondisi sebelumnya. Misalnya setelah menghapus 5 karakter dari “Halo Dunia” menjadi “Halo”, pengguna memilih undo, maka program mencetak: Undo berhasil. Teks sekarang: “Halo Dunia”. Jika tidak ada aksi yang bisa dibatalkan, program mencetak pesan “Tidak ada aksi yang bisa di-undo!”.

<img width="240" height="125" alt="Screenshot 2026-05-19 220358" src="https://github.com/user-attachments/assets/6ca7100c-64d3-4bc0-b753-c1f599267eb1" />

Jika pengguna memilih pilihan 4, program akan mengulangi aksi yang sebelumnya telah dibatalkan. Melanjutkan contoh sebelumnya, jika pengguna memilih redo setelah undo, maka program mencetak: Redo berhasil. Teks sekarang: “Halo”. Jika tidak ada aksi yang bisa diulangi, program mencetak pesan “Tidak ada aksi yang bisa di-redo!”.

<img width="249" height="204" alt="Screenshot 2026-05-19 220404" src="https://github.com/user-attachments/assets/86b9bb0e-067e-4596-a748-50dc927834ba" />

Jika pengguna memilih pilihan 5, program menampilkan teks aktif saat ini beserta isi riwayat undo dan redo dalam format tumpukan dari atas ke bawah. Jika stack kosong, ditampilkan tanda “(kosong)”.

<img width="254" height="122" alt="Screenshot 2026-05-19 220412" src="https://github.com/user-attachments/assets/596bd34a-6a13-48a2-9ffa-956821e99a14" />

Jika pengguna memilih pilihan 6, program mencetak “Program selesai.” dan perulangan dihentikan sehingga program berakhir.


## Link YouTube
[https://youtu.be/OlNdW49gGVA?si=UgLFUdSMZpVDt6Wk]

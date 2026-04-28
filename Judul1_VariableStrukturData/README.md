# Riwayat Browsing Sederhana menggunakan Doubly Linked List
 
## Deskripsi Singkat
 
Program ini adalah simulasi fitur riwayat browsing pada sebuah web browser sederhana. Pengguna dapat mengunjungi halaman web baru, melihat daftar halaman yang sudah dikunjungi, serta berpindah ke halaman sebelumnya (Back) dan halaman berikutnya (Forward), persis seperti tombol Back dan Forward pada browser sungguhan.
Program ini mengimplementasikan struktur data Doubly Linked List karena setiap node memiliki dua pointer yaitu prev yang menunjuk ke halaman sebelumnya dan next yang menunjuk ke halaman berikutnya, sehingga navigasi dua arah bisa dilakukan dengan mudah tanpa perlu mengulang dari awal. Pointer current digunakan untuk menandai halaman yang sedang aktif dibuka.

## Source Code
 <img width="536" height="109" alt="1-5" src="https://github.com/user-attachments/assets/aaa49d3d-ccfa-4c20-aa28-1f0f6434c6ee" />


Pada baris 1-5, kode digunakan untuk membuat class Node yang berfungsi sebagai tempat menyimpan data halaman. Pada baris 2 dibuat konstruktor __init__ yang akan dijalankan saat objek dibuat. Baris 3 menyimpan nama halaman ke dalam atribut self.halaman, sedangkan baris 4 dan 5 digunakan untuk menyimpan pointer ke node sebelumnya (prev) dan node berikutnya (next), keduanya diisi None karena belum ada sambungan saat node pertama kali dibuat.

 <img width="536" height="100" alt="7-10" src="https://github.com/user-attachments/assets/28cc3a3f-8032-429f-8eb3-e3077db9f738" />


Pada baris 7-10, baris 7 dibuat class RiwayatBrowser sebagai class utama untuk mengelola seluruh linked list. Baris 8 adalah konstruktor class tersebut. Baris 9 mendefinisikan self.head sebagai node pertama dalam linked list, dan baris 10 mendefinisikan self.current sebagai penunjuk halaman yang sedang aktif dibuka, keduanya diisi None karena riwayat masih kosong saat program dijalankan pertama kali.

 <img width="536" height="227" alt="12-22" src="https://github.com/user-attachments/assets/77a5bafc-6e11-408e-bec0-34c5c01dad15" />


Pada baris 12-22, baris 12 mendefinisikan fungsi kunjungi yang digunakan untuk menambahkan halaman baru ke dalam riwayat. Baris 13 membuat node baru berisi nama halaman. Baris 14 mengecek apakah riwayat masih kosong. Jika kosong (baris 15-16), node baru langsung dijadikan head sekaligus current. Jika tidak kosong (baris 17-20), baris 17 terlebih dahulu memutus semua node yang ada di depan current agar riwayat Forward yang lama terhapus saat halaman baru dibuka, lalu baris 18 menyambungkan node baru ke next milik current, baris 19 menyambungkan prev milik node baru ke current sehingga terbentuk hubungan dua arah, dan baris 20 menggeser current ke node baru. Baris 22 menampilkan konfirmasi bahwa halaman berhasil dibuka.

 <img width="536" height="269" alt="24-36" src="https://github.com/user-attachments/assets/37e581fc-7b70-4350-9f68-6e8c2f877f8c" />


Pada baris 24-36, baris 24 mendefinisikan fungsi tampilkan_riwayat yang berfungsi menampilkan seluruh halaman dalam riwayat. Baris 25-27 mengecek apakah riwayat kosong, jika iya maka program mencetak "Belum ada riwayat" lalu menghentikan fungsi dengan return. Baris 28 mencetak judul daftar. Baris 29 memulai penelusuran dari node pertama menggunakan variabel temp, lalu baris 30-35 melakukan perulangan untuk menampilkan semua halaman. Jika halaman tersebut adalah yang sedang aktif (baris 31-32), maka output diberi tanda panah (->), jika tidak maka output biasa (baris 33-34). Baris 35 digunakan untuk berpindah ke node berikutnya, dan baris 36 menambahkan baris kosong agar tampilan lebih rapi.

 <img width="536" height="147" alt="38-43" src="https://github.com/user-attachments/assets/651f10c7-088e-4fda-b5f7-291f06af3a3b" />


Pada baris 38-43, baris 38 mendefinisikan fungsi kembali yang berfungsi untuk berpindah ke halaman sebelumnya. Baris 39 mengecek apakah current ada dan memiliki node sebelumnya. Jika ada (baris 40-41), maka pointer current berpindah ke node sebelumnya menggunakan self.current.prev dan program menampilkan nama halaman yang sekarang aktif. Jika tidak ada (baris 42-43), maka program mencetak "Tidak ada halaman sebelumnya".

 <img width="536" height="133" alt="45-50" src="https://github.com/user-attachments/assets/94429f40-da9d-4e36-90c1-05deb5f6fef8" />


Pada baris 45-50, baris 45 mendefinisikan fungsi maju yang berfungsi untuk berpindah ke halaman berikutnya. Cara kerjanya sama persis dengan fungsi kembali, perbedaannya hanya pada baris 46 yang mengecek self.current.next dan baris 47 yang menggeser current ke node berikutnya menggunakan pointer next. Jika tidak ada halaman berikutnya (baris 49-50), program mencetak "Tidak ada halaman berikutnya".
 
 <img width="536" height="203" alt="52- 61" src="https://github.com/user-attachments/assets/21fbc8d2-3e68-4b4e-98da-816493bddf57" />


Pada baris 52, dibuat objek browser dari class RiwayatBrowser untuk digunakan dalam program utama.

Pada baris 54-60, merupakan program utama dengan perulangan while True agar program terus berjalan sampai pengguna memilih keluar. Baris 55-60 menampilkan pilihan menu ke layar setiap kali perulangan berjalan. Lalu, baris 61 menerima input pilihan dari pengguna. 
 
 <img width="536" height="286" alt="63-76" src="https://github.com/user-attachments/assets/731f482a-ac20-4ffe-9fd8-1a94d1b9a87a" />


Baris 63-65 digunakan untuk mengunjungi halaman baru dengan meminta input nama halaman lalu memanggil fungsi kunjungi. Baris 66-67 menampilkan riwayat. Baris 68-69 digunakan untuk berpindah ke halaman sebelumnya. Baris 70-71 digunakan untuk berpindah ke halaman berikutnya. Baris 72-74 digunakan untuk keluar dari program dengan mencetak "Program selesai" lalu menghentikan perulangan menggunakan break. Sedangkan baris 75-76 berfungsi jika input yang dimasukkan tidak valid.

## Output Program
<img width="317" height="583" alt="menu 1" src="https://github.com/user-attachments/assets/afae3f81-8668-4c06-8442-736ba77fd6de" />


User memilih menu 1 (Kunjungi halaman baru) sebanyak tiga kali, program meminta input nama halaman, dan user menginput Google, YouTube, dan GitHub secara berurutan. Setiap kali input dimasukkan, program langsung mencetak konfirmasi seperti "Membuka: 'Google'", "Membuka: 'YouTube'", dan "Membuka: 'GitHub'", lalu menu ditampilkan kembali untuk menunggu input selanjutnya.

<img width="329" height="248" alt="menu 2" src="https://github.com/user-attachments/assets/a94eb86d-1d72-459c-9f42-a3451c5ca97a" />


Saat memilih menu 2 (Lihat riwayat), program menelusuri linked list dari head dan mencetak semua halaman yang ada. Google dan YouTube ditampilkan biasa, sedangkan GitHub ditampilkan dengan tanda -> di depannya karena GitHub adalah node yang sedang ditunjuk oleh current atau halaman yang sedang aktif dibuka.

<img width="308" height="521" alt="menu 3" src="https://github.com/user-attachments/assets/64f741e1-5d99-46f8-987b-1f499e161546" />


Saat memilih menu 3 (Kembali) untuk pertama kali, program mencetak "Kembali ke: 'YouTube'" karena pointer current berpindah ke node sebelumnya yaitu YouTube. Saat menu 3 dipilih lagi, program mencetak "Kembali ke: 'Google'" karena current berpindah lagi ke node sebelumnya yaitu Google. Saat menu 3 dipilih sekali lagi, program mencetak "Tidak ada halaman sebelumnya" karena Google adalah node pertama dan self.current.prev bernilai None.

<img width="309" height="514" alt="menu 4" src="https://github.com/user-attachments/assets/bf35528e-fe24-46b9-89d4-d5dd99a62ce2" />


Saat memilih menu 4 (Maju) dari posisi Google, program mencetak "Maju ke: 'YouTube'" karena pointer current berpindah ke node berikutnya yaitu YouTube. Saat menu 4 dipilih lagi, program mencetak "Maju ke: 'GitHub'" karena current berpindah lagi ke GitHub. Saat menu 4 dipilih sekali lagi, program mencetak "Tidak ada halaman berikutnya" karena GitHub adalah node terakhir dan self.current.next bernilai None.

<img width="283" height="173" alt="menu 5" src="https://github.com/user-attachments/assets/7c41886e-192b-4441-a8c1-7cfa061a5da1" />


Saat pengguna memilih menu 5 (Keluar), program menampilkan "Program selesai", kemudian program berhenti karena perintah break menghentikan perulangan while.

## Link YouTube

[https://youtu.be/uSq9Sy_b0XY?si=yMy30Cjw-XAy-7QK]

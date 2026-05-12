# Sistem Pencarian Plat Nomor Parkir Menggunakan Algoritma Sequential Search

## Deskripsi Singkat
Program ini merupakan simulasi sistem pencarian log kendaraan pada area parkir. Pengguna dapat memasukkan plat nomor kendaraan yang ingin dicari, kemudian sistem akan menampilkan berapa kali kendaraan tersebut tercatat masuk ke area parkir serta pada indeks ke berapa kendaraan tersebut terakhir kali terlihat dalam log.
Program ini mengimplementasikan algoritma Sequential Search karena data log kendaraan bersifat acak dan tidak terurut, sehingga tidak memungkinkan penggunaan Binary Search. Algoritma ini menelusuri setiap elemen satu per satu dari awal hingga akhir tanpa berhenti saat pertama kali ditemukan, sehingga seluruh kemunculan plat nomor yang dicari dapat dihitung. Selain itu, variabel last_index digunakan untuk mencatat posisi terakhir kendaraan ditemukan dalam log, sehingga informasi yang ditampilkan lebih lengkap dan berguna.

## Source Code
<img width="1422" height="403" alt="code3 1" src="https://github.com/user-attachments/assets/91e918e0-3807-4c06-b640-aa19ba62c6c0" />
Pada baris 1–10, dibuat fungsi sequential_search yang digunakan untuk menelusuri seluruh data log parkir dan menghitung kemunculan plat nomor target. Baris 2 menginisialisasi variabel i sebagai indeks penelusuran yang dimulai dari 0. Baris 3 menginisialisasi variabel counter untuk menghitung jumlah kemunculan, dimulai dari 0 karena belum ada yang ditemukan. Baris 4 menginisialisasi variabel last_index dengan nilai -1 yang berarti plat nomor belum ditemukan sama sekali.
Pada baris 5 dilakukan perulangan while selama i belum melewati batas array. Baris 6 melakukan pengecekan apakah elemen pada posisi i sama dengan plat nomor yang dicari. Jika cocok, baris 7 menambahkan counter sebanyak 1 dan baris 8 memperbarui last_index dengan nilai i saat itu, sehingga yang tersimpan selalu indeks kemunculan paling akhir. Baris 9 menggeser indeks ke elemen berikutnya agar penelusuran dapat dilanjutkan. Setelah seluruh data selesai ditelusuri, baris 10 mengembalikan dua nilai sekaligus yaitu counter dan last_index. Bagian ini berfungsi untuk memastikan seluruh kemunculan plat nomor tercatat dan posisi terakhirnya diketahui.
<img width="1422" height="288" alt="code3 2" src="https://github.com/user-attachments/assets/29f17973-0dee-4680-939b-dde2fa6ea494" />
Pada baris 12–18, dibuat fungsi main sebagai pengatur jalannya program. Baris 13–17 mendefinisikan data log plat nomor kendaraan yang sudah ditentukan isinya, terdiri dari 10 entri log kendaraan yang masuk ke area parkir. Baris 18 menghitung panjang array secara otomatis menggunakan len() sehingga tidak perlu ditulis manual. Bagian ini berfungsi sebagai sumber data utama yang akan ditelusuri oleh algoritma pencarian.
<img width="1422" height="377" alt="code3 3" src="https://github.com/user-attachments/assets/555005ab-62b5-42e7-8d68-5256d3e273dd" />
Pada baris 20–28, program menampilkan seluruh isi log parkir dalam format tabel. Baris 20–22 mencetak garis pembatas dan judul program agar tampilan lebih rapi. Baris 23–24 mencetak header tabel berupa kolom nomor dan plat nomor. Baris 25–26 melakukan perulangan untuk menampilkan setiap entri log beserta indeksnya. Baris 27 menampilkan total keseluruhan log kendaraan dan baris 28 mencetak garis penutup tabel. Bagian ini berfungsi untuk memberikan gambaran data kepada pengguna sebelum melakukan pencarian.
<img width="1422" height="224" alt="code3 4" src="https://github.com/user-attachments/assets/59d0c7fc-c876-47e8-9eea-498b9aeffb47" />
Pada baris 30–34, program menerima input plat nomor dari pengguna menggunakan perulangan while True untuk memastikan input tidak kosong. Baris 31 menerima input dari pengguna dan langsung mengonversinya menggunakan .upper().strip() agar input seperti b1234ab tetap terbaca sama dengan B1234AB sehingga pencarian tidak peka terhadap huruf besar atau kecil. Baris 32–33 melakukan pengecekan apakah input tidak kosong, jika valid maka perulangan dihentikan menggunakan break. Jika input kosong, baris 34 akan menampilkan pesan peringatan dan meminta input ulang. Bagian ini berfungsi untuk memastikan data yang dimasukkan pengguna valid sebelum diproses.
<img width="1422" height="506" alt="code3 5 BNR" src="https://github.com/user-attachments/assets/88630217-8188-40da-ad11-f4cd05b43b54" />
Pada baris 36, fungsi sequential_search dipanggil dengan memasukkan data log, jumlah elemen, dan plat nomor target sebagai argumen. Dua nilai kembalian dari fungsi tersebut ditampung sekaligus ke variabel counter dan last_index. Baris 38 mencetak baris kosong sebagai pemisah agar output lebih rapi. Baris 39 melakukan pengecekan apakah counter lebih dari 0. Jika iya, baris 40–41 mencetak plat nomor yang ditemukan beserta frekuensi kemunculan dan indeks terakhirnya. Baris 42 menangani kondisi sebaliknya menggunakan else, kemudian baris 43 mencetak pesan bahwa plat nomor tidak ditemukan dalam log. Bagian ini berfungsi sebagai output akhir yang menyampaikan hasil pencarian kepada pengguna secara informatif.
Pada baris 46–47, terdapat blok kondisi if name == "main" yang digunakan untuk memastikan fungsi main() hanya dipanggil dan dijalankan ketika file ini dieksekusi secara langsung. Jika file ini diimpor oleh program lain, maka fungsi main() tidak akan otomatis berjalan. Bagian ini berfungsi sebagai titik masuk utama program sesuai dengan praktik penulisan kode Python yang baik dan benar.

## 0utput Program
<img width="317" height="339" alt="Screenshot 2026-05-12 181151" src="https://github.com/user-attachments/assets/264af056-0e2e-42d3-9f3e-c83e53200fba" />

Program dimulai dengan menampilkan seluruh isi log kendaraan dalam bentuk tabel yang berisi nomor indeks dan plat nomor kendaraan yang tercatat masuk ke area parkir. Setelah tabel ditampilkan beserta total log kendaraan, program meminta pengguna untuk memasukkan plat nomor yang ingin dicari.
Jika pengguna langsung menekan enter tanpa mengisi plat nomor, program akan menampilkan pesan "Input tidak boleh kosong!" kemudian meminta input kembali hingga pengguna memasukkan data yang valid.
Selanjutnya, pengguna memasukkan plat nomor yang ingin dicari, misalnya B1234AB. Program kemudian menelusuri seluruh data log dari indeks 0 hingga indeks terakhir secara berurutan. Setiap kali plat nomor tersebut ditemukan, counter bertambah dan last_index diperbarui. 

<img width="323" height="305" alt="Screenshot 2026-05-12 181206" src="https://github.com/user-attachments/assets/dc92e807-b658-4698-b96d-5dcf963aad46" />

Jika pengguna memasukkan plat nomor dalam huruf kecil, misalnya d567cd, program tetap dapat menemukannya karena input otomatis dikonversi ke huruf kapital menggunakan .upper() sebelum proses pencarian dilakukan.

<img width="334" height="287" alt="Screenshot 2026-05-12 181220" src="https://github.com/user-attachments/assets/53e1591b-f616-42b8-9257-a23612ac544b" />

Jika pengguna memasukkan plat nomor yang tidak terdapat dalam log, misalnya Z9999AA, maka program akan menelusuri seluruh data hingga habis tanpa menemukan kecocokan.
Program kemudian berhenti setelah hasil ditampilkan karena tidak menggunakan perulangan menu, sesuai dengan struktur kode dari modul yang langsung menampilkan hasil pencarian tanpa opsi pencarian ulang.


## Link YouTube
[https://youtu.be/-X0-q3PK8oc?si=sLpVaz88Dxee_iaG]

## Tugas Akhir Tulis Tangan
<img width="750" height="1046" alt="WhatsApp Image 2026-05-12 at 20 47 33" src="https://github.com/user-attachments/assets/377960f8-b778-402a-b221-ffec3f2b5678" />


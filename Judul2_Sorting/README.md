# Sistem Ranking Nilai Mahasiswa Menggunakan Algoritma Insertion Sort

## Deskripsi Singkat
Program ini merupakan simulasi sistem penilaian dan perankingan mahasiswa sederhana. Pengguna dapat memasukkan data berupa nama dan nilai mahasiswa, kemudian melihat daftar ranking yang sudah terurut dari nilai tertinggi ke terendah, serta mengetahui huruf mutu berdasarkan nilai yang diperoleh. Program ini mengimplementasikan algoritma Insertion Sort karena setiap kali data baru ditambahkan, sistem langsung melakukan proses pengurutan sehingga data selalu dalam kondisi terurut tanpa perlu menunggu semua input selesai. Pendekatan ini membuat proses penentuan ranking menjadi lebih efisien dan langsung dapat ditampilkan kapan saja. Selain itu, fungsi konversi nilai ke huruf mutu digunakan untuk mempermudah interpretasi hasil penilaian agar lebih mudah dipahami.

## Source Code
<img width="1155" height="356" alt="ta 2 1" src="https://github.com/user-attachments/assets/f52a19c6-a54d-4f47-a481-cf031970acb5" />
Pada baris 1–8, dibuat fungsi insertion_sort yang digunakan untuk mengurutkan data mahasiswa berdasarkan nilai dari tertinggi ke terendah. Baris 2 melakukan perulangan mulai dari indeks ke-1 karena data pertama dianggap sudah terurut. Baris 3 menyimpan data sementara ke variabel temp, lalu baris 4 membuat variabel j untuk menunjuk ke data sebelumnya.
Pada baris 5 dilakukan pengecekan menggunakan while untuk membandingkan nilai sebelumnya dengan nilai pada temp. Jika nilai sebelumnya lebih kecil, maka pada baris 6 data akan digeser ke kanan. Baris 7 mengurangi indeks agar pengecekan bisa lanjut ke kiri. Setelah posisi yang tepat ditemukan, pada baris 8 data dari temp dimasukkan ke posisi tersebut. Bagian ini berfungsi untuk memastikan data selalu terurut setiap kali ada perubahan.

<img width="1155" height="605" alt="ta 2 2" src="https://github.com/user-attachments/assets/b5d190bc-6d68-49ea-81cc-58cce70ed086" />
Pada baris 11–24, dibuat fungsi get_mutu yang digunakan untuk mengubah nilai angka menjadi huruf mutu. Setiap kondisi if pada baris 12–23 digunakan untuk menentukan kategori nilai, misalnya nilai ≥ 76 mendapat "A". Pengecekan dilakukan dari atas ke bawah. Jika tidak memenuhi semua kondisi, maka pada baris 24 akan mengembalikan nilai "E". Fungsi ini berguna untuk menyederhanakan nilai dalam bentuk kategori.

<img width="1155" height="494" alt="ta 2 3" src="https://github.com/user-attachments/assets/d58c5dea-a36e-469e-bd64-cc19fb5b93d1" />
Pada baris 27–37, dibuat fungsi tampilkan_ranking yang berfungsi untuk menampilkan data mahasiswa. Baris 28–30 digunakan untuk mengecek apakah data kosong, jika kosong maka program menampilkan pesan lalu berhenti.
Jika data ada, pada baris 32–34 ditampilkan judul dan header tabel agar output rapi. Baris 35 melakukan perulangan menggunakan enumerate untuk menampilkan semua data sekaligus nomor urut. Pada baris 36–37, fungsi get_mutu dipanggil untuk mendapatkan huruf mutu, lalu data ditampilkan dalam format tabel. Fungsi ini digunakan untuk menampilkan hasil ranking secara terstruktur.

<img width="1155" height="718" alt="ta 2 4" src="https://github.com/user-attachments/assets/5d779ae9-db81-42db-8e0e-c625d3f84bfa" />
Pada baris 40–56, dibuat fungsi input_mahasiswa untuk menerima input dari pengguna. Baris 41–45 digunakan untuk meminta input nama dan memastikan tidak kosong. Jika kosong, user diminta mengisi ulang.
Baris 47–54 digunakan untuk input nilai dengan tipe float agar bisa menerima desimal. Di sini juga dilakukan validasi agar nilai berada di antara 0–100. Jika input salah, program akan meminta ulang. Pada baris 56, data dikembalikan dalam bentuk dictionary berisi nama dan nilai. Fungsi ini memastikan data yang masuk valid.

<img width="1155" height="262" alt="ta 2 5" src="https://github.com/user-attachments/assets/6fb94fc9-0242-4b9f-af57-0a409997db8d" />
Pada baris 59–63, dibuat fungsi menu yang digunakan untuk menampilkan pilihan menu kepada pengguna, yaitu tambah data, tampilkan ranking, dan keluar. Fungsi ini berfungsi sebagai tampilan awal interaksi user.

<img width="1155" height="887" alt="ta 2 6" src="https://github.com/user-attachments/assets/f7efb765-0ef6-432a-9800-8157743e165d" />
Pada baris 66–84, dibuat fungsi main sebagai pengatur jalannya program. Baris 67 membuat list kosong untuk menyimpan data mahasiswa. Baris 69 membuat perulangan agar program terus berjalan.
Baris 70 memanggil fungsi menu, lalu baris 71 menerima input pilihan user. Jika memilih 1 (baris 73–77), program akan mengambil input data, menyimpannya ke list, lalu langsung mengurutkan dengan insertion_sort.
Jika memilih 2 (baris 78–79), program menampilkan ranking. Jika memilih 3 (baris 80–82), program berhenti. Jika input tidak sesuai, maka pada baris 83–84 akan muncul pesan error. Fungsi ini berfungsi sebagai pengontrol utama alur program.
Pada baris 86–87, terdapat blok kondisi if __name__ == "__main__" yang digunakan sebagai entry point program. Baris 87 memanggil fungsi main() agar program dijalankan hanya ketika file dieksekusi secara langsung, bukan saat diimpor sebagai modul. Bagian ini berfungsi sebagai titik awal eksekusi program.

## Output Program
<img width="338" height="187" alt="Screenshot 2026-05-05 185311" src="https://github.com/user-attachments/assets/bd495d4f-bdd8-434e-a75c-6f632915e720" />
Program dimulai dengan menampilkan menu utama yang berisi pilihan Masukkan Data Mahasiswa, Tampilkan Ranking, dan Keluar. Setelah itu, user diminta untuk memasukkan pilihan sesuai kebutuhan. Jika user langsung memilih menu 2 (Tampilkan Ranking) saat belum ada data yang dimasukkan, maka program akan menampilkan pesan "Belum ada data." karena list masih kosong, kemudian menu akan ditampilkan kembali untuk menunggu input selanjutnya.

<img width="494" height="715" alt="Screenshot 2026-05-05 190249" src="https://github.com/user-attachments/assets/6672be30-5ec9-43e2-a3ab-46e50e81b2ad" />
Selanjutnya, user memilih menu 1 (Masukkan Data Mahasiswa) sebanyak tiga kali, kemudian program meminta input nama dan nilai mahasiswa. User menginput data secara berurutan, misalnya Andi dengan nilai 75, Budi dengan nilai 80, dan Cindi dengan nilai 60. Setiap kali data dimasukkan, program langsung mencetak konfirmasi seperti "Data 'Andi' berhasil ditambahkan", "Data 'Budi' berhasil ditambahkan", dan "Data 'Cindi' berhasil ditambahkan", lalu menu ditampilkan kembali untuk menunggu input berikutnya.

<img width="528" height="357" alt="Screenshot 2026-05-05 190305" src="https://github.com/user-attachments/assets/e237e191-6943-4dfc-8707-88ff4c745854" />
Saat user memilih menu 2 (Tampilkan Ranking), program akan menampilkan seluruh data mahasiswa dalam bentuk tabel. Data yang ditampilkan sudah dalam kondisi terurut dari nilai tertinggi ke terendah karena setiap penambahan data langsung diproses menggunakan algoritma insertion sort. Pada contoh tersebut, Budi akan berada di urutan pertama karena memiliki nilai tertinggi, diikuti oleh Andi, kemudian Cindi. Selain itu, setiap nilai juga ditampilkan dalam bentuk huruf mutu sesuai dengan kategorinya sehingga hasilnya lebih mudah dipahami.

<img width="612" height="613" alt="Screenshot 2026-05-05 190344" src="https://github.com/user-attachments/assets/9f739d33-278a-4d66-a9a5-29aac2ebb4b2" />
Jika user kembali menambahkan data baru melalui menu 1, misalnya Deni dengan nilai 90, maka program akan langsung menyisipkan data tersebut ke posisi yang sesuai dan memperbarui ranking. Saat menu 2 dipilih kembali, Deni akan berada di posisi pertama karena memiliki nilai tertinggi tanpa perlu dilakukan pengurutan ulang secara manual.

<img width="448" height="173" alt="Screenshot 2026-05-05 190402" src="https://github.com/user-attachments/assets/e24337b3-770d-41ca-9533-7917766a2c8a" />
Terakhir, saat pengguna memilih menu 3 (Keluar), program akan menampilkan pesan "Terima kasih. Selesai." kemudian program berhenti karena perintah break menghentikan perulangan pada fungsi utama.


## Link YouTube
[https://youtu.be/wCAY0wj7-6k?si=ctOjIObGQhETKE7E]

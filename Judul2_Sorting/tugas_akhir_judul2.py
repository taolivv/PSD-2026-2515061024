def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["nilai"] < temp["nilai"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def get_mutu(nilai):
    if nilai >= 76: 
        return "A"
    if nilai >= 71: 
        return "B+"
    if nilai >= 66: 
        return "B"
    if nilai >= 61: 
        return "C+"
    if nilai >= 56: 
        return "C"
    if nilai >= 50: 
        return "D"
    return "E"


def tampilkan_ranking(arr):
    if not arr:
        print("Belum ada data.")
        return

    print("\n========== RANKING MAHASISWA ==========")
    print(f"{'No':<4} {'Nama':<20} {'Nilai':<8} {'Mutu'}")
    print("-" * 39)
    for i, m in enumerate(arr, 1):
        mutu = get_mutu(m["nilai"])
        print(f"{i:<4} {m['nama']:<20} {m['nilai']:<8.1f} {mutu}")


def input_mahasiswa():
    while True:
        nama = input("Nama: ").strip()
        if nama:
            break
        print("Nama tidak boleh kosong!")

    while True:
        try:
            nilai = float(input("Nilai (0-100): "))
            if 0 <= nilai <= 100:
                break
        except ValueError:
            pass
        print("Input salah! Masukkan angka antara 0-100.")

    return {"nama": nama, "nilai": nilai}


def menu():
    print("\nSISTEM NILAI MAHASISWA")
    print("1. Masukkan Data Mahasiswa")
    print("2. Tampilkan Ranking")
    print("3. Keluar")


def main():
    data = []

    while True:
        menu()
        pilih = input("Pilih Menu (1-3): ").strip()

        if pilih == "1":
            m = input_mahasiswa()
            data.append(m)
            insertion_sort(data, len(data))
            print(f"Data '{m['nama']}' berhasil ditambahkan.")
        elif pilih == "2":
            tampilkan_ranking(data)
        elif pilih == "3":
            print("Terima kasih. Selesai.")
            break
        else:
            print("Pilihan tidak valid! Masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()
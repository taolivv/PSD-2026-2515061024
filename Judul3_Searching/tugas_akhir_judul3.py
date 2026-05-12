def sequential_search(data, n, target):
    i = 0
    counter = 0
    last_index = -1
    while i < n:
        if data[i] == target:
            counter += 1
            last_index = i
        i += 1
    return counter, last_index

def main():
    data = [
        "B1234AB", "D5678CD", "B1234AB", "F9999XY",
        "D5678CD", "B1234AB", "H1111ZZ", "F9999XY",
        "B1234AB", "H1111ZZ"
    ]
    n = len(data)

    print("=" * 45)
    print("     SISTEM PENCARIAN PLAT NOMOR PARKIR")
    print("=" * 45)
    print(f"{'No':<6} {'Plat Nomor'}")
    print("-" * 45)
    for i in range(n):
        print(f"{i:<6} {data[i]}")
    print(f"\nTotal log kendaraan: {n}")
    print("=" * 45)

    while True:
        target = input("\nMasukkan plat nomor yang ingin dicari: ").upper().strip()
        if target:
            break
        print("Input tidak boleh kosong!")

    counter, last_index = sequential_search(data, n, target)

    print()
    if counter > 0:
        print(f"Plat {target} ditemukan sebanyak {counter} kali,")
        print(f"terakhir terlihat pada indeks ke-{last_index}.")
    else:
        print(f"Plat {target} tidak ditemukan dalam log parkir.")


if __name__ == "__main__":
    main()
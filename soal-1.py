

print("Selamat Datang!")
print("===============")
while True:
    print("---menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        kontak = {}
        for x in kontak:
            print("======================")
            print(f"Nama: {kontak['nama']}")
            print(f"Telepon: {kontak['telepon']}")
            print(kontak)
    elif menu == "2":
        nama = input("Masukkan nama: ")
        telepon = input("Masukkan telepon: ")
        kontak = {
        "nama" == nama,
        "telepon" == telepon
        }        
        print(kontak)
        print("Kontak berhasil ditambahkan")
    elif menu == "3":
        print("program selesai, sampai jumpa!")
        break
    else:
        print("menu tidak tersedia")
        break
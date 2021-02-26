print("Selamat Datang!")
print("===============")

while True:
    print("---menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        dict = {}
        kontak = ['nama'== 'nama', 'telepon' == 'telepon']
        kontak.append(print(kontak))

        
    elif menu == "2":
        nama = input("Masukkan nama: ")
        telepon = input("Masukkan telepon: ")
        kontak = {
        "nama" : nama,
        "telepon" : telepon
        }        
        for x in kontak:
            print(kontak[x])
        print("Kontak berhasil ditambahkan")
        
    elif menu == "3":
        print("program selesai, sampai jumpa!") 
        break

    else:
        print("menu tidak tersedia")
        break
import modul as data

print("Selamat datang di program manajemen stock barang!")
print("Pilihan :")
print("1. Tambah data barang")
print("2. Edit data")
print("3. Hapus data barang")
print("4. Cari data")
print("5. Tampilkan data barang")
print("6. Tampilkan jumlah data")
print("7. Keluar")
print('\n')

while True:
    pilihan = int(input("Masukkan pilihan : "))
    print("____________________________________")
    print("____________________________________")
    if pilihan == 1:
        print(data.tambah())
        print("")
    elif pilihan == 2:
        print(data.edit())
        print("")
    elif pilihan == 3:
        print(data.hapus())
        print("")
    elif pilihan == 4:
        print(data.cari())
    elif pilihan == 5:
        print(data.index())
    elif pilihan == 6:
        print(data.total())
        print("")
    elif pilihan == 7:
        exit()
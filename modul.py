stok = []
def tambah():
    nama_barang = input("Masukkan nama barang : ").title()
    stok_barang = input("Masukkan stok barang : ")
    barang = {"Nama" : nama_barang, "Stok" : stok_barang}
    stok.append(barang)
    return "--- Data berhasil ditambahkan ---"

def edit():
    input_data = int(input("Hapus data ke : "))
    input_data -= 1
    input_nama = input("Masukkan nama : ").title()
    input_stok = int(input("Masukkan stok : "))
    data_change = {"Nama" : input_nama, "Stok" : input_stok}
    stok[input_data] = data_change
    return "--- Data berhasil diperbarui ---"

def hapus():
    input_data = int(input("Hapus data ke : "))
    input_data -= 1
    del stok[input_data]
    return "--- Data berhasil dihapus ---"

def cari():
    input_data = input("Cari nama barang : ").title()
    number = 1
    for i in stok:
        if input_data in i['Nama']:
            print(f"{number}. {i["Nama"]} | Stok : {i["Stok"]}")
            number += 1
        else:
            print("--- Data tidak ditemukan ---")
            break
    return ""

def index():
    print("--- Data barang ---")
    number = 1
    for i in stok:
        print(f"{number}. {i["Nama"]} | Stok : {i["Stok"]}")
        number += 1
    return ""

def total():
    data = f"Jumlah data tersimpan : {len(stok)}"
    return data

Totalbelanja = []

def daftarmenu():
    print("-----TOKO BUKU-----")
    print(" No | NAMA BARANG | Harga")
    print("-------------------------------")
    print(" 1  | BUKU TULIS      | 3000")
    print(" 2  | PULPEN  | 2000")
    print(" 3  | PENGHAPUS | 1000")
    print(" 4  | TIPE-X | 6000")
    menu = int(input("Masukkan angka barang  : "))
    if menu == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 3000 * jumlah1
        Totalbelanja.append(total1)
        tanya()
    elif menu == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 2000 * jumlah2
        Totalbelanja.append(total2)
        tanya()
    elif menu == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 1000 * jumlah3 
        Totalbelanja.append(total3)
        tanya()
    elif menu == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 1000 * jumlah4
        Totalbelanja.append(total4)
        tanya()
    else :
        print("barang tidak ada")
    return

def tanya():
    print("-------------------------------")
    tanya = input("Ingin tambah belanjaan? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftarmenu()
    elif tanya == "t":
        penutup()

def penutup() :
    for Total in(Totalbelanja):
        print(f"total:", sum(Totalbelanja))
        Total = sum(Totalbelanja)
        print("----------terima kasih sudah ----------------")
daftarmenu()
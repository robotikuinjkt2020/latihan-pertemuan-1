c = 1
while c == 1:
    print("aplikas penjumlahan dua angka")
    try:
        a = float(input("masukan angka pertama: "))
    except ValueError:
        print("input salah, masukan angka pertama : ")
        a = float(input(
            "masukan angka pertama jika anda kembali salah menginput maka anda akan keluar: "))
    else:
        try:
            b = float(input("masukan angka kedua: "))
        except ValueError:
            print("input salah, masukan angka pertama : ")
            b = float(input(
                "masukan angka pertama jika anda kembali salah menginput maka anda akan keluar "))
        else:
            sum = a + b
            print(a, "+", b, "hasilnya", sum)
            c = float(input("masukan angka 1 jika ingin menghtung kembali :"))
else:
    print("Terimakasih")

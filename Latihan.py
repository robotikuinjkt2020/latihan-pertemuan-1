# latihan-pertemuan-1
Repository utk latihan pertemuan 1

def Tambah(x, y):
   return x + y


def Kurang(x, y):
   return x - y

def Kali(x, y):
   return x * y

def Bagi(x, y):
   return x / y
  

print("Pilih Jenis Operasi")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")


choice = input("Masukkan Pilihan(1/2/3/4): ")

num1 = int(input("Masukkan Angka Pertama: "))
num2 = int(input("Masukkan Angka Kedua: "))

if choice == '1':
   print(num1,"+",num2,"=", Tambah(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", Kurang(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", Kali(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", Bagi(num1,num2))
else:
   print("Invalid input")




	

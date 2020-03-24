'ELANG ANJI KALIANGAN'
'11170910000044'
'PROGRAM KALKULATOR'

#Penjumlahan
def add(x, y):
   return x + y
#Pengurangan
def subtract(x, y):
   return x - y
#Perkalian
def multiply(x, y):
   return x * y
#Pembagian
def divide(x, y):
   return x / y

print("Operasi Bilangan :")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

choice = input("Masukkan pilihan(1/2/3/4): ")
bil1 = int(input("Bilangan pertama = "))
bil2 = int(input("Bilangan kedua = "))
if choice == '1':
   print(bil1,"+",bil2,"=", add(bil1,bil2))
elif choice == '2':
   print(bil1,"-",bil2,"=", subtract(bil1,bil2))
elif choice == '3':
   print(bil1,"*",bil2,"=", multiply(bil1,bil2))
elif choice == '4':
   print(bil1,"/",bil2,"=", divide(bil1,bil2))
else:
   print("Pilihan anda salah")
   

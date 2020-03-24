print ("Latihan 1 Kalkulator\n\n")

def jumlah(x,y): 
	return x + y

def kurang(x,y):
	return x - y

def kali(x,y):
	return x * y

def bagi(x,y):
	return x / y

print ("Berikut pilihan fungsi :")
print ("1. Penjumlahan")
print ("2. pengurangan")
print ("3. perkalian")
print ("4. pembagian")

pilihan = input ("pilih fungsi 1, 2, 3, atau 4 : ")

angka1 = int (input("Angka Pertama : "))
angka2 = int (input("Angka kedua : "))

if pilihan == '1':
	print (angka1, "+", angka2, "=", jumlah(angka1, angka2))

elif pilihan =='2' :
	print (angka1,"-", angka2, "=", kurang(angka1,angka2))

elif pilihan == '3' : 
	print (angka1,"*", angka2, "=", kali(angka1,angka2))

elif pilihan == '4' : 
	print (angka1,"/", angka2, "=", bagi(angka1,angka2))

else :
	print("maaf tidak terdaftar")


print ("Latihan 1 Kalkulator\n\n")

def add(x,y) : 
	return x + y

def subtract (x, y) :
	return x - y
def multiply (x, y) :
	return x * y
def divide (x,y) :
	return x / y

print ("1. Penjumlahan")
print ("2. pengurangan")
print ("3. perkalian")
print ("4. pembagian")

choice = input ("pilih fungsi 1 - 4 : ")

num1 = int (input("Angka Pertama : "))
num2 = int (input("Angka kedua : "))

if choice == '1':
	print (num1, "+", num2, "=", add (num1,num2))

elif choice =='2' :
	print (num1,"-", num2, "=", add (num1,num2))

elif choice == '2' : 
	print (num1,"*", num2, "=", add (num1,num2))

elif choice == '2' : 
	print (num1,"/", num2, "=", add (num1,num2))

else :
	print("maaf tidak terdaftar")


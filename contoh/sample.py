#!/usr/bin/env python
# encoding: utf-8

#kalkulator sederhana
# penjumlahan
def add(x, y):
   return x + y
# pengurangan
def subtract(x, y):
   return x - y
# perkalian
def multiply(x, y):
   return x * y
# pembagian
def divide(x, y):
   return x / y
# operasi
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# Meminta input dari user
choice = input("Silahkan Pilih Menu(1/2/3/4): ")
num1 = int(input("Input bilangan pertama: "))
num2 = int(input("Input bilangan kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Input salah")

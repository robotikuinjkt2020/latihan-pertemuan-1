from pip._vendor.distlib.compat import raw_input

def penjumlahan(a, b):
    penjumlahan = float(a) + float(b)
    return penjumlahan

def pengurangan(a, b):
    pengurangan =float (a) -float (b)
    return pengurangan


def perkalian(a, b):
    perkalian = float(a) * float(b)
    return perkalian


def pembagian(a, b):
    pembagian = float(a) / float(b)
    return pembagian


lagi = 'ya'
while lagi == 'ya':
    print(' \t \t Program Kalkulator Yuhuuu')
    a = input('Masukan Bilangan 1: ')
    b = input('Masukan Bilangan 2 : ')
    print(' 1. penjumlahan \n 2. pengurangan \n 3. perkalian \n 4. pembagian \n')
    c = input('Pilih 1-4 : ')
    if c == '1':
        print(' Hasilnya adalah = ', penjumlahan(a, b))
    elif c == '2':
        print(' Hasilnya adalah = ', pengurangan(a, b))
    elif c == '3':
        print(' Hasilnya adalah = ', perkalian(a, b))
    else :
        print(' Hasilnya adalah = ', pembagian(a, b))

    lagi = raw_input(" Mau Lagi ? [ya/tidak] : ")
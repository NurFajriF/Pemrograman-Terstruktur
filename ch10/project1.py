'''1.	Buatlah program Python untuk membaca sebuah file text berisi 
beberapa data bilangan yang tersusun secara vertikal. Output dari 
program adalah menampilkan banyaknya bilangan genap dan ganjil dari 
data bilangan tersebut. Sebagai contoh misalnya isi file text adalah 
sederetan data berikut:
'''
file = open('d:/ch10pythontext/ch10project1.txt','r')
bil = file.readlines()
a = 0
b = 0
for i in range(len(bil)):
    if (int(bil[i]) % 2 == 0):
        a += 1
    else:
        b += 1
print('Banyaknya bilangan genap : ',a)
print('Banyaknya bilangan ganjil : ',b)
file.close()

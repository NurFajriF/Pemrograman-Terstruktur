'''2.	Buatlah program Python untuk menyimpan data peminjaman buku suatu 
perpustakaan. Data yang disimpan adalah: kode member, nama member, judul buku, 
tanggal pinjam (mengambil tanggal sekarang), dan tanggal maks pengembalian 
(7 hari setelah tanggal pinjam). Data peminjaman tersimpan di dalam sebuah 
file teks. Berikut ini adalah tampilan program yang diharapkan:
'''
from datetime import*
file = open('d:/ch11pythontext/project2.txt','a')
print('-'*33)
print('='*5,'Perpustakaan Sukasuka','='*5)
print('-'*33)
skrng = datetime.date(datetime.now())
print('Sekarang tanggal : ', skrng,'\n')
maks = skrng + timedelta(days=7)
print(maks)
while True:
    kode = str(input('Masukkan Kode Member      : '))
    nama = str(input('Masukkan Nama Member      : '))
    judul = str(input('Masukkan Judul Buku       : '))
    data = str(kode + '|' + nama +'|' + judul + '|' + str(skrng) + '|' + str(maks))
    print('\n'+data)
    file.write(data + '\n')
    lagi = str(input('\nUlangi input lagi(y/n)? : '))
    if(lagi == 'y' or lagi == 'Y'):
        True
    elif(lagi == 'n' or lagi == 'N'):
        break
    else:
        print('Input data salah')

file.close()

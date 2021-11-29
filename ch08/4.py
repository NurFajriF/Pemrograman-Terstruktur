'''4.	Diketahui data sayur sebagai berikut: 
bayam, kangkung, wortel, selada. 
Buatlah program untuk menambah dan menghapus data sayur tersebut. 
Untuk proses menambah dan menghapus data dilakukan melalui sebuah 
menu pilihan. Contoh tampilan menu:
Menu:
A.	Tambah data sayur
B.	Hapus data sayur
C.	Tampilkan data sayur
Pilihan Anda: ...
Untuk proses menghapus data sayur, user diminta mengetikkan nama sayur 
yang akan dihapus. Jika nama sayur yang mau dihapus tidak ada, maka 
munculkan pesan peringatan bahwa data tidak ditemukan.
Sedangkan jika tampilkan data sayur pada menu dipilih, maka program 
menampilkan data terakhir semua sayur yang ada. 
'''

sayur = ['bayam','kangkung','wortel','selada']
print('Sayur : ', sayur)
while True:
    print('Menu : ')
    print('A.	Tambah data sayur')
    print('B.	Hapus data sayur')
    print('C.	Tampilkan data sayur')
    print('D.	Keluar')
    pilih = str(input('\nPilih menu : \n'))
    if(pilih == 'A' or pilih == 'a'):
        while True:
            tambahsayur = str(input('Sayur yang ditambahkan : '))
            sayur.append(tambahsayur)
            lagi = str(input('lagi(y/n)? : '))
            if(lagi == 'y' or lagi == 'Y'):
                True
            elif(lagi == 'n' or lagi == 'N'):
                break
            else:
                print('Input menu salah')

    elif(pilih == 'B' or pilih == 'b'):
        while True:
            try:
                hapussayur = str(input('Sayur yang ingin dihapus : '))
                sayur.remove(hapussayur)
                lagi = str(input('lagi(y/n)? : '))
                if(lagi == 'y' or lagi == 'Y'):
                    True
                elif(lagi == 'n' or lagi == 'N'):
                    break
                else:
                    print('Input menu salah')
            except ValueError:
                print('Data tidak ditemukan')
    elif(pilih == 'C' or pilih == 'c'):
        print('Data sayur : ',sayur )
    elif(pilih == 'D' or pilih == 'd'):
        break
    else:
        print('Input menu salah')




'''2.	Buatlah program Python untuk membaca input berupa: nim, nama mhs, alamat.
Kemudian simpan data tersebut ke dalam file text, dengan format: nim|nama|alamat
'''
print('-----------------------------')
print('PROGRAM INPUT DATA MAHASISWA ')
print('-----------------------------')

file = open('d:/ch10pythontext/ch10project2.txt','a')
while True:
    nim = str(input('Masukkan NIM      : '))
    nama = str(input('Masukkan Nama Mhs : '))
    alamat = str(input('Masukkan Alamat   : '))
    data = str(nim + '|' + nama +'|' + alamat)
    file.write(data + '\n')
    lagi = str(input('\nUlangi input lagi(y/n)? : '))
    if(lagi == 'y' or lagi == 'Y'):
        True
    elif(lagi == 'n' or lagi == 'N'):
        break
    else:
        print('Input data salah')
file.close()




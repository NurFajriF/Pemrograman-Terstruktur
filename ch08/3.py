'''3.	Buatlah program Python yang menerima input berupa 
nama mahasiswa (string) sebanyak n data. Selanjutnya program menampilkan 
semua nama mahasiswa yang tersusun secara urut (ascending) serta 
banyaknya karakter yang menyusun setiap nama mahasiswa tersebut sebagai 
output. Contoh tampilan:
Amalia (6 karakter)
Budiman (7 karakter)
Cici (4 karakter)
Dedi Dukun (10 karakter)
'''
def listnama():
    while True:
        nama = str(input('Masukkan nama mahasiswa : '))
        data.append(nama)
        lagi = str(input('lagi(y/n)? : '))
        if(lagi == 'y' or lagi == 'Y'):
            True
        elif(lagi == 'n' or lagi == 'N'):
            break
        else:
            print('Input data salah')
    data.sort()
    for i in range(len(data)):
        nama = print(data[i])
        jmlkarakter = len(data[i])
        i += 1
    print(nama ,'(',jmlkarakter,'karakter',')')

data = []
listnama()

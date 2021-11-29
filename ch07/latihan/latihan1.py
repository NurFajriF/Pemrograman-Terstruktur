#Buatlah program Python untuk membuka, membaca, dan kemudian menampilkan 
# isi sebuah file text. Input dari program Python ini adalah nama file text 
# yang akan dibaca.
#Keterangan:
#Pastikan tidak ada exception yang muncul ketika file yang akan 
# dibaca tidak ada/salah penulisan

pilihfile  = input('Masukkan nama file: ') 
try:
    file = open(pilihfile , "r")
    print('Isi file ',pilihfile,' adalah: ')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')


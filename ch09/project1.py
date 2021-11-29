'''1. Buatlah sebuah function ubahHuruf(teks, a, b) yang nantinya 
digunakan untuk mengubah huruf pada parameter a dengan huruf yang ada 
di b dari suatu string teks. Contohnya adalah:
ubahHuruf('MATEMATIKA', 'T', 'S') maka function tersebut akan menghasilkan 
string MASEMASIKA, dalam hal ini setiap huruf T dalam string MATEMATIKA 
diubah menjadi S.
Petunjuk:
-	Terlebih dahulu ubah string ke dalam list
-	Lakukan pengubahan huruf menggunakan looping
-	Gunakan join() untuk menggabung setiap elemen dari list menjadi string
Alternatif cara lain yang lebih sederhana bisa menggunakan replace()
'''

teks = str(input("Masukkan kata : "))
a = str(input('Huruf yang ingin diubah : '))
b = str(input('Diubah menjadi huruf : '))
def ubahhuruf(teks,a,b):
    teksbaru = teks.replace(str(a),str(b))
    print(teksbaru)

    
ubahhuruf(teks,a,b)

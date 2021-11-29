#1.Buatlah list a = [1, 5, 6, 3, 6, 9, 11, 20, 12] dan 
# b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print('\n=======================================\n')
#2.	Sisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)

print('\n=======================================\n')
#3.	Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b
a.append(4)
b.append(8)
print(a)
print(b)

print('\n=======================================\n')
#4.	Kemudian lakukan sorting secara ascending pada list a dan b
a.sort()
b.sort()
print(a)
print(b)

print('\n=======================================\n')
#5.	Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)
c = [0,1,2,3,4,5,6,7]
a.append(c)
d = [2,3,4,5,6,7,8,9]
b.append(d)
print(a)
print(b)

print('\n=======================================\n')
#6.	Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.
#e = [c0+d0, c1+d1, c2+d2, ...]
#Petunjuk: gunakan looping for
e = [c[0]+d[0],c[1]+d[1],c[2]+d[2],c[3]+d[3],c[4]+d[4],c[5]+d[5],c[6]+d[6],c[7]+d[7]]
print(e)
    
print('\n=======================================\n')
#7.	Ubahlah list e ke dalam tuple
tuple_e = tuple(e)
print(e)

print('\n=======================================\n')
#8.	Carilah nilai min, maks, dan jumlahan seluruh elemen dari e
print('Nilai minimal dalam e : ', min(e))
print('Nilai minimal dalam e : ', max(e))
jumlah = sum(e)
print('Jumlah seluruh nilai dalam e : ', jumlah)

print('\n=======================================\n')
#9.	Buatlah sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)
print('\n=======================================\n')

#10.	Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut
myset = set(myString)
print(myset)

print('\n=======================================\n')
#11.	Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list. 
mylist = list(myset)
mylist.sort()
print(mylist)

'''4.	Buatlah sebuah function shuffleString(x, n). Function ini akan 
menghasilkan sebuah list string sebanyak n elemen berbeda yang merupakan 
hasil pengacakan setiap karakter yang menyusun string x. Contoh:
randomString(‘aku’, 2) -> [‘aku’, ‘kua’]
randomString(‘aku’, 3) -> [‘auk’, ‘kau’, ‘uak’]
randomString(‘aku’, 3) -> [‘kua’, ‘auk’, ‘aku’, ‘uka’]

Petunjuk:
-	Gunakan function random.sample() dan join() untuk menghasilkan string acak.  
-	Hasil dari pengacakan string, masukkan ke dalam list. Pastikan tidak ada 
string hasil pengacakan yang duplikat di dalam list.
'''

x = str(input('Masukkan kata : '))
n = int(input('Jumlah kata acak : '))
def shuffleString(x,n):
    import random
    for i in range(n):
        l = list(x)
        random.shuffle(l)
        i += 1
        result = ''.join(l)
        listacak.append(result)
    print('randomString(', x ,',',n,') -> ',listacak)

listacak = []
shuffleString(x,n)

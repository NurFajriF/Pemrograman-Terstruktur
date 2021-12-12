'''6.	Buatlah sebuah program Python untuk melakukan enkripsi menggunakan 
sandi Caesar. Sandi Caesar adalah teknik penyandian pesan dengan cara 
menggeser setiap hurufnya sejauh n langkah tertentu, dalam hal ini n disebut 
juga keyword. Contohnya:
'''
print('='*33)
print('='*2 + 'Program Enkripsi Sandi Caesar' + '='*2)
print('='*33)
kalimat = input('\nMasukkan kalimat yg ingin dienkripsi : ')
n = int(input('Masukkan selisih geser karakter : '))
kalimat2 = list(kalimat)
print('Teks sandi : ')
for i in range(len(kalimat2)):
    bil = ord(kalimat2[i])
    bil += n
    kalimat3 = chr(bil)
    print(kalimat3,end='')




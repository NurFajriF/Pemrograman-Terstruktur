'''1.	Buatlah program Python yang dapat digunakan untuk mengubah 
kembali suatu file teks berisi teks hasil penyandian menggunakan Sandi Caesar 
menjadi file teks aslinya. Input program adalah file teks berisi teks hasil 
penyandian, dan nilai n. Outputnya adalah file teks berisi file teks asli 
yang bisa dipahami isinya.'''

print('='*34)
print('='*2 + 'Program Translasi Sandi Caesar' + '='*2)
print('='*34)
sandi = input('\nMasukkan sandi yg ingin ditranslasi : ')
n = int(input('Masukkan selisih geser karakter : '))
sandi2 = list(sandi)
print('Hasil translasi : ')
for i in range(len(sandi2)):
    bil = ord(sandi2[i])
    bil -= n
    arti = chr(bil)
    print(arti,end='')


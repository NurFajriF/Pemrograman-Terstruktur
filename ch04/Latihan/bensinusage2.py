print("     Penggunaan Bensin     ")
# 1 liter dapat menempuh 12 km
# jarak yg ditempuh 795 km
Jarak = float(input('Jarak : '))
bensin = float(Jarak / 12)
print("Bensin yang dibutuhkan : " , bensin , " liter ")
#kapasitas tangki bensin 50 liter
pengisian_ulang = int(bensin / 50)
print("Minimal pengisian ulang : " , pengisian_ulang , "kali")
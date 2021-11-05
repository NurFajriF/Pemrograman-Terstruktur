#Modifikasilah kode program nomor 5, sehingga bisa menampilkan score pemain. Berikut ini aturan perhitungan scorenya:
#Mula-mula score pemain adalah 100 poin
#Setiap kali tebakan pemain salah, maka skornya berkurang 2 poin
#Score minimal pemain adalah 0 (score negatif tidak diperbolehkan)

print("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
from random import randint
bil = randint(0,100)
skor = 100
while True:
    tebakan = int(input("Tebakan anda : "))
    if(tebakan < bil):
        print("Hehehe...Bilangan tebakan anda terlalu kecil")
        skor -= 2
    elif(tebakan > bil):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
        skor -= 2
    elif(tebakan == bil):
        print("Yatta..Tebakan anda BENAR :)")
        print("Skor anda : ", skor)
        lagi = str(input("Ingin mencoba lagi ? "))
        if(lagi == "ya"):
            continue
            bil = randint(0,100)
        elif(lagi == "tidak"):
            break
    if(skor == 0):
        print("Yaah..skor kamu udah habis")
        break

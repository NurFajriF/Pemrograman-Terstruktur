#Komputer akan memilih sebuah bilangan bulat secara random, antara 0 s/d 100.
#Bilangan tersebut tersimpan dalam memori komputer
#Tugas pemain adalah menebak bilangan yang dipilih komputer tersebut
#Untuk menebak bilangan, pemain mengentri beberapa bilangan
#Komputer memberikan respon ‘Bilangan tebakan Anda terlalu besar’ jika bilangan yang dientri pemain lebih besar dari bilangan yang dipilih komputer, atau ‘Bilangan tebakan Anda terlalu kecil’ jika bilangan yang dientri pemain lebih kecil dari bilangan yang dipilih komputer. 
print("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
from random import randint
bil = randint(0,100)
while True:
    tebakan = int(input("Tebakan anda : "))
    if(tebakan < bil):
        print("Hehehe...Bilangan tebakan anda terlalu kecil")
    elif(tebakan > bil):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
    elif(tebakan == bil):
        print("Yatta..Tebakan anda BENAR :)")
        lagi = str(input("Ingin mencoba lagi ? "))
        if(lagi == "ya"):
            continue
            bil = randint(0,100)
        elif(lagi == "tidak"):
            break


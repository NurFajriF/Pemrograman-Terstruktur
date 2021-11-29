#2.	Buatlah function dataStat(x) dengan sebuah parameter x 
# berupa list bilangan. Function tersebut menghasilkan 
# nilai balikan (return value) berupa list juga yang 
# berisi [a, b, c], di mana a adalah nilai rata-rata dari 
# list bilangan x, b adalah nilai tertinggi dari list x, dan c 
# adalah nilai terendah dari list x.
print('==============================')
print('Penghitung statistik list')
print('==============================')
import time
time.sleep(2)
print('Buat list anda terlebih dahulu')
time.sleep(2)
def buatlist():
    while True:
        try:
            bil = int(input('Masukkan bilangan bulat : '))
            x.append(bil)
            lagi = str(input('lagi(y/n)? : '))
            if(lagi == 'y' or lagi == 'Y'):
                True
            elif(lagi == 'n' or lagi == 'N'):
                break
            else:
                print('Input data salah')
        except ValueError:
            print('Bukan bilangan bulat')
    print('List anda : ', x)

def dataStat(x):
    sum = 0
    i = 0
    for data in x:
        sum += data
        i += 1
    a = sum / i
    Statx.append(a)
    b = max(x)
    Statx.append(b)
    c = min(x)
    Statx.append(c)
    print(Statx)
    return Statx

x = []
Statx = []
buatlist()
dataStat(x)

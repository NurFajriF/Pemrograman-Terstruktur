print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA ')
print('-----------------------------')
def inputdata():
    while True:
        try:
            bil = int(input('Masukkan bilangan bulat: '))
            lagi = input(str('Lagi (y/n)? : '))
            if(lagi == 'y'):
                data.append(bil)
            elif(lagi == 'n'):
                data.append(bil)
                break
        except ValueError:
            print('Bukan bilangan bulat')

def average():
    sum = 0
    for i in range(len(data)):
        sum = sum + data[i]
        i += 1
        rata2 = sum / len(data)
    print('Rata-ratanya adalah: ', rata2)

data = []
inputdata()
average()
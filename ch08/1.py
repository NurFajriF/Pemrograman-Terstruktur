def buatlist():
    while True:
        try:
            bil = int(input('Masukkan bilangan bulat : '))
            data.append(bil)
            lagi = str(input('lagi(y/n)? : '))
            if(lagi == 'y' or lagi == 'Y'):
                True
            elif(lagi == 'n' or lagi == 'N'):
                break
        except ValueError:
            print('Bukan bilangan bulat')
    data.sort(reverse = True)
    print(data)

data = []
buatlist()



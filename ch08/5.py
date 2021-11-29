'''
5.	Buatlah sebuah function dengan nama kuadrat(bil), dengan bil adalah 
parameternya dalam bentuk list berupa bilangan bulat. Fungsi dari function 
kuadrat() nantinya adalah menghasilkan sebuah list yang berisi nilai 
kuadrat dari masing-masing bilangan dalam bil. Contohnya:
bil = [2, 4, 5, 6]  
hasil = kuadrat(bil)
sehingga isi dari hasil berupa list dalam bentuk [4, 16, 25, 36]
'''
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
def kuadrat():
    i = 0
    for data in range(len(x)):
        kua = x[i] ** 2
        kuadra.append(kua)
        i += 1    
    print('Hasil kuadrat list anda : ' ,kuadra)

x = []
kuadra = []
buatlist()
kuadrat()


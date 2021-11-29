'''3.	Modifikasilah function yang ada dari hasil nomor 1, sehingga 
diperoleh tampilan formasi berikut ini
     *
    ***
   *****
  *******
   *****
    ***
     * 
Contoh tersebut adalah tampilan untuk n = 7. Dalam hal ini, nilai n harus 
berupa bilangan ganjil. 
'''
print('======== POLA BERLIAN ========')
#membuat function 
def diamond(n):
    for a1 in range(1, (n+1)//2 + 1):
        for a2 in range((n+1)//2 - a1):
            print(" ", end = "")
        for a3 in range((a1*2)-1):
            print("*", end = "")
        print()

    for a1 in range((n+1)//2 + 1, n + 1):
        for a2 in range(a1 - (n+1)//2):
            print(" ", end = "")
        for a3 in range((n+1 - a1)*2 - 1):
            print("*", end = "")
        print()
while True:
    try:
        n = int(input('Masukkan bilangan ganjil : '))
        if(n % 2 == 1):
            diamond(n)
            break
        elif(n % 2 == 0):
            print('Bukan bilangan ganjil')
    except ValueError:
        print('Input data salah')
        

    
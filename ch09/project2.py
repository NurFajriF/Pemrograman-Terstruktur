'''2.	Buatlah function bintang(n), dengan n adalah suatu bilangan 
bulat positif. Function bintang(n) nantinya akan mencetak formasi bintang 
sebanyak n baris dengan bentuk:

     *
    ***
   *****
  ******* 

Contoh tersebut adalah tampilan untuk n = 4.
Petunjuk: gunakan perintah center() untuk mengatur formasi bintangnya.
'''

def bintang(n):
    space = 2*n-1
    for i in range(n):
        print(('*' * (2*i+1)).center(space))
bintang(5)


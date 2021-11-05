'''Buatlah function faktorial(n) yang digunakan untuk menghitung 
nilai n faktorial. Output dari function ini adalah sebuah bilangan yang 
merupakan nilai dari n faktorial tersebut.'''
#Gunakan function tersebut untuk menghitung nilai dari:
#a.	C(5, 3)
#b.	P(10, 7)

def faktorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    print(f'{n}! = {faktorial}')

from math import fakctorial
def C(n,r):
    

#a. C(5,3)
a = 5
b = 3


#b. P(10,7)
a = 10
b = 7
faktorial(a)

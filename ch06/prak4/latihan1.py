#mengecek apakah a,b,dan c merupakan triple pythagoras atau bukan
#c merupakan sisi miring
def isPythagoras(a,b,c):
    pythagoras = bool(a ** 2 + b ** 2 == c ** 2)
    print(pythagoras)

#Ujilah beberapa pasangan sisi segitiga ini
#a.	a = 3, b = 4, c = 5	-> True
#b.	a = 5, b = 9, c = 12	-> False
#c.	a = 8, b = 6, c = 10	-> True
#d.	a = 7, b = 8, c = 11	-> False

isPythagoras(3,4,5)

isPythagoras(5,9,12)

isPythagoras(8,6,10)

isPythagoras(7,8,11)
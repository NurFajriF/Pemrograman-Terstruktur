#a. function sum(a,b,c,...) dengan parameter tdk terbatas
#b. function average(a,b,c,...) dengan parameter tdk terbatas
#c. function maks(a,b,c,...) dengan parameter tdk terbatas
#d. function min(a,b,c,...) dengan parameter tdk terbatas

#a.
def sum(*mydata):
    sum = 0
    i = 0
    for data in mydata:
        sum += data
        i += 1
    print('Jumlahnya = ', sum)

sum(2,3,4,5,6)

#b
def average(*mydata):
    sum = 0
    i = 0
    for data in mydata:
        sum += data
        i += 1
    rata2 = sum / i
    print('Rata-ratanya = ', rata2)

average(6,6,6,6,8,8,7)

#c
def maks(*mydata):
    max(*mydata)
    print('Data tertinggi = ', max(*mydata))

maks(5,6,7,8,9)

#d
def minim(*mydata):
    min(*mydata)
    print('Data terendah = ',min(*mydata))
minim(3,6,7,8,9)

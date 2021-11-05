from operation import *
a = 10
b = 7
print(a, '+', b, '=', jumlah(a,b))
print(a, '*', b, '=', kali(a,b))
print(a, '-', b, '=', kurang(a,b))
print(a, '/', b, '=', bagi(a,b))

#a.	2 + 4 * 6 – 4
a = 2
b = 4
c = 6
d = 4
print(a, "+", b, "*", c, "-", d, "=", kurang(jumlah(a,kali(b,c)),d))

#b.	(4 + 7) * (6 - 9)
a = 4
b = 7
c = 6
d = 9
print("(", a, "+", b, ")", "*", "(", c, "-", d, ") ", "=", kali(jumlah(a,b),kurang(c,d)))

#c.	(10 + 2) / (7 + 5) / (12 - 34) 
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print("(", a, "+", b, ")", "/", "(", c, "+", d, ")", "/", "(", e,"-",f ,")","=", jumlah(a,b) / jumlah(c,d) / kurang(e,f))

# -*- coding: utf-8 -*-

o,b,i = [float(x) for x in input().split()]
o = round(o,3)
b = round(b,3)
i = round(i,3)

if (o < b) and (o < i):
    print("Otavio")
elif (b < o) and (b < i):
    print("Bruno")
elif (i < o) and (i < b):
    print("Ian")
else:
    print("Empate")

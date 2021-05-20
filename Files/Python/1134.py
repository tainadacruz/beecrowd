# -*- coding: utf-8 -*-

t = 0
a = 0
g = 0
d = 0

while t != 4:
    t = int(input())
    if t == 1:
        a = a + 1
    elif t == 2:
        g = g + 1
    elif t == 3:
        d = d + 1
        
print("MUITO OBRIGADO")
print("Alcool: %d"%(a))
print("Gasolina: %d"%(g))
print("Diesel: %d"%(d))

# -*- coding: utf-8 -*-

n = int(input())
pares = []
impares = []

for i in range(n):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
        
pares.sort()
impares.sort()

for i in pares:
    print(i)
for i in reversed(impares):
    print(i)
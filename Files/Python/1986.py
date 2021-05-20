# -*- coding: utf-8 -*-

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto = list(alfabeto)

hexa = [None]*26
start = 61
p = 0

for i in range(len(hexa)):
    if i <= 8:
        hexa[i] = start
        start += 1
    elif i > 8 and i <= 14:
        hexa[i] = "6" + alfabeto[p].upper()
        p += 1
    elif i > 14 and i <= 24:
        hexa[i] = start
        start += 1
    elif i > 24:
        p = 0
        hexa[i] = "7" + alfabeto[p].upper()

for i in range(len(hexa)):
    hexa[i] = str(hexa[i])

n = int(input())
letra = [None]*n
valores = input().split()

for i in range(n):
    valores[i] = str(valores[i])
    
for i in range(len(valores)):
    for k in range(len(hexa)):
        if valores[i] == hexa[k]:
            letra[i] = alfabeto[k]

letra = "".join(letra)
print(letra)
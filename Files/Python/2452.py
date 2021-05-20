# -*- coding: utf-8 -*-
#URI 2452 - Semente

count = 0
f,r = [int(x) for x in input().split()]
fita = [0]*f
numeros = [int(r) for r in input().split()]

for i in range(len(numeros)):
    if numeros[i] > 0:
        fita[numeros[i]-1] = 1

while 0 in fita:
    for j in numeros:
        if fita[j-1] != 0:
            if fita[j-2] == 0:
                fita[j-2] = 1
            if j < len(fita):
                if fita[j] == 0:
                    fita[j] = 1
            else:
                if fita[j-1] == 0:
                    fita[j-1] = 1
 
    for j in range(len(fita)):
        if fita[j] == 1:
            numeros.append(fita.index(fita[j]))
            print(fita.index(fita[j]))
            print(numeros)
            
    count += 1
    
print(count)
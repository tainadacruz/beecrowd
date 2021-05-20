# -*- coding: utf-8 -*-
'''
def min(a,b,c,d):
    x = a
    if b < x:
        x = b
    if c < x:
        x = c
    if d < x:
        x = d
    return x
'''

while True:
    n = int(input())
    if n == 0:
        break
    
    matriz = [None]*n
    for i in range(0,n):
        matriz[i] = [None]*n
    
    count = 0
    auxColuna1 = 0
    for i in range(0,n):
        for j in range(0,n):
            if j == 0:
                matriz[i][j] = 2**(auxColuna1)
                print(matriz[i][j])
                auxColuna1 += 1
            else:
                matriz[i][j] = 2**(i+count)
            count += 1
        count = 0
            
    for i in range(n):
        print("%3d"% matriz[i][0], end="")
        for j in range(1,n):
            print(" %3d"% matriz[i][j], end="")
        print("")
    print("")
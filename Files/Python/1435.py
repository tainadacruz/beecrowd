# -*- coding: utf-8 -*-

def min(a,b,c,d):
    x = a
    if b < x:
        x = b
    if c < x:
        x = c
    if d < x:
        x = d
    return x

while True:
    n = int(input())
    if n == 0:
        break
    
    matriz = [None]*n
    for i in range(0,n):
        matriz[i] = [None]*n
        
    for i in range(0,n):
        for j in range(0,n):
            matriz[i][j] = min(i+1,j+1,n-i,n-j)
            
    for i in range(n):
        print("%3d"% matriz[i][j], end="")
        for j in range(1,n):
            print(" %3d"% matriz[i][j], end="")
        print("")
    print("")
    

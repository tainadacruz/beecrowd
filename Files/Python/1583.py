# -*- coding: utf-8 -*-

def contamina(t,linha,coluna,n,m):
    if t == "T":
        if linha != 0:
            matriz[i-1][j] = "T" 
        if linha < n-1
            matriz[i+1][j] = "T"
        if coluna != 0:
            matriz[i][j-1] = "T"
        if coluna < m-1:
            matriz[i][j+1] = "T"
    return matriz

while True:
    n,m = [int(x) for x in input().split()]
    global matriz = [None]*n
    
    if m == 0 or n == 0:
        break
    
    for i in range(n):
        matriz[i] = [None]*m
        for j in range(m):
            matriz[i][j] = str(input())
            
    
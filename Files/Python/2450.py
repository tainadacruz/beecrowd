# -*- coding: utf-8 -*-
#URI 2450 - Matriz Escada

n,m = [int(x) for x in input().split()]
esquerda = False
escada = False
count = 0

numeros = [None] * n
for i in range(n):
    numeros[i] = [int(m) for m in input().split()]
    
for i in range(n):
    for j in range(m):
        if i == 0:
            esquerda = True
            
        if esquerda:
            if numeros[i][j] != 0:
                for k in range(n-1):
                    if numeros[i+k][j] == 0 and:
                        count += 1
                if count == (n-1):
                    numeros[ik]
                        
             
            #pos = [(i,j)]
            
            
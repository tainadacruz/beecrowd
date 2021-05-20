# -*- coding: utf-8 -*-

n,m = [int(x) for x in input().split()]
count = 0
menosUm = 0

matriz = [None] * n
for i in range(0,n):
    matriz[i] = input().split()
    for j in range(0,m):
        matriz[i][j] = int(matriz[i][j])
        if matriz[i][j] == 0:
            count += 1
    if count > 0:
        menosUm +=1
    count = 0
    
print(n-menosUm)

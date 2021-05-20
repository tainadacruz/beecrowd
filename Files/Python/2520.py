# -*- coding: utf-8 -*-

a = 0
b = 0
c = 0
d = 0

while True:
    try:
        n,m = [int(x) for x in input().split()]

        matriz = [None] * n
        for i in range(0,n):
            matriz[i] = input().split()
            for j in range(0,m):
                matriz[i][j] = int(matriz[i][j])
                if matriz[i][j] == 1:
                    a = i
                    b = j
                elif matriz[i][j] == 2:
                    c = i
                    d = j
        
        distancia = abs(d-b) + abs(c-a)            
        print(distancia)        
    
    except EOFError:
        break
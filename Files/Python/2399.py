# -*- coding: utf-8 -*-

n = int(input())
bombas = [0]*(n)
    
for i in range(n):
    
    x = int(input())
    
    vizinhoEsquerdo = i-1
    vizinhoDireito = i+1
    
    bombas[i] += x
    if vizinhoEsquerdo >= 0:
        bombas[vizinhoEsquerdo] += x
    if vizinhoDireito <= n-1:
        bombas[vizinhoDireito] += x
        
for i in range(0,n):
    print(bombas[i])
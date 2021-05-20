# -*- coding: utf-8 -*-

n,m = [int(x) for x in input().split()]
maior = 0
somaLinha = 0
somaColuna = 0

matriz = [None] * n
for i in range(0,n):
    matriz[i] = input().split()
    for j in range(0,m):
        matriz[i][j] = int(matriz[i][j])
        somaLinha += matriz[i][j]
    if somaLinha > maior:
        maior = somaLinha
    somaLinha = 0

aux = 0
while aux != m:
    for i in range(0,n):
        somaColuna += matriz[i][aux]
        if somaColuna > maior:
            maior = somaColuna
    somaColuna = 0
    aux += 1
    
print(maior)
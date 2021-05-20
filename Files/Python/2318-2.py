# -*- coding: utf-8 -*-

entrada = [0] * 3
for i in range(3):
    entrada[i] = [int(x) for x in input().split()]
    for j in range(3):
        entrada[i][j] = int(entrada[i][j])

somaLinha = [0] * 3
somaColuna = [0] * 3

for i in range(3):
    for j in range(3):
        somaLinha[i] += entrada[i][j] 
        somaColuna[j] += entrada[i][j]


somasDiferentesLinha = {}
somasDiferentesColuna = {}

for i in range(3):
    if not somaLinha[i] in somasDiferentesLinha: 
        somasDiferentesLinha[somaLinha[i]] = [i] 
    else:
        somasDiferentesLinha[somaLinha[i]].append(i) 
        
    if not somaColuna[i] in somasDiferentesColuna: 
        somasDiferentesColuna[somaColuna[i]] = [i]
    else:
        somasDiferentesColuna[somaColuna[i]].append(i)

somaErrada = -1 
somaCorreta = -1 
linhaErrada = -1

for x in somasDiferentesLinha: 
    if len(somasDiferentesLinha[x]) == 1: 
        linhaErrada = somasDiferentesLinha[x][0] 
        somaErrada = x 
    else:
        somaCorreta = x 

colunaErrada = -1 
for x in somasDiferentesColuna: 
    if len(somasDiferentesColuna[x]) == 1: 
        colunaErrada = somasDiferentesColuna[x][0] 
        break
        
valorErrado = entrada[linhaErrada][colunaErrada] 
valorOriginal = valorErrado + somaCorreta - somaErrada 
print("%d %d" % (valorOriginal, valorErrado))
'''
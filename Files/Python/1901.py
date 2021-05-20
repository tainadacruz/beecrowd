# -*- coding: utf-8 -*-
#URI 1901 - Borboletas

n = int(input()) #entrada do tamanho da floresta
floresta = [] #inicialização do vetor floresta
borboletas = [] #inicialização do vetor borboletas

for i in range(n): #para cada linha da floresta
    borbo = [int(n) for n in input().split()] #recebe-se uma quantidade n borboletas
    floresta.append(borbo) #armazena tudo isso na floresta
    
for i in range(n*2): #para cada célula visitada por Bino
    a,b = [int(x) for x in input().split()] #armazena a posição da célula
        
    if floresta[a-1][b-1] not in borboletas: #verifica se a borboleta dessa célula já foi armazenada
        borboletas.append(floresta[a-1][b-1]) #se não foi, então armazena
        
print(len(borboletas)) #saída com a quantidade de espécies diferentes que foram armazenadas
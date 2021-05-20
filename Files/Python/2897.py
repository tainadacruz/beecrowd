# -*- coding: utf-8 -*-
#URI 2897 - Histórico de Comandos

while True:
    count = -1
    resultado = 0
    
    n = int(input())
    if n == 0:
        break
    
    numeroDuplicado = False
    posi = [None]*n #vetor que deveria armazenar a posição do número no vetor p
    duplicado = [None]*n #vetor que deveria armazenar os números anteriores aos duplicados
    historico = [None]*n #vetor que verifica se existem números repetidos
    
    p = [int(n) for n in input().split()]
    
    for i in range(len(p)):
        historico[i] = p[i]
    
    historico.sort()
    
    for i in range(1,len(historico)):
        if historico[i] == historico[i-1]:
            numeroDuplicado = True
        # -->
            posi[i-1] = p.index(historico[i-1])
            duplicado[i-1] = historico[i]
            print(posi)
            print(duplicado)
            print(p)
        # -->
        
    for i in range(0,n):
        count += 1
        # -->
        if numeroDuplicado and p[i] == (duplicado[posi[i]]):   
            #print(duplicado)
            countAlt = count - duplicado.index(duplicado[p[i]])
            resultado += countAlt
        # -->
        else:
            resultado += count + p[i]
        
    print(resultado)
        
    

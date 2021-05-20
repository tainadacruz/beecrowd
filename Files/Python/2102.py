# -*- coding: utf-8 -*-
#URI 2102 - Contando em Chinês
from operator import itemgetter #importação do operador que realizará o ordenamento da matriz

t = int(input()) #entrada com o número de instâncias

#para cada instância, faça
for o in range(0,t):
    # n = dimensão das matrizes | l = entradas não nulas
    n,l = [int(x) for x in input().split()] 
    
    #criação de uma matriz l+1x3
    #precisa-se de uma linha auxiliar, no final da matriz, para que não ocorra problemas na hora de printar os valores da linha l
    #um número grande (999) é inserido para que a linha l+1 não atrapalhe a ordenação da matriz
    matrix = [999] * (l+1)
    for i in range(l+1):
        matrix[i] = [999] * 3
    
    #para cada entrada não nula, faça
    for i in range(l): 
        # pk = matriz pk
        # vk = valor da matriz pk
        # lk = linha da matriz com o valor
        # ck = coluna da matriz com o valor
        pk,lk,ck,vk = [int(x) for x in input().split()]
        
        #inserindo os valores em uma matriz
        matrix[i][0] = lk
        matrix[i][1] = ck
        matrix[i][2] = vk
        
    #usamos o operador itemgetter para ordenar a matriz de acordo com:
    #primeiro, o valor das linhas (inseridos na linha 0 da matriz)
    #após isso, o valor das colunas (inseridos na linha 1 da matriz)
    matrix = sorted(matrix, key=itemgetter(0,1))
     
    #para cada linha da matriz, é verificado se os valores das linhas e colunas já foram inseridos anteriormente
    for i in range(l):
        if matrix[i][0] == matrix[i-1][0] and matrix[i][1] == matrix[i-1][1]:
            #se foram inseridos, é armazenado a soma de ambos
            soma = matrix[i][2]+matrix[i-1][2]
            print(matrix[i][0],matrix[i][1],soma)
        elif i != l:
            #se não, e se não for a linha l a ser verificada, e não existindo valores idênticos na linha seguinte
            if matrix[i][0] != matrix[i+1][0] and matrix[i][1] != matrix[i+1][1]:
                print(matrix[i][0],matrix[i][1],matrix[i][2]) #então printa a linha atual
        elif i == l:
            #se for a linha l a ser verificada, precisamos saber se ela é diferente da linha anterior
            if matrix[i][0] != matrix[i-1][0] and matrix[i][1] != matrix[i-1][1]:
                print(matrix[i][0],matrix[i][1],matrix[i][2]) #se for, então printa a linha
   
    #se estivermos entre duas instâncias, precisamos deixar um espaço no final
    if o == t-1:
        print("", end="")
    else:
        print("")
# -*- coding: utf-8 -*-
#URI 2463 - Corredor

n = int(input()) #entrada do número de salas no corredor

#inicialização de variáveis
maior = 0
soma = 0

corredor = [None]*n #criação do vetor corredor
auxiliar = [0]*n #criação do vetor auxiliar (com valores zerados)

#inserção dos valores no vetor corredor
corredor = [int(x) for x in input().split()]

#se a primeira sala não for negativa, ela será usada em consideração na soma
if corredor[0] > 0:
    auxiliar[0] = corredor[0]

#pulando a primeira sala, laço for realizará as somas
for i in range(1,n):
    soma = auxiliar[i-1] + corredor[i] #soma a sala anterior com a atual

    #se essa soma for positiva, o vetor auxiliar vai considerá-la na próxima soma
    #se não, o vetor auxiliar manterá seu valor 0 e vamos contar a partir da próxima sala
    if soma >= 0:
       auxiliar[i] = soma
    
    #se a soma for maior que o valor armazenado até agora, ela recebe esse valor
    if soma > maior:
        maior = soma
        
#printa a maior soma       
print(maior)
    
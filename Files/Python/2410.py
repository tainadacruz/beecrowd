# -*- coding: utf-8 -*-
#URI 2410 - Frequencia na Aula

n = int(input()) #entrada do número de registros
vetor = [None]*n #criação do vetor que armazenará os números
count = n #inicialização da variável que contará o número de alunos

for i in range(n): #para cada registro, faça
    v = int(input()) #insere o número do registro
    vetor[i] = v #vetor recebe o registro
    
vetor.sort() #alinha o vetor em ordem crescente

for i in range(1,len(vetor)): #para cada registro do vetor, verifica se há números duplicados
    if vetor[i] == vetor[i-1]: #se existir, remove esse registro do count
        count -= 1

print(count) #saída com o número de alunos
    
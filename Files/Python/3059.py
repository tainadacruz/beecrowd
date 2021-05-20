# -*- coding: utf-8 -*-
#URI 3059 - Pares de Números

count = 0 #inicialização da variável acumuladora

#entrada de variáveis:
#n = tamanho do vetor | i = valor mínimo da soma | f = valor máximo da soma
n,i,f = [int(x) for x in input().split()]
#entrada dos números no vetor
vetor = [int(n) for n in input().split()]

for j in range(n):#para cada número, faça
    #laço for que percorre os números que estiverem a frente do vetor[j], para que não ocorram repetições
    for k in range(j,n):
        #primeira condição: os números comparados não podem ser iguais
        if vetor[j] != vetor[k]:
            #segunda condição: a soma dos números precisa ser >= a i e <= a f
            if vetor[j] + vetor[k] >= i and vetor[j] + vetor[k] <= f:
                count += 1 #se os números satisfazem as condições, o count armazenará 1
                
print(count) #saída com o resultado
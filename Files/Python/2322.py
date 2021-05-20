# -*- coding: utf-8 -*-
#URI 2322 - Peça Perdida

n = int(input()) #entrada do inteiro representando as peças
vetor = [] #inicialização do vetor

#laço for que preencherá o vetor com todas as peças, de 1 a n+1
for i in range(1,n+1): 
    vetor.append(i)

#entrada das peças
numeros = [int(x) for x in input().split()] 

#para cada peça que Joãozinho possuir, o laço vai remove-la do vetor
for i in numeros:
    vetor.remove(i)
#assim, o vetor resultante possuirá apenar o valor da peça que falta, que será printado na tela    
print(vetor[0])
        
        

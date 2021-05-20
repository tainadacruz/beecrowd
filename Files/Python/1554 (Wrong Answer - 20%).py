# -*- coding: utf-8 -*-
#URI 1554 - Bilhar N+1

c = int(input()) #entrada da quantidade de casos de teste

for i in range(c): #para cada caso de teste, faça...
    n = int(input()) #entrada que define o número de bolas, além da branca       
    soma = [0]*(n) #vetor que armazenará a soma da posição das bolas
    diferenca = [0]*(n) #vetor que armazenará a diferença entre a bola branca e as outras

    for j in range(n+1): #para cada bola de bilhar + a bola branca, faça
        #entrada das variáveis da posição das bolas
        x,y = [int(a) for a in input().split()] 
        
        #se o laço está na posição 0, significa que o valor inserido é da bola branca
        if j == 0:
            somaBranca = x + y #variável que guarda a soma da posição da bola branca
        #se não, é das outras bolas
        else:
            #vetor armazena a soma das posições de cada bola:
            #é j-1 porque o vetor começa a armazenar na posição 0, enquanto a posição do laço começaria armazenando em 1
            soma[j-1] = x + y
            #vetor diferenca armazena o módulo da diferença entre as distâncias
            diferenca[j-1] = abs(soma[j-1] - somaBranca)
                        
    #variável que armazena o valor mínimo do vetor da diferença entre as distâncias
    minimo = min(diferenca) 
    #variável que armazena a posição do valor mínimo dentro do vetor, com o auxílio do index
    posicao = diferenca.index(minimo)
        
    #saida com o valor da posição. ele soma +1 porque o vetor começa em 0
    print((posicao+1))
        
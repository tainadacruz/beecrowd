# -*- coding: utf-8 -*-
#URI 2871 - Colheita de Café

while True: #início do loop que só quebra com EOFError
    try:
        #inicialização das variáveis
        sacas = 0
        litros = 0
        
        m,n = [int(x) for x in input().split()] #números que indicam o tamanho mxn da matriz
        
        #criação das linhas da matriz lavoura
        lavoura = [None]*m
        for i in range(m):        
            #inserção dos valores em cada posição da matriz
            lavoura[i] = [int(n) for n in input().split()]
            litros += sum(lavoura[i]) #variável litros acumula os valores da lavoura
             
        #enquanto a variável litros acumular um valor que pode ser transformado em saca...
        while(litros > 59):
            sacas += 1 #sacas recebe 1
            litros = litros - 60 #variável litros retira os 60 litros que foram contabilizados como 1 saca
        
        #saída com o resultados concatenados
        print("{sacas} saca(s) e".format(sacas = sacas), end = " ")
        print("{litros} litro(s)".format(litros = litros))
        
    except EOFError:
        break
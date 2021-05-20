# -*- coding: utf-8 -*-
#URI 1890 - Emplacando os Tuk-tuks

t = int(input()) #entrada com o número de instâncias
result = 1 #variável auxiliar para a multiplicação

#laço de repetição, seguindo o valor das instâncias:
for i in range(t):
    #entrada do número de consoantes e dígitos de determinado sistema de placas
    c,d = [int(a) for a in input().split()]
    
    #para cada consoante, há 26 possibilidades
    for j in range(c): 
        #logo, realiza-se a multiplicação para todas as consoantes, e armazena 
        result *= 26
    #para cada dígito, há 10 possibilidades
    for k in range(d):
        #logo, realiza-se a multiplicação para todos os dígitos, e armazena
        result *= 10
        
    if (c == 0) and (d == 0): #se não houver consoantes nem dígitos, result precisa ser 0
        result = 0
        
    print(result) #saída com o resultado
    result = 1 #atualização da variável auxiliar, para o próxima instância do laço for
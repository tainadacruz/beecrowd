# -*- coding: utf-8 -*-
#URI 2982 - A Greve para ou Continua?

n = int(input()) #entrada do número de valores citados na reunião
verba = 0 #inicialização da variável verba
gastos = 0 #inicialização da variável gastos

#para cada valor citado na reunião, faça
for i in range(n):
    #t = string que define se o valor é Verba ou Gastos
    #c = valor dos gastos
    t,c = input().split() #ambos são inseridos pelo usuário na mesma linha
    t = str(t)
    c = int(c)
    
    if (t == "V"): #se o valor inserido for uma verba
        verba += c #variável verba armazena o valor, somando com os anteriores
    else: #se não for,
        gastos += c #variável gastos armazena o valor, somando com os anteriores
    
if verba < gastos:  #se o valor das verbas for insuficiente para cobrir os gastos, a greve não para
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else: #se for suficiente, a greve para
    print("A greve vai parar.")
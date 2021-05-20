# -*- coding: utf-8 -*-

while True: #laço de repetição que só vai quebrar se for induzido a isso
     
    x,y = [int(x) for x in input().split()] #recebe duas variáveis na mesma linha e as define como int
    
    #sequência de decisões a serem tomadas, de acordo com a regra dos quadrantes
    if (x > 0) and (y > 0):
        print("primeiro")
    elif (x < 0) and (y > 0):
        print("segundo")
    elif (x < 0) and (y < 0):
        print("terceiro")
    elif (x > 0) and (y < 0):
        print("quarto")
    else:
        break #quebra do laço while, caso alguma variável seja nula


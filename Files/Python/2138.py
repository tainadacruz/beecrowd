# -*- coding: utf-8 -*-
#URI 2138 - Dígito Mais Frequente

#função que define o número mais frequente
def frequente(lista):
    count = 0 #count inicializa com zero
    frequente = lista[0] #número mais frequente inicializa com o primeiro número da lista
    
    for i in lista: #para cada número da lista
        atual = lista.count(i) #conta quantas vezes o i aparece na lista
        if (atual > count): #se ele aparecer mais vezes que o valor do count
            count = atual #count recebe esse valor
            frequente = i #frequente recebe o número atual
        elif (atual == count): #caso ocorra empate
            if i > frequente: #então verifica qual o maior número
                frequente = i #se i for maior, substitui na variável
            
    return frequente #retorna o número mais frequente

while True:
    try:
        numero = list(input()) #entrada do número, separando em uma lista
        for i in numero: #para cada número na lista, converto para um inteiro
            i = int(i)
        
        freq = frequente(numero) #chamo a função que checa o mais frequente
        print(freq) #printa o mais frequente
        
    except EOFError:
        break
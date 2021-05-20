# -*- coding: utf-8 -*-
#URI 2140 - Duas Notas
from itertools import combinations #importa módulo de combinação
dinheiro = [2,5,10,20,50,100] #define cédulas disponíveis
    
while True:
    pos = 0 #inicializa variável auxiliar
    n,m = [int(x) for x in input().split()] #entrada com o valor do produto e o dinheiro pago pelo cliente
    
    if m == 0 or n == 0: #se alguma entrada for 0, então quebra o laço
        break
    
    troco = m - n #cálculo do troco

    #com o auxílio do combinations, verificamos todas as combinações disponíveis com as cédulas
    combinacoes = list(combinations(dinheiro, 2))

    #para cada tupla de combinação
    for i in combinacoes:
        soma = i[0] + i[1] #somamos o valor dela
        if soma == troco: #se esse valor for igual ao troco, então há uma possibildade
            pos += 1 #portanto pos recebe +1

    #se existir possibilidade, então printa que sim
    if pos > 0:
        print("possible")
    else:#se não, printa que não há
        print("impossible")

# -*- coding: utf-8 -*-
#URI 2298 - Mini-Poker

n = int(input())
teste = 1
repetiu = 0

for i in range(n):
    cards = [None]*5
    repetidos = []
    cards[0],cards[1],cards[2],cards[3],cards[4] = [int(x) for x in input().split()]
    
    for j in cards:
        for k in range(j,len(cards)):
            if j == cards[k]:
                repetiu += 1
                repetidos.append(j)
    
    repetidos.sort()
    print(repetidos)
    
    '''if c1 < (c2+1) and c2 < (c3+1) and c3 < (c4+1) and c4 < (c5+1):
        resultado = c1 + 200
    elif 
    
    
    
    
    print("Teste %d"%(teste))
    print(resultado)
    print("")
    teste += 1'''
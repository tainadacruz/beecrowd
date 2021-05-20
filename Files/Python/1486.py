# -*- coding: utf-8 -*-

comprimento = [None] * 1001 

while True:
    p,n,c = input().split()
    p = int(p)
    n = int(n)
    c = int(c)
    
    if p == 0 and n == 0 and c == 0: 
        break

    maioresPalitos = 0
    for i in range(p): 
        comprimento[i] = 0 
    
    for _ in range(n):
        medicoes = input().split() 
        for i in range(p):
            if medicoes[i] == '1': 
                comprimento[i] += 1
            else:
                if comprimento[i] >= c:
                    maioresPalitos += 1  
                comprimento[i] = 0
    
    for i in range(p):
        if comprimento[i] >= c:
            maioresPalitos += 1
    
    print(maioresPalitos)


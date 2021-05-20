# -*- coding: utf-8 -*-
t = int(input())
trad = {}
frase = ""

for i in range(t):
    m,n = [int(x) for x in input().split()]
    
    for j in range(m):
        japones = str(input())
        portugues = str(input())
        
        trad[japones] = portugues
        
    for j in range(n):
        letra = input()
        letraSeparada = list(input())
        
        for palavra in letraSeparada:
            if palavra == trad[palavra].keys():
                frase = trad[palavra] + " "
            else:
                frase = palavra + " "
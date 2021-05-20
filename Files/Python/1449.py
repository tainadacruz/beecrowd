# -*- coding: utf-8 -*-
t = int(input())
trad = {}

for i in range(t):
    m,n = [int(x) for x in input().split()]
    
    for j in range(m):
        japones = str(input())
        portugues = str(input())
        
        trad[japones] = portugues
    
    musica = [""]*n
    for j in range(n):
        letra = [str(x) for x in input().split()]
        frase = []
        for palavra in letra:
            if palavra in trad:
                frase.append(trad[palavra])
            else:
                frase.append(palavra)
        frase = " ".join(frase)
        musica[j] = frase
    
    for j in range(n):
        print(musica[j])
    print("")

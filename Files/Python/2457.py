# -*- coding: utf-8 -*-

letra = input()
frase = input().split()
palavras = 0
contem = 0

for i in frase:
    palavras += 1
    letras = list(frase[palavras-1])
    for k in letras:
        if k == letra:
            contem +=1
            break

percent = contem / palavras
percent = 100 * percent
print("%.1f"%(percent))
# -*- coding: utf-8 -*-

entrada = input()
saida = ""

for i in entrada.split():
    for a in range(1,len(i),2):
        saida += i[a]
    saida += " "

print(saida[:-1])
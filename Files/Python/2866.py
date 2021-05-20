# -*- coding: utf-8 -*-

c = int(input())
palavra = []

for i in range(c):
    cript = input()
    cript = list(cript)
    
    for j in cript:
        if j.islower():
            palavra.insert(0,j)
            
    palavra = [''.join(palavra)]
    print(palavra[0])
    palavra.clear()
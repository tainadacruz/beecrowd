# -*- coding: utf-8 -*-

n = int(input())
dic = {}

for i in range(n):
    lingua = str(input())
    trad = str(input())
    
    dic[lingua] = trad
    
m = int(input())

for i in range(m):
    nome = str(input())
    lingua = str(input())
    
    print(nome)
    print(dic[lingua])
    print("")

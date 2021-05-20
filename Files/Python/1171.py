# -*- coding: utf-8 -*-

def checa(x):
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

n = int(input())
dic = {}

for i in range(n):
    x = int(input())
    checa(x)
    
for i in sorted(dic):
    print("%d aparece %d vez(es)"% (i, dic[i]))
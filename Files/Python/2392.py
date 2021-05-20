# -*- coding: utf-8 -*-

n,m = [int(x) for x in input().split()]

n = n + 1
resposta = [0]*(n)

for _ in range(m):
    p,d = [int(x) for x in input().split()]
    
    for i in range(p, n, d):
        resposta[i] = 1
        
    for i in range(p, 0, -d):
        resposta[i] = 1
    
for i in range(1,n):
    print("%d"%(resposta[i]))
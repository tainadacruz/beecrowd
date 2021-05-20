# -*- coding: utf-8 -*-

n = int(input())
r = 0
for i in range(n):
        
    a = int(input())
    b = input().split()
    c = int(input())
        
    b.insert(0, a)
    b.insert(5, c)
    
    d = [int(i) for i in b]
    
    if (d[0] + d[5]) == 7 and (d[1] + d[3]) == 7 and (d[2] + d[4]) == 7:
        r = 1
    else: 
        r = 0
    
    for i in range(len(d)):
        #verifica se o dado possui números maiores do que seis ou 0
        if d[i] > 6 or d[i] < 1: 
            r = 0
        
        # esse for ordena a lista em ordem crescente    
        # for i in range(1, len(d)):
        #    if int(d[i-1]) > int(d[i]):
        #        d[i-1],d[i] = d[i], d[i-1]
    
    d.sort()
    
    #verifica se há números duplicados no vetor
    for i in range(1,6):
        if i != int(d[i-1]):
            r = 0
            break
        
    if r == 1:
        print("SIM")
    else:
        print("NAO")

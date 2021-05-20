# -*- coding: utf-8 -*-
t = 1

while True:
    a = 0
    b = 0
    c = 0
    d = 0
    count = 0
    
    n = int(input())
    if n == 0:
        break
    
    for i in range(n):
        x,y,u,v = [int(o) for o in input().split()]
        
        if max(x,y) > max(u,v) and min(x2,y2) < min(x,y):
            a = x2 
            b = y2
            print("a")
        if max(u,v) < max(x,y) and min(x2,y2) > min(u,v):
            c = u
            d = v
            print("b")
            
        x2 = x
        y2 = y
            
    if (a!=0) and (b!=0) and (c!=0) and (d!=0):
        count = 1
            
    print("Teste %d"%(t))
    if count == 1:
        print("%d %d %d %d"%(a,b,c,d))
    else:
        print("nenhum")
    print("")
    t += 1
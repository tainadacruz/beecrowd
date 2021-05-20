# -*- coding: utf-8 -*-
t = 1

while True:
    r = int(input())
    if r == 0:
        break
    x = 0
    y = 0
    for i in range(r):
        a,b = [int(x) for x in input().split()]
        
        x += a
        y += b
        
    if x > y:
        v = "Aldo"
    elif x < y:
        v = "Beto"
        
    print("Teste %d"%(t))
    print(v)
    print("")
    
    t += 1
    
    
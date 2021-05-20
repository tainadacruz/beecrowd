# -*- coding: utf-8 -*-

v = int(input())
n = 0

while v != 0:
    n = n + 1
    
    i = 0
    j = 0
    k = 0
    l = 0
    vR = 0
    
    vR = v/50
        
    if vR >=1:
        i = 1*vR
        
    v = v%50
    vR = v//10
        
    if vR >=1:
        j = 1*vR
        
    v = v%10
    vR = v//5
        
    if vR >=1:
        k = 1*vR

    vR = v%5
        
    if vR >=1:
        l = 1*vR
            
    print("Teste %d"%(n))
    print("%d %d %d %d"%(i,j,k,l))
    print("")
        
    v = int(input())
        
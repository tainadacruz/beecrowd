# -*- coding: utf-8 -*-
import math

n = int(input())
cont = 0
for p in range(n):
    
    x = int(input())
    raiz = math.sqrt(x)
    raizC = int(raiz // 1)
    
    for i in range(2,raizC+1):
        if x%i == 0:
            cont = cont + 1
            if cont == 1:
                print("Not Prime")
            
    if cont == 0:
        print("Prime")         
    cont = 0

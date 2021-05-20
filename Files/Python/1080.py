# -*- coding: utf-8 -*-
y = 0

for i in range (100):
    x = int(input())
    
    if x > y:
        maior = x
        pos = i+1
        y = x
        
print(maior)
print(pos)
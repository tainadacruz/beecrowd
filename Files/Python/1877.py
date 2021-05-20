# -*- coding: utf-8 -*-
count = 0

n,k =  [int(x) for x in input().split()]   
h = input().split()

for i in range(n):
    h[i] = int(h[i])

valorPicos = 0
valorVales = 0

pico = False
vale = False

for i in range(1,n):
    if h[i] > h[i-1]:
        if not pico:
           pico = True
           vale = False
           valorPicos += 1
    
    if h[i] < h[i-1]:
        if not vale:
            pico = False
            vale = True
            valorVales += 1
    
if valorVales == k and valorPicos == k:
    print("beautiful")
else:
    print("ugly")
        
        
    
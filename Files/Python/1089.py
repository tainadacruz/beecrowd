# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break
    
    h = [int(n) for n in input().split()]
    
    h.append(h[0])
    h.append(h[1])
    
    picos = 0
    for i in range(1, n+1):
        if h[i] < h[i-1] and h[i] < h[i+1]:
            picos += 1
        elif h[i] > h[i-1] and h[i] > h[i+1]:
            picos +=1
    print(picos)
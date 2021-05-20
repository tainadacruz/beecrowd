# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break
    
    v = [int(n) for n in input().split()]

    for i in range(n):
        v[i] = int(v[i])
        
    r = sorted(v,key=int)
    
    for x, i in enumerate(v):
        if i == r[n-2]:
            print(x+1)
            
   # for i in range(n):
   #     if v[i] < max(v) and v[i] > v[i-1]:
   #        p = i+1
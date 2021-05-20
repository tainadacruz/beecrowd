# -*- coding: utf-8 -*-

while True:
    r = 0
    n = int(input())
    
    if n == 0:
        break
    
    for i in range(n):
        c,v = [int(x) for x in input().split()]
        r += (v//2)
        
    r = r//2
    print(r)
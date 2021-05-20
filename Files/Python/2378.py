# -*- coding: utf-8 -*-

n,c = [int(x) for x in input().split()]
v = 0
t = 0

for i in range(n):
    s,e = [int(x) for x in input().split()]
    
    t += e - s
    
    if t > c:
        v += 1
        
if v > 0:
    print("S")
else:
    print("N")
# -*- coding: utf-8 -*-

n,m = [int(x) for x in input().split()]
postos = [int(n) for n in input().split()]

consegue = True
for i in range(1,n):
    if postos[i] - postos[i-1] > m:
        consegue = False
        break
    
if consegue and 42195 - postos[n-1] > m:
    consegue = False
    
if consegue:
    print("S")
else:
    print("N")
    
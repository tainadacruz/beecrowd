# -*- coding: utf-8 -*-
go = False

p,n = [int(x) for x in input().split()]
a = [int(n) for n in input().split()]

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(n-1):
    
    d = abs(a[i] - a[i+1])
    
    if d > p:
        go = True

if go == True:
    print("GAME OVER")
else:
    print("YOU WIN")
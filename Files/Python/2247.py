# -*- coding: utf-8 -*-
t = 1
while True:   
    n = int(input())
    if n == 0:
        break
    
    print("Teste %d"%t)
    t += t
    div = 0
    
    for i in range(n):
        j,z = [int(x) for x in input().split()]
        div += (j - z)
        print(div)
    print("")
   



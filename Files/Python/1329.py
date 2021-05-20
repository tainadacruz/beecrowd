# -*- coding: utf-8 -*-

#Maria: cara. João: coroa

while True:
    x = 0
    y = 0
    n = int(input())
    
    if n == 0:
        break
    
    r = [int(n) for n in input().split()]
    
    for i in range(n):
        if r[i] == 0:
            x += 1
        elif r[i] == 1:
            y += 1
            
    print("Mary won %d times and John won %d times"% (x,y))
    
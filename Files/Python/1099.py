# -*- coding: utf-8 -*-

n = int(input())
for f in range(n):
    r = 0
    x,y = [int(i) for i in input().split()]
    if y > x:
            for i in range(x+1,y):
                if i%2 != 0:
                    r = r + i
    elif x > y:
            for i in range(y+1,x):
                if i%2 != 0:
                    r = r + i
    else:
        r = 0
    print(r)
        

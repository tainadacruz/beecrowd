# -*- coding: utf-8 -*-
x = 4
c = [int(x) for x in input().split()]

for i in range(0,len(c)):
    num = c[i]
    if num == 1:
        pos = i + 1
        break
        
print(pos)


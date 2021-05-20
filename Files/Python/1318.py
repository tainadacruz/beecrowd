# -*- coding: utf-8 -*-

while True:
    count = 0
    n,m = [int(x) for x in input().split()]
    if n == 0 and m == 0:
        break
    
    t = [int(m) for m in input().split()]
    t.sort()
    
    for i in range(len(t)):
        if t[i] == t[i-1]:
            count += 1
        if t[i] == t[i-1] and t[i-1] == t[i-2]:
            count -= 1
            
    print(count)
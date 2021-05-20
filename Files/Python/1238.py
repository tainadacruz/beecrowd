# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    count = 0
    a,b = [str(i) for i in input().split()]
    result = []
    
    a = list(a)
    b = list(b)
    
    for x,y in zip(a,b):
        count += 1
        result.append(x)
        result.append(y)
        
    if count >= len(a) and count < len(b):
        for y in range(count,len(b)):
            result.append(b[y])
    elif count >= len(b) and count < len(a):
        for x in range(count,len(a)):
            result.append(a[x])
        
    result = ["".join(result)]  
    print(result[0])
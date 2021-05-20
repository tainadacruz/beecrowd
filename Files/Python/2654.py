# -*- coding: utf-8 -*-
from operator import itemgetter

n = int(input())
dic = {}

for i in range(n):
    s,p,k,m = input().split()
    p = int(p)
    k = int(k)
    m = int(m)
    
    dic[s] = (p,k,m)
    
print(dic)  
sorted(dic.values(), key=itemgetter(0,1), reverse = True)
print(dic)
sorted(dic.values(), key=itemgetter(2), reverse = False)   
print(dic)
    
    
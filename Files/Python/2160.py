# -*- coding: utf-8 -*-

count = 0
l = list(input())

for i in range(len(l)):
    count += 1
    
if count > 80:
    print("NO")
else:
    print("YES")
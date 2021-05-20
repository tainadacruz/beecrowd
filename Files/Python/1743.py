# -*- coding: utf-8 -*-

count = 0

x = [int(x) for x in input().split()]

y = [int(y) for y in input().split()]

for i in range(5):
    if x[i] == y[i]:
        count += 1
    
if count >= 1:
    print("N")
else:
    print("Y")

# -*- coding: utf-8 -*-

l = int(input())
p = 0

while l >= 2:
    l //= 2 
    p += 1

print(4**p)

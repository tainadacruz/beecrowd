# -*- coding: utf-8 -*-

n = int(input())
qnt = 0

for n in range(n):
    l,c = [int(i) for i in input().split()]
    if l > c:
        qnt = qnt + c

print(qnt)
    
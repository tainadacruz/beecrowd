# -*- coding: utf-8 -*-

q = int(input())
v = [int(q) for q in input().split()]

media = q/2

if sum(v) >= media:
    print("N")
else:
    print("Y")
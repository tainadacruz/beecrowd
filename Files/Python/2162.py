# -*- coding: utf-8 -*-

n = int(input())
h = [int(n) for n in input().split()]

padrao = True
vale = False
pico = False

for i in range(1,n):
    if h[i] < h[i-1]:
        if vale:
            padrao = False
            break
        else:
            vale = True
            pico = False
    elif h[i] > h[i-1]:
        if pico:
            padrao = False
            break
        else:
            pico = True
            vale = False
    else:
        padrao = False
        break
if padrao:
    print("1")
else:
    print("0")
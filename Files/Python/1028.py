# -*- coding: utf-8 -*-

def mdc(f1,f2):
    return f1 if not f2 else mdc(f2, f1%f2)

n = int(input())
for i in range(n):
    f1,f2 = [int(x) for x in input().split()]

    print(mdc(f1,f2))
    
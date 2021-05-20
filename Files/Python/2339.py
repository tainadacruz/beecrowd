# -*- coding: utf-8 -*-

C,P,F = input().split()
C = int(C)
P = int(P)
F = int(F)

if F*C <= P:
    print("S")
else:
    print("N")

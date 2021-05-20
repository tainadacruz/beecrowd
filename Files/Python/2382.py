# -*- coding: utf-8 -*-

L,A,P,R = input().split()
L = int(L)
A = int(A)
P = int(P)
R = int(R)

if (L*L + A*A + P*P) <= 4*R*R:
    print("S")
else:
    print("N")

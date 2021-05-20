# -*- coding: utf-8 -*-

N = int(input())
A,L,P = input().split()
A = int(A)
L = int(L)
P = int(P)



if N <= A and N <= L and N <= P:
    print("S")
else:
    print("N")

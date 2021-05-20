# -*- coding: utf-8 -*-

A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

if (A>B and A<C) or (A<B and A>C):
    print(A)
elif (B>A and B<C) or (B<A and B>C):
    print(B)
else:
    print(C)
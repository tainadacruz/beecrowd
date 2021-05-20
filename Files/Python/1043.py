# -*- coding: utf-8 -*-

A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

if ((A+C)>B) and ((B+C)>A) and ((A+B)>C):
    P = A + B + C
    print("Perimetro = %.1f"%(P))
else:
    A = ((A+B)*C)/2
    print("Area = %.1f"%(A))

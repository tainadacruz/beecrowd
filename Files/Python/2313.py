# -*- coding: utf-8 -*-

a,b,c = [int(i) for i in input().split()]

if ((a+c)>b) and ((b+c)>a) and ((a+b)>c):
    if (a == b and b == c):
        print("Valido-Equilatero")
    elif (a == b or b == c or c == a):
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")    
    if ((a*a) + (b*b) == (c*c)) or ((c*c) + (b*b) == (a*a)) or ((a*a) + (c*c) == (b*b)):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
        
   
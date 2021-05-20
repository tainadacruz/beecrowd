# -*- coding: utf-8 -*-

l, n = [int(x) for x in input().split()]

A = [None] * 21
B = [None] * 21

for i in range(0, l):
    A[i], B[i] = input().split()
    
for _ in range(0, n):
    palavra = input()
    
    acheiNoVetor = False
    for i in range(0,l):
        if A[i] == palavra:
            print(B[i]) 
            acheiNoVetor = True
            break
            
    if not acheiNoVetor:
        t = len(palavra) 
        
        if t > 1 and palavra[t-1] == 'y' and not (palavra[t-2] == 'a' or palavra[t-2] == 'e' or palavra[t-2] == 'i' or palavra[t-2] == 'o' or palavra[t-2] == 'u') :
            print(palavra[0:t-1] + "ies")
        elif palavra[t-1] == 'o' or palavra[t-1] == 's' or palavra[t-1] == 'x':
            print(palavra + "es")
        elif t > 1 and palavra[t-1] == 'h' and (palavra[t-2] == 's' or palavra[t-2] == 'c'):
            print(palavra + "es")
        else:
            print(palavra + "s")



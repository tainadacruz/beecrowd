# -*- coding: utf-8 -*-

numeros = [None]*3
for i in range(0,3):
    numeros[i] = [None]*3
    
zero = [None]*3
    
maior = 0
for i in range(0,3):
    numeros[i] = [int(x) for x in input().split()]
    separado = list(numeros[i])
    
    if 0 in separado:
        break
    soma += sum(separado)
    if soma > maior:
        maior = soma
    elif soma < maior:
        zero[i] = maior - soma
        
    
    
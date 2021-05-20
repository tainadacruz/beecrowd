# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):
    if n > 20:
        break
    
    senha = str(input())
    numeros = []
    
    for i in senha:
        if i in "GQaku":
            numeros += "0"
        elif i in "ISblv":
            numeros += "1"
        elif i in "EOYcmw":
            numeros += "2"
        elif i in "FPZdnx":
            numeros += "3"
        elif i in "JTeoy":
            numeros += "4"
        elif i in "DNXfpz":
            numeros += "5"
        elif i in "AKUgq":
            numeros += "6"
        elif i in "CMWhr":
            numeros += "7"
        elif i in "BLVis":
            numeros += "8"
        elif i in "HRjt":
            numeros += "9"
        
        if len(numeros) >= 12:
            break
    
    numeros = ["".join(numeros)]
    print(numeros[0])
    

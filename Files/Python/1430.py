# -*- coding: utf-8 -*-

notas = {"W": 1,"H": 0.5,"Q": 0.25,"E": 0.125,"S": 0.0625, "T": 0.03125,"X": 0.015625}

while True:
    soma = 0
    compasso = 0
    
    string = str(input())
    if string == "*":
        break
    
    string = list(string)
    
    for i in range(1,len(string)):
        if string[i] == "/":
            soma = 0
        else:
            soma += notas[string[i]]
            
        if soma == 1 and string[i+1] == "/":
            compasso += 1
    
    print(compasso)
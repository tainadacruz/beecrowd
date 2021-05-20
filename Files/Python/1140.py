# -*- coding: utf-8 -*-
while True:
    count = False
    frase = list(input())
    if frase[0] == '*':
        break
        
    for i in range(len(frase)):
        frase[i] = frase[i].lower()
            
    letra = frase[0]
        
    for i in range(len(frase)):
        if frase[i-1] == " " and frase[i] != letra:
            count = True

    if count == True:
        print("N")
    else:
        print("Y")
        
    frase.clear()
    

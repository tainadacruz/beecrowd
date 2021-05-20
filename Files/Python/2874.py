# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        letra = [None]*n
        
        for i in range(n):
            b = str(input())
            b = chr(int(b,2))
            letra[i] = b
        
        result = [''.join(letra)]
        print(result[0])            
            
    except EOFError:
        break
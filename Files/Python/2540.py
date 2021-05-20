# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        voto = [int(n) for n in input().split()]
        imp = 0
        
        for i in range(n):
            if voto[i] == 1:
                imp += 1
        
        if imp >= ((n*2)/3):
            print("impeachment")
        else:
            print("acusacao arquivada")
                    
    except EOFError:
        break
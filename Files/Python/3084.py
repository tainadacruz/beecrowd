# -*- coding: utf-8 -*-

while True:
    try:
        h,m = [int(i) for i in input().split()]

        hora = h/30
        minuto = m/6
        
        print("%.2d:%.2d"%(hora,minuto))
        
    except EOFError:
        break
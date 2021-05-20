# -*- coding: utf-8 -*-

vector = [31,29,31,30,31,30,31,31,30,31,30,31]

while True: 
    try:
        dias = 0
        total = 0
        
        m,d = [int(x) for x in input().split()]
        
        if (m == 12) and (d == 24):
            print("E vespera de natal!")
        elif (m == 12) and (d > 25):
            print("Ja passou!")
        elif (m == 12) and (d == 25):
            print("E natal!")
        else:
            for a in range(m-1):
                dias += int(vector[a])
                #atual = vector[a+1]        
            dias = dias + d
            total = 360 - dias
            print("Faltam %d dias para o natal!"%(total))    
    except EOFError:
        break
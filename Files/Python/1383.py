# -*- coding: utf-8 -*-
matrix = [None] * 9
n = int(input())

for k in range(1,n+1):
    
    for i in range(9):
        matrix[i] = input().split()
        for j in range(9):
            matrix[i][j] = int(matrix[i][j])
    
    sim = True
    presente = [0] * 10
    
    for i in range(9):        
        for x in range(1,10):
            presente[x] = False
        
        for j in range(9):
            if presente[matrix[i][j]]:
                sim = False
                break
            else:
                presente[matrix[i][j]] = True
        if not sim:
            break
    
    if sim:
        for j in range(9):
            for x in range(1,10):
                presente[x] = False
            
            for i in range(9):
                if presente[matrix[i][j]]:
                    sim = False
                    break
                else:
                    presente[matrix[i][j]] = True
            if not sim: 
                break
    if sim:
        for o in range(0,3):
            for p in range(0,3):
                for x in range(1,10):
                    presente[x] = False
                
                for i in range(o*3,(o+1)*3):
                    for j in range(p*3,(p+1)*3):
                        if presente[matrix[i][j]]:
                            sim = False
                            break
                        else:
                            presente[matrix[i][j]] = True  
                    if not sim:
                        break
                if not sim:
                    break
            if not sim:
                break        
    
    print("Instancia %d" % (k))
    if sim:
        print("SIM")
    else:
        print("NAO")
    print("")

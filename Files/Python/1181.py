# -*- coding : utf-8 -*-

l = int(input())
t = input()

mat = [None]*12
for i in range(0,12):
    mat[i] = [None]*12
    
for i in range(0,12): #Lê os 144 elementos
    for j in range(0,12):
        mat[i][j] = float(input())
        
soma = 0

for i in range(0,12):
    soma += mat[l][i]
    
if t == "S":
    print ("%.1f"%(soma))
else:
    print ("%.1f"%(soma/12))
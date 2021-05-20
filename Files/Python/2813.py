# -*- coding: utf-8 -*-
n = int(input())

chuvaCasa = 0
chuvaTrabalho = 0

comprarCasa = 0
comprarTrabalho = 0

for i in range(n):
    ida,volta = [str(x) for x in input().split()]
    
    if ida == 'chuva':
        if chuvaCasa > 0:
            chuvaCasa -= 1
            chuvaTrabalho += 1
        else:
            comprarCasa += 1
            chuvaTrabalho += 1
    if volta == 'chuva':
        if chuvaTrabalho > 0:
            chuvaTrabalho -= 1
            chuvaCasa += 1
        else:
            comprarTrabalho += 1
            chuvaCasa += 1
            
print("%d %d"%(comprarCasa,comprarTrabalho))
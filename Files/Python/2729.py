# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    alim = input().split()
    alim = sorted(alim)
        
    for j in range(1,len(alim)):
        if alim[j] == alim[j-1]:
            alim[j-1] = None
             
    for j in alim:
        if j != None:
            if alim[len(alim)-1] != j:
                print(j, end=" ")
            else:
                print(j)
                    
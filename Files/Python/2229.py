# -*- coding: utf-8 -*-

n = int(input()) #número de vezes que a operação D foi aplicada
t = 0
re = 0

while n != -1:
    t += 1
    
    if n == 0:
        re = 4
    elif n == 1:
        re = 9
    else:
        re = (1+ pow(2,n))*(1+pow(2,n))
    
    print("Teste %d"%(t))
    print(re)
    print("")
    
    n = int(input())

# -*- coding: utf-8 -*-

def hanoi(n):
    count = (2**n) - 1
    return count
    
teste = 0
while True:
    count = 0
    teste += 1
    
    n = int(input())
    if n == 0:
        break
    
    count = hanoi(n)
    
    print("Teste %d"%(teste))
    print(count)
    print("")
    
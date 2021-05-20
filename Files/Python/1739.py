# -*- coding: utf-8 -*-
import math
def isQuadradoPerfeito(x):
    s = int(math.sqrt(x))
    if s*s == x:
        return True 

def isFibonnaci(y):
    if isQuadradoPerfeito(5*y*y + 4) or isQuadradoPerfeito(5*y*y - 4):
        return True

def isMultiplo(z):
    if z % 3 == 0:
        return True

def threebonnaci(n):
    if n <= 1:
        return 1
    if n not in dicti:
        if isFibonnaci(n) and isMultiplo(n):
            dicti[n] = n
            return dicti[n]
        else:
            return 0

while True:
    try:
        n = int(input())
        dicti = {}
        vetor = []
        
        for i in range(n):
            vetor.append(threebonnaci(i))
            
        print(vetor[n-1])
            
    except EOFError:
        break

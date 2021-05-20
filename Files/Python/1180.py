# -*- coding: utf-8 -*-

n = int(input())
x = []*n
x = input().split()

for i in range(len(x)):
    x[i] = int(x[i])
        
print("Menor valor: %d" % (min(x)))
p = x.index(min(x))
print("Posicao: %d" % (p))
    
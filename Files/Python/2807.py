# -*- coding: utf-8 -*-

def fibonnaci(n):
    if n <= 1:
        return 1
    if n not in dicti:
        dicti[n] = fibonnaci(n-1) + fibonnaci(n-2)
    return dicti[n]

n = int(input())
vetor = []
dicti = {}

for i in range(n):
    vetor.append(fibonnaci(i))

ind = 0
for i in reversed(vetor):
    ind += 1
    if ind < n:
        print(i, end=" ")
    else:
        print(i)
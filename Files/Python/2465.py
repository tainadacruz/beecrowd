# -*- coding: utf-8 -*-

n = int(input())

camisa = [None] * n 
for i in range(n):
    camisa[i] = [None] * n

bandeira = [None] * n
for i in range(n):
    bandeira[i] = [None] * n

i,j = input().split()
i = int(i) -1
j = int(j) -1

for k in range(n):
    camisa[k] = [int(x) for x in input().split()]
    for l in range(n):
        bandeira[k][l] = False
        
somaBandeira = 1
bandeira[i][j] = True
novosAlunos = []
novosAlunos.append((i,j))

while novosAlunos != []:  
    (k,l) = novosAlunos.pop(0)
    
    vizinhoK = k-1
    vizinhoL = l
    if vizinhoK >= 0 and bandeira[vizinhoK][vizinhoL] == False and camisa[k][l] <= camisa[vizinhoK][vizinhoL]:
        bandeira[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaBandeira += 1

    vizinhoK = k+1
    vizinhoL = l
    if vizinhoK < n and bandeira[vizinhoK][vizinhoL] == False and camisa[k][l] <= camisa[vizinhoK][vizinhoL]:
        bandeira[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaBandeira += 1
        
    vizinhoK = k
    vizinhoL = l-1
    if vizinhoL >= 0 and bandeira[vizinhoK][vizinhoL] == False and camisa[k][l] <= camisa[vizinhoK][vizinhoL]:
        bandeira[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaBandeira += 1
        
    vizinhoK = k
    vizinhoL = l+1
    if vizinhoL < n and bandeira[vizinhoK][vizinhoL] == False and camisa[k][l] <= camisa[vizinhoK][vizinhoL]:
        bandeira[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaBandeira += 1

print(somaBandeira)

    
    
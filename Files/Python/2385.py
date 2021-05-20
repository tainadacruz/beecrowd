# -*- coding: utf-8 -*-

n = int(input())
p,q,r,s,x,y = [int(x) for x in input().split()]
x1,x2 = [int(x) for x in input().split()]

a = [None]*n
for i in range(0,n):
    a[i] = [None]*n
    for j in range(0,n):
        a[i][j] = (p*i+q*j) % x
        
b = [0]*n
for i in range(0,n):
    b[i] = [None]*n
    for j in range(0,n):
        b[i][j] = (r*i+s*j) % y

print(a)
print(b)
        
c = [0]*n
aux = 0
count = 0
test = 0
soma = 0

for i in range(0,n):
    c[i] = [0]*n
    while aux != n:
        for j in range(0,n):
            c[i][test] += a[i][aux] * b[j][count]
            aux += 1
        soma = 0
        test = +1
    print(c)
    aux = 0
    count += 1

print(c[x1][x2])
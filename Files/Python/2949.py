# -*- coding: utf-8 -*-

def incrementa(tipo):
    dic[tipo] += 1

n = int(input())
dic = {"X":0,"H":0,"E":0,"A":0,"M":0}

for i in range(n):
    nome,tipo = input().split()
    incrementa(tipo)
    
print("%d Hobbit(s)"%(dic["X"]))
print("%d Humano(s)"%(dic["H"]))
print("%d Elfo(s)"%(dic["E"]))
print("%d Anao(s)"%(dic["A"]))
print("%d Mago(s)"%(dic["M"]))

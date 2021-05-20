# -*- coding: utf-8 -*-
  
n = float(input())
n = round(n,2)

nCem = n // 100
n -= (nCem*100)
n = round(n,2)

nCinq = (n % 100) // 50
n -= (nCinq*50)
n = round(n,2)

nVinte = (n % 50) // 20
n -= (nVinte*20)
n = round(n,2)

nDez = (n % 20) // 10
n -= (nDez*10)
n = round(n,2)

nCinco = (n % 10) // 5
n -= (nCinco*5)
n = round(n,2)

nDois = (n % 5) // 2
n -= (nDois*2)
n = round(n,2)

if (n != 0):
    n1 = (n % 2) // 1
    n -= (n1*1)
    n = round(n,2)
    
    n05 = (n % 1) // 0.5
    n -= (n05*0.5)
    n = round(n,2)
    
    n025 = (n % 0.5) // 0.25
    n -= (n025*0.25)
    n = round(n,2)
    
    n010 = (n % 0.25) // 0.10
    n -= (n010*0.10)
    n = round(n,2)
    
    n005 = (n % 0.10) // 0.05
    n -= (n005*0.05)
    n = round(n,2)
    
    n001 = (n % 0.05) / 0.01
    n -= (n001*0.01)
    n = round(n,2)
    
else:
    n1 = 0
    n05 = 0
    n025 = 0
    n010 = 0
    n005 = 0
    n001 = 0

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % nCem)
print("%d nota(s) de R$ 50.00" % nCinq)
print("%d nota(s) de R$ 20.00" % nVinte)
print("%d nota(s) de R$ 10.00" % nDez)
print("%d nota(s) de R$ 5.00" % nCinco)
print("%d nota(s) de R$ 2.00" % nDois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % n1)
print("%d moeda(s) de R$ 0.50" % n05)
print("%d moeda(s) de R$ 0.25" % n025)
print("%d moeda(s) de R$ 0.10" % n010)
print("%d moeda(s) de R$ 0.05" % n005)
print("%d moeda(s) de R$ 0.01" % n001)
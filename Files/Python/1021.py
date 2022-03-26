# -*- coding: utf-8 -*-

def update(number, aux, bill):
    number -= (aux * bill)
    number = round(number,2)
    return number

def counting(number, bill, last):
    if number == 0:
        return 0

    if bill >= 100:
        x = number // bill
    else:
        x = (number % last) // bill
    return x

    
num = float(input())
num = round(num,2)

print("NOTAS:")
aux = counting(num, 100, None)
print("%d nota(s) de R$ 100.00" % aux)
num = update(num, aux, 100)
aux = counting(num, 50, 100)
print("%d nota(s) de R$ 50.00" % aux)
num = update(num, aux, 50)
aux = counting(num, 20, 50)
print("%d nota(s) de R$ 20.00" % aux)
num = update(num, aux, 20)
aux = counting(num, 10, 20)
print("%d nota(s) de R$ 10.00" % aux)
num = update(num, aux, 10)
aux = counting(num, 5, 10)
print("%d nota(s) de R$ 5.00" % aux)
num = update(num, aux, 5)
aux = counting(num, 2, 5)
print("%d nota(s) de R$ 2.00" % aux)
num = update(num, aux, 2)

print("MOEDAS:")
aux = counting(num, 1, 2)
print("%d moeda(s) de R$ 1.00" % aux)
num = update(num, aux, 1)
aux = counting(num, 0.5, 1)
print("%d moeda(s) de R$ 0.50" % aux)
num = update(num, aux, 0.5)
aux = counting(num, 0.25, 0.5)
print("%d moeda(s) de R$ 0.25" % aux)
num = update(num, aux, 0.25)
aux = counting(num, 0.10, 0.25)
print("%d moeda(s) de R$ 0.10" % aux)
num = update(num, aux, 0.10)
aux = counting(num, 0.05, 0.10)
print("%d moeda(s) de R$ 0.05" % aux)
num = update(num, aux, 0.05)
aux = counting(num, 0.01, 0.05)
print("%d moeda(s) de R$ 0.01" % aux)

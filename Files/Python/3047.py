# -*- coding: utf-8 -*-
#URI 3047 - A Idade de Dona Mônica

m = int(input()) #entrada da idade de Mônica
a = int(input()) #entrada da idade do primeiro filho
b = int(input()) #entrada da idade do segundo filho

c = m - (a+b) #cálculo que descobre a idade do terceiro filho

#estrutura de decisão que verifica qual filho é o mais velho
if (a > b) and (a > c):
    print(a)
elif (b > a) and (b > c):
    print(b)
else:
    print(c)
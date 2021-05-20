# -*- coding: utf-8 -*-

alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dic = {}

for i in range(1,27):
    dic[alfabeto[i-1]] = i
    
letra = input()
print(dic[letra])
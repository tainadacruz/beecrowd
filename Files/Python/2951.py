# -*- coding: utf-8 -*-
#URI 2951 - O Retorno do Rei

#entrada da quantidade de runas e valor de amizade necessário
n,g = [int(x) for x in input().split()]
dicionario = {} #inicializa dicionário
amizade = 0 #inicializa amizade

for i in range(n): #para cada runa
    r,v = input().split() #recebe seu nome e seu valor de amizade
    v = int(v) #converte o valor para inteiro
    dicionario[r] = v #adiciona o par no dicionário
    
x = int(input()) #entrada da quantidade de runas
runa = [str(x) for x in input().split()] #lista de runas recitadas

for i in runa: #para cada elemento na lista de runas
    amizade += dicionario[i] #soma seu valor na amizade
 
print(amizade) #printa o valor de amizade final
if amizade >= g: #se esse valor foi o suficiente para vencer Gollum
    print("You shall pass!") #então printa you shall pass!
else: #se não foi
    print("My precioooous") #então printa a frase do Gollum
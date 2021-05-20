# -*- coding: utf-8 -*-
#URI 3039 - Brinquedos do Papai Noel

n = int(input()) #entrada do número de crianças
carrinho = 0 #inicialização da variável carrinho
boneca = 0 #inicialização da variável boneca

for i in range(n): #para cada criança..
    name,s = input().split() #é dito seu nome e o gênero
    
    if s == "F": #se for uma menina, boneca armazena +1
        boneca += 1
    else: #se não, carrinho armazena +1
        carrinho += 1

#saídas com o número de bonecas e carrinhos
print("%d carrinhos"%(carrinho))
print("%d bonecas"%(boneca))
    
    
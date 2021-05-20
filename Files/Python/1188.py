# -*- coding: utf-8 -*-
#URI 1188 - Área Inferior

o = input() #entrada que indica o tipo de operaçãp

#criação de uma matriz 12x12
mat = [None]*12
for i in range(0,12):
    mat [i] = [None]*12
    
#para cada posição da matriz, é inserido um valor pelo usuário    
for i in range(0,12): 
    for j in range(0,12):
        mat[i][j] = float(input())

#inicialização da variável soma
soma = 0 
#inicialização da variável que armazena a quantidade de posições que serão consideradas no cálculo
qtde = (144-24)/4
 
#para cada quadro, que estão sendo consideros a partir da linha 6 do vetor, faça
for i in range(6,12):
    for j in range(12-i,i): #12-i vai iniciar a contagem na posição que precisamos, assim como i termina
        soma += mat[i][j] #variável soma armazena o valor dos quadradinhos

if o == "S": #se a entrada for S, só mostra a soma
    print("%.1f"%(soma))
else: #se for M, então realiza a média
    print("%.1f"%(soma/qtde))
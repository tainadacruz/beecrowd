# -*- coding: utf-8 -*-
#URI 3037 - Jogando Dardos Por Distância

n = int(input()) #entrada do número de casos de teste
multij = 0 #inicialização da variável multi de João
multim = 0 #inicialização da variável multi de Maria

#para cada caso de teste, faça
for i in range(n):
    #verifica os 3 arremessos de João:
    for a in range(3):
        #variável dj = distância, variável xj = pontuação, ambas escritas na mesma linha
        dj,xj = [int(a) for a in input().split()]
        multij += dj*xj #multij armazena a multiplicação em cada varredura do for
    #verifica os 3 arremessos de Maria:
    for b in range(3):
        #variável dm = distância, variável xm = pontuação, ambas escritas na mesma linha
        dm,xm = [int(b) for b in input().split()]
        multim += dm*xm #multim armazena a multiplicação em cada varredura do for
    
    if multim > multij: #se os pontos de Maria forem maiores que os de João, escreve MARIA
        print("MARIA")
    else: #se não forem, então escreve JOAO
        print("JOAO")
    
    #variáveis de multiplicação zeram para o próximo for
    multim = 0 
    multij = 0

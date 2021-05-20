# -*- coding: utf-8 -*-
#URI 2473 - Loteria

count = 0 #inicialização da variável auxiliar

jogada = [int(x) for x in input().split()] #entrada com a jogada 
sorteado = [int(x) for x in input().split()] #entrada com o valor dos números sorteados

for i in range(6): #para cada numero jogado...
    for k in sorteado: #verifica se ele é equivalente a algum número sorteado
        if jogada[i] == k:
            count += 1 #se for, variável auxiliar recebe +1

#dependendo do valor do count, a saída terá um print diferente
if count == 3:
    print("terno")
elif count == 4:
    print("quadra")
elif count == 5:
    print("quina")
elif count == 6:
    print("sena")
else: #se não há nenhuma equivalência, significa que o jogador não acertou nada
    print("azar")
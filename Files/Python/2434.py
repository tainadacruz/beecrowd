# -*- coding: utf-8 -*-

# n = número de dias no período | s = saldo inicial
n,s = [int(x) for x in input().split()]

menor = s #define o menor saldo, antes de qualquer movimentação

for i in range(n):
    mov = int(input()) #recebe a movimentação da conta
    atual = s + mov #atualiza o saldo
    
    #se o saldo atual for menor, atualiza a variável
    if atual <= menor:
        menor = atual
        
    s = atual #define o saldo anterior para a próxima conta
print(menor) #mostra o menor saldo no período
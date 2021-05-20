# -*- coding: utf-8 -*-
#URI 3117 - Atrasadinhos

#entrada das variáveis n (quantidade de alunos) e k (quantidade mínima de pessoas)
n,k = [int(x) for x in input().split()]
#entrada dos horários de cada aluno
horario = [int(n) for n in input().split()]

#incialização da variável que definirá se treinamento vai ocorrer ou não
treinamento = False

for i in range(n):#para cada aluno, faça
    #se o horário for maior ou igual a 0, o aluno não está atrasado
    if horario[i] <= 0:
        k -= 1 #logo, o número mínimo de pessoas na sala diminui
    #se o número mínimo de pessoas chegou na sala...
    if k <= 0:
        treinamento = True #então o treinamento vai ocorrer

if treinamento:
    print("YES") #se o treinamento ocorrer, a saida será YES
else:
    print("NO") #se não ocorrer, a saída será NO
        


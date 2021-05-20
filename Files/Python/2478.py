# -*- coding: utf-8 -*-
#URI 2478 - Acerte o Presente

dic = {} #inicialização do dicionário
x = int(input()) #quantidade de participantes do amigo secreto

for i in range(x): #para cada participante
    n,p1,p2,p3 = input().split() #recebe seu nome e seus presentes
    dic[n] = (p1,p2,p3) #guarda isso no dicionário

while True: #inicia o loop de tentativas
    try:    
        nome, presente = input().split() #insere um nome e um presente
        #checa se o nome está no dicionário e se o presente está contido nessa chave
        if nome in dic and presente in dic[nome]: #se estiver, então printa que acertou 
            print("Uhul! Seu amigo secreto vai adorar o/")
        else: #se não, printa o aviso para tentar novamente
            print("Tente Novamente!")
    except EOFError:
        break
# -*- coding: utf-8 -*-
#URI 2464 - Decifra

alfabeto = list(str(input())) #entrada que recebe a ordem criptografada do alfabeto e a separa em posições do vetor
frase = list(str(input())) #entrada que recebe a frase criptografa e também separa em posições do vetor

#vetor que recebe o alfabeto correto
correto = "abcdefghijklmnopqrstuvwxyz"
correto = list(correto)

descript = "" #variável que receberá a frase descriptografada

for i in frase: #para cada letra da frase
    for j in range(len(alfabeto)): #verifica qual é a letra correspondente no alfabeto criptografado
        if i == alfabeto[j]: #quando achar, troca pela letra correta e armazena na variável
            descript += correto[j]
            
print(descript) #saída com a frase descriptografada




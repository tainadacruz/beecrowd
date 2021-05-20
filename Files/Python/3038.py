# -*- coding: utf-8 -*-
#URI 3038 - Carta de Natal Criptografada

while True:
    try:
        f = str(input()) #entrada da frase da cartinha
        f = list(f) #função que separa os elementos da frase em posições separadas no vetor
        
        #para cada posição da lista, o laço vai verificar se ela é um símbolo da criptografia
        for i in range(len(f)):
            #se for, ele vai substituir pela letra correspondente na tabela
            if f[i] == "@":
                f[i] = "a"
            elif f[i] == "&":
                f[i] = "e"
            elif f[i] == "!":
                f[i] = "i"
            elif f[i] == "*":
                f[i] = "o"
            elif f[i] == "#":
                f[i] = "u"
        
        #a lista volta a juntar todos os elementos em uma única posição
        f = ["".join(f)]
        print(f[0]) #saída com a carta descriptografada
        
    except EOFError:
        break
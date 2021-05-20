# -*- coding: utf-8 -*-

#vários casos de teste, enquanto não der EOFError
while True:
    try:
        entrada = str(input()) #entrada da frase
        entrada = list(entrada) #separação dos elementos da frase em posições diferentes no vetor
        
        #para cada elemento da frase, começando com o segundo, ele checa se é um ponto ou uma vírgula
        for i in range(1,len(entrada)):
            #se for um ponto, e antes dele existir um espaço, ele é apagado
            if entrada[i] == "." and entrada[i-1] == " ":
                entrada[i-1] = ""
            #se for uma vírgula, e antes dela existir um espaço, ele é apagado
            elif entrada[i] == "," and entrada[i-1] == " ":
                entrada[i-1] = ""
        
        #o vetor, após o processo, junta seus elementos novamente, em uma  única posição
        entrada = ["".join(entrada)]
        print(entrada[0]) #saída com a frase finalizada

    except EOFError:
        break
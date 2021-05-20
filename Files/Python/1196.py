# -*- coding: utf-8 -*-

teclado = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
teclado = list(teclado)

while True:
    try:
        entrada = input()
        entrada = list(entrada)
        saida = []

        for i in entrada:
            if i == " ":
                saida.append(i)
            else:
                saida.append(teclado[teclado.index(i)-1])

        saida = ["".join(saida)]
            
        print(saida[0])
        
    except EOFError:
        break

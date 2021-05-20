# -*- coding: utf-8 -*-
#URI 3060 - Parcelamento Sem Juros

v = int(input()) #entrada do valor da compra
p = int(input()) #entrada do valor das parcelas

#se o valor da compra é divisível pelo número de parcelas...
if (v % p == 0): 
    result = v / p #...cada parcela terá um valor igual
    for i in range(p):
        #o resultado é mostrado para cada parcela
        print(int(result))
#se o valor da compra não for divisível por p...
else:
    resto = v % p #variável armazena o resto da divisão
    result = v // p #resultado armazena o valor, retirando o resto da divisão
    for i in range(p):
        #se o resto ainda não for zero
        if resto > 0:
            #o valor mostrado na parcela da posição i será somado com o valor do resto dividido por ele mesmo (para dar 1)
            print(int(result+(resto/resto)))
            resto -= 1 #resto retira o valor acrescentado na parcela anterior, e o laço for repete o processo
        #quando o resto for 0, o valor da parcela será mostrado normalmente
        else:
            print(int(result))
    
    

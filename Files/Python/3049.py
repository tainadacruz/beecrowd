# -*- coding: utf-8 -*-
#URI 3049 - Nota Cortada

#Tamanho da nota: 160x70 cm

b = int(input()) #entrada da distância do ponto inicial do corte, na base
t = int(input()) #entrada da distância do ponto final do corte

#se a soma das distâncias dos cortes for maior que 160:
#significa que o corte ultrapassa a metade da nota

#se a soma das distâncias dos cortes for menor que 160:
#significa que o corte não ultrapassa a metade da nota

#se a soma das distâncias dos cortes for igual a 160:
#significa que a nota está sendo dividida igualmente

#estrutura de decisão que verifica os pontos citados acima:
if (t+b) == 160:
    #se o corte está na metade, a nota não tem valor algum
    count = 0
elif (t+b) < 160:
    #se o corte não ultrapassa o tamanho da nota, a nota que vale 100 pertence a Marzia
    count = 2
else:
    #se o corte ultrapassa, a nota que vale 100 pertence ao Felix
    count = 1
    
print(count)
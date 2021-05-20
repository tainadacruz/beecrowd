# -*- coding: utf-8 -*-

#entrada das variáveis para os dias e os meses:
a,b = [int(x) for x in input().split()]
c,d = [int(y) for y in input().split()]
dia = 0 #inicializa a variável dia

# 1 3 5 7 8 10 12 = 31
# 4 6 8 11 = 30
# 2 = 28

if(b==d): # se o mês for o mesmo, apenas realiza a subtração dos dias 
    dia = c-a
else:
    for i in range(b,d+1): #laço que percorre os meses, +1 acrescentado pois o laço não percorria o último mês
        if (i==4) or (i==6) or (i==8) or (i==11):# se o mês for um desses, ele possui 30 dias            
            #se o laço estiver no primeiro mês, "dia" recebe os 30 dias do mês e subtrai os dias que já passaram em "a"    
            if(i==b):
                dia += 30 - a
            #se o laço estiver no último mês, ele acrescenta os dias que já passaram nele
            elif(i==d):
                dia += c
            #se o laço estiver em qualquer outro mês, apenas soma todos os dias desse
            else:
                dia += 30;
        elif (i==2):#mesmo esquema para os outros ifs, apenas diferindo o número de dias, de acordo com o mês
            if(i==b):
                dia += 28 - a
            elif(i==d):
                dia += c
            else:
                dia += 28
        else:
            if(i==b):
                dia += 31 - a
            elif(i==d):
                dia += c
            else:
                dia += 31
print(dia) #mostra ao resultado da diferenças de dias
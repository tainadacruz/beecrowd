# -*- coding: utf-8 -*-

n = int(input())
tempo = 0

#prim = variável "primeira"
#t = último segundo em que o sensor ativou
#ant = o segundo anterior

prim = -1   #variável inicia com valor não positivo 
ant = prim  #ant(anterior) a recebe. processo feito para que, na primeira varredura do laço for, não caia em if

for i in range(1,n+1):
    
    t = int(input())
    
    #se o segundo anterior for diferente de prim, e o tempo atual - o tempo anterior for menor do que 10, faça
    if (ant != prim) and (t - ant < 10): 
        #tempo retira seus 10 segundos e subtrai a diferença entre o segundo atual e o segundo anterior, para que possa armazenar os segundos e reiniciar a contagem
        tempo -= 10 - (t - ant) 
    
    ant = t #segundo anterior recebe o segundo atual, para a próxima varredura
    tempo += 10 #tempo acrescenta +10 segundos, pois o sensor ligou novamente
        
print(tempo)
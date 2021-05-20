# -*- coding: utf-8 -*-
#URI 2231 - Temperatura Lunar

t = 1 #inicialização da variável de marcação do Teste
while True:
    #inicialização de variáveis necessárias para os cálculos
    total = 0
    menor = 0
    maior = 0
    media = 0
    
    # n = número total de medições | m = tamanho dos intervalos, em minutos
    n,m = [int(a) for a in input().split()]
    
    #regra para finalizar o laço While:
    if (n == 0) or (m == 0):
        break
    
    #inicialização do vetor que armazenará as temperaturas
    array = []*(n+1)#ele possuirá tamanho n+1
    
    #laço que armazenará as temperaturas em um vetor
    for i in range(n):
        temp = int(input()) #entrada da temperatura
        array.insert(i,temp) #inserção da temperatura na posição i do array
    
    #laço que fará o cálculo, de acordo com o tamanho dos invervalos e o número de medições
    for j in range(1,n+1):
        #variável total começa somando os valores respectivos da temperatura
        total += array[j-1] 
        
        #quando o laço excede o tamanho do intervalo proposto...
        if (j >= m+1):
            #ele começa a  subtrair o valor da posição j-m, para que o intervalo prossiga sendo m 
            total -= array[(j-1)-m] #array ficou (j-1)-m pois o laço for é n+1, enquanto as posiçõeos do array são armazenadas em n
        
        #o cálculo da média só pode ocorrer quando a variável total alcança a soma necessária, de tamanho m
        if (j >= m):
            media = total / m
                
        #quando o laço estiver pronto para realizar o cálculo..
        #inicializa-se as variáveis menor e maior, com a primeira média calculada
        if (j == m):
            menor = media
            maior = media
        
        #se a média atual for menor do que a média armazenada, ela é gravada na variável menor    
        if (media < menor):
            menor = media
        
        #se a média atual for maior do que a média armazenada, ela é gravada na variável maior                    
        if (media > maior):
            maior = media
        
    print("Teste %d"%(t)) #saída que mostra a marcação do Teste
    print("%d %d"%(menor,maior)) #saída que mostra a menor média e a maior média
    print("") #saída vazia, como determina o problema
    t += 1 #Teste recebe +1 para a próxima varredura d o laço While
    
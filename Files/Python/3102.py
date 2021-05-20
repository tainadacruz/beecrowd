# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    #entrada dos valores das coordenadas do triângulo
    x1,y1,x2,y2,x3,y3 = [int(a) for a in input().split()]
 
    # matriz + sarrus:
    #  | x1 y1 1 | x1 y1
    #  | x2 y2 1 | x2 y2
    #  | x3 y3 1 | x3 y3
    
    #cálculo da determinante de  uma matriz quadrada
    #essa matriz é formada pelos pontos das coordenadas do triângulo
    
    det = -(x3*y2)-(x1*y3)-(y1*x2)+(x1*y2)+(y1*x3)+(x2*y3)
    
    area = det/2 #a área pode ser calculada dividindo a determinante por 2
    area = abs(area) #extrai o módulo do número
    print("%.3f"%(area)) #mostra o valor da área, com casas decimais definidas 
    
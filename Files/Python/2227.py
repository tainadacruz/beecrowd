# -*- coding: utf-8 -*-
teste = 1

while True:
    a,v = [int(x) for x in input().split()]
    aeroportos = [None]*(a+2)
    
    if a == 0 and v == 0:
        break
    
    for i in range(1,a+1):
        aeroportos[i] = 0
    
    for i in range(v):
        #x,y = há voo de x para y
        x,y = [int(x) for x in input().split()]
        
        aeroportos[x] += 1
        aeroportos[y] += 1
    
    maximo = 0
    for i in range(1,a+1):
        if aeroportos[i] > maximo:
            maximo = aeroportos[i]
        
    print("Teste %d"%(teste))
    for i in range(1,a+1):
        if aeroportos[i] == maximo:
            print("%d "%(i),end="")
    print("")
    print("")
    teste += 1
        
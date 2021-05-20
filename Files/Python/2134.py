# -*- coding: utf-8 -*-

ins = 0
while True:
    try:
        ins += 1
        n = int(input())
        
        dic = {}
        nomes = []
        
        for i in range(n):
            nome,numero = input().split()
            numero = int(numero)
            dic[nome] = numero
             
        for key in dic:
            if dic[key] == min(dic.values()):
                nomes.append(key)
                
        nomes = sorted(nomes)
        
        print("Instancia %d"% (ins))
        print(max(nomes))
        print("")
        
    except EOFError:
        break
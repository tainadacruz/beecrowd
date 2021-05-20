# -*- coding: utf-8 -*-
direito = [None]*61
esquerdo = [None]*61

while True:
    try:
        n = int(input())
    
        for i in range(30, 61):
            direito[i] = 0
            esquerdo[i] = 0
        
        for i in range(n):
            m,l = [str(x) for x in input().split()]
            
            if l == "D":
                direito[int(m)] += 1
            else:
                esquerdo[int(m)] += 1
            
            resposta = 0
            
        for i in range(30,61):
            if direito[i] < esquerdo[i]:
                resposta += direito[i]
            else:
                resposta += esquerdo[i]
                
        print(resposta)
              
        
    except EOFError:
        break
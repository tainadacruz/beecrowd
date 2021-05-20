# -*- coding: utf-8 -*-

solucao = [None] * 101
while True:
    n,m = [int(x) for x in input().split()]
    if n == 0 and m == 0:
        break
    
    for i in range(m):
        solucao[i] = 0

    ngnResolveuTodos = True
    aoMenosUmProblema = True
    todoProblemaResolvido = True
    naoResolvidoPorTodos = True
    
    for i in range(n):
        matriz = input().split()
        
        qtdeResolvidosTime = 0
        for j in range(m):
            if matriz[j] == '1':
                qtdeResolvidosTime += 1
                solucao[j] += 1 
            
        if qtdeResolvidosTime == m:
            ngnResolveuTodos = False
        if qtdeResolvidosTime == 0: 
            aoMenosUmProblema = False
    

    for i in range(m):
        if solucao[i] == 0:
            todoProblemaResolvido = False
        if solucao[i] == n:
            naoResolvidoPorTodos = False
    
    criterios = 0
    if ngnResolveuTodos:
        criterios += 1
    if aoMenosUmProblema:
        criterios += 1
    if todoProblemaResolvido:
        criterios += 1
    if naoResolvidoPorTodos:
        criterios += 1
    
    print(criterios)
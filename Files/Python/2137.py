# -*- coding: utf-8 -*-

def ordena(livros):
    ordem = min(livros)
    livros.remove(ordem)
    return ordem

while True:
    try:
        livros = []
        ordenado = []

        n = int(input())
        
        for i in range(n):
            livros.append(int(input()))
        
        for i in range(len(livros)):
            ordenado.append(ordena(livros))
            
        for i in ordenado:
            verifica = str(i)
            if len(verifica) == 3:
                print("0%d"%(i))
            elif len(verifica) == 2:
                print("00%d"%(i))
            elif len(verifica) == 1:
                print("000%d"%(i))
            else:
                print(i)
        
    except EOFError:
        break
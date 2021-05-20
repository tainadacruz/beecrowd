# -*- coding: utf-8 -*-
#URI 2803 - Estados do Norte

estado = input() #entrada com o nome do estado
estado = str(estado) #definindo o tipo da variável

#se o estado for pertencente a região norte, a saída mostrará isso
if estado == "roraima" or estado == "acre" or estado == "amapa" or estado == "amazonas" or estado == "para" or estado == "tocantins" or estado == "rondonia":
    print("Regiao Norte")
else:#se não, mostrará que é de outra região
    print("Outra regiao")
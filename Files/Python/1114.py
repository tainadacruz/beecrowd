# -*- coding: utf-8 -*-

val = 1

while val != 0:
    senha = int(input())
    if (senha == 2002):
        val = 0
        print("Acesso Permitido")
    else:
        print("Senha Invalida")
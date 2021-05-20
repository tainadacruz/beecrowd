# -*- coding: utf-8 -*-

a1 = input()
a2 = input()
a3 = input()

if a1 == "vertebrado":
    if a2 == "ave":
        if a3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if a3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if a2 == "inseto":
        if a3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if a3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
                
# -*- coding: utf-8 -*-

n = int(input())
dic = {"EPR" : 0, "EHD" : 0, "INTRUSOS" : 0}

for i in range(n):
    num, sigla = input().split()
    
    if sigla != "EPR" and sigla != "EHD":
        dic["INTRUSOS"] += 1
    else:
        dic[sigla] += 1

print("EPR: %d"% dic["EPR"])
print("EHD: %d"% dic["EHD"])    
print("INTRUSOS: %d"% dic["INTRUSOS"])
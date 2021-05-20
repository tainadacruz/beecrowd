# -*- coding: utf-8 -*-

i,n = [int(x) for x in input().split()]

saldoD = i
saldoE = i
saldoF = i

entrada = []*4

for a in range(n):
    entrada.append(input().split())
    entrada = list(entrada[0])
    
    if entrada[0] == "A":
        entrada[3] = int(entrada[3])
    else:
        entrada[2] = int(entrada[2])

    if entrada[1] == "D":
        if entrada[0] == "C":
            saldoD -= entrada[2]
        elif entrada[0] == "V":
            saldoD += entrada[2]
        else:
            saldoD += entrada[3]
            if entrada[2] == "E":
                saldoE -= entrada[3]
            else:
                saldoF -= entrada[3]
    elif entrada[1] == "E":
        if entrada[0] == "C":
            saldoE -= entrada[2]
        elif entrada[0] == "V":
            saldoE += entrada[2]
        else:
            saldoE += entrada[3]
            if entrada[2] == "D":
                saldoD -= entrada[3]
            else:
                saldoF -= entrada[3]
    elif entrada[1] == "F":
        if entrada[0] == "C":
            saldoF -= entrada[2]
        elif entrada[0] == "V":
            saldoF += entrada[2]
        else:
            saldoF += entrada[3]
            if entrada[2] == "E":
                saldoE -= entrada[3]
            else:
                saldoD -= entrada[3]
                
    entrada.clear()
            
print("%d %d %d"%(saldoD,saldoE,saldoF))
# -*- coding: utf-8 -*-

while True:
    try:
        hh = []
        mm = []
        
        ledH = ["  "]*6
        ledM = ["  "]*8
 
        horario = input()
        horario = list(horario)
        
        hh.append(horario[0])
        hh.append(horario[1])
        mm.append(horario[3])
        mm.append(horario[4])
        
        hh = ["".join(hh)]
        mm = ["".join(mm)]
        
        for a in range(len(hh)):
            hh[a] = int(hh[a])
        for b in range(len(mm)):
            mm[b] = int(mm[b])
        
        binHH = list(bin(hh[0]))
        binMM = list(bin(mm[0]))
        
        
        for x in range(2,len(binHH)):
            if binHH[x] == "1":
                ledH[x] = "o"
            else:
                ledH[x] = " "

        for y in range(2,len(binMM)):
            if binMM[y] == "1":
                ledM[y] = "o"
            else:
                ledM[y] = "  "
                
        if len(binMM) < 8:
            for k in range(8-len(binMM)):
                ledM.insert(0,"  ")
        
        if len(binHH) < 6:
            for k in range(6-len(binHH)):
                ledH.insert(0,"  ")     
        

        print(" ____________________________________________")
        print("|                                            |")
        print("|    ____________________________________    |_")
        print("|   |                                    |   |_)")
        print("|   |   8         4         2         1  |   |")
        print("|   |                                    |   |")
        print("|   |  %s         %s         %s         %s  |   |"%(ledH[2],ledH[3],ledH[4],ledH[5]))
        print("|   |                                    |   |")
        print("|   |                                    |   |")
        print("|   |   %s    %s   %s    %s    %s    %s  |   | "%(ledM[2],ledM[3],ledM[4],ledM[5],ledM[6],ledM[7]))
        print("|   |                                    |   |")
        print("|   |   32    16    8     4     2     1  |   |_")
        print("|   |____________________________________|   |_)")
        print("|                                            |")
        print("|____________________________________________|")
        print("")     
        
    except EOFError:
        break
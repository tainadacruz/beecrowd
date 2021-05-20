# -*- coding: utf-8 -*-

Cv,Ce,Cs,Fv,Fe,Fs = input().split()
Cv = int(Cv)
Ce = int(Ce)
Cs = int(Cs)
Fv = int(Fv)
Fe = int(Fe)
Fs = int(Fs)

if (Cv*3 + Ce) == (Fv*3 + Fe):
    if Cs == Fs:
        print("=")
    elif Cs > Fs:
        print("C")
    else:
        print("F")
elif (Cv*3 + Ce) > (Fv*3 + Fe):
    print("C")
else:
    print("F")


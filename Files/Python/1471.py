# -*- coding: utf-8 -*-

while True:
    try:
        n,r = [int(x) for x in input().split()]
        mergulhou = []
        
        for i in range(1,n+1):
            mergulhou.append(i)
            
        r = [int(x) for x in input().split()]
        
        for j in r:
            mergulhou.remove(j)
        
        if not mergulhou:
            print("*",end="")
        else:
            for k in range(len(mergulhou)):
                print("%d "%(mergulhou[k]),end=" ")
        print("")

    except EOFError:
        break
# -*- coding: utf-8 -*-

while True:
    d,n = [str(x) for x in input().split()] 
    if d == "0" and n == "0":
        break
    
    count = 0
    n = list(n)
    result = []
    resultFinal = []
    
    for i in n:
        if i != d:
            result.append(int(i))
            
    for i in result:
        if count == 0:
            if i != 0:
                resultFinal.append(i)
                count += 1
        else:
            resultFinal.append(i)
            count += 1
        
    if sum(resultFinal) == 0:
        print("0")
    else:
        for i in range(len(resultFinal)):
            resultFinal[i] = str(resultFinal[i])
            
        resultFinal = [''.join(resultFinal)]
        print(resultFinal[0])
n,m = [int(x) for x in input().split()]
aux = 0
ok = True
bo = True

numeros = [None] * n
for i in range(n):
    numeros[i] = [int(m) for m in input().split()]
    
for i in range(n):
    zeros = 0
    bo = True
    for j in range(m):
        if (numeros[i][j] == 0 or bo):
            zeros += 1
        else:
            bo = False
            
        if (numeros[i] != 0):
            if((zeros > aux or (zeros == aux and zeros == m)) or ok):
                aux = zeros
            else:
                aux = 0
                ok = False
        else:
            aux = zeros

if(aux > 0):
    print("S")
else:
    print("N")

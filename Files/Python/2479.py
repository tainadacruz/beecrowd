# -*- coding: utf-8 -*-

comportada = 0
notComportada = 0

n = int(input())
ordem = [None]*n

for i in range(n):
    kid = str(input())
    kid = list(kid)
    
    if kid[0] == "+":
        comportada += 1
        kid.remove("+")
        kid.remove(" ")
    else:
        notComportada += 1
        kid.remove("-")
        kid.remove(" ")
        
    ordem[i] = "".join(kid)

for i in sorted(ordem):
    print(i)

print("Se comportaram: %d | Nao se comportaram: %d"%(comportada,notComportada))
    

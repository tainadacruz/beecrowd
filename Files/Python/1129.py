# -*- coding: utf-8 -*-

while True:
    n = int(input())
    
    if n == 0:
        break

    for i in range(n):
        q = [int(n) for n in input().split()]
        
        if q[0] <= 127 and q[1] > 127 and q[2] > 127 and q[3] > 127 and q[4] > 127:
            print("A")
        elif q[0] > 127 and q[1] <= 127 and q[2] > 127 and q[3] > 127 and q[4] > 127:
            print("B")
        elif q[0] > 127 and q[1] > 127 and q[2] <= 127 and q[3] > 127 and q[4] > 127:
            print("C")
        elif q[0] > 127 and q[1] > 127 and q[2] > 127 and q[3] <= 127 and q[4] > 127:
            print("D")
        elif q[0] > 127 and q[1] > 127 and q[2] > 127 and q[3] > 127 and q[4] <= 127:
            print("E")
        else:
            print("*")

# -*- coding: utf-8 -*-

a,b,c = [int(i) for i in input().split()]
h,l = [int(i) for i in input().split()]

if l >= b and h >= a:
    print("S")    
elif l >= c and h >= a:
    print("S")
elif l >= a and h >= b:
    print("S")    
elif l >= c and h >= b:
    print("S")   
elif l >= a and h >= c:
    print("S")
elif l >= b and h >= c:
    print("S")
else:
    print("N")
    
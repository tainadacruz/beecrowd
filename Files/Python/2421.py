# -*- coding: utf-8 -*-

x,y = [int(a) for a in input().split()]

l1,h1 = [int(b) for b in input().split()]
l2,h2 = [int(c) for c in input().split()]

if ((l1+h2) <= x) and (max(l2,h1) <= y):
    print("S")
elif ((h1+l2) <= x) and (max(l1,h2) <= y): 
    print("S")
elif (((l1+l2) <= x) and (max(h1,h2) <= y)):
    print("S")
elif (((h1+h2) <= x) and (max(l1,l2) <= y)):
    print("S")
else:
    print("N")
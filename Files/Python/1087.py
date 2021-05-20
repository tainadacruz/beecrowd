# -*- coding: utf-8 -*-

while True:
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    
    if (x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0):
        break
    
    if (x1 == x2 and y1 == y2):
        print("0\n")
    elif((x2-x1) == (y2-y1) or -(x2-x1) == -(y2-y1) or -(x2-x1) == (y2-y1) or (x2-x1) == -(y2-y1)):
        print("1\n")
    elif (x1 == x2 or y1 == y2):
        print("1\n")
    else:
        print("2\n")
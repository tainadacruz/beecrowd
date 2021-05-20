# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    led = 0
    v = list(input())
    
    for i in v:
        if i == "1":
            led += 2
        elif i == "2" or i == "3" or i == "5":
            led += 5
        elif i == "4":
            led += 4
        elif i == "6" or i == "9" or i == "0":
            led += 6
        elif i == "7":
            led += 3
        elif i == "8":
            led += 7
            
    print("%d leds"%(led))
            

# -*- coding: utf-8 -*-

s = str(input())
quant = 0

for i in range(0, len(s)):
    if s[i] == "1":
        quant += 1

if quant%2 == 0:
    print(s + "0")
else:
    print(s + "1")
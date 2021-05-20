# -*- coding: utf-8 -*-
from fractions import Fraction

a,b,c,d = [int(x) for x in input().split()]

print(Fraction(a,b))
print(Fraction(c,d))
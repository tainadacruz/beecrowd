# -*- coding: utf-8 -*-

while True:
  try:
    a,b,c = [int(i) for i in input().split()]
    if (a == b == c):
        print("*")
    elif (b == c):
        print("A")
    elif (a == c):
        print("B")
    else:
        print("C")
  except (EOFError):
    break
# -*- coding: utf-8 -*-

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
if((A + B == C) or (A + C == B) or (C + B == A)):
  area = (C * (A + B))/2
  print("Area = {}".format(area))
else:
  perimetro = A + B + C
  print("Perimetro = {}".format(perimetro))

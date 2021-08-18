# -*- coding: utf-8 -*-

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
lista = []
lista.append([A, B, C])
lista[0].sort(reverse=True)

A, B, C = lista[0]

#se A ≥ B+C
if(A >= B + C):
  print("NAO FORMA TRIANGULO")
else:
  #se A2 > B2 + C2
  if(A**2 > B**2 + C**2):
    print("TRIANGULO OBTUSANGULO")
  #se A2 < B2 + C2
  elif(A**2 < B**2 + C**2):
    print("TRIANGULO ACUTANGULO")
  #se A2 = B2 + C2
  if(A**2 == B**2 + C**2):
    print("TRIANGULO RETANGULO")
  if(A == B == C):
    print("TRIANGULO EQUILATERO")
  elif(A == B or A == C or B == C):
    print("TRIANGULO ISOSCELES")

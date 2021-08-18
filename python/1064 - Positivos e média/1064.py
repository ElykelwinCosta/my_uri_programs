# -*- coding: utf-8 -*-

cont = 0
soma = 0
for k in range(6):
  x = float(input())
  if(x >= 0):
    cont += 1
    soma += x

print("{} valores positivos".format(cont))
print("{:.1f}".format(soma / cont))

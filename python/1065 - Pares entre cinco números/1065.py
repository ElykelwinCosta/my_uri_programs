# -*- coding: utf-8 -*-

cont = 0
for k in range(5):
  if(int(input()) % 2 == 0):
    cont += 1

print("{} valores pares".format(cont))

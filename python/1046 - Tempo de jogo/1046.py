# -*- coding: utf-8 -*-

I, F = input().split()
I, F = int(I), int(F)
if(F > I):
  print("O JOGO DUROU {} HORA(S)".format(F - I))
elif(F == I):
  print("O JOGO DUROU {} HORA(S)".format(24))
else:
  print("O JOGO DUROU {} HORA(S)".format(24 - I + F))

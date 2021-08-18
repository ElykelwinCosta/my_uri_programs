# -*- coding: utf-8 -*-

valorInicial = int(input())
valor = valorInicial
c100 = 0
c50 = 0
c20 = 0
c10 = 0 
c5 = 0
c2 = 0
c1 = 0
#Decomposição
while(valor > 0):
  if(valor >= 100):
    c100 += 1
    valor -= 100
    continue
  elif(valor >= 50):
    c50 += 1
    valor -= 50
    continue
  elif(valor >= 20):
    c20 += 1
    valor -= 20
    continue
  elif(valor >= 10):
    c10 += 1
    valor -= 10
    continue
  elif(valor >= 5):
    c5 += 1
    valor -= 5
    continue
  elif(valor >= 2):
    c2 += 1
    valor -= 2
    continue
  elif(valor >= 1):
    c1 += 1
    valor -= 1
    continue
print(valorInicial)
print(c100 ,"nota(s) de R$ 100,00")
print(c50 ,"nota(s) de R$ 50,00")
print(c20 ,"nota(s) de R$ 20,00")
print(c10 ,"nota(s) de R$ 10,00")
print(c5 ,"nota(s) de R$ 5,00")
print(c2 ,"nota(s) de R$ 2,00")
print(c1 ,"nota(s) de R$ 1,00")

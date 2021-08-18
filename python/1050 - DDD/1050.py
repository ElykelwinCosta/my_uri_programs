# -*- coding: utf-8 -*-

lista = {61 : "Brasilia", 71 : "Salvador", 11 : "Sao Paulo",
         21 : "Rio de Janeiro", 32 : "Juiz de Fora", 19 : "Campinas",
         27 : "Vitoria", 31 : "Belo Horizonte"}

ddd = int(input())

if(ddd not in lista):
  print("DDD nao cadastrado")

for k in lista:
  if(k == ddd):
    print(lista[k])


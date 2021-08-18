# -*- coding: utf-8 -*-

entrada = input().split()
v1 = int(entrada[0])
v2 = int(entrada[1])
v3 = int(entrada[2])

lista = []
lista.append([v1, v2, v3])
lista[0].sort()
lista[0].append("\n".rstrip())

for k in lista[0]:
  print(k)
  
for k in entrada:
  print(k)


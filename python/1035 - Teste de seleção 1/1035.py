# -*- coding: utf-8 -*-

entrada = input()
numeros = entrada.split()
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
d = int(numeros[3])
aceito = False
if(b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0):
  print("Valores aceitos")
else:
  print("Valores nao aceitos")

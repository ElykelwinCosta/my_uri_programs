# -*- coding: utf-8 -*-

p1 = input()
p2 = input()
x = p1.split()
y = p2.split()
x1 = float(x[0])
y1 = float(x[1])
x2 = float(y[0])
y2 = float(y[1])
distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print("%.4f" %distancia)

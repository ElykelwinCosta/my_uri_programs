# -*- coding: utf-8 -*-

cord = input().split()
c1 = float(cord[0])
c2 = float(cord[1])

if(c1 == 0 and c2 == 0):
    print("Origem")
elif(c2 == 0):
    print("Eixo X")
elif(c1 == 0):
    print("Eixo Y")
elif(c1 > 0 and c2 > 0):
    print("Q1")
elif(c1 < 0 and c2 > 0):
    print("Q2")
elif(c1 < 0 and c2 < 0):
    print("Q3")
elif(c1 > 0 and c2 < 0):
    print("Q4")

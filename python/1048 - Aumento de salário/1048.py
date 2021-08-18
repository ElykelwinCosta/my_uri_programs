# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
P1 = 0.15; P2 = 0.12; P3 = 0.1; P4 = 0.07; P5 = 0.04

salario = float(input())
novoSalario = 0
reajuste = 0
percentual = 0

if(salario <= 400.00):
  reajuste = salario * P1
  novoSalario = salario + reajuste
  percentual = "{} %".format(int(P1 * 100))

elif(400.00 < salario <= 800.00):
  reajuste = salario * P2
  novoSalario = salario + reajuste
  percentual = "{} %".format(int(P2 * 100))

elif(800.00 < salario <= 1200.00):
  reajuste = salario * P3
  novoSalario = salario + reajuste
  percentual = "{} %".format(int(P3 * 100))

elif(1200.00 < salario <= 2000.00):
  reajuste = salario * P4
  novoSalario = salario + reajuste
  percentual = "{} %".format(int(P4 * 100))

elif(salario > 2000.00):
  reajuste = salario * P5
  novoSalario = salario + reajuste
  percentual = "{} %".format(int(P5 * 100))


print("Novo salario: {:.2f}".format(novoSalario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {}".format(percentual))

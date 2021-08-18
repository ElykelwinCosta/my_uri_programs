# -*- coding: utf-8 -*-

valor = float(input())

n100 = valor // 100
valor -= n100*100

n50 = valor // 50
valor -= n50*50

n20 = valor // 20
valor -= n20*20

n10 = valor // 10
valor -= n10*10

n5 = valor // 5
valor -= n5*5

n2 = valor // 2
valor -= n2*2

m1 = valor // 1
valor -= m1*1
#m1 = float("%.2f"%m1)
valor = float("%.2f" %valor)
m1 = float("%.2f" %m1)

m050 = valor // 0.5
valor -= m050*0.5
valor = float("%.2f" %valor)
m050 = float("%.2f" %m050)

m025 = valor // 0.25
valor -= m025*0.25
valor = float("%.2f" %valor)
m025 = float("%.2f" %m025)

m010 = valor // 0.1
valor -= m010*0.1
valor = float("%.2f" %valor)
m010 = float("%.2f" %m010)

m005 = valor // 0.05
valor -= m005*0.05
valor = float("%.2f" %valor)
m005 = float("%.2f" %m005)

m001 = valor*100
valor = float("%.2f" %valor)
m001 = float("%.2f" %m001)

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(n100)))
print("{} nota(s) de R$ 50.00".format(int(n50)))
print("{} nota(s) de R$ 20.00".format(int(n20)))
print("{} nota(s) de R$ 10.00".format(int(n10)))
print("{} nota(s) de R$ 5.00".format(int(n5)))
print("{} nota(s) de R$ 2.00".format(int(n2)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(m1)))
print("{} moeda(s) de R$ 0.50".format(int(m050)))
print("{} moeda(s) de R$ 0.25".format(int(m025)))
print("{} moeda(s) de R$ 0.10".format(int(m010)))
print("{} moeda(s) de R$ 0.05".format(int(m005)))
print("{} moeda(s) de R$ 0.01".format(int(m001)))

# -*- coding: utf-8 -*-

nums = input()
num = nums.split()
a = int(num[0])
b = int(num[1])
c = int(num[2])
maiorAB = (a + b + abs(a - b))/2
maiorTodos = int((maiorAB + c + abs(maiorAB - c))/2)
print(maiorTodos, "eh o maior")

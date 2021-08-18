lista = []
C = int(input())
for k in range(C):
    x = int(input())
    lista.append(x)

for i in lista:
    if(i % 2 == 0):
        print("0")
    else:
        print("1")


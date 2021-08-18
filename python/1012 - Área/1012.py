linhaLida = input()
lista = linhaLida.split()
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])
areaTriangulo = A * C / 2
areaCirculo = 3.14159 * C * C
areaTrapezio = (A + B) * C / 2
areaQuadrado = B * B
areaRetangulo = A * B
print("TRIANGULO: %.3F" %areaTriangulo)
print("CIRCULO: %.3F" %areaCirculo)
print("TRAPEZIO: %.3F" %areaTrapezio)
print("QUADRADO: %.3F" %areaQuadrado)
print("RETANGULO: %.3F" %areaRetangulo)

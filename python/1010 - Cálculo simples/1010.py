readLine = input()
itemRead = readLine.split()
codeProd = int(itemRead[0])
qtdeProd = int(itemRead[1])
pricProd = float(itemRead[2])
totalPric1 = qtdeProd * pricProd
readLine2 = input()
itemRead2 = readLine2.split()
codeProd2 = int(itemRead2[0])
qtdeProd2 = int(itemRead2[1])
pricProd2 = float(itemRead2[2])
totalPric2 = qtdeProd2 * pricProd2
finalPric = totalPric1 + totalPric2
print("VALOR A PAGAR: R$ %.2f"%finalPric)

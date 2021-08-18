entry = input()
entryN = entry.split()
X = int(entryN[0])
Y = int(entryN[1])
price = 0
if (X == 1):
  price = (Y * 4)
elif (X == 2):
  price = (Y * 4.50)
elif (X == 3):
  price = (Y * 5.00)
elif (X == 4):
  price = (Y * 2.00)
elif (X == 5):
  price = (Y * 1.50)
print("Total: R$ %.2f"%price)

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
par = 0
imp = 0
pos = 0
neg = 0
for n in (A,B,C,D,E):
  if n % 2 ==0:
    par = par + 1
  else:
    imp = imp + 1
  if n > 0:
    pos = pos + 1
  if n < 0:
    neg = neg + 1
print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %imp)
print("%d valor(es) positivo(s)" %pos)
print("%d valor(es) negativo(s)" %neg)

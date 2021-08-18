dias = int(input())
qtdeAnos = dias // 365
qtdeMeses = (dias % 365) // 30
qtdeDias = (dias % 365) % 30
print("%d ano(s)" %qtdeAnos)
print("%d mes(es)" %qtdeMeses)
print("%d dia(s)" %qtdeDias)

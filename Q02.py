qtd = int(input("Dgite a quantidade de maçãs: "))
if qtd < 12:
  valor = qtd*0.3
else:
  valor = qtd*0.25
print(qtd, " maçãs custam R$",valor)
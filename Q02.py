# Cálcular o preço da maça baseado na quantidade de maçãs compradas

qtd = int(input("Digite a quantidade de maçăs: "))
if qtd < 12:
  valor = qtd*0.3
else:
  valor = qtd*0.25
print(qtd, " maçăs custam R$",valor)

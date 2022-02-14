qtd = int(input("Digite a quantidade de numeros a serem cadastrados:"))
contatos = []
numeros = []
for i in range(qtd):
  contatos.append(input("\nNome:"))
  numeros.append(input("Telefone:"))
while True:
  consulta = input("\nQual nome que você deseja consultar o telefone?")
  if consulta in contatos:
    a = contatos.index(consulta)
    print("Número:",numeros[a])
  else:
    print("Nome não cadastrado")
  x = int(input("\nDeseja pesquisar outro número?\n1-Sim\n2-Não\n"))
  if x == 2:
    break
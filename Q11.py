entrada1 = input("Digite a primeira lista ordenada, separando por espaço: ")
entrada2 = input("Digite a segunda lista ordenada, separando por espaço: ")
lista_1 = entrada1.split(" ")
lista_2 = entrada2.split(" ")
nova_lista = []
while True:
  if len(lista_1)!=0 and len(lista_2)!=0:
    if lista_1[0] >= lista_2[0]:
      nova_lista.append(lista_2[0])
      del lista_2[0]
    else:
      nova_lista.append(lista_1[0])
      del lista_1[0]
  else:
    for i in lista_1 or lista_2:
      nova_lista.append(i)
    break
print(nova_lista) 
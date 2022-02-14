lista_1 = []
print("Digite para a lista 1")
for i in range(10):
  lista_1.append(int(input("Digite:")))
lista_2 = []
print("Digite para a lista 2")
for i in range(10):
  lista_2.append(int(input("Digite:")))
multip = []
print("Resultado")
for i in range(10):
  multip.append(lista_1[i]*lista_2[i])
print(multip)
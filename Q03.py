lista = []
while True:
  num = int(input("Digite um número: "))
  if num==0:
    break
  lista.append(num)
soma = 0
for i in lista:
  soma = soma + i
media=soma/len(lista)
print("\nA média é:",media)
cont=0
for i in lista:
  if i > media:
    cont=cont+1
if cont==1:
  print("\nExiste",cont,"número acima da média.")
else:
    print("\nExistem",cont,"números acima da média.")
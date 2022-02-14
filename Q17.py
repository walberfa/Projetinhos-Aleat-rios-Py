c = int(input("Qual a capacidade da cabine?"))
a = int(input("Quantos alunos?"))
x = a//(c-1)
y = a%(c-1)
if y == 0:
  v = x
else:
  v = x + 1
print("São necessárias",v,"viagens")

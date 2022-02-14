palavra = input("Digite uma mensagem: ")
L1 = input("Digite qual letra deve ser trocada: ")
L2 = input("Digite por qual letra você quer trocar: ")
nova = ""
for i in palavra:
  if i == L1:
    nova=nova+L2
  else:
    nova=nova+i
print("Mensagem trocada: ",nova)
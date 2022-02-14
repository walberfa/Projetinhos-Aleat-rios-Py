palavra = input("Digite uma mensagem: ")
vogais = ["A","E","I","O","U","a","e","i","o","u"]
cont = 0
nova = ""
c = input("Digite o caractere de troca: ")
for i in palavra:
  if i in vogais:
    nova=nova+c
    cont=cont+1
  else:
    nova=nova+i
print("A mensagem tinha ",cont," vogais.")
print("Mensagem trocada: ",nova)
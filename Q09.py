entrada = input ("Digite uma mensagem: ")
vogais = ["A","E","I","O","U","a","e","i","o","u"]
nova = ""
for i in entrada:
	if i not in vogais:
		nova = nova+i
print("Mensagem sem vogais: ",nova)
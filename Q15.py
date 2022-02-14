i=0
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
p1 = palavra1.lower()
p2 = palavra2.lower()
if len(palavra1) <= len(palavra2):
  letras = len(palavra1)
else:
  letras = len(palavra2)
while i < letras:
  cod_p1 = ord(palavra1[i])
  cod_p2 = ord(palavra2[i])
  if cod_p1 < cod_p2:
    print("A palavra",palavra1,"vem primeiro na ordem alfabética")
    break
  elif cod_p1 > cod_p2:
    print("A palavra",palavra2,"vem primeiro na ordem alfabética ")
    break
  else:
    i = i+1
while i == letras:
  if len(palavra1) <= len(palavra2):
    print("A palavra",palavra1,"vem primeiro na ordem alfabética")
    break
  else:
    print("A palavra",palavra2,"vem primeiro na ordem alfabética")
    break

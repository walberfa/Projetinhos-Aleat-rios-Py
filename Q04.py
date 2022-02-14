print("Digite os angulos de um triangulo:")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
t = a+b+c
if t!=180:
  print("Você digitou ângulos inválidos.")
else:
  if a==90 or b==90 or c==90:
    print("O triângulo é retângulo.")
  elif a>90 or b>90 or c>90:
    print("O triângulo é obtusângulo")
  else:
    print("O triângulo é acutângulo")
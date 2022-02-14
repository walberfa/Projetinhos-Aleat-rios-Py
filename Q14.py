sexo = []
altura = []
a = 1
soma_alt = 0
maior = 0
menor = 3
qtd_mulheres = 0
soma_alt_mulh = 0
media = 0
media_mulh = 0
for i in range(12):
  print("\nAluno numero",a)
  a = a+1
  entrada_s = int(input("Digite o sexo:\n1-Homens\n2-Mulheres\n"))
  sexo.append(entrada_s)
  entrada_a = float(input("Digite a altura:"))
  altura.append(entrada_a)
  soma_alt = soma_alt + entrada_a
  if entrada_a > maior:
    maior = entrada_a
  if entrada_a < menor:
    menor = entrada_a
  if entrada_s == 2:
    qtd_mulheres = qtd_mulheres + 1
    soma_alt_mulh = soma_alt_mulh + entrada_a
media = soma_alt/(a-1)
media_mulh = soma_alt_mulh/qtd_mulheres
print("\nMaior altura:",maior)
print("Menor altura:",menor)
print("\nMulheres com altura acima da média de altura das mulheres: ")
for i in range(12):
  if sexo[i] == 2 and altura[i] > media_mulh:
    print("Aluna",i+1,"com altura",altura[i])
print("\nHomens com altura abaixo da média de altura das mulheres: ")
for i in range(12):
  if sexo[i] == 1 and altura[i] < media_mulh:
    print("Aluno",i+1,"com altura",altura[i])
print("\nPessoas com altura abaixo da média da turma:")
for i in range(12):
  if altura[i] < media:
    print("Aluno",i+1,"com altura",altura[i])
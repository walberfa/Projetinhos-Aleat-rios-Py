n = int(input("Digite um número inteiro (1<=N<=500): "))
maior = n
while n > 1:
  if n%2 == 0:
    n = n//2
  else:
    n = 3*n+1
  if n > maior:
    maior = n
print("Maior valor da sequencia:",maior)
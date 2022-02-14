import random
sorteio = []
for i in range(13): 
  numero = random.randint(1,100) 
  if numero not in sorteio: 
    sorteio.append(numero)
sorteio.sort()
while True:
  aposta = []
  cartao = int(input("Digite o número do cartão do apostador: "))
  acertos = 0
  while len(aposta) < 13: 
    n = int(input("Digite:"))
    if n not in aposta:
      aposta.append(n)
      if n in sorteio:
        acertos = acertos + 1
  if acertos != 13:
    print("O cartão",cartao,"acertou",acertos,"números.")
  else:
    print("GANHADOR")
    print("O cartão",cartao,"acertou",acertos,"números.")
    break

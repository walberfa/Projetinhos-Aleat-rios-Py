#Atividade da disciplina de Fundamentos da Programação, S1 do curso de Ciência da Computação

#ENTRADA DE DADOS
nome = input("Digite o nome do(a) servidor(a):")
cargo = input("Digite qual o cargo:")
SBI = float(input("Qual o salário base inicial?"))
dep = int(input("Entre com o número de dependentes:"))
anos_s = int(input("Quantos anos em serviço?")) #Tempo de serviço como servidor(a)
chefia = int(input("Exerce cargo de chefia atualmente? Para SIM, digite 1. Para NÃO, digite 2:"))
if chefia == 1:
  GRAT = 0.1*SBI #GRAT é 10% do SBI (escolha do programador)
elif chefia == 2:
  chefiou = int(input("Já exerceu? Para SIM digite 1. Para NÃO, digite 2:"))
  if chefiou == 1:
    anos_c = int(input("Por quantos anos?")) #Tempo de serviço como chefia
    if anos_c<2:
      GRAT = 0
    elif anos_c>=2 and anos_c<4:
      GRAT = 0.02*SBI
    elif anos_c>=4 and anos_c<6:
      GRAT = 0.04*SBI
    elif anos_c>=6 and anos_c<8:
      GRAT = 0.06*SBI
    elif anos_c>=8 and anos_c<10:
      GRAT = 0.08*SBI
    elif anos_c>=10:
      GRAT = 0.1*SBI
  elif chefiou == 2:
    GRAT = 0
  else:
    print("Resposta inválida")
else:
  GRAT = 0
  print("Resposta inválida")
#PROCESSAMENTO DE DADOS
QUIN = ((anos_s//5)*5/100)*SBI
if anos_s>=20:
  SET_P = (SBI+GRAT+QUIN)/6
else:
  SET_P = 0
SBT = SBI+GRAT+QUIN+SET_P
IAMSP = 0.02*SBT
prev = 0.11*SBT
#IR é o calculo base pro imposto de renda
#dIR é o valor a ser deduzido do imposto
#vIR é o valor cobrado pelo imposto de renda
IR = SBT-IAMSP-prev-(150.69*dep)
if IR<1499.15:
  dIR = 0
  vIR = 0
  SL = (SBT-IAMSP-prev) - vIR
  total = SBT - SL
elif IR>=1499.15 and IR<2246.75:
  dIR = 112.43
  vIR = ((SBT-IAMSP-prev)*0.075)-dIR
  SL = (SBT-IAMSP-prev) - vIR
  total = SBT - SL
elif IR>=2246.75 and IR<2995.70:
  dIR = 280.94
  vIR = ((SBT-IAMSP-prev)*0.15)-dIR
  SL = (SBT-IAMSP-prev) - vIR
  total = SBT - SL
elif IR>=2995.70 and IR<37432.19:
  dIR = 505.62
  vIR = ((SBT-IAMSP-prev)*0.225)-dIR
  SL = (SBT-IAMSP-prev) - vIR
  total = SBT - SL
elif IR>=37432.19:
  dIR = 692.78
  vIR = ((SBT-IAMSP-prev)*0.275)-dIR
  SL = (SBT-IAMSP-prev)- vIR
  total = SBT - SL
#SAÍDAS DE DADOS
print ("EXTRATO")
print ("Nome:", nome)
print ("Cargo:", cargo)
print ("Vencimento:", SBI)
print ("Gratificação de representação:", GRAT)
print ("Adicional de tempo de serviço:", QUIN)
print ("Sexta Parte:", SET_P)
print ("Salário Bruto:", SBT)
print ("DESCONTOS:")
print ("Contribuição previdenciária:", prev)
print ("IAMSP:", IAMSP)
print ("Imposto de Renda:", vIR)
print ("Total de Descontos: ", total)
print ("Salário Líquido", SL)
